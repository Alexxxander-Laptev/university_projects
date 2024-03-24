set terminal png
set output "1.png"
set grid
set xlabel 'x'
set ylabel 'y'
set xrange [0:20]
set yrange [0:20]
plot     5 notitle,\
		-0.5*x + 10 notitle,\
		-2 * x + 20
