## Lesson_003 task
Write a program that does the following:
1. calculates the values ​​of the functions f1 (x) = x / (x + 100) and f2 (x) = 1 / x when x changes in the range from 5 to 90 with a step of 1.
2. calculates the value of the functions f3 (x) = 20 * (f1 (x) + f2 (x)) / x.
3. represents the result in the form of a dictionary of the following form *: {x1: [f1 (x1), f2 (x1), f3 (x1)], x2: [f1 (x2), f2 (x2), f3 (x2)], ...}.
4. saves the result of calculations in a CSV file, the header (columns) of which are the values ​​x, f1 (x), f2 (x), f3 (x).
5. reads the recorded CSV file and presents the result as a list [[x1, f1 (x1), f2 (x1), f3 (x1)], [x2, f1 (x2), f2 (x2), f3 (x2) ], ...].
6. saves the list [[x1, f1 (x1), f2 (x1), f3 (x1)], [x2, f1 (x2), f2 (x2), f3 (x2)], ...] in JSON file.