// top.cpp
#include <stdint.h>

#define H 28
#define W 28

void conv3x3(uint8_t in[H][W], int8_t kernel[3][3], int16_t out[H][W]) {
#pragma HLS INTERFACE mode=s_axilite port=return bundle=CTRL
#pragma HLS INTERFACE mode=m_axi depth=784 port=in offset=slave bundle=Gmem
#pragma HLS INTERFACE mode=m_axi depth=9 port=kernel offset=slave bundle=Gmem
#pragma HLS INTERFACE mode=m_axi depth=784 port=out offset=slave bundle=Gmem

    for (int i = 1; i < H-1; i++) {
        for (int j = 1; j < W-1; j++) {
#pragma HLS PIPELINE II=1
            int sum = 0;
            for (int ki = 0; ki < 3; ki++)
                for (int kj = 0; kj < 3; kj++)
                    sum += in[i-1+ki][j-1+kj] * kernel[ki][kj];
            out[i][j] = sum;
        }
    }
}