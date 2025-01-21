## Lesson_019 task
Given a dataset with the results of exchange trading (located in the dataset.csv file).
Run the following:
1. Calculate descriptive statistics (minimum value, maximum value, mean value, median, mode, standard deviation) using Pandas for columns High, Low, Open, Close.
2. Build graphical dependences of changes in stock prices for each of the five main indicators (High, Low, Open, Close).
3. Train an LSTM neural network for time series forecasting using TensorFlow and Keras:\
    3.1. To train the model, use only data corresponding to the close of trading (column Close).\
    3.2. Use most of the data from the beginning of the sample (80-85%) as “past” values, and the rest as values ​​in the “artificial” future.\
    3.3. The main settings of hyperparameters, as well as the architecture of the neural network, are taken from the example presented in the lesson.\
    3.4. In the first experiment, choose the window size (window_size) equal to 7, and the horizon size (horizon) - 1.
4. Evaluate the quality of the trained model by calculating the standard deviation (RMSE) on the training and test parts of the sample.
5. Display graphically the results of the model, showing in the same coordinate system the real change in quotes and predicted using the model.
6. Conduct 5-7 experiments aimed at improving the model by changing the window size less than the base value of 7, and also more than it. For example, choose a window size of 4, 5, 6, 7, 8, 9, 10. Leave the horizon (the number of values ​​predicted per call) unchanged (equal to 1). For each of the experiments, follow steps 4 and 5.
7. Compare the performance of all models in terms of RMSE for both training and test sets. Build an appropriate bar chart.