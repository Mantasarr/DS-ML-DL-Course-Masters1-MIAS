# Longitudinal Project Brief - *Barcelona: Pricing and Compliance in the Short-Term Rental Market*

**Student-facing.** This is the single project running through all 12 sessions. You will not do twelve disconnected exercises; you will build one analysis, and at the end you will defend it.

---

## 1. The situation

Barcelona has the most contested short-term rental market in Europe. In 2024 the city announced it would phase out all licensed tourist apartments by 2028 - a policy with no precedent at this scale. Around that decision sit two organisations who want very different things from the same data.

**Client A - Direcció de Turisme, Ajuntament de Barcelona (the regulator).**
Enforcement capacity is finite: inspectors can visit a few hundred listings a month out of more than fifteen thousand. They want to know which listings are operating **without a valid tourist licence**, so inspections can be targeted rather than random. They also need to defend that targeting publicly - if the model concentrates enforcement in poorer districts, that is a political and legal problem, not merely a technical one.

**Client B - a property-management company operating in the city.**
They manage a growing portfolio and want a **pricing tool**: given a new apartment's characteristics, what should it be listed at? Their current process is a manager eyeballing three "comparable" listings.

You will work for **both**. They will not always want the same thing, and part of your job is noticing when.

---

## 2. The data

**Inside Airbnb, Barcelona, snapshot of 24 June 2026.** 15,293 listings × 90 columns, vendored in the repository at `data/raw/`.

Inside Airbnb is an activist project that scrapes public Airbnb listing pages to support housing-policy debate. That origin matters. The data was **not** collected for your purpose, has no documentation contract, and contains artifacts of how the scraper works. Part of the work - a real part, not a warm-up - is figuring out what each column actually measures.

Do **not** re-download the data. The snapshot is pinned. Inside Airbnb rotates snapshots quarterly and your results would stop being comparable to everyone else's.

### What is in it, broadly
- **Physical:** capacity, bedrooms, beds, bathrooms, property and room type
- **Geographic:** latitude/longitude, 69 neighbourhoods within 10 districts
- **Host:** identifier, tenure, portfolio size
- **Commercial:** price, availability, minimum stay, occupancy and revenue estimates
- **Reputation:** review counts and seven review score dimensions
- **Regulatory:** a `license` field
- **Text:** listing name, description, host bio, and a JSON list of amenities
- **Images:** photo URLs (optional extension only)

### Two warnings, given honestly
1. **Some columns are empty or constant.** Not a mistake in the file - the format changed. Find them; don't assume a column exists because it has a name.
2. **Some columns will make your model look excellent.** Be suspicious of good news. If a result surprises you pleasantly, that is a signal to investigate, not to celebrate. This will happen to you more than once, by design.

---

## 3. The two questions

### Q1 - Regression (Client B): what should a listing charge per night?
**Target:** nightly price.
You will have to decide what "the nightly price of a listing" actually means in this data before you can model it. That decision is part of the assessment, and it is not a formality - it changes the answer.

### Q2 - Classification (Client A): is this listing operating with a valid licence?
**Target:** derived by you from the `license` field.
The field is free text with several formats and a lot of missing values. Deriving a defensible binary target from it is the first real task, and reasonable people will derive slightly different targets. Document yours.

**Optional stretch:** predict occupancy. Harder than it looks - a third of listings sit at zero, and the most obviously useful features are contaminated.

---

## 4. What you will produce, session by session

| After | Milestone | What it is |
|---|---|---|
| S1 | **M0** | Dataset fact sheet + problem statement |
| S2 | **M1** | Cleaning pipeline + decision log + **sealed test set** |
| S3 | **M2** | Preprocessing pipeline + leakage audit |
| S4 | **M3** | Regression: baseline → linear → regularised |
| S5 | **M4** | Classification: three models + threshold recommendation |
| S6 | **M5** | Validated, tuned model with uncertainty intervals |
| S7 | **M6** | Ensemble champion + **Model Card v1** |
| S8 | **M7** | Neural network from scratch (NumPy) + PyTorch twin |
| S9 | **M8** | PyTorch MLP + honest comparison against M6 |
| S10 | **M9** | Regularisation ablation study |
| S11 | **M10** | Text + fusion model + **Final Model Card** |
| S12 | - | Report + defense |

