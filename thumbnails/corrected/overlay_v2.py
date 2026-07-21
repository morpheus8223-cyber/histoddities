import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT_PATH = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

def _line_width(draw, line, font, stroke_width, tracking):
    w = 0
    for ch in line:
        bbox = draw.textbbox((0, 0), ch, font=font, stroke_width=stroke_width)
        w += (bbox[2] - bbox[0]) + tracking
    return w - tracking if line else 0

def _draw_tracked(draw, xy, line, font, fill, stroke_width, stroke_fill, tracking):
    x, y = xy
    for ch in line:
        draw.text((x, y), ch, font=font, fill=fill, stroke_width=stroke_width, stroke_fill=stroke_fill)
        bbox = draw.textbbox((0, 0), ch, font=font, stroke_width=stroke_width)
        x += (bbox[2] - bbox[0]) + tracking

def draw_thumb_text(bg_path, out_path, lines, font_size=130, fill="#FFFFFF",
                     stroke_width=4, stroke_fill="#000000", shadow_offset=(3, 5), shadow_blur=4,
                     line_spacing=10, margin_x=44, anchor_y="top", top_pad=36, bottom_pad=40,
                     max_width_frac=0.60, tracking=2, align="left"):
    img = Image.open(bg_path).convert("RGB")
    W, H = img.size
    draw_measure = ImageDraw.Draw(img)
    max_w = W * max_width_frac

    while font_size > 24:
        font = ImageFont.truetype(FONT_PATH, font_size)
        widest = max(_line_width(draw_measure, l, font, stroke_width, tracking) for l in lines)
        if widest <= max_w:
            break
        font_size -= 4

    sizes = []
    for line in lines:
        w = _line_width(draw_measure, line, font, stroke_width, tracking)
        bbox = draw_measure.textbbox((0, 0), "Ag", font=font, stroke_width=stroke_width)
        h = bbox[3] - bbox[1]
        sizes.append((w, h))
    total_h = sum(h for _, h in sizes) + line_spacing * (len(lines) - 1)

    if anchor_y == "top":
        y = top_pad
    elif anchor_y == "bottom":
        y = H - bottom_pad - total_h
    else:
        y = (H - total_h) // 2

    shadow_layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow_layer)
    text_layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    td = ImageDraw.Draw(text_layer)

    cy = y
    for line, (w, h) in zip(lines, sizes):
        x = margin_x if align == "left" else W - margin_x - w
        _draw_tracked(sd, (x + shadow_offset[0], cy + shadow_offset[1]), line, font,
                      (0, 0, 0, 150), stroke_width, (0, 0, 0, 150), tracking)
        _draw_tracked(td, (x, cy), line, font, fill, stroke_width, stroke_fill, tracking)
        cy += h + line_spacing

    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(shadow_blur))

    out = img.convert("RGBA")
    out.alpha_composite(shadow_layer)
    out.alpha_composite(text_layer)
    out.convert("RGB").save(out_path, quality=95)
    print("wrote", out_path)

if __name__ == "__main__":
    bg, out = sys.argv[1], sys.argv[2]
    lines = sys.argv[3:]
    draw_thumb_text(bg, out, lines)
