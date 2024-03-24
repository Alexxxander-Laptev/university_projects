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
a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
b = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
c = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
if (a == b) & (a == c) & (b == c)
    puts ('Etot treygolnic - ravnostoronniyi')
else
    puts ('Etot treygolnic - ne ravnostoronniyi')
end