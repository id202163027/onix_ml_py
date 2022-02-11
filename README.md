## Lesson_013 task
Write a program that has the following functionality:\
– loads data from text files located in a specified directory (given in the docs directory). Data from each file must be presented as separate text documents for the vectorizer;\
– calculates a statistical measure of vocabulary frequency (Tf-idf) for the entire sample of text documents (the result should be a rectangular matrix);\
– returns a dictionary of features (words) with their indices (the vocabulary_ method of the CountVectorizer class), arranges this dictionary in ascending order of the index, and saves it to a human-readable JSON file;\
– creates a Pandas dataframe, the indices in which are the words from the generated dictionary (you can use the get_feature_names method to get them), and the values are the corresponding elements of the Tf-idf-matrix.