#include <ap_int.h>

#define IMG_SIZE 32
#define K 3

typedef ap_int<16> data_t;

void cnn_top(data_t input[IMG_SIZE][IMG_SIZE],
             data_t output[IMG_SIZE-2][IMG_SIZE-2],
             data_t kernel[K][K])
{
#pragma HLS INTERFACE m_axi port=input  offset=slave bundle=gmem
#pragma HLS INTERFACE m_axi port=output offset=slave bundle=gmem
#pragma HLS INTERFACE m_axi port=kernel offset=slave bundle=gmem
#pragma HLS INTERFACE s_axilite port=return bundle=control

    for(int i = 0; i < IMG_SIZE-2; i++) {
        for(int j = 0; j < IMG_SIZE-2; j++) {
#pragma HLS PIPELINE
            data_t sum = 0;

            for(int ki = 0; ki < K; ki++) {
                for(int kj = 0; kj < K; kj++) {
                    sum += input[i+ki][j+kj] * kernel[ki][kj];
                }
            }

            if(sum < 0) sum = 0;
            output[i][j] = sum;
        }
    }
}


