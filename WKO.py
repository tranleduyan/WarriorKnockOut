import pygame, sys
from pygame.constants import KEYDOWN, KEYUP, K_ESCAPE, K_KP_ENTER, K_LEFT, K_RETURN, K_RIGHT, K_SPACE, MOUSEBUTTONDOWN, NUMEVENTS, QUIT
from pygame.draw import rect
import random
import math
#initialize Pygame
pygame.init()


pause = False
messageIMG = pygame.image.load('images/message.png')
endgameBackground = pygame.image.load('images/endgameBackground.png')
endGame = False

#Create title and Icon
pygame.display.set_caption('Warrior Knock Out')
icon = pygame.image.load('images/gameIcon.png')
pygame.display.set_icon(icon)


score1BirdGIMG= []
score1BirdGX= [80, 110, 140]
score1BirdGY = []
numOfScore1 = 3
score1HollyIMG= []
score1HollyX= [80, 120, 160]
score1HollyY = []
score1GodleIMG= []
score1GodleX= [80, 110, 140]
score1GodleY = []
score1SolDIMG= []
score1SolDX= [80, 110, 140]
score1SolDY = []

score2BirdGIMG=[]
score2BirdGX = [690, 660, 630]
score2BirdGY = []
numOfScore2 = 3
score2HollyIMG=[]
score2HollyX = [690, 650, 610]
score2HollyY = []
score2GodleIMG=[]
score2GodleX = [690, 660, 630]
score2GodleY = []
score2SolDIMG=[]
score2SolDX = [690, 660, 630]
score2SolDY = []


for i in range(numOfScore1):
    score1BirdGIMG.append(pygame.image.load('images/score.png'))
    score1BirdGY.append(60)
    score1HollyIMG.append(pygame.image.load('images/hollyScore.png'))
    score1HollyY.append(60)
    score1GodleIMG.append(pygame.image.load('images/godleScore.png'))
    score1GodleY.append(60)
    score1SolDIMG.append(pygame.image.load('images/solDScore.png'))
    score1SolDY.append(60)
for i in range(numOfScore2):
    score2BirdGIMG.append(pygame.image.load('images/score2.png'))
    score2BirdGY.append(60)
    score2HollyIMG.append(pygame.image.load('images/hollyScore.png'))
    score2HollyY.append(60)
    score2GodleIMG.append(pygame.image.load('images/godleScore2.png'))
    score2GodleY.append(60)
    score2SolDIMG.append(pygame.image.load('images/solDScore2.png'))
    score2SolDY.append(60)

def score1Display(x,y,i):
    if p1_selected_character == "Bird G":
        screen.blit(score1BirdGIMG[i], (x,y))
    elif p1_selected_character == "Holly":
        screen.blit(score1HollyIMG[i], (x,y))
    elif p1_selected_character == "Godle":
        screen.blit(score1GodleIMG[i], (x,y))
    elif p1_selected_character == "Sol D":
        screen.blit(score1SolDIMG[i], (x,y))
def score2Display(x,y,i):
    if p2_selected_character == "Bird G":
        screen.blit(score2BirdGIMG[i], (x,y))
    elif p2_selected_character == "Holly":
        screen.blit(score2HollyIMG[i], (x,y))
    elif p2_selected_character == "Godle":
        screen.blit(score2GodleIMG[i], (x,y))
    elif p2_selected_character == "Sol D":
        screen.blit(score2SolDIMG[i], (x,y))

player1X = 50
player1Y =334

player2X = 620
player2Y = 334

p1_isJump = False
p2_isJump = False
v1 = 9
m1 = 1
v2 = 9
m2 = 1

p1_pushaway_force = 0
p2_pushaway_force = 0
player2_runattackright = False

player2Wins= False
player1Wins = False

clock = pygame.time.Clock()

player1Left = False
player1Right = False
player1FaceLeft = False
player1FaceRight = True
player1_attackState = "ready"
player1AttackRight = False
player1AttackLeft = False
player2Left = False
player2Right = False
player2FaceLeft = True
player2FaceRight = False
player2_attackState = "ready"
player2AttackRight = False
player2AttackLeft = False
p1_current_character = ""
p2_current_character = ""
p1_selected_character = ""
p2_selected_character = ""
p1_attack_damage = 0
p2_attack_damage = 0
p1_defense = 0
p2_defense = 0
walkCount1 = 0
runattackCount1=0
idleCount1 = 0
attackCount1 = 0
walkCount2 = 0
idleCount2 = 0
attackCount2 = 0
runattackCount2 = 0


birdGWalkRight = [pygame.image.load('images/birdG/birdGrunright1.png'), pygame.image.load('images/birdG/birdGrunright2.png'), pygame.image.load('images/birdG/birdGrunright3.png'), pygame.image.load('images/birdG/birdGrunright4.png'), pygame.image.load('images/birdG/birdGrunright5.png'), pygame.image.load('images/birdG/birdGrunright6.png')]
birdGWalkLeft =  [pygame.image.load('images/birdG/birdGrunleft1.png'), pygame.image.load('images/birdG/birdGrunleft2.png'), pygame.image.load('images/birdG/birdGrunleft3.png'), pygame.image.load('images/birdG/birdGrunleft4.png'), pygame.image.load('images/birdG/birdGrunleft5.png'), pygame.image.load('images/birdG/birdGrunleft6.png')]
birdGIdleRight = [pygame.image.load('images/birdG/birdGidleright1.png'), pygame.image.load('images/birdG/birdGidleright2.png'), pygame.image.load('images/birdG/birdGidleright3.png'), pygame.image.load('images/birdG/birdGidleright4.png'), pygame.image.load('images/birdG/birdGidleright5.png')]
birdGIdleLeft = [pygame.image.load('images/birdG/birdGidleleft1.png'), pygame.image.load('images/birdG/birdGidleleft2.png'), pygame.image.load('images/birdG/birdGidleleft3.png'), pygame.image.load('images/birdG/birdGidleleft4.png'), pygame.image.load('images/birdG/birdGidleleft5.png')]
birdGJumpRight = [pygame.image.load('images/birdG/birdGjumpright1.png'), pygame.image.load('images/birdG/birdGjumpright2.png'), pygame.image.load('images/birdG/birdGjumpright3.png')]
birdGJumpLeft = [pygame.image.load('images/birdG/birdGjumpleft1.png'), pygame.image.load('images/birdG/birdGjumpleft2.png'), pygame.image.load('images/birdG/birdGjumpleft3.png')]
birdGAttackRight =[pygame.image.load('images/birdG/birdGattackright1.png'), pygame.image.load('images/birdG/birdGattackright2.png'), pygame.image.load('images/birdG/birdGattackright3.png'), pygame.image.load('images/birdG/birdGattackright4.png')]
birdGAttackLeft = [pygame.image.load('images/birdG/birdGattackleft1.png'), pygame.image.load('images/birdG/birdGattackleft2.png'), pygame.image.load('images/birdG/birdGattackleft3.png'), pygame.image.load('images/birdG/birdGattackleft4.png')]

