class Point(object):
    '''Represents a point in 2D space'''

print(Point)
print()

#Passing an instance of Point() into variable blank
blank = Point()
print(blank)

#Assigning values to variables in the object.
blank.x = 3.0
blank.y = 4.0
print(blank.x,blank.y)

#Function to print points
def print_point(point):
    print('({},{})'.format(point.x,point.y))



#Create a rectanlge class
class Rectangle(object):
    '''Represents a rectangle in a space.
    Atributes: width, height, corner.
    Corner is a point object'''

#Initiating Rectangle class
box = Rectangle()

#Assigning values
box.width = 100.0
box.height = 200.0
box.corner = Point() #Initializes Point object in Rectable variable
box.corner.x = 0.0
box.corner.y = 0.0

#Instances as return values
#Return a point that contains the coordinates of the center of rectangle.
def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p

center = find_center(box)
print('center at: ({},{})'.format(center.x,center.y))


#Objects are mutable
#Changing size of rectangle
box.width += 50
box.height += 100
print(box.width)

#Function that does the same
def grow_rectanlge(rect,dwidth,dheight):
    rect.width += dwidth
    rect.height += dheight

print('Before Function: ')
print(box.width,box.height)
grow_rectanlge(box,50,100)
print('After function: ')
print(box.width,box.height)


#Copying
#The module copy contains a function that duplicates objects.
import copy

p1 = Point()
p1.x = 3.0
p1.y = 4.0
print(p1.x,p1.y)

p2 = copy.copy(p1)
print_point(p1)
print_point(p2)

#Same data, not the same point. This should return False. This checks object identidy, not equivalence.
print(p1 == p2)

#Check if a function has anm atribute
p = Point()
p.x = 1.0
print(type(p))
print(hasattr(p,'x'))
print(hasattr(p,'z'))
