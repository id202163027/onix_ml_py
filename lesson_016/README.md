## Lesson_016 task 
Using the MLPClassifier class from Scikit-learn, train a multilayer perceptron simulating the operation of a logic circuit with the following truth table:\
A | B | C | D = F(A, B, C)
--- | --- | --- | --- 
0 | 0 | 0 | 1
0 | 0 | 1 | 0
0 | 1 | 0 | 1
0 | 1 | 1 | 0
1 | 0 | 0 | 1
1 | 0 | 1 | 0
1 | 1 | 0 | 1
1 | 1 | 1 | 0

To train the model, generate a dataset of 80 rows (each combination of A, B, C, D must vary 10 times, including the original truth table). Zero variation should be in the range from 0 to 0.4, one variation - from 0.6 to 1.2.
Adhere to the following rules:
1. D values ​​can only be 0 or 1.
2. Generate a dataset randomly, varying the data from the truth table randomly in the above range. To generate random values ​​in a range, use the function random.uniform.
3. The truth table itself must also be included in the dataset without change.
4. Demonstrate the work of a trained perceptron using 10 examples.