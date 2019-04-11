from __future__ import print_function
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np
import block
from mcpi.minecraft import Minecraft


mc = Minecraft.create()
start_x = start_y = start_z = end_x = end_y = end_z = 0


def char_to_pixels(text, path='res/font.ttf', fontsize=20):
    font = ImageFont.truetype(path, fontsize)
    w, h = font.getsize(text)
    h *= 2
    image = Image.new('L', (w, h), 1)
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, font=font)
    arr = np.asarray(image)
    arr = np.where(arr, 0, 1)
    arr = arr[(arr != 0).any(axis=1)]
    return arr


def print_text(pos_x, pos_y, pos_z, text, fontsize=20):
    global start_x, start_y, start_z, end_x, end_y, end_z
    mc.setBlocks(start_x, start_y, start_z, end_x, end_y, end_z, 0)
    arr = char_to_pixels(text, fontsize=fontsize)
    mc.setBlocks(pos_x, pos_y, pos_z, pos_x + len(arr[0]), pos_y + len(arr) + 1, pos_z, block.WOOL)
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if arr[y][x] == 1:
                mc.setBlock(pos_x + len(arr[y]) - x, pos_y + len(arr) - y, pos_z, arr[y][x])
    start_x, start_y, start_z, end_x, end_y, end_z = (pos_x, pos_y, pos_z, pos_x + len(arr[0]), pos_y + len(arr) + 1, pos_z)
