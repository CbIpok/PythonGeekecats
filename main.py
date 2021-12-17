from mcpi.minecraft import Minecraft
import numpy as np
import time
import mcpi.block
import font
import asyncio
import image_print

mc = Minecraft.create()  # Подключение к миру Minecraft

x,y,z = mc.player.getTilePos()  # Получение координат игрока

font.print_text(x,y,z,"!№;%:?*()_",mcpi.block.TNT)
# image_print.print_image(pos,mc)
# mc.getBlock(x, y, z)



#font.print_text(x,y,z,"MC",mcpi.block.WOOL)

# async def get_value(massive, index):
#     await asyncio.sleep(0.5)
#     massive[index] = 5
#
#
# async def get_values(len_):
#     tasks = []
#     values = np.zeros(len_)
#     for i in range(len_):
#         tasks.append(asyncio.create_task(get_value(values, i)))
#     print("tasks created")
#     for task in tasks:
#         await task
#     print("tasks complited")
#     return values
#
#
# x = 0
# start = time.time()
# values = asyncio.run(get_values(20))
# time_process = time.time() - start
# print(time_process)
# print(values)
