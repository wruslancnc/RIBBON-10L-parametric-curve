
## File: plot2D-calc-frate-limit-13B-u-versus-FRateLimit-CurrFRate.gp

clear
set size square
set autoscale
set grid

set xlabel "u[2]"
set ylabel "FRateLimit[8], CurrFRate[14]"
set title  " plot2D-calc-frate-limit-13A-u-versus-FRateLimit-CurrFRate"

# COMMENT RANGES FOR DEFAULT
set xrange [ 0.0 : +1.0]
set yrange [ 0.0 : +60.0] 


## PLOT CHECK (DIFFERENT DATA FILES)
plot   "data_calc_frate_limit.txt" using 2:8 with lines 
replot "data_calc_u_next.txt"  using 2:14 with lines


# DATA COLUMNS INDEX = COLUMN NUMBER
# rtime[1], 
# u[2], 
# u_next[3], 
# FRate_limit_1[4], 
# FRate_limit_2[5], 
# FRate_limit_3[6], 
# FRate_limit_4[7], 
# FRate_limit[8], 
# eps_N[9], 
# rho_N[10] 

# DTStamp_FHdata_calc_u_next 2022-06-23 12:23:39 179309410 

# EXECUTION
# gnuplot -p plot2D_calc_u_next_00_u_versus_u_next.gp


