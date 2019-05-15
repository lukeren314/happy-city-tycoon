import pygame, math, random, time, textwrap, gc, operator, json
#from pygame.locals import *
#window constants
GAME_NAME = "Happy City Tycoon"
WIDTH = 1600
HEIGHT = 900
SCREEN_SIZE = (WIDTH,HEIGHT)

#window dimensions
FRAME_WIDTH = 1000
FRAME_HEIGHT = 900
FRAME_DIMENSIONS = (FRAME_WIDTH,FRAME_HEIGHT)
CITY_WIDTH = 2000
CITY_HEIGHT = 2000
CITY_DIMENSIONS = (CITY_WIDTH,CITY_HEIGHT)
CITY_BORDER = 20
CITY_LEFT = WIDTH-FRAME_WIDTH
CITY_RECTANGLE = (CITY_LEFT,0,FRAME_WIDTH,FRAME_HEIGHT)
SCROLL_WIDTH = FRAME_WIDTH*FRAME_WIDTH/CITY_WIDTH
GENERAL_BORDER = 5
CITIZEN_WIDTH = 15
CITIZEN_HEIGHT = 15
THECAT_WIDTH = 120
THECAT_HEIGHT = 134
#game initialization
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(GAME_NAME)
icon_img = pygame.image.load("data/icon2.png")
icon_img.set_colorkey((0,255,0))
pygame.display.set_icon(icon_img)
__file__ = "Atom Projects"

clock = pygame.time.Clock()

#colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
pink = (255,130,255)
brown = (150,70,20)
grey = (128,128,128)
yellow = (255,255,0)
orange = (255,70,0)
cyan = (0,255,255)
purple = (255,0,255)
indigo = (111,0,255)
violet = (160,0,255)
forestgreen = (34,139,34)
greenyellow = (173,255,47)

#images handler
def load(fileN):
    return pygame.image.load("data/"+fileN)

#gun_img = load("gun.png")
#cherry_img = load("cherry.png")
#cupcake_img = load("cupcake.png")
#star_img = load("star.png")
#cloud_img = load("cloud.png")
#watermelon_img = load("watermelon.png")
#background_img = load("background.png")
#thecat_img = load("thecat.png")
#textbox_img = load("textbox.png")
#grass_img = load("grass.png")
#cathead_img = load("cathead.png")
#button_img = load("button.png")
#cathouse_img = load("cathouse.png")
#kittyhall_img = load("kittyhall.png")
#kittizen_img = load("kittizen.png")
#bank_img = load("bank.png")
#kittymall_img = load("kittymall.png")
#library_img = load("library.png")
#cultcircle_img = load("cultcircle.png")
#fill_img = load("fill.png")
#icon_img = load("icon2.png")
#clock_img = load("Clock.png")

#font constants
pygame.font.init()
FONT_SIZE = 20
SMALL_SIZE = 10
TITLE_SIZE = 120
BUTTON_SIZE = 25
TEXT_MARGIN = FONT_SIZE*1.5
TEXT_WRAP = 50

MAIN_FONT = 'data/CHERI.TTF'
TITLE_FONT = 'data/Happy_brown_cat_shadow.ttf'

default_font = pygame.font.Font(MAIN_FONT,FONT_SIZE)
small_font = pygame.font.Font(MAIN_FONT,SMALL_SIZE)
title_font = pygame.font.Font(TITLE_FONT,TITLE_SIZE)
button_font = pygame.font.Font(MAIN_FONT,BUTTON_SIZE)

#ui constants
STATUS_BAR_WIDTH = CITY_LEFT-TEXT_MARGIN*2
STATUS_BAR_HEIGHT = 10
MINI_BAR_HEIGHT = 100
STATUS_BAR_X = GENERAL_BORDER
STATUS_BAR_Y = THECAT_HEIGHT+TEXT_MARGIN
STATUS_BAR_COORDINATES = (GENERAL_BORDER,THECAT_HEIGHT+TEXT_MARGIN)
CLOCK_X = CITY_LEFT-100-GENERAL_BORDER
CLOCK_Y = CITY_BORDER+TEXT_MARGIN*2+GENERAL_BORDER
#in_game constants
COMMAND_RANGE = 300
HOUSE_LIMIT = 5
DAY_LENGTH = 2000
EFFECT_RANGE = 50
EFFECT_TIME = 50
EFFECT_COOLDOWN = 300
LENGTH_OF_LOAN = 3
MESSAGE_LENGTH = 100
SECONDS_PER_CYCLE = 60
OVERALL_LIMIT = 700
MAX_EMOTION = 25
#status bar indexes
#["Population","Capital","Happiness","FEAR","Awareness","Violence","Innovation","Mutant"]
POPULATION = 0
CAPITAL = 1
HAPPINESS = 2
AWARENESS = 3
FEAR = 4
VIOLENCE = 5
INNOVATION = 6
MUTANT = 7

#event names
GAME_STARTED = 0
BUILDING_ADDED = 1
BUILDING_REMOVED = 2
STATUS_CHANGE = 3
NEW_DAY = 4
NEW_NIGHT = 5
TIER_1_EMOTION_ADDED = 6
TIER_2_EMOTION_ADDED = 7
BUILDING_LIMIT = 8
BUILDING_STATUS = 9
TAX_COLLECTED = 10
BROKE = 11
FUNCTION_BROKE = 12
KITTIZEN_ADDED = 13
KITTIZEN_REMOVED = 14
INQUIRY = 15
ACHIEVEMENT = 16
FUNCTION_ADDED = 17
SAVED_SUCCESSFULLY = 18
LOADED_SUCCESSFULLY = 19
LOAD_ERROR = 20
#building types
KITTY_HALL = 0
HOUSE = 1
BANK = 2
KITTY_MALL = 3
SHRINE = 4
SCHOOL = 5
LABORATORY = 6
DOJO = 7
PRISON = 8
LIBRARY = 9
KITTIZEN = 100
COMMAND_BLOCK = 101
CULT_CIRCLE = 102
FOOD_TRUCK = 103
PROPAGANDA_POSTER = 104
VIDEO_VISION = 105
ENRAGED_KITTIZEN = 106
BALL_OF_YARN = 107
RIOT = 108
CAT_EXPERIMENT = 109
CULTIST = 110
POLICE = 111
THUG = 112
ROBBER = 113
PROTECTOR = 114
GUARD = 115
DARK_SPIRIT = 116
INVADER = 117
KUNG_FU_WARRIOR = 118
MYSTERIOUS_WARRIOR = 119
RUNAWAY_PRISONER = 120
HAPPINESS_MACHINE = 121
MUTATION = 122
victory_image = load("fill.png")
# names = {KITTY_HALL:"Kitty Hall",
#         HOUSE:"House",
#         BANK:"Bank",
#         KITTY_MALL:"Kitty Mall",
#         SHRINE:"Shrine",
#         SCHOOL:"School",
#         LABORATORY:"Laboratory",
#         DOJO:"Dojo",
#         PRISON:"Prison",
#         LIBRARY:"Library",
#
#         KITTIZEN:"Kittizen",
#         COMMAND_BLOCK:"Command Block",
#         CULT_CIRCLE:"Cult Circle",
#         FOOD_TRUCK:"Food Truck",
#         PROPAGANDA_POSTER:"Propaganda Poster",
#         VIDEO_VISION:"Video Vision",
#         ENRAGED_KITTIZEN:"Enraged Kittizen",
#         BALL_OF_YARN:"Ball of Yarn",
#         RIOT:"Riot",
#         CAT_EXPERIMENT:"Cat Experiment",
#         CULTIST:"Cultist",
#         POLICE:"Police",
#         THUG:"Thug",
#         ROBBER:"Robber",
#         PROTECTOR:"Protector",
#         DARK_SPIRIT:"Dark Spirit",
#         GUARD:"Guard",
#         INVADER:"Invader",
#         KUNG_FU_WARRIOR:"Kung-Fu Warrior",
#         MYSTERIOUS_WARRIOR:"Mysterious Warrior",
#         RUNAWAY_PRISONER:"Runaway Prisoner",
#         HAPPINESS_MACHINE:"Happiness Machine"}
def text(string,coordinates):
    screen.blit(default_font.render(string,True,black),coordinates)
def inBox(coords,rect):
    givenX, givenY = coords
    boxX, boxY, boxWidth, boxHeight = rect
    check = False
    if (givenX >= boxX and givenX <= boxX+boxWidth and givenY >= boxY and givenY <= boxY+boxHeight):
        check = True
    return check

class cmd:
    list_of_commands = ['list','new_day','mode','build','grid','kittizen']
    def parse(user_input):
        words = user_input.split()
        if words == "" or words == "\n" or words == None or not words:
            command = " "
        else:
            command = words[0]      # first word is the command
        parameters = words[1:]    # the rest are parameters for the command
        if command == 'list':
            cmd.c_list()
        elif command == 'new_day':
            cmd.c_new_day()
        elif command == 'mode':
            cmd.c_mode()
        elif command == 'build':
            cmd.c_build(parameters[0])
        elif command == 'grid':
            cmd.c_grid()
        elif command == 'kittizen':
            cmd.c_kittizen()
        elif command == 'num_of_citizens':
            cmd.c_num_of_citizens()
        elif command == 'sus':
            cmd.c_sus(parameters[0])
        elif command == 'new_night':
            cmd.c_new_night()
        elif command == 'add_emotion':
            cmd.c_add_emotion(parameters[0],parameters[1])
        elif command == 'switches':
            cmd.c_switches()
        else:
            print('Command not recognised')
    def c_list():
        for command in cmd.list_of_commands:
            print(command)
    def c_new_day():
        ui.new_day()
    def c_new_night():
        ui.new_night()
    def c_mode():
        print(switch.switches["game_mode"])
    def c_build(buildingID):
        city.buy_building(int(buildingID))
    def c_grid():
        if city.grid:
            print(city.grid)
        else:
            print("No buildings!")
    def c_kittizen():
        city.new_kittizen(pygame.mousd.get_pos())
    def c_add_emotion(emotion,value):
        ui.add_status(int(emotion),int(value))
    def c_switches():
        print(switch.switches)
class switch:
        switches = {"fullscreen":False,
        "gore" : False,
        "music" : False,
        "fps" : True,
        "mind_control" : False,
        "shrine_converted" : False,
        "shrine_upgraded" : False,
        "school_dark_arts" : False,
        "dojo_warriors" : False,
        "research_complete" : False,
        "fully_educated" : False,
        "invasion" : False,
        "propaganda" : False,
        "video_vision" : False,
        "cheats" : False,
        "game_mode" : 0,
        "game_speed" : 1
        }
class achievements:
    images = {
        "Locked":load("locked.png"),
        "Game Over":load("gameover.png"),
        "MUTATE!": load("mutation.png"),
        "Money Ending":load("moneyending.png"),
        "Happy Ending":load("happyending.png"),
        "Awareness Ending":load("awarenessending.png"),
        "Gore Ending":load("goreending.png"),
        "Fear Ending":load("fearending.png"),
        "Violent Ending":load("violentending.png"),
        "Innovation Ending":load("innovationending.png"),
        "Mutant Ending":load("mutantending.png")
    }
    list = {
        "Game Over": False,
        "MUTATE!": False,
        "Money Ending":False,
        "Happy Ending":False,
        "Awareness Ending":False,
        "Gore Ending":False,
        "Fear Ending":False,
        "Violent Ending":False,
        "Innovation Ending":False,
        "Mutant Ending":False
    }
    victory = load("fill.png")
    def add(achievement):
        if not achievements.list[achievement]:
            achievements.list[achievement] = True
            event_handler.add(ACHIEVEMENT,achievement,50)
