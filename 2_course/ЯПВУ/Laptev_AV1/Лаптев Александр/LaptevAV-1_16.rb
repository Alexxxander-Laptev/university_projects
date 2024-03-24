# encoding utf-8
puts ('Vvedite veshestvennoe chislo: ')
a = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
b = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
c = gets.to_i
p = (a + b + c) / 2
r = ((p - a) * (p - b) * (p - c) / p) ** 0.5
print ("#{r}")