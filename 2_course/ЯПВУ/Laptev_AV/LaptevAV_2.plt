set terminal png
set output "2.1.png"
set grid
set xlabel 'x'
set ylabel 'y'
set xrange [-20:20]
set yrange [-10:10]
plot     2*sin(x),\
		 7 + sin(x),\
		 5 + cos(x / 5),\
		 5 + cos(x),\
		 tan(x)
