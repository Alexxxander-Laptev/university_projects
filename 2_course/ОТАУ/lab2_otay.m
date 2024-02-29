Ts = 18.0
K = 0.08
TR = 1
Toc = 5
Tv = 1

P = tf ( K, [Ts 1 0] )
R0 = tf ( 1, [TR 0] )
R = feedback ( R0, 1 )
G = P * R
step ( G )
H = tf ( 2*K, [Toc 1] )
L = G * H
bode ( L )
sisotool
Cpd = 1 + tf ( [Ts 0], [Tv 1] )
W = Cpd*G / (1 + Cpd*G*H)
W = minreal(W)
pole ( W )
dcgain ( W )
Wu = minreal(C/ (1 + C*G*H))
step ( Wu )