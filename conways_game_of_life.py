from platform import platform
import sys
from tkinter import mainloop
import turtle as t
import random
import pickle
import time
## Global Variablen
clear = "\n" * 100
print(clear)
def logo():
    print("   ___                               _                   ")
    print("  / __\___  _ ____      ____ _ _   _( )__                ")
    print(" / /  / _ \| '_ \ \ /\ / / _` | | | |/ __|               ")
    print("/ /__| (_) | | | \ V  V / (_| | |_| |\__ \               ")
    print("\____/\___/|_| |_|\_/\_/ \__,_|\__, ||___/               ")
    print("                               |___/                     ")
    print("   ___                              __     __ _  __      ")
    print("  / _ \__ _ _ __ ___   ___    ___  / _|   / /(_)/ _| ___ ")
    print(" / /_\/ _` | '_ ` _ \ / _ \  / _ \| |_   / / | | |_ / _ \ ")
    print("/ /_\\\\ (_| | | | | | |  __/ | (_) |  _| / /__| |  _|  __/")
    print("\____/\__,_|_| |_| |_|\___|  \___/|_|   \____/_|_|  \___|")
    print("                                                         ")
logo()
if len(sys.argv)<3:
    print("Bitte sende beim Start der Anwendung 2 Argumente mit.\n    Grid size als erstes Argument.\n    Länge der Würfel in px als zweites Argument.")
    exit()
grid=sys.argv[1]
length_of_quader=sys.argv[2]
size=int(length_of_quader)*int(grid)
start_calc=(int(length_of_quader)*int(grid))/2
new_startposi=-abs(start_calc),(start_calc)
new_startposit=-abs(start_calc),(start_calc)
g_grid=int(grid)/2
flist=[]
update_list=[]
print("    Grid: "+grid +"\n    Quadrat Länge: "+ length_of_quader + "\n    Size: "+ str(size)+ "\n    Start Calc: "+ str(start_calc)) ## test
print("    Start Position: "+str(new_startposi)+"\n")

def help():
    print("Press C for 1 random block              Press Y to save the game")
    print("Press S for 1 Generation interval       Press X to load the savestate")
    print("Press D for 20 Generation interval      Press V to reload the board")
    print("Press F for 50 Generation interval      Press Q to to quit the game and close the window")
def loadgame():
    with open('savefile.dat', 'rb') as f:
        gamestate, lengthsave, gridsave = pickle.load(f)
    x=0
    y=0
    global ts, new_startposi
    for x in ts:
        for y in x:
            y.clear()
    grid=gridsave
    ts = [] # Baustein
    t2d= [] # 2d matrix
    nr= [] 
    i=0
    j=0
    while j<grid:
        while i<grid:
            t2d.append(t.Turtle())
            i+=1
        ts.append(t2d)
        j+=1
        t2d= []
        i=0
    i=0
    for x in ts:
        for y in x:
            i+=1
            y.speed(10)
            y.shape('arrow')
            startpos(y)
            y.turtlesize(1,1)
            if i==grid:
                i=0
                new_startposi=-abs(start_calc),new_startposi[1]-int(length_of_quader)
    new_startposi=new_startposit
    for x in ts:
        for y in x:
            i+=1
            y.speed(10)
            quadrat2(y,lengthsave)
    for x in gamestate:
        if x[2]==1:
            belebe(ts[x[0]][x[1]])
    ts.reverse()
    t.update()
def savegame():
    gamestate=[]
    lengthsave=int(length_of_quader)
    gridsave=int(grid)
    x=0
    y=0
    for i in ts:
        for j in i:
            a=death_or_alive(x,y)
            if a == False:
                ii=x,y,0
                #print(ii)
                gamestate.append(ii)
            else:
                ii=x,y,1
                #print(ii)
                gamestate.append(ii)
            y+=1
        x+=1
        y=0
    x=0
    with open('savefile.dat', 'wb') as f:
        pickle.dump([gamestate, lengthsave, gridsave], f, protocol=2)