class _input:
    mouse_left = False
    mouse_right = False
    mouse_middle = False
    x = False
    one = False
    two = False
    three = False
    four = False
class util:
    def mouse_pos():
        return pygame.mouse.get_pos()
    def textwrapped(string,coordinates):
        wrap_num = int(len(string)/TEXT_WRAP)+1
        x,y = coordinates
        for row in range(wrap_num):
            if row < wrap_num - 1:
                screen.blit(default_font.render(string[row*TEXT_WRAP:(row+1)*TEXT_WRAP]+"-",True,black),(x,y+row*TEXT_MARGIN))
            else:
                screen.blit(default_font.render(string[row*TEXT_WRAP:(row+1)*TEXT_WRAP],True,black),(x,y+row*TEXT_MARGIN))
    def text_size(string,size = FONT_SIZE,color = black,font_type = MAIN_FONT,textWrap = TEXT_WRAP,owidth = 0, ocolor = black,screen = screen):
        font = pygame.font.Font(font_type,size)
        nStr = font.render(textwrap.fill(string,textWrap),True,color)
        return (nStr.get_width(),nStr.get_height())
    def centerimg(imgName,coordinates):
        x,y = coordinates
        imgX, imgY = imgName.get_size()
        screen.blit(imgName,(x-imgX/2,y-imgY/2))
    def centertext(text, coordinates, size = FONT_SIZE, color = black, font_type = MAIN_FONT,screen = screen):
        x,y = coordinates
        font = pygame.font.Font(font_type, size)
        text = font.render(text, True, color)
        textWidth = text.get_width()
        screen.blit(text, (x-textWidth/2,y))
    def inBox(givenCoords,rect):
        givenX, givenY = givenCoords
        boxX, boxY, boxWidth, boxHeight = rect
        check = False
        if (givenX >= boxX and givenX <= boxX+boxWidth and givenY >= boxY and givenY <= boxY+boxHeight):
            check = True
        return check

    #shapes
    def rect(color,position,border_width = 0,border_color = black,surface = screen):
        pygame.draw.rect(surface,color,position)
        if border_width != 0:
            pygame.draw.rect(surface,border_color,position,border_width)
class scroller:
    x = 0
    y = 0
    def move():
        dx,dy = pygame.mouse.get_rel()
        if _input.mouse_right and util.inBox(pygame.mouse.get_pos(),CITY_RECTANGLE):
            if scroller.x-dx > SCROLL_WIDTH or scroller.x-dx < 0:
                dx = 0
            if scroller.y-dy > SCROLL_WIDTH or scroller.y-dy < 0:
                dy = 0
            scroller.x -= dx
            scroller.y -= dy
    def translateX():
        return -scroller.x*CITY_WIDTH/FRAME_WIDTH+CITY_LEFT
    def translateY():
        return -scroller.y*CITY_HEIGHT/FRAME_HEIGHT
    def reverseX():
        return -(CITY_LEFT)+scroller.x*CITY_WIDTH/FRAME_WIDTH
    def reverseY():
        return scroller.y*CITY_HEIGHT/FRAME_HEIGHT
    def translateRect(rect):
        x,y,w,h = rect
        return (x+scroller.translateX(),y+scroller.translateY(),w,h)
    def translateCoordinates(coordinates):
        x,y = coordinates
        return (x+scroller.translateX(),y+scroller.translateY())
    def reverseCoordinates(coordinates):
        x,y = coordinates
        return (x+scroller.reverseX(),y+scroller.reverseY())
    def reset():
        scroller.x = 0
        scroller.y = 0
class GameObjects:
    names = {KITTY_HALL:"Kitty Hall",
            HOUSE:"House",
            BANK:"Bank",
            KITTY_MALL:"Kitty Mall",
            SHRINE:"Shrine",
            SCHOOL:"School",
            LABORATORY:"Laboratory",
            DOJO:"Dojo",
            PRISON:"Prison",
            LIBRARY:"Library",

            KITTIZEN:"Kittizen",
            COMMAND_BLOCK:"Command Block",
            CULT_CIRCLE:"Cult Circle",
            FOOD_TRUCK:"Food Truck",
            PROPAGANDA_POSTER:"Propaganda Poster",
            VIDEO_VISION:"Video Vision",
            ENRAGED_KITTIZEN:"Enraged Kittizen",
            BALL_OF_YARN:"Ball of Yarn",
            RIOT:"Riot",
            CAT_EXPERIMENT:"Cat Experiment",
            CULTIST:"Cultist",
            POLICE:"Police",
            THUG:"Thug",
            ROBBER:"Robber",
            PROTECTOR:"Protector",
            DARK_SPIRIT:"Dark Spirit",
            GUARD:"Guard",
            INVADER:"Invader",
            KUNG_FU_WARRIOR:"Kung-Fu Warrior",
            MYSTERIOUS_WARRIOR:"Mysterious Warrior",
            RUNAWAY_PRISONER:"Runaway Prisoner",
            HAPPINESS_MACHINE:"Happiness Machine",
            MUTATION:"Mutant"}
    functions = {KITTY_HALL:{"Destroy":0,"Command":0},
                 HOUSE:{"Destroy":0},
                 BANK:{"Destroy":0,"Collect Taxes":0,"Hire Guard":5,"Bribe Mafia":5},
                 KITTY_MALL:{"Destroy":0,"Give Jobs":10,"Restock":5,"Hold Discounts":0},
                 SHRINE:{"Destroy":0,"Gain Mind Control":10,"Convert":50,"Upgrade Shrine":75},
                 SCHOOL:{"Destroy":0,"Educate":10},
                 LABORATORY:{"Destroy":0,"Research":20},
                 DOJO:{"Destroy":0,"Train":15},
                 PRISON:{"Destroy":0,"Hire Police":10},
                 LIBRARY:{"Destroy":0,"Learn Dark Arts":50,"Read Books":0},

                 KITTIZEN:{"Destroy":0},
                 COMMAND_BLOCK:{"Destroy":0},
                 CULT_CIRCLE:{"Destroy":0},
                 FOOD_TRUCK:{"Destroy":0},
                 PROPAGANDA_POSTER:{"Destroy":0},
                 VIDEO_VISION:{"Destroy":0},
                 ENRAGED_KITTIZEN:{"Destroy":50},
                 BALL_OF_YARN:{"Destroy":0},
                 RIOT:{"Destroy":100},
                 CAT_EXPERIMENT:{"Destroy":0},
                 CULTIST:{"Destroy":20},
                 POLICE:{"Destroy":0},
                 THUG:{},
                 ROBBER:{"Destroy":30},
                 PROTECTOR:{"Destroy":0},
                 DARK_SPIRIT:{},
                 GUARD:{"Destroy":0},
                 INVADER:{},
                 KUNG_FU_WARRIOR:{"Destroy":0},
                 MYSTERIOUS_WARRIOR:{"Destroy":0,"Inquire":100},
                 RUNAWAY_PRISONER:{},
                 HAPPINESS_MACHINE:{"Destroy":0},
                 MUTATION:{"Destroy":0,"Spread Mutation":0}}
    # functions = {KITTY_HALL:["Destroy","Command",None,None],
    #              HOUSE:["Destroy",None,None,None],
    #              BANK:["Destroy","Collect Taxes","Hire Guard","Bribe Mafia"],
    #              KITTY_MALL:["Destroy","Give Jobs","Restock","Hold Discounts"],
    #              SHRINE:["Destroy","Gain Mind Control","Convert",None],
    #              SCHOOL:["Destroy","Educate",None,None],
    #              LABORATORY:["Destroy","Research",None,None],
    #              DOJO:["Destroy","Training",None,None],
    #              PRISON:["Destroy","Hire Police",None,None],
    #              LIBRARY:["Destroy","Learn Dark Arts",None,None],
    #
    #              KITTIZEN:["Destroy",None,None,None],
    #              COMMAND_BLOCK:["Destroy",None,None,None],
    #              CULT_CIRCLE:["Destroy",None,None,None],
    #              FOOD_TRUCK:["Destroy",None,None,None],
    #              PROPAGANDA_POSTER:["Destroy",None,None,None],
    #              VIDEO_VISION:["Destroy",None,None,None],
    #              ENRAGED_KITTIZEN:["Destroy",None,None,None],
    #              BALL_OF_YARN:["Destroy",None,None,None],
    #              RIOT:["Destroy",None,None,None],
    #              CAT_EXPERIMENT:["Destroy",None,None,None],
    #              CULTIST:["Destroy",None,None,None],
    #              POLICE:["Destroy",None,None,None],
    #              THUG:[None,None,None,None],
    #              ROBBER:["Destroy",None,None,None],
    #              PROTECTOR:["Destroy",None,None,None],
    #              DARK_SPIRIT:[None,None,None,None],
    #              GUARD:["Destroy",None,None,None],
    #              INVADER:[None,None,None,None],
    #              KUNG_FU_WARRIOR:["Destroy",None,None,None],
    #              MYSTERIOUS_WARRIOR:["Destroy","Inquire",None,None],
    #              RUNAWAY_PRISONER:[None,None,None,None],
    #              HAPPINESS_MACHINE:["Destroy",None,None,None]}
    dimensions = {
            KITTY_HALL:(300,150),
            HOUSE:(76,76),
            BANK:(126,126),
            KITTY_MALL:(200,200),
            SHRINE:(50,50),
            SCHOOL:(200,100),
            LABORATORY:(100,100),
            DOJO:(120,120),
            PRISON:(80,80),
            LIBRARY:(100,80),

            KITTIZEN:(15,15),
            COMMAND_BLOCK:(15,15),
            CULT_CIRCLE:(76,76),
            FOOD_TRUCK:(30,15),
            PROPAGANDA_POSTER:(50,50),
            VIDEO_VISION:(15,15),
            ENRAGED_KITTIZEN:(15,15),
            BALL_OF_YARN:(15,15),
            RIOT:(75,50),
            CAT_EXPERIMENT:(15,15),
            CULTIST:(15,15),
            POLICE:(15,15),
            THUG:(15,15),
            ROBBER:(15,15),
            PROTECTOR:(15,15),
            DARK_SPIRIT:(15,15),
            GUARD:(15,15),
            INVADER:(60,45),
            KUNG_FU_WARRIOR:(15,15),
            MYSTERIOUS_WARRIOR:(15,15),
            RUNAWAY_PRISONER:(15,15),
            HAPPINESS_MACHINE:(15,15),
            MUTATION:(15,15)}
    images = {KITTY_HALL:load("kittyhall.png"),
              HOUSE:load("cathouse.png"),
              BANK:load("bank.png"),
              KITTY_MALL:load("kittymall.png"),
              SHRINE:load("shrine.png"),
              SCHOOL:load("school.png"),
              LABORATORY:load("laboratory.png"),
              DOJO:load("dojo.png"),
              PRISON:load("prison.png"),
              LIBRARY:load("library.png"),

              KITTIZEN:load("kittizen.png"),
              COMMAND_BLOCK:load("commandblock.png"),
              CULT_CIRCLE:load("cultcircle.png"),
              FOOD_TRUCK:load("foodtruck.png"),
              PROPAGANDA_POSTER:load("propagandaposter.png"),
              VIDEO_VISION:load("videovision.png"),
              ENRAGED_KITTIZEN:load("enragedkittizen.png"),
              BALL_OF_YARN:load("ballofyarn.png"),
              RIOT:load("riot.png"),
              CAT_EXPERIMENT:load("catexperiment.png"),
              CULTIST:load("cultist.png"),
              POLICE:load("police.png"),
              THUG:load("thug.png"),
              ROBBER:load("robber.png"),
              PROTECTOR:load("protector.png"),
              DARK_SPIRIT:load("darkspirit.png"),
              GUARD:load("police.png"),
              INVADER:load("invader.png"),
              KUNG_FU_WARRIOR:load("kungfuwarrior.png"),
              MYSTERIOUS_WARRIOR:load("mysteriouswarrior.png"),
              RUNAWAY_PRISONER:load("runawayprisoner.png"),
              HAPPINESS_MACHINE:load("happinessmachine.png"),
              MUTATION:load("mutant.png")}
    prices = {KITTY_HALL:20,
              HOUSE:10,
              BANK:20,
              KITTY_MALL:30,
              SHRINE:40,
              SCHOOL:40,
              LABORATORY:50,
              LIBRARY:50,
              DOJO:50,
              PRISON:50,
              KITTIZEN:10,
              COMMAND_BLOCK:10,
              CULT_CIRCLE:10,
              FOOD_TRUCK:10,
              PROPAGANDA_POSTER:10,
              VIDEO_VISION:10,
              ENRAGED_KITTIZEN:10,
              BALL_OF_YARN:10,
              RIOT:10,
              CAT_EXPERIMENT:10,
              CULTIST:10}
    descriptions = {KITTY_HALL:"Pun definitely intended.",
                    HOUSE:"Looks cozy.",
                    BANK:"Taking a citizen's hard earned money.",
                    KITTY_MALL:"The best place to buy your favorite kitty goods.",
                    SHRINE:"Call upon The Cat himself.",
                    SCHOOL:"Raising the next generation of dog-fighting kittizens.",
                    LABORATORY:"Perform inhumane cat experiments.",
                    DOJO:"Kat Chop!",
                    PRISON:"Where all the bad kitties go.",
                    LIBRARY:"My favorite authors: J.K. Growling and Charles Kittens.",

                    KITTIZEN:"One of your faithful kittizens",
                    COMMAND_BLOCK:"Cat's love yarn, but they are too lazy to attack it right away.",
                    CULT_CIRCLE:"Get rid of the cultists quick!",
                    FOOD_TRUCK:"Some cats would go crazy over this stuff...",
                    PROPAGANDA_POSTER:"Reminding citizens that they aren't merely in a game.",
                    VIDEO_VISION:"Reminds me of the 80's.",
                    ENRAGED_KITTIZEN:"You don't wanna mess with this guy...",
                    BALL_OF_YARN:"A cat's ultimate weakness.",
                    RIOT:"They look angry...",
                    CAT_EXPERIMENT:"Lets hope this doesn't go horribly wrong...",
                    CULTIST:"I wouldn't mess with these guys.",
                    POLICE:"Stops robbers in the act.",
                    THUG:"You can't mess with this one...",
                    ROBBER:"You better stop him soon!",
                    PROTECTOR:"To remind citizens that they are not in a game...",
                    DARK_SPIRIT:"What have you done.",
                    GUARD:"Basically cheaper, more temporary police.",
                    INVADER:"You can't defeat them alone!",
                    KUNG_FU_WARRIOR:"Your only chance at stopping evil.",
                    MYSTERIOUS_WARRIOR:"You might be able to learn something from him.",
                    RUNAWAY_PRISONER:"Get the police!",
                    HAPPINESS_MACHINE:"The key to happiness, give it a scratch!",
                    MUTATION:"Something looks wrong..."}
