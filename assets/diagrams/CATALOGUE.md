# Diagram library

Imported from `Cours ML/` by `tools/import_diagrams.py`. 172 files.

## Read this before using anything here

**Every file below is marked `publish: no`.** Not because it is known to be restricted, but because for almost none of it can authorship be established, and for some of it authorship can be established and it is not ours. Showing a diagram on a projector in a classroom and redistributing it in a public Git repository are different acts.

`tools/make_release.py` refuses to publish any path under `assets/diagrams/`, so nothing here can reach the student repository by accident. To publish one, establish the rights first, then add it to the release allow-list deliberately.

### What the `source` column means

| value | meaning |
|---|---|
| `islr` | An Introduction to Statistical Learning (Springer). Printed figure caption still visible in the image. |
| `pdsh` | Python Data Science Handbook (VanderPlas). Filename matches that book's figure convention. Prose is CC-BY-NC-ND. |
| `mglearn` | Introduction to Machine Learning with Python (Mueller & Guido). Filename matches that book's figure set. |
| `slide-capture` | Screen capture of someone else's slide. All of these are exactly 1020x574 px, and the module4_* files come from the Michigan 'Applied Machine Learning in Python' Coursera course cited in the source notebook. |
| `unknown` | No attribution and no identifying marks. Origin not established. |

### Totals

| source | files |
|---|---:|
| `islr` | 1 |
| `pdsh` | 13 |
| `mglearn` | 10 |
| `slide-capture` | 45 |
| `unknown` | 103 |
| **total** | **172** |

## Catalogue

### `clustering/`

| file | shows | source | publish |
|---|---|---|---|
| `agglomerative-steps.png` | Agglomerative merging, step by step | `mglearn` | no |
| `cluster-distances.png` | Linkage criteria: single, complete, average, ward | `mglearn` | no |
| `dbscan.png` | DBSCAN core, border and noise points | `slide-capture` | no |
| `expectation-maximization.png` | EM iterations on a Gaussian mixture | `pdsh` | no |
| `hierarchical-clusters.png` | A dendrogram beside the clusters it encodes | `mglearn` | no |
| `Iris.png` | The iris dataset, scattered | `slide-capture` | no |
| `kmeans-steps.png` | k-means iterations: assign, move centroids, repeat | `mglearn` | no |
| `Petal-sepal.jpg` | Which part of the flower each iris measurement refers to | `unknown` | no |

### `reference/cnn/`

| file | shows | source | publish |
|---|---|---|---|
| `cnn_channels.png` | Channels through a conv layer | `unknown` | no |
| `cnn_count.png` | Counting convolution parameters | `unknown` | no |
| `cnn_f1.png` | Learned filters, early layer | `unknown` | no |
| `cnn_f2.png` | Learned filters, middle layer | `unknown` | no |
| `cnn_f3.png` | Learned filters, deep layer | `unknown` | no |
| `cnn_fc_.png` | Fully connected head after convolutions | `unknown` | no |
| `cnn_final.png` | A full CNN architecture | `unknown` | no |
| `cnn_summary.png` | CNN architecture summary | `unknown` | no |
| `cnn_textures.png` | Textures a network responds to | `unknown` | no |
| `conv2d_no_padding.png` | A convolution sliding over an image, no padding | `unknown` | no |
| `conv2d_padding.gif` | Animated convolution with padding | `unknown` | no |
| `fc_after_conv.png` | Flatten then dense | `unknown` | no |
| `maxpool.png` | Max pooling | `unknown` | no |
| `maxpool_b.png` | Max pooling, worked | `unknown` | no |
| `padding.png` | Padding, static | `unknown` | no |
| `transfer_learning.JPG` | Transfer learning: frozen base, new head | `unknown` | no |
| `whole_cnn.png` | End to end CNN | `unknown` | no |

### `reference/naive_bayes/`

