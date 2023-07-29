'''
Paint Program
Elsie Wang
November 19, 2021

This is a paint program with a theme of 'Genshin Impact' that has basic drawing tools and functions.
'''
#=================
#importing everything 
from pygame import *
from random import *
from math import *
from tkinter import *
from tkinter import filedialog
import time

#hiding the small window pop-up while using tkinter
root = Tk()
root.withdraw()

#initiating fonts
font.init()

#================== FUNCTIONS =====================
#function to find if specified point is in a circle
def inCircle (mx, my, x, y, r):
    #uses equation of a circle and checks if the point is less than or equal to the radius (meaning it is in the circle)
    return ((mx - x)**2 + (my - y)**2)**0.5 < r

#function to find distance of two points 
def distance(x1, y1, x2, y2):
    #distance formula is applied to first and second sets of points
    return (sqrt((x1 - x2)**2 + (y1 - y2)**2))

#setting size of screen and displaying screen 
width,height=1200,700
screen=display.set_mode((width,height))

#creating a mask/cover for opacity
cover=Surface((width, height)).convert()

#sets window title to "Genshin Impact Paint"
display.set_caption("Genshin Impact Paint")

#defining colour variables
RED=(207, 62, 39)
BLACK=(82,27,43)
WHITE=(255,255,255)
BEIGE = (230, 204, 184)
accentCol = (247, 232, 220)
accentShapeCol = (82,27,43)

#List for all the colours stored by the palette
palColours = [(255,255,255), (255,255,255), (255,255,255),
              (255,255,255), (255,255,255), (255,255,255),
              (255,255,255), (255,255,255), (255,255,255),
              (255,255,255), (255,255,255), (255,255,255),
              (255,255,255), (255,255,255), (255,255,255),
              (255,255,255), (255,255,255), (255,255,255)]

#loading and blitting background image from top left corner (0,0)
backgroundPic = image.load("Images/background.png")
screen.blit(backgroundPic, (0,0))

#==================== RECTS =======================
#Defining all Rects, use Rects to allow for collidepoint and more convenient access to areas
canvasRect = Rect(160, 85, 865, 575)
saveRect = Rect(20, 20, 50, 50)
loadRect = Rect(90, 20, 50,50)
sizeRect = Rect(180, 30, 400, 30)
sizeSliderRect = Rect(180, 25, 15, 40)

#left side of screen
pencilRect = Rect(15, 130, 60, 60)
brushRect = Rect(85, 130, 60, 60)
eraserRect = Rect(15, 200, 60, 60)
sprayRect = Rect(85, 200, 60, 60)
shapesRect = Rect(15, 290, 60, 60)
stampsRect = Rect(85, 290, 60, 60)
optionsRect = Rect(15, 370, 130, 290)
undoRect = Rect(15, 90, 60, 30)
redoRect = Rect(85, 90, 60, 30)

#right side of screen
colsliderRect = Rect(1040, 250, 10, 20)
colpaletteRect = Rect(1045, 350, 140, 310)
eyedropRect = Rect(1045, 290, 40 , 40)
fillbgRect = Rect(1095, 290, 40, 40)
clearbgRect = Rect(1145, 290, 40, 40)
bgOneRect = Rect(1038, 20, 45, 45)
bgTwoRect = Rect(1091, 20, 45, 45)
bgThreeRect = Rect(1144, 20, 45, 45)

#List containing all rectangles of the colour palette
palColoursRect = [Rect(1055, 390, 30, 30), Rect(1100, 390, 30, 30), Rect(1145, 390, 30, 30),
                  Rect(1055, 435, 30, 30), Rect(1100, 435, 30, 30), Rect(1145, 435, 30, 30),
                  Rect(1055, 480, 30, 30), Rect(1100, 480, 30, 30), Rect(1145, 480, 30, 30),
                  Rect(1055, 525, 30, 30), Rect(1100, 525, 30, 30), Rect(1145, 525, 30, 30),
                  Rect(1055, 570, 30, 30), Rect(1100, 570, 30, 30), Rect(1145, 570, 30, 30),
                  Rect(1055, 615, 30, 30), Rect(1100, 615, 30, 30), Rect(1145, 615, 30, 30)]

#================ DRAWING ITEMS ===================
#Drawing all rectangles onto the screen using predetermined colour and rectangle variables
draw.rect(screen, WHITE, canvasRect)
draw.rect(screen, accentCol, saveRect)
draw.rect(screen, accentCol, loadRect)
draw.rect(screen, accentCol, sizeRect)

#left side
draw.rect(screen, accentCol, pencilRect)
draw.rect(screen, accentCol, brushRect)
draw.rect(screen, accentCol, eraserRect)
draw.rect(screen, accentCol, sprayRect)
draw.rect(screen, accentCol, shapesRect)
draw.rect(screen, accentCol, stampsRect)
draw.rect(screen, accentCol, optionsRect)
draw.rect(screen, accentCol, undoRect)
draw.rect(screen, accentCol, redoRect)

#right side
draw.rect(screen, accentCol, colpaletteRect)
draw.rect(screen, accentCol, eyedropRect)
draw.rect(screen, accentCol, fillbgRect)
draw.rect(screen, accentCol, clearbgRect)
draw.rect(screen, accentCol, bgOneRect)
draw.rect(screen, accentCol, bgTwoRect)
draw.rect(screen, accentCol, bgThreeRect)

#looping through both colour palette lists, using i as index for both
for i in range(len(palColoursRect)):
    draw.rect(screen, palColours[i], palColoursRect[i])

