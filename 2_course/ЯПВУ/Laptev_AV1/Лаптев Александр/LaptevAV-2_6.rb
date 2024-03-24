# encoding utf-8
puts ('Vvedite veshestvennoe chislo: ')
a = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
b = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
c = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
d = gets.to_i
if (a <= 0) || (b <= 0) || (c <= 0) || (d <= 0)
    puts ('Necorrectnie dannie')
elsif (a == c) & (b == d)
    puts ('Mojno postroit pryamoygolnic s takimi storonami')
else
    puts ('Nelzya postroit pryamoygolnic s takimi storonami')
end