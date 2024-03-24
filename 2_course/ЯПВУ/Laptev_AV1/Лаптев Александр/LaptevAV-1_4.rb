ch = 269
puts ("Vvedite chislo: #{ch}")
c = ch % 10
b = ch / 10 % 10
a = ch / 100
sum = a + b + c
print ("#{sum}")