class building(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, id_ = 0, coordinates = (0,0),status = 0):
       # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
        self.image = GameObjects.images[id_]

       #define attributes
        self.id_ = id_
        self.name = GameObjects.names[id_]
        self.functions = GameObjects.functions[id_]
        if id_ not in GameObjects.prices:
            self.price = 10
        else:
            self.price = GameObjects.prices[id_]
        self.description = GameObjects.descriptions[id_]
       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.coordinates = coordinates
        self.rect.x,self.rect.y = self.x+scroller.translateX(),self.y+scroller.translateY()
        self.status = status
    def update(self):
        self.rect.x = self.x+scroller.translateX()
        self.rect.y = self.y+scroller.translateY()
        if _input.mouse_left and self.rect.collidepoint(pygame.mouse.get_pos()):
            ui.set_data(self)
            ui.menu_show = True
    def move(self,coords = (0,0)):
        new_coords = coords
        if self.id_ == INVADER:
            if not inBox((self.x,self.y),(CITY_WIDTH/2-250,CITY_HEIGHT/2-250,500,500)):
                angle = math.atan2(CITY_HEIGHT/2-self.y,CITY_WIDTH/2-self.x)
                detector1 = detection((self.x+math.sin(angle)*200,self.y+math.cos(angle)*200),(self.image.get_width(),self.image.get_height()))
                if pygame.sprite.spritecollide(detector1,city.grid,False):
                    for in_the_way in pygame.sprite.spritecollide(detector1,city.grid,False):
                        city.destroy_object(in_the_way)
                self.x,self.y = (self.x+math.sin(angle)*200,self.y+math.cos(angle)*200)
                del detector1
        else:
            if new_coords == (0,0):
                new_coords = city.find_coordinate((self.width,self.height),city.grid)
            else:
                self.x,self.y = new_coords
    def fixed_move(self,coord_range):
        counter = 0
        x,y,w,h = coord_range
        if x < 0:
            x = 0
        if x > CITY_WIDTH-CITIZEN_WIDTH:
            x = CITY_WIDTH-CITIZEN_WIDTH
        if y < 0:
            y = 0
        if y > CITY_HEIGHT-CITIZEN_HEIGHT:
            y = CITY_HEIGHT-CITIZEN_HEIGHT
        new_coord_range = (int(x),int(y),int(w),int(h))
        new_coords = city.find_coordinate((self.width,self.height),city.grid,new_coord_range)
        self.x,self.y = new_coords
    def function(self,option):
        if option == "Destroy" and "Destroy" in GameObjects.functions[self.id_]:
            city.destroy_object(self)
            ui.menu_show = False
        if self.id_ == KITTY_HALL:
            if option == "Command":
                city.buy_building(101)
            if option == "Put up Propaganda" and swtich.propaganda:
                city.buy_building(104)
                ui.add_cat_dialogue("They call me Big Kitty")
            if option == "Install Video Vision" and switch.switches["video_vision"]:
                city.buy_building(105)
                ui.add_cat_dialogue("Watch their every move")
        elif self.id_ == HOUSE:
            if option == "Spawn Cult":
                city.corrupt_building(0,self)
        elif self.id_ == BANK:
            if option == "Collect Taxes":
                emotion_added(CAPITAL,self,-2,2)
            if option == "Hire Guard":
                city.buy_building(GUARD)
            if option == "Bribe Mafia":
                city.buy_building(THUG)
        elif self.id_ == KITTY_MALL:
            if option == "Give Jobs":
                city.emotion_added(CAPITAL,self,2,2)
            if option == "Restock":
                city.buy_building(103)
            if option == "Hold Discounts":
                city.emotion_added(CAPITAL,self,-5)
                city.emtion_added(HAPPINESS,self,5,2)
        elif self.id_ == SHRINE:
            if option == "Gain Mind Control":
                if not switch.switches["mind_control"]:
                    switch.switches["mind_control"] = True
                    building.add_function(KITTIZEN,{"Control Mind":0})
                    ui.menu_show = False
            if option == "Convert":
                if not switch.switches["shrine_converted"]:
                    switch.switches["shrine_converted"] = True
                    building.add_function(HOUSE,{"Spawn Cult":10})
                    ui.menu_show = False
            if option == "Upgrade Shrine":
                if not switch.switches["shrine_upgraded"]:
                    switch.switches["shrine_upgraded"] = True
                    kittizen.add_function(KITTIZEN,{"Become Protector":50})
        elif self.id_ == LIBRARY:
            if option == "Learn Dark Arts":
                if not switch.switches["school_dark_arts"]:
                    switch.switches["school_dark_arts"] = True
                    building.add_function(SCHOOL,{"Teach Dark Arts":50})
            if option == "Read Books":
                city.emotion_added(HAPPINESS,self,2,2)
        elif self.id_ == SCHOOL:
            if option == "Educate":
                city.emotion_added(INNOVATION,self,2,2)
            elif option == "Teach Dark Arts" and switch.switches["school_dark_arts"]:
                city.emotion_added(AWARENESS,self,10,2)
        elif self.id_ == LABORATORY:
            if option == "Research":
                city.buy_building(CAT_EXPERIMENT)
            if option == "Mutate MORE!" and switch.switches["research_complete"]:
                city.emotion_added(MUTANT,self,10,2)
            if option == "Build Happiness Machine" and switch.switches["fully_educated"]:
                city.buy_building(HAPPINESS_MACHINE)
        elif self.id_ == DOJO:
            if option == "Train":
                city.emotion_added(VIOLENCE,self,2,2)
            if option == "Train Warrior" and switch.switches["dojo_warriors"]:
                city.buy_building(KUNG_FU_WARRIOR)
        elif self.id_ == PRISON:
            if option == "Hire Police":
                city.buy_building(POLICE)
        elif self.id_ == MYSTERIOUS_WARRIOR:
            if option == "Inquire":
                if random.randrange(0,5) == 0:
                    switch.switches["dojo_warriors"] = True
                    building.add_function(DOJO,{"Train Warrior":50})
                    ui.add_cat_dialogue("You can train warriors!")
                    event_handler.add(INQUIRY,1,50)
                else:
                    event_handler.add(INQUIRY,0,50)
    def add_function(building_type,function):
        if list(function.keys())[0] not in GameObjects.functions[building_type]:
            GameObjects.functions[building_type].update(function)
            event_handler.add(FUNCTION_ADDED,list(function.keys())[0],50)
            for game_object in city.get_all_of(building_type).sprites():
                if list(function.keys())[0] not in game_object.functions:
                    game_object.functions.update(function)
