# encoding utf-8
puts ('Vvedite chislo: ')
ch = gets.to_i
d = ch % 10
c = ch / 10 % 10
b = ch / 100 %10
a = ch / 1000
puts ("#{d} #{c} #{b} #{a}")