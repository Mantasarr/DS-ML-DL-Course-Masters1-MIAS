# Figures générées : cours et TD des séances 8 à 10

Produites par `tools/make_block3_fr_figures.py`. Ne pas modifier à la main :
relancer le script.

**Droits d'utilisation :** création originale pour ce cours (code et figures).
Même régime que le reste du dépôt ; aucune contrainte de tiers. Les figures qui
portent des mesures sont recalculées à partir des données du cours
(Inside Airbnb, Barcelone, instantané du 24 juin 2026, licence CC BY 4.0 d'Inside
Airbnb) et vérifiées contre les sorties des notebooks instructeurs.

| fichier | ce qu'elle montre | provenance des valeurs |
|---|---|---|
| `f01_xor.png` | XOR : logistic regression à 0,5 partout contre la frontière d'un réseau 2-4-1 | recalcul du TinyNet de S8 §5, loss finale vérifiée contre S8 |
| `f02_activations.png` | sigmoïde, tanh, ReLU, Leaky ReLU et leurs dérivées | analytique |
| `f03a_approximation.png` | sin approchée par 3, 6 et 12 unités ReLU (construction explicite) | analytique |
| `f03b_extrapolation.png` | la même approximation hors de la zone d'entraînement | analytique |
| `f04_reseau_fiche.png` | le réseau 2-2-1 de la fiche de S8, avec ses valeurs | sorties S8 §3, vérifiées |
| `f05_graphe_calcul.png` | computational graph de la fiche : forward pass et backward pass | sorties S8 §3 et §4 |
| `f06_taux_apprentissage.png` | courbes de loss pour cinq learning rates | recalcul de S8 §7, losses finales vérifiées |
| `f07_descente_echelle.png` | gradient descent sur une cuvette étirée contre ronde | analytique (quadratique) |
| `f08_optimiseurs.png` | trajectoires SGD, momentum, Adam sur un ravin | analytique (quadratique) |
| `f09_planification.png` | learning rate constant, par paliers, cosinus, warm-up | analytique |
| `f10_premiere_courbe.png` | première courbe de S9 : minimum de validation et patience | recalcul de S9 §3, minimum vérifié |
| `f11_trois_courbes.png` | les trois allures : underfitting, sain, cassé | recalcul de S9 §7 |
| `f12_gradient_evanescent.png` | norme du gradient par couche, sigmoïde contre ReLU | données du cours, fold 0 |
| `f13_plis_apparies.png` | AUC par fold, MLP contre HistGB | sorties S9 §8 |
| `f14_ablation.png` | ablation de S10 avec écarts-types et seuil 2 sigma | sorties S10 §4 |
| `f15_normalisation.png` | axes de normalisation : batch norm contre layer norm | schéma |
| `f16_carte_des_notions.png` | carte des liens entre prérequis, S8, S9 et S10 | schéma |
| `courbes_mystere.csv` | quatre historiques d'entraînement anonymisés (P, Q, R, S) pour le TD 4 | recalcul sur le fold 0 ; configurations dans ce script |
