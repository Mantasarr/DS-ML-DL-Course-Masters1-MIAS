# Data Science, Machine Learning & Deep Learning

Course notebooks, the project brief, and the pinned dataset.

One dataset carries the whole course: a snapshot of the Barcelona short-term
rental market, 15,293 listings × 90 columns, vendored in `data/raw/`. **Do not
download a fresh copy** - Inside Airbnb rotates its snapshots, and every figure
in these notebooks is tied to this exact file.

## Setup

Do this before Session 1. It takes about fifteen minutes.

```bash
python -m venv .venv
.venv/Scripts/activate          # Windows
source .venv/bin/activate       # macOS / Linux
pip install -r requirements.txt
python tools/check_setup.py
```

`check_setup.py` prints every version it finds and loads the dataset. It exits
non-zero with specific instructions if anything is missing. **It must print
"Setup is good" before Session 1** - the library versions are pinned because
results move between releases, and yours need to match the ones in the notebooks.

If imports work in the terminal but fail inside JupyterLab, your notebook is
running a different Python. Put `import sys; print(sys.executable)` in the first
cell and compare it against the interpreter you installed into.


## Working in these notebooks

Cells marked `# TODO` are yours to complete; the notebook around them explains
what each one is for. Work in order - every session builds directly on the one
before, and several sessions depend on a file you created in an earlier one.

Keep `data/SEALED_TEST/` on your own machine and do not commit it. You create it
in Session 2 and you do not open it again until the final session.
