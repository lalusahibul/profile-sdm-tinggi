from rembg import remove
from PIL import Image, ImageDraw, ImageEnhance

def profile_sdm_tinggi(input_path,output_path,bg_color='red',bar_color='black',eye_y_ratio=500,bar_height_ratio=0.02,bar_width_ratio=0.2,offset=10,slope_deg=0,contrast=1.0):

    open_img = Image.open(input_path)
    rem = remove(open_img)
    grayscale_img = rem.convert('L')
    enhancer = ImageEnhance.Contrast(grayscale_img)
    grayscale_img = enhancer.enhance(contrast)
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
    bar_layer = Image.new('RGBA',(width, height),(0, 0, 0, 0))
    draw = ImageDraw.Draw(bar_layer)
    eye_y = int(height * eye_y_ratio)
    bar_height = int(height * bar_height_ratio)
    bar_width = int(width * bar_width_ratio)
    start = (width - bar_width) // 2 + offset
    end = start + bar_width

    draw.rectangle([start,eye_y - bar_height // 2, end, eye_y + bar_height // 2], fill=bar_color)
    rotated_bar = bar_layer.rotate(slope_deg, resample=Image.Resampling.BICUBIC, center=(width // 2, eye_y))
    bg = Image.alpha_composite(bg.convert("RGBA"), rotated_bar)
    bg.save(output_path)
profile_sdm_tinggi('input.jpg', 'output.png', 'red', "#4102D3", 0.320, 0.07, 0.4, 0, -3, 1.5)
#profile_sdm_tinggi(1.input.jpg,2.output.png,3.bg_color',4.bar_color,5.eye_position,6.bar_height,7.bar_width,8.offset,9.slope,10.contrast):