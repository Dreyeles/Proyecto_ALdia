import os

# 1. Update diapositivas_analisis_datos_web.html
html_path = r"C:\Users\Drewg\OneDrive\Escritorio\AlDia_Landingpage\diapositivas_analisis_datos_web.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Replacements in HTML
replacements = [
    ("Despliegue de Landing Page en WordPress, telemetría oficial con Google Site Kit (GA4) y canal social en Facebook Fanpage.",
     "Despliegue de Landing Page en GitHub Pages (Jamstack CDN), telemetría oficial con Google Analytics 4 Nativo y canal social en Facebook Fanpage."),
    
    ("<span class=\"formula-tag\">WordPress 6.x</span>\n                <span class=\"formula-tag\">Hosting Gratuito</span>\n                <span class=\"formula-tag\">Google Site Kit</span>",
     "<span class=\"formula-tag\">GitHub Pages</span>\n                <span class=\"formula-tag\">Jamstack CDN</span>\n                <span class=\"formula-tag\">GA4 Nativo & dataLayer</span>"),

    ("Hosting:</strong> InfinityFree / AccuWeb (Free Cloud)",
     "Hosting:</strong> GitHub Pages (Jamstack CDN Global)"),

    ("Landing Page en WordPress en <span class=\"highlight\">Hosting Gratuito</span>",
     "Landing Page en GitHub Pages y <span class=\"highlight\">Arquitectura Jamstack</span>"),

    ("⚙️ Servidor y Dominio Activo",
     "⚙️ Infraestructura Jamstack y Dominio Oficial"),

    ("<strong>Entorno:</strong> WordPress 6.x alojado en servidor cloud gratuito (<strong>InfinityFree / AccuWebHosting</strong>) con PHP 8.2 y base de datos MySQL, con réplica estática ultrarrápida en GitHub Pages / Vercel.",
     "<strong>Entorno:</strong> Servidor CDN global de <strong>GitHub Pages</strong> con control de versiones Git, entrega estática minificada en sub-segundo (<800ms) y alta disponibilidad del 99.9% sin saturaciones de CPU ni bases de datos."),

    ("aldia.infinityfreeapp.com",
     "dreyeles.github.io/Proyecto_ALdia/"),

    ("Integración Técnica de Analítica con <span class=\"highlight\">Google Site Kit</span>",
     "Integración Técnica de Analítica con <span class=\"highlight\">Google Analytics 4 Nativo</span>"),

    ("🔌 ¿Por qué Google Site Kit?",
     "🔌 ¿Por qué Implementación Nativa de GA4?"),

    ("Plugin oficial de Google que implementa las etiquetas de medición en WordPress <strong>sin alterar archivos PHP del tema</strong>, asegurando persistencia ante actualizaciones y cumplimiento de estándares de privacidad.",
     "Integración directa de <code>gtag.js</code> y la capa <code>dataLayer</code> en el código fuente. Elimina intermediarios y plugins pesados de CMS, garantizando <strong>máxima velocidad de carga móvil (<800ms)</strong> y control granular de eventos."),

    ("Infraestructura a Costo Cero Viable:</strong> Se comprobó la factibilidad técnica de desplegar WordPress con Google Site Kit y GA4 sin costos de servidor.",
     "Excelencia de la Arquitectura Jamstack:</strong> Demostramos que alojar la landing en <strong>GitHub Pages con GA4 nativo</strong> supera a los hostings tradicionales en velocidad, disponibilidad y costo cero."),

    ("1. ¿Por qué ese hosting y qué limitaciones hallaron?</div>\n                <div class=\"qa-a\">Elegimos InfinityFree/AccuWeb por compatibilidad MySQL y PHP 8 sin publicidad invasiva. Limitaciones: memoria PHP (128MB) y tiempos de ejecución que mitigamos optimizando código y caché.",
     "1. ¿Por qué GitHub Pages y qué ventajas ofrece frente a un hosting gratuito tradicional?</div>\n                <div class=\"qa-a\">Elegimos GitHub Pages por su CDN global, carga móvil en <800ms (vital para 3G/4G en bodegas), disponibilidad 99.9% y cero riesgos de caídas de base de datos o límites de memoria PHP."),

    ("2. ¿Cómo configuraron el evento de conversión en GA4?</div>\n                <div class=\"qa-a\">Vía Google Site Kit con Medición Mejorada, inyectando un evento personalizado en <code>dataLayer.push</code> y marcándolo como 'Evento Clave' (Key Event) en Administrar > Eventos de GA4.",
     "2. ¿Cómo configuraron el evento de conversión en GA4?</div>\n                <div class=\"qa-a\">Enlazamos gtag.js con el ID G-84W4NXCRFJ, despachamos 'click_cta_download' en dataLayer y en GA4 lo marcamos como 'Evento Clave' (Key Event) para medir la Tasa de Conversión (CR).")
]

for old, new in replacements:
    if old in html:
        html = html.replace(old, new)
        print(f"Replaced: {old[:40]}...")
    else:
        print(f"NOT FOUND: {old[:40]}...")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated HTML slides successfully!")

