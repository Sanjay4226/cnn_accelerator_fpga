create_clock -period 10 [get_ports clk]
# Ignore I/O constraint errors (for simulation / research)
set_property SEVERITY Warning [get_drc_checks NSTD-1]
set_property SEVERITY Warning [get_drc_checks UCIO-1]

# Dummy clock
create_clock -period 10 [get_ports clk]