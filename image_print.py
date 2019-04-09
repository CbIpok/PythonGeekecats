from PIL import Image

# https://minecraft.gamepedia.com/Wool
WOOL_COLOR = {
    0: (0xFF, 0xFF, 0xFF),
    1: (0xF0, 0x76, 0x13),
    2: (0xBD, 0x44, 0xB3),
    3: (0x3A, 0xAF, 0xD9),
    4: (0xF8, 0xC6, 0x27),
    5: (0x70, 0xB9, 0x19),
    6: (0xED, 0x8D, 0xAC),
    7: (0x3E, 0x44, 0x47),
    8: (0x8E, 0x8E, 0x86),
    9: (0x15, 0x89, 0x91),
    10: (0x79, 0x2A, 0xAC),
    11: (0x35, 0x39, 0x9D),
    12: (0x72, 0x47, 0x28),
    13: (0x54, 0x6D, 0x1B),
    14: (0xA1, 0x27, 0x22),
    15: (0x00, 0x00, 0x00),
}


def load_image(path_to_file, resize_width_to):
    image = Image.open(path_to_file)
    image_resize_ratio = (resize_width_to / float(image.size[0]))  # equels (отношение) не проценты доебался до названия
    resize_height_to = int(
        (float(image.size[1]) * float(image_resize_ratio)))  # раз уж resize_width_to следовательно resize_height_to
    image = image.resize((resize_width_to, resize_height_to), Image.ANTIALIAS)
    data = image.load()
    return data, resize_height_to, resize_width_to


def color_distance(rgb1, rgb2):
    d = abs(rgb1[0] - rgb2[0]) + abs(rgb1[1] - rgb2[1]) + abs(rgb1[2] - rgb2[2])
    return d


def get_wool_id_by_rgb(rgb):
    best_id_wool = -1
    min_distance = 255 * 3  # max color distance is 255*3 (see color_distance(rgb1, rgb2))
    for wool_id, wool_color in WOOL_COLOR.items():
        distance = color_distance(rgb, wool_color)
        if min_distance > distance:
            best_id_wool = wool_id
            min_distance = distance
    return best_id_wool


def get_wool_id_texture(path_to_file, resize_width_to):
    data, h, w = load_image(path_to_file, resize_width_to)
    wool_id_texture = []
    for y in range(h):
        wool_id_texture.append([])
        for x in range(w):
            pixel = data[x, y]
            wool_id = get_wool_id_by_rgb(pixel)
            wool_id_texture[y].append(wool_id)
    return wool_id_texture
