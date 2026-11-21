#!/usr/bin/env python3
"""Draw VELMORA — a travel poster for a place that does not exist.

Renders entry.png (1024x1024) for make.fun bounty
the-poster-for-a-place-that-i-2-20261121-0539.

Deterministic (fixed seed, no network, Pillow only). Run once:
    python3 draw.py
then main.py copies entry.png to /output/entry.png at grade time.
"""
import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1024, 1024
OUT = Path(__file__).with_name("entry.png")
FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
RNG = random.Random(20261121)

# Palette: deep indigo night, violet dusk, teal aurora sea, amber light.
INDIGO = (11, 16, 53)
VIOLET = (59, 42, 107)
TEAL_DUSK = (23, 84, 96)
TEAL = (31, 138, 138)
AURORA_GREEN = (124, 255, 178)
AURORA_TEAL = (64, 224, 208)
AURORA_VIOLET = (167, 139, 250)
AMBER = (255, 179, 71)
GOLD = (232, 200, 122)
CREAM = (255, 243, 214)
SEA_DEEP = (8, 28, 52)
SEA_GLOW = (24, 90, 104)
ROCK = (13, 20, 38)
ROCK_EDGE = (30, 46, 78)


def font(name, size):
    cand = FONT_DIR / name
    if cand.exists():
        return ImageFont.truetype(str(cand), size)
    return ImageFont.load_default()


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)  # noqa: E731
SANS = lambda s: font("DejaVuSans.ttf", s)  # noqa: E731


def vgrad(img, top, mid, bottom, y0=0, y1=H):
    """Vertical gradient, top -> mid -> bottom, over rows y0..y1."""
    d = ImageDraw.Draw(img)
    span = max(1, y1 - y0)
    for y in range(y0, y1):
        t = (y - y0) / span
        if t < 0.5:
            a, b, f = top, mid, t / 0.5
        else:
            a, b, f = mid, bottom, (t - 0.5) / 0.5
        d.line([(0, y), (W, y)], fill=tuple(int(a[i] + (b[i] - a[i]) * f) for i in range(3)))


def glow_layer(draw_fn, blur):
    """Draw onto a transparent overlay, blur it, return the overlay."""
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw_fn(ImageDraw.Draw(ov))
    return ov.filter(ImageFilter.GaussianBlur(blur))


