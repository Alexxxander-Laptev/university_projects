# encoding utf-8
puts ('Vvedite veshestvennoe chislo: ')
a = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
b = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
c = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print ("#{s}")