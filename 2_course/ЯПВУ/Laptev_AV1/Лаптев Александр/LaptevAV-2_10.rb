# encoding utf-8
puts ('Vvedite veshestvennoe chislo: ')
a = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
b = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
c = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
d = gets.to_i
y = ([a, b].max + [a, b, c].max) / ([a - b, b - c].max + a + b + c)
puts (y)