"""
Documentary motion-graphics compositing primitives -- the in-house devices
identified in the Pythia V2 video and the existing thumbnail brand, rebuilt
as reusable, scriptable steps instead of one-off manual edits.

Four building blocks:
  - archival_bw()      desaturate a sourced real photo to the archival look
  - circle_callout()   the yellow "look here" evidence circle on a real photo
  - definition_card()  the Vox-style term card (colored circle cutout + label)
  - ken_burns_clip()   slow zoom/pan on a still, turning it into a video clip

These are meant to be interleaved with Higgsfield-generated AI clips at the
assembly stage -- real sourced photos for anything with surviving photography
or artwork, AI generation for everything else, matching the pattern already
observed across HistOddities' own catalog and the Pythia V2 video.
"""
import shutil
import subprocess

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

def _default_ffmpeg():
    found = shutil.which("ffmpeg")
    if found:
        return found
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()

SANS_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"

BRAND_YELLOW = "#F2D336"
BRAND_RED = "#D0201E"
BRAND_WHITE = "#FFFFFF"
BRAND_INK = "#1A1A1A"


def archival_bw(image_path, out_path, contrast=1.08, warmth=0.0):
    """Desaturate a real sourced photo to match the B&W archival treatment
    used throughout Pythia V2's main body (engravings, statues, museum
    photography). warmth=0..1 tints slightly sepia instead of pure gray."""
    img = Image.open(image_path).convert("RGB")
    gray = ImageOps.grayscale(img)
    gray = ImageOps.autocontrast(gray, cutoff=1)
    if warmth > 0:
        sepia = Image.merge("RGB", [
            gray.point(lambda p: min(255, int(p * (1 + 0.15 * warmth)))),
            gray.point(lambda p: min(255, int(p * (1 + 0.05 * warmth)))),
            gray.point(lambda p: int(p * (1 - 0.10 * warmth))),
        ])
        out = sepia
    else:
        out = gray.convert("RGB")
    out.save(out_path, quality=95)
    return out_path


def circle_callout(image_path, out_path, center_frac, radius_frac=0.12,
                    color=BRAND_YELLOW, thickness_frac=0.008):
    """Draw the recurring 'evidence' callout circle at a normalized
    (x_frac, y_frac) point on a real photo. Matches the device confirmed in
    both the thumbnail audit (Palme suspect, Cleopatra's ochre bowl, Tulip
    price tag) and the Pythia V2 in-video use (Socrates' face)."""
    img = Image.open(image_path).convert("RGBA")
    W, H = img.size
    cx, cy = int(center_frac[0] * W), int(center_frac[1] * H)
    r = int(radius_frac * min(W, H))
    thickness = max(3, int(thickness_frac * min(W, H)))

    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=thickness)

    out = Image.alpha_composite(img, overlay)
    out.convert("RGB").save(out_path, quality=95)
    return out_path


def _fit_font(draw, text, font_path, max_width, start_size, min_size=18):
    size = start_size
    while size > min_size:
        font = ImageFont.truetype(font_path, size)
        bbox = draw.textbbox((0, 0), text, font=font)
        if bbox[2] - bbox[0] <= max_width:
            return font
        size -= 2
    return ImageFont.truetype(font_path, min_size)


def definition_card(portrait_path, label, subtitle, body_lines, out_path,
                     accent_color=BRAND_YELLOW, canvas_size=(1920, 1080),
                     portrait_is_bw=True, portrait_has_alpha=None):
    """The recurring Vox-style glossary card: a cutout portrait sitting on a
    solid accent-color circle, paired with a bold serif label, a bracketed
    subtitle, and a short body text block. accent_color cycles per subject
    the same way the source video alternates yellow/green per term.

    portrait_path should be a subject-only cutout with a transparent
    background (run it through Higgsfield's remove_background first if the
    source photo has a busy/plain background) -- otherwise the portrait's
    own rectangular background just covers the accent circle instead of
    letting it show around the silhouette, which is the whole point of the
    device. portrait_has_alpha auto-detects from the file when left None.
    """
    W, H = canvas_size
    canvas = Image.new("RGBA", (W, H), "#EDEBE6")
    draw = ImageDraw.Draw(canvas)

    circle_d = int(H * 0.72)
    circle_cx, circle_cy = int(W * 0.27), int(H * 0.52)
    draw.ellipse([
        circle_cx - circle_d // 2, circle_cy - circle_d // 2,
        circle_cx + circle_d // 2, circle_cy + circle_d // 2,
    ], fill=accent_color)

    portrait = Image.open(portrait_path)
    has_alpha = portrait_has_alpha if portrait_has_alpha is not None else (
        portrait.mode == "RGBA" and portrait.getchannel("A").getextrema()[0] < 255
    )
    if not has_alpha:
        portrait = portrait.convert("RGBA")
    if portrait_is_bw:
        gray = ImageOps.grayscale(portrait.convert("RGB")).convert("RGBA")
        gray.putalpha(portrait.getchannel("A") if has_alpha else Image.new("L", portrait.size, 255))
        portrait = gray

    target_h = int(H * 0.9)
    scale = target_h / portrait.height
    portrait = portrait.resize((int(portrait.width * scale), target_h))
    px = circle_cx - portrait.width // 2
    py = H - portrait.height
    canvas.alpha_composite(portrait, (px, py))

    text_x = int(W * 0.50)
    label_font = _fit_font(draw, label, SERIF_BOLD, W * 0.35, 96)
    draw.rectangle(
        [text_x - 10, int(H * 0.30), text_x + draw.textbbox((0, 0), label, font=label_font)[2] + 20,
         int(H * 0.30) + 100],
        fill=accent_color,
    )
    draw.text((text_x, int(H * 0.30) + 8), label, font=label_font, fill=BRAND_INK)

    sub_font = ImageFont.truetype(SERIF_BOLD, 40)
    draw.text((text_x, int(H * 0.30) + 115), f"[{subtitle}]", font=sub_font, fill=BRAND_INK)

    body_font = ImageFont.truetype(SANS_BOLD, 34)
    y = int(H * 0.30) + 190
    for line in body_lines:
        draw.text((text_x, y), line, font=body_font, fill=BRAND_INK)
        y += 50

    canvas.convert("RGB").save(out_path, quality=95)
    return out_path


def ken_burns_clip(image_path, out_path, duration_s=6, fps=24,
                    size=(1920, 1080), zoom_start=1.0, zoom_end=1.18,
                    pan="center", ffmpeg_bin=None):
    """Slow zoom/pan on a still via ffmpeg's zoompan filter -- the subtle
    motion seen on every real-photo shot in Pythia V2, instead of a static
    frame sitting on screen."""
    frames = int(duration_s * fps)
    zoom_step = (zoom_end - zoom_start) / frames

    pans = {
        "center": "x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'",
        "left-to-right": "x='(iw/zoom/2)*(on/{f})':y='ih/2-(ih/zoom/2)'".format(f=frames),
        "top-to-bottom": "x='iw/2-(iw/zoom/2)':y='(ih/zoom/2)*(on/{f})'".format(f=frames),
    }
    pan_expr = pans.get(pan, pans["center"])
    ffmpeg_bin = ffmpeg_bin or _default_ffmpeg()

    vf = (
        f"scale=8000:-1,zoompan=z='min(zoom+{zoom_step},{zoom_end})':"
        f"{pan_expr}:d={frames}:s={size[0]}x{size[1]}:fps={fps}"
    )
    cmd = [
        ffmpeg_bin, "-y", "-loop", "1", "-i", image_path,
        "-vf", vf, "-t", str(duration_s),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", out_path,
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    return out_path
