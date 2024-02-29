from random import randrange as rnd, choice
import tkinter as tk
import math
import time

print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

g_y = 9.8 / 3
i = 0

class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.live = 30
     
    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        
        self.x += self.vx
        self.y -= self.vy
        self.vy -= g_y
        self.set_coords()
       
    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        rad_shar = self.r + obj.r
        d = ((obj.x - self.x) ** 2 + (obj.y - self.y) ** 2) ** 0.5
        if (d <= rad_shar):
            return True
        else:
            return False


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20,450,50,420,width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class target():
    def __init__(self):
            self.points = 0
            self.live = 1
            self.id = canv.create_oval(0,0,0,0)
            self.id_points = canv.create_text(30,30,text = self.points,font = '28')
            
    
    def new_target(self):
        """ Инициализация новой цели. """
        self.vx = 5
        self.vy = 5
        x = self.x = rnd(500, 750)
        y = self.y = rnd(50, 550)
        r = self.r = rnd(10, 50)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)
        
    def new_target1(self):
        """ Инициализация новой цели. """
        self.vx = 5
        self.vy = 5
        x = self.x = rnd(500, 750)
        y = self.y = rnd(50, 550)
        r = self.r = rnd(10, 50)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)    
    def new_target2(self):
        """ Инициализация новой цели. """
        self.vx = 5
        self.vy = 5
        x = self.x = rnd(500, 750)
        y = self.y = rnd(50, 550)
        r = self.r = rnd(10, 50)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)    
    def new_target3(self):
        """ Инициализация новой цели. """
        self.vx = 5
        self.vy = 5
        x = self.x = rnd(500, 750)
        y = self.y = rnd(50, 550)
        r = self.r = rnd(10, 50)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)        
    def new_target4(self):
        """ Инициализация новой цели. """
        self.vx = 5
        self.vy = 5
        x = self.x = rnd(500, 750)
        y = self.y = rnd(50, 550)
        r = self.r = rnd(10, 50)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)        

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        if (self.x <= 750 and self.y <= 550) or (self.x >= 400 and self.y >= 50):
            self.x += self.vx
            self.y -= self.vy
            self.set_coords()
        if self.x <= 400 or self.x >= 750:
            self.vx = -self.vx
        if self.y <= 50 or self.y >= 550:
            self.vy = -self.vy
        
    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        for i in range(5):
            self.points += points
        canv.itemconfig(self.id_points, text=self.points)


t1 = target()
t2 = target()
t3 = target()
t4 = target()
t5 = target()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []

k = 0

def new_game(event=''):
    global gun, t1,t2,t3,t4,t5, screen1, balls, bullet
    t1.new_target()
    t2.new_target1()
    t3.new_target2()
    t4.new_target3()
    t5.new_target4()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    k = 0
    z = 0.03
    t1.live = 1
    t2.live = 1
    t3.live = 1
    t4.live = 1
    t5.live = 1
    t1.move()
    t2.move()
    t3.move()
    t4.move()
    t5.move()
    
    while t1.live and t2.live and t3.live and t4.live and t5.live or balls:
        if t1.live == 1:
            t1.move()
        if t2.live == 1:
            t2.move()
        if t3.live == 1:
            t3.move()
        if t4.live == 1:
            t4.move()
        if t5.live == 1:
            t5.move()
        for b in balls:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                k += 1
            if b.hittest(t2) and t2.live:
                t2.live=0
                t2.hit()
                k += 1
            if b.hittest(t3) and t3.live:
                t3.live=0
                t3.hit()
                k += 1
            if b.hittest(t4) and t4.live:
                t4.live =0
                t4.hit()
                k += 1
            if b.hittest(t5) and t5.live:
                t5.live =0
                t5.hit()
                k += 1
            if k==5:
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)


new_game()

mainloop()