def letter_spaced(draw, cx, y, text, fnt, fill, tracking=6):
    """Draw centered caps with manual tracking."""
    widths = [draw.textlength(ch, font=fnt) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x = cx - total / 2
    for ch, w in zip(text, widths):
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += w + tracking


def main():
    img = Image.new("RGB", (W, H), INDIGO)
    d = ImageDraw.Draw(img)

    # ---- sky: indigo -> violet -> teal dusk, down to the horizon ----
    HORIZON = 560
    vgrad(img, INDIGO, VIOLET, TEAL_DUSK, 0, HORIZON)

    # ---- stars (on an overlay, to carry alpha) ----
    stars = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(stars)
    for _ in range(260):
        x = RNG.uniform(0, W)
        y = RNG.uniform(0, 470)
        r = RNG.choice([1, 1, 1, 2, 2, 3])
        a = RNG.randint(90, 235)
        sd.ellipse([x - r, y - r, x + r, y + r], fill=(255, 250, 230, a))
    for _ in range(14):  # bright stars with a sparkle cross
        x = RNG.uniform(30, W - 30)
        y = RNG.uniform(30, 400)
        L = RNG.randint(7, 13)
        sd.line([(x - L, y), (x + L, y)], fill=(255, 250, 230, 200), width=1)
        sd.line([(x, y - L), (x, y + L)], fill=(255, 250, 230, 200), width=1)
        sd.ellipse([x - 2, y - 2, x + 2, y + 2], fill=(255, 250, 230, 230))
    img = Image.alpha_composite(img.convert("RGBA"), stars)

    # ---- aurora ribbons: translucent sine bands, blurred soft ----
    def aurora(draw):
        for (base_y, amp, col, alpha, thick) in [
            (150, 46, AURORA_GREEN, 115, 72),
            (215, 60, AURORA_TEAL, 100, 92),
            (285, 40, AURORA_VIOLET, 90, 62),
            (120, 30, AURORA_GREEN, 70, 40),
        ]:
            pts = []
            for x in range(-40, W + 41, 20):
                y = base_y + amp * math.sin(x / 170.0 + base_y)
                pts.append((x, y))
            upper = [(x, y - thick / 2) for x, y in pts]
            lower = [(x, y + thick / 2) for x, y in reversed(pts)]
            draw.polygon(upper + lower, fill=col + (alpha,))
    img = Image.alpha_composite(img, glow_layer(aurora, 13))
    d = ImageDraw.Draw(img)

    # ---- horizon glow ----
    def horizon_glow(draw):
        draw.rectangle([0, HORIZON - 26, W, HORIZON + 26], fill=(120, 220, 200, 60))
    img = Image.alpha_composite(img, glow_layer(horizon_glow, 18))
    d = ImageDraw.Draw(img)

    # ---- sea: deep gradient + reflected shimmer ----
    vgrad(img, SEA_GLOW, SEA_DEEP, (6, 18, 40), HORIZON, H)
    d = ImageDraw.Draw(img)
    # soft teal lift just below the horizon so the upper sea is not flat black
    def sea_lift(draw):
        draw.rectangle([0, HORIZON, W, HORIZON + 90], fill=(60, 170, 165, 46))
    img = Image.alpha_composite(img, glow_layer(sea_lift, 20))
    d = ImageDraw.Draw(img)
    # horizon line of light
    d.line([(0, HORIZON), (W, HORIZON)], fill=(150, 230, 210), width=2)
    # reflection streaks under the lighthouse (drawn after the tower below)
    for _ in range(46):
        x = RNG.uniform(60, W - 60)
        y = RNG.uniform(HORIZON + 14, H - 60)
        ln = RNG.uniform(14, 70)
        a = RNG.randint(24, 90)
        col = RNG.choice([(124, 255, 178), (64, 224, 208), (255, 179, 71)])
        d.line([(x, y), (x + ln, y)], fill=col, width=2)
        _ = a  # keep the palette calm; streaks stay subtle

    # ---- lighthouse islet ----
    LX = 700  # lighthouse centre x (kept clear of the title block)
    # rocky islet
    d.polygon(
        [(LX - 150, HORIZON + 6), (LX - 96, HORIZON - 26), (LX - 30, HORIZON - 38),
         (LX + 44, HORIZON - 34), (LX + 118, HORIZON - 18), (LX + 158, HORIZON + 6)],
        fill=ROCK,
    )
    d.line([(LX - 96, HORIZON - 26), (LX - 30, HORIZON - 38), (LX + 44, HORIZON - 34),
            (LX + 118, HORIZON - 18)], fill=ROCK_EDGE, width=2)

    # ---- the crystal lighthouse: ONE landmark ----
    TOP, BASE = 330, HORIZON - 30
    W_TOP, W_BASE = 44, 76
    # tower facets: light face left, deep face right
    d.polygon([(LX - W_TOP // 2, TOP), (LX + W_TOP // 2, TOP),
               (LX + W_BASE // 2, BASE), (LX - W_BASE // 2, BASE)],
              fill=(214, 240, 244))
    d.polygon([(LX, TOP), (LX + W_TOP // 2, TOP),
               (LX + W_BASE // 2, BASE), (LX, BASE)],
              fill=(140, 190, 208))
    d.polygon([(LX - W_TOP // 2, TOP), (LX, TOP), (LX, BASE), (LX - W_BASE // 2, BASE)],
              fill=(232, 248, 250))
    # facet seams
    for frac in (0.28, 0.52, 0.76):
        y = TOP + (BASE - TOP) * frac
        half = (W_TOP + (W_BASE - W_TOP) * frac) // 2
        d.line([(LX - half, y), (LX + half, y)], fill=(120, 170, 190), width=2)
    # warm windows down the tower
    for i, frac in enumerate((0.18, 0.36, 0.54, 0.72, 0.88)):
        y = TOP + (BASE - TOP) * frac
        half = (W_TOP + (W_BASE - W_TOP) * frac) // 2
        ww = 9 if i % 2 == 0 else 7
        d.rectangle([LX - ww // 2, y - 6, LX + ww // 2, y + 6], fill=AMBER)
    # lamp room + dome
    d.rectangle([LX - 34, TOP - 34, LX + 34, TOP - 2], fill=(30, 52, 92))
    d.rectangle([LX - 26, TOP - 28, LX + 26, TOP - 8], fill=AMBER)
    d.ellipse([LX - 30, TOP - 52, LX + 30, TOP - 26], fill=(214, 240, 244))
    d.rectangle([LX - 4, TOP - 62, LX + 4, TOP - 50], fill=(232, 248, 250))

    # lamp glow + sweeping beam (over the sea, to the left)
    def beam(draw):
        draw.polygon([(LX - 20, TOP - 20), (LX - 20, TOP - 8),
                      (60, HORIZON + 100), (60, HORIZON + 240)], fill=(255, 210, 120, 85))
        draw.ellipse([LX - 90, TOP - 90, LX + 90, TOP + 30], fill=(255, 200, 110, 130))
    img = Image.alpha_composite(img, glow_layer(beam, 22))
    d = ImageDraw.Draw(img)

    # ---- reflection of the lamp on the water ----
    def lamp_reflection(draw):
        for i in range(9):
            y = HORIZON + 18 + i * 26
            w = 60 - i * 4
            draw.line([(LX - w // 2, y), (LX + w // 2, y)], fill=(255, 179, 71, 170 - i * 12), width=5)
    img = Image.alpha_composite(img, glow_layer(lamp_reflection, 6))
    d = ImageDraw.Draw(img)

    # ---- rowboat with a lantern (scale + the promise of a stay) ----
    BX, BY = 190, 800
    d.polygon([(BX - 70, BY), (BX + 70, BY), (BX + 50, BY + 24), (BX - 50, BY + 24)],
              fill=(10, 16, 34))
    d.line([(BX - 70, BY), (BX + 70, BY)], fill=(60, 90, 130), width=2)
    # rower silhouette
    d.ellipse([BX + 8, BY - 34, BX + 24, BY - 18], fill=(10, 16, 34))
    d.polygon([(BX - 4, BY - 2), (BX + 34, BY - 2), (BX + 26, BY - 22), (BX + 6, BY - 22)],
              fill=(10, 16, 34))
    # oar
    d.line([(BX + 32, BY - 8), (BX + 82, BY + 20)], fill=(40, 60, 92), width=3)
    # lantern glow
    def lantern(draw):
        draw.ellipse([BX - 58 - 16, BY - 28 - 16, BX - 58 + 16, BY - 28 + 16],
                     fill=(255, 190, 90, 170))
    img = Image.alpha_composite(img, glow_layer(lantern, 12))
    d = ImageDraw.Draw(img)
    d.rectangle([BX - 64, BY - 34, BX - 52, BY - 22], fill=AMBER)
    d.line([(BX - 58, BY - 22), (BX - 58, BY - 10)], fill=(40, 60, 92), width=2)
    # boat reflection
    d.line([(BX - 54, BY + 34), (BX + 54, BY + 34)], fill=(255, 179, 71), width=2)
    d.line([(BX - 40, BY + 52), (BX + 40, BY + 52)], fill=(120, 200, 190), width=2)

    # ---- foreground shore: dark rock + glowing tide pools ----
    d.polygon([(0, H), (0, 930), (120, 902), (260, 928), (330, 968), (300, H)],
              fill=ROCK)
    d.polygon([(W, H), (W, 946), (920, 916), (800, 944), (740, 978), (780, H)],
              fill=ROCK)
    for (x, y, r) in [(70, 952, 5), (120, 968, 4), (180, 946, 3),
                      (880, 962, 5), (940, 950, 4), (830, 972, 3)]:
        d.ellipse([x - r, y - r, x + r, y + r], fill=(64, 224, 208))

    # ---- type: the name carries the poster ----
    # soft shadow behind the title so it reads over the aurora
    title = "VELMORA"
    tf = SERIF_B(128)
    tw = d.textlength(title, font=tf)
    tx, ty = (W - tw) / 2, 56
    d.text((tx + 3, ty + 4), title, font=tf, fill=(6, 10, 34))
    d.text((tx, ty), title, font=tf, fill=CREAM)
    # gold rule under the title
    d.line([(W / 2 - 130, 208), (W / 2 + 130, 208)], fill=GOLD, width=3)
    # descriptor, letterspaced
    letter_spaced(d, W / 2, 226, "THE CITY BENEATH THE AURORA SEA",
                  SANS(27), GOLD, tracking=5)

    img.convert("RGB").save(OUT, format="PNG", optimize=True)
    print("wrote", OUT, OUT.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