#================== SCREENSHOTS =====================
#Taking screenshots of rectangles around of the colour wheel, colour slider and size slider
#Need these screenshots to blit them later to get rid of the sliders staying on the outside edges
colourwheelCap = screen.subsurface(Rect(1025, 70, 175, 180)).copy()
coloursliderCap = screen.subsurface(Rect(1035, 250, 160, 20)).copy()
sizeCap = screen.subsurface(Rect(180, 25, 400, 40)).copy()

#=================== IMAGES ======================
#Assigning variables to loaded images and adjusting scale of them

#===== TOOLS ======
colwheelPic = image.load("Images/colourwheel.png")
colsliderPic = image.load("Images/colourslider.jpg")
#scaled from the original width and height multiplied by a decimal to maintain the same aspect ratio
colwheelPic = transform.scale(colwheelPic,((int(colwheelPic.get_width()*0.41)), (int(colwheelPic.get_height()*0.41))))
screen.blit(colwheelPic, (1035, 80))

colsliderPic = transform.scale(colsliderPic, (150, 15))
screen.blit(colsliderPic, (1040,252))
colslidergradRect = Rect(1040, 252, 150, 15)

#==== BG PICS =====
inazumaPic = image.load("Images/Inazuma.jpg")
#scaled to match canvas size
inazumaPic = transform.scale(inazumaPic, (865, 575))

liyuePic = image.load("Images/liyue.jpg")
liyuePic = transform.scale(liyuePic, (865, 575))

mondstadtPic = image.load("Images/mondstadt.jpg")
mondstadtPic = transform.scale(mondstadtPic, (865, 575))

#Seperate images loaded for the thumbnails of background image options
#The loaded images are already cropped to be a square so there is no distrotion and the area shown can be adjusted
inazumaPrePic = image.load("Images/InazumaThumbnail.jpg")
#scaled to match thumbnail Rect size
inazumaPrePic = transform.scale(inazumaPrePic, (45, 45))
screen.blit(inazumaPrePic, (1038, 20))

liyuePrePic = image.load("Images/liyueThumbnail.jpg")
liyuePrePic = transform.scale(liyuePrePic, (45, 45))
screen.blit(liyuePrePic, (1091, 20))

mondstadtPrePic = image.load("Images/mondstadtThumbnail.jpg")
mondstadtPrePic = transform.scale(mondstadtPrePic, (45, 45))
screen.blit(mondstadtPrePic, (1144, 20))

#===== TEXT ======
genshinlogoPic = image.load("Images/genshinlogo.png")
genshinlogoPic = transform.scale(genshinlogoPic, (int(genshinlogoPic.get_width()* 0.5), (int(genshinlogoPic.get_height()*0.5))))
screen.blit(genshinlogoPic, (660,3))

#loading in fonts, rendering them and blitting onto screen
fontSmall = font.SysFont("Goudy Stout", 11)
colpaletteLabelTop = fontSmall.render("•Colour•", True, (82,27,43))
colpaletteLabelBtm = fontSmall.render("Palette", True, (82,27,43))
screen.blit(colpaletteLabelTop, (1067, 355))
screen.blit(colpaletteLabelBtm, (1068, 367))

fontBig = font.SysFont("Goudy Stout", 25)
title = fontBig.render(":Paint", True, WHITE)
screen.blit(title, (855, 27))

fontInstruct = font.SysFont("Bahnschrift", 14)
text1 = fontInstruct.render("For eraser and brush tool:", True, WHITE)
text2 = fontInstruct.render("Scroll up to increase opacity and down to decrease opacity", True, WHITE)
screen.blit(text1, (5, 663))
screen.blit(text2, (5, 678))

text3 = fontInstruct.render("Right click to add colour", True, WHITE)
text4 = fontInstruct.render("Left click to get colour", True, WHITE)
screen.blit(text3, (1035, 663))
screen.blit(text4, (1040, 678))

#======== TOOL ICONS ==========

#loading in all images and transforming them to be the correct size
#smoothscale is used with simplier images to makes edges appear smoother
#images are blitting onto screen

pencilPic = image.load("Images/pencil.png")
pencilPic = transform.smoothscale(pencilPic, (60, 60))
screen.blit(pencilPic, (15,130))

brushPic = image.load("Images/brush.png")
brushPic = transform.smoothscale(brushPic, (60, 60))
screen.blit(brushPic, (85,130))

eraserPic = image.load("Images/eraser.png")
eraserPic = transform.smoothscale(eraserPic, (60, 60))
screen.blit(eraserPic, (15,200))

sprayPic = image.load("Images/spraycan.png")
sprayPic = transform.smoothscale(sprayPic, (60, 60))
screen.blit(sprayPic, (85,200))

shapesPic = image.load("Images/shapesicon.png")
shapesPic = transform.smoothscale(shapesPic, (60, 60))
screen.blit(shapesPic, (15, 290))

stampPic = image.load("Images/stamp.png")
stampsPic = transform.smoothscale(stampPic, (55, 55))
screen.blit(stampsPic, (87, 292))

eyedropPic = image.load("Images/eyedropper.png")
eyedropPic = transform.smoothscale(eyedropPic, (40, 40))
screen.blit(eyedropPic, (1045, 290))

fillPic = image.load("Images/paintbucket.png")
fillPic = transform.smoothscale(fillPic, (35, 35))
screen.blit(fillPic, (1098, 293))

