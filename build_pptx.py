import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette Constants (Turquesa Médico / Tech & Cyan Neón)
    COLOR_BG = RGBColor(3, 13, 18)          # #030D12
    COLOR_CARD = RGBColor(8, 27, 36)        # #081B24
    COLOR_CARD_HL = RGBColor(12, 38, 51)    # #0C2633
    COLOR_BORDER = RGBColor(19, 62, 79)     # #133E4F
    COLOR_CYAN = RGBColor(45, 212, 191)     # #2DD4BF (Neon Cyan)
    COLOR_TEAL = RGBColor(20, 184, 166)     # #14B8A6 (Teal/Turquesa)
    COLOR_TEXT = RGBColor(248, 250, 252)    # #F8FAFC (White/Bright)
    COLOR_MUTED = RGBColor(148, 163, 184)   # #94A3B8 (Slate Muted)
    COLOR_AMBER = RGBColor(251, 191, 36)    # #FBBF24 (Gold)
    COLOR_CORAL = RGBColor(244, 63, 94)     # #F43F5E (Coral)
    COLOR_BLUE = RGBColor(56, 189, 248)     # #38BDF8 (Sky Blue)

    assets_dir = r"C:\Users\Drewg\OneDrive\Escritorio\AlDia_Landingpage\assets"

    def apply_slide_base(slide, pretitle, title, timing, slide_num):
        # Background
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG
        bg.line.fill.background()

        # Header bar divider line
        divider = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.35), Inches(11.733), Inches(0.02))
        divider.fill.solid()
        divider.fill.fore_color.rgb = COLOR_BORDER
        divider.line.fill.background()

        # Header Text Box
        header_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.35), Inches(9.5), Inches(0.95))
        tf = header_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p_pre = tf.paragraphs[0]
        p_pre.text = pretitle.upper()
        p_pre.font.size = Pt(10)
        p_pre.font.bold = True
        p_pre.font.color.rgb = COLOR_CYAN
        p_pre.font.name = "Arial"

        p_title = tf.add_paragraph()
        p_title.text = title
        p_title.font.size = Pt(21)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_TEXT
        p_title.font.name = "Arial"

        # Timing pill badge on top right
        pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.6), Inches(0.55), Inches(1.9), Inches(0.4))
        pill.fill.solid()
        pill.fill.fore_color.rgb = COLOR_CARD
        pill.line.color.rgb = COLOR_BORDER
        pill_tf = pill.text_frame
        pill_p = pill_tf.paragraphs[0]
        pill_p.text = f"⏱️ {timing}"
        pill_p.font.size = Pt(11)
        pill_p.font.bold = True
        pill_p.font.color.rgb = COLOR_CYAN
        pill_p.alignment = PP_ALIGN.CENTER

        # Footer divider line
        f_div = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(6.9), Inches(11.733), Inches(0.015))
        f_div.fill.solid()
        f_div.fill.fore_color.rgb = COLOR_BORDER
        f_div.line.fill.background()

        # Footer Text
        footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(6.95), Inches(11.733), Inches(0.4))
        ftf = footer_box.text_frame
        ftf.word_wrap = True
        ftf.margin_left = ftf.margin_top = ftf.margin_right = ftf.margin_bottom = 0
        fp = ftf.paragraphs[0]
        fp.text = "AlDía · Análisis de Datos Web · Zegel 2026-II  |  Grupo 7"
        fp.font.size = Pt(9.5)
        fp.font.color.rgb = COLOR_MUTED

        fp2 = ftf.add_paragraph()
        fp2.text = f"Lámina {slide_num:02d} / 10"
        fp2.font.size = Pt(9.5)
        fp2.font.bold = True
        fp2.font.color.rgb = COLOR_CYAN
        fp2.alignment = PP_ALIGN.RIGHT

    def add_card(slide, left, top, width, height, title, bg_color=COLOR_CARD, border_color=COLOR_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)

        if title:
            tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), width - Inches(0.4), Inches(0.45))
            tf = tb.text_frame
            tf.word_wrap = True
            tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
            p = tf.paragraphs[0]
            p.text = title
            p.font.size = Pt(13)
            p.font.bold = True
            p.font.color.rgb = COLOR_CYAN
            p.font.name = "Arial"
        return card

    # =========================================================================
    # LÁMINA 1: PORTADA Y PRESENTACIÓN (0:00 - 0:45 min)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    apply_slide_base(s1, "Evaluación Oficial · Sesión 05 · Avance 1 Grupal", 
                     "Estrategia Digital y Analítica Web Multicanal", "0:00 – 0:45 min", 1)

    # Left Column: Project Overview
    add_card(s1, Inches(0.8), Inches(1.6), Inches(6.8), Inches(4.9), "🎯 Propósito del Proyecto")
    tb1 = s1.shapes.add_textbox(Inches(1.05), Inches(2.25), Inches(6.3), Inches(4.0))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "Despliegue y Telemetría Integral para el Aplicativo Móvil AlDía"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = COLOR_TEXT

    bullets_s1 = [
        ("Landing Page en GitHub Pages:", " Arquitectura Jamstack de alta velocidad servida desde CDN global."),
        ("Google Analytics 4 Nativo:", " Conexión directa mediante gtag.js y capa dataLayer (ID: G-84W4NXCRFJ)."),
        ("Atracción Social Multicanal:", " Fanpage oficial en Facebook para generar tráfico e impulsar el embudo."),
        ("Rigor Metodológico:", " Definición, sustentación y comparativa analítica de KPIs entre la Web y Facebook.")
    ]
    for b_title, b_desc in bullets_s1:
        p = tf1.add_paragraph()
        p.space_before = Pt(8)
        run1 = p.add_run()
        run1.text = "• " + b_title
        run1.font.bold = True
        run1.font.color.rgb = COLOR_CYAN
        run1.font.size = Pt(11.5)
        run2 = p.add_run()
        run2.text = b_desc
        run2.font.color.rgb = COLOR_MUTED
        run2.font.size = Pt(11.5)

    # Right Column: Evaluation Sheet Card
    add_card(s1, Inches(7.8), Inches(1.6), Inches(4.7), Inches(4.9), "📋 Ficha Técnica de Evaluación", bg_color=COLOR_CARD_HL)
    tb1_r = s1.shapes.add_textbox(Inches(8.05), Inches(2.3), Inches(4.2), Inches(4.0))
    tf1_r = tb1_r.text_frame
    tf1_r.word_wrap = True

    eval_items = [
        ("Institución:", "Zegel Ipae (Educación Superior)"),
        ("Curso:", "Análisis de Datos Web (Ciclo 2026-II)"),
        ("Hito Evaluativo:", "Avance 1 Grupal (Sesión 05)"),
        ("Equipo:", "Grupo 7 (Integrantes Oficiales)"),
        ("Producto:", "AlDía (Micro-SaaS para Bodegas)"),
        ("Formato:", "Exposición 10-11 min + Preguntas"),
        ("Infraestructura:", "GitHub Pages CDN + GA4 Nativo")
    ]
    for i, (lbl, val) in enumerate(eval_items):
        p = tf1_r.paragraphs[0] if i == 0 else tf1_r.add_paragraph()
        p.space_before = Pt(6)
        r1 = p.add_run()
        r1.text = lbl + " "
        r1.font.bold = True
        r1.font.color.rgb = COLOR_CYAN
        r1.font.size = Pt(11)
        r2 = p.add_run()
        r2.text = val
        r2.font.color.rgb = COLOR_TEXT
        r2.font.size = Pt(11)

    s1.notes_slide.notes_text_frame.text = (
        "LÁMINA 1 (0:00 - 0:45 min): Saludo formal, presentación de integrantes del Grupo 7, "
        "planteamiento de la evaluación del Avance 1 de Análisis de Datos Web y alcance de la arquitectura "
        "multicanal: GitHub Pages (Jamstack CDN) + Google Analytics 4 nativo + Facebook Fanpage."
    )

    # =========================================================================
    # LÁMINA 2: PROPUESTA DEL APLICATIVO MÓVIL Y EMBUDO (0:45 - 1:45 min)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    apply_slide_base(s2, "Modelo de Negocio & Funnel Multicanal", 
                     "Propuesta del Aplicativo Móvil y Embudo de Conversión", "0:45 – 1:45 min", 2)

    # Left: The Value Prop
    add_card(s2, Inches(0.8), Inches(1.6), Inches(5.6), Inches(4.9), "🛒 AlDía: Control Inteligente de Mermas")
    tb2_l = s2.shapes.add_textbox(Inches(1.05), Inches(2.25), Inches(5.1), Inches(4.0))
    tf2_l = tb2_l.text_frame
    tf2_l.word_wrap = True

    p = tf2_l.paragraphs[0]
    p.text = "Problema Central en Pequeños Comercios:"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_CORAL

    p = tf2_l.add_paragraph()
    p.text = "Bodegas y minimarkets en Perú pierden S/ 350 - S/ 600 mensuales por mercadería que vence en anaquel y pérdida de la ventana de canje con proveedores (Bimbo, Gloria)."
    p.font.size = Pt(11)
    p.font.color.rgb = COLOR_MUTED

    p = tf2_l.add_paragraph()
    p.space_before = Pt(8)
    p.text = "Solución de Baja Fricción:"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_CYAN

    p = tf2_l.add_paragraph()
    p.text = "No exige pistolear cada venta en caja. Automatiza ingresos por foto de guías de remisión (IA), activa un Semáforo Preventivo de canjes y descuenta lotes bajo regla FEFO."
    p.font.size = Pt(11)
    p.font.color.rgb = COLOR_MUTED

    p = tf2_l.add_paragraph()
    p.space_before = Pt(8)
    p.text = "Buyer Persona Objetivo:"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_AMBER

    p = tf2_l.add_paragraph()
    p.text = "Dueños de bodegas y minimarkets (30-55 años, Régimen NRUS, urbanos en Lima y provincias)."
    p.font.size = Pt(11)
    p.font.color.rgb = COLOR_MUTED

    # Right: The Funnel
    add_card(s2, Inches(6.7), Inches(1.6), Inches(5.8), Inches(4.9), "🔻 Arquitectura del Embudo (Funnel)", bg_color=COLOR_CARD_HL)
    
    stages = [
        ("Top of Funnel (ToFU) · Descubrimiento", "Fanpage en Facebook: Generar conciencia del dolor ('¿Cuánta plata botas al mes en productos vencidos?').", COLOR_BLUE, Inches(2.3)),
        ("Middle of Funnel (MoFU) · Consideración", "Landing Page en GitHub Pages: Explicación de la solución, calculadora interactiva de ahorro y bot demo.", COLOR_TEAL, Inches(3.5)),
        ("Bottom of Funnel (BoFU) · Conversión", "Clic en Botón CTA 'Descargar App / Prueba Gratis de 14 días' (Activación del Lead y Evento Clave en GA4).", COLOR_CYAN, Inches(4.7))
    ]
    for st_title, st_desc, st_color, top_pos in stages:
        box = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.95), top_pos, Inches(5.3), Inches(1.05))
        box.fill.solid()
        box.fill.fore_color.rgb = COLOR_CARD
        box.line.color.rgb = st_color
        box.line.width = Pt(1.5)

        tb = s2.shapes.add_textbox(Inches(7.1), top_pos + Inches(0.08), Inches(5.0), Inches(0.9))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = st_title
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = st_color
        p2 = tf.add_paragraph()
        p2.text = st_desc
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = COLOR_MUTED

    s2.notes_slide.notes_text_frame.text = (
        "LÁMINA 2 (0:45 - 1:45 min): Explicar el valor de AlDía, el problema de las pérdidas en bodegas "
        "y cómo se estructura el embudo entre Facebook (atracción ToFU), Landing Page en GitHub Pages (MoFU) y descarga CTA (BoFU)."
    )

    # =========================================================================
    # LÁMINA 3: LANDING PAGE EN GITHUB PAGES (1:45 - 3:00 min)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    apply_slide_base(s3, "Infraestructura Web & Principio AIDA", 
                     "Landing Page en GitHub Pages y Arquitectura Jamstack", "1:45 – 3:00 min", 3)

    # Left: Details
    add_card(s3, Inches(0.8), Inches(1.6), Inches(5.8), Inches(4.9), "⚙️ Infraestructura Jamstack y AIDA")
    tb3 = s3.shapes.add_textbox(Inches(1.05), Inches(2.25), Inches(5.3), Inches(4.0))
    tf3 = tb3.text_frame
    tf3.word_wrap = True

    p = tf3.paragraphs[0]
    p.text = "Servidor Cloud Global (Jamstack CDN):"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_CYAN
    p2 = tf3.add_paragraph()
    p2.text = "Despliegue estático en GitHub Pages (dreyeles.github.io/Proyecto_ALdia/) con SSL HTTPS nativo. Carga en <800ms en celulares 3G/4G, alta disponibilidad 99.9% y cero límites de memoria PHP."
    p2.font.size = Pt(10.5)
    p2.font.color.rgb = COLOR_MUTED

    aida_points = [
        ("Atención (A):", "Titular de pérdida contundente: 'Deja de botar plata por productos vencidos'."),
        ("Interés (I):", "Mockup visual de smartphone con alertas de canje preventivo (Yogurt 9 días)."),
        ("Deseo (D):", "Calculadora interactiva de plata salvada según compras mensuales."),
        ("Acción (A):", "Botón CTA 'Quiero probarlo gratis' visible inmediatamente 'Above the fold'.")
    ]
    p_header = tf3.add_paragraph()
    p_header.space_before = Pt(8)
    p_header.text = "Arquitectura Persuasiva AIDA:"
    p_header.font.bold = True
    p_header.font.size = Pt(12)
    p_header.font.color.rgb = COLOR_AMBER

    for a_lbl, a_desc in aida_points:
        p = tf3.add_paragraph()
        p.space_before = Pt(3)
        r1 = p.add_run()
        r1.text = "• " + a_lbl + " "
        r1.font.bold = True
        r1.font.color.rgb = COLOR_CYAN
        r1.font.size = Pt(10)
        r2 = p.add_run()
        r2.text = a_desc
        r2.font.color.rgb = COLOR_MUTED
        r2.font.size = Pt(10)

    # Right: Image
    img_path = os.path.join(assets_dir, "landing_page_hero_aldia.png")
    if os.path.exists(img_path):
        s3.shapes.add_picture(img_path, Inches(6.9), Inches(1.6), Inches(5.6), Inches(4.9))

    s3.notes_slide.notes_text_frame.text = (
        "LÁMINA 3 (1:45 - 3:00 min): Guiar visualmente por la Landing Page, justificar la elección de GitHub Pages "
        "por velocidad de carga (<800ms) frente a hostings compartidos y destacar el botón CTA 'Above the fold'."
    )

    # =========================================================================
    # LÁMINA 4: INTEGRACIÓN CON GA4 NATIVO (3:00 - 4:15 min)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    apply_slide_base(s4, "Telemetría Oficial & Modelo de Eventos", 
                     "Integración Técnica de Analítica con Google Analytics 4 Nativo", "3:00 – 4:15 min", 4)

    # Left: Technical Justification
    add_card(s4, Inches(0.8), Inches(1.6), Inches(5.8), Inches(4.9), "🔌 Conexión Oficial y Eventos GA4")
    tb4 = s4.shapes.add_textbox(Inches(1.05), Inches(2.25), Inches(5.3), Inches(4.0))
    tf4 = tb4.text_frame
    tf4.word_wrap = True

    p = tf4.paragraphs[0]
    p.text = "¿Por qué Implementación Nativa de GA4?"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_CYAN
    p2 = tf4.add_paragraph()
    p2.text = "Integración directa de gtag.js y window.dataLayer en el código fuente. Elimina intermediarios y plugins pesados de CMS, garantizando máxima velocidad de carga (<800ms) y control granular de eventos."
    p2.font.size = Pt(10.5)
    p2.font.color.rgb = COLOR_MUTED

    tech_points = [
        ("Google Analytics 4 (GA4):", "ID oficial G-84W4NXCRFJ. Opera bajo modelo centrado en Eventos y Parámetros."),
        ("Capa dataLayer Activa:", "Envío estructurado de micro-conversiones (clics en CTA, calculadora y WhatsApp)."),
        ("Medición Mejorada:", "Seguimiento automático de desplazamientos (scroll), enlaces salientes y vistas."),
        ("Eventos Clave (Key Events):", "Configuración de click_cta_download para medición de conversión directa.")
    ]
    p_header = tf4.add_paragraph()
    p_header.space_before = Pt(8)
    p_header.text = "Pilares de la Telemetría:"
    p_header.font.bold = True
    p_header.font.size = Pt(12)
    p_header.font.color.rgb = COLOR_AMBER

    for t_lbl, t_desc in tech_points:
        p = tf4.add_paragraph()
        p.space_before = Pt(3)
        r1 = p.add_run()
        r1.text = "• " + t_lbl + " "
        r1.font.bold = True
        r1.font.color.rgb = COLOR_CYAN
        r1.font.size = Pt(10)
        r2 = p.add_run()
        r2.text = t_desc
        r2.font.color.rgb = COLOR_MUTED
        r2.font.size = Pt(10)

    # Right: Stream Details Image
    img_path4 = os.path.join(assets_dir, "ga4_flujo_datos_aldia.jpg")
    if os.path.exists(img_path4):
        s4.shapes.add_picture(img_path4, Inches(6.9), Inches(1.6), Inches(5.6), Inches(4.9))

    s4.notes_slide.notes_text_frame.text = (
        "LÁMINA 4 (3:00 - 4:15 min): Explicar cómo la integración nativa de GA4 con dataLayer garantiza "
        "trazabilidad total sin scripts pesados de terceros y la captura de eventos clave (G-84W4NXCRFJ)."
    )

    # =========================================================================
    # LÁMINA 5: CANAL SOCIAL: FANPAGE EN FACEBOOK (4:15 - 5:30 min)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    apply_slide_base(s5, "Atracción Social & Generación de Tráfico", 
                     "Canal de Tráfico Social: Fanpage en Facebook", "4:15 – 5:30 min", 5)

    # Left: Strategy
    add_card(s5, Inches(0.8), Inches(1.6), Inches(5.8), Inches(4.9), "📘 Estrategia en Facebook: 'AlDía Perú'")
    tb5 = s5.shapes.add_textbox(Inches(1.05), Inches(2.25), Inches(5.3), Inches(4.0))
    tf5 = tb5.text_frame
    tf5.word_wrap = True

    p = tf5.paragraphs[0]
    p.text = "Justificación del Canal:"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_CYAN
    p2 = tf5.add_paragraph()
    p2.text = "Facebook es la red principal donde interactúan dueños de bodegas y minimarkets en Perú, participando en grupos gremiales y comerciales de sus distritos."
    p2.font.size = Pt(10.5)
    p2.font.color.rgb = COLOR_MUTED

    fb_points = [
        ("Botón CTA de la Fanpage:", "Configurado como 'Usar aplicación / Visitar web' direccionando a GitHub Pages."),
        ("Estrategia de Contenidos:", "Infografías de vencimiento, alertas de canje Bimbo/Gloria y tips de rentabilidad."),
        ("Parámetros UTM:", "Enlaces con utm_source=facebook&utm_medium=organic_post para trazabilidad en GA4."),
        ("Objetivo del Canal:", "Alimentar la fase ToFU y empujar tráfico cualificado hacia la Landing Page.")
    ]
    p_header = tf5.add_paragraph()
    p_header.space_before = Pt(8)
    p_header.text = "Configuración Operativa:"
    p_header.font.bold = True
    p_header.font.size = Pt(12)
    p_header.font.color.rgb = COLOR_AMBER

    for f_lbl, f_desc in fb_points:
        p = tf5.add_paragraph()
        p.space_before = Pt(3)
        r1 = p.add_run()
        r1.text = "• " + f_lbl + " "
        r1.font.bold = True
        r1.font.color.rgb = COLOR_CYAN
        r1.font.size = Pt(10)
        r2 = p.add_run()
        r2.text = f_desc
        r2.font.color.rgb = COLOR_MUTED
        r2.font.size = Pt(10)

    # Right: Facebook Mockup Visual
    add_card(s5, Inches(6.9), Inches(1.6), Inches(5.6), Inches(4.9), "📱 Simulación Visual de la Fanpage", bg_color=COLOR_CARD_HL)
    tb5_fb = s5.shapes.add_textbox(Inches(7.15), Inches(2.3), Inches(5.1), Inches(4.0))
    tf5_fb = tb5_fb.text_frame
    tf5_fb.word_wrap = True

    p = tf5_fb.paragraphs[0]
    p.text = "AlDía Perú – App para Bodegas"
    p.font.bold = True
    p.font.size = Pt(15)
    p.font.color.rgb = COLOR_TEXT

    p = tf5_fb.add_paragraph()
    p.text = "@aldia.pe  ·  Software de gestión comercial para minimarkets"
    p.font.size = Pt(10)
    p.font.color.rgb = COLOR_BLUE

    # Post simulation box
    post_box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.15), Inches(3.2), Inches(5.1), Inches(2.9))
    post_box.fill.solid()
    post_box.fill.fore_color.rgb = COLOR_CARD
    post_box.line.color.rgb = COLOR_BORDER

    tb_post = s5.shapes.add_textbox(Inches(7.35), Inches(3.3), Inches(4.7), Inches(2.7))
    tf_post = tb_post.text_frame
    tf_post.word_wrap = True

    p = tf_post.paragraphs[0]
    p.text = "🚨 ¿Sabías que el 4.5% de tus ganancias se van a la basura en yogurts y embutidos vencidos?"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = COLOR_TEXT

    p = tf_post.add_paragraph()
    p.space_before = Pt(4)
    p.text = "Con AlDía programas el canje gratuito con el repartidor antes de que caduque el plazo. ¡Prueba gratis por 14 días!"
    p.font.size = Pt(10)
    p.font.color.rgb = COLOR_MUTED

    p = tf_post.add_paragraph()
    p.space_before = Pt(10)
    p.text = "👉 Probar AlDía Gratis (dreyeles.github.io/Proyecto_ALdia/)"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = COLOR_CYAN

    s5.notes_slide.notes_text_frame.text = (
        "LÁMINA 5 (4:15 - 5:30 min): Presentar la Fanpage de Facebook, la estrategia de contenidos "
        "y cómo se estructura como canal generador de tráfico hacia la landing page en GitHub Pages."
    )

    # =========================================================================
    # LÁMINA 6: DEFINICIÓN Y SUSTENTACIÓN DE KPIS PARA LA WEB (5:30 - 7:00 min)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    apply_slide_base(s6, "Rúbrica Clave · Criterio Científico de Medición", 
                     "Definición y Sustentación de KPIs para la Web", "5:30 – 7:00 min", 6)

    # Table of KPIs
    rows, cols = 6, 4
    left, top, width, height = Inches(0.8), Inches(1.6), Inches(11.733), Inches(4.9)
    table_shape = s6.shapes.add_table(rows, cols, left, top, width, height)
    table = table_shape.table

    # Column widths
    table.columns[0].width = Inches(2.6)
    table.columns[1].width = Inches(3.2)
    table.columns[2].width = Inches(4.2)
    table.columns[3].width = Inches(1.733)

    headers = ["Indicador (KPI)", "Fórmula / Métrica en GA4", "Sustentación Analítica (Por qué importa)", "Meta / Benchmark"]
    for col_idx, h_text in enumerate(headers):
        cell = table.cell(0, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_CARD_HL
        p = cell.text_frame.paragraphs[0]
        p.text = h_text
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = COLOR_CYAN

    data_kpis = [
        ("Usuarios y Sesiones", "Total Users & Sessions", "Mide el volumen neto de bodegueros alcanzados y la frecuencia de retorno.", "Volumen base"),
        ("Tasa de Interacción (Engagement)", "(Sesiones Interactivas / Total) * 100", "Reemplazo oficial del rebote en GA4. Mide sesiones >10s o con eventos.", "> 60.0%"),
        ("Tiempo Medio de Interacción", "Average Engagement Time", "Retención real: valida si el comerciante leyó la propuesta y usó la calculadora.", "> 1m 15s"),
        ("⭐ TASA DE CONVERSIÓN (CR)", "(Clics en Descargar / Sesiones) * 100", "KPI Maestro: valida cuántos visitantes decidieron descargar o probar la app.", "3.0% – 7.0% (SaaS)"),
        ("Canales de Adquisición", "Session Default Channel Group", "Evalúa el aporte de Facebook (Social) frente a tráfico Directo y Referencias.", "Facebook > 40%")
    ]

    for row_idx, row_data in enumerate(data_kpis, start=1):
        for col_idx, cell_value in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.fill.solid()
            if row_idx == 4: # KPI Maestro highlight
                cell.fill.fore_color.rgb = RGBColor(12, 45, 40)
            else:
                cell.fill.fore_color.rgb = COLOR_CARD if row_idx % 2 == 1 else RGBColor(5, 18, 25)
            
            p = cell.text_frame.paragraphs[0]
            p.text = cell_value
            p.font.size = Pt(10)
            if col_idx == 0:
                p.font.bold = True
                p.font.color.rgb = COLOR_CYAN if row_idx == 4 else COLOR_TEXT
            elif col_idx == 3:
                p.font.bold = True
                p.font.color.rgb = COLOR_AMBER if row_idx == 4 else COLOR_CYAN
            else:
                p.font.color.rgb = COLOR_MUTED

    s6.notes_slide.notes_text_frame.text = (
        "LÁMINA 6 (5:30 - 7:00 min) - RÚBRICA CLAVE: Sustentar técnicamente los 5 KPIs de la web, "
        "explicar por qué el Engagement Rate supera al antiguo rebote y destacar el CR Maestro como indicador de viabilidad."
    )

    # =========================================================================
    # LÁMINA 7: DEFINICIÓN Y SUSTENTACIÓN DE KPIS PARA FACEBOOK (7:00 - 8:15 min)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    apply_slide_base(s7, "Analítica Social & Tráfico Derivado", 
                     "Definición y Sustentación de KPIs para Facebook", "7:00 – 8:15 min", 7)

    # Left: Social KPI Table
    add_card(s7, Inches(0.8), Inches(1.6), Inches(6.8), Inches(4.9), "📊 Indicadores Clave en Meta Business Suite")
    
    rows7, cols7 = 5, 3
    t7_shape = s7.shapes.add_table(rows7, cols7, Inches(1.0), Inches(2.2), Inches(6.4), Inches(4.0))
    t7 = t7_shape.table
    t7.columns[0].width = Inches(1.9)
    t7.columns[1].width = Inches(2.2)
    t7.columns[2].width = Inches(2.3)

    h7 = ["KPI Facebook", "Definición / Cálculo", "Propósito Analítico"]
    for c_i, h in enumerate(h7):
        cell = t7.cell(0, c_i)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_CARD_HL
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.bold = True
        p.font.size = Pt(10)
        p.font.color.rgb = COLOR_CYAN

    fb_kpi_data = [
        ("Alcance (Reach)", "Cuentas únicas que vieron posts.", "Amplitud inicial del embudo (ToFU)."),
        ("Impresiones", "Visualizaciones totales.", "Frecuencia de impacto del mensaje."),
        ("Tasa Engagement", "(Interacciones / Alcance) * 100", "Evalúa resonancia y debate en bodegas."),
        ("⭐ CTR SALIENTE", "(Clics al Enlace / Impresiones) * 100", "KPI Estrella: mide visitas enviadas a la web.")
    ]
    for r_i, r_val in enumerate(fb_kpi_data, start=1):
        for c_i, val in enumerate(r_val):
            cell = t7.cell(r_i, c_i)
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(12, 45, 55) if r_i == 4 else COLOR_CARD
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(9.5)
            p.font.color.rgb = COLOR_CYAN if r_i == 4 else (COLOR_TEXT if c_i == 0 else COLOR_MUTED)
            if c_i == 0 or r_i == 4:
                p.font.bold = True

    # Right: Vanity Metrics vs Real Value
    add_card(s7, Inches(7.8), Inches(1.6), Inches(4.7), Inches(4.9), "⚖️ Criterio: Likes vs Clics Reales", bg_color=COLOR_CARD_HL)
    tb7_r = s7.shapes.add_textbox(Inches(8.05), Inches(2.25), Inches(4.2), Inches(4.0))
    tf7_r = tb7_r.text_frame
    tf7_r.word_wrap = True

    p = tf7_r.paragraphs[0]
    p.text = "Métricas de Vanidad vs Valor Real"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_TEXT

    p = tf7_r.add_paragraph()
    p.space_before = Pt(8)
    p.text = "❌ Métrica de Vanidad:"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = COLOR_CORAL

    p = tf7_r.add_paragraph()
    p.text = "500 'Me gusta' en una publicación pueden lucir bien, pero no representan usuarios ni descargas de la aplicación."
    p.font.size = Pt(10)
    p.font.color.rgb = COLOR_MUTED

    p = tf7_r.add_paragraph()
    p.space_before = Pt(8)
    p.text = "✅ Métrica de Valor (CTR Saliente):"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = COLOR_CYAN

    p = tf7_r.add_paragraph()
    p.text = "40 comerciantes que hicieron clic en el enlace demuestran necesidad real, visitan la landing y activan el funnel de conversión."
    p.font.size = Pt(10)
    p.font.color.rgb = COLOR_MUTED

    p = tf7_r.add_paragraph()
    p.space_before = Pt(10)
    p.text = "🎯 Benchmark B2B: Outbound CTR de 1.5% a 3.2%."
    p.font.bold = True
    p.font.size = Pt(10.5)
    p.font.color.rgb = COLOR_AMBER

    s7.notes_slide.notes_text_frame.text = (
        "LÁMINA 7 (7:00 - 8:15 min): Explicar los KPIs de Facebook, desarmar métricas de vanidad (likes) "
        "y sustentar por qué el Outbound CTR es el indicador clave que alimenta la landing page."
    )

    # =========================================================================
    # LÁMINA 8: RESULTADOS INICIALES Y COMPARATIVA (8:15 - 9:30 min)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    apply_slide_base(s8, "Evidencia Empírica de Telemetría", 
                     "Resultados Iniciales y Comparativa Multicanal", "8:15 – 9:30 min", 8)

    # Left: Image GA4 Realtime
    img_path8 = os.path.join(assets_dir, "ga4_dashboard_realtime_users.png")
    if os.path.exists(img_path8):
        s8.shapes.add_picture(img_path8, Inches(0.8), Inches(1.6), Inches(5.8), Inches(4.9))

    # Right: Data & Analysis
    add_card(s8, Inches(6.9), Inches(1.6), Inches(5.6), Inches(4.9), "📊 Datos Registrados en la Prueba")
    tb8 = s8.shapes.add_textbox(Inches(7.15), Inches(2.25), Inches(5.1), Inches(4.0))
    tf8 = tb8.text_frame
    tf8.word_wrap = True

    p = tf8.paragraphs[0]
    p.text = "Evidencia Empírica en GA4 (ID: G-84W4NXCRFJ):"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = COLOR_CYAN

    results = [
        ("8 Usuarios Activos:", " Registro simultáneo en tiempo real durante las pruebas de despliegue."),
        ("Audiencia Objetivo Perú:", " 3 usuarios activos confirmados desde Lima y provincias."),
        ("Tiempo de Permanencia:", " Media superior a 1m 30s en visitantes con interacción."),
        ("Eventos Capturados:", " Scroll depth (25% - 90%), interacción con celular demo y simulador.")
    ]
    for r_lbl, r_desc in results:
        p = tf8.add_paragraph()
        p.space_before = Pt(4)
        r1 = p.add_run()
        r1.text = "• " + r_lbl + " "
        r1.font.bold = True
        r1.font.color.rgb = COLOR_TEXT
        r1.font.size = Pt(10)
        r2 = p.add_run()
        r2.text = r_desc
        r2.font.color.rgb = COLOR_MUTED
        r2.font.size = Pt(10)

    p_comp = tf8.add_paragraph()
    p_comp.space_before = Pt(10)
    p_comp.text = "Comparativa Multicanal:"
    p_comp.font.bold = True
    p_comp.font.size = Pt(12)
    p_comp.font.color.rgb = COLOR_AMBER

    p_comp_desc = tf8.add_paragraph()
    p_comp_desc.text = "Facebook aportó el 40% del flujo de entrada inicial (alto volumen, baja permanencia), mientras que la Landing Page retuvo el análisis profundo de la solución (conversión MoFU)."
    p_comp_desc.font.size = Pt(10)
    p_comp_desc.font.color.rgb = COLOR_MUTED

    s8.notes_slide.notes_text_frame.text = (
        "LÁMINA 8 (8:15 - 9:30 min): Interpretar las capturas reales de Google Analytics con 8 usuarios activos, "
        "describir el tráfico de Perú y contrastar el rendimiento entre Facebook y la web."
    )

    # =========================================================================
    # LÁMINA 9: CONCLUSIONES Y PRÓXIMOS PASOS (9:30 - 10:30 min)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    apply_slide_base(s9, "Evaluación Crítica & Hoja de Ruta", 
                     "Conclusiones del Avance 1 y Próximos Pasos", "9:30 – 10:30 min", 9)

    # Left: Conclusions
    add_card(s9, Inches(0.8), Inches(1.6), Inches(5.8), Inches(4.9), "🎯 Conclusiones del Avance 1")
    tb9_l = s9.shapes.add_textbox(Inches(1.05), Inches(2.25), Inches(5.3), Inches(4.0))
    tf9_l = tb9_l.text_frame
    tf9_l.word_wrap = True

    concs = [
        ("Excelencia de Arquitectura Jamstack:", "Demostramos que alojar la landing en GitHub Pages con GA4 nativo ofrece un desempeño superior a hostings compartidos: velocidad sub-segundo (<800ms), disponibilidad 99.9% y costo cero."),
        ("Trazabilidad Total de Telemetría:", "El flujo de datos entre dataLayer y el panel de GA4 opera en tiempo real sin latencias ni pérdida de eventos."),
        ("Control y Despliegue con Git (CI/CD):", "Cada mejora en el diseño o eventos se despliega mediante control de versiones en GitHub, permitiendo trazabilidad y reversibilidad inmediata.")
    ]
    for i, (c_lbl, c_desc) in enumerate(concs):
        p = tf9_l.paragraphs[0] if i == 0 else tf9_l.add_paragraph()
        p.space_before = Pt(8) if i > 0 else Pt(0)
        r1 = p.add_run()
        r1.text = "✅ " + c_lbl + "\n"
        r1.font.bold = True
        r1.font.color.rgb = COLOR_CYAN
        r1.font.size = Pt(11)
        r2 = p.add_run()
        r2.text = c_desc
        r2.font.color.rgb = COLOR_MUTED
        r2.font.size = Pt(10)

    # Right: Next Steps (Avance 2)
    add_card(s9, Inches(6.9), Inches(1.6), Inches(5.6), Inches(4.9), "🚀 Hoja de Ruta para el Avance 2", bg_color=COLOR_CARD_HL)
    tb9_r = s9.shapes.add_textbox(Inches(7.15), Inches(2.25), Inches(5.1), Inches(4.0))
    tf9_r = tb9_r.text_frame
    tf9_r.word_wrap = True

    next_steps = [
        ("Pruebas A/B en el Botón CTA:", "Experimentar con el contraste de color (Terracota vs Cian) y copy ('Descargar App' vs 'Calcular mi ahorro gratis') para optimizar la tasa de conversión."),
        ("Dashboard Integral en Looker Studio:", "Construir un cuadro de mando automatizado conectando las APIs de Google Analytics 4 y Meta Facebook Insights en un solo reporte visual."),
        ("Segmentación de Audiencia:", "Analizar la conversión discriminada por distrito y tipo de dispositivo móvil (Android vs iOS).")
    ]
    for i, (n_lbl, n_desc) in enumerate(next_steps):
        p = tf9_r.paragraphs[0] if i == 0 else tf9_r.add_paragraph()
        p.space_before = Pt(8) if i > 0 else Pt(0)
        r1 = p.add_run()
        r1.text = "🔹 " + n_lbl + "\n"
        r1.font.bold = True
        r1.font.color.rgb = COLOR_AMBER
        r1.font.size = Pt(11)
        r2 = p.add_run()
        r2.text = n_desc
        r2.font.color.rgb = COLOR_MUTED
        r2.font.size = Pt(10)

    s9.notes_slide.notes_text_frame.text = (
        "LÁMINA 9 (9:30 - 10:30 min): Sintetizar los logros del Avance 1, abordar con madurez "
        "las ventajas de GitHub Pages y GA4 nativo y conectar con la visión del Avance 2 (Pruebas A/B y Looker Studio)."
    )

    # =========================================================================
    # LÁMINA 10: CIERRE Y RONDA DE PREGUNTAS (10:30 - 11:00 min)
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    apply_slide_base(s10, "Sustentación Final · Ronda de Preguntas", 
                     "Cierre de Exposición y Ronda de Preguntas", "10:30 – 11:00 min", 10)

    # Left: Formal Closing
    add_card(s10, Inches(0.8), Inches(1.6), Inches(4.8), Inches(4.9), "🤝 Agradecimiento")
    tb10_l = s10.shapes.add_textbox(Inches(1.05), Inches(2.25), Inches(4.3), Inches(4.0))
    tf10_l = tb10_l.text_frame
    tf10_l.word_wrap = True

    p = tf10_l.paragraphs[0]
    p.text = "¡Muchas Gracias por su Atención!"
    p.font.bold = True
    p.font.size = Pt(16)
    p.font.color.rgb = COLOR_TEXT

    p = tf10_l.add_paragraph()
    p.space_before = Pt(10)
    p.text = "Equipo Evaluado: Grupo 7\nCurso: Análisis de Datos Web (Ciclo 2026-II)\nInstituto Zegel Ipae"
    p.font.size = Pt(11)
    p.font.color.rgb = COLOR_MUTED

    p = tf10_l.add_paragraph()
    p.space_before = Pt(16)
    p.text = "Quedamos a disposición del docente para responder las preguntas de sustentación técnica."
    p.font.bold = True
    p.font.size = Pt(11.5)
    p.font.color.rgb = COLOR_CYAN

    # Right: Prepared Answers to Typical Questions
    add_card(s10, Inches(5.9), Inches(1.6), Inches(6.6), Inches(4.9), "🛡️ Respuestas Técnicas Preparadas", bg_color=COLOR_CARD_HL)
    tb10_r = s10.shapes.add_textbox(Inches(6.15), Inches(2.2), Inches(6.1), Inches(4.1))
    tf10_r = tb10_r.text_frame
    tf10_r.word_wrap = True

    qa_list = [
        ("1. ¿Por qué GitHub Pages y qué ventajas ofrece?", 
         "Elegimos GitHub Pages por su CDN global, carga móvil en <800ms (vital para 3G/4G en bodegas), disponibilidad 99.9% y cero riesgos de caídas de base de datos o límites de memoria PHP."),
        ("2. ¿Cómo configuraron el evento de conversión en GA4?", 
         "Enlazamos gtag.js con el ID G-84W4NXCRFJ, despachamos 'click_cta_download' en dataLayer y en GA4 lo marcamos como 'Evento Clave' (Key Event) para medir la Tasa de Conversión (CR)."),
        ("3. ¿Si el rebote supera el 70%, qué harían en la landing?", 
         "En landing de conversión un 70% es crítico. Hipótesis: lentitud móvil o 'message mismatch' con Facebook. Plan: comprimir activos, unificar copy y ubicar el CTA más visible.")
    ]
    for i, (q, a) in enumerate(qa_list):
        p = tf10_r.paragraphs[0] if i == 0 else tf10_r.add_paragraph()
        p.space_before = Pt(6) if i > 0 else Pt(0)
        r1 = p.add_run()
        r1.text = q + "\n"
        r1.font.bold = True
        r1.font.color.rgb = COLOR_CYAN
        r1.font.size = Pt(10)
        r2 = p.add_run()
        r2.text = a
        r2.font.color.rgb = COLOR_MUTED
        r2.font.size = Pt(9)

    s10.notes_slide.notes_text_frame.text = (
        "LÁMINA 10 (10:30 - 11:00 min): Cierre formal de la exposición grupal y pase directo "
        "a la ronda de preguntas aleatorias del docente. Apoyarse en las 3 respuestas técnicas estructuradas."
    )

    output_path = r"C:\Users\Drewg\OneDrive\Escritorio\AlDia_Landingpage\Presentacion_Avance1_Analisis_Datos_Web.pptx"
    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == "__main__":
    create_presentation()