class kittizen(pygame.sprite.Sprite):
    adjectives = {CAPITAL:"Wealthy",
                    HAPPINESS:"Happy",
                    AWARENESS:"Aware",
                    FEAR:"Safe",
                    VIOLENCE:"Violent",
                    INNOVATION:"Smart",
                    MUTANT:"Weird"}
    names = ["Jim","Fluffers","Snuffy","McPufferson","Quintash","Fred","BigRed","Bunny","Dogo","CatCat",
                "Garfo","Zombo","Gumbi","ChiChi","Choco","Paco","Pato","Hand Sanitizer","breadys","Red",
                "Canine","Giovanni","Thor","Uncle","Aaron","Lil' Slugger", "Yellow","Pikachu","John",
                "Cracker","Steven","Meow"]
    active_emotions = [False,True,True,False,False,False,False]
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, coordinates = (0,0), emotions = [0,10,10,0,0,0,0],name = "N",status = 0,cooldown = False):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = load("kittizen.png")
        self.blank = pygame.Surface((0,0))
        self.id_ = 100
        if name == "N":
            self.name = random.choice(kittizen.names)
        else:
            self.name = name
        self.emotions = emotions
        self.status = status
        self.decription = ""
        self.functions = GameObjects.functions[100]

        self.cooldown = cooldown

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.coordinates = coordinates
        self.rect.x,self.rect.y = self.x+scroller.translateX(),self.y+scroller.translateY()
    def update(self):
        self.rect.x = self.x+scroller.translateX()
        self.rect.y = self.y+scroller.translateY()

        self.status = self.emotions.index(max(self.emotions))
        self.description = "Feeling " + kittizen.adjectives[self.status]

        if _input.mouse_left and self.rect.collidepoint(pygame.mouse.get_pos()) and ui.day_time:
            ui.set_data(self)
            ui.menu_show = True
    def function(self,key):
        if key == 1:
            city.destroy_object(self)
            ui.menu_show = False
        elif key == "Control Mind" and switch.switches["mind_control"]:
            city.buy_building(BALL_OF_YARN)
            ui.selected_kittizen = self
        elif key == "Become Protector" and switch.switches["shrine_upgraded"]:
            city.construct_building(PROTECTOR,(self.x,self.y))
            city.destroy_object(self)
    def move(self,coords = (0,0)):
        new_coords = coords
        if new_coords == (0,0):
            new_coords = city.find_coordinate((CITIZEN_WIDTH,CITIZEN_HEIGHT),city.grid)
        self.x,self.y = new_coords
    def fixed_move(self,coord_range):
        counter = 0
        x,y,w,h = coord_range
        if x < 0:
            x = 0
        if x > CITY_WIDTH-CITIZEN_WIDTH:
            x = CITY_WIDTH-CITIZEN_WIDTH
        if y < 0:
            y = 0
        if y > CITY_HEIGHT-CITIZEN_HEIGHT:
            y = CITY_HEIGHT-CITIZEN_HEIGHT
        new_coord_range = (int(x),int(y),int(w),int(h))
        new_coords = city.find_coordinate((CITIZEN_WIDTH,CITIZEN_HEIGHT),city.grid,new_coord_range)
        self.x,self.y = new_coords
    def emote(self, emotion, value = 2, tier = 1):
        if self.emotions[emotion] + value <= 0:
            city.destroy_object(self)
        elif ui.day_time:
            if tier == 1:
                if emotion == CAPITAL and value < 0:
                    ui.add_status(CAPITAL,-value)
                else:
                    ui.add_status(emotion,value)
                if emotion == MUTANT:
                    if random.randrange(0,50) == 0:
                        city.construct_building(MUTATION,(self.x,self.y))
                        city.destroy_object(self)
                        switch.switches["research_complete"] = True
                        achievements.add("MUTATE!")
                        building.add_function(LABORATORY,{"Mutate MORE!":50})
                self.emotions[emotion] += value
                event_handler.add(TIER_1_EMOTION_ADDED,self,50)
                city.emotion_added(emotion,self,value,2)
            elif tier == 2:
                if not self.cooldown:
                    self.cooldown = True
                    self.emotions[emotion] += value
                    if emotion == MUTANT:
                        if random.randrange(0,50) == 0:
                            city.construct_building(MUTATION,(self.x,self.y))
                            city.destroy_object(self)
                            switch.switches["research_complete"] = True
                            achievements.add("MUTATE!")
                            building.add_function(LABORATORY,{"Mutate MORE!":50})
                    event_handler.add(TIER_2_EMOTION_ADDED,self,50)
                    city.emotion_added(emotion,self,value,2)

    def add_function(building_type,function):
        if list(function.keys())[0] not in GameObjects.functions[building_type]:
            GameObjects.functions[building_type].update(function)
            event_handler.add(FUNCTION_ADDED,list(function.keys())[0],50)
            for game_object in city.get_all_of(building_type).sprites():
                if list(function.keys())[0] not in game_object.functions:
                    game_object.functions.update(function)
    def decay(self):
        for emotion in self.emotions:
            if emotion != 0:
                if emotion - 1 == 0:
                    city.destroy_object(self)
                else:
                    emotion -= 1
class tutorial_image(pygame.sprite.Sprite):
    images = ["cherry.png","cupcake.png","star.png","cloud.png","watermelon.png"]
    def __init__(self, speed, angle, coordinates):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = load(random.choice(tutorial_image.images))

       #initial speed and angle
       self.speed = speed
       self.angle = angle

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.coordinates = coordinates
       self.rect.x,self.rect.y = coordinates
    def update(self):
        self.rect.x += math.cos(self.angle)*self.speed
        self.rect.y += math.sin(self.angle)*self.speed
        self.coordinates = (self.rect.x,self.rect.y)
        if (not util.inBox(self.coordinates,(-WIDTH,0,WIDTH*2,HEIGHT))):
            self.kill()
class button_(pygame.sprite.Sprite):
    def __init__(self,label,coordinates):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = button_font.render(label,True,black)

       #initializes label
       self.label = label
       self.clicked = False
       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y

       self.rect = self.image.get_rect()
       self.coordinates = coordinates
       self.rect.x,self.rect.y = coordinates
    def update(self):

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            util.centerimg(load("thecat.png"),(self.rect.x-THECAT_WIDTH/2,self.rect.y+self.image.get_height()/2))
            if _input.mouse_left:
                self.clicked = True
                _input.mouse_left = False
    def draw(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))
    def next(self):
        if self.label == "GameSpeed 1x":
            self.label = "GameSpeed 2x"
            switch.switches["game_speed"] = 2
        elif self.label == "GameSpeed 2x":
            self.label = "GameSpeed 4x"
            switch.switches["game_speed"] = 4
        elif self.label == "GameSpeed 4x":
            self.label = "GameSpeed 10x"
            switch.switches["game_speed"] = 10
        elif self.label == "GameSpeed 10x":
            self.label = "GameSpeed 1x"
            switch.switches["game_speed"] = 1

        self.image = button_font.render(self.label,True,black)
        SECONDS_PER_CYCLE = int(60/switch.switches["game_speed"])
class detection(pygame.sprite.Sprite):
    def __init__(self,coordinates=(0,0),dimensions=(0,0),proximity=(0,0,0,0)):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       width,height = dimensions
       width += proximity[2]
       height += proximity[3]
       self.image = pygame.Surface((width,height))

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       x,y=coordinates
       x += proximity[0]
       y += proximity[1]
       self.x = x
       self.y = y
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y
class city:
    grid = pygame.sprite.Group()
    dark = pygame.Surface((FRAME_WIDTH,FRAME_HEIGHT), flags=pygame.SRCALPHA)
    def update():
        city.grid.update()
    def draw():
        transX = scroller.translateX()
        transY = scroller.translateY()
        revX = scroller.reverseX()
        revY = scroller.reverseY()

        #screen.blit(scale(get_image("grass.png"),(CITY_WIDTH,CITY_HEIGHT)),(0,0))
        pygame.draw.rect(screen,forestgreen,(transX,transY,CITY_WIDTH,CITY_HEIGHT))
        pygame.draw.rect(screen,greenyellow,(transX+CITY_WIDTH/5,transY+CITY_HEIGHT/3,5,5))
        pygame.draw.rect(screen,greenyellow,(transX+CITY_WIDTH/2,transY+CITY_HEIGHT/6*5,5,5))
        pygame.draw.rect(screen,greenyellow,(transX+CITY_WIDTH/8*5,transY+CITY_HEIGHT/4,5,5))
        pygame.draw.rect(screen,greenyellow,(transX+CITY_WIDTH/7*5,transY+CITY_HEIGHT/3*2,5,5))
        pygame.draw.rect(screen,greenyellow,(transX+CITY_WIDTH/8,transY+CITY_HEIGHT/8*7,5,5))
        pygame.draw.rect(screen,greenyellow,(transX+CITY_WIDTH/9*7,transY+CITY_HEIGHT/9,5,5))

        city.grid.draw(screen)

        if not ui.day_time:
            screen.blit(city.dark, (CITY_LEFT, 0), special_flags=pygame.BLEND_RGBA_SUB)
            #del dark
            #pygame.draw.rect(screen,(50,50,50,0.01),(CITY_LEFT,0,FRAME_WIDTH,FRAME_HEIGHT))
    def has(objectID):
        check = False
        for num,game_object in enumerate(city.grid.sprites()):
            if game_object.id_ == objectID:
                check = True
        return check
    def get_all_of(objectID):
        list_of_objects = pygame.sprite.Group()
        for num, game_object in enumerate(city.grid.sprites()):
            if game_object.id_ == objectID:
                list_of_objects.add(game_object)
        return list_of_objects
    def buy_building(buildingID):
        ui.build = True
        ui.new_structure = building(buildingID)
    def construct_building(buildingID,coordinates, status = 0):
        full = False
        if buildingID in [0,101,103,107]:
            if city.has(buildingID):
                full = True
        if buildingID == GUARD:
            if len(city.get_all_of(GUARD).sprites()) < len(city.get_all_of(BANK).sprites()):
                full = True

        if not full:
            new_building = building(buildingID,coordinates)
            city.grid.add(new_building)

            if buildingID == 1:
                ui.population_limit += HOUSE_LIMIT
            elif buildingID == 103:
                city.emotion_added(AWARENESS,new_building,-10)
            elif buildingID == 104:
                city.emotion_added(FEAR,new_building)
            elif buildingID == 105:
                city.emotion_added(VIOLENCE,new_building)
            elif buildingID == 106:
                city.emotion_added(VIOLENCE,new_building)
            elif buildingID == 108:
                city.emotion_added(INNOVATION,new_building)
            elif buildingID == 109:
                city.emotion_added(HAPPINESS,new_building)
            if buildingID < 100:
                city.emotion_added(AWARENESS,new_building,3)

            city.emotion_added(AWARENESS,new_building,5,2)
            del new_building
            event_handler.add(BUILDING_ADDED,None,50)
    def new_kittizen(coords=(0,0)):
        if coords == (0,0):
            coords = city.find_coordinate((15,15),city.grid)
        kitty = kittizen(coords)
        city.grid.add(kitty)
        ui.add_status(POPULATION,1)
        ui.add_status(HAPPINESS,10)
        ui.add_status(CAPITAL,10)
        del kitty
        event_handler.add(KITTIZEN_ADDED,None,50)
    def new_fixed_kittizen(coords_rect):
        coords = city.find_coordinate((15,15),city.grid,coords_rect)
        kitty = kittizen(coords)
        city.grid.add(kitty)
        del kitty
    def destroy_object(game_object):
        if game_object.id_ == 1:
            ui.population_limit -= HOUSE_LIMIT
        elif game_object.id_ == 106:
            new_1 = pygame.Rect(tuple(map(operator.add,event[3],(-EFFECT_RANGE,-EFFECT_RANGE,EFFECT_RANGE*2,EFFECT_RANGE*2))))
            for num,citizen in enumerate(city.get_all_of(100).sprites()):
                new_2 = citizen.rect()
                if new_1.colliderect(new_2):
                    citizen.kill()
                    del citizen
        if game_object.id_ == 100:
            event_handler.add(KITTIZEN_REMOVED,None,50)
            status_bars.add_status(POPULATION,-1)
        else:
            event_handler.add(BUILDING_REMOVED,None,50)
        if game_object.id_ == 108:
            city.emotion_added(AWARENESS,game_object,10)
        if game_object.id_ < 100:
            city.emotion_added(AWARENESS,game_object)

        game_object.kill()
        del game_object
    def collision_exclude(sprite,excluded,list):
        check = False
        for object in list:
            if object not in excluded:
                if pygame.sprite.colliderect(sprite,object):
                    check = True
        return check
    def emotion_added(emotion,game_object,value = 3,tier = 1,range = EFFECT_RANGE):
        x = game_object.rect.x
        y = game_object.rect.y
        width = game_object.width
        height = game_object.height
        effect_rect = pygame.Rect(x-range,y-range,range*2+width,range*2+height)
        for kittizen in city.get_all_of(100).sprites():
            if kittizen.rect.colliderect(effect_rect):
                kittizen.emote(emotion,value,tier)
            if tier == 1:
                event_handler.add(TIER_1_EMOTION_ADDED,None,50)
            else:
                event_handler.add(TIER_2_EMOTION_ADDED,None,50)
    def find_coordinate(dimensions,list,range = (0,0,CITY_WIDTH,CITY_HEIGHT)):
        new_coords = (int(random.uniform(range[0],range[0]+range[2])),int(random.uniform(range[1],range[1]+range[3])))
        detector1 = detection(scroller.translateCoordinates(new_coords),dimensions)
        counter = 0
        while pygame.sprite.spritecollideany(detector1,list) != None:
            counter +=1
            if counter > 10000:
                print("Not enough space for more citizens!")
                break
            new_coords = (int(random.uniform(range[0],range[0]+range[2])),int(random.uniform(range[1],range[1]+range[3])))
            detector1 = detection(scroller.translateCoordinates(new_coords),dimensions)
        return new_coords
    def corrupt_building(stage, game_object):
        if game_object.status == stage:
            if stage == 0:
                game_object.status = 1
                for i in range(5):
                    if len(city.get_all_of(100).sprites()) > 5:
                        city.remove_object(city.get_all_of(100).sprites()[len(city.get_all_of(100).sprites())-i-1])
            if stage == 1:
                detector1 = detection((game_object.rect.x,game_object.rect.y),(game_object.width,game_object.height),(0,0,0,76))
                game_object.status = 2
                if pygame.sprite.spritecollide(detector1,city.grid,False):
                    for in_the_way in pygame.sprite.spritecollide(detector1,city.grid,False):
                        city.destroy_object(in_the_way)
                del detector1
                coords = (game_object.x+game_object.width/2-CITIZEN_WIDTH,game_object.y+game_object.height)
                city.construct_building(102,(game_object.x,game_object.y+game_object.height))
                city.construct_building(110,coords)
                city.construct_building(110,tuple(map(operator.add,coords,(2,0))))
                city.construct_building(110,tuple(map(operator.add,coords,(-34,28))))
                city.construct_building(110,tuple(map(operator.add,coords,(38,38))))
                city.construct_building(110,tuple(map(operator.add,coords,(-22,76))))
                city.construct_building(110,tuple(map(operator.add,coords,(26,76))))
