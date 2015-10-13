#PyMath Created by: Andrew Eckerman
#===================================
#Adding

def Add(num1, num2):
	return (num1 + num2)

#Subtracting

def Subtract(num1, num2):
	return (num1 - num2)

#Multiplying

def Multiply(num1, num2):
	return (num1 * num2)

#Dividing

def Divide(num1, num2):
	return (num1 / num2)

#start-Geometery

#Finding Area of Circle

def Acircle(radius):
	return (radius * radius * 3.14)

#Finding Circumfrence of Circle

def Ccircle(radius):
	return (radius * 3.14 * 2)

#Parameter of a square

def Psquare(side):
	return (side + side + side + side)

#Area of a square

def Asquare(side):
	return (side * side)

#Parameter of a rectangle

def Prect(width, height):
	return (width + height * 2)

#Area of a rectangle

def Arect(width, height):
	return (width * height)

#Perimeter of a triangle

def Ptri(side1, side2, side3):
	return (side1 + side2 + side3)

#Area of a triangle

def Atri(base, height):
	return (base * height / 2)

#Parameter of trapezoid

def Ptrapez(base1, base2, side1, side2):
	return (base1 + base2 + side1 + side2)

#Area of trapeziod

def Atrapez(height, base1, base2):
	return (base1 + base2 / 2 * height)

#end-Geometery

#To the Power of 0

def TP0(number):
	return (0)

#To the Power of 1

def TP1(number):
	return (number)

#To the Power of 2

def TP2(number):
	return (number * number)

#To the Power of 3

def TP3(number):
	return (number * number * number)

#To the Power of 4

def TP4(number):
	return (number * number * number * number)

#Finding the Mechanical Advantage of a lever

def MechAdv(d1, d2):
	return (d1 / d2)
