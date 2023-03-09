import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

not_safe_blocks = [block.AIR.id,
                   block.WATER_STATIONARY.id, block.WATER_FLOWING.id]


def safeFeet():
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x, pos.y-1, pos.z)
    if b in not_safe_blocks:
        mc.postToChat('not safe')
    else:
        mc.postToChat('safe')


while True:
    time.sleep(0.5)
    safeFeet()
