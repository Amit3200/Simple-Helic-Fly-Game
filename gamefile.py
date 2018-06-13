import pygame
import time
from random import randint

#python recognizes the color codes in the rgba
black=(0,0,0)
white=(255,255,255)


pygame.init()

surfacewidth = 1000
surfaceheight = 600
imageheight = 45
imagewidth = 101
surface = pygame.display.set_mode((surfacewidth,surfaceheight)) #This generates the display for the game
pygame.display.set_caption('Helicopter') #title for the game
clock=pygame.time.Clock() #Sets the game state

img=pygame.image.load("Helic1.png")#this saves lot of time to not to waste memory



def score(count):
    font= pygame.font.Font("freesansbold.ttf",20)
    text = font.render("Score: "+str(count),True,white)
    surface.blit(text,[0,0])



#makes the obstacles draw two blocks
def blocks(x_block,y_block,block_width,block_height,gap):
    pygame.draw.rect(surface,white,[x_block,y_block,block_width,block_height])#block size
    pygame.draw.rect(surface,white,[x_block,y_block+block_height+gap,block_width,surfaceheight])#block size it should be down and the gap should be there
    






#replay or quit the game
def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN,pygame.KEYUP,pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            continue
        
        return event.key

    return None

#generates or creates the text Object Renders it
def makeTextObjs(text,font):
    textSurface = font.render(text,True,white)
    return textSurface,textSurface.get_rect()



#message surface show the text
def msgSurface(text):
    surfacewidth = 1000
    surfaceheight = 600
    smallText = pygame.font.Font("freesansbold.ttf",20)
    largeText = pygame.font.Font("freesansbold.ttf",150)
    titleTextSurf,titleTextRect = makeTextObjs(text,largeText)
    titleTextRect.center = surfacewidth/2,surfaceheight/2
    surface.blit(titleTextSurf,titleTextRect)
    
    typTextSurf,typTextRect = makeTextObjs('Press any key to continue',smallText)
    typTextRect.center = surfacewidth/2,((surfaceheight/2)+100)
    surface.blit(typTextSurf,typTextRect)

    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() == None:
        clock.tick()
    main()
        

#function to gameover
def gameOver():
    msgSurface("Kaboom!")
    pygame.quit()
    quit()




#functions here like for the helicopter
def helicopter(x,y,image):
    surface.blit(image,(x,y)) #put the image at the coordinate at x,y
    

def main():
    #add x we move right and add y we move downwards graphics coordinate
    x = 150
    y = 200

    y_move = 0 #initial movement of helicopter
    #helicpter sets up
    game_over =  False #Constant to stop the game

    x_block = surfacewidth
    y_block = 0
    block_width = 75 #block width
    block_height = randint(0,surfaceheight/2)
    gap = imageheight*3
    block_move = 5
    current_score = 0

    #game loop
    while game_over!= True:
        for event in pygame.event.get(): #All kind of event like what keys are pressed and where is the mouse
            if event.type == pygame.QUIT: #x in window will quit
                game_over=True

            if event.type == pygame.KEYDOWN: #key is pressed
                if event.key == pygame.K_UP: #upward key
                    y_move = -5 # negative 5 is upward movement

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 5 # downwards

        y += y_move
        
        surface.fill(black) # fill the surface with the color
        helicopter(x,y,img) #order matters after black you get the helicopter
        score(current_score)
        blocks(x_block,y_block,block_width,block_height,gap)

        
        x_block-=block_move
        #before update so that we can check the notes
        if y>surfaceheight-20 or y<-30:
            gameOver()

        if x_block<(-1*block_width):
            x_block=surfacewidth
            block_height=randint(0,surfaceheight/2)

        #logic for obstacles
        if x+imagewidth > x_block:
            if x < x_block+block_width:
               #print("Possible within the boundaries of x")
                if y<block_height:
                    #print("Y Crossover Upper")
                    if x-imagewidth<block_width+x_block:
                        print("GAME OVER")
                        gameOver()
        if x+imagewidth>x_block:
            #print("x crossover")
            if y+imageheight>block_height+gap:
                #print("y crossover")
                if x<block_width+x_block:
                    gameOver()

        print(x,x_block,x_block-block_move)
        if x<=x_block and x>=x_block-block_move:
            current_score+=1
            print(current_score)
            
        
        pygame.display.update() # will update the display specific area in the game if no parameter the whole window else particular area and display.flip() updates whole thing
        clock.tick(60) # will be 60 fps game

main()
pygame.quit()
quit()
