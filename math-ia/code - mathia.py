import math

Nterms = 10000 #the number of terms we are going to calculate

Num = []
Den = []

Num = [0 for i in range(Nterms + 1)]
Den = [0 for i in range(Nterms + 1)]

Theta0 = math.pi / 2 #Input opening angle
k = math.sin(Theta0/2)
ksquared = k ** 2

Num[1] = 1
Den[0] = 1

for i in range(1, Nterms):
  Num[i+1] = Num[i] * 2 * (2*i+1) #Calculating coefficients (Numerator)
  Den[i] = Den[i-1] * 2*i #Calculating coefficients (Denomenator)

Den[Nterms] = Den[Nterms - 1] * 2 * Nterms

BigK = 1
for i in range(1, Nterms + 1):
  BigK = BigK + (Num[i]/Den[i]) ** 2 * ksquared ** i

print(BigK * math.pi / 2)