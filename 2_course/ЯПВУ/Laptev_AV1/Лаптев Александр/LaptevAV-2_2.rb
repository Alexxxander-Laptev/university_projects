# encoding utf-8
puts ('Vvedite veshestvennoe chislo: ')
a = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
b = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
c = gets.to_i
d = b * b - 4 * a * c
if (d < 0)
    puts ('Korney net')
elsif (d == 0)
    x = -b / (2 * a)
    puts ("#{x}")
else
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    puts ("#{x1} #{x2}")
end