| file | shows | source | publish |
|---|---|---|---|
| `Bayes_theorem_visualisation.svg` | Bayes theorem as areas | `unknown` | no |
| `gaussian-NB.png` | Gaussian naive Bayes decision regions | `pdsh` | no |
| `NaiveBayes.jpg` | Naive Bayes worked example, panel 0 | `slide-capture` | no |
| `NaiveBayes2.jpg` | Naive Bayes worked example, panel 2 | `slide-capture` | no |
| `NaiveBayes3.jpg` | Naive Bayes worked example, panel 3 | `slide-capture` | no |
| `NaiveBayes4.jpg` | Naive Bayes worked example, panel 4 | `slide-capture` | no |
| `NaiveBayes5.jpg` | Naive Bayes worked example, panel 5 | `slide-capture` | no |
| `NaiveBayes6.jpg` | Naive Bayes worked example, panel 6 | `slide-capture` | no |
| `NaiveBayes7.jpg` | Naive Bayes worked example, panel 7 | `slide-capture` | no |

### `reference/rnn/`

| file | shows | source | publish |
|---|---|---|---|
| `rnn_activation.png` | Activation flow through an RNN | `unknown` | no |
| `rnn_grouped.png` | RNN layers grouped | `unknown` | no |
| `rnn_loop.png` | A recurrent cell with its loop | `unknown` | no |
| `rnn_lstm.png` | LSTM cell internals | `unknown` | no |
| `rnn_unrolled.png` | The same cell unrolled over time | `unknown` | no |

### `reference/svm/`

| file | shows | source | publish |
|---|---|---|---|
| `hard-margin-issues.png` | Where a hard margin fails | `unknown` | no |
| `hyperparameter-C.png` | The SVM C parameter widening and narrowing the margin | `unknown` | no |
| `large-margin-classification.png` | Maximum margin separation | `unknown` | no |
| `svm-feature-scaling.png` | Why an SVM needs scaled features | `unknown` | no |
| `svm-regressor.png` | Support vector regression | `unknown` | no |

### `reference/time_series/`

| file | shows | source | publish |
|---|---|---|---|
| `Cov_nonstationary.png` | A series with changing variance | `unknown` | no |
| `Mean_nonstationary.png` | A series with a drifting mean | `unknown` | no |

### `s04_regression/`

| file | shows | source | publish |
|---|---|---|---|
| `3-linear_output_modIFIED.png` | Linear model output, annotated | `unknown` | no |
| `5.-ridge-table_modified.png` | Ridge coefficients as alpha increases | `unknown` | no |
| `8.-lasso-table_modified.png` | Lasso coefficients as alpha increases, some driven to zero | `unknown` | no |
| `bias-variance-2.png` | Bias-variance, second panel | `pdsh` | no |
| `bias-variance.png` | High-bias underfit against high-variance overfit, side by side | `pdsh` | no |
| `Coefficient_of_Determination.svg` | R2 as explained over total variance, as areas | `unknown` | no |
| `estimating_coefficients.png` | Least squares: the residuals being minimised | `unknown` | no |
| `L1_vs_L2.png` | Lasso diamond against ridge circle, RSS contours. ISLR Figure 6.7 | `islr` | no |
| `learning-curve.png` | Training and validation score against training set size | `pdsh` | no |
| `linear_regression.png` | A fitted regression line through a scatter | `unknown` | no |
| `linear_regression_error.gif` | Animated: the error shrinking as the line is fitted | `unknown` | no |
| `overfitting.png` | An overfitted curve through noisy points | `unknown` | no |
| `reg_overfitting.png` | Regression overfitting, small format | `unknown` | no |
| `slope_intercept.png` | Slope and intercept of a fitted line, annotated | `unknown` | no |

### `s05_classification/`

