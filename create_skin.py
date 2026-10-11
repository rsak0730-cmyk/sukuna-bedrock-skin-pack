from PIL import Image, ImageDraw
from pathlib import Path

output = Path("pack/skins/sukuna.png")
output.parent.mkdir(parents=True, exist_ok=True)

image = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
draw = ImageDraw.Draw(image)

skin = (238, 198, 174, 255)
black = (22, 17, 25, 255)
red = (135, 18, 35, 255)
hair = (12, 12, 18, 255)
dark_red = (92, 12, 27, 255)
gold = (190, 135, 45, 255)

def box(x1, y1, x2, y2, color):
    draw.rectangle((x1, y1, x2, y2), fill=color)

# Head: Minecraft 64x64 skin layout
box(8, 0, 15, 7, hair)
box(16, 0, 23, 7, hair)

box(0, 8, 7, 15, skin)
box(8, 8, 15, 15, skin)
box(16, 8, 23, 15, skin)
box(24, 8, 31, 15, skin)

# Hairline
box(8, 8, 15, 9, hair)
box(16, 8, 23, 9, hair)
box(8, 10, 9, 10, hair)
box(22, 10, 23, 10, hair)

# Eyes
box(10, 11, 11, 11, red)
box(20, 11, 21, 11, red)

# Facial markings
box(12, 12, 13, 12, red)
box(18, 12, 19, 12, red)
box(11, 13, 12, 13, dark_red)
box(19, 13, 20, 13, dark_red)
box(14, 14, 17, 14, black)

# Torso
box(20, 20, 27, 31, black)
box(28, 20, 35, 31, black)
box(16, 20, 19, 31, black)
box(36, 20, 39, 31, black)

# Shirt and cursed-energy details
box(20, 20, 35, 21, dark_red)
box(20, 26, 35, 27, red)
box(22, 22, 23, 25, red)
box(32, 22, 33, 25, red)
box(25, 29, 30, 30, red)

# Arms
box(40, 20, 47, 31, black)
box(48, 20, 55, 31, black)
box(40, 22, 41, 25, red)
box(54, 22, 55, 25, red)
box(44, 29, 45, 30, gold)
box(50, 29, 51, 30, gold)

# Legs
box(20, 32, 27, 47, black)
box(28, 32, 35, 47, black)
box(22, 35, 23, 39, red)
box(32, 35, 33, 39, red)
box(25, 42, 26, 43, dark_red)
box(29, 42, 30, 43, dark_red)

# Shoes
box(20, 48, 27, 51, black)
box(28, 48, 35, 51, black)
box(22, 49, 23, 49, gold)
box(32, 49, 33, 49, gold)

image.save(output)
print(f"Created {output}")
