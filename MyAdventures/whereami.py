import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    mc.postToChat("My Pos: x=" + str(pos.x) + " z=" +
                  str(pos.z) + " y=" + str(pos.y))
