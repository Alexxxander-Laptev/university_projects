from tkinter import *
from tkinter.ttk import Combobox
from random import randint
import time

r = 15
R = 60
x = -15
y = 240
xm1 = 210
ym1 = 225
xm2 = 210
ym2 = 270
xm3 = 555
ym3 = 240
xm4 = 555
ym4 = 285
xm5 = 450
ym5 = 255
xm6 = 855
ym6 = 255
xm7 = 855
ym7 = 300
xm8 = 765
ym8 = 240
xm9 = 765
ym9 = 285
x_new = 0
y_new = 0

text_x = 60
text_y = 515

k = 0

Hm1 = 15
Hm2 = 15
Hm3 = 15
Hm4 = 15
Hm5 = 15
Hm6 = 15
Hm7 = 15
Hm8 = 15
Hm9 = 15
Ha = 20
Ha_new = 20
Am = 0
Aa = 0
Mac = 1
Aac1 = 1
Aac2 = 2
Aac3 = 3
Aac4 = 4
Aac5 = 5
Aac6 = 6
Aac7 = 7
Aac8 = 8
Aa_base = 5
Aa_mod = 2
Hm1 = Hm1 + Mac
Hm2 = Hm2 + Mac
Hm3 = Hm3 + Mac
Hm4 = Hm4 + Mac
Hm5 = Hm5 + Mac
Hm6 = Hm6 + Mac
Hm7 = Hm7 + Mac
Hm8 = Hm8 + Mac
Hm9 = Hm9 + Mac

