
import pygame
from pygame.locals import *

##see all commands at https://github.com/damiafuentes/DJITelloPy/blob/master/djitellopy/tello.py

##initialize pygame
pygame.init()
dispay = pygame.display.set_mode((600,600), 0,32)
clock = pygame.time.Clock()

#intialize joystick
pygame.joystick.init()
joystick = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

#left joystic filtering
axis_0 = [10,10,10]
axis_1 = [10,10,10]
avg_0 = 20
avg_1 = 20

#right joystick filtering
axis_2 = [10,10,10]
axis_3 = [10,10,10]
avg_2 = 20
avg_3 = 20


keepflying = True

while keepflying:
    for event in pygame.event.get():
        if event.type ==JOYBUTTONDOWN:
            #Buttons
            if (event.button == 0):
                print('a pressed')
            if (event.button == 1):
                print('b pressed')
            if (event.button == 2):
                print('x pressed')
            if (event.button == 3):
                print('y pressed')
                
            #Bumpers
            if (event.button == 4):
                print('left bumper pressed')
            if (event.button == 5):
                print('right bumper pressed')

            #Middle buttons
            if (event.button == 6):
                print('left middle pressed')
            if (event.button == 7):
                print('right middle pressed')
        if event.type ==JOYBUTTONUP:
            print('released')


        if event.type == JOYAXISMOTION:
            #Left Joystick
            if (event.axis ==0):
                axis_0.insert(0,event.value)
                axis_0.pop()
                avg_0 = sum(axis_0)/len(axis_0)
            elif(event.axis== 1):
                axis_1.insert(0,event.value)
                axis_1.pop()
                avg_1 = sum(axis_1)/len(axis_1)
            if (event.axis ==0) or (event.axis== 1):
                if (-.25<avg_0<.25) and (-1<avg_1<-.75):
                    print('up')
                elif (-.75<avg_0<-.25) and (-.75<avg_1<-.25):
                    print('up left')
                elif (-1<avg_0<-.75) and (-.25<avg_1<.25):
                    print('left')
                elif (-.75<avg_0<-.25) and (.25<avg_1<.75):
                    print('down left')
                elif (-.25<avg_0<.25) and (.75<avg_1<1):
                    print('down')
                elif (.25<avg_0<.75) and (.25<avg_1<.75):
                    print('down right')
                elif (.75<avg_0<1) and (-.25<avg_1<.25):
                    print('right')
                elif (.25<avg_0<.75) and (-75<avg_1<-.25):
                    print('up right')
            

            #Right Joystick
            if (event.axis ==2):
                axis_2.insert(0,event.value)
                axis_2.pop()
                avg_2 = sum(axis_2)/len(axis_2)
            elif(event.axis== 3):
                axis_3.insert(0,event.value)
                axis_3.pop()
                avg_3 = sum(axis_3)/len(axis_3)
            if (event.axis ==2) or (event.axis== 3):
                if (-.25<avg_2<.25) and (-1<avg_3<-.75):
                    print('up')
                elif (-.75<avg_2<-.25) and (-.75<avg_3<-.25):
                    print('up left')
                elif (-1<avg_2<-.75) and (-.25<avg_3<.25):
                    print('left')
                elif (-.75<avg_2<-.25) and (.25<avg_3<.75):
                    print('down left')
                elif (-.25<avg_2<.25) and (.75<avg_3<1):
                    print('down')
                elif (.25<avg_2<.75) and (.25<avg_3<.75):
                    print('down right')
                elif (.75<avg_2<1) and (-.25<avg_3<.25):
                    print('right')
                elif (.25<avg_2<.75) and (-75<avg_3<-.25):
                    print('up right')
        
            #Left Trigger
            if (event.axis == 4):
                print('left trigger')
                speed = 50
            #Right Trigger
            if (event.axis == 5):
                print('right trigger')
        
        if event.type == JOYHATMOTION:
            #DPAD up,down,left,right
            if (event.value == (1,0)):
                print('right dpad')
            if (event.value == (-1,0)):
                print('left dpad')
            if (event.value == (0,1)):
                print('up dpad')
            if (event.value == (0,-1)):
                print('down dpad')
            
        #exitx button on py display
        if event.type == QUIT:
            pygame.quit() 



#Xbox controller pygame
#JOTBUTTON (DOWN/UP) event
    #ABXY .button->
        #a = 0
        #b = 1
        #y = 3
        #x = 2

    #Bumpers .button -> 
        #left : 4
        #right : 5

#JOYAXISMOTION event

    #Right joystick: .axis ->
        #  up/down  2:(up:pos, down:neg)  
        # left/right  3: (left:neg, right:pos)

    #Left joystick: .axis -> 
        #  up/down  0: .value(down:neg, up:pos)  
        # left/right  1: .value(left:neg, right:pos)

    #Triggers Left and Right .axis ->
        #right trig (5): .value (1 =pulldown, -1 = letup)
        #left trig  (4): .value (1 =pulldown, -1 = letup)

#JOYHATMOTION event
    # DPAD .value ->
        # right:(1,0)
        # left: (-1,0)
        # up: (0,1)
        # down: (0,-1)           
         
        

        

       
