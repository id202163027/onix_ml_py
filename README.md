## Lesson_009 task 
Write a program that has the following functionality opportunities:
1. Combines two Pandas dataframes (df1 and df2) by two columns (x_1, y_1 and x_2, y_2) so that:
• common strings - creates df3 (provide for the presence of arguments left_on and right_on for "left" and "right" dataframe indexes);
• all lines left - creates df4.
2. Finds the positions of all missing values in the df4 dataframe (forms a list of the “coordinates” of such values) and replaces them with the value 0.
3. Adds a z_avg column on the right to the df4 dataframe, in which the arithmetic average of z_left (from df1) and z_left (from df1) is calculated.
Note. Dataframes for testing the capabilities of the program are set as follows:
```
df1 = pd.DataFrame({'x_1': ['A', 'B', 'C'] * 3, 'y_1': ['D', 'E', 'F'] * 3,
    'z': np.random.randint(0, 20, 9)})
df2 = pd.DataFrame({'factor1': ['A', 'B', 'C'] * 4,'factor2': ['D', 'E'] * 6,
    'result': np.random.randint(0, 10, 12)})
```