#include <stdio.h>

// Function prototype
void conv2d(int in[32][32], int kernel[3][3], int out[30][30]);

int main() {
    int in[32][32];
    int kernel[3][3];
    int out[30][30];

    // Initialize input
    for(int i=0;i<32;i++){
        for(int j=0;j<32;j++){
            in[i][j] = 1; // dummy data
        }
    }

    // Initialize kernel
    int k[3][3] = {{1,0,-1},{1,0,-1},{1,0,-1}};
    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
            kernel[i][j] = k[i][j];

    // Call hardware function
    conv2d(in, kernel, out);

    // Print few outputs
    printf("Output[0][0] = %d\n", out[0][0]);
    printf("Output[10][10] = %d\n", out[10][10]);

    return 0;
}