# Youtube video
  - [Let’s Write a Decision Tree Classifier from Scratch - Machine Learning Recipes #8](https://www.youtube.com/watch?v=LDRbO9a6XPU)

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