open_project C:/hls/ip_test/ip_test
open_solution solution1
set_part xc7z020clg484-1
create_clock -period 10 -name default
csynth_design
export_design -format ip_catalog -rtl verilog