# encoding utf-8
puts ("Vvedite chislo: ")
ch = gets.to_i
c = ch % 10
b = ch / 10 % 10
a = ch / 100
pr = a * b * c
puts ("#{pr}")