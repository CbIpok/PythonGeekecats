from mcpi.minecraft import Minecraft
import numpy as np
import time
import asyncio
start = 0

mc = Minecraft.create()  # Подключение к миру Minecraft

x, y, z = mc.player.getTilePos()  # Получение координат игрока

print(x, y, z)


async def get_value(x, y, z, index_x, index_y, index_z, data):
    data[index_x][index_y][index_z] = mc.getBlock(x, y, z)


async def get_cube(x_start, y_start, z_start, dx, dy, dz):
    x_range = range(min(x_start, x_start + dx), max(x_start, x_start + dx))
    y_range = range(min(y_start, y_start + dy), max(y_start, y_start + dy))
    z_range = range(min(z_start, z_start + dx), max(z_start, z_start + dz))
    data = np.zeros((len(x_range), len(y_range), len(z_range)))
    tasks = []
    global start
    for x in x_range:
        for y in y_range:
            for z in z_range:
                index_x = x - x_range[0]
                index_y = y - y_range[0]
                index_z = z - z_range[0]
                tasks.append(asyncio.create_task(get_value(x, y, z, index_x, index_y, index_z, data)))
    print("tasks created in ", time.time() - start)
    for task in tasks:
        await task
    print("tasks complited in ", time.time() - start)
    return data


def build_cube(x_start, y_start, z_start, dx, dy, dz, data):
    x_range = range(min(x_start, x_start + dx), max(x_start, x_start + dx))
    y_range = range(min(y_start, y_start + dy), max(y_start, y_start + dy))
    z_range = range(min(z_start, z_start + dx), max(z_start, z_start + dz))
    for x in x_range:
        for y in y_range:
            for z in z_range:
                index_x = x - x_range[0]
                index_y = y - y_range[0]
                index_z = z - z_range[0]
                mc.setBlock(x, y, z, data[index_x][index_y][index_z])
    return data


dx, dy, dz = 6, 14, 6
start = time.time()
cube_data = asyncio.run(get_cube(x - int(dx / 2), y - int(dy / 2), z - int(dz / 2), dx, dy, dz))
time_process = time.time() - start
print("time in process get_cube: ", time_process)
start = time.time()
build_cube(x - int(dx / 2), y - int(dy / 2) + 30, z - int(dz / 2), dx, dy, dz, cube_data)
time_process = time.time() - start
print("time in process build_cube: ", time_process)

# print(get_cube(x, y, z, 4, -7, 4))
