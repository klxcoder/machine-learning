# Youtube video
  - [Let’s Write a Decision Tree Classifier from Scratch - Machine Learning Recipes #8](https://www.youtube.com/watch?v=LDRbO9a6XPU)
  - https://github.com/random-forests/tutorials/blob/master/decision_tree.ipynb

# Training data
| Color | Diameter | Label |
| ----- | -------- | ----- |
| Green | 3 | Apple |
| Yellow | 3 | Apple |
| Red | 1 | Grape |
| Red | 1 | Grape |
| Yellow | 3 | Lemon |

# CART
  - Classification and Regression Tree
  - Gini Impurity
  - Information Gain

# Calculate Gini Impurity
  - First, let's count each label in your dataset:
    + Apple: 2
    + Grape: 2
    + Lemon: 1

  - Total samples = 5.
  - Next, calculate the probability for each label:
    + $p(Apple)=\frac{2}{5}​=0.4$
    + $p(Grape)=\frac{2}{5}=0.4$
    + $p(Lemon)=\frac{1}{5}=0.2$

  - The Gini impurity formula is: $G = 1 - \sum(p_i)^2$
  - Plug in the probabilities:
    + $G = 1 - (0.4^2 + 0.4^2 + 0.2^2) = 0.64$
  - So, the `Gini impurity` of your dataset is `0.64`.

# Possible splits
  - Is Color equal to Green?
  - Is Color equal to Yellow?
  - Is Color equal to Red?
  - Is Diameter < 2.0?

# Steps
  - Iterate through all possible splits
  - Choose the split that maximize `information gain`

# Evaluate if "Is Color equal to Green?" is a good split

## Step 1: Split the Data
  - Left Group (Color = Green):
    + ('Green', 3, 'Apple')
  - Right Group (Color ≠ Green):
    + ('Yellow', 3, 'Apple')
    + ('Red', 1, 'Grape')
    + ('Red', 1, 'Grape')
    + ('Yellow', 3, 'Lemon')

## Step 2: Calculate Gini Impurity for Each Group
  - Left Group (1 item, all Apple)
    + Labels: ['Apple']
    + Gini Impurity = 0.0 (Pure group)
  - Right Group (4 items: 1 Apple, 2 Grapes, 1 Lemon)
    + Probabilities:
      * Apple: 1/4 = 0.25
      * Grape: 2/4 = 0.5
      * Lemon: 1/4 = 0.25
    + Gini Impurity:
      * $1-(0.25^2 + 0.5^2 + 0.25^2) = 0.625$

## Step 3: Calculate Weighted Gini Impurity
  - Weighted Gini = $(\frac{1}{5} * 0.0) + (\frac{4}{5} * 0.625) = 0.5$

## Step 4: Compute Information Gain
  - Information Gain = $Orignial Gini - Weighted Gini = 0.64 - 0.5 = 0.14$

# Desired steps to build tree

```txt
---------
rows = [['Green', 3, 'Apple'], ['Yellow', 3, 'Apple'], ['Red', 1, 'Grape'], ['Red', 1, 'Grape'], ['Yellow', 3, 'Lemon']]
best_gain = 0.37333333333333324
best_question = Is diameter >= 3?
---------
rows = [['Green', 3, 'Apple'], ['Yellow', 3, 'Apple'], ['Yellow', 3, 'Lemon']]
best_gain = 0.11111111111111116
best_question = Is color == Yellow?
---------
rows = [['Yellow', 3, 'Apple'], ['Yellow', 3, 'Lemon']]
best_gain = 0
best_question = None
---------
rows = [['Green', 3, 'Apple']]
best_gain = 0
best_question = None
---------
rows = [['Red', 1, 'Grape'], ['Red', 1, 'Grape']]
best_gain = 0
best_question = None
```

# print tree

```txt
Is diameter >= 3?
--> True:
  Is color == Yellow?
  --> True:
    Predict {'Apple': 1, 'Lemon': 1}
  --> False:
    Predict {'Apple': 1}
--> False:
  Predict {'Grape': 2}
```