import os
from PIL import Image, ImageDraw, ImageFont

# Dimensioni A4 Verticale (Portrait) a 150 DPI: 1240 x 1754 px
PAGE_W = 1240
PAGE_H = 1754

output_pdf_path = r'd:\antigravity\martina_portfolio\Portfolio_Martina_Taglietti_Print_A4.pdf'
assets_dir = r'd:\antigravity\martina_portfolio\assets'

COLOR_BG = (248, 247, 244)
COLOR_DARK = (18, 19, 22)
COLOR_MUTED = (110, 114, 125)
COLOR_GOLD = (207, 178, 113)
COLOR_CORAL = (231, 97, 56)
COLOR_WHITE = (255, 255, 255)

def get_font(size, bold=False):
    try:
        font_name = "segoeuib.ttf" if bold else "segoeui.ttf"
        return ImageFont.truetype(font_name, size)
    except:
        try:
            font_name = "arialbd.ttf" if bold else "arial.ttf"
            return ImageFont.truetype(font_name, size)
        except:
            return ImageFont.load_default()

font_massive = get_font(95, bold=True)
font_title = get_font(36, bold=True)
font_heading = get_font(24, bold=True)
font_sub = get_font(18, bold=False)
font_body = get_font(15, bold=False)
font_body_bold = get_font(15, bold=True)
font_tag = get_font(13, bold=True)
font_small = get_font(11, bold=False)

def create_base_page(header_left="MARTINA TAGLIETTI", header_right="PORTFOLIO 2026", footer_page="01"):
    img = Image.new('RGB', (PAGE_W, PAGE_H), COLOR_BG)
    draw = ImageDraw.Draw(img)
    draw.text((70, 50), header_left, font=font_tag, fill=COLOR_MUTED)
    draw.text((PAGE_W - 70 - 180, 50), header_right, font=font_tag, fill=COLOR_MUTED)
    draw.line([(70, 78), (PAGE_W - 70, 78)], fill=(225, 223, 218), width=1)
    
    draw.line([(70, PAGE_H - 70), (PAGE_W - 70, PAGE_H - 70)], fill=(225, 223, 218), width=1)
    draw.text((70, PAGE_H - 55), "Graphic & Visual Designer • Bergamo / Milano", font=font_small, fill=COLOR_MUTED)
    draw.text((PAGE_W - 70 - 40, PAGE_H - 55), footer_page, font=font_tag, fill=COLOR_MUTED)
    return img, draw

def add_img_to_page(img, path, x, y, w, h, border=True):
    if not os.path.exists(path):
        return
    src = Image.open(path).convert('RGB')
    src_ratio = src.width / src.height
    box_ratio = w / h
    
    if src_ratio > box_ratio:
        new_w = w
        new_h = int(w / src_ratio)
        src_resized = src.resize((new_w, new_h), Image.Resampling.LANCZOS)
        offset_y = y + (h - new_h) // 2
        img.paste(src_resized, (x, offset_y))
    else:
        new_h = h
        new_w = int(h * src_ratio)
        src_resized = src.resize((new_w, new_h), Image.Resampling.LANCZOS)
        offset_x = x + (w - new_w) // 2
        img.paste(src_resized, (offset_x, y))
        
    draw = ImageDraw.Draw(img)
    if border:
        draw.rectangle([x, y, x + w, y + h], outline=(220, 218, 212), width=1)

pages_imgs = []

# ==================== PAGINA 1: COVER A4 ====================
p1 = Image.new('RGB', (PAGE_W, PAGE_H), COLOR_BG)
d1 = ImageDraw.Draw(p1)
d1.text((80, 100), "SELECTED WORKS & CASE STUDIES", font=font_tag, fill=COLOR_MUTED)
d1.text((PAGE_W - 80 - 150, 100), "EDITION 2025 / 2026", font=font_tag, fill=COLOR_CORAL)
d1.line([(80, 130), (PAGE_W - 80, 130)], fill=(220, 218, 212), width=1)

d1.text((80, 320), "PORTFOLIO", font=font_massive, fill=COLOR_DARK)
d1.line([(80, 440), (PAGE_W - 80, 440)], fill=COLOR_DARK, width=3)

d1.text((80, 500), "MARTINA TAGLIETTI", font=font_title, fill=COLOR_DARK)
d1.text((80, 560), "Graphic, Visual & Digital Designer • 19 Anni", font=font_heading, fill=COLOR_CORAL)