def no_duplicates(x):
    seen = set()
    newlist = []
    for item in x:
        t = tuple(item)
        if t not in seen:
            newlist.append(item)
            seen.add(t)
    return newlist
def get_neighbors(x,y):
    A=[]
    X = int(grid)
    Y = int(grid)
    neighbors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                               for y2 in range(y-1, y+2)
                               if (-1 < x <= X and
                                   -1 < y <= Y and
                                   (x != x2 or y != y2) and
                                   (0 <= x2 <= X) and
                                   (0 <= y2 <= Y))]
    for i in neighbors(x,y):
        xx=i[0]
        yy=i[1]
        if xx==int(grid) or yy==int(grid):
            continue
        A.append(i)
    return A
def game_clear():
    global ts
    for x in ts:
        for y in x:
            y.clear()
    main()
def belebe(this):
        #print("belebt")
        i=0
        this.fillcolor("black")
        this.begin_fill()
        while i < 4:
            this.fd(int(length_of_quader))
            this.rt(90)
            i=i+1
        this.end_fill()
        this.hideturtle()
def kill(this):
        i=0
        this.fillcolor("white")
        this.begin_fill()
        while i < 4:
            this.fd(int(length_of_quader))
            this.rt(90)
            i=i+1
        this.end_fill()
        this.hideturtle()
def rule(x,y):
    global flist, update_list
    z=0
    X = int(grid)
    Y = int(grid)
    neighbors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                               for y2 in range(y-1, y+2)
                               if (-1 < x <= X and
                                   -1 < y <= Y and
                                   (x != x2 or y != y2) and
                                   (0 <= x2 <= X) and
                                   (0 <= y2 <= Y))]
    for i in neighbors(x,y):
        xx=i[0]
        yy=i[1]
        if xx==int(grid) or yy==int(grid):
            continue
        a=death_or_alive(xx,yy)
        d=death_or_alive(x,y)

        if a == True:
            z+=1
    r=x,y,z
    flist.append(r)
    update_list.append(flist)
    flist=[]
def game_interval():
    global ts, update_list
    x=0
    y=0
    for i in ts:
        for j in i:
            rule(x,y)
            y+=1
        x+=1
        y=0
    x=0
    if update_list != []:
        for cv in update_list:
            cv=no_duplicates(cv)
            asd=cv[0][0]
            dsa=cv[0][1]
            asdf=cv[0][2]
            a=death_or_alive(asd,dsa)

            if asdf <= 1:
                kill(ts[asd][dsa])
            if asdf > 3:
                kill(ts[asd][dsa]) 
            if asdf == 3:
                belebe(ts[asd][dsa])

        update_list=[]
    
    update_list=[]
    t.update()      
def death_or_alive(x,y):
    if ts[x][y].fillcolor() == "black":
        return True
    else:
        ts[x][y].fillcolor() == "white"
        return False
def quadrat(this):
    i=0
    #this.fillcolor("white")
    r = random.randint(1,5)
    if r==0:
        this.fillcolor("black")
    else:
        this.fillcolor("white")
    this.begin_fill()
    while i < 4:
        this.fd(int(length_of_quader))
        this.rt(90)
        i=i+1
    this.end_fill()
    this.hideturtle()
def quadrat2(this,lengthsave):# Used 4 loadsavegame
    i=0
    #this.fillcolor("white")

    this.fillcolor("white")
    this.begin_fill()
    while i < 4:
        this.fd(lengthsave)
        this.rt(90)
        i=i+1
    this.end_fill()
    this.hideturtle()
def colored(this):
    if this.fillcolor() == "white":
        i=0
        this.fillcolor("black")
        this.begin_fill()
        while i < 4:
            this.fd(int(length_of_quader))
            this.rt(90)
            i=i+1
        this.end_fill()
        this.hideturtle()
        t.update()
    elif this.fillcolor() == "black":
        i=0
        this.fillcolor("white")
        this.begin_fill()
        while i < 4:
            this.fd(int(length_of_quader))
            this.rt(90)
            i=i+1
        this.end_fill()
        this.hideturtle()
        t.update()
