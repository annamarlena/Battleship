# Programming Project - Battleship Game Simulation
# Programmer: Anna Marlena K.
# April 19, 2015

"""

Battleship Game

This program simulates the popular board game Battleship. It graphs a
board with a 20x20 grid. In this version, 5 different ships are randomly
placed on the grid. The program then begins to 'fire shots', trying to
hit one of the ships. Once one of the ships receives a direct hit, the
program will begin a localized search for the rest of the ship. Once it has
hit all the spaces occupied by the ship, that ship 'sinks' and the program
begins its search for the next ship to sink. Once all the ships have been
sunk, the program will print the average number of shots taken during the
simulations to sink all the ships.

*Note: all graphic images used in this simulation were acquired from open source
image files on the web. 

"""

# import the math, random, and graphics modules
import math
from random import choice, randint
from graphics import *
from time import sleep

# create a brief greeting window
def greeting(Draw = True):
    
    # if Draw = True:
    win = GraphWin("Battleship", 800, 800, autoflush=True)

    # set window coordinates
    win.setCoords(-2, -2, 22, 22)

    # welcome screen
    welcome = Image(Point(10,10),'battleship2.gif')
    welcome.draw(win)
    title = Text(Point(10,19),'Battleship')
    title.setOutline('white')
    title.setFace('courier')
    title.setStyle('bold')
    title.setSize(36)
    title.draw(win)
    myName = Text(Point(18,-1),'Programmed by Marlena')
    myName.setOutline('white')
    myName.setFace('courier')
    myName.setSize(14)
    myName.draw(win)
 
    sleep(2)
    win.close()

# create a window for the graphics
def gameWindow(Draw = True):
    
    # if Draw = True:
    win = GraphWin("Battleship", 800, 800, autoflush=True)

    # set window coordinates
    win.setCoords(-2, -2, 22, 22)

    win.autoflush=False
      
    #create a set of boundaries for the x and y axis
    xp1 = Point(0,0)
    xp2 = Point(19,0)
    xaxis = Line(xp1,xp2)
    yp1 = Point(0,0)
    yp2 = Point(0,19)
    yaxis = Line(yp1,yp2)

    # create a list of all points
    ptList = []

    for y in range(0,20):
        for x in range(0,20):
            ptList.append((x,y))

    # set the background image
    background = Image(Point(10,10),'LightFilter.gif')
    background.draw(win)
    
    # draw the gameboard grid
    gridList = []

    for n in range(len(ptList)):
        y = ptList[n][1]
        x = ptList[n][0]
        grid = Rectangle(Point(x,y),Point((x+1),(y+1)))
        grid.setOutline('white')
        grid.setFill('blue1')
        grid.draw(win)
        gridList.append(grid)

    # mark points on the x axis for comprehension of scale
    yaxisPoint = 0

    for n in range(0,20):
        x = -.5
        y = ptList[n][0]
        yaxisPoints = Text(Point(x,y+.5), yaxisPoint)
        yaxisPoints.setOutline('white')
        yaxisPoints.draw(win)
        yaxisPoint += 1

    xaxisPoint = 0

    for n in range(0,20):
        x = ptList[n][0]
        y = -.5
        xaxisPoints = Text(Point(x+.5,y),xaxisPoint)
        xaxisPoints.setOutline('white')
        xaxisPoints.draw(win)
        xaxisPoint += 1

    # write the program name in the window of the game simulation screen
    progName = Text(Point(10,21),'Battleship')
    progName.setOutline('white')
    progName.setFace('courier')
    progName.setStyle('bold')
    progName.setSize(22)
    progName.draw(win)

    return ptList, win

