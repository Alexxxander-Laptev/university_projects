# encoding utf-8
puts ('Vvedite veshestvennoe chislo: ')
a = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
b = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
c = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
d = gets.to_i
if ((a <= c) & (b <= d)) || ((a <= d) & (b <= c))
    puts ('Da, mojet')
else
    puts ('Net, ne mojet')
end