def randoblack():
    global ts
    x = random.randint(0,int(grid))
    y = random.randint(0,int(grid))
    if x>0:
        x-=1
    if y>0:
        y-=1
    resu=ts[x][y]
    colored(resu)
def startpos(this):
    global startposit, new_startposi
    this.up()
    # this.goto(startposit)
    this.goto(new_startposi)
    this.down()
    # startposit=startposit[0]+int(length_of_quader),startposit[1]
    new_startposi=new_startposi[0]+int(length_of_quader),new_startposi[1]
def get_feld(x,y):
    minus=size/2
    feld1=x+minus
    feld2=y+minus
    resu=round(feld1,int(length_of_quader))
    resu2=round(feld2,int(length_of_quader))
    resu=feld1/int(length_of_quader)
    resu2=feld2/int(length_of_quader)
    resu=round(resu,int(length_of_quader)),round(resu2,int(length_of_quader))
    return int(resu[0]),int(resu[1])
def mouse_clicked(x,y):
    global ts
    if -abs(start_calc)> x or x > (start_calc):
        print("auserhalb des Brettes")
    elif -abs(start_calc)> y or y > (start_calc):
        print("auserhalb des Brettes")
    else:
        feld_cord=get_feld(x,y)
        n1=feld_cord[0]
        n2=feld_cord[1]
        theOne=ts[n2][n1]
        colored(theOne)
def generation20():
    start_time = time.time()
    i=0
    while i<21:
        i+=1
        game_interval()
        print("durchlauf: "+str(i))
    clear = "\n" * 100
    print(clear)
    logo()
    help()
    print("Die 20 Generationen brauchten,", time.time() - start_time, "Sekunden zum durchlaufen")
def generation50():
    start_time = time.time()
    i=0
    while i<51:
        i+=1
        game_interval()
        print("durchlauf: "+str(i)) 
    clear = "\n" * 100
    print(clear)
    logo()
    help()
    print("Die 50 Generationen brauchten,", time.time() - start_time, "Sekunden zum durchlaufen")
def main():
    global grid, startposit, startpos, length_of_quader,new_startposi,start_calc,ts,new_startposit
    grid=int(grid)
    ts = [] # Baustein
    t2d= [] # 2d matrix
    nr= [] 
    i=0
    j=0
    while j<grid:
        while i<grid:
            t2d.append(t.Turtle())
            i+=1
        ts.append(t2d)
        j+=1
        t2d= []
        i=0
    i=0
    for x in ts:
        for y in x:
            i+=1
            y.speed(10)
            y.shape('arrow')
            startpos(y)
            y.turtlesize(1,1)
            if i==grid:
                i=0
                # startposit=-400,startposit[1]-int(length_of_quader)
                new_startposi=-abs(start_calc),new_startposi[1]-int(length_of_quader)
    new_startposi=new_startposit
    for x in ts:
        for y in x:
            i+=1
            y.speed(10)
            quadrat(y)
    ts.reverse()
    t.update()
def init():
    t.listen()
    t.onkey(randoblack,'c')
    t.listen()
    t.onkey(game_interval,'s')
    t.onkey(generation20,'d')
    t.onkey(generation50,'f')
    t.listen()
    t.onkey(loadgame,'x')
    t.onkey(game_clear,'v')
    t.getscreen().onclick(mouse_clicked)
    t.onkey(savegame,'y')
    t.onkey(t.bye,'q')
    help()

t.Screen().tracer(False)
t.title("Conways Game of Life by ZennCode")
if size < 1030:
    t.setup(size+18,size+18)
else:
    t.setup(1920,1000)
main()
init()
mainloop()