# the function that shoots at the board
def takeShots(ptList, win):

    drawList = []

    # create a list of ships and their grid lengths
    shipSize = [2,3,4,5,6]
    ships = []

    # remove ships out of the shipSize list as they are generated
    # while the shipSize list has more than 0 items in it, run the following
    # to generate each ship:
    while len(shipSize) > 0:
        # Random point
        a = choice(ptList)  # points can only come from inside the graph
        shipChoice = choice(shipSize) # randomly choose from the shipSize list
        x = a[0]                        # and create a beginning point for it
        y = a[1]

        # this part of the program runs while building ships
        buildShips = True
        while buildShips:

            # create a shipNow list to store the points of the ship currently
            # being generated
            shipNow = []
            horVert = choice([0,1]) # choose horizontal or vertical positioning
            xIterator = 0
            yIterator = 0
            if horVert == 0: 
                xIterator = 1
            else:
                yIterator = 1
                
            # create the ship points
            for i in range(shipChoice):
                pt = ((x + (xIterator * i)), (y + (yIterator * i)))
                shipNow.append(pt)

            # check for boundaries
            outOfBounds = False
            for i in range(len(shipNow)):
                if shipNow[i] not in ptList:  #(if any points are off the grid)
                    outOfBounds = True
                    
             # if out of bounds, try again                   
            if outOfBounds:
                buildShips = False
                
            # if not out of bounds, check for ship overlap
            else:
                overL = False
                for i in range(len(ships)):
                        for shipPt in shipNow:
                            if shipPt in ships[i]:  #(if any 2 ships have matching points)
                                overL = True
                                buildShips = False #(if there is overlap, try again)

                # if in bounds with no overlap, append the ship to the ships list
                # and remove that ship from the shipSize list so the next ship can be created
                if not overL:
                    ships.append(shipNow)
                    shipSize.pop(shipSize.index(shipChoice)) 
                else:
                    buildShips = False


    # graph each ship on the grid. 
    for n in range(len(ships)):
        for k in range(len(ships[n])):
            y = ships[n][k][1]
            x = ships[n][k][0]
            boat = Rectangle(Point(x,y),Point((x+1),(y+1)))
            boat.setFill('grey')
            boat.draw(win)
            drawList.append(boat)

    win.autoflush = True
    # create a graphic countdown before shots are fired
    five = Text(Point(2.5,17.5),'5')
    five.setOutline('yellow')
    five.setFace('courier')
    five.setStyle('bold')
    five.setSize(36)
    five.draw(win)
    sleep(.5)
    five.undraw()
    four = Text(Point(4.5,17.5),'4')
    four.setOutline('yellow')
    four.setFace('courier')
    four.setStyle('bold')
    four.setSize(36)
    four.draw(win)
    sleep(.3)
    four.undraw()
    three = Text(Point(6.5,17.5),'3')
    three.setOutline('yellow')
    three.setFace('courier')
    three.setStyle('bold')
    three.setSize(36)
    three.draw(win)
    sleep(.3)
    three.undraw()
    two = Text(Point(8.5,17.5),'2')
    two.setOutline('yellow')
    two.setFace('courier')
    two.setStyle('bold')
    two.setSize(36)
    two.draw(win)
    sleep(.3)
    two.undraw()
    one = Text(Point(10.5,17.5),'1')
    one.setOutline('yellow')
    one.setFace('courier')
    one.setStyle('bold')
    one.setSize(36)
    one.draw(win)
    sleep(.3)
    one.undraw()
    go = Text(Point(14.5,17.5),'Fire!')
    go.setOutline('orange2')
    go.setFace('courier')
    go.setStyle('bold')
    go.setSize(36)
    go.draw(win)
    sleep(.3)
    go.undraw()
    #  Now for the fun part: time to start shooting at these suckers!  :)
    #  This function chooses shots randomly from the existing grid points. Each shot will
    #  either hit a ship or hit the water. Each point will be removed from the
    #  list of grid points as it is used so that it isn't chosen twice.
    #  If a shot hits a ship, that square will generate a graphic image representing fire.
   
    # this part of the program runs while shooting at our ships, until
    # all ships have been sunk

    # set counters to track the number of shots fired. As each is fired, the coordinates are
    # popped from the ptList and a counter is incremented by 1.
    # a counter is set to determine when all the ships have been sunk, which takes
    # a total of 20 hits, because there are 20 ship coordinate points total.
    hits = 0
    misses = 0
    totalShots = 0

    while hits < 20:

        # choose a random target point from the list of grid points
        target = choice(ptList)  # points can only come from inside the graph
        x = target[0]            # randomly choose from the possible shots list
        y = target[1]            # and create a point of impact
                                     
        # check for a direct hit
        directHit = False
        for i in range(len(ships)):
            for shipPt in ships[i]:
                if target == shipPt:  # if impact & any ships have matching points
                    directHit = True
                    
        # if in bounds with no direct hit, increment the misses count
        # and remove that point from the possible shots list so it's not reused.
        # if a shot hits a ship, the point is removed from the possible shots list and
        # the direct hits count is incremented by 1
        if not directHit:
            misses += 1
            ptList.pop(ptList.index(target))
            droplets = Image(Point(x + .5, y + .5),'WaterDrops.gif')
            droplets.draw(win)
            drawList.append(droplets)
        else:
            hits += 1
            ptList.pop(ptList.index(target))
            fire1 = Image(Point(x + .5, y + .5),'pow.gif')
            fire1.draw(win)
            drawList.append(fire1)

                
            directions = ['left','right','up','down'] # if hit, we begin a local search
            while len(directions) > 0:
                
                
                Dir = choice(directions) #  choose a random direction to try
                directions.pop(directions.index(Dir))#  remove it so it can't be tried again
                
                    
                xi = 0  #  set x and y iterators and define directions
                yi = 0
                if Dir == 'left':
                    xi = -1
                elif Dir == 'down':
                    yi = -1
                elif Dir == 'right':
                    xi = 1
                else:
                    yi = 1

                # begin a localized search   
                localized = True
                c = 1  # set a variable to be used with coordinates in the localized search                
                while localized:
                    sleep(.2) # delay the autoflush so it's easier to follow
                    
                    newTarget = (x + (xi * c), y + (yi * c)) # set coordinates of the new target
                    
                    if newTarget not in ptList:
                        break
                                           
                    xnew = newTarget[0]  # set new x and y points for the new target
                    ynew = newTarget[1]

                    # remove the new target from the list of potential target points
                    ptList.pop(ptList.index(newTarget))  
                                   
                    checking = True  # look for other ship points around the hit                   
                    while checking:
                        directHit = False
                        for i in range(len(ships)):
                            for shipPt in ships[i]:
                                if newTarget == shipPt:  
                                    directHit = True
                                    break

                        # draw the new hit in the graphics window                                   
                        if directHit:
                            fire1 = Image(Point(xnew + .5, ynew + .5),'pow.gif')
                            fire1.draw(win)
                            drawList.append(fire1)
                            
                            # once the positioning of the ship is known, the search in the other 2
                            # directions can end, so pop those directions out of the direction list
                            if (Dir == 'left') or (Dir == 'right'):
                                try:
                                    directions.pop(directions.index('up'))
                                except:
                                    pass
                                try:
                                    directions.pop(directions.index('down'))
                                except:
                                    pass
                            else:
                                try:
                                    directions.pop(directions.index('left'))
                                except:
                                    pass
                                try:
                                    directions.pop(directions.index('right'))
                                except:
                                    pass
                            c+=1 # increment the coordinate count so the hits continue down the hull
                            hits += 1 # add to the hit count so that the search ends at 20 hits
                            checking = False
                            
                                   
                        else:
                            try:
                                misses += 1 # keep counting shots taken even if missed for final tally
                                # graph all the misses
                                droplets = Image(Point(xnew + .5, ynew + .5),'WaterDrops.gif')
                                droplets.draw(win)
                                drawList.append(droplets)
                                checking = False
                                localized = False
                            except:
                                pass
    # pause after the final ship is 'sunk' in order for the viewer to ovserve the screen before
    # seeing the final tally of shots taken
    sleep(.5)
    totalShots = hits + misses
    win.autoflush = False
    for n in range(len(drawList)):
        drawList[n].undraw()   
    win.update()
    win.close()
    return totalShots

