%11 вариант
n2 = 2.0
n1 = 0.60
n0 = -0.360
d2 = 1.2000
d1 = 0.7406
d0 = 0.2734

n = [n2 n1 n0]
d = [1 d2 d1 d0]
f = tf ( n, d )
[n1, d1] = tfdata ( f, 'v' )
z = zero ( f )
p = pole ( f )
k = dcgain ( f )
b = bandwidth ( f )

f_ss = ss ( f )
f_ss.d = 1
k1 = dcgain ( f_ss )

f_zp = zpk ( f )
whos
pzmap ( f )

[wc, ksi, p] = damp ( f )
ltiview
print -dmeta

w = logspace (-1, 2, 100)
r = freqresp ( f, w )
r = r(:)
semilogx ( w, abs(r) )
print -dmeta

[u,t] = gensig('square',4)
lsim (f, u, t)
print -dmeta