| file | shows | source | publish |
|---|---|---|---|
| `boundary_plot.png` | A decision boundary over scattered points | `mglearn` | no |
| `CM.png` | Compact confusion matrix | `unknown` | no |
| `confusion1.png` | Confusion matrix walkthrough, step 1 | `unknown` | no |
| `confusion2.png` | Confusion matrix walkthrough, step 2 | `unknown` | no |
| `confusion_mc.png` | Multi-class confusion matrix: TP/FP/FN/TN for one class against the rest | `unknown` | no |
| `ConfusionMatrix.pdf` | Confusion matrix, vector version | `unknown` | no |
| `ConfusionMatrix.png` | Confusion matrix layout with the four cells named | `slide-capture` | no |
| `DecisFunc.png` | Decision function, compact version | `unknown` | no |
| `decision-tree-choosing-split.png` | Choosing a split by impurity reduction | `mglearn` | no |
| `decision-tree-levels.png` | Boundary at successive depths | `pdsh` | no |
| `decision-tree-overfitting.png` | An unbounded tree memorising the training set | `pdsh` | no |
| `decision-tree.png` | A small decision tree | `unknown` | no |
| `Decision_Tree_Algorithm1.png` | The recursive splitting algorithm as a diagram | `unknown` | no |
| `DecisionFunc.jpg` | Decision function values across a feature plane | `unknown` | no |
| `DecisionTree.png` | Decision tree, larger format | `unknown` | no |
| `decisiontrees-finalstep.png` | Tree growth, final partition | `mglearn` | no |
| `decisiontrees-step1.png` | Tree growth, step 1 | `mglearn` | no |
| `decisiontrees-step2.png` | Tree growth, step 2 | `mglearn` | no |
| `dt_animals.png` | The classic animal-guessing tree, for intuition | `mglearn` | no |
| `Dummy1.png` | A majority-class baseline and its accuracy | `slide-capture` | no |
| `Dummy2.png` | Why the baseline's accuracy is misleading | `slide-capture` | no |
| `Euclidian.png` | Euclidean distance | `slide-capture` | no |
| `Euclidian_Manhatan.png` | Euclidean against Manhattan, same two points | `slide-capture` | no |
| `FitEval.png` | Fit on train, evaluate on test: the loop drawn | `slide-capture` | no |
| `KNN.png` | k nearest neighbours voting | `slide-capture` | no |
| `knn2.jpg` | KNN, alternate illustration | `unknown` | no |
| `Manhatan.png` | Manhattan distance | `slide-capture` | no |
| `micro_macro_avg.png` | Micro against macro averaging, worked | `unknown` | no |
| `minko.png` | Minkowski distance as p varies | `unknown` | no |
| `One_vs_rest1.png` | One-vs-rest decomposition, part 1 | `unknown` | no |
| `One_vs_rest2.png` | One-vs-rest decomposition, part 2 | `unknown` | no |
| `PercisionRecall.pdf` | Precision and recall, vector version | `unknown` | no |
| `PercisionRecall.png` | Precision against recall, defined on the matrix | `slide-capture` | no |
| `PRCurve.png` | A precision-recall curve | `unknown` | no |
| `ProbThreshold.png` | Predicted probabilities against a decision threshold | `slide-capture` | no |
| `PRThreshold.png` | Precision and recall as the threshold moves | `unknown` | no |
| `roc_Curve.png` | ROC curve with the chance diagonal | `slide-capture` | no |
| `Threshold.png` | Moving the threshold along a score distribution | `slide-capture` | no |
| `TP_TN.png` | True and false positives and negatives, illustrated | `slide-capture` | no |
| `WeightedKnn.png` | Distance-weighted KNN | `slide-capture` | no |

### `s06_validation/`

| file | shows | source | publish |
|---|---|---|---|
| `2-fold-CV.png` | Two-fold cross-validation, as labelled strips | `pdsh` | no |
| `5-fold-CV.png` | Five-fold cross-validation: five trials, the validation block moving | `pdsh` | no |
| `CV.jpg` | Cross-validation overview, jpg | `slide-capture` | no |
| `CV.png` | Cross-validation overview | `slide-capture` | no |

