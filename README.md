# Machine learning
  - [Categorized machine learning](https://chatgpt.com/share/67ee7ad7-e894-8010-8a1d-adea403d4429)

## Supervised learing
  - Examples
    + Classification
      * spam detection
      * image recognition
    + Regression
      * predicting house prices
      * stock market trends
  - Algorithms
    + Linear regression
    + Logistic regression
    + Decision trees
      * ID3
      * C4.5
      * C5.0
      * CART (Classification and Regression Tree)
    + Random forest
    + Support vector machine (SVM)
    + Neural networks

## Unsupervised Learning
  - Examples
    + Clustering
      * customer segmentation
      * anomaly detection
    + Dimensionality reduction
      * PCA
      * t-SNE for visualization
  - Algorithms
    + K-means
    + DBSCAN
    + Principal Component Analysis (PCA)
    + Autoencoders

## Reinforcement Learning (RL)
  - Examples
    + Game playing
      * AlphaGo
      * OpenAI's Dota 2 bot
    + Robotics
      * Autonomous driving
      * Robot control
  - Algorithms
    + Q-Learning
      + Q-table
      + Bellman equation
        * Learing rate: controls how much the agent updates its knowledge with each new experience
        * discount factor: controls the importance of future rewards compared to immediate rewards
        * epsilon: controls the importance of exploration compared to exploitation
      + epsilon decay
      + discount factor decay
      + Q-table can add states along training
    + Deep Q-Networks (DQN)
    + Policy Gradient Methods
      * PPO
      * A3C

# Questions and notes
  - Compare L1 (MAE) and L2 (MSE) loss function
  - Is L1 or L2 more robust for outliners?
  - Huber loss (Mix of L1 and L2)
  - Hinge loss (Use in SVM)
  - Compare Neural Network with Deep Neural Network
  - Compare Transformer and RNN
  - RNN read books from start to end
  - Transformer jump from chapters to chapters, from pages to pages to get relevant information
  - RNN use "hidden state"
  - Each RNN layer has its own hidden state
  - Hidden state is different from weights and biases
  - Weights and biases are learned during training and stay constant
  - while the hidden state changes as the network processes new input
  - Hidden state is more like a temporary memory that helps the network understand the context of the input sequence
  - The weights and biases are like the network's long-term memory, storing what it has learned from the training data
  - The hidden state is more like short-term memory, changing as the network processes new information
  - Hidden state is stored in RAM
  - CNN is just Convolutional and Pooling layers before DNN
  - LLM is just classification (use softmax and 1-hot encoding for the output layer)
  - Compare ReLU and Softmax activation functions
  - ReLU avoid vanishing gradient
  - But ReLU can sometimes lead to very large numbers in the neurons, which can cause problems
  - Prevent large numbers in neurons:
    + batch normalization
    + layer normalization
    + gradient clipping
    + weight normalization
  - LLM are self-supervised learning:
    + It's a bit like supervised learning because the model learns from labeled data
    + but the labels are automatically generated from the input text itself
  - Compare L1 regularization (Lasso regression) and Dimensionality reduction (techniques in unsupervised learning)
    + L1 regularization: used for features selection (remove some features, do not add features)
    + PCA (dimensionality reduction): Creates new features that are combinations of the original ones
  - Math: What is standard deviations
  - Why softmax use $e^x$? Why not use abs(x) or not use $x^2$?
  - Compare binary classification, multi-class classification, multi-label classification:
    + Which activation apply to the output layer? Sigmoid or softmax?
    + The number of neurons in the output layer? 1 for binary classification, n for others
# Binary classification
  - Logistic regression
  - SVM

# Multi-class classification
  - Decision tree
  - Random forest
  - k-nearest neighbors
  - Naive Bayes
  - Gradient boosting

# Regularization
  - Regularization:
    + adds a penalty to the model's loss function
    + which discourages overly complex models
  - Types:
    + L1 regularization:
      * adds the absolute value of the coefficients to the loss function
      * which can lead to sparse solutions where some coefficients are exactly zero
      * can be very useful for feature selection
    + L2 regularization:
      * adds the squared value of the coefficients to the loss function
      * which shrinks all coefficients towards zero but doesn't force them to be exactly zero

# Data preprocessing
  - Detect outliers:
    + interquartile range (IQR)
    + z-score
    + robust scaling
    + Isolation Forest
    + One-Class SVM
