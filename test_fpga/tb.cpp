// tb.cpp
#include <stdio.h>
#include <stdint.h>

#define H 28
#define W 28

extern void conv3x3(uint8_t in[H][W], int8_t kernel[3][3], int16_t out[H][W]);

int main() {
    static uint8_t img[H][W];
    static int8_t ker[3][3] = {{1,0,-1},{1,0,-1},{1,0,-1}};
    static int16_t out[H][W];
    // fill img with a simple pattern
    for (int i=0;i<H;i++) for (int j=0;j<W;j++) img[i][j] = (i+j)&0xFF;

    conv3x3(img, ker, out);

    // print few output values
    for (int i=13;i<15;i++){
        for (int j=13;j<15;j++){
            printf("out[%d][%d]=%d\n", i, j, out[i][j]);
        }
    }
    return 0;
}