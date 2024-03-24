# encoding utf-8
puts ('Vvedite veshestvennoe chislo: ')
x1 = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
y1 = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
x2 = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
y2 = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
x3 = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
y3 = gets.to_i
s = ((x1 - x3) * (y2 - y3) - ((y1 - y3) * (x2 - x3))) / 2
print ("#{s.abs}")