hollyWalkRight = [pygame.image.load('images/Holly/hollyrunright1.png'), pygame.image.load('images/Holly/hollyrunright2.png'), pygame.image.load('images/Holly/hollyrunright3.png'), pygame.image.load('images/Holly/hollyrunright4.png'), pygame.image.load('images/Holly/hollyrunright5.png'), pygame.image.load('images/Holly/hollyrunright6.png')]
hollyWalkLeft = [pygame.image.load('images/Holly/hollyrunleft1.png'), pygame.image.load('images/Holly/hollyrunleft2.png'), pygame.image.load('images/Holly/hollyrunleft3.png'), pygame.image.load('images/Holly/hollyrunleft4.png'), pygame.image.load('images/Holly/hollyrunleft5.png'), pygame.image.load('images/Holly/hollyrunleft6.png')]
hollyIdleRight = [pygame.image.load('images/Holly/hollyidleright1.png'), pygame.image.load('images/Holly/hollyidleright2.png'), pygame.image.load('images/Holly/hollyidleright3.png'), pygame.image.load('images/Holly/hollyidleright4.png'), pygame.image.load('images/Holly/hollyidleright5.png')]
hollyIdleLeft = [pygame.image.load('images/Holly/hollyidleleft1.png'), pygame.image.load('images/Holly/hollyidleleft2.png'), pygame.image.load('images/Holly/hollyidleleft3.png'), pygame.image.load('images/Holly/hollyidleleft4.png'), pygame.image.load('images/Holly/hollyidleleft5.png')]
hollyAttackRight = [pygame.image.load('images/Holly/hollyattackright1.png'), pygame.image.load('images/Holly/hollyattackright2.png'), pygame.image.load('images/Holly/hollyattackright3.png'), pygame.image.load('images/Holly/hollyattackright4.png'), pygame.image.load('images/Holly/hollyattackright5.png')]
hollyAttackLeft = [pygame.image.load('images/Holly/hollyattackleft1.png'), pygame.image.load('images/Holly/hollyattackleft2.png'), pygame.image.load('images/Holly/hollyattackleft3.png'), pygame.image.load('images/Holly/hollyattackleft4.png'), pygame.image.load('images/Holly/hollyattackleft5.png')]
hollyRunAttackRight = [pygame.image.load('images/Holly/hollyrunattackright1.png'), pygame.image.load('images/Holly/hollyrunattackright2.png'), pygame.image.load('images/Holly/hollyrunattackright3.png'), pygame.image.load('images/Holly/hollyrunattackright4.png'), pygame.image.load('images/Holly/hollyrunattackright5.png'), pygame.image.load('images/Holly/hollyrunattackright6.png')]

godleWalkRight = [pygame.image.load('images/Godle/godlerunright1.png'), pygame.image.load('images/Godle/godlerunright2.png'), pygame.image.load('images/Godle/godlerunright3.png'), pygame.image.load('images/Godle/godlerunright4.png'), pygame.image.load('images/Godle/godlerunright5.png'), pygame.image.load('images/Godle/godlerunright6.png')]
godleWalkLeft =  [pygame.image.load('images/Godle/godlerunleft1.png'), pygame.image.load('images/Godle/godlerunleft2.png'), pygame.image.load('images/Godle/godlerunleft3.png'), pygame.image.load('images/godle/godlerunleft4.png'), pygame.image.load('images/Godle/godlerunleft5.png'), pygame.image.load('images/Godle/godlerunleft6.png')]
godleIdleRight = [pygame.image.load('images/Godle/godleidleright1.png'), pygame.image.load('images/Godle/godleidleright2.png'), pygame.image.load('images/Godle/godleidleright3.png'), pygame.image.load('images/Godle/godleidleright4.png'), pygame.image.load('images/Godle/godleidleright5.png')]
godleIdleLeft = [pygame.image.load('images/Godle/godleidleleft1.png'), pygame.image.load('images/Godle/godleidleleft2.png'), pygame.image.load('images/Godle/godleidleleft3.png'), pygame.image.load('images/Godle/godleidleleft4.png'), pygame.image.load('images/Godle/godleidleleft5.png')]
godleAttackRight =[pygame.image.load('images/Godle/godleattackright1.png'), pygame.image.load('images/Godle/godleattackright2.png'), pygame.image.load('images/Godle/godleattackright3.png'), pygame.image.load('images/Godle/godleattackright4.png')]
godleAttackLeft = [pygame.image.load('images/Godle/godleattackleft1.png'), pygame.image.load('images/Godle/godleattackleft2.png'), pygame.image.load('images/Godle/godleattackleft3.png'), pygame.image.load('images/Godle/godleattackleft4.png')]

solDWalkRight = [pygame.image.load('images/SolD/solDrunright1.png'), pygame.image.load('images/SolD/solDrunright2.png'), pygame.image.load('images/SolD/solDrunright3.png'), pygame.image.load('images/SolD/solDrunright4.png'), pygame.image.load('images/SolD/solDrunright5.png'), pygame.image.load('images/SolD/solDrunright6.png')]
solDWalkLeft =  [pygame.image.load('images/SolD/solDrunleft1.png'), pygame.image.load('images/SolD/solDrunleft2.png'), pygame.image.load('images/SolD/solDrunleft3.png'), pygame.image.load('images/SolD/solDrunleft4.png'), pygame.image.load('images/SolD/solDrunleft5.png'), pygame.image.load('images/SolD/solDrunleft6.png')]
solDIdleRight = [pygame.image.load('images/SolD/solDidleright1.png'), pygame.image.load('images/SolD/solDidleright2.png'), pygame.image.load('images/SolD/solDidleright3.png'), pygame.image.load('images/SolD/solDidleright4.png'), pygame.image.load('images/SolD/solDidleright5.png')]
solDIdleLeft = [pygame.image.load('images/SolD/solDidleleft1.png'), pygame.image.load('images/SolD/solDidleleft2.png'), pygame.image.load('images/SolD/solDidleleft3.png'), pygame.image.load('images/SolD/solDidleleft4.png'), pygame.image.load('images/SolD/solDidleleft5.png')]
solDAttackRight =[pygame.image.load('images/SolD/solDattackright1.png'), pygame.image.load('images/SolD/solDattackright2.png'), pygame.image.load('images/SolD/solDattackright3.png'), pygame.image.load('images/SolD/solDattackright4.png')]
solDAttackLeft = [pygame.image.load('images/SolD/solDattackleft1.png'), pygame.image.load('images/SolD/solDattackleft2.png'), pygame.image.load('images/SolD/solDattackleft3.png'), pygame.image.load('images/SolD/solDattackleft4.png')]