def choice():
    root = Tk()
    root.title('Desperado')
    root.geometry('1080x720')
    root['bg'] = 'black'
    
    lbl = Label(root, text = 'CHOICE OF EQUIPMENT', font = ('Times New Roman', 50), fg = 'red', bg = 'black')
    lbl.pack(pady = 75)
    
    def armor1(self):
        root.destroy()
        root1 = Tk()
        root1.title('Desperado')
        root1.geometry('1080x720')
        root1['bg'] = 'black'
        
        lbl = Label(root1, text = 'CHOICE OF EQUIPMENT', font = ('Times New Roman', 50), fg = 'red', bg = 'black')
        lbl.pack(pady = 25)

        war1()
        
        def play1(self):
            global Ha
            global Ha_new
            global Aac1
            root1.destroy()
            Ha_new = Ha + Aac1
            war1()
            war2()
            war3()
            war4()
            war5()

        def play2(self):
            global Ha
            global Ha_new
            global Aac2
            root1.destroy()
            Ha_new = Ha + Aac2
            war1()
            war2()
            war3()
            war4()
            war5()

        def play3(self):
            global Ha
            global Ha_new
            global Aac3
            root1.destroy()
            Ha_new = Ha + Aac3
            war1()
            war2()
            war3()
            war4()
            war5()

        def play4(self):
            global Ha
            global Ha_new
            global Aac4
            root1.destroy()
            Ha_new = Ha + Aac4
            war1()
            war2()
            war3()
            war4()
            war5()

        def play5(self):
            global Ha
            global Ha_new
            global Aac5
            root1.destroy()
            Ha_new = Ha + Aac5
            war1()
            war2()
            war3()
            war4()
            war5()

        def play6(self):
            global Ha
            global Ha_new
            global Aac6
            root1.destroy()
            Ha_new = Ha + Aac6
            war1()
            war2()
            war3()
            war4()
            war5()

        def play7(self):
            global Ha
            global Ha_new
            global Aac7
            root1.destroy()
            Ha_new = Ha + Aac7
            war1()
            war2()
            war3()
            war4()
            war5()

        def play8(self):
            global Ha
            global Ha_new
            global Aac8
            root1.destroy()
            Ha_new = Ha + Aac8
            war1()
            war2()
            war3()
            war4()
            war5()
        
        tissue = Button(root1, text = 'TISSUE', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        tissue.pack(pady = 10)
        tissue.bind("<Button-1>", play1)
        
        leather = Button(root1, text = 'LEATHER', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        leather.pack(pady = 10)
        leather.bind("<Button-1>", play2)
        
        tl = Button(root1, text = 'TANNED LEATHER', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        tl.pack(pady = 10)
        tl.bind("<Button-1>", play3)
        
        cm = Button(root1, text = 'CHAIN MAIL', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        cm.pack(pady = 10)
        cm.bind("<Button-1>", play4)
        
        op = Button(root1, text = 'ONE-PIECE BREASTPLATE', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        op.pack(pady = 10)
        op.bind("<Button-1>", play5)
        
        lamellar = Button(root1, text = 'LAMELLAR', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        lamellar.pack(pady = 10)
        lamellar.bind("<Button-1>", play6)
        
        hb = Button(root1, text = 'HALF-BLAME', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        hb.pack(pady = 10)
        hb.bind("<Button-1>", play7)
        
        plate = Button(root1, text = 'PLATE', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        plate.pack(pady = 10)
        plate.bind("<Button-1>", play8)

    def armor2(self):
        root.destroy()
        root1 = Tk()
        root1.title('Desperado')
        root1.geometry('1080x720')
        root1['bg'] = 'black'
        
        lbl = Label(root1, text = 'CHOICE OF EQUIPMENT', font = ('Times New Roman', 50), fg = 'red', bg = 'black')
        lbl.pack(pady = 25)

        war2()
        
        def play1(self):
            global Ha
            global Ha_new
            global Aac1
            root1.destroy()
            Ha_new = Ha + Aac1
            war1()
            war2()
            war3()
            war4()
            war5()

        def play2(self):
            global Ha
            global Ha_new
            global Aac2
            root1.destroy()
            Ha_new = Ha + Aac2
            war1()
            war2()
            war3()
            war4()
            war5()

        def play3(self):
            global Ha
            global Ha_new
            global Aac3
            root1.destroy()
            Ha_new = Ha + Aac3
            war1()
            war2()
            war3()
            war4()
            war5()

        def play4(self):
            global Ha
            global Ha_new
            global Aac4
            root1.destroy()
            Ha_new = Ha + Aac4
            war1()
            war2()
            war3()
            war4()
            war5()

        def play5(self):
            global Ha
            global Ha_new
            global Aac5
            root1.destroy()
            Ha_new = Ha + Aac5
            war1()
            war2()
            war3()
            war4()
            war5()

        def play6(self):
            global Ha
            global Ha_new
            global Aac6
            root1.destroy()
            Ha_new = Ha + Aac6
            war1()
            war2()
            war3()
            war4()
            war5()

        def play7(self):
            global Ha
            global Ha_new
            global Aac7
            root1.destroy()
            Ha_new = Ha + Aac7
            war1()
            war2()
            war3()
            war4()
            war5()

        def play8(self):
            global Ha
            global Ha_new
            global Aac8
            root1.destroy()
            Ha_new = Ha + Aac8
            war1()
            war2()
            war3()
            war4()
            war5()
        
        tissue = Button(root1, text = 'TISSUE', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        tissue.pack(pady = 10)
        tissue.bind("<Button-1>", play1)
        
        leather = Button(root1, text = 'LEATHER', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        leather.pack(pady = 10)
        leather.bind("<Button-1>", play2)
        
        tl = Button(root1, text = 'TANNED LEATHER', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        tl.pack(pady = 10)
        tl.bind("<Button-1>", play3)
        
        cm = Button(root1, text = 'CHAIN MAIL', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        cm.pack(pady = 10)
        cm.bind("<Button-1>", play4)
        
        op = Button(root1, text = 'ONE-PIECE BREASTPLATE', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        op.pack(pady = 10)
        op.bind("<Button-1>", play5)
        
        lamellar = Button(root1, text = 'LAMELLAR', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        lamellar.pack(pady = 10)
        lamellar.bind("<Button-1>", play6)
        
        hb = Button(root1, text = 'HALF-BLAME', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        hb.pack(pady = 10)
        hb.bind("<Button-1>", play7)
        
        plate = Button(root1, text = 'PLATE', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        plate.pack(pady = 10)
        plate.bind("<Button-1>", play8)

    def armor3(self):
        root.destroy()
        root1 = Tk()
        root1.title('Desperado')
        root1.geometry('1080x720')
        root1['bg'] = 'black'
        
        lbl = Label(root1, text = 'CHOICE OF EQUIPMENT', font = ('Times New Roman', 50), fg = 'red', bg = 'black')
        lbl.pack(pady = 25)

        war3()
        
        def play1(self):
            global Ha
            global Ha_new
            global Aac1
            root1.destroy()
            Ha_new = Ha + Aac1
            war1()
            war2()
            war3()
            war4()
            war5()

        def play2(self):
            global Ha
            global Ha_new
            global Aac2
            root1.destroy()
            Ha_new = Ha + Aac2
            war1()
            war2()
            war3()
            war4()
            war5()

        def play3(self):
            global Ha
            global Ha_new
            global Aac3
            root1.destroy()
            Ha_new = Ha + Aac3
            war1()
            war2()
            war3()
            war4()
            war5()

        def play4(self):
            global Ha
            global Ha_new
            global Aac4
            root1.destroy()
            Ha_new = Ha + Aac4
            war1()
            war2()
            war3()
            war4()
            war5()

        def play5(self):
            global Ha
            global Ha_new
            global Aac5
            root1.destroy()
            Ha_new = Ha + Aac5
            war1()
            war2()
            war3()
            war4()
            war5()

        def play6(self):
            global Ha
            global Ha_new
            global Aac6
            root1.destroy()
            Ha_new = Ha + Aac6
            war1()
            war2()
            war3()
            war4()
            war5()

        def play7(self):
            global Ha
            global Ha_new
            global Aac7
            root1.destroy()
            Ha_new = Ha + Aac7
            war1()
            war2()
            war3()
            war4()
            war5()

        def play8(self):
            global Ha
            global Ha_new
            global Aac8
            root1.destroy()
            Ha_new = Ha + Aac8
            war1()
            war2()
            war3()
            war4()
            war5()
        
        tissue = Button(root1, text = 'TISSUE', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        tissue.pack(pady = 10)
        tissue.bind("<Button-1>", play1)
        
        leather = Button(root1, text = 'LEATHER', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        leather.pack(pady = 10)
        leather.bind("<Button-1>", play2)
        
        tl = Button(root1, text = 'TANNED LEATHER', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        tl.pack(pady = 10)
        tl.bind("<Button-1>", play3)
        
        cm = Button(root1, text = 'CHAIN MAIL', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        cm.pack(pady = 10)
        cm.bind("<Button-1>", play4)
        
        op = Button(root1, text = 'ONE-PIECE BREASTPLATE', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        op.pack(pady = 10)
        op.bind("<Button-1>", play5)
        
        lamellar = Button(root1, text = 'LAMELLAR', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        lamellar.pack(pady = 10)
        lamellar.bind("<Button-1>", play6)
        
        hb = Button(root1, text = 'HALF-BLAME', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        hb.pack(pady = 10)
        hb.bind("<Button-1>", play7)
        
        plate = Button(root1, text = 'PLATE', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        plate.pack(pady = 10)
        plate.bind("<Button-1>", play8)

    def armor4(self):
        root.destroy()
        root1 = Tk()
        root1.title('Desperado')
        root1.geometry('1080x720')
        root1['bg'] = 'black'
        
        lbl = Label(root1, text = 'CHOICE OF EQUIPMENT', font = ('Times New Roman', 50), fg = 'red', bg = 'black')
        lbl.pack(pady = 25)

        war4()
        
        def play1(self):
            global Ha
            global Ha_new
            global Aac1
            root1.destroy()
            Ha_new = Ha + Aac1
            war1()
            war2()
            war3()
            war4()
            war5()

        def play2(self):
            global Ha
            global Ha_new
            global Aac2
            root1.destroy()
            Ha_new = Ha + Aac2
            war1()
            war2()
            war3()
            war4()
            war5()

        def play3(self):
            global Ha
            global Ha_new
            global Aac3
            root1.destroy()
            Ha_new = Ha + Aac3
            war1()
            war2()
            war3()
            war4()
            war5()

        def play4(self):
            global Ha
            global Ha_new
            global Aac4
            root1.destroy()
            Ha_new = Ha + Aac4
            war1()
            war2()
            war3()
            war4()
            war5()

        def play5(self):
            global Ha
            global Ha_new
            global Aac5
            root1.destroy()
            Ha_new = Ha + Aac5
            war1()
            war2()
            war3()
            war4()
            war5()

        def play6(self):
            global Ha
            global Ha_new
            global Aac6
            root1.destroy()
            Ha_new = Ha + Aac6
            war1()
            war2()
            war3()
            war4()
            war5()

        def play7(self):
            global Ha
            global Ha_new
            global Aac7
            root1.destroy()
            Ha_new = Ha + Aac7
            war1()
            war2()
            war3()
            war4()
            war5()

        def play8(self):
            global Ha
            global Ha_new
            global Aac8
            root1.destroy()
            Ha_new = Ha + Aac8
            war1()
            war2()
            war3()
            war4()
            war5()
        
        tissue = Button(root1, text = 'TISSUE', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        tissue.pack(pady = 10)
        tissue.bind("<Button-1>", play1)
        
        leather = Button(root1, text = 'LEATHER', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        leather.pack(pady = 10)
        leather.bind("<Button-1>", play2)
        
        tl = Button(root1, text = 'TANNED LEATHER', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        tl.pack(pady = 10)
        tl.bind("<Button-1>", play3)
        
        cm = Button(root1, text = 'CHAIN MAIL', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        cm.pack(pady = 10)
        cm.bind("<Button-1>", play4)
        
        op = Button(root1, text = 'ONE-PIECE BREASTPLATE', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        op.pack(pady = 10)
        op.bind("<Button-1>", play5)
        
        lamellar = Button(root1, text = 'LAMELLAR', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        lamellar.pack(pady = 10)
        lamellar.bind("<Button-1>", play6)
        
        hb = Button(root1, text = 'HALF-BLAME', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        hb.pack(pady = 10)
        hb.bind("<Button-1>", play7)
        
        plate = Button(root1, text = 'PLATE', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        plate.pack(pady = 10)
        plate.bind("<Button-1>", play8)

    def armor5(self):
        root.destroy()
        root1 = Tk()
        root1.title('Desperado')
        root1.geometry('1080x720')
        root1['bg'] = 'black'
        
        lbl = Label(root1, text = 'CHOICE OF EQUIPMENT', font = ('Times New Roman', 50), fg = 'red', bg = 'black')
        lbl.pack(pady = 25)

        war5()
        
        def play1(self):
            global Ha
            global Ha_new
            global Aac1
            root1.destroy()
            Ha_new = Ha + Aac1
            war1()
            war2()
            war3()
            war4()
            war5()

        def play2(self):
            global Ha
            global Ha_new
            global Aac2
            root1.destroy()
            Ha_new = Ha + Aac2
            war1()
            war2()
            war3()
            war4()
            war5()

        def play3(self):
            global Ha
            global Ha_new
            global Aac3
            root1.destroy()
            Ha_new = Ha + Aac3
            war1()
            war2()
            war3()
            war4()
            war5()

        def play4(self):
            global Ha
            global Ha_new
            global Aac4
            root1.destroy()
            Ha_new = Ha + Aac4
            war1()
            war2()
            war3()
            war4()
            war5()

        def play5(self):
            global Ha
            global Ha_new
            global Aac5
            root1.destroy()
            Ha_new = Ha + Aac5
            war1()
            war2()
            war3()
            war4()
            war5()

        def play6(self):
            global Ha
            global Ha_new
            global Aac6
            root1.destroy()
            Ha_new = Ha + Aac6
            war1()
            war2()
            war3()
            war4()
            war5()

        def play7(self):
            global Ha
            global Ha_new
            global Aac7
            root1.destroy()
            Ha_new = Ha + Aac7
            war1()
            war2()
            war3()
            war4()
            war5()

        def play8(self):
            global Ha
            global Ha_new
            global Aac8
            root1.destroy()
            Ha_new = Ha + Aac8
            war1()
            war2()
            war3()
            war4()
            war5()
        
        tissue = Button(root1, text = 'TISSUE', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        tissue.pack(pady = 10)
        tissue.bind("<Button-1>", play1)
        
        leather = Button(root1, text = 'LEATHER', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        leather.pack(pady = 10)
        leather.bind("<Button-1>", play2)
        
        tl = Button(root1, text = 'TANNED LEATHER', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        tl.pack(pady = 10)
        tl.bind("<Button-1>", play3)
        
        cm = Button(root1, text = 'CHAIN MAIL', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        cm.pack(pady = 10)
        cm.bind("<Button-1>", play4)
        
        op = Button(root1, text = 'ONE-PIECE BREASTPLATE', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        op.pack(pady = 10)
        op.bind("<Button-1>", play5)
        
        lamellar = Button(root1, text = 'LAMELLAR', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        lamellar.pack(pady = 10)
        lamellar.bind("<Button-1>", play6)
        
        hb = Button(root1, text = 'HALF-BLAME', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        hb.pack(pady = 10)
        hb.bind("<Button-1>", play7)
        
        plate = Button(root1, text = 'PLATE', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
        plate.pack(pady = 10)
        plate.bind("<Button-1>", play8)

    sword = Button(root, text = 'SWORD', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
    sword.pack(pady = 10)
    sword.bind("<Button-1>", armor2)
    
    dagger = Button(root, text = 'DAGGER', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
    dagger.pack(pady = 10)
    dagger.bind("<Button-1>", armor1)
    
    ax = Button(root, text = 'AX', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
    ax.pack(pady = 10)
    ax.bind("<Button-1>", armor2)
    
    saber = Button(root, text = 'SABER', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
    saber.pack(pady = 10)
    saber.bind("<Button-1>", armor4)
    
    th = Button(root, text = 'TWO-HANDRED SWORD', width = 25, font = ('Times New Roman', 18), fg = 'red', bg = 'blue')
    th.pack(pady = 10)
    th.bind("<Button-1>", armor5)
canvas = Canvas(width = 1080, height = 720, bg = 'black')
canvas.pack()
canvas.create_text(540, 360, font = ('TimesNewRoman', 12), text = 'Press select "escape" key to select equipment. Press the right arrow key to start the game.\nInitially you have 20 lives and the base attack value is 5 without equipment. Each of your op-\nponents has 16 lives, taking into account modifications, and there is no base attack.', fill = 'white', justify = CENTER)
canvas.create_text(540, 120, font = ('TimesNewRoman', 80), text = 'DESPERADO', fill = 'red', justify = CENTER)

def escape(self):
    choice()

canvas.bind_all('<Escape>', escape)

def right(self):
    global x
    global y
    global Hm1
    global Hm2
    global Hm3
    global Hm4
    global Hm5
    global Hm6
    global Hm7
    global Hm8
    global Hm9
    global Ha
    global Am
    global Aa
    global Aa_base
    global Aa_mod
    global xm1
    global ym1
    global xm2
    global ym2
    global xm3
    global ym3
    global xm4
    global ym4
    global xm5
    global ym5
    global xm6
    global ym6
    global xm7
    global ym7
    global xm8
    global ym8
    global xm9
    global ym9
    global text_x
    global text_y
    global x_new
    x_new = x
    x += 15
    if (((x >= 195) and (x <= 195) and (y >= 0) and (y < 30)) or ((x >= 225) and (x <= 225) and (y >= 15) and (y < 215)) or ((x >= 570) and (x <= 570) and (y >= 0) and (y < 230)) or ((x >= 870) and (x <= 870) and (y >= 0) and (y < 245)) or ((x >= 165) and (x <= 165) and (y >= 310) and (y < 480)) or ((x >= 225) and (x <= 225) and (y >= 250) and (y < 340)) or ((x >= 525) and (x <= 525) and (y >= 280) and (y < 480)) or ((x >= 570) and (x <= 570) and (y >= 265) and (y < 570)) or ((x >= 765) and (x <= 765) and (y >= 300) and (y < 480)) or ((x >= 870) and (x <= 870) and (y >= 280) and (y < 870))):
        x -= 15
        rooms1()
        canvas.create_text(xm1, ym1, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm2, ym2, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    else:
        rooms1()
        canvas.create_text(xm1, ym1, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm2, ym2, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    death()
    war1()
    war2()
    war3()
    war4()
    war5()
    open_door()
    chase()
    if (Ha <= 0):
        lose()

def left(self):
    global x
    global y
    global Hm1
    global Hm2
    global Hm3
    global Hm4
    global Hm5
    global Hm6
    global Hm7
    global Hm8
    global Hm9
    global Ha
    global Am
    global Aa
    global Aa_base
    global Aa_mod
    global xm1
    global ym1
    global xm2
    global ym2
    global xm3
    global ym3
    global xm4
    global ym4
    global xm5
    global ym5
    global xm6
    global ym6
    global xm7
    global ym7
    global xm8
    global ym8
    global xm9
    global ym9
    global text_x
    global text_y
    global x_new
    x_new = x
    x -= 15
    if (((x <= 0) and (x >= 0) and (y >= 0) and (y < 215)) or ((x <= 240) and (x >= 240) and (y >= 135) and (y < 215)) or ((x <= 270) and (x >= 270) and (y >= 45) and (y < 150)) or ((x <= 300) and (x >= 300) and (y >= 0) and (y < 60)) or ((x <= 585) and (x >= 585) and (y >= 195) and (y < 230)) or ((x <= 720) and (x >= 720) and (y >= 0) and (y < 210)) or ((x <= 0) and (x >= 0) and (y >= 255) and (y < 480)) or ((x <= 240) and (x >= 240) and (y >= 255) and (y < 340)) or ((x <= 390) and (x >= 390) and (y >= 340) and (y < 480)) or ((x <= 585) and (x >= 585) and (y >= 265) and (y < 480))):
        x += 15
        rooms1()
        canvas.create_text(xm1, ym1, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm2, ym2, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    else:
        rooms1()
        canvas.create_text(xm1, ym1, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm2, ym2, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    death()
    war1()
    war2()
    war3()
    war4()
    war5()
    open_door()
    chase()
    if (Ha <= 0):
        lose()

def down(self):
    global x
    global y
    global Hm1
    global Hm2
    global Hm3
    global Hm4
    global Hm5
    global Hm6
    global Hm7
    global Hm8
    global Hm9
    global Ha
    global Am
    global Aa
    global Aa_base
    global Aa_mod
    global xm1
    global ym1
    global xm2
    global ym2
    global xm3
    global ym3
    global xm4
    global ym4
    global xm5
    global ym5
    global xm6
    global ym6
    global xm7
    global ym7
    global xm8
    global ym8
    global xm9
    global ym9
    global text_x
    global text_y
    global y_new
    y_new = y
    y += 15
    if (((y >= 250) and (x >= 0) and (x < 15)) or ((y >= 480) and (x >= 15) and (x < 165)) or ((y >= 315) and (x >= 165) and (x < 225)) or ((y >= 250) and (x >= 225) and (x < 255)) or ((y >= 345) and (x >= 255) and (x < 405)) or ((y >= 480) and (x >= 405) and (x < 535)) or ((y >= 285) and (x >= 525) and (x < 570)) or ((y >= 265) and (x >= 570) and (x < 600)) or ((y >= 480) and (x >= 600) and (x < 765)) or ((y >= 300) and (x >= 765) and (x < 870)) or ((y >= 280) and (x >= 870) and (x < 945))):
        y -= 15
        rooms1()
        canvas.create_text(xm1, ym1, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm2, ym2, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    else:
        rooms1()
        canvas.create_text(xm1, ym1, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm2, ym2, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    death()
    war1()
    war2()
    war3()
    war4()
    war5()
    open_door()
    chase()
    if (Ha <= 0 ):
        lose()

def up(self):
    global x
    global y
    global Hm1
    global Hm2
    global Hm3
    global Hm4
    global Hm5
    global Hm6
    global Hm7
    global Hm8
    global Hm9
    global Ha
    global Am
    global Aa
    global Aa_base
    global Aa_mod
    global xm1
    global ym1
    global xm2
    global ym2
    global xm3
    global ym3
    global xm4
    global ym4
    global xm5
    global ym5
    global xm6
    global ym6
    global xm7
    global ym7
    global xm8
    global ym8
    global xm9
    global ym9
    global text_x
    global text_y
    global y_new
    y_new = y
    y -= 15
    if (((y <= 220) and (x >= 0) and (x < 15)) or ((y <= 0) and (x >= 15) and (x < 195)) or ((y <= 15) and (x >= 195) and (x < 225)) or ((y <= 215) and (x >= 225) and (x < 255)) or ((y <= 135) and (x >= 255) and (x < 285)) or ((y <= 45) and (x >= 285) and (x < 315)) or ((y <= 0) and (x >= 315) and (x < 570)) or ((y <= 230) and (x >= 570) and (x < 600)) or ((y <= 195) and (x >= 600) and (x < 735)) or ((y <= 0) and (x >= 735) and (x < 870)) or ((y <= 245) and (x >= 870) and (x < 945))):
        y += 15
        rooms1()
        canvas.create_text(xm1, ym1, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm2, ym2, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    else:
        rooms1()
        canvas.create_text(xm1, ym1, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm2, ym2, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    death()
    war1()
    war2()
    war3()
    war4()
    war5()
    open_door()
    chase()
    if (Ha <= 0):
        lose()

def main():
    global x
    global y
    global xm1
    global ym1
    global xm2
    global ym2
    global xm3
    global ym3
    global xm4
    global ym4
    global xm5
    global ym5
    global xm6
    global ym6
    global xm7
    global ym7
    global xm8
    global ym8
    global xm9
    global ym9
    canvas.delete('all')
    canvas.create_line(15, 230, 30, 230, 30, 20, 210, 20, 210, 35, 240, 35, 240, 230, 270, 230, 270, 155, 300, 155, 300, 65, 330, 65, 330, 20, 585, 20, 585, 245, 615, 245, 615, 215, 750, 215, 750, 20, 885, 20, 885, 260, 960, 260, fill = 'green')
    canvas.create_line(15, 265, 30, 265, 30, 490, 180, 490, 180, 325, 240, 325, 240, 265, 270, 265, 270, 355, 420, 355, 420, 490, 540, 490, 540, 295, 585, 295, 585, 280, 615, 280, 615, 490, 780, 490, 780, 310, 885, 310, 885, 295, 960, 295, fill = 'green')
    canvas.create_text(x+15, y+15, anchor = W, font = ('TimesNewRoman', 12), text = '@', fill = 'red')
    canvas.create_text(xm1, ym1, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    canvas.create_text(xm2, ym2, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    canvas.create_line(30, 500, 720, 500, fill = 'white')
    canvas.create_text(text_x, text_y, anchor = W, font = ('TimesNewRoman', 12), text = 'You walk along the stone floor of the cave. You can restore your helth by step ping on "+".', fill = 'white')

def rooms1():
    global x
    global y
    global Ha
    global Ha_new
    canvas.delete('all')
    canvas.create_line(255, 230, 255, 265, fill = 'red', width = 5)
    canvas.create_line(600, 245, 600, 280, fill = 'red', width = 5)
    canvas.create_line(960, 260, 960, 295, fill = 'red', width = 5)
    canvas.create_line(15, 230, 30, 230, 30, 20, 210, 20, 210, 35, 240, 35, 240, 230, 270, 230, 270, 155, 300, 155, 300, 65, 330, 65, 330, 20, 585, 20, 585, 245, 615, 245, 615, 215, 750, 215, 750, 20, 885, 20, 885, 260, 960, 260, fill = 'green')
    canvas.create_line(15, 265, 30, 265, 30, 490, 180, 490, 180, 325, 240, 325, 240, 265, 270, 265, 270, 355, 420, 355, 420, 490, 540, 490, 540, 295, 585, 295, 585, 280, 615, 280, 615, 490, 780, 490, 780, 310, 885, 310, 885, 295, 960, 295, fill = 'green')
    canvas.create_text(x+15, y+15, anchor = W, font = ('TimesNewRoman', 12), text = '@', fill = 'red')
    canvas.create_line(30, 500, 720, 500, fill = 'white')
    canvas.create_text(text_x, text_y, anchor = W, font = ('TimesNewRoman', 12), text = 'You walk along the stone floor of the cave. You can restore your helth by step ping on "+".', fill = 'white')
    canvas.create_text(195, 30, anchor = W, font = ('TimesNewRoman', 12), text = '+', fill = 'blue')
    if ((x == 0) and (y == 240)):
        Ha = Ha_new
    if ((x == 180) and (y == 15)):
        canvas.create_text(text_x, text_y + 30, anchor = W, font = ('TimesNewRoman', 12), text = 'Your helth is restored', fill = 'white')
        Ha = Ha_new
    if Ha <= 5:
        canvas.create_text(text_x, text_y + 60, anchor = W, font = ('TimesNewRoman', 12), text = 'Restore your helth', fill = 'white')
    if (x == 225):
        canvas.create_text(text_x, text_y + 30, anchor = W, font = ('TimesNewRoman', 12), text = 'To open the door, hit it', fill = 'white')

def rooms2():
    global x
    global y
    global Ha
    global Ha_new
    canvas.delete('all')
    canvas.create_line(600, 245, 600, 280, fill = 'red', width = 5)
    canvas.create_line(960, 260, 960, 295, fill = 'red', width = 5)
    canvas.create_line(15, 230, 30, 230, 30, 20, 210, 20, 210, 35, 240, 35, 240, 230, 270, 230, 270, 155, 300, 155, 300, 65, 330, 65, 330, 20, 585, 20, 585, 245, 615, 245, 615, 215, 750, 215, 750, 20, 885, 20, 885, 260, 960, 260, fill = 'green')
    canvas.create_line(15, 265, 30, 265, 30, 490, 180, 490, 180, 325, 240, 325, 240, 265, 270, 265, 270, 355, 420, 355, 420, 490, 540, 490, 540, 295, 585, 295, 585, 280, 615, 280, 615, 490, 780, 490, 780, 310, 885, 310, 885, 295, 960, 295, fill = 'green')
    canvas.create_text(x+15, y+15, anchor = W, font = ('TimesNewRoman', 12), text = '@', fill = 'red')
    canvas.create_line(30, 500, 720, 500, fill = 'white')
    canvas.create_text(text_x, text_y, anchor = W, font = ('TimesNewRoman', 12), text = 'You walk along the stone floor of the cave. You can restore your helth by step ping on "+".', fill = 'white')
    canvas.create_text(300, 75, anchor = W, font = ('TimesNewRoman', 12), text = '+', fill = 'blue')
    canvas.create_text(525, 480, anchor = W, font = ('TimesNewRoman', 12), text = '+', fill = 'blue')
    if ((x == 285) and (y == 60)) or ((x == 510) and (y == 465)):
        canvas.create_text(text_x, text_y + 30, anchor = W, font = ('TimesNewRoman', 12), text = 'Your helth is restored', fill = 'white')
        Ha = Ha_new
    if Ha <= 5:
        canvas.create_text(text_x, text_y + 60, anchor = W, font = ('TimesNewRoman', 12), text = 'Restore your helth', fill = 'white')
    if (x == 225):
        canvas.create_text(text_x, text_y + 30, anchor = W, font = ('TimesNewRoman', 12), text = 'You opened the door, you can go inside', fill = 'white')
    if (x == 570):
        canvas.create_text(text_x, text_y + 30, anchor = W, font = ('TimesNewRoman', 12), text = 'To open the door, hit it', fill = 'white')

def rooms3():
    global x
    global y
    global Ha
    global Ha_new
    canvas.delete('all')
    canvas.create_line(960, 260, 960, 295, fill = 'red', width = 5)
    canvas.create_line(15, 230, 30, 230, 30, 20, 210, 20, 210, 35, 240, 35, 240, 230, 270, 230, 270, 155, 300, 155, 300, 65, 330, 65, 330, 20, 585, 20, 585, 245, 615, 245, 615, 215, 750, 215, 750, 20, 885, 20, 885, 260, 960, 260, fill = 'green')
    canvas.create_line(15, 265, 30, 265, 30, 490, 180, 490, 180, 325, 240, 325, 240, 265, 270, 265, 270, 355, 420, 355, 420, 490, 540, 490, 540, 295, 585, 295, 585, 280, 615, 280, 615, 490, 780, 490, 780, 310, 885, 310, 885, 295, 960, 295, fill = 'green')
    canvas.create_text(x+15, y+15, anchor = W, font = ('TimesNewRoman', 12), text = '@', fill = 'red')
    canvas.create_line(30, 500, 720, 500, fill = 'white')
    canvas.create_text(text_x, text_y, anchor = W, font = ('TimesNewRoman', 12), text = 'You walk along the stone floor of the cave. You can restore your helth by step ping on "+".', fill = 'white')
    canvas.create_text(765, 480, anchor = W, font = ('TimesNewRoman', 12), text = '+', fill = 'blue')
    canvas.create_text(615, 225, anchor = W, font = ('TimesNewRoman', 12), text = '+', fill = 'blue')
    canvas.create_text(750, 30, anchor = W, font = ('TimesNewRoman', 12), text = '+', fill = 'blue')
    if ((x == 750) and (y == 465)) or ((x == 600) and (y == 210)) or ((x == 735) and (y == 15)):
        canvas.create_text(text_x, text_y + 30, anchor = W, font = ('TimesNewRoman', 12), text = 'Your helth is restored', fill = 'white')
        Ha = Ha_new
    if Ha <= 5:
        canvas.create_text(text_x, text_y + 60, anchor = W, font = ('TimesNewRoman', 12), text = 'Restore your helth', fill = 'white')
    if (x == 570):
        canvas.create_text(text_x, text_y + 30, anchor = W, font = ('TimesNewRoman', 12), text = 'You opened the door, you can go inside', fill = 'white')
    if (x == 930):
        canvas.create_text(text_x, text_y + 30, anchor = W, font = ('TimesNewRoman', 12), text = 'To open the door, hit it', fill = 'white')

def rooms4():
    global x
    global y
    canvas.delete('all')
    canvas.create_line(15, 230, 30, 230, 30, 20, 210, 20, 210, 35, 240, 35, 240, 230, 270, 230, 270, 155, 300, 155, 300, 65, 330, 65, 330, 20, 585, 20, 585, 245, 615, 245, 615, 215, 750, 215, 750, 20, 885, 20, 885, 260, 960, 260, fill = 'green')
    canvas.create_line(15, 265, 30, 265, 30, 490, 180, 490, 180, 325, 240, 325, 240, 265, 270, 265, 270, 355, 420, 355, 420, 490, 540, 490, 540, 295, 585, 295, 585, 280, 615, 280, 615, 490, 780, 490, 780, 310, 885, 310, 885, 295, 960, 295, fill = 'green')
    canvas.create_text(x+15, y+15, anchor = W, font = ('TimesNewRoman', 12), text = '@', fill = 'red')
    canvas.create_line(30, 500, 720, 500, fill = 'white')
    canvas.create_text(text_x, text_y, anchor = W, font = ('TimesNewRoman', 12), text = 'You walk along the stone floor of the cave. You can restore your helth by step ping on "+".', fill = 'white')

def chase():
    global x
    global y
    global xm1
    global ym1
    global xm2
    global ym2
    global xm3
    global ym3
    global xm4
    global ym4
    global xm5
    global ym5
    global xm6
    global ym6
    global xm7
    global ym7
    global xm8
    global ym8
    global xm9
    global ym9
    global R
    global r
    global x_new
    global y_new
    if (xm1 - x <= R + r) and (xm1 - x >= 2 * r) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym1 <= R) and (y - ym1 >= -R):
        xm1 -= r
    elif (x - xm1 <= R - r) and (x - xm1 >= 0) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym1 <= R) and (y - ym1 >= -R):
        xm1 += r
    elif (x - xm1 <= 0) and (x - xm1 >= -R) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (ym1 - y <= R + r) and (ym1 - y >= 2 * r):
        ym1 -= r
    elif (x - xm1 <= 0) and (x - xm1 >= -R) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym1 <= R - r) and (y - ym1 >= 0):
        ym1 += r

    if (xm2 - x <= R + r) and (xm2 - x >= 2 * r) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym2 <= R) and (y - ym2 >= -R):
        xm2 -= r
    elif (x - xm2 <= R - r) and (x - xm2 >= 0) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym2 <= R) and (y - ym2 >= -R):
        xm2 += r
    elif (x - xm2 <= 0) and (x - xm2 >= -R) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (ym2 - y <= R + r) and (ym2 - y >= 2 * r):
        ym2 -= r
    elif (x - xm2 <= 0) and (x - xm2 >= -R) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym2 <= R - r) and (y - ym2 >= 0):
        ym2 += r

    if (xm3 - x <= R + r) and (xm3 - x >= 2 * r) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym3 <= R) and (y - ym3 >= -R):
        xm3 -= r
    elif (x - xm3 <= R - r) and (x - xm3 >= 0) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym3 <= R) and (y - ym3 >= -R):
        xm3 += r
    elif (x - xm3 <= 0) and (x - xm3 >= -R) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (ym3 - y <= R + r) and (ym3 - y >= 2 * r):
        ym3 -= r
    elif (x - xm3 <= 0) and (x - xm3 >= -R) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym3 <= R - r) and (y - ym3 >= 0):
        ym3 += r

    if (xm4 - x <= R + r) and (xm4 - x >= 2 * r) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym4 <= R) and (y - ym4 >= -R):
        xm4 -= r
    elif (x - xm4 <= R - r) and (x - xm4 >= 0) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym4 <= R) and (y - ym4 >= -R):
        xm4 += r
    elif (x - xm4 <= 0) and (x - xm4 >= -R) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (ym4 - y <= R + r) and (ym4 - y >= 2 * r):
        ym4 -= r
    elif (x - xm4 <= 0) and (x - xm4 >= -R) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym4 <= R - r) and (y - ym4 >= 0):
        ym4 += r

    if (xm5 - x <= R + r) and (xm5 - x >= 2 * r) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym5 <= R) and (y - ym5 >= -R):
        xm5 -= r
    elif (x - xm5 <= R - r) and (x - xm5 >= 0) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym5 <= R) and (y - ym5 >= -R):
        xm5 += r
    elif (x - xm5 <= 0) and (x - xm5 >= -R) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (ym5 - y <= R + r) and (ym5 - y >= 2 * r):
        ym5 -= r
    elif (x - xm5 <= 0) and (x - xm5 >= -R) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym5 <= R - r) and (y - ym5 >= 0):
        ym5 += r

    if (xm6 - x <= R + r) and (xm6 - x >= 2 * r) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym6 <= R) and (y - ym6 >= -R):
        xm6 -= r
    elif (x - xm6 <= R - r) and (x - xm6 >= 0) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym6 <= R) and (y - ym6 >= -R):
        xm6 += r
    elif (x - xm6 <= 0) and (x - xm6 >= -R) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (ym6 - y <= R + r) and (ym6 - y >= 2 * r):
        ym6 -= r
    elif (x - xm6 <= 0) and (x - xm6 >= -R) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym6 <= R - r) and (y - ym6 >= 0):
        ym6 += r

    if (xm7 - x <= R + r) and (xm7 - x >= 2 * r) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym7 <= R) and (y - ym7 >= -R):
        xm7 -= r
    elif (x - xm7 <= R - r) and (x - xm7 >= 0) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym7 <= R) and (y - ym7 >= -R):
        xm7 += r
    elif (x - xm7 <= 0) and (x - xm7 >= -R) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (ym7 - y <= R + r) and (ym7 - y >= 2 * r):
        ym7 -= r
    elif (x - xm7 <= 0) and (x - xm7 >= -R) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym7 <= R - r) and (y - ym7 >= 0):
        ym7 += r

    if (xm8 - x <= R + r) and (xm8 - x >= 2 * r) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym8 <= R) and (y - ym8 >= -R):
        xm8 -= r
    elif (x - xm8 <= R - r) and (x - xm8 >= 0) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym8 <= R) and (y - ym8 >= -R):
        xm8 += r
    elif (x - xm8 <= 0) and (x - xm8 >= -R) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (ym8 - y <= R + r) and (ym8 - y >= 2 * r):
        ym8 -= r
    elif (x - xm8 <= 0) and (x - xm8 >= -R) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym8 <= R - r) and (y - ym8 >= 0):
        ym8 += r

    if (xm9 - x <= R + r) and (xm9 - x >= 2 * r) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym9 <= R) and (y - ym9 >= -R):
        xm9 -= r
    elif (x - xm9 <= R - r) and (x - xm9 >= 0) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym9 <= R) and (y - ym9 >= -R):
        xm9 += r
    elif (x - xm9 <= 0) and (x - xm9 >= -R) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (ym9 - y <= R + r) and (ym9 - y >= 2 * r):
        ym9 -= r
    elif (x - xm9 <= 0) and (x - xm9 >= -R) and ((x_new == x + r) or (x_new == x - r) or (y_new == y - r) or (y_new == y + r)) and (y - ym9 <= R - r) and (y - ym9 >= 0):
        ym9 += r

def lose():
    canvas.delete('all')
    canvas.create_text(540, 360, font = ('TimesNewRoman', 90), text = 'YOU LOSE', fill = 'blue')

def death():
    global Hm1
    global Hm2
    global Hm3
    global Hm4
    global Hm5
    global Hm6
    global Hm7
    global Hm8
    global Hm9
    global xm1
    global ym1
    global xm2
    global ym2
    global xm3
    global ym3
    global xm4
    global ym4
    global xm5
    global ym5
    global xm6
    global ym6
    global xm7
    global ym7
    global xm8
    global ym8
    global xm9
    global ym9
    if ((Hm1 <= 0) and (Hm2 > 0)):
        rooms1()
        canvas.create_text(xm2, ym2, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if ((Hm1 <= 0) and (Hm2 <= 0)):
        rooms1()
        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if ((Hm2 <= 0) and (Hm1 > 0)):
        rooms1()
        canvas.create_text(xm1, ym1, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 > 0)):
        rooms2()
        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if ((Hm4 <= 0) and (Hm3 > 0) and (Hm5 > 0)):
        rooms2()
        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if ((Hm5 <= 0) and (Hm3 > 0) and (Hm4 > 0)):
        rooms2()
        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
        rooms2()
        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 > 0)):
        rooms2()
        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if ((Hm3 > 0) and (Hm4 <= 0) and (Hm5 <= 0)):
        rooms2()
        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 <= 0)):
        rooms2()
        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 > 0)):
        rooms3()
        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if ((Hm7 <= 0) and (Hm6 > 0) and (Hm8 > 0) and (Hm9 > 0)):
        rooms3()
        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if ((Hm8 <= 0) and (Hm6 > 0) and (Hm7 > 0) and (Hm9 > 0)):
        rooms3()
        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if ((Hm9 <= 0) and (Hm6 > 0) and (Hm7 > 0) and (Hm8 > 0)):
        rooms3()
        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
        rooms3()
    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 > 0)):
        rooms3()
        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if ((Hm6 > 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
        rooms3()
        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
        rooms3()
        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 > 0)):
        rooms3()
        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 <= 0)):
        rooms3()
        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
        rooms3()
        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
        rooms3()
        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
        rooms3()
        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
        rooms3()
        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
        rooms3()
        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')

def open_door():
    global x
    global y
    global k
    global xm1
    global ym1
    global xm2
    global ym2
    global xm3
    global ym3
    global xm4
    global ym4
    global xm5
    global ym5
    global xm6
    global ym6
    global xm7
    global ym7
    global xm8
    global ym8
    global xm9
    global ym9
    global text_x
    global text_y
    if (x >= 240):
        while k < 1:
            x -= 15
            k += 1
        main()
        canvas.create_line(600, 245, 600, 280, fill = 'red', width = 5)
        canvas.create_line(960, 260, 960, 295, fill = 'red', width = 5)
        if ((Hm1 <= 0) and (Hm2 > 0)):
            rooms2()
            canvas.create_text(xm2, ym2, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm1 <= 0) and (Hm2 <= 0)):
            rooms2()
            canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm2 <= 0) and (Hm1 > 0)):
            rooms2()
            canvas.create_text(xm1, ym1, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 > 0)):
            rooms2()
            canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm4 <= 0) and (Hm3 > 0) and (Hm5 > 0)):
            rooms2()
            canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm5 <= 0) and (Hm3 > 0) and (Hm4 > 0)):
            rooms2()
            canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
            rooms2()
            canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 > 0)):
            rooms2()
            canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm3 > 0) and (Hm4 <= 0) and (Hm5 <= 0)):
            rooms2()
            canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 <= 0)):
            rooms2()
            canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= 585):
        while k < 2:
            x -= 15
            k += 1
        main()
        canvas.create_line(960, 260, 960, 295, fill = 'red', width = 5)
        if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 > 0)):
            rooms3()
            canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm4 <= 0) and (Hm3 > 0) and (Hm5 > 0)):
            rooms3()
            canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm5 <= 0) and (Hm3 > 0) and (Hm4 > 0)):
            rooms3()
            canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
            rooms3()
            canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 > 0)):
            rooms3()
            canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm3 > 0) and (Hm4 <= 0) and (Hm5 <= 0)):
            rooms3()
            canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 <= 0)):
            rooms3()
            canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 > 0)):
            rooms3()
            canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm7 <= 0) and (Hm6 > 0) and (Hm8 > 0) and (Hm9 > 0)):
            rooms3()
            canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm8 <= 0) and (Hm6 > 0) and (Hm7 > 0) and (Hm9 > 0)):
            rooms3()
            canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm9 <= 0) and (Hm6 > 0) and (Hm7 > 0) and (Hm8 > 0)):
            rooms3()
            canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
            rooms3()
        if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 > 0)):
            rooms3()
            canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm6 > 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
            rooms3()
            canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
            rooms3()
            canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 > 0)):
            rooms3()
            canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 <= 0)):
            rooms3()
            canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
            rooms3()
            canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
            canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
            rooms3()
            canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
            rooms3()
            canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
            rooms3()
            canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
        if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
            rooms3()
            canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= 945):
        while k < 3:
            x -= 15
            k += 1
        canvas.delete('all')
        canvas.create_text(540, 360, font = ('TimesNewRoman', 90), text = 'YOU WIN', fill = 'blue')

