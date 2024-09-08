// #include <stdio.h>

// int main()
// {
//     // Write C code here
//     printf("hello dustin\n");
//     printf("giatay ka man dung\n");
    
//     return 0;
// }

// #include <stdio.h>

// int main() {
//     int num1 = 10, num2 = 5;
//     int sum, diff, prod;
//     float quotient;

//     sum = num1 + num2;
//     diff = num1 - num2;
//     prod = num1 * num2;
//     quotient = (float)num1 / num2;  // Typecasting to ensure floating-point division

//     printf("Sum: %d\n", sum);
//     printf("Difference: %d\n", diff);
//     printf("Product: %d\n", prod);
//     printf("Quotient: %.2f\n", quotient);  // Displaying with 2 decimal places

//     return 0;
// }

// #include <stdio.h>
// #include <stdbool.h>

// #define N 9  // Size of the Sudoku grid

// // Function to print the Sudoku grid
// void printGrid(int grid[N][N]) {
//     for (int row = 0; row < N; row++) {
//         for (int col = 0; col < N; col++) {
//             printf("%d ", grid[row][col]);
//         }
//         printf("\n");
//     }
// }

// // Function to check if a number can be placed in a given cell
// bool isSafe(int grid[N][N], int row, int col, int num) {
//     // Check if the number is already in the row, column, or 3x3 subgrid
//     for (int x = 0; x < N; x++) {
//         if (grid[row][x] == num || grid[x][col] == num)
//             return false;
//     }

//     int startRow = row - row % 3, startCol = col - col % 3;
//     for (int i = 0; i < 3; i++) {
//         for (int j = 0; j < 3; j++) {
//             if (grid[i + startRow][j + startCol] == num)
//                 return false;
//         }
//     }
//     return true;
// }

// // Function to find an empty cell
// bool findEmptyCell(int grid[N][N], int *row, int *col) {
//     for (*row = 0; *row < N; (*row)++) {
//         for (*col = 0; *col < N; (*col)++) {
//             if (grid[*row][*col] == 0)
//                 return true;
//         }
//     }
//     return false;
// }

// // Function to solve the Sudoku using backtracking
// bool solveSudoku(int grid[N][N]) {
//     int row, col;

//     // If no empty cell is found, the Sudoku is solved
//     if (!findEmptyCell(grid, &row, &col))
//         return true;

//     // Try numbers from 1 to 9
//     for (int num = 1; num <= 9; num++) {
//         if (isSafe(grid, row, col, num)) {
//             grid[row][col] = num;  // Place the number

//             // Recursively solve for the next cell
//             if (solveSudoku(grid))
//                 return true;

//             grid[row][col] = 0;  // Backtrack
//         }
//     }
//     return false;  // Trigger backtracking
// }

// // Main function
// int main() {
//     int grid[N][N] = {
//         {5, 3, 0, 0, 7, 0, 0, 0, 0},
//         {6, 0, 0, 1, 9, 5, 0, 0, 0},
//         {0, 9, 8, 0, 0, 0, 0, 6, 0},
//         {8, 0, 0, 0, 6, 0, 0, 0, 3},
//         {4, 0, 0, 8, 0, 3, 0, 0, 1},
//         {7, 0, 0, 0, 2, 0, 0, 0, 6},
//         {0, 6, 0, 0, 0, 0, 2, 8, 0},
//         {0, 0, 0, 4, 1, 9, 0, 0, 5},
//         {0, 0, 0, 0, 8, 0, 0, 7, 9}
//     };

//     if (solveSudoku(grid))
//         printGrid(grid);
//     else
//         printf("No solution exists");

//     return 0;
// }



// #include <stdio.h>

// int main() {
//     char name[25];
//     int age;
//     float height, weight;
//     double pi = 3.141592653589793;  // Define Pi as a double
//     char gender;

//     printf("Start of the program\n");

//     // Asking for user input
//     printf("Enter your name: ");
//     scanf("%49s", name);  // %49s to avoid buffer overflow

//     printf("Enter your age: ");
//     scanf("%d", &age);  // %d for integer input

//     printf("Enter your gender (M/F): ");
//     scanf(" %c", &gender);  // %c for char input, notice the space before %c to ignore newline

//     printf("Enter your height (cm): ");
//     scanf("%f", &height);  // %f for float input

//     printf("Enter your weight (kg): ");
//     scanf("%f", &weight);  // %f for float input

//     // Printing the entered information
//     printf("You entered:\n");
//     printf("Name: %s\n", name);
//     printf("Age: %d\n", age);
//     printf("Gender: %c\n", gender);
//     printf("Height: %.2f cm\n", height);  // %.2f to limit the float to 2 decimal places
//     printf("Weight: %.2f kg\n", weight);  // %.2f to limit the float to 2 decimal places

//     // Printing Pi value
//     printf("The value of Pi is: %.15lf\n", pi);  // %.15lf to print Pi with high precision

//     return 0;
// }