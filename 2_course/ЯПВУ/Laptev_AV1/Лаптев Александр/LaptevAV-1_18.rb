# encoding utf-8
puts ('Vvedite veshestvennoe chislo: ')
x1 = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
y1 = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
x2 = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
y2 = gets.to_i
k = (y2 - y1) / (x2 - x1)
b = y1 - (y2 - y1) / (x2 - x1) * x2
print ("#{k} #{b}")