bio_summary = (
    "Portfolio professionale di Graphic Design, Brand Identity, Interfacce Web e Mobile,\n"
    "Suite Adobe, Figma e Direzione Fotografica d'Officina.\n\n"
    "Formazione presso CFP Scuola d'Arte Andrea Fantoni (Bergamo) ed esperienza\n"
    "sul campo in azienda nella grafica per abbigliamento, vettorializzazione e prestampa."
)
d1.text((80, 660), bio_summary, font=font_sub, fill=COLOR_MUTED, spacing=10)

# Featured project list
d1.rectangle([80, 940, PAGE_W - 80, 1400], fill=COLOR_WHITE, outline=(225, 223, 218), width=1)
d1.text((120, 980), "INDICE DEI PROGETTI SELEZIONATI", font=font_tag, fill=COLOR_MUTED)
d1.line([(120, 1010), (PAGE_W - 120, 1010)], fill=(235, 233, 228), width=1)

projects_index = [
    ("01", "CAMELIA — LAGO MAGGIORE", "Brand Identity, Manuale del Marchio & Packaging"),
    ("02", "FORME ESSENZIALI", "UI/UX Web & E-Commerce Artigianato (Desktop & Mobile)"),
    ("03", "SOUNDMATCH", "Mobile App UI/UX Design per Produttori Musicali"),
    ("04", "DGM MOTORI", "Studio di Rebranding & Presenza Web Autofficina"),
    ("05", "WORKSHOP ATMOSPHERE", "Set Fotografico d'Officina Meccanica sul Campo")
]

for idx, (num, p_title, p_desc) in enumerate(projects_index):
    py = 1040 + idx * 65
    d1.text((120, py), num, font=font_body_bold, fill=COLOR_CORAL)
    d1.text((170, py), p_title, font=font_body_bold, fill=COLOR_DARK)
    d1.text((170, py + 22), p_desc, font=font_small, fill=COLOR_MUTED)

d1.text((80, 1500), "CONTATTO: ifts.taglietti.martina@cfpscuolafantoni.org", font=font_body_bold, fill=COLOR_CORAL)
d1.text((80, 1530), "BERGAMO / MILANO, ITALIA", font=font_tag, fill=COLOR_MUTED)
pages_imgs.append(p1)


# ==================== PAGINA 2: CHI SONO & COMPETENZE ====================
p2, d2 = create_base_page(footer_page="02")
d2.text((70, 110), "01 / PROFILO PERSONALE & TOOLKIT", font=font_tag, fill=COLOR_CORAL)
d2.text((70, 140), "Chi Sono & Competenze", font=font_title, fill=COLOR_DARK)

about_p2 = (
    "Mi chiamo Martina Taglietti, ho 19 anni e considero la grafica un punto di convergenza\n"
    "tra rigore matematico-proporzionale ed espressione visiva.\n\n"
    "Ho studiato Graphic Design presso il CFP Scuola d'Arte Andrea Fantoni di Bergamo e ho arricchito\n"
    "la mia preparazione con un'esperienza di apprendistato presso Kapo (abbigliamento sportivo).\n"
    "In azienda mi sono occupata della creazione di grafiche, vettorializzazione loghi, prestampa\n"
    "e preparazione tecnica dei file per la pressatura a caldo su tessuti e capi finiti.\n\n"
    "Sul versante digitale realizzo prototipi completi su Figma e curo la messa online di siti e negozi\n"
    "con WordPress, Elementor e Shopify, integrando conoscenze di base HTML5 e CSS3."
)
d2.text((70, 210), about_p2, font=font_body, fill=COLOR_DARK, spacing=6)

# Skills Boxes in Portrait
skill_boxes = [
    ("ADOBE CREATIVE SUITE", ["Photoshop (Fotoritocco, Scontorni, Mockup)", "Illustrator (Vettori, Loghi, Iconografia)", "InDesign (Editoria, Brand Books, Brochure)", "Lightroom (Color Grading Fotografico)"], COLOR_CORAL),
    ("FIGMA & CANVA (UI/UX)", ["Design System, Componenti & Auto-Layout", "Prototipi Cliccabili Mobile & Desktop", "Wireframing & Architettura Informativa", "Canva per Grafiche Social & Presentazioni"], COLOR_DARK),
    ("WEB, CMS & E-COMMERCE", ["Basi di HTML5 e fogli di stile CSS3", "WordPress & Gestione Contenuti CMS", "Elementor Pro per Pagine Visive Dinamiche", "Shopify Store, Cataloghi & Configurazione Prodotti"], COLOR_GOLD),
    ("PRODUZIONE & PRESTAMPA", ["Grafica per Abbigliamento & Merchandising", "Loghi per Termopresse & Plotter da Taglio", "Controllo Colore CMYK & Prove di Stampa", "Reportage Fotografico in Loco (Sony Alpha)"], COLOR_DARK)
]

