# encoding utf-8
puts ('Vvedite veshestvennoe chislo: ')
x = gets.to_i
c = x % 10
b = x / 10 % 10
a = x / 100
if (a == b)
  print ('TRUE')
elsif (a == c)
  print ('TRUE')
elsif (b == c)
  print ('TRUE')
elsif (a == b) & (b == c) & (a == c)
  print ('TRUE')
else
  print ('FALSE')
end