# encoding utf-8
puts ('Vvedite veshestvennoe chislo: ')
x = gets.to_i
c = x % 10
b = x / 10 % 10
a = x / 100
if a == c
  print ('TRUE')
else
  print ('FALSE')
end