clearPic = image.load("Images/trashcan.png")
clearPic = transform.smoothscale(clearPic, (40, 40))
screen.blit(clearPic, (1145, 290))

savePic = image.load("Images/save.png")
savePic = transform.smoothscale(savePic, (40, 40))
screen.blit(savePic, (25, 25))

loadPic = image.load("Images/load.png")
loadPic = transform.smoothscale(loadPic, (40, 40))
screen.blit(loadPic, (95, 25))

undoPic = image.load("Images/undo.png")
undoPic = transform.smoothscale(undoPic, (40, 25))
screen.blit(undoPic, (25, 93))

redoPic = image.load("Images/redo.png")
redoPic = transform.smoothscale(redoPic, (40, 25))
screen.blit(redoPic, (95, 93))
#========= STAMP ICONS ==========
pyroPic = image.load("Images/pyro.png")
pyroPic = transform.scale(pyroPic,((int(pyroPic.get_width()*0.4)), (int(pyroPic.get_height()*0.4))))

geoPic = image.load("Images/geo.png")
geoPic = transform.scale(geoPic,((int(pyroPic.get_width()*0.8)), (int(pyroPic.get_height()*0.8))))

dendroPic = image.load("Images/dendro.png")
dendroPic = transform.scale(dendroPic,((int(dendroPic.get_width()*0.4)), (int(dendroPic.get_height()*0.4))))

amenoPic = image.load("Images/ameno.png")
amenoPic = transform.scale(amenoPic,((int(amenoPic.get_width()*0.4)), (int(amenoPic.get_height()*0.4))))

cyroPic = image.load("Images/cyro.png")
cyroPic = transform.scale(cyroPic,((int(cyroPic.get_width()*0.4)), (int(cyroPic.get_height()*0.4))))

hydroPic = image.load("Images/hydro.png")
hydroPic = transform.scale(hydroPic,((int(hydroPic.get_width()*0.4)), (int(hydroPic.get_height()*0.4))))

electroPic = image.load("Images/electro.png")
electroPic = transform.scale(electroPic,((int(electroPic.get_width()*0.4)), (int(electroPic.get_height()*0.4))))



#==================== TOP LAYER =====================
#drawing rectangles that are on top layer (above everything else) and must appear from start
draw.rect(screen, RED, colsliderRect)
draw.rect(screen, RED, sizeSliderRect)

#================== DICTIONARIES ====================
#dicitonaries for shapes, stamp rectangles and stamp pictures
#these are used to iterate through the dictionaries instead of going through each element seperately 
shapes = {"rect": Rect(25, 380, 50, 50), "ellipse": Rect(85, 380, 50, 50),
          "fillrect": Rect(25, 440, 50, 50), "fillellipse": Rect(85, 440, 50, 50),
          "line": Rect(25, 500, 50, 50)
          }

stampsRectDic = {"stamp1": Rect(25, 380, 50, 50), "stamp2": Rect(85, 380, 50, 50),
                 "stamp3": Rect(25, 440, 50, 50), "stamp4": Rect(85, 440, 50, 50),
                "stamp5": Rect(25, 500, 50, 50), "stamp6": Rect(85, 500, 50, 50),
                "stamp7": Rect(25, 560, 50, 50)
          }

stampsPic = {"stamp1": pyroPic, "stamp2": geoPic, "stamp3": dendroPic, "stamp4": amenoPic,
             "stamp5": cyroPic, "stamp6": hydroPic, "stamp7": electroPic}

#iterates through each shape preview rectangle and draws them onto screen
for shape in shapes:
        draw.rect(screen, BEIGE, shapes[shape])

#draws each of the small shape previews
draw.rect(screen, accentShapeCol, (30, 390, 40, 30), 3)
draw.ellipse(screen, accentShapeCol, (90, 387, 40, 35), 3)
draw.rect(screen, accentShapeCol, (30, 450, 40, 30))
draw.ellipse(screen, accentShapeCol, (90, 447, 40, 35))
draw.line(screen, accentShapeCol, (30, 510), (70, 540), 3)

#================== PLACEHOLDERS ====================
#placeholders that will be changed later on as events occur

purecolour = Color(0,0,0,0) #colour without applying saturation settings
colour = Color(0,0,0,0) #colour after adding saturation settings
tool = "pencil" #current tool being selected/used
saturation = Color(0,0,0,0) #saturation level (pygame Color type to be able to add to 'purecolour'
bgColour = (255,255,255) #current background colour
maxSize = 5 #maximum size that can be set on the size slider
size = 1 #current size
trans = 255
selection = "shapes" #selection of stamps or shapes on the menu located on the bottom left corner
bgPic = False #if a background picture is currently being used
drawing = False #if the user is drawing something on the canvas
undo=[(screen.subsurface(canvasRect)).copy()] #list that stores copies of the screen to blit for undos
redo=[] #list that stores redo screenshots

running = True #running boolean

screenCap = screen.subsurface(canvasRect).copy() #takes a screenshot of only the canvas area and assigns it to the variable 'screenCap'

