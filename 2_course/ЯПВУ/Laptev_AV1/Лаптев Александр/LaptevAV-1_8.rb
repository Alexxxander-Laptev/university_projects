# encoding utf-8
puts ('Vvedite chislo: ')
ch = gets.to_i
c = ch / 10 % 10
b = ch / 100 %10
sum = b + c
print ("#{sum}")