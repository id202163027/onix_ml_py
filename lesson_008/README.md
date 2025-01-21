## Lesson_008 task
Using Pandas library, write a program that does the following:
1. Loads data from dataset.csv into a DataFrame. The header of the csv file should be ignored.
2. Displays a given number of consecutive rows from any given position in the dataframe.
3. Finds all unique genres (Genre) in the source data and separates the loaded dataframe into genre dataframes. For example, Shooter, Racing, Fighting, Puzzle, etc. genres should be placed in separate dataframes.
4. Orders the rows in each of the generated genre dataframes in ascending order of the values in Year column. For example, 1985, 1986, 1987, etc.
5. In each of the received genre dataframes, it re-indexes in ascending order of the index. The order of rows inside the dataframes should not change - corresponds to point 4.
6. Saves results to csv files. The file name must match the name of the genre (eg action.csv).