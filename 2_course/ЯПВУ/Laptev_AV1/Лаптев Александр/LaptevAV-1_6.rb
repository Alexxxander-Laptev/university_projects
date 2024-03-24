# encoding utf-8
puts ("Vvedite chislo: ")
ch = gets.to_i
b = ch % 10
a = ch / 1000
sum = a + b
puts ("#{sum}")