for idx, (title, items, col) in enumerate(skill_boxes):
    by = 520 + idx * 260
    d2.rectangle([70, by, PAGE_W - 70, by + 230], fill=COLOR_WHITE, outline=(220, 218, 212), width=1)
    d2.rectangle([70, by, 76, by + 230], fill=col)
    d2.text((100, by + 25), title, font=font_heading, fill=COLOR_DARK)
    for i_idx, item in enumerate(items):
        col_x = 100 if i_idx < 2 else 600
        row_y = by + 80 + (i_idx % 2) * 55
        d2.text((col_x, row_y), f"✓  {item}", font=font_body, fill=COLOR_MUTED)

pages_imgs.append(p2)


# ==================== PAGINA 3: CAMELIA ====================
p3, d3 = create_base_page(footer_page="03")
d3.text((70, 110), "CASE STUDY 01 / BRAND IDENTITY & GUIDELINES", font=font_tag, fill=COLOR_CORAL)
d3.text((70, 140), "Camelia — Lago Maggiore", font=font_title, fill=COLOR_DARK)
d3.text((70, 195), "Manuale del Marchio di 32 Pagine, Geometria Proporzionale & Immagine Coordinata", font=font_sub, fill=COLOR_MUTED)

p3_desc = (
    "Progettazione dell'identità visiva per il brand Camelia Lago Maggiore.\n"
    "Monogramma iconico 'C', costruzione geometrica aurea, palette cromatica\n"
    "(Nero Profondo, Oro Assoluto #CFB271, Bianco Origine) e declinazione coordinata su cancelleria e packaging."
)
d3.text((70, 240), p3_desc, font=font_body, fill=COLOR_DARK, spacing=6)

add_img_to_page(p3, os.path.join(assets_dir, 'camelia', 'camelia_p05.jpg'), 70, 360, 1100, 480)
d3.text((70, 855), "Logo Istituzionale e Monogramma Camelia", font=font_tag, fill=COLOR_MUTED)

add_img_to_page(p3, os.path.join(assets_dir, 'camelia', 'camelia_p18.jpg'), 70, 900, 530, 380)
d3.text((70, 1295), "Gabbia Geometrica di Costruzione", font=font_tag, fill=COLOR_MUTED)

add_img_to_page(p3, os.path.join(assets_dir, 'camelia', 'camelia_p30.jpg'), 640, 900, 530, 380)
d3.text((640, 1295), "Immagine Coordinata & Buste da Lettera", font=font_tag, fill=COLOR_MUTED)

pages_imgs.append(p3)


# ==================== PAGINA 4: FORME ESSENZIALI ====================
p4, d4 = create_base_page(footer_page="04")
d4.text((70, 110), "CASE STUDY 02 / UI/UX & E-COMMERCE DESIGN", font=font_tag, fill=COLOR_CORAL)
d4.text((70, 140), "Forme Essenziali — Collettivo Artigianato", font=font_title, fill=COLOR_DARK)
d4.text((70, 195), "Web E-Commerce Desktop (1440px) & Mobile Responsive (412px)", font=font_sub, fill=COLOR_MUTED)

p4_desc = (
    "Esperienza digitale per valorizzare il design italiano fatto a mano.\n"
    "Homepage immersiva, catalogo a griglia asimmetrica, schede maestri artigiani e carrello rapido."
)
d4.text((70, 240), p4_desc, font=font_body, fill=COLOR_DARK, spacing=6)

add_img_to_page(p4, os.path.join(assets_dir, 'forme_essenziali', 'hero_homepage.jpg'), 70, 350, 1100, 480)
d4.text((70, 845), "Interfaccia Desktop Homepage (Figma Prototype)", font=font_tag, fill=COLOR_MUTED)

add_img_to_page(p4, os.path.join(assets_dir, 'forme_essenziali', 'hero_collezione.jpg'), 70, 890, 680, 420)
d4.text((70, 1325), "Catalogo Prodotti & Filtri Materici", font=font_tag, fill=COLOR_MUTED)

add_img_to_page(p4, os.path.join(assets_dir, 'forme_essenziali', 'mobile_homepage.jpg'), 790, 890, 380, 420)
d4.text((790, 1325), "Versione Mobile Ottimizzata (412px)", font=font_tag, fill=COLOR_MUTED)

