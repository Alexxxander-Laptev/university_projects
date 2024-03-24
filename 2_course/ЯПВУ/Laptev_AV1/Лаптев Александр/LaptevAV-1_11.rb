# encoding utf-8
puts ('Vvedite veshestvennoe chislo: ')
x1 = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
y1 = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
x2 = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
y2 = gets.to_i
ras = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print ("#{ras}")