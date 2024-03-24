puts ('Vvedite veshestvennoe chislo: ')
a = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
b = gets.to_i
puts ('Vvedite veshestvennoe chislo: ')
c = gets.to_i
c_al = (b ** 2.0 + c ** 2.0 - a ** 2.0) / (2 * b * c)
al = Math.acos(c_al) * 180 / Math::PI
puts ("#{al}")
c_bet = (a ** 2.0 + c ** 2.0 - b ** 2.0) / (2 * a * c)
bet = Math.acos(c_bet) * 180 / Math::PI
puts ("#{bet}")
c_gam = (b ** 2.0 + a ** 2.0 - c ** 2.0) / (2 * b * a)
gam = Math.acos(c_gam) * 180 / Math::PI
puts ("#{gam}")