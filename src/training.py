"""A minimal PyTorch training loop, extracted in Session 9.

You write this loop by hand in Session 8 and again at the start of Session 9. Then we
refactor it here, once, and reuse it for Sessions 10 and 11 so that the interesting
part of those sessions is the *experiment* rather than the boilerplate.

Nothing here is magic, and that is the point: every line has a counterpart in the
loop you already wrote. If you cannot say what a line does, go back to Session 8 §6.

    from src.training import TabularDataset, fit, evaluate, EarlyStopping
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset


class TabularDataset(Dataset):
    """Wraps a dense feature matrix and a target vector as a torch Dataset.

    Targets are stored as a column, shape (n, 1), to match what a single-output
    network produces. Session 0c §7 explains why that detail is not cosmetic: an
    (n,) target against an (n,1) prediction broadcasts to (n,n) silently.
    """

    def __init__(self, X, y=None):
        self.X = torch.as_tensor(np.asarray(X, dtype=np.float32))
        self.y = None
        if y is not None:
            self.y = torch.as_tensor(
                np.asarray(y, dtype=np.float32)).reshape(-1, 1)

    def __len__(self) -> int:
        return len(self.X)

    def __getitem__(self, i):
        if self.y is None:
            return self.X[i]
        return self.X[i], self.y[i]


@dataclass
class EarlyStopping:
    """Stop when validation loss has not improved for `patience` epochs.

    Keeps a copy of the best weights, because the point of early stopping is to
    *use* the best model, not merely to stop training near it. Forgetting to
    restore is a common and silent mistake: you stop at the right time and then
    keep the overfitted parameters anyway.
    """

    patience: int = 10
    min_delta: float = 0.0
    best: float = float("inf")
    epochs_without_improvement: int = 0
    best_state: dict | None = field(default=None, repr=False)

    def step(self, val_loss: float, model: nn.Module) -> bool:
        """Record an epoch. Returns True when training should stop."""
        if val_loss < self.best - self.min_delta:
            self.best = val_loss
            self.epochs_without_improvement = 0
            self.best_state = {k: v.detach().clone()
                               for k, v in model.state_dict().items()}
            return False
        self.epochs_without_improvement += 1
        return self.epochs_without_improvement >= self.patience

    def restore(self, model: nn.Module) -> None:
        if self.best_state is not None:
            model.load_state_dict(self.best_state)


@torch.no_grad()
def evaluate(model, loader, loss_fn) -> tuple[float, np.ndarray]:
    """Mean loss and predicted logits over a loader, in eval mode.

    `model.eval()` matters: it switches dropout off and makes batch-norm use its
    running statistics. Omitting it is the single most common PyTorch bug, and it
    is silent - you simply get worse validation numbers than you should.
    `torch.no_grad()` skips building the autograd graph, which is faster and uses
    less memory.
    """
    model.eval()
    total, n_seen, outputs = 0.0, 0, []
    for batch in loader:
        xb, yb = batch
        logits = model(xb)
        total += loss_fn(logits, yb).item() * len(xb)
        n_seen += len(xb)
        outputs.append(logits.detach().cpu().numpy())
    return total / max(n_seen, 1), np.vstack(outputs)


def fit(
    model: nn.Module,
    train_loader: DataLoader,
    val_loader: DataLoader | None = None,
    *,
    epochs: int = 50,
    lr: float = 1e-3,
    weight_decay: float = 0.0,
    loss_fn: nn.Module | None = None,
    optimizer: torch.optim.Optimizer | None = None,
    early_stopping: EarlyStopping | None = None,
    seed: int | None = None,
    verbose: bool = False,
) -> dict[str, list[float]]:
    """Train `model`, returning the loss history.

    The five lines in the inner loop are exactly Session 8's:

        optimizer.zero_grad()   # gradients accumulate; clear them
        logits = model(xb)      # forward
        loss = loss_fn(...)     # how wrong
        loss.backward()         # the chain rule
        optimizer.step()        # parameters -= lr * gradient

    Returns {"train": [...], "val": [...]} so the caller can plot both curves from
    epoch 1. Plotting validation only at the end hides every interesting failure.
    """
    if seed is not None:
        torch.manual_seed(seed)
    loss_fn = loss_fn or nn.BCEWithLogitsLoss()
    optimizer = optimizer or torch.optim.Adam(
        model.parameters(), lr=lr, weight_decay=weight_decay)

    history: dict[str, list[float]] = {"train": [], "val": []}

    for epoch in range(epochs):
        model.train()
        running, n_seen = 0.0, 0
        for xb, yb in train_loader:
            optimizer.zero_grad()
            loss = loss_fn(model(xb), yb)
            loss.backward()
            optimizer.step()
            running += loss.item() * len(xb)
            n_seen += len(xb)
        history["train"].append(running / max(n_seen, 1))

        if val_loader is not None:
            val_loss, _ = evaluate(model, val_loader, loss_fn)
            history["val"].append(val_loss)
            if verbose and (epoch % 10 == 0 or epoch == epochs - 1):
                print(f"    epoch {epoch:3d}  train {history['train'][-1]:.4f}  "
                      f"val {val_loss:.4f}")
            if early_stopping is not None and early_stopping.step(val_loss, model):
                if verbose:
                    print(f"    early stop at epoch {epoch} "
                          f"(best val {early_stopping.best:.4f})")
                early_stopping.restore(model)
                break
        elif verbose and epoch % 10 == 0:
            print(f"    epoch {epoch:3d}  train {history['train'][-1]:.4f}")

    return history


def make_mlp(n_inputs: int, hidden=(64, 32), dropout: float = 0.0,
             batch_norm: bool = False) -> nn.Sequential:
    """A plain MLP with one output logit.

    Written as a factory so Session 10's ablation can vary dropout and batch-norm
    without rewriting the architecture each time. Order within a block is
    Linear -> [BatchNorm] -> ReLU -> [Dropout], which is the common convention.
    """
    layers: list[nn.Module] = []
    previous = n_inputs
    for width in hidden:
        layers.append(nn.Linear(previous, width))
        if batch_norm:
            layers.append(nn.BatchNorm1d(width))
        layers.append(nn.ReLU())
        if dropout > 0:
            layers.append(nn.Dropout(dropout))
        previous = width
    layers.append(nn.Linear(previous, 1))
    return nn.Sequential(*layers)


def loaders_from_arrays(X_train, y_train, X_val=None, y_val=None, *,
                        batch_size: int = 256, seed: int = 42):
    """Build train/validation DataLoaders with a reproducible shuffle."""
    generator = torch.Generator().manual_seed(seed)
    train_loader = DataLoader(TabularDataset(X_train, y_train),
                              batch_size=batch_size, shuffle=True,
                              generator=generator, drop_last=False)
    val_loader = None
    if X_val is not None:
        val_loader = DataLoader(TabularDataset(X_val, y_val),
                                batch_size=1024, shuffle=False)
    return train_loader, val_loader
