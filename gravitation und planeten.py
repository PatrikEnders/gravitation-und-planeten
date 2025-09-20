import pygame
import math

sizeX = 448793612100
sizeY = 448793612100

windowX = 950
windowY = 950

def xAccurateToUnaccurate(x):
    x = windowX*x/sizeX
    return x
def yAccurateToUnaccurate(y):
    y = windowY*y/sizeY
    return y

# meassures distance between star and object in meters
def getDistance():
    distance = (math.sqrt( (x_Star-x_Object)**2 + (y_Star-y_Object)**2 ))
    #print(distance/40524193199)
    return distance


def getAcceleration():
    try:
        return (6.67430*10**-11)*mass_Star/getDistance()**2
    except:
        return (6.67430*10**-11)*mass_Star/0.0001**2
    
def getXAcceleration():
    return getAcceleration()*(x_Star-x_Object)/(abs(x_Star-x_Object)+abs(y_Star-y_Object))
    

def getYAcceleration():
    return getAcceleration()*(y_Star-y_Object)/(abs(y_Star-y_Object)+abs(x_Star-x_Object))


#initalizations
pygame.init()
win = pygame.display.set_mode((windowX,windowY))
pygame.display.set_caption("gravitation'n'things")
#pygame.display.toggle_fullscreen()




#pos
mass_Star = 1.988*10**30
x_Star = 224396806050
y_Star = 224396806050
xStarVelocity = 0
yStarVelocity = 0

mass_Object = 5.97*10**24
x_Object = 224396806050-149597870700*0.88   # *0.88 is a multiplicator to correct the overall deviation (missing asteroid belt)
y_Object = 224396806050

xObjectVelocity = 0
yObjectVelocity = -29290 # actual velocity of the earth
seconds = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    win.fill((0,0,0))

    for i in range(0,2000):
        xObjectVelocity += getXAcceleration()
        yObjectVelocity += getYAcceleration()
        x_Object += xObjectVelocity
        y_Object += yObjectVelocity

    seconds += 2000
    print(seconds/60/60/24/365.25," Years")
    print(math.sqrt(yObjectVelocity**2+xObjectVelocity**2)," m/s")

    pygame.draw.circle(win, (255,255,00),(
        xAccurateToUnaccurate(x_Star),yAccurateToUnaccurate(y_Star)
        ),5,5) # star
    pygame.draw.circle(win, (255,255,255),(
        xAccurateToUnaccurate(x_Object),yAccurateToUnaccurate(y_Object)
        ),5,5) # object

    pygame.display.update()
pygame.quit()