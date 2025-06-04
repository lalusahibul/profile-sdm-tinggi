from rembg import remove
from PIL import Image, ImageDraw

def profile_sdm_tinggi(input_path,output_path,bg_color='red', eye_y_ratio=0, bar_height_ratio=0, bar_width_ratio=0, offset=10, line_color='black'):

    open_img = Image.open(input_path)
    rem = remove(open_img)
    grayscale_img = rem.convert('L')
    width, height = grayscale_img.size
    bg = Image.new('RGB', (width, height), color=bg_color)

    if rem.mode == 'RGBA':
        alpha_mask = rem.split()[-1]
    else:
        alpha_mask = rem.convert('L')
    grayscale_rgba = Image.new('RGBA', grayscale_img.size)
    grayscale_rgba.paste(grayscale_img, (0, 0), mask=None)
    grayscale_rgba.putalpha(alpha_mask)
    bg.paste(grayscale_rgba, (0, 0), grayscale_rgba)

    #tambahkan garis HYTAM!!
    draw = ImageDraw.Draw(bg)
    eye_y = int(height * eye_y_ratio)
    bar_height = int(height * bar_height_ratio)
    bar_width = int(width * bar_width_ratio)
    start = (width - bar_width) // 2 + offset
    end = start + bar_width

    draw.rectangle([start,eye_y - bar_height // 2, end, eye_y + bar_height // 2], fill=line_color)
    bg.save(output_path)

profile_sdm_tinggi('input.jpg', 'output.png', 'red', 0.320, 0.07, 0.4, 0, 'black')