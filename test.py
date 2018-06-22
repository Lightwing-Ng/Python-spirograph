#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Jun 23, 2018, 03:51
 * Software: PyCharm
 * Project Name: Tutorial
"""

import math
import turtle


# draw circle using turtle
def drawCircleTurtle(x, y, r):
    # got to start of circle
    turtle.up()
    turtle.setpos(x + r, y)
    turtle.down()

    # draw circle
    for i in range(0, 365, 5):
        a = math.radians(i)
        turtle.setpos(x + r * math.cos(a), y + r * math.sin(a))


# draw spiral using turtle
def drawSpiralTurtle(x, y, r):
    # got to start of spiral
    turtle.up()
    turtle.setpos(x + r, y)
    turtle.down()

    # draw spiral
    for i in range(0, 360 * 10, 5):
        a = math.radians(i)
        x = r * math.cos(a) * math.exp(0.05 * a)
        y = r * math.sin(a) * math.exp(0.05 * a)
        turtle.setpos(x, y)


def main():
    print('testing...')
    drawCircleTurtle(100, 100, 50)
    drawSpiralTurtle(0, 0, 5)
    turtle.mainloop()


# call main
if __name__ == '__main__':
    main()
