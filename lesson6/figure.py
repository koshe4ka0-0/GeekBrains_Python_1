# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math

class figure():

    def P(self):
        pass 

    def high(self):
        pass 

    def S(self):
        pass


class Triangle(figure):
    def __init__(self, xa, xb, xc, ya, yb, yc):
        self._xa = xa
        self._xb = xb
        self._xc = xc

        self._ya = ya
        self._yb = yb
        self._yc = yc

        self.AB = math.sqrt(((xb - xa)**2) + ((yb - xa)**2))
        self.BC = math.sqrt(((xc - xb)**2) + ((yc - yb)**2))
        self.AC = math.sqrt(((xa - xc)**2) + ((ya - yc )**2))

    @property
    def xa(self):
        return self._xa

    @property
    def xb(self):
        return self._xb

    @property
    def xc(self):
        return self._xc

    @property
    def ya(self):
        return self._ya

    @property
    def yb(self):
        return self._yb

    @property
    def yc(self):
        return self._yc

    def P(self):
        self.P = self.AB + self.BC + self.AC
        return self.P

    def S(self):
        self.S = math.sqrt(math.fabs((self.P/2)*((self.P/2) - self.BC)*((self.P/2) - self.AB)*((self.P/2) - self.AC)))
        return self.S

    def h(self):
        self.h = 2 * self.S / self.AC
        return self.h


class trapezium(figure):
    def __init__(self, xa, xb, xc, xd, ya, yb, yc, yd):
        self._xa = xa
        self._xb = xb
        self._xc = xc
        self._xd = xd

        self._ya = ya
        self._yb = yb
        self._yc = yc
        self._yd = yd


        self.AB = math.sqrt(((xb - xa)**2) + ((yb - ya)**2))
        self.BC = math.sqrt(((xc - xb)**2) + ((yc - yb)**2))
        self.CD = math.sqrt(((xd - xc)**2) + ((yd - yc )**2))
        self.DA = math.sqrt(((xa - xd)**2) + ((ya - yd )**2))

    @property
    def xa(self):
        return self._xa

    @property
    def xb(self):
        return self._xb

    @property
    def xc(self):
        return self._xc

    @property
    def xd(self):
        return self._xd

    @property
    def ya(self):
        return self._ya

    @property
    def yb(self):
        return self._yb

    @property
    def yc(self):
        return self._yc

    @property
    def yd(self):
        return self._yd

    def P(self):
        self.P = self.AB + self.BC + self.CD + self.DA
        return self.P

    

    def h(self):
        self.h = math.sqrt(self.BC **2 -(((self.CD - self.AB)**2 + self.BC **2 - self.DA **2)/(2*(self.CD - self.AB)))**2)
        return self.h
        
    def S(self):
        self.S = (self.AB + self.CD) * self.h / 2
        return self.S

    def equal(self):
        if self.CD == self.AB:
            return True
        else:
            return false



    

# tri = Triangle(2,2,5,8,7,4)
tri = Triangle(2,5,7,2,8,4)

print("Треугольник ABC: ")
print("")
print('Сторона А = {}, сторона В = {}, сторона С = {}'.format(tri.AB , tri.BC , tri.AC))
print('Периметр треугольника = {}'.format(tri.P()))
print('Площадь треугольника равна {}'.format(tri.S()))
print('Высота, опущенная на сторону А = {}'.format(tri.h()))
print("")

trap  = trapezium(6, 6, 1, 1, 21, 15,13, 17)
# trap  = trapezium(2, 10, 7, 4, 1, 1, 9, 9)

print("")
print("Трапеция ABCD с основаниями AB DC:")
print("")
print('Сторона АB = {}, сторона ВC = {}, сторона СD = {}, сторона DA = {}'.format(trap.AB , trap.BC , trap.CD, trap.DA))
print('Периметр трапеции = {}'.format(trap.P()))
print('Высота трапеции равна {}'.format(trap.h()))
print('Площадь трапеции равна {}'.format(trap.S()))

if trap.equal is True:
    print("Трапеция ABCD равнобедренная ")
else:
    print("Трапеция ABCD не равнобедренная ")





    