class ui:
    day_time = True
    days = 0
    time = 0
    clock_time = 0
    city_loaded = False

    new_structure = building()
    build = False
    build_check = True
    status_bars = {
        POPULATION:0,
        CAPITAL:10,
        HAPPINESS:10
    }
    colors = [red,orange,yellow,blue,green,purple,indigo,brown]
    emotion_names = ["Population","Capital","Happiness","Awareness","Fear","Violence","Innovation","Mutant"]
    population_limit = 5

    menu_show = False
    selected_object = pygame.sprite.Sprite()

    selected_kittizen = kittizen()

    the_cat_dialogue_options = ["Cats have 9 lives!","Mice love cheese!","Sometimes your kittens hide at the edge"]
    the_cat_dialogue = 0
    def update():

        if time.clock() >= 1+ui.clock_time and tutorial.tPart == 0:
            ui.clock_time = time.clock()
            ui.clock_time = int(ui.clock_time)
            ui.time += 1
            if(ui.time%int(60/switch.switches["game_speed"]) < int(60/switch.switches["game_speed"])/2):
                ui.day_time = True
            else:
                ui.day_time = False

            if(ui.time%int(60/switch.switches["game_speed"]) == 0):
                ui.new_day()
                ui.the_cat_dialogue = (ui.the_cat_dialogue+1) % len(ui.the_cat_dialogue_options)
            if(ui.time%int(60/switch.switches["game_speed"]) == int(60/switch.switches["game_speed"])/2):
                ui.new_night()
                ui.the_cat_dialogue = (ui.the_cat_dialogue+1) % len(ui.the_cat_dialogue_options)
        if ui.build:
            ui.build_check = True
            mouseX,mouseY = pygame.mouse.get_pos()
            width = ui.new_structure.width
            height = ui.new_structure.height
            ui.new_structure.rect.x = mouseX-width/2
            ui.new_structure.rect.y = mouseY-height/2
            if pygame.sprite.spritecollideany(ui.new_structure,city.grid) != None:
                ui.build_check = False
            if not util.inBox((mouseX-width/2,mouseY-height/2),CITY_RECTANGLE):
                ui.build_check = False
            if ui.build_check:
                pygame.draw.rect(screen,blue,(mouseX-width/2,mouseY-height/2,width,height))
                if _input.mouse_left:
                    if ui.get_value(CAPITAL) >= ui.new_structure.price:
                        city.construct_building(ui.new_structure.id_,(mouseX-width/2+scroller.reverseX(),mouseY-height/2+scroller.reverseY()))
                        _input.mouse_left = False
                        ui.add_status(CAPITAL,-ui.new_structure.price)
                    else:
                        event_handler.add_once(BROKE,ui.new_structure,50)
            else:
                pygame.draw.rect(screen,red,(mouseX-width/2,mouseY-height/2,width,height))
        if _input.mouse_right:
            ui.build = False
            ui.menu_show = False

    def draw():
        pygame.draw.rect(screen,pink,(0,0,CITY_LEFT,HEIGHT))
        pygame.draw.line(screen,black,(CITY_LEFT,0),(CITY_LEFT,HEIGHT),GENERAL_BORDER)
        screen.blit(load("clock.png"),(CITY_LEFT-load("clock.png").get_width()-GENERAL_BORDER,CITY_BORDER+TEXT_MARGIN*2+GENERAL_BORDER))
        text("Day:"+str(ui.days),(CITY_BORDER,THECAT_HEIGHT+CITY_BORDER))
        pygame.draw.line(screen,black,(CLOCK_X+50,CLOCK_Y+50),(CLOCK_X+50+50*math.cos(2*math.pi*ui.time/int(60/switch.switches["game_speed"])+math.pi),CLOCK_Y+50+50*math.sin(2*math.pi*ui.time/int(60/switch.switches["game_speed"])+math.pi)),5)

        for bar in ui.status_bars:
            if bar == POPULATION:
                text("Population "+str(ui.status_bars[bar])+"/"+str(ui.population_limit),(STATUS_BAR_X,STATUS_BAR_Y+TEXT_MARGIN*(bar+1)))
                pygame.draw.rect(screen,ui.colors[bar],(STATUS_BAR_X,STATUS_BAR_Y+TEXT_MARGIN*(bar+1)+CITY_BORDER,min(ui.status_bars[bar]*STATUS_BAR_WIDTH/ui.population_limit,STATUS_BAR_WIDTH),STATUS_BAR_HEIGHT))
            else:
                text("{} {}".format(ui.emotion_names[bar],ui.status_bars[bar]),(STATUS_BAR_X,STATUS_BAR_Y+TEXT_MARGIN*(bar+1)))
                pygame.draw.rect(screen,ui.colors[bar],(STATUS_BAR_X,STATUS_BAR_Y+TEXT_MARGIN*(bar+1)+CITY_BORDER,min(ui.status_bars[bar]*STATUS_BAR_WIDTH/OVERALL_LIMIT,STATUS_BAR_WIDTH),STATUS_BAR_HEIGHT))
                # if ui.status_bars[bar] > ui.population_limit:
                #     pygame.draw.rect(screen,ui.colors[bar],(STATUS_BAR_X,STATUS_BAR_Y+TEXT_MARGIN*(bar+1)+CITY_BORDER,STATUS_BAR_WIDTH,STATUS_BAR_HEIGHT))
                # else:
                #     self.image = pygame.Surface((self.value*STATUS_BAR_WIDTH/ui.population_limit,STATUS_BAR_HEIGHT))

        if ui.menu_show:
            text("Name: " + ui.selected_object.name,(1,FRAME_HEIGHT/2+TEXT_MARGIN*1))
            if ui.selected_object.id_ == KITTIZEN and ui.selected_object.cooldown:
                text("*Emotionally Exhausted*",(CITY_LEFT/2,FRAME_HEIGHT/2+TEXT_MARGIN*1))
            util.textwrapped("Description: "+ ui.selected_object.description,(1,FRAME_HEIGHT/2+TEXT_MARGIN*2))
            if ui.selected_object.functions:
                text("Options:",(1,FRAME_HEIGHT/2+TEXT_MARGIN*4))
                for num,option in enumerate(ui.selected_object.functions):
                    text("{}-{} ${}".format(num+1,option,GameObjects.functions[ui.selected_object.id_][option]),(1,FRAME_HEIGHT/2+TEXT_MARGIN*5+num*TEXT_MARGIN))
                    if _input.one and num == 0:
                        ui.selected_object.function(option)
                        _input.one = False
                    if _input.two and num == 1:
                        ui.selected_object.function(option)
                        _input.two = False
                    if _input.three and num == 2:
                        ui.selected_object.function(option)
                        _input.three = False
                    if _input.four and num == 3:
                        ui.selected_object.function(option)
                        _input.four = False
            if ui.selected_object.id_ == 100:
                for num,emotion in enumerate(kittizen.active_emotions):
                    if emotion and num != POPULATION:
                        dial = default_font.render(ui.emotion_names[num],True,black)
                        if ui.selected_object.rect.y < HEIGHT/2:
                            screen.blit(pygame.transform.rotate(dial,90),(ui.selected_object.rect.x-STATUS_BAR_HEIGHT+TEXT_MARGIN*num,ui.selected_object.rect.y+MINI_BAR_HEIGHT-dial.get_width()))
                            pygame.draw.rect(screen,ui.colors[num],(ui.selected_object.rect.x+STATUS_BAR_HEIGHT+TEXT_MARGIN*num,ui.selected_object.rect.y+MINI_BAR_HEIGHT-ui.selected_object.emotions[num]/MAX_EMOTION*MINI_BAR_HEIGHT,STATUS_BAR_HEIGHT,ui.selected_object.emotions[num]/MAX_EMOTION*MINI_BAR_HEIGHT))
                        else:
                            screen.blit(pygame.transform.rotate(dial,90),(ui.selected_object.rect.x-STATUS_BAR_HEIGHT+TEXT_MARGIN*num,ui.selected_object.rect.y))
                            pygame.draw.rect(screen,ui.colors[num],(ui.selected_object.rect.x+STATUS_BAR_HEIGHT+TEXT_MARGIN*num,ui.selected_object.rect.y,STATUS_BAR_HEIGHT,ui.selected_object.emotions[num]/MAX_EMOTION*MINI_BAR_HEIGHT))


        dialogue = default_font.render(ui.the_cat_dialogue_options[ui.the_cat_dialogue],True,black)
        screen.blit(load("thecat.png"),(CITY_BORDER,CITY_BORDER))
        util.rect(white,(CITY_BORDER+THECAT_WIDTH,CITY_BORDER,dialogue.get_width()+TEXT_MARGIN,dialogue.get_height()+TEXT_MARGIN),GENERAL_BORDER*2)
        #screen.blit(scale(get_image("textbox.png"),(int(box_width),int(box_height))),(coordinates[0]+catWidth,coordinates[1]))
        screen.blit(dialogue,(CITY_BORDER+THECAT_WIDTH+TEXT_MARGIN/2,CITY_BORDER+TEXT_MARGIN/2))
        del dialogue
    def add_status(emotion,value):
        if emotion in ui.status_bars:
            ui.status_bars[emotion] += value
            if ui.status_bars[emotion] < 0:
                ui.status_bars[emotion] = 0
            if emotion != POPULATION and ui.status_bars[emotion] >= OVERALL_LIMIT:
                win(emotion)

            if ui.status_bars[emotion] == 0 and emotion == POPULATION:
                achievements.add("Game Over")
            if emotion == AWARENESS:
                if ui.status_bars[emotion] > 100:
                    switch.switches["propaganda"] = True
                    building.add_function(KITTY_HALL, {"Put up Propaganda":10})
            elif emotion == FEAR:
                if ui.status_bars[emotion] > 200:
                    switch.switches["video_vision"] = True
                    building.add_function(KITTY_HALL, {"Install Video Vision":20})
            elif emotion == INNOVATION:
                if ui.status_bars[emotion] > 500:
                    switch.switches["fully_educated"] = True
                    building.add_function(LABORATORY, {"Build Happiness Machine":30})
        else:
            ui.status_bars[emotion] = value
            if ui.status_bars[emotion] < 0:
                ui.status_bars[emotion] = 0
            if emotion != 0:
                kittizen.active_emotions[emotion-1] = True
    def set_status(emotion,value):
        if emotion in ui.status_bars:
            ui.status_bars[emotion] = value
        else:
            ui.status_bars[emotion] = value
            if emotion != 0:
                kittizen.active_emotions[emotion-1] = True
    def get_value(bar):
        if bar in ui.status_bars:
            return ui.status_bars[bar]
        else:
            return(0)
    def set_data(game_object):
        ui.selected_object = game_object
    def add_cat_dialogue(dialogue):
        if dialogue not in ui.the_cat_dialogue_options:
            ui.the_cat_dialogue_options.append(dialogue)
            ui.the_cat_dialogue = len(ui.the_cat_dialogue_options)-1
    def new_day():
        ui.days += 1
        ui.add_status(CAPITAL,5)

        command = False
        command_rect = (0,0,0,0)
        truck = False
        truck_coords = (0,0)
        control = False
        control_coords = (0,0)
        police_zones = []
        power_zones = []
        danger_zones = []
        for game_object in city.grid.sprites():
            if game_object.id_ == KITTIZEN:
                game_object.cooldown = False
                game_object.decay()
            if game_object.id_ == COMMAND_BLOCK:
                command = True
                command_rect = (game_object.x-COMMAND_RANGE,game_object.y-COMMAND_RANGE,game_object.width+COMMAND_RANGE*2,game_object.height+COMMAND_RANGE*2)
                city.destroy_object(game_object)

        for kittizen in city.get_all_of(KITTIZEN).sprites():
            if command:
                kittizen.fixed_move(command_rect)
            else:
                kittizen.move()
        for game_object in city.grid.sprites():
            x = game_object.rect.x
            y = game_object.rect.y
            width = game_object.width
            height = game_object.height

            # if game_object.status == 1:
            #     city.corrupt_building(1,game_object)

            if game_object.id_ == KITTY_HALL:
                city.emotion_added(HAPPINESS,game_object)
            elif game_object.id_ == BANK:
                city.emotion_added(CAPITAL,game_object)
                ui.add_status(CAPITAL,3)
            elif game_object.id_ == KITTY_MALL:
                city.emotion_added(CAPITAL,game_object,-2)
                city.emotion_added(HAPPINESS,game_object)
            elif game_object.id_ == SHRINE:
                city.emotion_added(AWARENESS,game_object)
            elif game_object.id_ == SCHOOL:
                city.emotion_added(INNOVATION,game_object)
                city.emotion_added(HAPPINESS,game_object,-2)
            elif game_object.id_ == LABORATORY:
                city.emotion_added(INNOVATION,game_object,4)
                city.emotion_added(VIOLENCE,game_object,-2)
            elif game_object.id_ == DOJO:
                city.emotion_added(VIOLENCE,game_object)
                city.emotion_added(FEAR,game_object,-2)
            elif game_object.id_ == PRISON:
                city.emotion_added(FEAR,game_object)
                city.emotion_added(HAPPINESS,game_object,-2)
            elif game_object.id_ == LIBRARY:
                city.emotion_added(INNOVATION,game_object)
            elif game_object.id_ == FOOD_TRUCK:
                truck = True
                truck_coords = (game_object.x,game_object.y)
                city.destroy_object(game_object)
            elif game_object.id_ == PROPAGANDA_POSTER:
                city.emotion_added(FEAR,game_object,10)
                city.destroy_object(game_object)
            elif game_object.id_ == VIDEO_VISION:
                city.emotion_added(FEAR,game_object)
            elif game_object.id_ == ENRAGED_KITTIZEN:
                city.emotion_added(VIOLENCE,game_object)
            elif game_object.id_ == BALL_OF_YARN:
                control = True
                control_coords = (game_object.x,game_object.y)
                city.destroy_object(game_object)
            elif game_object.id_ == RIOT:
                city.emotion_added(VIOLENCE,game_object)
                city.emotion_added(FEAR,game_object,-5)
            elif game_object.id_ == CAT_EXPERIMENT:
                city.emotion_added(MUTANT,game_object,10)
                if random.randrange(0,50) == 0:
                    city.construct_building(MUTATION,(game_object.x,game_object.y))
                    switch.switches["research_complete"] = True
                    achievements.add("MUTATE!")
                    building.add_function(LABORATORY,{"Mutate MORE!":50})
                city.destroy_object(game_object)
            elif game_object.id_ == game_object:
                city.emotion_added(AWARENESS,game_object)
            elif game_object.id_ == POLICE:
                police_zones.append((game_object.x,game_object.y,game_object.width,game_object.height))
            elif game_object.id_ == THUG:
                city.emotion_added(VIOLENCE,game_object)
                city.emotion_added(CAPITAL,game_object,-1)
            elif game_object.id_ == ROBBER:
                city.emotion_added(CAPITAL,game_object,-2)
            elif game_object.id_ == PROTECTOR:
                city.emotion_added(AWARENESS,game_object,-5)
                city.emotion_added(FEAR,game_object)
                power_zones.append((game_object.x,game_object.y,game_object.width,game_object.height))
            elif game_object.id_ == DARK_SPIRIT:
                city.emotion_added(AWARENESS,game_object)
            elif game_object.id_ == GUARD:
                police_zones.append((game_object.x,game_object.y,game_object.width,game_object.height))
            elif game_object.id_ == INVADER:
                game_object.move()
                danger_zones.append((game_object.x,game_object.y,game_object.width,game_object.height))
            elif game_object.id_ == KUNG_FU_WARRIOR:
                power_zones.append((game_object.x,game_object.y,game_object.width,game_object.height))
            elif game_object.id_ == RUNAWAY_PRISONER:
                city.emotion_added(HAPPINESS,game_object,-2)
            elif game_object.id_ == HAPPINESS_MACHINE:
                city.emotion_added(HAPPINESS,game_object,20,2)

        for anger in range(int(ui.get_value(VIOLENCE)/5)):
            if random.randrange(0,15) == 0:
                city.construct_building(ENRAGED_KITTIZEN,city.find_coordinate(GameObjects.dimensions[ENRAGED_KITTIZEN],city.grid))
                ui.add_cat_dialogue("Your citizens are getting violent!")
        for fear in range(int(ui.get_value(FEAR)/5)):
            if random.randrange(0,15) == 0:
                city.construct_building(RIOT,city.find_coordinate(GameObjects.dimensions[RIOT],city.grid))
                ui.add_cat_dialogue("Your citizens are getting out of control!")
        for protector in range(int(ui.get_value(HAPPINESS)/5)):
            if random.randrange(0,20) == 0:
                city.construct_building(PROTECTOR,city.find_coordinate(GameObjects.dimensions[PROTECTOR],city.grid))
                ui.add_cat_dialogue("I've sent a protector to help!")
        if random.randrange(0,10) == 0:
            city.construct_building(MYSTERIOUS_WARRIOR,city.find_coordinate(GameObjects.dimensions[MYSTERIOUS_WARRIOR],city.grid))
            ui.add_cat_dialogue("Mysterious warriors are very wise")
        thugs = city.get_all_of(THUG).sprites()
        robbers = city.get_all_of(ROBBER).sprites()
        prisoners = city.get_all_of(RUNAWAY_PRISONER).sprites()
        baddies = thugs+robbers+prisoners
        if police_zones and baddies:
            for guard in police_zones:
                detector1 = pygame.Rect(tuple(map(operator.add,guard,(-EFFECT_RANGE,-EFFECT_RANGE,EFFECT_RANGE*2,EFFECT_RANGE*2))))
                #baddies = city.get_all_of(THUG).append(city.get_all_of(ROBBER).append(city.get_all_of(RUNAWAY_PRISONER)))
                for enemy in baddies:
                    detector2 = pygame.Rect((enemy.x,enemy.y,enemy.width,enemy.height))
                    if detector1.colliderect(detector2):
                        city.destroy_object(enemy)
                    del detector2
                del detector1
            del baddies
        dark_spirits = city.get_all_of(DARK_SPIRIT).sprites()
        invaders = city.get_all_of(INVADER).sprites()
        strong_baddies = dark_spirits+invaders
        if power_zones and strong_baddies:
            for protector in power_zones:
                detector1 = pygame.Rect(tuple(map(operator.add,protector,(-EFFECT_RANGE,-EFFECT_RANGE,EFFECT_RANGE*2,EFFECT_RANGE*2))))
                #strong_baddies = city.get_all_of(DARK_SPIRIT).append(city.get_all_of(INVADER))
                for enemy in strong_baddies:
                    detector2 = pygame.Rect((enemy.x,enemy.y,enemy.width,enemy.height))

                    if detector1.colliderect(detector2):
                        city.destroy_object(enemy)
                    del detector2
                del detector1
            del strong_baddies
        if truck:
            for i in range(1):
                city.new_kittizen(truck_coords[0]+CITIZEN_WIDTH*i,truck_coords[1])
        if control:
            ui.selected_kittizen.move(control_coords)

        for newcat in range(int(len(city.get_all_of(1).sprites()))):
            if ui.get_value(POPULATION) <= ui.population_limit and random.randrange(0,5) == 0:
                if command:
                    city.new_fixed_kittizen(command_rect)
                else:
                    city.new_kittizen()
        event_handler.add(NEW_DAY,None,50)

    def new_night():
        ui.add_status(CAPITAL,5)
        ui.menu_show = False
        truck = False
        control = False

        for game_object in city.grid.sprites():
            if game_object.id_ == COMMAND_BLOCK:
                command = True
                command_rect = (game_object.x-COMMAND_RANGE,game_object.y-COMMAND_RANGE,game_object.width+COMMAND_RANGE*2,game_object.height+COMMAND_RANGE*2)
                city.destroy_object(game_object)

        for game_object in city.grid.sprites():
            if game_object.id_ == KITTIZEN:
                game_object.x,game_object.y = (-500,-500)
            if ui.get_value(AWARENESS) > 100 or ui.get_value(FEAR) > 300 and game_object.id_ < 100 and len(city.get_all_of(100).sprites()) > 5:
                detector1 = detection((x,y),(width,height),(-250,-250,500,500))
                detector2 = detection((x,y),(0,0,0,100))
                if not city.collision_exclude(detector,[object],city.get_all_of(0)) and not city.collision_exclude(detector2,[object],city.grid.sprites()):
                    if random.randrange(0,3) == 0:
                        city.corrupt_building(0,object)
                        ui.add_cat_dialogue("I think a cult is forming...")
                del detector1
                del detector2

            if game_object.id_ == BANK:
                if random.randrange(0,5) == 0:
                    city.construct_building(ROBBER,city.find_coordinate((15,15),city.grid,(game_object.x-250,game_object.y-250,500,500)))
            elif game_object.id_ == PRISON:
                if random.randrange(0,5) == 0:
                    city.construct_building(RUNAWAY_PRISONER,city.find_coordinate((15,15),city.grid,(game_object.x-250,game_object.y-250,500,500)))
            elif game_object.id_ == DOJO:
                if random.randrange(0,5) == 0:
                    city.construct_building(THUG,city.find_coordinate((15,15),city.grid,(game_object.x-250,game_object.y-250,500,500)))
            elif game_object.id_ == FOOD_TRUCK:
                truck = True
                truck_coords = (game_object.x,game_object.y)
                city.destroy_object(game_object)
            elif game_object.id_ == BALL_OF_YARN:
                control = True
                control_coords = (game_object.x,game_object.y)
                city.destroy_object(game_object)
            elif game_object.id_ == THUG or game_object.id_ == ROBBER or game_object.id_ == RUNAWAY_PRISONER :
                game_object.move()

        if control:
            ui.selected_kittizen.move(control_coords)

        for dark_spirit in range(int(ui.get_value(AWARENESS)/10)):
            if random.randrange(0,20) == 0:
                city.construct_building(DARK_SPIRIT,city.find_coordinate(GameObjects.dimensions[DARK_SPIRIT],city.grid))

        if switch.switches["invasion"] and len(city.get_all_of(INVADER).sprites()) == 0:
            switch.switches["invasion"] = False
        if not switch.switches["invasion"] and ui.get_value(VIOLENCE) > 100 and ui.get_value(INNOVATION) > 100 and random.randrange(0,20) == 0:
            ui.add_cat_dialogue("Beware the invasion!")
            switch.switches["invasion"] = True
            for enemy in range(5):
                city.construct_building(INVADER,city.find_coordinate(GameObjects.dimensions[INVADER],city.grid,(0,0,CITY_WIDTH,100)))
            for enemy in range(5):
                city.construct_building(INVADER,city.find_coordinate(GameObjects.dimensions[INVADER],city.grid,(0,0,100,CITY_HEIGHT)))
            for enemy in range(5):
                city.construct_building(INVADER,city.find_coordinate(GameObjects.dimensions[INVADER],city.grid,(CITY_WIDTH-100,0,100,CITY_HEIGHT)))
            for enemy in range(5):
                city.construct_building(INVADER,city.find_coordinate(GameObjects.dimensions[INVADER],city.grid,(0,CITY_HEIGHT-100,CITY_WIDTH,100)))
        event_handler.add(NEW_NIGHT,None,50)
