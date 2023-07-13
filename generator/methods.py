from PIL import Image, ImageDraw, ImageFont
from django.conf import settings


def calculate_x_position(image_width, text_width, position):
    if position == 'left':
        return 0
    elif position == 'center':
        return 0
    elif position == 'right':
        return 0
    else:
        return 0

def calculate_y_position(image_height, text_height, position):
    if position == 'top':
        return 50
    elif position == 'center':
        return (image_height - text_height) // 2
    elif position == 'bottom':
        return (image_height - text_height) - 100
    else:
        return 0


def generate_meme(image_path, captions, caption_colors, caption_positions, caption_bgcolors):
    """
        1. colors
        2. captions
        3. positions: top, center, bottom
        3. set background for captions
    """
    image = Image.open(image_path)
    draw_canvas = ImageDraw.Draw(image)

    font_path = f"{settings.BASE_DIR}/static/assets/css/Arial.ttf"
    font_size = 24
    font = ImageFont.truetype(font=font_path, size=font_size)

    for caption, color, position, bg_color in zip(captions, caption_colors, caption_positions, caption_bgcolors):
        x = calculate_x_position(image.width, 15, position)
        y = calculate_y_position(image.height, 15, position)
        # Set the background color
        captions_width = len(caption)*10
        text_height = font_size+10
        draw_canvas.rectangle([(x, y), (x + captions_width + 10, y + text_height)], fill=bg_color)
        draw_canvas.text((x, y), caption, fill=color, font=font)

    return image