#background
backgroundAnimation=[pygame.image.load('images/background1.png'), pygame.image.load('images/background2.png'), pygame.image.load('images/background3.png'), pygame.image.load('images/background4.png'), pygame.image.load('images/background5.png')]
backgroundMenu = pygame.image.load('images/background.png')
backgroundCount = 0
def backgroundAnimate():
    global backgroundCount
    screen.blit(backgroundAnimation[backgroundCount // 10], (0,0))
    backgroundCount += 1
    if backgroundCount + 1 >= 50:
        backgroundCount = 0

battleBackgroundIMG = [pygame.image.load('images/battlegroundbackground1.png'), pygame.image.load('images/battlegroundbackground2.png')]
platformBackgroundIMG = [pygame.image.load('images/platform_battleground1.png'), pygame.image.load('images/platform_battleground2.png')]
battleRandomNum = 0
numOfBattleBackground = 2
currentbattleBackground = ""
def battleBackground(x,y):
        if  battleRandomNum == 0:
            screen.blit(battleBackgroundIMG[0], (x,y))
            screen.blit(platformBackgroundIMG[0], (0,400))
        elif battleRandomNum == 1:
            screen.blit(battleBackgroundIMG[1], (x,y))
            screen.blit(platformBackgroundIMG[1], (0,400))

birdGPopUp = False
hollyPopUp = False
godlePopUp = False

selectionBackground= pygame.image.load('images/selectionBackground.png')
birdGSelectionIMG = pygame.image.load('images/BirdGSelection.png')
birdGSelectionX = 50
birdGSelectionY = 170
hollySelectionIMG  = pygame.image.load('images/HollySelection.png')
hollySelectionX = birdGSelectionX + 180
hollySelectionY = 170
godleSelectionIMG = pygame.image.load('images/GodleSelection.png')
godleSelectionX = hollySelectionX + 180
godleSelectionY = 170
solDSelectionIMG = pygame.image.load('images/SolDSelection.png')
solDSelectionX = godleSelectionX + 180
solDSelectionY = 170

birdG_HP = 200
p1_birdG_currentHP = 200
p1_holly_currentHP = 220
p1_godle_currentHP = 120
p1_solD_currentHP = 150
p2_holly_currentHP = 220
p2_birdG_currentHP = 200
p2_godle_currentHP = 120
p2_solD_currentHP = 150
birdG_ATK = 15
birdG_DEF = 30
holly_HP = 220
holly_ATK = 10
holly_DEF = 25
godle_HP = 120
godle_ATK = 25
godle_DEF = 10
solD_HP = 150
solD_ATK = 20
solD_DEF = 20

p1_birdGStatsIcon = pygame.image.load('images/birdG/P1_birdGIcon.png')
p2_birdGStatsIcon = pygame.image.load('images/birdG/p2_birdGIcon.png')

p1_hollyStatsIcon = pygame.image.load('images/Holly/P1_hollyIcon.png')
p2_hollyStatsIcon = pygame.image.load('images/Holly/P2_hollyIcon.png')

p1_godleStatsIcon = pygame.image.load('images/Godle/P1_godleIcon.png')
p2_godleStatsIcon = pygame.image.load('images/Godle/P2_godleIcon.png')

p1_solDStatsIcon = pygame.image.load('images/SolD/P1_solDIcon.png')
p2_solDStatsIcon = pygame.image.load('images/SolD/P2_solDIcon.png')

def isCollision (x1, y1, x2, y2):
    distance = math.sqrt((math.pow((x1-x2), 2)) + (math.pow((y1-y2),2)))
    if distance <63:
        return True
    else: 
        return False
def birdGSelection(x, y):
    screen.blit(birdGSelectionIMG, (x, y))
def hollySelection(x,y):
    screen.blit(hollySelectionIMG, (x,y))   
def godleSelection(x,y):
    screen.blit(godleSelectionIMG, (x,y)) 
def solDSelection(x,y):
    screen.blit(solDSelectionIMG, (x,y))
def displayFinalSelection():
    if p1_current_character == "Bird G":
        drawText('HP - ' + str(birdG_HP), font, (255, 255, 255), screen, 80, 390)
        drawText('ATK - ' + str(birdG_ATK), font, (255, 255, 255), screen,80, 420)
        drawText('DEF - ' + str(birdG_DEF), font, (255, 255, 255), screen, 80, 450)
    if p1_current_character == "Holly":
        drawText('HP - ' + str(holly_HP), font, (255, 255, 255), screen, 80, 390)
        drawText('ATK - ' + str(holly_ATK), font, (255, 255, 255), screen, 80, 420)
        drawText('DEF - ' + str(holly_DEF), font, (255, 255, 255), screen, 80, 450)
    if p1_current_character == "Godle":
        drawText('HP - ' + str(godle_HP), font, (255, 255, 255), screen, 80, 390)
        drawText('ATK - ' + str(godle_ATK), font, (255, 255, 255), screen, 80, 420)
        drawText('DEF - ' + str(godle_DEF), font, (255, 255, 255), screen, 80, 450)
    if p1_current_character == "Sol D":
        drawText('HP - ' + str(solD_HP), font, (255, 255, 255), screen, 80, 390)
        drawText('ATK - ' + str(solD_ATK), font, (255, 255, 255), screen, 80, 420)
        drawText('DEF - ' + str(solD_DEF), font, (255, 255, 255), screen, 80, 450)

    if p2_current_character == "Bird G":
        drawText('HP - ' + str(birdG_HP), font, (255, 255, 255), screen, 620, 390)
        drawText('ATK - ' + str(birdG_ATK), font, (255, 255, 255), screen,620, 420)
        drawText('DEF - ' + str(birdG_DEF), font, (255, 255, 255), screen, 620, 450)
    if p2_current_character == "Holly":
        drawText('HP - ' + str(holly_HP), font, (255, 255, 255), screen, 620, 390)
        drawText('ATK - ' + str(holly_ATK), font, (255, 255, 255), screen, 620, 420)
        drawText('DEF - ' + str(holly_DEF), font, (255, 255, 255), screen, 620, 450)
    if p2_current_character == "Godle":
        drawText('HP - ' + str(godle_HP), font, (255, 255, 255), screen, 620, 390)
        drawText('ATK - ' + str(godle_ATK), font, (255, 255, 255), screen, 620, 420)
        drawText('DEF - ' + str(godle_DEF), font, (255, 255, 255), screen, 620, 450)
    if p2_current_character == "Sol D":
        drawText('HP - ' + str(solD_HP), font, (255, 255, 255), screen, 620, 390)
        drawText('ATK - ' + str(solD_ATK), font, (255, 255, 255), screen, 620, 420)
        drawText('DEF - ' + str(solD_DEF), font, (255, 255, 255), screen, 620, 450)
#selection bool for 2 player 
p1 = False
p2 = False
#arrow initialize
startGame = False  

arrow1 = pygame.image.load("images/arrowSelection.png")
arrow1X = 50 
arrow1Y = 209
arrow1X_change = 0
arrow1Y_change = 0
screenWidth = 500
arrow = []
arrowX =[]
arrowY = []
arrowX_change = []
arrowY_change = []
numOfArrow = 2
arrow1MoveRight = False
arrow2MoveRight = False
arrow1MoveLeft = False
arrow2MoveLeft = False
for i in range(numOfArrow):
    arrow.append(pygame.image.load('images/arrowSelection.png'))
    arrowX.append(birdGSelectionX + 55)
    arrowY.append(birdGSelectionY - 55)
    arrowX_change.append(0)
    arrowY_change.append(0)
def selectionArrow(x,y, i):
    global birdGPopUp, hollyPopUp, godlePopUp
    screen.blit(arrow[i], (x,y))
   
#create Screen
screen = pygame.display.set_mode((800,500))

#button Image
start_IMG = pygame.image.load('images/startButton.png').convert_alpha()

#draw Text
menufont = pygame.font.Font('Minecraft.ttf', 50)
versusFont = pygame.font.Font('Minecraft.ttf', 80)
font = pygame.font.Font('Minecraft.ttf', 20)
damageFont = pygame.font.Font('Minecraft.ttf', 10)
def drawText(text, font, color, surface, x, y):
    textObj = font.render(text, 1, color) 
    textRect = textObj.get_rect()
    textRect.topleft = (x,y)
    surface.blit(textObj, textRect)

#create mainmenu
click = False
def mainMenu():

    global arrowX
    global arrowY, birdG_HP, p1_birdG_currentHP, p2_birdG_currentHP, p1_godle_currentHP, p2_godle_currentHP, p1_holly_currentHP, p2_holly_currentHP, \
        player1X, player1Y, player2X, player2Y, p1_solD_currentHP, p2_solD_healthbarX, p2_solD_currentHP
    global player1Wins,p1, p2, player2Wins, player1FaceRight, player1FaceLeft, player2FaceLeft, player2FaceRight, p1_selected_character, p2_selected_character, p1_current_character, p2_current_character
    global v1, m1, v2, m2
    v1 = 9
    m1 = 1
    v2 = 9
    m2 = 1
    birdG_HP = 200
    p1_birdG_currentHP = 200
    p2_birdG_currentHP = 200
    p1_holly_currentHP = 220
    p2_holly_currentHP = 220
    p1_godle_currentHP = 120
    p2_godle_currentHP = 120
    p1_solD_currentHP = 150
    p2_solD_currentHP = 150
    player1X = 50
    player1Y =334
    p1_selected_character=""
    p2_selected_character=""
    p1_current_character=""
    p2_current_character=""
    player2X = 620
    player2Y = 334
    player1FaceRight = True
    player2FaceLeft = True
    player1FaceLeft = False
    player2FaceRight =False
    player1Wins = False
    player2Wins = False
    p1 = True
    p2 = False
    while True:
        screen.fill((0,0,0))
        backgroundAnimate()
        #start_button.draw()
        drawText('WARRIOR', menufont, (0, 0, 0), screen, 300, 23)
        drawText('WARRIOR', menufont, (255, 255, 255), screen, 295, 20)
        drawText('KNOCK OUT', menufont, (0, 0, 0), screen, 278, 103)
        drawText('KNOCK OUT', menufont, (255, 255, 255), screen, 273, 100)
        drawText('PRESS ENTER TO CONTINUE!', font, (0, 0, 0), screen, 278, 479)
        drawText('PRESS ENTER TO CONTINUE!', font, (255, 255, 255), screen, 275, 477)
        drawText('\'IN A LAND, NO ONE HAS EVER', font, (0, 0, 0), screen, 48, 187)
        drawText(' STEP ON, THE LAND OF MARTIALS', font, (0, 0, 0), screen, 48, 217)
        drawText(' WHERE ONLY ONE CAN HOLD', font, (0, 0, 0), screen, 48, 247)
        drawText(' THE SECRET... OF SHOHKU.', font, (0, 0, 0), screen, 48, 277)
        drawText(' ONE HAS TO FIGHT!\'', font, (0, 0, 0), screen, 48, 307)
        drawText('\'IN A LAND, NO ONE HAS EVER', font, (255, 255, 255), screen, 45, 185)
        drawText(' STEP ON, THE LAND OF MARTIALS', font, (255, 255, 255), screen, 45, 215)
        drawText(' WHERE ONLY ONE CAN HOLD', font, (255, 255, 255), screen, 45, 245)
        drawText(' THE SECRET... OF SHOHKU.', font, (255, 255, 255), screen, 45, 275)
        drawText(' ONE HAS TO FIGHT!\'', font, (255, 255, 255), screen, 45, 305)
        drawText('[ESC]: HELP', font, (0,0,0), screen, 673, 26)
        drawText('[ESC]: HELP', font, (255,255,255), screen, 670, 23)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    help()
            if event.type == KEYUP:
                if event.key == K_RETURN:
                    selectionBoard()
        pygame.display.update()
finishSelection = False
p2_healthbar = pygame.draw.rect(screen,(0,0,0), pygame.Rect(0,0,0,0),0,0,0,0)
p2_birdG_healthbarX = 532
p2_holly_healthbarX = 512
p2_godle_healthbarX = 613
p2_solD_healthbarX = 582
def redraw():
    global runattackCount1, runattackCount2,p2_healthbar,walkCount1, idleCount1, walkCount2, idleCount2, attackCount1, attackCount2, player1_attackState, player2_attackState
    battleBackground(0,0)
    drawText("P2", font, (255,255,255), screen, player2X + 40, player2Y - 35 )
    drawText("P1", font, (255,255,255), screen, player1X + 40, player1Y - 35 )

    if pause:
        pygame.draw.rect(screen, (0,0, 0), pygame.Rect(295,173, 220, 70),0,0,0,0)
        drawText("PAUSE", menufont, (255,255, 255), screen, 326, 190)

    if p1_selected_character == "Bird G":
        for i in range(numOfScore1):
            score1Display(score1BirdGX[i], score1BirdGY[i], i)
    elif p1_selected_character == "Holly":
        for i in range(numOfScore1):
            score1Display(score1HollyX[i], score1HollyY[i], i)
    elif p1_selected_character == "Godle":
        for i in range(numOfScore1):
            score1Display(score1GodleX[i], score1GodleY[i], i)
    elif p1_selected_character == "Sol D":
        for i in range(numOfScore1):
            score1Display(score1SolDX[i], score1SolDY[i], i)
    if p2_selected_character == "Bird G":
        for i in range(numOfScore2):
            score2Display(score2BirdGX[i], score2BirdGY[i], i)
    elif p2_selected_character == "Holly":
        for i in range(numOfScore2):
            score2Display(score2HollyX[i], score2HollyY[i], i)
    elif p2_selected_character == "Godle":
        for i in range(numOfScore2):
            score2Display(score2GodleX[i], score2GodleY[i], i)
    elif p2_selected_character == "Sol D":
        for i in range(numOfScore2):
            score2Display(score2SolDX[i], score2SolDY[i],i)
    if p1_selected_character == "Bird G":
        pygame.draw.rect(screen, (255,255, 255), pygame.Rect(67,26, birdG_HP + 5, 30),0,5,0,5)
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(67,31, p1_birdG_currentHP, 20), 0,5,0,5)
        screen.blit(p1_birdGStatsIcon, (12, 10))
    elif p1_selected_character == "Holly":
        pygame.draw.rect(screen, (255,255, 255), pygame.Rect(67,26, holly_HP + 5, 30),0,5,0,5)
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(67,31, p1_holly_currentHP, 20), 0,5,0,5)
        screen.blit(p1_hollyStatsIcon, (12, 10))
    elif p1_selected_character == "Godle":
        pygame.draw.rect(screen, (255,255, 255), pygame.Rect(68,26, godle_HP + 5, 30),0,5,0,5)
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(68,31, p1_godle_currentHP, 20), 0,5,0,5)
        screen.blit(p1_godleStatsIcon, (12, 10))
    elif p1_selected_character == "Sol D":
        pygame.draw.rect(screen, (255,255, 255), pygame.Rect(68,26, solD_HP + 5, 30),0,5,0,5)
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(68,31, p1_solD_currentHP, 20), 0,5,0,5)
        screen.blit(p1_solDStatsIcon, (12, 10))
    
    if p2_selected_character== "Bird G":
        pygame.draw.rect(screen, (255,255, 255), pygame.Rect(527,26, birdG_HP +5, 30),0,5,5,0)
        p2_healthbar = pygame.draw.rect(screen, (0,0,0), pygame.Rect(p2_birdG_healthbarX,31, p2_birdG_currentHP, 20), 0,5,5,0)
        screen.blit(p2_birdGStatsIcon, (728, 10))
    elif p2_selected_character== "Holly":
        pygame.draw.rect(screen, (255,255, 255), pygame.Rect(507,26, holly_HP +5, 30),0,5,5,0)
        p2_healthbar = pygame.draw.rect(screen, (0,0,0), pygame.Rect(p2_holly_healthbarX,31, p2_holly_currentHP, 20), 0,5,5,0)
        screen.blit(p2_hollyStatsIcon, (728, 10))
    elif p2_selected_character== "Godle":
        pygame.draw.rect(screen, (255,255, 255), pygame.Rect(608,26, godle_HP +5, 30),0,5,5,0)
        p2_healthbar = pygame.draw.rect(screen, (0,0,0), pygame.Rect(p2_godle_healthbarX,31, p2_godle_currentHP, 20), 0,5,5,0)
        screen.blit(p2_godleStatsIcon, (728, 10))
    elif p2_selected_character== "Sol D":
        pygame.draw.rect(screen, (255,255, 255), pygame.Rect(577,26, solD_HP +5, 30),0,5,5,0)
        p2_healthbar = pygame.draw.rect(screen, (0,0,0), pygame.Rect(p2_solD_healthbarX,31, p2_solD_currentHP, 20), 0,5,5,0)
        screen.blit(p2_solDStatsIcon, (728, 10))
    if p1_selected_character == "Bird G":
        if walkCount1 + 1 >= 18:
            walkCount1 = 0
        if runattackCount1 + 1>=18:
            runattackCount1 = 0
        if idleCount1 +1 >=15:
            idleCount1 = 0
        if attackCount1 + 1 >=12:
            player1_attackState = "ready"
            attackCount1 = 0
        if player1_attackState == "ready":
            if player1Left:
                screen.blit(birdGWalkLeft[walkCount1//3], (player1X, player1Y))
                walkCount1 += 1
            elif player1Right:
                screen.blit(birdGWalkRight[walkCount1//3], (player1X, player1Y))
                walkCount1 += 1
            if player1FaceRight and player1Right == False and player1Left == False:
                screen.blit(birdGIdleRight[idleCount1//3], (player1X, player1Y))
                idleCount1 += 1 
            elif player1FaceLeft and player1Left == False and player1Right == False:
                screen.blit(birdGIdleLeft[idleCount1//3], (player1X, player1Y))
                idleCount1 +=1
        if player1_attackState == "attack":
            if player1AttackRight:
                screen.blit(birdGAttackRight[attackCount1//3], (player1X, player1Y))
                attackCount1+= 1 
            if player1AttackLeft:
                screen.blit(birdGAttackLeft[attackCount1//3], (player1X, player1Y))
                attackCount1 +=1
    
    if p1_selected_character == "Holly":
        if walkCount1 + 1 >= 18:
            walkCount1 = 0
        if idleCount1 +1 >=15:
            idleCount1 = 0
        if attackCount1 + 1 >=12:
            player1_attackState = "ready"
            attackCount1 = 0
        if player1_attackState == "ready":
            if player1Left:
                screen.blit(hollyWalkLeft[walkCount1//3], (player1X, player1Y))
                walkCount1 += 1
            elif player1Right:
                screen.blit(hollyWalkRight[walkCount1//3], (player1X, player1Y))
                walkCount1 += 1
            if player1FaceRight and player1Right == False and player1Left == False:
                screen.blit(hollyIdleRight[idleCount1//3], (player1X, player1Y))
                idleCount1 += 1 
            elif player1FaceLeft and player1Left == False and player1Right == False:
                screen.blit(hollyIdleLeft[idleCount1//3], (player1X, player1Y))
                idleCount1 +=1
        if player1_attackState == "attack":
            if player1AttackRight:
                screen.blit(hollyAttackRight[attackCount1//3], (player1X, player1Y))
                attackCount1+= 1 
            if player1AttackLeft:
                screen.blit(hollyAttackLeft[attackCount1//3], (player1X, player1Y))
                attackCount1 +=1
    
    if p1_selected_character == "Godle":
        if walkCount1 + 1 >= 18:
            walkCount1 = 0
        if runattackCount1 + 1>=18:
            runattackCount1 = 0
        if idleCount1 +1 >=15:
            idleCount1 = 0
        if attackCount1 + 1 >=12:
            player1_attackState = "ready"
            attackCount1 = 0
        if player1_attackState == "ready":
            if player1Left:
                screen.blit(godleWalkLeft[walkCount1//3], (player1X, player1Y))
                walkCount1 += 1
            elif player1Right:
                screen.blit(godleWalkRight[walkCount1//3], (player1X, player1Y))
                walkCount1 += 1
            if player1FaceRight and player1Right == False and player1Left == False:
                screen.blit(godleIdleRight[idleCount1//3], (player1X, player1Y))
                idleCount1 += 1 
            elif player1FaceLeft and player1Left == False and player1Right == False:
                screen.blit(godleIdleLeft[idleCount1//3], (player1X, player1Y))
                idleCount1 +=1
        if player1_attackState == "attack":
            if player1AttackRight:
                screen.blit(godleAttackRight[attackCount1//3], (player1X, player1Y))
                attackCount1+= 1 
            if player1AttackLeft:
                screen.blit(godleAttackLeft[attackCount1//3], (player1X, player1Y))
                attackCount1 +=1
    
    if p1_selected_character == "Sol D":
        if walkCount1 + 1 >= 18:
            walkCount1 = 0
        if runattackCount1 + 1>=18:
            runattackCount1 = 0
        if idleCount1 +1 >=15:
            idleCount1 = 0
        if attackCount1 + 1 >=12:
            player1_attackState = "ready"
            attackCount1 = 0
        if player1_attackState == "ready":
            if player1Left:
                screen.blit(solDWalkLeft[walkCount1//3], (player1X, player1Y))
                walkCount1 += 1
            elif player1Right:
                screen.blit(solDWalkRight[walkCount1//3], (player1X, player1Y))
                walkCount1 += 1
            if player1FaceRight and player1Right == False and player1Left == False:
                screen.blit(solDIdleRight[idleCount1//3], (player1X, player1Y))
                idleCount1 += 1 
            elif player1FaceLeft and player1Left == False and player1Right == False:
                screen.blit(solDIdleLeft[idleCount1//3], (player1X, player1Y))
                idleCount1 +=1
        if player1_attackState == "attack":
            if player1AttackRight:
                screen.blit(solDAttackRight[attackCount1//3], (player1X, player1Y))
                attackCount1+= 1 
            if player1AttackLeft:
                screen.blit(solDAttackLeft[attackCount1//3], (player1X, player1Y))
                attackCount1 +=1

    if p2_selected_character == "Bird G":
        if walkCount2 + 1 >= 18:
            walkCount2 = 0
        if idleCount2 +1 >=15:
            idleCount2 = 0
        if attackCount2 +1 >=12:
            player2_attackState = "ready"
            attackCount2 = 0
        if player2_attackState == "ready":
            if player2Left:
                screen.blit(birdGWalkLeft[walkCount2//3], (player2X, player2Y))
                walkCount2 += 1
            elif player2Right:
                screen.blit(birdGWalkRight[walkCount2//3], (player2X, player2Y))
                walkCount2 += 1
            if player2FaceRight and player2Right == False and player2Left == False:
                screen.blit(birdGIdleRight[idleCount2//3], (player2X, player2Y))
                idleCount2 += 1 
            elif player2FaceLeft and player2Left == False and player2Right == False:
                screen.blit(birdGIdleLeft[idleCount2//3], (player2X, player2Y))
                idleCount2 +=1

        if player2_attackState == "attack":
            if player2AttackRight:
                screen.blit(birdGAttackRight[attackCount2//3], (player2X, player2Y))
                attackCount2 += 1 
            if player2AttackLeft:
                screen.blit(birdGAttackLeft[attackCount2//3], (player2X, player2Y))
                attackCount2 +=1


    if p2_selected_character == "Holly":
        if walkCount2 + 1 >= 18:
            walkCount2 = 0
        if idleCount2 +1 >=15:
            idleCount2 = 0
        if attackCount2 +1 >=12:
            player2_attackState = "ready"
            attackCount2 = 0
        if player2_attackState == "ready":
            if player2Left:
                screen.blit(hollyWalkLeft[walkCount2//3], (player2X, player2Y))
                walkCount2 += 1
            elif player2Right:
                screen.blit(hollyWalkRight[walkCount2//3], (player2X, player2Y))
                walkCount2 += 1
            if player2FaceRight and player2Right == False and player2Left == False:
                screen.blit(hollyIdleRight[idleCount2//3], (player2X, player2Y))
                idleCount2 += 1 
            elif player2FaceLeft and player2Left == False and player2Right == False:
                screen.blit(hollyIdleLeft[idleCount2//3], (player2X, player2Y))
                idleCount2 +=1

        if player2_attackState == "attack":
            if player2AttackRight:
                screen.blit(hollyAttackRight[attackCount2//3], (player2X, player2Y))
                attackCount2 += 1 
            if player2AttackLeft:
                screen.blit(hollyAttackLeft[attackCount2//3], (player2X, player2Y))
                attackCount2 +=1
            if player2_runattackright:
                screen.blit(hollyRunAttackRight[runattackCount2//3], (player2X, player2Y))
    
    if p2_selected_character == "Godle":
        if walkCount2 + 1 >= 18:
            walkCount2 = 0
        if idleCount2 +1 >=15:
            idleCount2 = 0
        if attackCount2 +1 >=12:
            player2_attackState = "ready"
            attackCount2 = 0
        if player2_attackState == "ready":
            if player2Left:
                screen.blit(godleWalkLeft[walkCount2//3], (player2X, player2Y))
                walkCount2 += 1
            elif player2Right:
                screen.blit(godleWalkRight[walkCount2//3], (player2X, player2Y))
                walkCount2 += 1
            if player2FaceRight and player2Right == False and player2Left == False:
                screen.blit(godleIdleRight[idleCount2//3], (player2X, player2Y))
                idleCount2 += 1 
            elif player2FaceLeft and player2Left == False and player2Right == False:
                screen.blit(godleIdleLeft[idleCount2//3], (player2X, player2Y))
                idleCount2 +=1

        if player2_attackState == "attack":
            if player2AttackRight:
                screen.blit(godleAttackRight[attackCount2//3], (player2X, player2Y))
                attackCount2 += 1 
            if player2AttackLeft:
                screen.blit(godleAttackLeft[attackCount2//3], (player2X, player2Y))
                attackCount2 +=1
    
    if p2_selected_character == "Sol D":
        if walkCount2 + 1 >= 18:
            walkCount2 = 0
        if idleCount2 +1 >=15:
            idleCount2 = 0
        if attackCount2 +1 >=12:
            player2_attackState = "ready"
            attackCount2 = 0
        if player2_attackState == "ready":
            if player2Left:
                screen.blit(solDWalkLeft[walkCount2//3], (player2X, player2Y))
                walkCount2 += 1
            elif player2Right:
                screen.blit(solDWalkRight[walkCount2//3], (player2X, player2Y))
                walkCount2 += 1
            if player2FaceRight and player2Right == False and player2Left == False:
                screen.blit(solDIdleRight[idleCount2//3], (player2X, player2Y))
                idleCount2 += 1 
            elif player2FaceLeft and player2Left == False and player2Right == False:
                screen.blit(solDIdleLeft[idleCount2//3], (player2X, player2Y))
                idleCount2 +=1

        if player2_attackState == "attack":
            if player2AttackRight:
                screen.blit(solDAttackRight[attackCount2//3], (player2X, player2Y))
                attackCount2 += 1 
            if player2AttackLeft:
                screen.blit(solDAttackLeft[attackCount2//3], (player2X, player2Y))
                attackCount2 +=1

    if endGame:
        drawText("K", menufont, (0,0,0), screen, 375, 240)
        drawText("K", menufont, (255,0,0), screen, 370, 235)
        drawText(".O", menufont, (0,0,0), screen, 410, 240)
        drawText(".O", menufont, (255,103,0), screen, 405, 235)
        pygame.display.update()
        pygame.time.wait(2000)
        end()
    pygame.display.update()
def selectionBoard():

    global p1, p2, arrow1MoveRight, arrow2MoveRight, arrow2MoveLeft, arrow1MoveLeft, godlePopUp, hollyPopUp, birdGPopUp
    global birdGSelectionY, hollySelectionY, godleSelectionY, solDSelectionY
    global p1_current_character, p2_current_character, p1_selected_character, p2_selected_character
    global birdG_HP, holly_HP, godle_HP, solD_HP
    global finishSelection, battleRandomNum, startGame
    p1 = True
    p2 = False
    running = True
    p1_selected_character=""
    p2_selected_character=""
    p1_current_character=""
    p2_current_character=""
    for i in range(numOfArrow):
        arrow.append(pygame.image.load('images/arrowSelection.png'))
        arrowX.append(birdGSelectionX + 55)
        arrowY.append(birdGSelectionY - 55)
        arrowX_change.append(0)
        arrowY_change.append(0)
    while running:
        screen.fill((0,0,0))
        screen.blit(selectionBackground, (0,0))
        drawText('PLAYER SELECT', menufont, (255,255,255), screen, 205, 30)
        drawText('P1 - ' + p1_current_character, font, (255, 255, 255), screen, 80, 350)
        drawText('P2 - ' + p2_current_character, font, (255,255,255), screen, 620, 350)
        birdGSelection(birdGSelectionX, birdGSelectionY)
        hollySelection(hollySelectionX, hollySelectionY)
        godleSelection(godleSelectionX, godleSelectionY)
        solDSelection(solDSelectionX, solDSelectionY)
        displayFinalSelection()

        for i in range(numOfArrow):
            selectionArrow(arrowX[i],arrowY[i],i)
            if p1:
                if i == 0:
                    if arrowX[i] == 105:
                        birdGSelectionY = 160
                        hollySelectionY = 170
                        godleSelectionY = 170
                        solDSelectionY = 170
                        p1_current_character = "Bird G"
                    elif arrowX[i] == 285:
                        hollySelectionY = 160
                        birdGSelectionY = 170
                        godleSelectionY = 170 
                        solDSelectionY = 170
                        p1_current_character = "Holly"
                    elif arrowX[i] == 465:
                        godleSelectionY = 160
                        birdGSelectionY = 170
                        hollySelectionY = 170
                        solDSelectionY = 170
                        p1_current_character = "Godle"
                    elif arrowX[i] == 645:
                        solDSelectionY = 160
                        godleSelectionY = 170
                        birdGSelectionY = 170
                        hollySelectionY = 170
                        p1_current_character = "Sol D"
                    if arrowX[i] < 105:
                        arrowX[i] = 645
                    if arrowX[i] > 645:
                        arrowX[i] = 105
            if p2:
                if i == 1:
                    if arrowX[i] == 105:
                        birdGSelectionY = 160
                        hollySelectionY = 170
                        godleSelectionY = 170
                        solDSelectionY = 170
                        p2_current_character = "Bird G"
                    elif arrowX[i] == 285:
                        hollySelectionY = 160
                        birdGSelectionY = 170
                        godleSelectionY = 170 
                        solDSelectionY = 170
                        p2_current_character = "Holly"
                    elif arrowX[i] == 465:
                        godleSelectionY = 160
                        birdGSelectionY = 170
                        hollySelectionY = 170
                        solDSelectionY = 170
                        p2_current_character = "Godle"
                    elif arrowX[i] == 645:
                        solDSelectionY = 160
                        godleSelectionY = 170
                        birdGSelectionY = 170
                        hollySelectionY = 170
                        p2_current_character = "Sol D"
                    if arrowX[i] < 105:
                        arrowX[i] = 645
                    if arrowX[i] > 645:
                        arrowX[i] = 105


                    
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    mainMenu()
                if event.key == K_RIGHT:
                    for i in range(numOfArrow):
                        if p1:
                            if i == 0:
                                arrowX[i] += 180
                                print(arrowX[i])
                                print(i)
                        if p2:
                            if i == 1:
                                arrowX[i] += 180
                                print(arrowX[i])
                if event.key == K_LEFT:
                    for i in range(numOfArrow):
                        if p1:
                            if i == 0:
                                arrowX[i] -= 180
                                print(arrowX[i])
                        if p2:
                            if i == 1:
                                arrowX[i] -= 180
                                print(arrowX[i])
            if event.type == KEYUP:
                if event.key == K_RETURN:
                    if p1:
                        p1= False
                        p2 = True
                        p1_selected_character = p1_current_character
                        print('helo')
                    elif p2:
                        p2_selected_character = p2_current_character
                        p2 = False
                        finishSelection = True

        if finishSelection:
            drawText('VS.', versusFont, (255,255,255), screen, 350, 375)
            pygame.display.update()
            pygame.time.wait(2000)
            game()

        pygame.display.update()
def game():
    global battleRandomNum, player1X, player1Y, player2X, player2Y, p1_isJump, p2_isJump, v1, v2, m1,\
         m2, player1Left, player1Right, player2Left,player2Right, player2FaceLeft, player2FaceRight, player2Right, walkCount, player1FaceLeft, player1FaceRight
    battleRandomNum = random.randint(0,1)
    global finishSelection, p2_birdG_healthbarX, p2_godle_healthbarX, p2_godle_currentHP, walkCount2, walkCount1, player1AttackLeft, player1_attackState, player1AttackLeft, player1AttackRight
    global endGame,player2AttackLeft, player2_attackState, player2AttackRight,p1_birdG_currentHP,p2_birdG_currentHP, p2_attack_damage,p1_attack_damage, p1_defense, p2_defense
    global p1_godle_currentHP,p1_pushaway_force,p2_pushaway_force,player2_runattackright,numOfScore1, player2Wins, numOfScore2, player1Wins, p1_holly_currentHP,p1_selected_character, p2_selected_character, p1_current_character, p2_current_character, p2_holly_currentHP, p2_holly_healthbarX
    global p1_solD_currentHP, p2_solD_healthbarX, p2_solD_currentHP, pause
    running = True
    endGame = False
    finishSelection = False
    numOfScore1 = 3
    numOfScore2 = 3

    for i in range(numOfArrow):
        arrowX[i] = 105
    while running:
        if p2_selected_character == "Bird G" and endGame == False and pause == False:
            p2_attack_damage = random.randint(1,15)
            p2_defense = (p1_attack_damage * 30)/100
            p2_pushaway_force = random.randint(15,40)
        elif p2_selected_character == "Holly" and endGame == False and pause == False:
            p2_attack_damage = random.randint(1,10)
            p2_defense = (p1_attack_damage * 25)/100
            p2_pushaway_force = random.randint(10,35)
        elif p2_selected_character == "Godle" and endGame == False and pause == False:
            p2_attack_damage = random.randint(1,25)
            p2_defense = (p1_attack_damage * 10)/100
            p2_pushaway_force = random.randint(25,35)
        elif p2_selected_character == "Sol D" and endGame == False and pause == False:
            p2_attack_damage = random.randint(1,20)
            p2_defense = (p1_attack_damage * 20)/100
            p2_pushaway_force = random.randint(20, 30)
        else:
            p2_attack_damage = 0
            p2_defense = 0
        if p1_selected_character == "Bird G" and endGame == False and pause == False:
            p1_attack_damage = random.randint(1,15)
            p1_defense = (p2_attack_damage * 30)/100
            p1_pushaway_force = random.randint(15,40)
        elif p1_selected_character == "Holly" and endGame == False and pause == False:
            p1_attack_damage = random.randint(1,10)
            p1_defense = (p2_attack_damage * 25)/100
            p1_pushaway_force = random.randint(10,35)
        elif p1_selected_character == "Godle" and endGame == False and pause == False:
            p1_attack_damage = random.randint(1,25)
            p1_defense = (p2_attack_damage * 10)/100
            p1_pushaway_force = random.randint(25,35)
        elif p1_selected_character == "Sol D" and endGame == False and pause == False:
            p1_attack_damage = random.randint(1,20)
            p1_defense =(p2_attack_damage *20)/100
            p2_pushaway_force = random.randint(20,30)
        else:
            p1_attack_damage = 0
            p1_defense = 0
        keys = pygame.key.get_pressed()
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    if endGame == False and pause == False:
                        pause = True
                    elif endGame == False and pause == True:
                        pause = False
        if endGame == False and pause == False:
            if keys[pygame.K_LEFT]:
                if p2_selected_character == "Godle":
                    player2X -=10
                    player2FaceLeft = True
                    player2FaceRight = False
                    player2Left = True
                    player2Right = False
                else: 
                    player2X -=8
                    player2FaceLeft = True
                    player2FaceRight = False
                    player2Left = True
                    player2Right = False
            elif keys[pygame.K_RIGHT]:
                if p2_selected_character == "Godle":
                    player2X+= 10
                    player2FaceLeft = False
                    player2FaceRight = True
                    player2Left = False
                    player2Right = True
                else:
                    player2X+= 8
                    player2FaceLeft = False
                    player2FaceRight = True
                    player2Left = False
                    player2Right = True
            else:
                player2Right = False
                player2Left = False
                walkCount2 = 0
            if keys[pygame.K_j] or keys[pygame.K_l]:
                player2_attackState = "attack"
                if player2FaceRight:
                    player2AttackRight = True
                    player2AttackLeft = False
                if player2FaceLeft:
                    player2AttackLeft = True
                    player2AttackRight = False
        if endGame == False and pause == False:
            if keys[pygame.K_a]:
                if p1_selected_character == "Godle":
                    player1X -=10
                    player1FaceLeft = True
                    player1FaceRight = False
                    player1Left = True
                    player1Right = False
                else:
                    player1X -=8
                    player1FaceLeft = True
                    player1FaceRight = False
                    player1Left = True
                    player1Right = False
            elif keys[pygame.K_d]:
                if p1_selected_character == "Godle":
                    player1X += 10
                    player1FaceLeft = False
                    player1FaceRight = True
                    player1Left = False
                    player1Right = True
                else:
                    player1X += 8
                    player1FaceLeft = False
                    player1FaceRight = True
                    player1Left = False
                    player1Right = True
            else:
                player1Right = False
                player1Left = False
                walkCount1 = 0
            if keys[pygame.K_SPACE]:
                player1_attackState = "attack"
                if player1FaceRight:
                    player1AttackRight = True
                    player1AttackLeft = False
                if player1FaceLeft:
                    player1AttackRight = False
                    player1AttackLeft = True
        if not(p2_isJump) and endGame == False:
                if keys[pygame.K_UP]:
                    p2_isJump = True
                    player2Right = False
                    player2Left = False
                    walkCount2 = 0
        elif p2_isJump and endGame == False and pause == False:

            if v2 >= -9:
                m2 = 1
                if v2 < 0:
                    m2 = -1
                F2 = (1/2) * m2 * (v2**2)
                player2Y -= F2
                v2 -= 1
            else: 
                p2_isJump = False
                v2 = 9
        if not(p1_isJump) and endGame == False and pause == False:
                if keys[pygame.K_w]:
                    p1_isJump = True
                    player1Right = False
                    player1Left = False
                    walkCount1 = 0
        elif p1_isJump and endGame == False and pause == False:
            if v1 >= -9:
                m1 = 1
                if v1 < 0:
                    m1 = -1
                F1 = (1/2) * m1 * (v1**2)
                player1Y -= F1
                v1 -= 1
            else: 
                p1_isJump = False
                v1 = 9
            #pygame.time.delay(15)
        if player1X >=722:
            player1X = 722
        if player1X <= -18:
            player1X = -18
        if player2X >=722:
            player2X = 722
        if player2X <= -18:
            player2X = -18
        
        if player1_attackState == "attack" and endGame == False and pause == False:
            attackPlayer2Collision = isCollision(player1X, player1Y, player2X, player2Y)
            if attackPlayer2Collision:
                if player1FaceRight:
                    if p2_selected_character == "Bird G":
                        player2X += p1_pushaway_force
                        temp = p1_attack_damage - p2_defense
                        p2_birdG_currentHP -= (temp)
                        p2_birdG_healthbarX += temp
                    elif p2_selected_character == "Holly":
                        player2X += p1_pushaway_force
                        temp = p1_attack_damage - p2_defense
                        p2_holly_currentHP -= (temp)
                        p2_holly_healthbarX += temp
                    elif p2_selected_character == "Godle":
                        player2X += p1_pushaway_force
                        temp = p1_attack_damage - p2_defense
                        p2_godle_currentHP -= (temp)
                        p2_godle_healthbarX += temp
                    elif p2_selected_character == "Sol D":
                        player2X += p1_pushaway_force
                        temp = p1_attack_damage - p2_defense
                        p2_solD_currentHP -= (temp)
                        p2_solD_healthbarX += temp
                if player1FaceLeft:
                    if p2_selected_character == "Bird G":
                        player2X -= p1_pushaway_force
                        temp = p1_attack_damage - p2_defense
                        p2_birdG_currentHP -= (temp)
                        p2_birdG_healthbarX += temp
                    elif p2_selected_character == "Holly":
                        player2X -= p1_pushaway_force
                        temp = p1_attack_damage - p2_defense
                        p2_holly_currentHP -= (temp)
                        p2_holly_healthbarX += temp
                    elif p2_selected_character == "Godle":
                        player2X -= p1_pushaway_force
                        temp = p1_attack_damage - p2_defense
                        p2_godle_currentHP -= (temp)
                        p2_godle_healthbarX += temp
                    elif p2_selected_character == "Sol D":
                        player2X -= p1_pushaway_force
                        temp = p1_attack_damage - p2_defense
                        p2_solD_currentHP -= (temp)
                        p2_solD_healthbarX += temp
        if player2_attackState == "attack" and endGame == False and pause == False:
            attackPlayer1Collision = isCollision(player1X, player1Y, player2X, player2Y)
            if attackPlayer1Collision:
                if player2FaceRight:
                    if p1_selected_character == "Bird G":
                        player1X += p2_pushaway_force
                        p1_birdG_currentHP -= (p2_attack_damage - p1_defense)
                    elif p1_selected_character == "Holly":
                        player1X += p2_pushaway_force
                        p1_holly_currentHP -= (p2_attack_damage - p1_defense)
                    elif p1_selected_character == "Godle":
                        player1X += p2_pushaway_force
                        p1_godle_currentHP -= (p2_attack_damage - p1_defense)
                    elif p1_selected_character == "Sol D":
                        player1X += p2_pushaway_force
                        p1_solD_currentHP -= (p2_attack_damage - p1_defense)
                if player2FaceLeft:
                    if p1_selected_character == "Bird G":
                        player1X -= p2_pushaway_force
                        p1_birdG_currentHP -= (p2_attack_damage - p1_defense)
                    elif p1_selected_character == "Holly":
                        player1X -= p2_pushaway_force
                        p1_holly_currentHP -= (p2_attack_damage - p1_defense)
                    elif p1_selected_character == "Godle":
                        player1X -= p2_pushaway_force
                        p1_godle_currentHP -= (p2_attack_damage - p1_defense)
                    elif p1_selected_character == "Sol D":
                        player1X -= p2_pushaway_force
                        p1_solD_currentHP -= (p2_attack_damage - p1_defense)
        if p1_selected_character == "Bird G" and endGame == False and pause == False:
            if p1_birdG_currentHP <= 0:
                numOfScore1 -= 1
                p1_birdG_currentHP = 200
        elif p1_selected_character == "Holly" and endGame == False and pause == False:
            if p1_holly_currentHP <= 0:
                numOfScore1 -= 1
                p1_holly_currentHP = 220
        elif p1_selected_character == "Godle" and endGame == False and pause == False:
            if p1_godle_currentHP <= 0:
                numOfScore1 -= 1
                p1_godle_currentHP = 120
        elif p1_selected_character == "Sol D" and endGame == False and pause == False:
            if p1_solD_currentHP <= 0:
                numOfScore1 -= 1
                p1_solD_currentHP = 150
        if p2_selected_character == "Bird G" and endGame == False and pause == False:
            if p2_birdG_currentHP <=0:
                numOfScore2 -= 1
                p2_birdG_currentHP = 200
                p2_birdG_healthbarX =532
        elif p2_selected_character == "Holly" and endGame == False and pause == False:
            if p2_holly_currentHP <=0:
                numOfScore2 -= 1
                p2_holly_currentHP = 220
                p2_holly_healthbarX = 512
        elif p2_selected_character == "Godle" and endGame == False and pause == False:
            if p2_godle_currentHP <=0:
                numOfScore2 -= 1
                p2_godle_currentHP = 120
                p2_godle_healthbarX = 613
        elif p2_selected_character == "Sol D" and endGame == False and pause == False:
            if p2_solD_currentHP <=0:
                numOfScore2 -= 1
                p2_solD_currentHP = 150
                p2_solD_healthbarX = 593
        if numOfScore1 <=0:
            endGame = True
            player2Wins=True
        elif numOfScore2 <=0:
            endGame = True
            player1Wins=True
        clock.tick(30)
        redraw()
def end():
        running = True
        global player2Wins, player1Wins
        global endGame 
        while running:
            screen.fill((0,0,0))
            screen.blit(endgameBackground, (0,0))
            screen.blit(messageIMG, (135, 150))
            drawText('PRESS ENTER TO CONTINUE!', font, (0, 0, 0), screen, 273, 310)
            drawText('PRESS ENTER TO CONTINUE!', font, (255, 255, 255), screen, 276, 312)
            if player2Wins:
                drawText('WINNER: PLAYER 2', menufont, (0,0,0), screen, 175, 205)
            elif player1Wins:
                drawText('WINNER: PLAYER 1', menufont, (0,0,0), screen, 175, 205)
            
            for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == KEYUP:
                            if event.key == K_RETURN:
                                mainMenu()
            pygame.display.update()
up_IMG=pygame.image.load('images/instruction_UP.png')
left_IMG = pygame.image.load('images/instruction_LEFT.png')
right_IMG = pygame.image.load('images/instruction_RIGHT.png')
space_IMG = pygame.image.load('images/instruction_SPACE.png')
w_IMG=pygame.image.load('images/instruction_W.png')
a_IMG = pygame.image.load('images/instruction_A.png')
d_IMG=pygame.image.load('images/instruction_D.png')
j_IMG=pygame.image.load('images/instruction_J.png')
def help():
    running = True
    while running:
        screen.fill((0,0,0))
        drawText('INSTRUCTIONS', versusFont, (255,255,255), screen, 105, 20)
        drawText('PLAYER 1', menufont, (255, 255, 255), screen, 285, 110)
        screen.blit(up_IMG, (300, 170))
        screen.blit(left_IMG, (175, 170))
        screen.blit(right_IMG, (425,170))
        screen.blit(j_IMG, (550, 170))
        drawText('PLAYER 2', menufont, (255, 255, 255), screen, 285, 300)
        screen.blit(w_IMG, (300, 370))
        screen.blit(a_IMG, (175, 370))
        screen.blit(d_IMG, (425,370))
        screen.blit(space_IMG, (550,370))
        for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            running = False
        pygame.display.update()
mainMenu()