class event_handler:
    events = []
    def update():
        if event_handler.events:
            for num, event in enumerate(event_handler.events):
                #(event_type,source,duration)
                msg = ""
                id_ = event[0]
                if id_ == BUILDING_ADDED:
                    msg = "Building Added!"
                if id_ == BUILDING_REMOVED:
                    msg = "Building Removed!"
                if id_ == KITTIZEN_ADDED:
                    msg = "Your population has grown!"
                if id_ == KITTIZEN_REMOVED:
                    msg = "A kittizen has passed away"
                if id_ == STATUS_CHANGE:
                    msg = "Something changed!"
                if id_ == NEW_DAY:
                    msg = "A new day!"
                if id_ == NEW_NIGHT:
                    msg = "A new night!"
                if id_ == TIER_1_EMOTION_ADDED:
                    msg = "Something is starting to spread!"
                if id_ == TIER_2_EMOTION_ADDED:
                    msg = "Something is spreading!"
                if id_ == BUILDING_LIMIT:
                    msg = "Too many of these buildings!"
                if id_ == BUILDING_STATUS:
                    msg = "Something suspicious is going on!"
                if id_ == BROKE:
                    msg = "You can't afford "+GameObjects.names[event[1].id_]
                if id_ == FUNCTION_ADDED:
                    msg = "You can now "+event[1]
                if id_ == FUNCTION_BROKE:
                    msg = "You can't afford to"+event[1]
                if id_ == INQUIRY:
                    if event[1]:
                        msg = "Your inquiry succeeded!"
                    else:
                        msg = "Your inquiry failed!"
                if id_ == ACHIEVEMENT:
                    msg = "Achievement Earned: "+event[1]
                if id_ == SAVED_SUCCESSFULLY:
                    msg = "Game Saved!"
                if id_ == LOADED_SUCCESSFULLY:
                    msg = "Game Loaded!"
                if id_ == LOAD_ERROR:
                    msg = "No save file detected!"
                text(msg,(CITY_LEFT+CITY_BORDER,TEXT_MARGIN*num))
                event[2] -= 1
                if event[2] < 1:
                    del event_handler.events[num]
    def add(event_type,source,duration,value = None):
        if len(event_handler.events) < 50:
            event_handler.events.append([event_type,source,duration,value])
    def add_once(event_type,source,duration,value = None):
        if len(event_handler.events) < 50:
            if not event_handler.check(event_type):
                event_handler.events.append([event_type,source,duration,value])
    def check(event_type):
        switch = False
        if event_handler.events:
            for event in event_handler.events:
                if event[0] == event_type:
                    switch = event
        return switch
