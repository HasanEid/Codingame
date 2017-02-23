# Codingame
Python Code for closest temperature to 0

import sys
import math

# the standard input according to the problem statement.
n = int(raw_input())				# the number of temperatures to analyse
temps = raw_input()					# the n temperatures expressed as integers ranging from -273 to 5526

list_temps = temps.split()  		#break string of temperatures into a list of smaller strings

if len(temps) == 0: 
    print '0' 						#no temperature case
	
else:
    x = int(list_temps[0]) 			#define x as the first temperature 
    
    for i in range(n):
        y = int(list_temps[i])  
		
        if abs(x) > abs(y): 		#comparing the temperature we have to other temperatures
            x = y 					#choosing the smaller one
			
        elif abs(x) == abs(y):  	#in case of same distance to 0
            if x < y: 
                x = y 				#choose the positive
    print x 