def war1():
    global x
    global y
    global Hm1
    global Hm2
    global Hm3
    global Hm4
    global Hm5
    global Hm6
    global Hm7
    global Hm8
    global Hm9
    global Ha
    global Ha_new
    global Am
    global Aa
    global Aa_base
    global Aa_mod
    global xm1
    global ym1
    global xm2
    global ym2
    global xm3
    global ym3
    global xm4
    global ym4
    global xm5
    global ym5
    global xm6
    global ym6
    global xm7
    global ym7
    global xm8
    global ym8
    global xm9
    global ym9
    if (x >= xm1 - 30) and (y >= ym1 - 30) and (y <= ym1) and (x <= xm1):
        while (Hm1 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 19):
                    Dmg = randint(1, 4) * 2 + Aa_mod
                    Hm1 = Hm1 - Dmg
                    if ((Hm1 <= 0) and (Hm2 > 0)):
                        rooms1()
                        canvas.create_text(xm2, ym2, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm1 <= 0) and (Hm2 <= 0)):
                        rooms1()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 4) + Aa_mod
                    Hm1 = Hm1 - Dmg
                    if ((Hm1 <= 0) and (Hm2 > 0)):
                        rooms1()
                        canvas.create_text(xm2, ym2, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm1 <= 0) and (Hm2 <= 0)):
                        rooms1()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm2 - 30) and (y >= ym2 - 30) and (y <= ym2) and (x <= xm2):
        while (Hm2 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 19):
                    Dmg = randint(1, 4) * 2 + Aa_mod
                    Hm2 = Hm2 - Dmg
                    if ((Hm2 <= 0) and (Hm1 > 0)):
                        rooms1()
                        canvas.create_text(xm1, ym1, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm1 <= 0) and (Hm2 <= 0)):
                        rooms1()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 4) + Aa_mod
                    Hm2 = Hm2 - Dmg
                    if ((Hm2 <= 0) and (Hm1 > 0)):
                        rooms1()
                        canvas.create_text(xm1, ym1, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm1 <= 0) and (Hm2 <= 0)):
                        rooms1()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm3 - 30) and (y >= ym3 - 30) and (y <= ym3) and (x <= xm3):
        while (Hm3 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 19):
                    Dmg = randint(1, 4) * 2 + Aa_mod
                    Hm3 = Hm3 - Dmg
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 4) + Aa_mod
                    Hm3 = Hm3 - Dmg
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm4 - 30) and (y >= ym4 - 30) and (y <= ym4) and (x <= xm4):
        while (Hm4 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 19):
                    Dmg = randint(1, 4) * 2 + Aa_mod
                    Hm4 = Hm4 - Dmg
                    if ((Hm4 <= 0) and (Hm3 > 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 > 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 4) + Aa_mod
                    Hm4 = Hm4 - Dmg
                    if ((Hm4 <= 0) and (Hm3 > 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 > 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm5 - 30) and (y >= ym5 - 30) and (y <= ym5) and (x <= xm5):
        while (Hm5 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 19):
                    Dmg = randint(1, 4) * 2 + Aa_mod
                    Hm5 = Hm5 - Dmg
                    if ((Hm5 <= 0) and (Hm3 > 0) and (Hm4 > 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 > 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 4) + Aa_mod
                    Hm5 = Hm5 - Dmg
                    if ((Hm5 <= 0) and (Hm3 > 0) and (Hm4 > 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 > 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm6 - 30) and (y >= ym6 - 30) and (y <= ym6) and (x <= xm6):
        while (Hm6 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 19):
                    Dmg = randint(1, 4) * 2 + Aa_mod
                    Hm6 = Hm6 - Dmg
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    elif ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 4) + Aa_mod
                    Hm6 = Hm6 - Dmg
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    elif ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm7 - 30) and (y >= ym7 - 30) and (y <= ym7) and (x <= xm7):
        while (Hm7 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 19):
                    Dmg = randint(1, 4) * 2 + Aa_mod
                    Hm7 = Hm7 - Dmg
                    if ((Hm7 <= 0) and (Hm6 > 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 4) + Aa_mod
                    Hm7 = Hm7 - Dmg
                    if ((Hm7 <= 0) and (Hm6 > 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm8 - 30) and (y >= ym8 - 30) and (y <= ym8) and (x <= xm8):
        while (Hm8 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 19):
                    Dmg = randint(1, 4) * 2 + Aa_mod
                    Hm8 = Hm8 - Dmg
                    if ((Hm8 <= 0) and (Hm6 > 0) and (Hm7 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 > 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 4) + Aa_mod
                    Hm8 = Hm8 - Dmg
                    if ((Hm8 <= 0) and (Hm6 > 0) and (Hm7 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 > 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm9 - 30) and (y >= ym9 - 30) and (y <= ym9) and (x <= xm9):
        while (Hm9 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 19):
                    Dmg = randint(1, 4) * 2 + Aa_mod
                    Hm9 = Hm9 - Dmg
                    if ((Hm9 <= 0) and (Hm6 > 0) and (Hm7 > 0) and (Hm8 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 > 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 4) + Aa_mod
                    Hm9 = Hm9 - Dmg
                    if ((Hm9 <= 0) and (Hm6 > 0) and (Hm7 > 0) and (Hm8 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 > 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')

def war2():
    global x
    global y
    global Hm1
    global Hm2
    global Hm3
    global Hm4
    global Hm5
    global Hm6
    global Hm7
    global Hm8
    global Hm9
    global Ha
    global Ha_new
    global Am
    global Aa
    global Aa_base
    global Aa_mod
    global xm1
    global ym1
    global xm2
    global ym2
    global xm3
    global ym3
    global xm4
    global ym4
    global xm5
    global ym5
    global xm6
    global ym6
    global xm7
    global ym7
    global xm8
    global ym8
    global xm9
    global ym9
    if (x >= xm1 - 30) and (y >= ym1 - 30) and (y <= ym1) and (x <= xm1):
        while (Hm1 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 19):
                    Dmg = randint(1, 8) * 2 + Aa_mod
                    Hm1 = Hm1 - Dmg
                    if ((Hm1 <= 0) and (Hm2 > 0)):
                        rooms1()
                        canvas.create_text(xm2, ym2, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm1 <= 0) and (Hm2 <= 0)):
                        rooms1()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 8) + Aa_mod
                    Hm1 = Hm1 - Dmg
                    if ((Hm1 <= 0) and (Hm2 > 0)):
                        rooms1()
                        canvas.create_text(xm2, ym2, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm1 <= 0) and (Hm2 <= 0)):
                        rooms1()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm2 - 30) and (y >= ym2 - 30) and (y <= ym2) and (x <= xm2):
        while (Hm2 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 19):
                    Dmg = randint(1, 8) + Aa_mod
                    Hm2 = Hm2 - Dmg
                    if ((Hm2 <= 0) and (Hm1 > 0)):
                        rooms1()
                        canvas.create_text(xm1, ym1, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm1 <= 0) and (Hm2 <= 0)):
                        rooms1()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 8) + Aa_mod
                    Hm2 = Hm2 - Dmg
                    if ((Hm2 <= 0) and (Hm1 > 0)):
                        rooms1()
                        canvas.create_text(xm1, ym1, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm1 <= 0) and (Hm2 <= 0)):
                        rooms1()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm3 - 30) and (y >= ym3 - 30) and (y <= ym3) and (x <= xm3):
        while (Hm3 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 19):
                    Dmg = randint(1, 8) * 2 + Aa_mod
                    Hm3 = Hm3 - Dmg
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 8) + Aa_mod
                    Hm3 = Hm3 - Dmg
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm4 - 30) and (y >= ym4 - 30) and (y <= ym4) and (x <= xm4):
        while (Hm4 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 19):
                    Dmg = randint(1, 8) * 2 + Aa_mod
                    Hm4 = Hm4 - Dmg
                    if ((Hm4 <= 0) and (Hm3 > 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 > 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 8) + Aa_mod
                    Hm4 = Hm4 - Dmg
                    if ((Hm4 <= 0) and (Hm3 > 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 > 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm5 - 30) and (y >= ym5 - 30) and (y <= ym5) and (x <= xm5):
        while (Hm5 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 19):
                    Dmg = randint(1, 8) * 2 + Aa_mod
                    Hm5 = Hm5 - Dmg
                    if ((Hm5 <= 0) and (Hm3 > 0) and (Hm4 > 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 > 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 8) + Aa_mod
                    Hm5 = Hm5 - Dmg
                    if ((Hm5 <= 0) and (Hm3 > 0) and (Hm4 > 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 > 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm6 - 30) and (y >= ym6 - 30) and (y <= ym6) and (x <= xm6):
        while (Hm6 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 19):
                    Dmg = randint(1, 8) * 2 + Aa_mod
                    Hm6 = Hm6 - Dmg
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    elif ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 8) + Aa_mod
                    Hm6 = Hm6 - Dmg
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    elif ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm7 - 30) and (y >= ym7 - 30) and (y <= ym7) and (x <= xm7):
        while (Hm7 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 19):
                    Dmg = randint(1, 8) * 2 + Aa_mod
                    Hm7 = Hm7 - Dmg
                    if ((Hm7 <= 0) and (Hm6 > 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 8) + Aa_mod
                    Hm7 = Hm7 - Dmg
                    if ((Hm7 <= 0) and (Hm6 > 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm8 - 30) and (y >= ym8 - 30) and (y <= ym8) and (x <= xm8):
        while (Hm8 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 19):
                    Dmg = randint(1, 8) * 2 + Aa_mod
                    Hm8 = Hm8 - Dmg
                    if ((Hm8 <= 0) and (Hm6 > 0) and (Hm7 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 > 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 8) + Aa_mod
                    Hm8 = Hm8 - Dmg
                    if ((Hm8 <= 0) and (Hm6 > 0) and (Hm7 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 > 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm9 - 30) and (y >= ym9 - 30) and (y <= ym9) and (x <= xm9):
        while (Hm9 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 19):
                    Dmg = randint(1, 8) * 2 + Aa_mod
                    Hm9 = Hm9 - Dmg
                    if ((Hm9 <= 0) and (Hm6 > 0) and (Hm7 > 0) and (Hm8 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 > 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 8) + Aa_mod
                    Hm9 = Hm9 - Dmg
                    if ((Hm9 <= 0) and (Hm6 > 0) and (Hm7 > 0) and (Hm8 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 > 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')

def war3():
    global x
    global y
    global Hm1
    global Hm2
    global Hm3
    global Hm4
    global Hm5
    global Hm6
    global Hm7
    global Hm8
    global Hm9
    global Ha
    global Ha_new
    global Am
    global Aa
    global Aa_base
    global Aa_mod
    global xm1
    global ym1
    global xm2
    global ym2
    global xm3
    global ym3
    global xm4
    global ym4
    global xm5
    global ym5
    global xm6
    global ym6
    global xm7
    global ym7
    global xm8
    global ym8
    global xm9
    global ym9
    if (x >= xm1 - 30) and (y >= ym1 - 30) and (y <= ym1) and (x <= xm1):
        while (Hm1 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 20):
                    Dmg = randint(1, 8) * 3 + Aa_mod
                    Hm1 = Hm1 - Dmg
                    if ((Hm1 <= 0) and (Hm2 > 0)):
                        rooms1()
                        canvas.create_text(xm2, ym2, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm1 <= 0) and (Hm2 <= 0)):
                        rooms1()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 8)+ Aa_mod
                    Hm1 = Hm1 - Dmg
                    if ((Hm1 <= 0) and (Hm2 > 0)):
                        rooms1()
                        canvas.create_text(xm2, ym2, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm1 <= 0) and (Hm2 <= 0)):
                        rooms1()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm2 - 30) and (y >= ym2 - 30) and (y <= ym2) and (x <= xm2):
        while (Hm2 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 20):
                    Dmg = randint(1, 8) * 3 + Aa_mod
                    Hm2 = Hm2 - Dmg
                    if ((Hm2 <= 0) and (Hm1 > 0)):
                        rooms1()
                        canvas.create_text(xm1, ym1, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm1 <= 0) and (Hm2 <= 0)):
                        rooms1()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 8) + Aa_mod
                    Hm2 = Hm2 - Dmg
                    if ((Hm2 <= 0) and (Hm1 > 0)):
                        rooms1()
                        canvas.create_text(xm1, ym1, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm1 <= 0) and (Hm2 <= 0)):
                        rooms1()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm3 - 30) and (y >= ym3 - 30) and (y <= ym3) and (x <= xm3):
        while (Hm3 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 20):
                    Dmg = randint(1, 8) * 3 + Aa_mod
                    Hm3 = Hm3 - Dmg
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 8) + Aa_mod
                    Hm3 = Hm3 - Dmg
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm4 - 30) and (y >= ym4 - 30) and (y <= ym4) and (x <= xm4):
        while (Hm4 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 20):
                    Dmg = randint(1, 8) * 3 + Aa_mod
                    Hm4 = Hm4 - Dmg
                    if ((Hm4 <= 0) and (Hm3 > 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 > 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 8) + Aa_mod
                    Hm4 = Hm4 - Dmg
                    if ((Hm4 <= 0) and (Hm3 > 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 > 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm5 - 30) and (y >= ym5 - 30) and (y <= ym5) and (x <= xm5):
        while (Hm5 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 20):
                    Dmg = randint(1, 8) * 3 + Aa_mod
                    Hm5 = Hm5 - Dmg
                    if ((Hm5 <= 0) and (Hm3 > 0) and (Hm4 > 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 > 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 8) + Aa_mod
                    Hm5 = Hm5 - Dmg
                    if ((Hm5 <= 0) and (Hm3 > 0) and (Hm4 > 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 > 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm6 - 30) and (y >= ym6 - 30) and (y <= ym6) and (x <= xm6):
        while (Hm6 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 20):
                    Dmg = randint(1, 8) * 3 + Aa_mod
                    Hm6 = Hm6 - Dmg
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    elif ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 8) + Aa_mod
                    Hm6 = Hm6 - Dmg
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    elif ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm7 - 30) and (y >= ym7 - 30) and (y <= ym7) and (x <= xm7):
        while (Hm7 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 20):
                    Dmg = randint(1, 8) * 3 + Aa_mod
                    Hm7 = Hm7 - Dmg
                    if ((Hm7 <= 0) and (Hm6 > 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 8) + Aa_mod
                    Hm7 = Hm7 - Dmg
                    if ((Hm7 <= 0) and (Hm6 > 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm8 - 30) and (y >= ym8 - 30) and (y <= ym8) and (x <= xm8):
        while (Hm8 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 20):
                    Dmg = randint(1, 8) * 3 + Aa_mod
                    Hm8 = Hm8 - Dmg
                    if ((Hm8 <= 0) and (Hm6 > 0) and (Hm7 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 > 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 8) + Aa_mod
                    Hm8 = Hm8 - Dmg
                    if ((Hm8 <= 0) and (Hm6 > 0) and (Hm7 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 > 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm9 - 30) and (y >= ym9 - 30) and (y <= ym9) and (x <= xm9):
        while (Hm9 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 20):
                    Dmg = randint(1, 8) * 3 + Aa_mod
                    Hm9 = Hm9 - Dmg
                    if ((Hm9 <= 0) and (Hm6 > 0) and (Hm7 > 0) and (Hm8 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 > 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 8) + Aa_mod
                    Hm9 = Hm9 - Dmg
                    if ((Hm9 <= 0) and (Hm6 > 0) and (Hm7 > 0) and (Hm8 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 > 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')

def war4():
    global x
    global y
    global Hm1
    global Hm2
    global Hm3
    global Hm4
    global Hm5
    global Hm6
    global Hm7
    global Hm8
    global Hm9
    global Ha
    global Ha_new
    global Am
    global Aa
    global Aa_base
    global Aa_mod
    global xm1
    global ym1
    global xm2
    global ym2
    global xm3
    global ym3
    global xm4
    global ym4
    global xm5
    global ym5
    global xm6
    global ym6
    global xm7
    global ym7
    global xm8
    global ym8
    global xm9
    global ym9
    if (x >= xm1 - 30) and (y >= ym1 - 30) and (y <= ym1) and (x <= xm1):
        while (Hm1 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 18):
                    Dmg = randint(1, 6) * 2 + Aa_mod
                    Hm1 = Hm1 - Dmg
                    if ((Hm1 <= 0) and (Hm2 > 0)):
                        rooms1()
                        canvas.create_text(xm2, ym2, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm1 <= 0) and (Hm2 <= 0)):
                        rooms1()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 6) + Aa_mod
                    Hm1 = Hm1 - Dmg
                    if ((Hm1 <= 0) and (Hm2 > 0)):
                        rooms1()
                        canvas.create_text(xm2, ym2, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm1 <= 0) and (Hm2 <= 0)):
                        rooms1()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm2 - 30) and (y >= ym2 - 30) and (y <= ym2) and (x <= xm2):
        while (Hm2 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 18):
                    Dmg = randint(1, 6) * 2 + Aa_mod
                    Hm2 = Hm2 - Dmg
                    if ((Hm2 <= 0) and (Hm1 > 0)):
                        rooms1()
                        canvas.create_text(xm1, ym1, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm1 <= 0) and (Hm2 <= 0)):
                        rooms1()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 6) + Aa_mod
                    Hm2 = Hm2 - Dmg
                    if ((Hm2 <= 0) and (Hm1 > 0)):
                        rooms1()
                        canvas.create_text(xm1, ym1, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm1 <= 0) and (Hm2 <= 0)):
                        rooms1()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm3 - 30) and (y >= ym3 - 30) and (y <= ym3) and (x <= xm3):
        while (Hm3 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 18):
                    Dmg = randint(1, 6) * 2 + Aa_mod
                    Hm3 = Hm3 - Dmg
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 6) + Aa_mod
                    Hm3 = Hm3 - Dmg
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm4 - 30) and (y >= ym4 - 30) and (y <= ym4) and (x <= xm4):
        while (Hm4 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 18):
                    Dmg = randint(1, 6) * 2 + Aa_mod
                    Hm4 = Hm4 - Dmg
                    if ((Hm4 <= 0) and (Hm3 > 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 > 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 6) + Aa_mod
                    Hm4 = Hm4 - Dmg
                    if ((Hm4 <= 0) and (Hm3 > 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 > 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm5 - 30) and (y >= ym5 - 30) and (y <= ym5) and (x <= xm5):
        while (Hm5 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 18):
                    Dmg = randint(1, 6) * 2 + Aa_mod
                    Hm5 = Hm5 - Dmg
                    if ((Hm5 <= 0) and (Hm3 > 0) and (Hm4 > 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 > 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 6) + Aa_mod
                    Hm5 = Hm5 - Dmg
                    if ((Hm5 <= 0) and (Hm3 > 0) and (Hm4 > 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 > 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm6 - 30) and (y >= ym6 - 30) and (y <= ym6) and (x <= xm6):
        while (Hm6 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 18):
                    Dmg = randint(1, 6) * 2 + Aa_mod
                    Hm6 = Hm6 - Dmg
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    elif ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 6) + Aa_mod
                    Hm6 = Hm6 - Dmg
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    elif ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm7 - 30) and (y >= ym7 - 30) and (y <= ym7) and (x <= xm7):
        while (Hm7 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 18):
                    Dmg = randint(1, 6) * 2 + Aa_mod
                    Hm7 = Hm7 - Dmg
                    if ((Hm7 <= 0) and (Hm6 > 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 6) + Aa_mod
                    Hm7 = Hm7 - Dmg
                    if ((Hm7 <= 0) and (Hm6 > 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm8 - 30) and (y >= ym8 - 30) and (y <= ym8) and (x <= xm8):
        while (Hm8 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 18):
                    Dmg = randint(1, 6) * 2 + Aa_mod
                    Hm8 = Hm8 - Dmg
                    if ((Hm8 <= 0) and (Hm6 > 0) and (Hm7 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 > 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 6) + Aa_mod
                    Hm8 = Hm8 - Dmg
                    if ((Hm8 <= 0) and (Hm6 > 0) and (Hm7 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 > 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm9 - 30) and (y >= ym9 - 30) and (y <= ym9) and (x <= xm9):
        while (Hm9 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 18):
                    Dmg = randint(1, 6) * 2 + Aa_mod
                    Hm9 = Hm9 - Dmg
                    if ((Hm9 <= 0) and (Hm6 > 0) and (Hm7 > 0) and (Hm8 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 > 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = randint(1, 6) + Aa_mod
                    Hm9 = Hm9 - Dmg
                    if ((Hm9 <= 0) and (Hm6 > 0) and (Hm7 > 0) and (Hm8 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 > 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')

def war5():
    global x
    global y
    global Hm1
    global Hm2
    global Hm3
    global Hm4
    global Hm5
    global Hm6
    global Hm7
    global Hm8
    global Hm9
    global Ha
    global Ha_new
    global Am
    global Aa
    global Aa_base
    global Aa_mod
    global xm1
    global ym1
    global xm2
    global ym2
    global xm3
    global ym3
    global xm4
    global ym4
    global xm5
    global ym5
    global xm6
    global ym6
    global xm7
    global ym7
    global xm8
    global ym8
    global xm9
    global ym9
    if (x >= xm1 - 30) and (y >= ym1 - 30) and (y <= ym1) and (x <= xm1):
        while (Hm1 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 20):
                    Dmg = (randint(1, 6) + randint(1, 6)) * 4 + Aa_mod
                    Hm1 = Hm1 - Dmg
                    if ((Hm1 <= 0) and (Hm2 > 0)):
                        rooms1()
                        canvas.create_text(xm2, ym2, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm1 <= 0) and (Hm2 <= 0)):
                        rooms1()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = (randint(1, 6) + randint(1, 6)) + Aa_mod
                    Hm1 = Hm1 - Dmg
                    if ((Hm1 <= 0) and (Hm2 > 0)):
                        rooms1()
                        canvas.create_text(xm2, ym2, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm1 <= 0) and (Hm2 <= 0)):
                        rooms1()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm2 - 30) and (y >= ym2 - 30) and (y <= ym2) and (x <= xm2):
        while (Hm2 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 20):
                    Dmg = (randint(1, 6) + randint(1, 6)) * 4 + Aa_mod
                    Hm2 = Hm2 - Dmg
                    if ((Hm2 <= 0) and (Hm1 > 0)):
                        rooms1()
                        canvas.create_text(xm1, ym1, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm1 <= 0) and (Hm2 <= 0)):
                        rooms1()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = (randint(1, 6) + randint(1, 6)) + Aa_mod
                    Hm2 = Hm2 - Dmg
                    if ((Hm2 <= 0) and (Hm1 > 0)):
                        rooms1()
                        canvas.create_text(xm1, ym1, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm1 <= 0) and (Hm2 <= 0)):
                        rooms1()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm3 - 30) and (y >= ym3 - 30) and (y <= ym3) and (x <= xm3):
        while (Hm3 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 20):
                    Dmg = (randint(1, 6) + randint(1, 6)) * 4 + Aa_mod
                    Hm3 = Hm3 - Dmg
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = (randint(1, 6) + randint(1, 6)) + Aa_mod
                    Hm3 = Hm3 - Dmg
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm4 - 30) and (y >= ym4 - 30) and (y <= ym4) and (x <= xm4):
        while (Hm4 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 20):
                    Dmg = (randint(1, 6) + randint(1, 6)) * 4 + Aa_mod
                    Hm4 = Hm4 - Dmg
                    if ((Hm4 <= 0) and (Hm3 > 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 > 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = (randint(1, 6) + randint(1, 6)) + Aa_mod
                    Hm4 = Hm4 - Dmg
                    if ((Hm4 <= 0) and (Hm3 > 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 > 0)):
                        rooms2()
                        canvas.create_text(xm5, ym5, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 > 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm5 - 30) and (y >= ym5 - 30) and (y <= ym5) and (x <= xm5):
        while (Hm5 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 20):
                    Dmg = (randint(1, 6) + randint(1, 6)) * 4 + Aa_mod
                    Hm5 = Hm5 - Dmg
                    if ((Hm5 <= 0) and (Hm3 > 0) and (Hm4 > 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 > 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = (randint(1, 6) + randint(1, 6)) + Aa_mod
                    Hm5 = Hm5 - Dmg
                    if ((Hm5 <= 0) and (Hm3 > 0) and (Hm4 > 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 > 0) and (Hm4 <= 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm3, ym3, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm3 <= 0) and (Hm4 > 0) and (Hm5 <= 0)):
                        rooms2()
                        canvas.create_text(xm4, ym4, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm6 - 30) and (y >= ym6 - 30) and (y <= ym6) and (x <= xm6):
        while (Hm6 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 20):
                    Dmg = (randint(1, 6) + randint(1, 6)) * 4 + Aa_mod
                    Hm6 = Hm6 - Dmg
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    elif ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = (randint(1, 6) + randint(1, 6)) + Aa_mod
                    Hm6 = Hm6 - Dmg
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    elif ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm7 - 30) and (y >= ym7 - 30) and (y <= ym7) and (x <= xm7):
        while (Hm7 > 0):
            AAm = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 20):
                    Dmg = (randint(1, 6) + randint(1, 6)) * 4 + Aa_mod
                    Hm7 = Hm7 - Dmg
                    if ((Hm7 <= 0) and (Hm6 > 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = (randint(1, 6) + randint(1, 6)) + Aa_mod
                    Hm7 = Hm7 - Dmg
                    if ((Hm7 <= 0) and (Hm6 > 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm8 - 30) and (y >= ym8 - 30) and (y <= ym8) and (x <= xm8):
        while (Hm8 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 20):
                    Dmg = (randint(1, 6) + randint(1, 6)) * 4 + Aa_mod
                    Hm8 = Hm8 - Dmg
                    if ((Hm8 <= 0) and (Hm6 > 0) and (Hm7 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 > 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = (randint(1, 6) + randint(1, 6)) + Aa_mod
                    Hm8 = Hm8 - Dmg
                    if ((Hm8 <= 0) and (Hm6 > 0) and (Hm7 > 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 > 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 > 0)):
                        rooms3()
                        canvas.create_text(xm9, ym9, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
    if (x >= xm9 - 30) and (y >= ym9 - 30) and (y <= ym9) and (x <= xm9):
        while (Hm9 > 0):
            Am = randint(1, 6)
            Aa = randint(1, 20)
            Aa_new = Aa + Aa_base + Aa_mod
            if (Aa_new < 16):
                Ha = Ha - Am
            else:
                if (Aa >= 20):
                    Dmg = (randint(1, 6) + randint(1, 6)) * 4 + Aa_mod
                    Hm9 = Hm9 - Dmg
                    if ((Hm9 <= 0) and (Hm6 > 0) and (Hm7 > 0) and (Hm8 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 > 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                else:
                    Dmg = (randint(1, 6) + randint(1, 6)) + Aa_mod
                    Hm9 = Hm9 - Dmg
                    if ((Hm9 <= 0) and (Hm6 > 0) and (Hm7 > 0) and (Hm8 > 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 <= 0) and  (Hm9 <= 0)):
                        rooms3()
                    if ((Hm6 > 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 > 0) and (Hm7 <= 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm6, ym6, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 > 0) and (Hm8 <= 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm7, ym7, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')
                    if ((Hm6 <= 0) and (Hm7 <= 0) and (Hm8 > 0) and (Hm9 <= 0)):
                        rooms3()
                        canvas.create_text(xm8, ym8, anchor = W, font = ('TimesNewRoman', 12), text = 'm', fill = 'red')

canvas.bind_all('<Right>', right)
canvas.bind_all('<Left>', left)
canvas.bind_all('<Up>', up)
canvas.bind_all('<Down>', down)

canvas.mainloop()
