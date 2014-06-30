"""
Project Euler Problem #3
=========================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
import math

def primes(num):

		primes = [false, false]
		for i in range(2, num):
				primes.append(true)
		p = 2
		while p**2 <= num:
				for j in range(1, num)
						if p * j > num:
								break
						else:
								primes[p*j] = false





print primes(100)

big_num = 600851475143
