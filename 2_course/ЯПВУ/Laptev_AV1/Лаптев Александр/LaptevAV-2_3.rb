# encoding utf-8
puts ('Vvedite veshestvennoe chislo: ')
a = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
b = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
c = gets.to_i
d = b * b - 4 * a * c
if (d < 0)
    print ('Korney net')
elsif (d == 0)
    print ('1 koren')
else
    print ('2 kornya')
end