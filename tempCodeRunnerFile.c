#include <stdio.h>

int main() {
    char name[25];
    int age;
    float height, weight;
    double pi = 3.141592653589793;  // Define Pi as a double
    char gender;

    printf("Start of the program\n");

    // Asking for user input
    printf("Enter your name: ");
    scanf("%49s", name);  // %49s to avoid buffer overflow

    printf("Enter your age: ");
    scanf("%d", &age);  // %d for integer input

    printf("Enter your gender (M/F): ");
    scanf(" %c", &gender);  // %c for char input, notice the space before %c to ignore newline

    printf("Enter your height (cm): ");
    scanf("%f", &height);  // %f for float input

    printf("Enter your weight (kg): ");
    scanf("%f", &weight);  // %f for float input

    // Printing the entered information
    printf("You entered:\n");
    printf("Name: %s\n", name);
    printf("Age: %d\n", age);
    printf("Gender: %c\n", gender);
    printf("Height: %.2f cm\n", height);  // %.2f to limit the float to 2 decimal places
    printf("Weight: %.2f kg\n", weight);  // %.2f to limit the float to 2 decimal places

    // Printing Pi value
    printf("The value of Pi is: %.15lf\n", pi);  // %.15lf to print Pi with high precision

    return 0;
}