while running: #while running is True loop
    screen.set_clip(None) #setting the changeable area to everything to allow for drawing of tools, sliders, ect.
    leftclick = False #leftclick is set to False as a default 
    mouseup = False #mouseup is False unless otherwise stated
    for evt in event.get(): #getting current events
        if evt.type==QUIT: #stops running is the window is closed
            running=False
        if evt.type == MOUSEBUTTONDOWN: #if a mouse button is pressed and it is the left button, 'leftclick' is True
            cover.fill((255,0,255)) #mask is filled with transparency mask colour
            if evt.button == 1: #when left click is pressed, 'leftclick' is set to True
                leftclick = True
        if evt.type == MOUSEBUTTONUP: #if mouse button is lifted, drawing is set to False and 'mouseup' variable is turned to True
            if evt.button == 4: #if mouse is being scrolled up, transparency variable increases by 10
                trans += 10
                trans = min (trans, 255) #makes sure 'trans' is less than 255 otherwise trans stays as 255
            if evt.button == 5: #if mouse is being scrolled down, transparency variable decreases by 10
                trans -= 10
                trans = max (15, trans) #makes sure trans is greater than 15 (makes sure it is still visible)
            drawing = False #when the mouse is lifted, drawing is set to False
            mouseup = True #'mouseup' is set to True

            #when the mouse is lifted and within canvas add a screenshot of the canvas to undo list
            #doesn't append screenshot is mouse is only scrolled up or down because nothing is changed on canvas
            if canvasRect.collidepoint(mx,my) and evt.button != 4 and evt.button != 5:
                undo.append(screen.subsurface(canvasRect).copy())

    mx,my=mouse.get_pos() #gets current position of mouse
    mb=mouse.get_pressed() #gets which mouse buttons are pressed
                

