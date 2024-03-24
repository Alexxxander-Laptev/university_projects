# encoding utf-8
puts ('Vvedite veshestvennoe chislo: ')
a = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
b = gets.to_i
if (a == 0) & (b != 0)
    puts ('yravnenie ne imeet resheniyi')
elsif (a == 0) & (b == 0)
    puts ('yravnenie imeet besconechnoe kol-vo resheniyi')
else
    x = b / a
    puts ("#{x}")
end