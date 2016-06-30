
from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()

def drawSquare(length):
	for i in range(4):
		fd(bob,length)
		lt(bob)

def drawPolygonWithAngle(length,sides,angle):
	for i in range(sides):
		lt(bob,angle)		
		fd(bob,length)
		

def drawPolygon(length, sides):
	angle = 360 / sides
	drawPolygonWithAngle(length,sides,angle)

def drawCircle(radius):
	"""draws a circle for the given
		radius
	"""
	circumference = 2 * math.pi * radius
	sides = int ( circumference / 3) + 1
	length = int ( sides / 3)
	drawPolygon(length,sides)

#drawCircle(9)

def drawPolygonPie(sides, length):
	angle = 360 / sides
	sideDistance = math.sqrt(2) * length
	sideAngle = (180 - angle) / 2
	sd = (math.sin(math.radians(90)) * (sides / 2) ) / math.sin(math.radians(sideAngle))
	print sides
	for i in range(sides):
		fd(bob, length)
		fd(bob, length)
		lt(bob, 180 - angle / 2)
		fd(bob, sd)
		lt(bob, angle)
		fd(bob, sd)
		lt(bob, 180 - angle / 2)
		fd(bob, length)
		fd(bob, length)
		lt(bob,angle)
		

drawPolygonPie(4,30)
	

