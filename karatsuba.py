import math
import time

m1 = 123456124517487187425952323487328363460463476
m2 = 432724545145610724650817265871269485495984596

def karatsuba(m1,m2):

	if m1 == 0:
		n1 = 0
	else:
		n1 = ((math.floor((math.log(m1,10)))+1)/2)

	if m2 == 0:
		n2 = 0
	else:
		n2 = ((math.floor((math.log(m2,10)))+1)/2)

	n = int(max(n1,n2))

	div = pow(10,n)

	a = int(m1/div)
	b = int(m1%div)

	c = int(m2/div)
	d = int(m2%div)

	if n <= 1:
		step1 = a*c
		step2 = b*d
		step4 = (a+b)*(c+d) - step1 - step2
		return step1*pow(10,2*n) + step4*pow(10,n) + step2
	else:
		step1 = karatsuba(a,c)
		step2 = karatsuba(b,d)
		step4 = karatsuba((a+b),(c+d)) - step1 - step2
		return step1*pow(10,2*n) + step4*pow(10,n) + step2

if __name__ == "__main__":

	kas_start = time.time()
	prod_kas = karatsuba(m1,m2)
	kas_end = time.time()

	norm_start = time.time()
	prod_normal = m1*m2
	norm_end = time.time()
	
	print kas_end - kas_start	
	print norm_end - norm_start

	print prod_kas - prod_normal