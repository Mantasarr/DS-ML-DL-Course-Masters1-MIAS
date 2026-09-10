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

## What is here

| | Session | Notebooks |
|---|---|---|
| **Session 0** | Prerequisites | `notebooks/00a_environment_setup.ipynb`<br>`notebooks/00b_python_for_data_science.ipynb`<br>`notebooks/00c_numpy_essentials.ipynb`<br>`notebooks/00d_visualization_reference.ipynb`<br>`notebooks/00e_diagnostic_quiz.ipynb`<br>`notebooks/00f_remediation.ipynb` |
| **Session 1** | The Data Science Workflow & First Contact with Data | `notebooks/01_workflow_and_first_contact.ipynb` |
| **Session 2** | Data Quality, the Split-First Rule & Visual Reasoning | `notebooks/02_data_quality_and_visual_reasoning.ipynb` |
| **Session 3** | Feature Engineering, Pipelines & Data Leakage | `notebooks/03_features_pipelines_and_leakage.ipynb` |

- `slides/00_fundamentals_and_vocabulary.pptx` - **start here**: the ideas and the
  words the rest of the course assumes, with no prior machine learning needed
- `project/PROJECT_BRIEF.md` - the brief, the two clients, and the one rule
- `project/MILESTONES.md` - what each deliverable must contain, and how it is assessed
- `src/` - shared helpers the notebooks import
- `tools/check_setup.py` - the setup verifier

## Not here yet

Later sessions are published as we reach them - pull this repository again before each session:

- Session 4 - Regression, Baselines & Honest Error
- Session 5 - Classification & the Metric Problem
- Session 6 - Validation, Model Selection & Tuning
- Session 7 - Ensembles, Interpretation & Error Analysis
- Session 8 - From Linear Models to Neural Networks
- Session 9 - Training Neural Networks in Practice
- Session 10 - Generalization in Deep Learning
- Session 11 - Representation Learning
- Session 12 - Assessment & Defence

## Working in these notebooks

Cells marked `# TODO` are yours to complete; the notebook around them explains
what each one is for. Work in order - every session builds directly on the one
before, and several sessions depend on a file you created in an earlier one.

Keep `data/SEALED_TEST/` on your own machine and do not commit it. You create it
in Session 2 and you do not open it again until the final session.
