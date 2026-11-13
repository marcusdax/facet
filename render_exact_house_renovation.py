import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

base_path = r'C:\Users\test 123\.gemini\antigravity\brain\89988694-c086-4aed-895f-e958b4cd5c24\house_base_hd.png'
base = Image.open(base_path).convert('RGB')
w, h = base.size
base_arr = np.array(base, dtype=np.float32)

# Foliage detection: keep foreground trees and shrubs in front
is_foliage = (base_arr[:, :, 1] > base_arr[:, :, 0] * 0.96) & (base_arr[:, :, 1] > base_arr[:, :, 2] * 1.08) & (base_arr[:, :, 1] > 55)
foliage_img = Image.fromarray((is_foliage * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.0))
foliage_alpha = np.array(foliage_img, dtype=np.float32) / 255.0

def generate_style(style='two-tone'):
    img = base.copy()
    
    # --- 1. FACADE MASONRY / LIMEWASH / SIDING ---
    facade_mask = Image.new('L', (w, h), 0)
    fdraw = ImageDraw.Draw(facade_mask)
    fdraw.polygon([(385, 138), (55, 290), (55, 515), (565, 485), (565, 295)], fill=255)
    fdraw.polygon([(750, 318), (1015, 335), (1015, 465), (750, 465)], fill=255)
    # Exclude openings
    fdraw.rectangle([284, 264, 488, 462], fill=0) # window bank
    fdraw.rectangle([808, 342, 982, 462], fill=0) # garage door
    fdraw.rectangle([565, 315, 720, 465], fill=0) # porch entry
    
    facade_np = np.array(facade_mask, dtype=np.float32) * (1.0 - foliage_alpha * 0.95)
    
    curr_arr = base_arr.copy()
    if style in ['two-tone', 'farmhouse']:
        target_color = np.array([238, 234, 226], dtype=np.float32) # warm alabaster limewash
        blend_factor = 0.74 * (facade_np[:, :, None] / 255.0)
        curr_arr = curr_arr * (1.0 - blend_factor) + (curr_arr * 0.28 + target_color * 0.72) * blend_factor
    elif style == 'cedar':
        target_color = np.array([242, 238, 228], dtype=np.float32) # Texas limestone cream
        blend_factor = 0.72 * (facade_np[:, :, None] / 255.0)
        curr_arr = curr_arr * (1.0 - blend_factor) + (curr_arr * 0.28 + target_color * 0.72) * blend_factor
    elif style == 'nordic':
        target_color = np.array([42, 45, 50], dtype=np.float32) # midnight architectural brick
        blend_factor = 0.78 * (facade_np[:, :, None] / 255.0)
        curr_arr = curr_arr * (1.0 - blend_factor) + (curr_arr * 0.22 + target_color * 0.78) * blend_factor
    elif style == 'slate':
        target_color = np.array([82, 98, 114], dtype=np.float32) # coastal slate gray
        blend_factor = 0.78 * (facade_np[:, :, None] / 255.0)
        curr_arr = curr_arr * (1.0 - blend_factor) + (curr_arr * 0.22 + target_color * 0.78) * blend_factor
    
    img = Image.fromarray(np.clip(curr_arr, 0, 255).astype(np.uint8))
    
    # --- 2. GABLE ACCENT (Cedar Slats, Ebony Slats, Board & Batten) ---
    y_cut = 270 if style != 'cedar' else 315
    g_mask = Image.new('L', (w, h), 0)
    gmdraw = ImageDraw.Draw(g_mask)
    gmdraw.polygon([(385, 142), (72, y_cut), (542, y_cut)], fill=255)
    if style == 'cedar':
        gmdraw.rectangle([284, 264, 488, 462], fill=0) # keep window opening clear
    
    g_mask_np = np.array(g_mask, dtype=np.float32) * (1.0 - foliage_alpha * 0.95)
    g_mask = Image.fromarray(g_mask_np.astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.0))
    
    accent_layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    adraw = ImageDraw.Draw(accent_layer)
    
    if style in ['two-tone', 'cedar']:
        plank_h = 7
        for py in range(138, y_cut + 5, plank_h):
            shade = (205, 122, 58) if (py // plank_h) % 2 == 0 else (192, 114, 52)
            adraw.rectangle([60, py, 550, py + plank_h - 1], fill=shade + (255,))
            adraw.line([(60, py + plank_h - 1), (550, py + plank_h - 1)], fill=(70, 38, 14, 255), width=1)
            adraw.line([(60, py), (550, py)], fill=(225, 142, 75, 140), width=1)
    elif style == 'nordic':
        slat_w = 6
        for px in range(70, 545, slat_w):
            c_base = (38, 40, 45) if (px // slat_w) % 2 == 0 else (30, 32, 36)
            adraw.rectangle([px, 138, px + slat_w - 1, y_cut], fill=c_base + (255,))
            adraw.line([(px, 138), (px, y_cut)], fill=(16, 17, 20, 255), width=1)
    elif style == 'farmhouse':
        batten_w = 14
        for px in range(70, 545, batten_w):
            adraw.rectangle([px, 138, px + batten_w - 1, y_cut], fill=(245, 245, 242, 255))
            adraw.rectangle([px + 5, 138, px + 8, y_cut], fill=(235, 235, 230, 255))
            adraw.line([(px + 8, 138), (px + 8, y_cut)], fill=(185, 185, 180, 200), width=1)
    elif style == 'slate':
        plank_h = 8
        for py in range(138, y_cut + 5, plank_h):
            shade = (76, 92, 108) if (py // plank_h) % 2 == 0 else (68, 84, 98)
            adraw.rectangle([60, py, 550, py + plank_h - 1], fill=shade + (255,))
            adraw.line([(60, py + plank_h - 1), (550, py + plank_h - 1)], fill=(45, 55, 65, 255), width=1)
    
    adraw.rectangle([68, y_cut - 2, 546, y_cut + 4], fill=(22, 24, 28, 255))
    img.paste(accent_layer, (0, 0), g_mask)
    
    # --- 3. MODERN BLACK CASEMENT WINDOWS ---
    win_layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    wdraw = ImageDraw.Draw(win_layer)
    wdraw.rectangle([286, 266, 486, 460], fill=(20, 22, 25, 255)) # outer black frame
    
    # Opaque reflective glass
    wdraw.rectangle([292, 306, 348, 454], fill=(26, 36, 48, 255))
    wdraw.rectangle([354, 272, 420, 454], fill=(24, 34, 46, 255))
    wdraw.rectangle([426, 306, 480, 454], fill=(26, 36, 48, 255))
    
    for y in range(272, 454):
        prog = (y - 272) / 182.0
        r = int(50 - prog * 24)
        g = int(72 - prog * 32)
        b = int(102 - prog * 45)
        if y >= 306:
            wdraw.line([(292, y), (348, y)], fill=(r, g, b, 255))
            wdraw.line([(426, y), (480, y)], fill=(r, g, b, 255))
        wdraw.line([(354, y), (420, y)], fill=(r, g, b, 255))
    
    # Subtle daylight reflection streaks
    for i in range(16):
        wdraw.line([(324 + i, 308), (298 + i, 452)], fill=(255, 255, 255, 40), width=1)
        wdraw.line([(392 + i, 276), (364 + i, 452)], fill=(255, 255, 255, 40), width=1)
        wdraw.line([(460 + i, 308), (432 + i, 452)], fill=(255, 255, 255, 40), width=1)
    
    # Black horizontal transom mullions
    wdraw.line([(292, 342), (348, 342)], fill=(16, 18, 20, 255), width=4)
    wdraw.line([(354, 332), (420, 332)], fill=(16, 18, 20, 255), width=4)
    wdraw.line([(426, 342), (480, 342)], fill=(16, 18, 20, 255), width=4)
    
    # Modern black sill
    wdraw.rectangle([282, 456, 490, 464], fill=(12, 14, 16, 255))
    wdraw.line([(282, 456), (490, 456)], fill=(50, 55, 60, 255), width=1)
    
    img.paste(win_layer, (0, 0), win_layer)
    
    # --- 4. MODERN ARCHITECTURAL GARAGE DOOR ---
    gar_layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(gar_layer)
    gdraw.rectangle([812, 346, 978, 458], fill=(20, 22, 25, 255))
    
    if style in ['two-tone', 'slate', 'nordic']:
        for row in range(4):
            py = 350 + row * 27
            for col in range(4):
                px = 816 + col * 40
                pw, ph = 37, 24
                tint = (192, 208, 218) if style != 'nordic' else (140, 150, 160)
                gdraw.rectangle([px, py, px + pw, py + ph], fill=tint + (255,))
                gdraw.line([(px + 1, py + 1), (px + pw - 1, py + 1)], fill=(245, 250, 255, 190), width=1)
                gdraw.line([(px + 8, py + 2), (px + 14, py + ph - 2)], fill=(255, 255, 255, 55), width=2)
    elif style == 'cedar':
        for row in range(14):
            py = 348 + row * 8
            shade = (195, 118, 55) if row % 2 == 0 else (182, 110, 50)
            gdraw.rectangle([816, py, 974, py + 6], fill=shade + (255,))
            gdraw.line([(816, py + 6), (974, py + 6)], fill=(55, 30, 12, 255), width=2)
        gdraw.rectangle([890, 395, 894, 415], fill=(20, 22, 24, 255))
        gdraw.rectangle([900, 395, 904, 415], fill=(20, 22, 24, 255))
    elif style == 'farmhouse':
        gdraw.rectangle([816, 350, 974, 454], fill=(245, 245, 242, 255))
        for col in range(4):
            px = 820 + col * 38
            gdraw.rectangle([px, 354, px + 34, 376], fill=(42, 54, 68, 255))
        gdraw.rectangle([816, 385, 845, 391], fill=(20, 22, 24, 255))
        gdraw.rectangle([945, 385, 974, 391], fill=(20, 22, 24, 255))
        gdraw.rectangle([816, 440, 845, 446], fill=(20, 22, 24, 255))
        gdraw.rectangle([945, 440, 974, 446], fill=(20, 22, 24, 255))
    
    gdraw.rectangle([810, 456, 980, 460], fill=(12, 14, 16, 255))
    img.paste(gar_layer, (0, 0), gar_layer)
    
    # --- 5. MODERN ENTRY POST & SCONCE ---
    porch_layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    pdraw = ImageDraw.Draw(porch_layer)
    pdraw.rectangle([642, 325, 656, 460], fill=(195, 118, 55, 255))
    pdraw.line([(642, 325), (642, 460)], fill=(225, 145, 80, 255), width=2)
    pdraw.line([(656, 325), (656, 460)], fill=(135, 75, 32, 255), width=2)
    pdraw.rectangle([640, 448, 658, 462], fill=(20, 22, 26, 255))
    
    pdraw.rectangle([734, 360, 742, 378], fill=(18, 20, 22, 255))
    pdraw.polygon([(734, 378), (722, 415), (754, 415), (742, 378)], fill=(255, 215, 130, 85))
    img.paste(porch_layer, (0, 0), porch_layer)
    
    # --- 6. STANDING SEAM CHARCOAL METAL ROOF ---
    roof_mask = Image.new('L', (w, h), 0)
    rmdraw = ImageDraw.Draw(roof_mask)
    rmdraw.polygon([(385, 124), (34, 275), (55, 298), (385, 146), (565, 305), (565, 280)], fill=255)
    rmdraw.polygon([(385, 124), (575, 175), (760, 245), (1032, 325), (1032, 345), (790, 328), (560, 305)], fill=255)
    rmdraw.polygon([(760, 245), (1032, 325), (790, 328)], fill=255)
    
    is_sky = (base_arr[:, :, 2] > base_arr[:, :, 0] * 1.15) & (base_arr[:, :, 2] > 145) & (np.arange(h)[:, None] < 310)
    roof_mask_np = np.array(roof_mask, dtype=np.float32)
    roof_mask_np[is_sky] = 0
    roof_mask_np[foliage_alpha > 0.6] = 0
    roof_mask = Image.fromarray(roof_mask_np.astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))
    
    roof_layer = Image.new('RGBA', (w, h), (36, 40, 46, 242) if style != 'nordic' else (22, 24, 28, 248))
    rodraw = ImageDraw.Draw(roof_layer)
    for x in range(30, 1030, 14):
        rodraw.line([(x, 120), (x - 22, 350)], fill=(78, 85, 96, 170), width=1)
        rodraw.line([(x + 1, 120), (x - 21, 350)], fill=(18, 20, 24, 210), width=1)
    rodraw.line([(34, 275), (385, 124), (565, 280)], fill=(18, 20, 24, 255), width=4)
    rodraw.line([(565, 305), (790, 328), (1032, 345)], fill=(18, 20, 24, 255), width=4)
    
    roof_composite = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    roof_composite.paste(roof_layer, (0, 0), roof_mask)
    img = Image.alpha_composite(img.convert('RGBA'), roof_composite).convert('RGB')
    
    return img

brain_dir = r'C:\Users\test 123\.gemini\antigravity\brain\89988694-c086-4aed-895f-e958b4cd5c24'
styles = ['two-tone', 'cedar', 'nordic', 'farmhouse', 'slate']

for s in styles:
    out = generate_style(s)
    fname = f'exact_house_after_{s}.jpg'
    fpath = os.path.join(brain_dir, fname)
    out.save(fpath, quality=95)
    print(f'Rendered {s} on exact house -> {fname}')

print('All 5 styles generated with 1:1 pixel alignment!')