#================ TOOL SELECTION ==================
    #========= COLOUR WHEEL ===========
    if inCircle(mx, my, 1116, 161, 81): #uses 'inCircle' function to check if mouse position is inside the circle of the colour wheel
        #colour that the mouse is hovering over on the colour wheel, getting the colour from the picture instead of screen to avoid getting colour from preview/hover
        #circle, mouse positions are subtracted by starting x and y position of colour wheel to find position of mouse in respect to colour wheel area
        hoverCol = colwheelPic.get_at((mx-1035,my-80)) #colour that the mouse is hovering over on the colour wheel,
        if mb[0] and drawing == False: #if left click is being pressed/held and user is not drawing...
            purecolour = hoverCol #'purecolour' is changed to be the colour being hovered over
            
            #blitting screenshot of rectangle surrounding colour wheel so when the preview is moved to the edge of circle, the preview circle doesn't stay there
            screen.blit(colourwheelCap, (1025, 70)) #blitting screenshot of rectangle surrounding colour wheel so when the preview is moved to the edge of circle, the 
            screen.blit(colwheelPic, (1035, 80)) #blitting screenshot of colour wheel so preview circle is being moved, not leaving trail
            draw.circle(screen, BEIGE, (mx,my), 8) #draws circle with beige "outline" and colour being hovered over
            draw.circle(screen, hoverCol,(mx,my), 6)
            colour = purecolour -  saturation
            #subtracts saturation Color variable from the pure colour form to get new colour, the darker the colour -> the smaller the rgb values and vice versa,
            #therefore getting a black, white or beige value and subtracting that value will result in changing darkness of colour
            mouse.set_visible(False) #mouse is set to invisible so colours can be seen easier
            
    if evt.type == MOUSEBUTTONUP: #if mouse button is lifted, mouse can be seen again
        mouse.set_visible(True)
        

    #========= COLOUR SLIDER ===========
    if colslidergradRect.collidepoint((mx,my)): #if mouse is on the colour slider...
        if mb[0] and drawing == False: #if left mouse is clicked or held and user is not drawing...
            colour = purecolour #purecolour is set to the current colour
            screen.blit(coloursliderCap, (1035, 250)) #screenshot of screen slightly larger than colour gradient is shown to get rid of any overhang
            screen.blit(colsliderPic, (1040,252)) #colour gradient is shown  
            colsliderRect[0] = mx-5 #x coordinate of colour slider is changed to be 5 less than mouse x position (half of colour slider width)
            if colsliderRect[0] >= 1180: #makes sure colour slider is within the colour gradient
                colsliderRect[0] = 1180
            if colsliderRect[0] <= 1040:
                colsliderRect[0] = 1040
            draw.rect(screen, RED, colsliderRect) #draws the new colour slider
        
            saturation = colsliderPic.get_at((mx-1040, 10)) #saturation is found by getting the greyscale value of colour gradient where the mouse is (in respect to picture)
            for i in range(3): #subtracts value from 255 to get 'saturation', repeats 3 times for each rgb value
                saturation[i] = 255 - saturation[i]
            colour = purecolour -  saturation 
                        
    #============= PENCIL ===============
    if tool == "pencil": #if tool is already pencil, black outline is drawn (same is done with every tool that can be 'selected')
        draw.rect(screen, BLACK, pencilRect, 3)
    else: #otherwise, outline "disapears"
        draw.rect(screen, accentCol, pencilRect, 3)
        
    if pencilRect.collidepoint((mx,my)) and tool != "pencil": #if mouse is on rectangle and tool is not already pencil, red outline temporarily appears
        draw.rect(screen, RED, pencilRect, 3)
        if leftclick == True: #if tool rectangle is clicked...
            tool = "pencil" #tool is set to be pencil
            size = 1 #size is reset to 1
            sizeSliderRect = Rect(180, 25, 15, 40) #size slider is reset to be at beginning
            maxSize = 3 #maximum size that is compatible with tool is determined

    

    #============== BRUSH ===============
    if tool == "brush":
        draw.rect(screen, BLACK, brushRect, 3)
        cover.set_alpha(trans) #transparency is set to 'cover'
        cover.set_colorkey((255, 0 , 255)) #uses mask colour to show each pixel's opacity
    else:
        draw.rect(screen, accentCol, brushRect, 3)
        
    if brushRect.collidepoint((mx,my)) and tool != "brush":
        draw.rect(screen, RED, brushRect, 3)
        if leftclick == True:
            tool = "brush"
            size = 1
            sizeSliderRect = Rect(180, 25, 15, 40)
            maxSize = 100
        
        
    #============= ERASER ===============
    if tool == "eraser":
        draw.rect(screen, BLACK, eraserRect, 3)
        cover.set_alpha(trans)
        cover.set_colorkey((255, 0 , 255))
    else:
        draw.rect(screen, accentCol, eraserRect, 3)
        
    if eraserRect.collidepoint((mx,my)) and tool != "eraser":
        draw.rect(screen, RED, eraserRect, 3)
        if leftclick == True:
            tool = "eraser"
            size = 1
            sizeSliderRect = Rect(180, 25, 15, 40)
            maxSize = 100
        
    #============== SAVE ================
    if saveRect.collidepoint((mx,my)):
        draw.rect(screen, RED, saveRect, 3) #if mouse is on save rectangle, there is a red outline
        if leftclick == True: #if left mouse button is clicked file dialog prompts for user to enter save name, the default extension is "png"
            savename = filedialog.asksaveasfilename(defaultextension = "png")
            if savename != "": #if save name is not left as empty, image of canvas rectangle is saved
                image.save(screen.subsurface(canvasRect), savename)
    else:
        draw.rect(screen, accentCol, saveRect, 3) #if mouse is not on save rectangle, outline is covered by resting colour
    #^^ this way of setting outlines is used with tools that can only be pressed and can not be selected/drawn with        

    #=============== LOAD ===============
    if loadRect.collidepoint((mx, my)):
        draw.rect(screen, RED, loadRect,3)
        if leftclick == True:
            loadname = filedialog.askopenfilename() #prompts user to enter load name
            ext = loadname[-3::1] #finds extension by getting last three characters of load name
            if ext == "png" or ext == "jpg": #only if extension is "png" or "jpg"...
                picture = image.load(loadname) #picture is loaded from load name
                draw.rect(screen, WHITE, canvasRect) #canvas is cleared
                width = picture.get_width()
                height = picture.get_height()
                if width > 865: #if width is larger than canvas size, width is set to be 865
                    width = 865 #we still need variable for latter transformations and to retain width if it is less than 865
                    picture = transform.scale(picture, (865, height)) #picture is scaled to have width of 865
                if height > 575: #if height is larger than canvas height, height is set to 575
                    picture = transform.scale(picture, (width, 575))
                screen.blit(picture, (160, 85)) #picture is blitted
    else:
        draw.rect(screen, accentCol, loadRect, 3)
            
        

    #=============== SIZE ===============
    interval = 400//maxSize #intervals of possible sizes is found by dividing 400 (length of size bar) by maximum size
    screen.blit(sizeCap, (180, 25)) #screenshot of area slightly larger than size bar is blitted to get rid of overhang
    draw.rect(screen, accentCol, sizeRect) #size bar is drawn
    draw.rect(screen, RED, sizeSliderRect) #size slider is drawn
    
    if sizeRect.collidepoint((mx,my)): #if mouse is on size slider...
        if mb[0] and drawing == False: #if left mouse button is clicked or held and user is not drawing...
            screen.blit(sizeCap, (180, 25)) 
            draw.rect(screen, accentCol, sizeRect)
            sizeSliderRect[0] = mx-5 
            if sizeSliderRect[0] >= 565:
                sizeSliderRect[0] = 565
            if sizeSliderRect[0] <= 180:
                sizeSliderRect[0] = 180
            draw.rect(screen, RED, sizeSliderRect)

            if 565 > mx > 180: #if mouse x-axis is within size bar...
                size = maxSize - ((400 - (mx - 180))//interval)
                #divides mouse x position by interval to find which 'section' of size mouse is in,
                #subtracts this from max size to get final size
                    

    #========== EYE DROPPER ============
    if eyedropRect.collidepoint((mx,my)) and tool != "eyedropper":
        draw.rect(screen, RED, eyedropRect,3)
        if leftclick == True: #if eye drop tool is selected...
            preTool = tool #previous tool is saved so it can switch back to it later
            tool = "eyedropper"
            
    if tool == "eyedropper":
        draw.rect(screen, BLACK, eyedropRect, 3)
        if mb[0] and canvasRect.collidepoint((mx,my)): #if canvas is clicked...
            colour = screen.get_at((mx,my)) #colour is changed to be colour at mouse position
            tool = preTool #changed back to previous tool
    else:
        draw.rect(screen, accentCol, eyedropRect, 3)
        


    #========== SPRAY PAINT ============
    if tool == "spray":
        draw.rect(screen, BLACK, sprayRect, 3)
    else:
        draw.rect(screen, accentCol, sprayRect, 3)
        
    if sprayRect.collidepoint((mx,my)) and tool != "spray":
        draw.rect(screen, RED, sprayRect, 3)
        if leftclick == True:
            tool = "spray"
            size = 1
            sizeSliderRect = Rect(180, 25, 15, 40)
            maxSize = 50

    #========== CLEAR BG ============
    if clearbgRect.collidepoint((mx,my)):
        draw.rect(screen, RED, clearbgRect, 3)
        if leftclick == True:
            if bgPic: #if there is a background picture blits the selected image
                if bgPic == "inazuma":
                    screen.blit(inazumaPic, (160,85))
                if bgPic == "liyue":
                    screen.blit(liyuePic, (160,85))
                if bgPic == "mondstadt":
                    screen.blit(mondstadtPic, (160,85))
                
            else: #otherwise, screen is filled with background colour
                draw.rect(screen, bgColour, canvasRect)
            screenCap = screen.subsurface(canvasRect).copy() #screenshot is taken/reset
    else:
        draw.rect(screen, accentCol, clearbgRect, 3)
            

    #=======  COLOUR PREVIEW ========
    draw.rect(screen, colour, (600, 25, 40, 40)) #rectangle is drawn with current colour as a preview

    #============ SHAPE =============
    if selection == "shapes": 
        draw.rect(screen, BLACK, shapesRect, 3)
    else:
        draw.rect(screen, accentCol, shapesRect, 3)
        
    if shapesRect.collidepoint((mx,my)) and selection != "shapes": 
        draw.rect(screen, RED, shapesRect, 3)
        if leftclick == True: #if selection is changed to shapes...
            selection = "shapes"
            draw.rect(screen, accentCol, optionsRect)
            for shape in shapes: #for each shape in shapes...
                draw.rect(screen, BEIGE, shapes[shape]) #previews are drawn
            draw.rect(screen, accentShapeCol, (30, 390, 40, 30), 3)
            draw.ellipse(screen, accentShapeCol, (90, 387, 40, 35), 3)
            draw.rect(screen, accentShapeCol, (30, 450, 40, 30))
            draw.ellipse(screen, accentShapeCol, (90, 447, 40, 35))
            draw.line(screen, accentShapeCol, (30, 510), (70, 540), 3)
    
    
    for shape in shapes:
        if tool == shape:
            draw.rect(screen, BLACK, shapes[shape], 3)
        else:
            draw.rect(screen, accentCol, shapes[shape], 3)
            
        if shapes[shape].collidepoint((mx,my)) and tool != shape and selection == "shapes":
            draw.rect(screen, RED, shapes[shape], 3)
            if leftclick == True:
                screenCap = screen.subsurface(canvasRect).copy()
                tool = shape
                size = 1
                sizeSliderRect = Rect(180, 25, 15, 40)

    #=========== STAMP =============
    if selection == "stamps": 
        draw.rect(screen, BLACK, stampsRect, 3)
        for stamp in stampsRectDic:
            if tool == stamp:
                draw.rect(screen, BLACK, stampsRectDic[stamp], 3)
            else:
                draw.rect(screen, accentCol, stampsRectDic[stamp], 3)
                
            if stampsRectDic[stamp].collidepoint((mx,my)) and tool != stamp and selection == "stamps":
                draw.rect(screen, RED, stampsRectDic[stamp], 3)
                if leftclick == True:
                    screenCap = screen.subsurface(canvasRect).copy()
                    tool = stamp
                    maxSize = 20
                    size = 1
                    sizeSliderRect = Rect(180, 25, 15, 40)
    else:
        draw.rect(screen, accentCol, stampsRect, 3)
        
    if stampsRect.collidepoint((mx,my)) and selection != "stamps": 
        draw.rect(screen, RED, stampsRect, 3)
        if leftclick == True: #if selection is changed to be stamps...
            selection = "stamps"
            draw.rect(screen, accentCol, optionsRect)
            for stamp in stampsRectDic: #previews are drawn
                draw.rect(screen, BEIGE, stampsRectDic[stamp])
                stampPrePic = transform.scale(stampsPic[stamp], (40,40))
                screen.blit(stampPrePic, ((stampsRectDic[stamp])[0]+5, (stampsRectDic[stamp])[1]+5))

    

    #=========== FILL BG ============
    if fillbgRect.collidepoint((mx,my)):
        draw.rect(screen, RED, fillbgRect, 3)
        if leftclick == True:
            bgPic = "" #background picture is changed to be False
            bgColour = colour #background colour is changed to be selected colour
            draw.rect(screen, bgColour, canvasRect) #canvas is filled with this colour
            screenCap = screen.subsurface(canvasRect).copy() #screenshot is taken
    else:
        draw.rect(screen, accentCol, fillbgRect, 3)
            
        
    #=========== BG 1 ============
    if bgPic == "inazuma":
        draw.rect(screen, BLACK, bgOneRect, 3)
    else:
        draw.rect(screen, accentCol, bgOneRect, 3)
        
    if bgOneRect.collidepoint((mx,my)) and bgPic != "inazuma": 
        draw.rect(screen, RED, bgOneRect, 3)
        if leftclick == True:
            bgPic = "inazuma" #background picture is set to corresponding background
            bgColour = WHITE #background colour is set to be white 
            screen.blit(inazumaPic, (160,85))
            screenCap = screen.subsurface(canvasRect).copy()
            undo =[(screen.subsurface(canvasRect)).copy()] #undo and redo list is reset (makes sure user cannot undo to a different background state)
            redo = []
        
    #=========== BG 2 ============
    if bgPic == "liyue":
        draw.rect(screen, BLACK, bgTwoRect, 3)
    else:
        draw.rect(screen, accentCol, bgTwoRect, 3)
        
    if bgTwoRect.collidepoint((mx,my)) and bgPic != "liyue":
        draw.rect(screen, RED, bgTwoRect, 3)
        if leftclick == True:
            bgPic = "liyue"
            bgColour = WHITE
            screen.blit(liyuePic, (160,85))
            screenCap = screen.subsurface(canvasRect).copy()
            undo =[(screen.subsurface(canvasRect)).copy()]
            redo = []

    #=========== BG 3 ============
    if bgPic == "mondstadt":
        draw.rect(screen, BLACK, bgThreeRect, 3)
    else:
        draw.rect(screen, accentCol, bgThreeRect, 3)
        
    if bgThreeRect.collidepoint((mx,my)) and bgPic != "monstadt":
        draw.rect(screen, RED, bgThreeRect, 3)
        if leftclick == True:
            bgPic = "mondstadt"
            bgColour = WHITE
            screen.blit(mondstadtPic, (160,85))
            screenCap = screen.subsurface(canvasRect).copy()
            undo =[(screen.subsurface(canvasRect)).copy()]
            redo = []

    #=========== UNDO ============
    if undoRect.collidepoint(mx,my):
        draw.rect(screen, RED, undoRect, 3)
        if leftclick == True:
            if len(undo) >= 2: #if undo is pressed and undo list is greater than or equal to 2...
                screen.blit(undo[-2], (160, 85)) #the second last element in undo list is blitted (second last, not last because last is what is shown on screen currently)
                redo.append(undo.pop()) #last element of undo is removed and added to redo list
    else:
        draw.rect(screen, accentCol, undoRect, 3)

    #=========== REDO =============
    if redoRect.collidepoint(mx,my):
        draw.rect(screen, RED, redoRect, 3)
        if leftclick == True:
            if len(redo) >= 1: #if redo is pressed and there is at least 1 element...
                screen.blit(redo[-1], (160, 85)) #last element in redo list is blitted
                undo.append(redo.pop()) #last element is removed from redo and added to undo list
    else:
        draw.rect(screen, accentCol, redoRect, 3)

    #======= COLOUR PALETTE ========
    for i in range(len(palColoursRect)):
        if palColoursRect[i].collidepoint(mx,my):
            if leftclick:
                colour = palColours[i] #if colour palette rectangle is left clicked, colour is changed to be colour of rectangle clicked
            if mb[2]:
                palColours[i] = colour #if right clicked, colour in palette is changed to be selected colour
                draw.rect(screen, palColours[i], palColoursRect[i]) #palette rectangle is redrawn with new colour
        
#=================== DRAWING ======================
    if mb[0]:
        screen.set_clip(canvasRect)
        #============ PENCIL ============
        if tool == "pencil":
            if canvasRect.collidepoint((mx,my)):
                drawing = True
                draw.line(screen, colour, (oldmx, oldmy), (mx,my), size) #line is drawn from mouse position from previous loop to where mouse is now to create a smooth line
            
        
            
        #============ ERASER ============
        if tool == "eraser" and canvasRect.collidepoint((mx,my)):
            if evt.type == MOUSEBUTTONDOWN: #if mouse button is pressed...
                screenCap = screen.subsurface(canvasRect).copy()
            drawing = True 
            dx = mx-oldmx #finds distance between old and new x and y postitions
            dy = my-oldmy
            dist = distance(oldmx, oldmy, mx, my) #uses distance function to find disstance between two positions
        
            for d in range(1, int(dist)): #for every pixel between original and new postions...
                dotx = dx * d/dist + oldmx
                doty = dy * d/dist + oldmy
                draw.circle(cover, bgColour, (int(dotx), int(doty)), size) #circle is drawn at each place in slope
            screen.blit(screenCap, (160, 85))
            screen.blit(cover, (0,0)) #blits the transparency mask on top of previous canvas

        #============ SPRAY ============
        if tool == "spray" and canvasRect.collidepoint((mx,my)):
            drawing = True
            randx = randint(mx-size,mx+size) #finds random integer in square around mouse position in size
            randy = randint(my-size,my+size)
            if inCircle(randx, randy, mx, my, size): #checks if both x and y are within circle using function
                draw.circle(screen, colour, (randx, randy),1) #if it is, the circle is drawn
                time.sleep(0.005) #very slight delay to make spray better looking

        #=========== BRUSH ============
        #same way of drawing as eraser tool but with a colour
        if tool == "brush" and canvasRect.collidepoint((mx,my)):
            if evt.type == MOUSEBUTTONDOWN:
                screenCap = screen.subsurface(canvasRect).copy()
            drawing = True
            dx = mx-oldmx
            dy = my-oldmy
            dist = distance(oldmx, oldmy, mx, my)
        
            for d in range(1, int(dist)):
                dotx = dx * d/dist + oldmx
                doty = dy * d/dist + oldmy
                draw.circle(cover, colour, (int(dotx), int(doty)), size)
            screen.blit(screenCap, (160, 85))
            screen.blit(cover, (0,0))
                
    
    #============ LINE ============
    if tool == "line":
        maxSize = 20
        screen.set_clip(canvasRect) #makes sure only area in canvas can be drawn on
        if leftclick:
            ix, iy = evt.pos #gets x and y position when left mouse button is clicked
                
        if evt.type == MOUSEBUTTONUP: #if mouse if lifted,
            drawing = False
            screen.blit(screenCap, (160, 85))
            draw.line(screen, colour, (ix, iy), (mx, my), size) #a line is drawn between first and new position
            screenCap = screen.subsurface(canvasRect).copy() #a screenshot is taken, line is drawn and remains there
        screen.blit(screenCap, (160, 85)) #screenshot is blitted to remove trail
        
    
        if mb[0]: #if left click is held or clicked
            drawing = True
            draw.line(screen, colour, (ix, iy), (mx, my), size) #(preview line)
            
    #============ RECT ============
    if tool == "rect":
        maxSize = 20
        
        if leftclick:
            ix, iy = evt.pos
            
        screen.set_clip(canvasRect)
        drawRect = Rect(ix, iy, mx-ix, my-iy) #rectangle that is about to be drawn
        drawRect.normalize() #normalized to fix negative values (drawing from bottom corners)
        maxLength = min(size, drawRect[2]) #makes sure length and width is not exceeding size (fixes very small rectangles)
        maxWidth = min(size, drawRect[3])

        if evt.type == MOUSEBUTTONUP:
            drawing = False
            screen.blit(screenCap, (160, 85))
            #four seperate rectangles are drawn for each side, uses this instead of one rectangle to fix corners
            draw.rect(screen, colour, (drawRect[0], drawRect[1], drawRect[2], maxWidth))
            draw.rect(screen, colour, (drawRect[0], drawRect[3]+drawRect[1]-maxWidth, drawRect[2], maxWidth))
            draw.rect(screen, colour, (drawRect[0], drawRect[1], maxLength, drawRect[3]))
            draw.rect(screen, colour, (drawRect[2]+drawRect[0]-maxLength, drawRect[1], maxLength, drawRect[3]))
            #same preview function as line tool
        
            screenCap = screen.subsurface(canvasRect).copy()
        screen.blit(screenCap, (160, 85))
        
        if mb[0]:
            drawing = True
            draw.rect(screen, colour, (drawRect[0], drawRect[1], drawRect[2], maxWidth))
            draw.rect(screen, colour, (drawRect[0], drawRect[3]+drawRect[1]-maxWidth, drawRect[2], maxWidth))
            draw.rect(screen, colour, (drawRect[0], drawRect[1], maxLength, drawRect[3]))
            draw.rect(screen, colour, (drawRect[2]+drawRect[0]-maxLength, drawRect[1], maxLength, drawRect[3]))
            

    #============ FILL RECT ============
    #same as unfilled rectangle however rectangle that is being drawn is just one because there is no corner problem
    if tool == "fillrect":
        sizeSliderRect = Rect(0, 0, 0, 0)
        maxSize = 1
        screen.set_clip(canvasRect)
        if leftclick:
            ix, iy = evt.pos
            
        fillRect = Rect(ix, iy, mx-ix, my-iy)
        fillRect.normalize()

        if evt.type == MOUSEBUTTONUP:
            drawing = False
            screen.blit(screenCap, (160, 85))
            draw.rect(screen, colour, fillRect)
            screenCap = screen.subsurface(canvasRect).copy()
        screen.blit(screenCap, (160, 85))
        
        if mb[0]:
            drawing = True
            draw.rect(screen, colour, fillRect)

    #========== ELLIPSE ===========
    #same as rectangle tool except drawing ellipses
    if tool == "ellipse":
        maxSize = 20
        screen.set_clip(canvasRect)
        if leftclick:
            ix, iy = evt.pos
            
        ellRect = Rect(ix, iy, mx-ix, my-iy)
        ellRect.normalize()

        if evt.type == MOUSEBUTTONUP:
            drawing = False
            screen.blit(screenCap, (160, 85))
            
            draw.ellipse(screen, colour, ellRect, size)
            screenCap = screen.subsurface(canvasRect).copy()
        screen.blit(screenCap, (160, 85))
        
        if mb[0]:
            drawing = True
            draw.ellipse(screen, colour, ellRect, size)

    #==========  FILLED ELLIPSE ===========
    if tool == "fillellipse":
        sizeSliderRect = Rect(0, 0, 0, 0)
        maxSize = 1
        screen.set_clip(canvasRect)
        if leftclick:
            ix, iy = evt.pos
            
        ellRect = Rect(ix, iy, mx-ix, my-iy)
        ellRect.normalize()

        if evt.type == MOUSEBUTTONUP:
            screen.blit(screenCap, (160, 85))
            draw.ellipse(screen, colour, ellRect)
            screenCap = screen.subsurface(canvasRect).copy()
        screen.blit(screenCap, (160, 85))
        
        if mb[0]:
            drawing = True
            draw.ellipse(screen, colour, ellRect)

    #========== STAMPS ============
    for stamp in stampsPic:
        if tool == stamp:
            screen.set_clip(canvasRect)
            if mb[0]:
                drawing = True
                scale = 1 + size/10 #sets scale factor to 1 + (size divided by 10) multiples this value by width and height to adjust size of stamp accordingly
                stampPicResize = transform.scale(stampsPic[stamp],((int(stampsPic[stamp].get_width()*scale)), (int(stampsPic[stamp].get_height()*scale))))
                screen.blit(screenCap, (160, 85))
                #draws stamp at mouse postition subtracted by half of width/height to have mouse be at middle of stamp
                screen.blit(stampPicResize, (mx-(stampPicResize.get_width()//2), my-(stampPicResize.get_height()//2)))
                #same preview method as line tool
            if evt.type == MOUSEBUTTONUP:
                drawing = False
                screen.blit(stampPicResize, (mx-(stampPicResize.get_width()//2), my-(stampPicResize.get_height()//2)))
                screenCap = screen.subsurface(canvasRect).copy()

    #sets current mouse positions to be old mouse positions that are saved for next iteration of loop
    oldmx, oldmy = mx, my

    display.flip() #display is flipped/properly shown
            
quit() #quits when running stops