### `s07_ensembles/`

| file | shows | source | publish |
|---|---|---|---|
| `Bagging.png` | Bootstrap samples feeding parallel learners, then a vote | `slide-capture` | no |
| `bagging1.png` | Bagging, second version | `unknown` | no |
| `Ensemble1.png` | Ensemble families side by side | `unknown` | no |
| `global_picture.png` | Blind men and the elephant, each labelled a model, the elephant labelled the unknown distribution. The best single image in this collection | `unknown` | no |
| `pruning.png` | Pruning a grown tree back | `unknown` | no |
| `sample-comparisons.png` | Several models compared across samples | `unknown` | no |

### `s08_networks/`

| file | shows | source | publish |
|---|---|---|---|
| `comp_graph.png` | Computational graph of a layer | `unknown` | no |
| `comp_graph2.png` | Computational graph with the loss written above it: W, a, B and y feeding multiply, add, sigmoid, MSE. Same structure as the Session 8 worksheet, but the worksheet ends in cross-entropy, not MSE | `unknown` | no |
| `comp_graph3.png` | Computational graph, wide layout | `unknown` | no |
| `module4_NN_1.png` | Michigan course slide on neural networks, capture 1 | `slide-capture` | no |
| `module4_NN_10.png` | Michigan course slide on neural networks, capture 10 | `slide-capture` | no |
| `module4_NN_11.png` | Michigan course slide on neural networks, capture 11 | `slide-capture` | no |
| `module4_NN_2.png` | Michigan course slide on neural networks, capture 2 | `slide-capture` | no |
| `module4_NN_3.png` | Michigan course slide on neural networks, capture 3 | `slide-capture` | no |
| `module4_NN_4.png` | Michigan course slide on neural networks, capture 4 | `slide-capture` | no |
| `module4_NN_5.png` | Michigan course slide on neural networks, capture 5 | `slide-capture` | no |
| `module4_NN_6.png` | Michigan course slide on neural networks, capture 6 | `slide-capture` | no |
| `module4_NN_7.png` | Michigan course slide on neural networks, capture 7 | `slide-capture` | no |
| `module4_NN_8.png` | Michigan course slide on neural networks, capture 8 | `slide-capture` | no |
| `module4_NN_9.png` | Michigan course slide on neural networks, capture 9 | `slide-capture` | no |
| `network.png` | A small fully connected network | `unknown` | no |
| `network2.png` | Fully connected network, larger | `unknown` | no |
| `neuralnetworks.png` | Tall network diagram | `unknown` | no |
| `neurons.png` | Biological neuron against artificial unit | `unknown` | no |
| `nn.png` | Network with layer labels | `unknown` | no |
| `nn2.png` | Network, alternate layout | `unknown` | no |
| `nn_bias_hidden.png` | Where the bias term enters a hidden layer | `unknown` | no |
| `nn_bio_math.png` | Biological neuron mapped onto the mathematical one, side by side | `unknown` | no |
| `nn_feedforward.png` | A single neuron: inputs x1..xn, weights, bias b, activation a | `unknown` | no |
| `NN_hidden.pdf` | Hidden-layer network, vector version | `unknown` | no |
| `NN_hidden.png` | Network with one hidden layer | `slide-capture` | no |
| `NN_single.png` | Single-layer network | `unknown` | no |
| `nn_single_layer.png` | Single layer, weights drawn individually | `unknown` | no |
| `nn_timeline.jpg` | Timeline of neural network milestones | `unknown` | no |
| `num_grad.png` | Numerical gradient by finite differences | `unknown` | no |
| `numpy_array.png` | NumPy array shape and axes | `unknown` | no |
| `perceptron.png` | A single perceptron, inputs and weights | `unknown` | no |
| `perceptron2.png` | Perceptron, second version | `unknown` | no |
| `samples-features.png` | The samples-by-features matrix convention | `pdsh` | no |
| `sigmoid_neuron.png` | A unit with a sigmoid activation | `unknown` | no |
| `sigmoid_shape.png` | The sigmoid curve | `unknown` | no |
| `simple_comp_graph.png` | Computational graph of a single operation | `unknown` | no |
| `simple_comp_graph2.png` | Computational graph, two operations | `unknown` | no |
| `softmax.png` | Softmax turning scores into a distribution | `unknown` | no |
| `tensor1.png` | Scalar, vector, matrix, tensor | `unknown` | no |
| `tensor2.png` | Tensor axes labelled | `unknown` | no |

