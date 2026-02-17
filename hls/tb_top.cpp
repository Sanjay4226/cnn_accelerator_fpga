#include <stdio.h>

// Declare the hardware function
void top(int a, int b, int *c);

int main() {
    int a = 10;
    int b = 20;
    int c;

    // Call hardware function
    top(a, b, &c);

    // Print result
    printf("Result = %d\n", c);

    // Check correctness
    if(c == 30) {
        printf("TEST PASSED\n");
    } else {
        printf("TEST FAILED\n");
    }

    return 0;
}