class tutorial:
    tPart = 0
    parts = {   1: ["Do you like creating things?",
                    (WIDTH*0.5,HEIGHT*0.5)],
                2: ["Of course you do!",
                    (WIDTH*0.5,HEIGHT*0.5)],
                3: ["Let me show you how to make a city!",
                    (WIDTH*0.5,HEIGHT*0.5)],
                4: ["The menu on the left shows you your status.",
                    (WIDTH*0.1,HEIGHT*0.5)],
                5: ["This is your population.",
                    (WIDTH*0.1,HEIGHT*0.3)],
                6: ["Don't let it drop to zero. EVER!",
                    (WIDTH*0.1,HEIGHT*0.3)],
                7: ["This is your city! Kittizens appear automatically.",
                    (WIDTH*0.45,HEIGHT*0.1)],
                8: ["You can use the build tab to place buildings.",
                    (WIDTH*0.45,HEIGHT*0.1)],
                9: ["You can press the right mouse button to stop building.",
                    (WIDTH*0.45,HEIGHT*0.1)],
                10: ["The other buttons are self explanatory",
                    (WIDTH*0.45,HEIGHT*0.1)],
                11: ["I'll place some buildings for you!",
                    (WIDTH*0.45,HEIGHT*0.1)],
                12: ["Oh no! We scared the kittizen!",
                    (WIDTH*0.45,HEIGHT*0.1)],
                13: ["We don't want him spreading rumors.",
                    (WIDTH*0.45,HEIGHT*0.1)],
                14: ["Click on him to get rid of him!",
                    (WIDTH*0.45,HEIGHT*0.1)],
                15: ["I'll do it for you!",
                    (WIDTH*0.45,HEIGHT*0.1)],
                16: ["Here's a better one to replace him!",
                    (WIDTH*0.45,HEIGHT*0.1)],
                17: ["Your buildings have options that use the keyboard",
                    (WIDTH*0.45,HEIGHT*0.1)],
                18: ["Span the screen with the right mouse button!",
                    (WIDTH*0.45,HEIGHT*0.1)],
                19: ["Everything else is pretty much self explanatory!",
                    (WIDTH*0.45,HEIGHT*0.1)],
                20: ["I'll be in the corner giving you tips!",
                    (WIDTH*0.45,HEIGHT*0.1)],
                21: ["Here's some money to start you off!",
                    (WIDTH*0.45,HEIGHT*0.1)],
                22: ["Make sure you beware the night!",
                    (WIDTH*0.45,HEIGHT*0.1)],
                23: ["End",(0,0)]
            }

    def update():
        num = tutorial.tPart
        text = tutorial.parts[num][0]
        coords = tutorial.parts[num][1]
        dialogue = default_font.render(text,True,black)
        screen.blit(load("thecat.png"),tuple(map(operator.add,coords,(-THECAT_WIDTH+GENERAL_BORDER*2,0))))
        util.rect(white,coords+(dialogue.get_width()+TEXT_MARGIN,dialogue.get_height()+TEXT_MARGIN),GENERAL_BORDER*2)
        #(CITY_BORDER+THECAT_WIDTH,CITY_BORDER,dialogue.get_width()+TEXT_MARGIN,dialogue.get_height()+TEXT_MARGIN)
        #screen.blit(scale(get_image("textbox.png"),(int(box_width),int(box_height))),(coordinates[0]+catWidth,coordinates[1]))
        screen.blit(dialogue,tuple(map(operator.add,coords,(TEXT_MARGIN/2,TEXT_MARGIN/2))))
        del dialogue
        if _input.mouse_left:
            tutorial.nextPart()
            _input.mouse_left = False
    def nextPart():
        if tutorial.parts[tutorial.tPart+1][0] != "End":
            if tutorial.tPart == 6:
                city.new_kittizen((400,225))
            if tutorial.tPart == 11:
                city.construct_building(0,(50,200))
                city.construct_building(1,(400,200))
            if tutorial.tPart == 14:
                city.destroy_object(city.get_all_of(KITTIZEN).sprites()[0])
            if tutorial.tPart == 15:
                city.new_kittizen((500,500))
            if tutorial.tPart == 20:
                ui.add_status(CAPITAL,20)
            tutorial.tPart += 1
        else:
            tutorial.tPart = 0
            city.days = 1
def save_file(object,filename):
    file = open("data/"+filename+".txt","w")
    file.write(object)
    file.close()
def load_file(filename):
    file = open("data/"+filename+".txt","r")
    temp = file.read()
    file.close()
    return temp
def save_game():
    city_objects_ = []
    for object_ in city.grid.sprites():
        if object_.id_ != 100:
            city_objects_.append([object_.id_,(object_.x,object_.y),object_.status])
        else:
            city_objects_.append([object_.id_,(object_.x,object_.y),object_.emotions,object_.name,object_.status,object_.cooldown])
    save_file(json.dumps(city_objects_),"city_objects")
    save_file(json.dumps(switch.switches),"switches")
    save_file(json.dumps(achievements.list),"achievements")
    save_file(json.dumps(GameObjects.functions),"functions")
    save_file(json.dumps(ui.the_cat_dialogue),"dialogue")
    save_file(json.dumps(ui.status_bars),"status_bars")

    constants = {"population_limit":ui.population_limit,
                "time":ui.time,
                "day_time":ui.day_time,
                "days":ui.days}
    save_file(json.dumps(constants),"constants")
    save_file("saved","config")
    event_handler.add(SAVED_SUCCESSFULLY,None,50)
def load_game():
    GameObjects.functions = {int(k):v for k,v in json.loads(load_file("functions")).items()}
    city.grid = pygame.sprite.Group()
    city_objects_ = json.loads(load_file("city_objects"))
    for obj in city_objects_:
        if obj[0] != 100:
            new_building = building(obj[0],obj[1],obj[2])
            city.grid.add(new_building)
            del new_building
        else:
            new_kittizen = kittizen(obj[1],obj[2],obj[3],obj[4],obj[5])
            city.grid.add(new_kittizen)
            del new_kittizen
    switch.switches = json.loads(load_file("switches"))
    achievements.list = json.loads(load_file("achievements"))
    ui.the_cat_dialogue = json.loads(load_file("dialogue"))
    ui.status_bars = {int(k):int(v) for k,v in json.loads(load_file("status_bars")).items()}
    constants = json.loads(load_file("constants"))
    ui.population_limit = constants["population_limit"]
    ui.time = constants["time"]
    ui.day_time = constants["day_time"]
    ui.days = constants["days"]

    event_handler.add(LOADED_SUCCESSFULLY,None,50)
