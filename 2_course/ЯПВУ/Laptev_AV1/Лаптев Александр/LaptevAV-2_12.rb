# encoding utf-8
puts ('Vvedite veshestvennoe chislo: ')
a = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
b = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
c = gets.to_i
if (((a > b) & (b > c)) || ((c > b) & (b > a)))
    y = b
    puts (y)
elsif (((b > a) & (a > c)) || ((c > a) & (a > b)))
    y = a
    puts (y)
elsif (((a > c) & (c > b)) || ((b > c) & (c > a)))
    y = c
    puts (y)
else
    puts ('Necorrectniyi vvod')
end