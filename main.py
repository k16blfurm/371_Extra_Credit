#import math
import cmath
import numpy as np

regions = 3
Eo = 8.854*10**(-12)
Uo = 1.257*10**(-6)

# the Electric field in Region 1
Em = 50
#our W or angular frequency
W = 2* np.pi * 10**8
#Enter your Beta value here, if given
B = 2.094
#Sigma given
sigma = 0


print("Welcome to my program\n")
#print("Make sure file is named as computations.csv")

# our permutivity/permativity/Distances
Earray = [1,4 ,16]
Uarray = [1,1,1]
#Enter your distances sequentially here
Darray = [1/3]
#The real Distance array
DistanceArray = np.zeros((regions + 1), dtype=np.complex)
k = 1
while k != (regions - 1):
    print(k)
    DistanceArray[k] = Darray[k-1]
    k = k + 1

#Our array for N
Narray = np.zeros((regions), dtype=np.complex)
# This is Z at the origin
ZoArray = np.zeros((regions), dtype=np.complex)
# This is Z at the distance
ZdistanceArray = np.zeros((regions), dtype=np.complex)
# This is the impedance coefficient (at origin)
Loarray = np.zeros((regions), dtype=np.complex)
# This is the impedance coefficient (at distance)
LDarray = np.zeros((regions), dtype=np.complex)
Barray = np.zeros((regions), dtype=np.complex)
Aarray = np.zeros((regions), dtype=np.complex)
GammaArray = np.zeros((regions), dtype=np.complex)


# our incrementor
i = 0

while i != regions :
    E = Earray[i]*Eo
    U = Uarray[i]*Uo
    # our Alpha and Beta Values
    A = (W*np.sqrt(U*E)/np.sqrt(2))*(np.sqrt(1+(sigma/(W*E)**2))-1)**(1/2)
    B = (W*np.sqrt(U*E)/np.sqrt(2))*(np.sqrt(1+(sigma/(W*E)**2))+1)**(1/2)
    gamma = np.complex(A,B)
    #saving each value in an array
    Barray[i] = B
    Aarray[i] = A
    GammaArray[i] = gamma
    # Our values for N
    N = np.csingle(((np.sqrt(U/E)*np.exp(1j*(1/2)*np.arctan(sigma/(W*E))))/(1+(sigma/(W*E))**(2))**(1/4)))
    print ("N ",i," is equal to =", N)
    Narray[i] = N
    i = i + 1

print ("Now, let calculate the impedance and reflections")
# removing from the top of our incrementor
i = i - 1

while i != 0:
    if i == regions:
        ZoArray[i] = Narray[i]
        ZoArray[i-1] = ZoArray[i]
    elif i != regions:
        Loarray[i] = (ZoArray[i] - Narray[i])/(ZoArray[i] + Narray[i])
        print(Loarray[i])
        LDarray[i] = Loarray[i]*np.exp(2*GammaArray[i]*(-DistanceArray[i]-DistanceArray[i+1]))
        print (LDarray[i])
    i = i - 1