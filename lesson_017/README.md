## Lesson_017 task
1. Load data from dataset.csv file into pandas dataframe.
2. Take the first 2 columns of the dataframe (position and intention) as the input vector, the third column as the target values ​​(you can use the drop method and general approaches to indexing and selecting data from the dataframe).
4. Using StandardScaler, transform the input data by scaling them, for example:\
scaler = StandardScaler()\
scaler.fit(X_train_unscaled)\
X_train=scaler.transform(X_train_unscaled)\
X_test = scaler.transform(X_test_unscaled)
3. Using the train_test_split function from Sklearn (from sklearn.model_selection import train_test_split) split the input and target data into training and test data; allocate 80% of the data for training (by setting the parameter train_size = 0.8). Target data do not scale.
5. Build a model with the same architecture as in the example discussed in the lesson, but with the following differences:\
– dimension of the input layer – 2 (input_shape=(2,).\
– the density of the output layer is 2, and its activation function must be specified explicitly (activation='softmax'.
6. Compile the model with the same optimizer as in the considered example (Adam), but with a different loss-function loss = 'sparse_categorical_crossentropy'. Also, set the parameter metrics = ['acc']. This is required for logging Accuracy.
7. Train the classifier model. The number of epochs (50 – 200) and the batch size (5 – 10) should be chosen independently, but in such a way that overfitting is not observed. The verbose hyperparameter can be set to 2 to log output during training.
8. Demonstrate the results of training in the form of curves of loss-functions (training and validation), as well as acc (training and validation). In the history (history), data on the change of acc and val_acc are available by the corresponding keys, that is:\
plt.plot(history.history['acc'], label='train')\
plt.plot(history.history['val_acc'], label='val')