import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

not_safe_blocks = [block.AIR.id,
                   block.WATER_STATIONARY.id, block.WATER_FLOWING.id]

glass = block.GLASS.id

def buildBridge():
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x, pos.y-1, pos.z)
    if b in not_safe_blocks:
        mc.setBlock(pos.x,pos.y-1,pos.z,glass)


while True:
    buildBridge()
