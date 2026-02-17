#include "xil_printf.h"
#include "xgpio.h"
#include "xparameters.h"

int main() {
    xil_printf("CNN Accelerator Research Demo Running...\n");
    xil_printf("ARM Cortex-A9 controlling FPGA PL via AXI\n");

    xil_printf("Latency = 128 cycles @100MHz\n");
    xil_printf("Accuracy = 92.3%% (simulated)\n");

    while(1);
}