pages_imgs.append(p4)


# ==================== PAGINA 5: SOUNDMATCH & DGM ====================
p5, d5 = create_base_page(footer_page="05")
d5.text((70, 110), "CASE STUDY 03 & 04 / MOBILE APP & REBRANDING", font=font_tag, fill=COLOR_CORAL)
d5.text((70, 140), "SoundMatch App & DGM Motori", font=font_title, fill=COLOR_DARK)
d5.text((70, 195), "Applicazione Musicale Dark Mode e Studio di Rebranding Meccanico", font=font_sub, fill=COLOR_MUTED)

add_img_to_page(p5, os.path.join(assets_dir, 'soundmatch', 'soundmatch_screen_1.jpg'), 70, 260, 340, 480)
add_img_to_page(p5, os.path.join(assets_dir, 'soundmatch', 'soundmatch_screen_2.jpg'), 450, 260, 340, 480)
add_img_to_page(p5, os.path.join(assets_dir, 'soundmatch', 'soundmatch_screen_3.jpg'), 830, 260, 340, 480)
d5.text((70, 755), "SoundMatch Mobile App — Profilo, Ricerca & Vetrina Beat Musicali", font=font_tag, fill=COLOR_MUTED)

d5.line([(70, 800), (PAGE_W - 70, 800)], fill=(225, 223, 218), width=1)
d5.text((70, 825), "DGM MOTORI — REBRANDING VISIVO", font=font_heading, fill=COLOR_DARK)
add_img_to_page(p5, os.path.join(assets_dir, 'dgm', 'dgm_page_21.jpg'), 70, 870, 680, 400)
add_img_to_page(p5, os.path.join(assets_dir, 'dgm', 'dgm_page_19.jpg'), 780, 870, 390, 400)
d5.text((70, 1285), "Rebranding DGM Motori, Logo & Palette Officina", font=font_tag, fill=COLOR_MUTED)

pages_imgs.append(p5)


# ==================== PAGINA 6: SET FOTOGRAFICO ====================
p6, d6 = create_base_page(footer_page="06")
d6.text((70, 110), "CASE STUDY 05 / EDITORIAL PHOTOGRAPHY", font=font_tag, fill=COLOR_CORAL)
d6.text((70, 140), "Workshop Atmosphere — Set Fotografico", font=font_title, fill=COLOR_DARK)
d6.text((70, 195), "Reportage Scattato dal Vivo in Autofficina (Sony Alpha, Luce Naturale)", font=font_sub, fill=COLOR_MUTED)

add_img_to_page(p6, os.path.join(assets_dir, 'photoshoot', 'photo_01_large.jpg'), 70, 260, 530, 480)
add_img_to_page(p6, os.path.join(assets_dir, 'photoshoot', 'photo_07_large.jpg'), 640, 260, 530, 480)

add_img_to_page(p6, os.path.join(assets_dir, 'photoshoot', 'photo_02_large.jpg'), 70, 780, 340, 340)
add_img_to_page(p6, os.path.join(assets_dir, 'photoshoot', 'photo_03_large.jpg'), 450, 780, 340, 340)
add_img_to_page(p6, os.path.join(assets_dir, 'photoshoot', 'photo_05_large.jpg'), 830, 780, 340, 340)

d6.text((70, 1140), "Dettagli metallici, attrezzi e narrazione visiva del lavoro meccanico", font=font_tag, fill=COLOR_MUTED)

# Chiusura contatti a fondo pagina 6
d6.rectangle([70, 1200, PAGE_W - 70, 1400], fill=COLOR_DARK)
d6.text((120, 1240), "MARTINA TAGLIETTI — PORTFOLIO 2026", font=font_tag, fill=COLOR_GOLD)
d6.text((120, 1280), "ifts.taglietti.martina@cfpscuolafantoni.org", font=font_heading, fill=COLOR_WHITE)
d6.text((120, 1330), "Disponibile per tirocini, stage formativi e progetti freelance", font=font_sub, fill=COLOR_MUTED)

pages_imgs.append(p6)

# Salva PDF
pages_imgs[0].save(
    output_pdf_path,
    save_all=True,
    append_images=pages_imgs[1:],
    resolution=150.0
)

import shutil
shutil.copyfile(output_pdf_path, r'C:\Users\salvo\Downloads\Portfolio_Martina_Taglietti_Print_A4.pdf')
print(f"SUCCESS: Generated Portrait A4 PDF with {len(pages_imgs)} pages in {output_pdf_path} (size: {os.path.getsize(output_pdf_path)} bytes)")