Details and rubrics: [MILESTONES.md](MILESTONES.md).

---

## 5. The one rule

**You will split the data in Session 2 and you will not touch the test set again until Session 12, in class, in front of everyone.**

Not "try not to look at it". Not "avoid using it for tuning". You will write it to disk, and you will not read that file. Every honest number you report for eleven weeks will come from cross-validation on your training data.

In Session 12 you will state your expected performance out loud, and *then* the test set is opened. The gap between those two numbers is the most informative result you will produce all semester - and it is only informative if the seal held.

---

## 6. How this will be graded

Read this carefully, because it is not how most courses work.

**A high score does not earn you a high grade.** Raw model performance is capped at roughly 20% of any milestone rubric. The remaining 80% is: was the decision defensible, did you know why you made it, did you check the thing that would have proved you wrong, and can you explain the result to someone who does not know what R² is.

A student reporting **R² = 0.61 with a correct protocol and an honest account of its limits will outrank** a student reporting 0.87 who cannot explain where it came from. The second student, in this dataset, is almost certainly wrong - and part of what you are learning is how to tell.

You may not always beat a simple baseline by much. That is a real finding, and reporting it clearly is worth more than manufacturing an improvement.

---

## 7. Working arrangements

- **Milestones M1–M2:** assigned pairs. **M3 onward:** re-paired.
- **Final report and defense:** individual. You must be able to defend every choice in your own notebook.
- Discussion across pairs is encouraged. Copying notebooks is not; you will be asked to explain your code in the defense.
- Budget **~4 hours per week** outside class.

---

## 8. Ethics - not an appendix

This project has a real subject and real consequences, and you are expected to engage with them rather than note them in a closing paragraph.

- **The regulator's model targets people.** A false positive is an inspection of a compliant host - a cost imposed on someone who did nothing wrong. Ask who bears it.
- **Compliance is not uniformly distributed across the city.** When you find that pattern, you will have to decide what it means, and whether a model that exploits it is defensible. Geography carries income, and income carries other things.
- **The pricing model has an aggregate effect.** A tool that helps every operator price optimally does not leave the rental market unchanged. Whether that is your problem is a fair question - argue it.
- **The data describes identifiable people.** Host names and photos have been removed from the copy you receive. Consider whether the analysis you are doing is one the hosts would recognise as fair.

You will not be graded on reaching a particular ethical conclusion. You will be graded on whether you noticed the questions and reasoned about them.

---

## 9. Deliverables at the end

1. **Reproducible notebook(s)** - runs top to bottom on a fresh checkout, fixed seeds, pinned environment
2. **Report, max 6 pages** - problem, data, method, results with uncertainty, interpretation, limitations, recommendation to each client
3. **Final Model Card** - what it does, how well, for whom it fails, when not to use it
4. **Defense** - 12 minutes, 6 minutes of questions, sealed test opened live

---

## 10. Pitfalls, stated in advance

You have been warned about all of these. Being caught by one anyway is normal; being caught by one *and not noticing* is what costs marks.

- Cleaning or exploring before splitting
- Fitting any transformer on data that includes your validation fold
- Treating a suspiciously strong feature as good luck
- Reporting a difference smaller than your fold-to-fold spread
- Random K-fold on data with obvious group structure
- Comparing a tuned model against an untuned baseline
- Imputing a value that cannot exist
- Dropping rows without checking what they had in common
- Choosing 0.5 as a threshold because it is the default
- Presenting feature importance as causation
- Concluding "deep learning is better" or "deep learning is useless" without a controlled comparison
