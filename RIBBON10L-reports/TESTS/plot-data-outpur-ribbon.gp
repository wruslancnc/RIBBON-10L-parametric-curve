
## File: plot-data-output-ribbon.gp

clear
set size square
set autoscale
set grid

set xlabel "x-position"
set ylabel "y-position"
set title  "Plot 2D (x,y) RIBBON parametric curve (square view)"

## COMMENT RANGES FOR DEFAULT
set xrange [ -1.0 : +6.0]
set yrange [ -1.0 : +6.0]

## PLOT CHECK
plot   "data-output-ribbon.txt" using 2:3 with lines title "(x,y) points"


## EXECUTION
## gnuplot -p plot-data-output-ribbon.gp