### `s09_s10_training/`

| file | shows | source | publish |
|---|---|---|---|
| `module4_DeepL_1.png` | Michigan course slide on deep learning, capture 1 | `slide-capture` | no |
| `module4_DeepL_2.png` | Michigan course slide on deep learning, capture 2 | `slide-capture` | no |
| `module4_DeepL_3.png` | Michigan course slide on deep learning, capture 3 | `slide-capture` | no |
| `module4_DeepL_4.png` | Michigan course slide on deep learning, capture 4 | `slide-capture` | no |
| `module4_DeepL_5.png` | Michigan course slide on deep learning, capture 5 | `slide-capture` | no |
| `module4_DeepL_6.png` | Michigan course slide on deep learning, capture 6 | `slide-capture` | no |
| `nn_dropout.png` | Dropout: units removed at random during training | `unknown` | no |
| `nn_learning_rate.png` | Successive gradient-descent steps t=0..3 of one learning rate down a loss curve | `unknown` | no |
| `nn_local.png` | Tangent lines at two points of a loss curve; the slope is zero at the minimum | `unknown` | no |
| `nn_loss.png` | A convex loss surface over two weights (w0, w1), with the steepest-descent arrow. Probable source, not established: Mitchell (1997), Machine Learning, fig. 4.4 | `unknown` | no |
| `nn_minimum.png` | A loss curve with a local and a global minimum | `unknown` | no |
| `nn_scale_driver.png` | Andrew Ng, "Scale drives machine learning progress" (Machine Learning Yearning, 2018): performance against amount of data for small, medium and large networks and a traditional algorithm. Third-party figure. Not about feature scaling: Session 9 §2 now uses `assets/generated/figures_en/scaling_descent.png` | `unknown` | no |

### `s11_representation/`

| file | shows | source | publish |
|---|---|---|---|
| `05.09-digits-pca-components.png` | Digits reconstructed from a few principal components | `pdsh` | no |
| `05.09-digits-pixel-components.png` | Digits reconstructed pixel by pixel, for contrast | `pdsh` | no |
| `05.09-PCA-rotation.png` | PCA as a rotation of the axes onto directions of variance | `pdsh` | no |
| `digitimage.png` | A handwritten digit as a pixel grid | `unknown` | no |
| `ImageDigit.png` | Digit image with its pixel values | `slide-capture` | no |
| `pca_inter.png` | PCA components, compact | `unknown` | no |
| `rnn_word_vec.png` | Words placed in an embedding space | `unknown` | no |

### `sources/`

| file | shows | source | publish |
|---|---|---|---|
| `decision-tree-choosing-split.pptx` | Editable source: choosing a split | `unknown` | no |
| `Presentation1.pptx` | Editable source: train/test split, CV, ROC curve, class separation | `unknown` | no |
| `unsupervised.pptx` | Editable source: 6 slides on DBSCAN criteria, ARI and silhouette | `unknown` | no |

## Generated figures are not in this library

Figures produced by the course itself live in `assets/generated/` (`figures_en/` for the English notebooks, `cours_08_10_fr/` for the French course and practicals of Sessions 8 to 10), each folder with its own README. They are original work, with no third-party rights, and `tools/make_release.py` ships the ones a released notebook references.
