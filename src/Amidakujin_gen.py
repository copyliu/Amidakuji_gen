#  -*- coding: UTF-8 -*-
#  +----------------------------------------+
#  |Author: Lau Gin San (CopyLiu)           |
#  |Email:copyliu@gmail.com                 |
#  |                                        |
#  |License:BSD License                     |
#  +----------------------------------------+
import os
import ImageDraw

__author__ = 'CopyLiu'

import random
import Image

random.seed()

def genlist(s, max, height=30, min=2):
    """s 列, p 每列最多橫線數, m 圖高度, min 每列最小橫線數"""

    AmiList = []
    for i in range(s - 1):
        Line = []
        random.seed()
        for j in range(random.randint(min, max)):
            if i == 0:#第一列隨意
                random.seed()
                Line.append(random.randint(1, height))
            else:
                random.seed()
                NewInt = random.randint(1, height)
                while NewInt in AmiList[i - 1]:
                    random.seed()
                    NewInt = random.randint(1, height)
                Line.append(NewInt)
        AmiList.append(Line)
    return AmiList


def drawresult(AmiList, scale=10, mergin=100, yLine=5, xLine=3):
    """繪圖, scale 放大比例"""
    width = (len(AmiList) + 2) * mergin
    height = (max([max(i) for i in AmiList]) + 5 ) * scale
    print (height, width)
    im = Image.new("RGBA", (width, height), "#FFFFFF")
    draw = ImageDraw.Draw(im)
    for i in range(len(AmiList)):
        draw.line((((i + 1) * mergin, scale), ((i + 1) * mergin), height - scale), fill="#000000", width=yLine)  #繪製豎線們
        Line = AmiList[i]
        for j in range(len(Line)):
            draw.line((((i + 1) * mergin, (Line[j] + 1) * scale), ((i + 2) * mergin, (Line[j] + 1) * scale)),
                fill="#000000", width=xLine)
    draw.line((((len(AmiList) + 1) * mergin, 10), ((len(AmiList) + 1) * mergin), height - 10), fill="#000000",
        width=yLine)  #最後一條

    im.save("1.png", "PNG")
    os.system("1.png")


def textresult(AmiList):
    x = len(AmiList)
    y = max([max(i) for i in AmiList])
    for i in range(x + 1):
        thisx = i
        for j in range(y):
            if thisx == 0:#跑到第一列
                if j in AmiList[thisx]:
                    thisx += 1
            elif thisx == x:#跑到最後一列
                if j in AmiList[thisx - 1]:
                    thisx -= 1
            else:
                if j in AmiList[thisx]:
                    thisx += 1
                elif j in AmiList[thisx - 1]:
                    thisx -= 1
        print i, "->", thisx


if __name__ == "__main__":
    MyList = genlist(80, max=10, min=2, height=100)
    drawresult(MyList, mergin=30, scale=10, )#xLine=1,yLine=1)
    textresult(MyList)