# create a window for the final tally of shots
def ending(allShots, gameCount):
    
    win = GraphWin("Battleship", 800, 800, autoflush=True)

    # set window coordinates
    win.setCoords(-2, -2, 22, 22)

    # find the total amount of shots taken to sink all ships
    gameEnd = Image(Point(10,10),'ocean.gif')
    gameEnd.draw(win)

    average = int(allShots / gameCount)
    
            
    # write the count of shots taken in the game end window
    end = Text(Point(10,17),'YOU SUNK MY BATTLESHIP!!!')
    end.setOutline('white')
    end.setFace('courier')
    end.setStyle('bold')
    end.setSize(36)
    end.draw(win)
    gameShots = Text(Point(10,5),'Average Shots Taken per Game: ')
    gameShots.setOutline('white')
    gameShots.setFace('courier')
    gameShots.setSize(30)
    gameShots.draw(win)
    points = Text(Point(10,4),average)
    points.setOutline('white')
    points.setFace('courier')
    points.setStyle('bold')
    points.setSize(30)
    points.draw(win)

    # exit window
    click = Text(Point(10,2),'Click to exit simulation')
    click.setOutline('white')
    click.setFace('courier')
    click.setSize(22)
    click.draw(win)
           
    win.getMouse()
    win.close()


# call the program functions
greeting()

gameCount = 1
allShots = 0

while gameCount <= 2:      
    ptList, win = gameWindow()
    totalShots = takeShots(ptList, win)
    allShots += totalShots
    gameCount += 1

ending(allShots, gameCount)

