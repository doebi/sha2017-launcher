import ugfx, json
from time import *

ugfx.init()

ugfx.clear();

font = "pixelade13"
w = 296
h = 128

text = "The festival is organized for and by volunteers from and around all facets of the international hacker community."

applistOffset = (10, 34)
infoOffset = (5, 85)
iconSize = 48

def drawCursor(i):
    ugfx.box(applistOffset[0] + i*(10 + iconSize) - 3, applistOffset[1] - 17, iconSize + 6, iconSize + 20, 0)

def drawBattery(percent):
    bw = int(20 * (percent / 100))
    ugfx.area(w-22, 1, bw, 10, 0)

# statusbar
ugfx.string(1, 0, "Sun, 18.06.2017", font, 0)
ugfx.string_box(0, 0, w, 13, "doebi", font, 0, ugfx.justifyCenter)
ugfx.line(0, 12, w, 12, 0)
ugfx.box(w-22, 1, 20, 10, 0)
drawBattery(50)

# applist
apps = ["nametag", "weather", "fahrplan", "foo", "bar"]
for i, app in enumerate(apps):
    ugfx.string_box(applistOffset[0] + i*(10 + iconSize), applistOffset[1]-17, iconSize, 14, app, font, 0, ugfx.justifyCenter)
    ugfx.box(applistOffset[0] + i*(10 + iconSize), applistOffset[1], iconSize, iconSize, 0)

drawCursor(2)

ugfx.line(0, 90, w, 90, 0)

ugfx.string_box(infoOffset[0], infoOffset[1], w, 43, text, font, 0, ugfx.justifyLeft)


ugfx.flush()

while True:
    pass
