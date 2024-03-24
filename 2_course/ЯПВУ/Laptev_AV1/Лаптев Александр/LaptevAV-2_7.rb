# encoding utf-8
puts ('Vvedite veshestvennoe chislo: ')
a = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
b = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
c = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
d = gets.to_i
if (a == b) & (b == c) & (a == c)
    puts ('Nomer chisla, otlichnogo ot ostalnih: 4')
elsif (a == c) & (c == d) & (a == d)
    puts ('Nomer chisla, otlichnogo ot ostalnih: 2')
elsif (a == b) & (b == d) & (a == d)
    puts ('Nomer chisla, otlichnogo ot ostalnih: 3')
elsif (b == c) & (c == d) & (b == d)
    puts ('Nomer chisla, otlichnogo ot ostalnih: 1')
else
    puts ('Necorrectniyi vvod')
end