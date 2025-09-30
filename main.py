from moviepy.editor import VideoFileClip
from PIL import Image
import math

# Minecraft block colors (wool, terracotta, concrete)
minecraft_colors = {
    # Wool
    "white_wool": (234, 236, 237),
    "orange_wool": (243, 140, 54),
    "magenta_wool": (190, 68, 201),
    "light_blue_wool": (58, 179, 218),
    "yellow_wool": (248, 198, 39),
    "lime_wool": (128, 199, 31),
    "pink_wool": (242, 142, 165),
    "gray_wool": (54, 57, 61),
    "light_gray_wool": (157, 161, 162),
    "cyan_wool": (22, 174, 174),
    "purple_wool": (126, 42, 184),
    "blue_wool": (60, 68, 170),
    "brown_wool": (111, 71, 40),
    "green_wool": (85, 110, 27),
    "red_wool": (161, 39, 34),
    "black_wool": (20, 21, 25),

    # Terracotta
    "white_terracotta": (209, 178, 161),
    "orange_terracotta": (160, 97, 42),
    "magenta_terracotta": (123, 47, 123),
    "light_blue_terracotta": (73, 91, 133),
    "yellow_terracotta": (179, 145, 71),
    "lime_terracotta": (94, 125, 42),
    "pink_terracotta": (214, 123, 123),
    "gray_terracotta": (55, 41, 36),
    "light_gray_terracotta": (141, 114, 97),
    "cyan_terracotta": (46, 89, 116),
    "purple_terracotta": (102, 44, 95),
    "blue_terracotta": (53, 57, 157),
    "brown_terracotta": (89, 61, 35),
    "green_terracotta": (73, 91, 36),
    "red_terracotta": (143, 32, 32),
    "black_terracotta": (24, 23, 23),

    # Concrete
    "white_concrete": (207, 213, 214),
    "orange_concrete": (224, 97, 0),
    "magenta_concrete": (169, 48, 159),
    "light_blue_concrete": (36, 137, 199),
    "yellow_concrete": (249, 199, 35),
    "lime_concrete": (94, 168, 24),
    "pink_concrete": (214, 101, 143),
    "gray_concrete": (54, 57, 61),
    "light_gray_concrete": (154, 161, 161),
    "cyan_concrete": (21, 137, 145),
    "purple_concrete": (121, 42, 172),
    "blue_concrete": (53, 57, 157),
    "brown_concrete": (114, 71, 40),
    "green_concrete": (84, 109, 27),
    "red_concrete": (161, 39, 34),
    "black_concrete": (21, 21, 26),
}

def closest_block(rgb):
    r, g, b = rgb
    return min(minecraft_colors.keys(), key=lambda block: math.sqrt(
        (minecraft_colors[block][0]-r)**2 +
        (minecraft_colors[block][1]-g)**2 +
        (minecraft_colors[block][2]-b)**2))

# --- User input ---
video_path = "your_movie.mp4"

# Wand-selected TV area coordinates
x_start = int(input("Enter X start: "))
y_start = int(input("Enter Y start: "))
z_start = int(input("Enter Z start: "))
x_end = int(input("Enter X end: "))
y_end = int(input("Enter Y end: "))
z_end = int(input("Enter Z end: "))

# Compute width & height based on wand
tv_width = abs(x_end - x_start) + 1
tv_height = abs(y_end - y_start) + 1

output_file = "minecraft_movie.txt"

clip = VideoFileClip(video_path)
commands = []

for i, frame in enumerate(clip.iter_frames()):
    img = Image.fromarray(frame).convert("RGB")
    img = img.resize((tv_width, tv_height))

    for y in range(tv_height):
        for x in range(tv_width):
            color = img.getpixel((x, y))
            block = closest_block(color)
            commands.append(f"/setblock {x_start + x} {y_start + (tv_height - y - 1)} {z_start} {block}")

with open(output_file, "w") as f:
    f.write("\n".join(commands))

print(f"Done! Commands saved in {output_file}")
