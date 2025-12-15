from tkinter import *



# pan ucitel, tu prosim nastavte font pre cervene X
# (napr. 'arial 20 bold', ale niesom si isty syntax)
# a pre cierne cisla v stvorcoch
# ja ich z technickych pricin nevidim a toto su moje odhady na ok vizual, farby maju automaticky
xfont = "arial 20 bold"
numfont = "arial 20 bold"



def draw_dots():
    for y in range(size+1):
        for x in range(size+1):
            c.create_oval(x*s+o-dot_size,y*s+o-dot_size,x*s+o+dot_size,y*s+o+dot_size,fill="black",tags='dot')


def draw_nums():
    f = open(f"take{size}.txt")
    nums = f.read().strip().split()
    for y in range(size):
        for x in range(size):
            c.create_text(x*s+s//2+o,y*s+s//2+o,text=nums[y][x],font=numfont,tags='num')


def leftclick(e):
    click(e,1)


def rightclick(e):
    click(e,2)



def click(e,mode):
    x = (e.x-o)//s
    y = (e.y-o)//s

    rx = e.x-x*s-o # relativne x a y vramci stvorca
    ry = e.y-y*s-o

    if rx+ry<=s: # TRUE ak topleft
        if rx>=ry: # TRUE ak topright
            pos = "top"
        else:
            pos = "left"
    else: # bottomright
        if rx<=ry:
            pos = "bottom"
        else:
            pos = "right"


    # check ci neklikame mimo pola
    if (x==size and (pos == "top" or pos == "bottom")) or (y==size and (pos == "right" or pos == "left")) or (y==-1 and (pos == "right" or pos == "left")) or (x==-1 and (pos == "top" or pos == "bottom")):
        return

    dx,dy = 0,0 # 'delta'x/y = ukladanie vysvetlim na hodine ale posuva index o bod dalej ak sme dole ci vpravo
    match pos: # foo znaci ci je ciara z daneho bodu zvisla alebo horizontalna a zaroven sluzi ako index pri ukladani
        case 'top':
            foo = 0
        case 'left':
            foo = 1
        case 'bottom':
            dy += 1
            foo = 0
        case 'right':
            dx += 1
            foo = 1

    if lines[y+dy][x+dx][foo] != 0:
        lines[y+dy][x+dx][foo] = 0
        c.delete(f"l{y+dy}{x+dx}{foo}")
    else:
        lines[y+dy][x+dx][foo] = mode

        if mode == 1:
            x1 = x*s+o+dx*s
            y1 = y*s+o+dy*s
            if foo == 0:
                x2 = x1+s
                y2 = y1
            else:
                x2 = x1
                y2 = y1 + s
            c.create_line(x1,y1,x2,y2,width=dot_size,tags=f"l{y+dy}{x+dx}{foo}")

        else:
            if foo == 0:
                c.create_text(x*s+o+s//2,y*s+o+dy*s,text="x",fill="red",font=xfont,tags=f"l{y+dy}{x+dx}{foo}")
            else:
                c.create_text(x*s+o+dx*s,y*s+o+s//2,text="x",fill="red",font=xfont,tags=f"l{y+dy}{x+dx}{foo}")


size,s,o,dot_size = 6, 100, 10, 3 # pri zmeneni size subor nacita txt file so zhodojucim cislom v nazve
W,H = s*size,s*size
root = Tk()
c = Canvas(root,width=W+2*o,height=H+2*o)
c.pack()
draw_dots()
draw_nums()
c.bind("<1>",leftclick)
c.bind("<3>",rightclick)

lines = [[[0,0] for n in range(size+1)] for n in range(size+1)]



root.mainloop()
