## Lesson_014 task
For data in dataset.csv, write code that realizes
classification with SVM algorithm (SVC class):\
– load data from a CSV file into a dataframe using the library Pandas, display first 10 and last 10 rows;\
– the last column of the dataframe (label) is considered a label, all previous (beginning with meanfreq and ending with modindx) – vector coordinates; split data appropriately (last column - y, all columns except the last - X);\
– encode labels using the LabelEncoder class, labels must be specified numerically (0 or 1);\
– standardize data – X (StandardScaler class);\
– split the data into training (80%) and test (20%) samples (from sklearn.model_selection import train_test_split);\
– train the model based on the SVC class (kernel='linear', other settings are by default);\
– calculate the accuracy_score metric (from sklearn import metrics);\
– change the kernel to RBF (kernel='rbf'), retrain the model on the same data, calculate the accuracy_score with the new kernel.