def win(emotion):
    if emotion == CAPITAL:
        victory_image = "Money Ending"
    if emotion == HAPPINESS:
        victory_image = "Happy Ending"
    if emotion == AWARENESS:
        if switch.switches["gore"]:
            victory_image = "Gore Ending"
        else:
            victory_image = "Awareness Ending"
    if emotion == FEAR:
        victory_image = "Fear Ending"
    if emotion == VIOLENCE:
        victory_image = "Violent Ending"
    if emotion == INNOVATION:
        victory_image = "Innovation Ending"
    if emotion == MUTANT:
        victory_image = "Mutant Ending"
    achievements.victory = achievements.images[victory_image]
    ui.city_loaded = False
    switch.switches["game_mode"] = 4
def main():
    colors = [red,orange,yellow,green,blue,indigo,violet]

    switch.switches["game_mode"] = 0
    mainCounter = 0

    title_options = ["New City", "Continue", "Options","Achievements"]
    game_options = ["Build","Save","Achievements","Options"]
    build_options = []
    menu_options = ["Fullscreen","Gore","Music"]

    back_up = False
    back_up_button = button_("Overwrite loaded city?",(int(WIDTH*2/3),HEIGHT/2))

    for name in GameObjects.names:
        if name < 100:
            build_options.append(GameObjects.names[name]+" $"+str(GameObjects.prices[name]))

    tutorial_buttons = pygame.sprite.Group()
    for num in range(len(title_options)):
        tutorial_buttons.add(button_(title_options[num],(WIDTH/2,HEIGHT/2+num*(TEXT_MARGIN+BUTTON_SIZE))))
    game_buttons = pygame.sprite.Group()
    for num in range(len(game_options)):
        game_buttons.add(button_(game_options[num],(TEXT_MARGIN,HEIGHT-BUTTON_SIZE*(3-num)-TEXT_MARGIN*2)))
    build_buttons = pygame.sprite.Group()
    for num, names in enumerate(build_options):
        if num % 2 == 0:
            build_buttons.add(button_(names,(CITY_LEFT-BUTTON_SIZE*16,HEIGHT-CITY_BORDER-BUTTON_SIZE*(2+num))))
        else:
            build_buttons.add(button_(names,(CITY_LEFT-BUTTON_SIZE*8,HEIGHT-CITY_BORDER-BUTTON_SIZE*(1+num))))
    menu_buttons = pygame.sprite.Group()
    for num in range(len(menu_options)):
        menu_buttons.add(button_(menu_options[num],(WIDTH/2,HEIGHT/2+num*(TEXT_MARGIN+BUTTON_SIZE))))
    game_speed_button = button_("GameSpeed 1x",(TEXT_MARGIN,HEIGHT-BUTTON_SIZE*(4)-TEXT_MARGIN*2))
    build_on = False

    title = title_font.render(GAME_NAME, True, black)

    projectile_clip = pygame.sprite.Group()
    city.dark.fill((50, 50, 50, 0))
    game_exit = False

    achievements.list = json.loads(load_file("achievements"))

    while not game_exit:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                save_file(json.dumps(achievements.list),"achievements")
                game_exit = True
            if switch.switches["game_mode"] != 0 and switch.switches["game_mode"] != 1 and event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                switch.switches["game_mode"] = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.key.K_ESCAPE:
                pygame.display.set_mode(SCREEN_SIZE)
                switch.switches["fullscreen"] = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKQUOTE and switch.switches["cheats"]:
                    if not switch.switches["fullscreen"]:
                        cmd.parse(input("Command:"))
                if event.key == pygame.K_x:
                    _input.x = True
                if event.key == pygame.K_1:
                    _input.one = True
                if event.key == pygame.K_2:
                    _input.two = True
                if event.key == pygame.K_3:
                    _input.three = True
                if event.key == pygame.K_4:
                    _input.four = True
                if event.key == pygame.K_F1:
                    switch.switches["fullscreen"] = True
                    pygame.display.set_mode(SCREEN_SIZE,pygame.FULLSCREEN)
                if switch.switches["cheats"]:
                    if event.key == pygame.K_n:
                        cmd.c_new_day()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_x:
                    _input.x = False
                if event.key == pygame.K_1:
                    _input.one = False
                if event.key == pygame.K_2:
                    _input.two = False
                if event.key == pygame.K_3:
                    _input.three = False
                if event.key == pygame.K_4:
                    _input.four = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    _input.mouse_left = True
                if event.button == 2:
                    _input.mouse_middle = True
                if event.button == 3:
                    _input.mouse_right = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    _input.mouse_left = False
                if event.button == 2:
                    _input.mouse_middle = False
                if event.button == 3:
                    _input.mouse_right = False

        screen.fill(pink)

        if switch.switches["game_mode"] == 0:
            for num in range(0,7):
                pygame.draw.rect(screen,colors[num],(0,int(mainCounter+HEIGHT/6*num) % int(HEIGHT*7/6)-HEIGHT/6,WIDTH,HEIGHT/6))

            util.rect(pink,(WIDTH*0.05,HEIGHT*0.15-TEXT_MARGIN,WIDTH*0.9,120+TEXT_MARGIN*2),20)

            screen.blit(title, (WIDTH/2-title.get_width()/2,HEIGHT*0.15))
            screen.blit(load("cathead.png"),(WIDTH*0.434,HEIGHT*0.119))

            if mainCounter % 2 == 0:
                projectile_clip.add(tutorial_image(20,math.pi/4,(random.uniform(-math.atan(math.pi/4)*HEIGHT,WIDTH),1)))

            projectile_clip.update()
            projectile_clip.draw(screen)

            tutorial_buttons.update()
            tutorial_buttons.draw(screen)
            if back_up:
                back_up_button.update()
                back_up_button.draw()
				if back_up_button.clicked:
                    switch.switches["game_mode"] = 1
                    city.new_kittizen()
                    ui.add_status(CAPITAL,20)
                    ui.city_loaded = True
            for num, option in enumerate(tutorial_buttons.sprites()):
                if option.clicked:
                    if num == 0:
                        if not ui.city_loaded and load_file("config") != "saved":
                            switch.switches["game_mode"] = 1
                            tutorial.tPart = 1
                            ui.city_loaded = True
                        else:
                            back_up = True
                    elif num == 1:
                        if ui.city_loaded:
                            switch.switches["game_mode"] = 1
                        else:
                            if load_file("config") == "saved":
                                load_game()
                                switch.switches["game_mode"] = 1
                            else:
                                event_handler.add(LOAD_ERROR,None,50)
                    elif num == 2:
                        switch.switches["game_mode"] = 2
                    elif num == 3:
                        switch.switches["game_mode"] = 3
                        scroller.reset()
                    projectile_clip.empty()
                    option.clicked = False
        elif switch.switches["game_mode"] == 1:
            scroller.move()
            city.update()
            city.draw()
            ui.update()
            ui.draw()
            if tutorial.tPart != 0:
                tutorial.update()
            game_buttons.update()
            game_buttons.draw(screen)
            game_speed_button.update()
            game_speed_button.draw()
            for num, option in enumerate(game_buttons.sprites()):
                if option.clicked:
                    if num == 0:
                        if build_on:
                            build_on = False
                        else:
                            build_on = True
                    if num == 1 and tutorial.tPart == 0:
                        save_game()
                        switch.switches["game_mode"] = 0
                    if num == 2 and tutorial.tPart == 0:
                        switch.switches["game_mode"] = 3
                    if num == 3 and tutorial.tPart == 0:
                        scroller.reset()
                        switch.switches["game_mode"] = 2
                    option.clicked = False
            if game_speed_button.clicked and tutorial.tPart == 0:
                game_speed_button.next()
                game_speed_button.clicked = False
            if build_on:
                build_buttons.update()
                build_buttons.draw(screen)
                for num, option in enumerate(build_buttons.sprites()):
                    if option.clicked and tutorial.tPart == 0:
                        city.buy_building(num)
                        option.clicked = False

        elif switch.switches["game_mode"] == 2:
            menuOpts = [switch.switches["fullscreen"],switch.switches["gore"],switch.switches["music"],switch.switches["fps"]]
            for num in range(0,7):
                pygame.draw.rect(screen,colors[num],(0,int(mainCounter+HEIGHT/6*num) % int(HEIGHT*7/6)-HEIGHT/6,WIDTH,HEIGHT/6))
            for num,opt in enumerate(menuOpts):
                if opt:
                    screen.blit(button_font.render("On",True,black),(WIDTH/3*2,HEIGHT/2+num*(TEXT_MARGIN+BUTTON_SIZE)))
                else:
                    screen.blit(button_font.render("Off",True,black),(WIDTH/3*2,HEIGHT/2+num*(TEXT_MARGIN+BUTTON_SIZE)))
            for num,button in enumerate(menu_buttons):
                if option.clicked:
                    if num == 0:
                        if switch.switches["fullscreen"]:
                            switch.switches["fullscreen"] = False
                            pygame.display.set_mode(SCREEN_SIZE)
                        else:
                            switch.switches["fullscreen"] = True
                            pygame.display.set_mode(SCREEN_SIZE,pygame.FULLSCREEN)
                    elif num == 1:
                        if switch.switches["gore"]:
                            switch.switches["gore"] = False
                        else:
                            switch.switches["gore"] = True
                    elif num == 2:
                        if switch.switches["music"]:
                            switch.switches["music"] = False
                        else:
                            switch.switches["music"] = True
                    elif num == 3:
                        if switch.switches["fps"]:
                            switch.switches["fps"] = False
                        else:
                            switch.switches["fps"] = True
                    option.clicked = False
            text("Press backspace to return to the menu",(1,1))
        elif switch.switches["game_mode"] == 3:
            for num in range(0,7):
                pygame.draw.rect(screen,colors[num],(0,int(mainCounter+HEIGHT/6*num) % int(HEIGHT*7/6)-HEIGHT/6,WIDTH,HEIGHT/6))
            scroller.move()
            for num, achiev in enumerate(achievements.list):
                check = achiev if achievements.list[achiev] else "Locked"
                text(check,(WIDTH/2-100,HEIGHT/8+scroller.translateY()+50+110*num))
                screen.blit(pygame.transform.scale(achievements.images[check],(100,100)),(WIDTH/2+100,HEIGHT/8+scroller.translateY()+110*num))
            text("Press backspace to return to the menu",(1,1))
            text("Scroll with the right mouse button", (1,1+TEXT_MARGIN*2))
        elif switch.switches["game_mode"] == 4:
            scroller.move()
            screen.blit(pygame.transform.scale(achievements.victory,(WIDTH,HEIGHT)),(scroller.translateY(),scroller.translateY()))
            text("Press backspace to return to the menu",(1,1))
            text("Scroll with the right mouse button", (1,1+TEXT_MARGIN*2))
        event_handler.update()
        mainCounter+=1
        if switch.switches["fps"]:
            text("FPS:"+str(clock.get_fps())[:5],(1,1))
        pygame.display.update()
        clock.tick(60)
main()
pygame.quit()
