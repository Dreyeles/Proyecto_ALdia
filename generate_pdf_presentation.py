import os
import subprocess
from bs4 import BeautifulSoup
import pymupdf

html_src = r"c:\Users\Drewg\OneDrive\Escritorio\AlDia_Landingpage\diapositivas_analisis_datos_web.html"
with open(html_src, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")
styles_tag = soup.find("style")
styles = str(styles_tag) if styles_tag else ""

slides = soup.find_all("section", class_=lambda c: c and "slide" in c.split())
print(f"BeautifulSoup found {len(slides)} slides.")

# Create printable HTML
printable_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Presentación Oficial Avance 1 - AlDía (PDF)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  {styles}
  <style>
    @page {{
      size: 16in 9in;
      margin: 0;
    }}
    *, *::before, *::after {{
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
      color-adjust: exact !important;
    }}
    html, body {{
      margin: 0;
      padding: 0;
      background: #FFF6E0 !important;
      width: 16in;
      font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
    }}
    .print-slide-page {{
      width: 16in;
      height: 9in;
      page-break-after: always;
      page-break-inside: avoid;
      break-after: page;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 0.35in 0.55in;
      box-sizing: border-box;
      background: #FFF6E0 !important;
    }}
    .slide {{
      position: relative !important;
      display: flex !important;
      opacity: 1 !important;
      visibility: visible !important;
      transform: none !important;
      width: 100% !important;
      height: 100% !important;
      border-radius: 18px !important;
      box-shadow: none !important;
      background: #FFFFFF !important;
      border: 2px solid #0F3D2E !important;
      box-sizing: border-box !important;
      padding: 1.8rem 2.4rem !important;
    }}
    .slide[data-slide="1"] {{
      background: #FFD54A !important;
      border: 3px solid #0F3D2E !important;
    }}
    .slide::before {{
      display: none !important;
    }}
    .nav-arrow, .top-toolbar, .speaker-drawer, .progress-bar-container {{
      display: none !important;
    }}
  </style>
</head>
<body class="theme-aldia">
"""

for i, s in enumerate(slides, 1):
    s_classes = s.get("class", [])
    if "active" in s_classes:
        s_classes.remove("active")
    s["class"] = s_classes
    printable_html += f'  <div class="print-slide-page">\n    {str(s)}\n  </div>\n'

printable_html += """</body>
</html>
"""

print_html_path = r"c:\Users\Drewg\OneDrive\Escritorio\AlDia_Landingpage\presentacion_imprimible.html"
with open(print_html_path, "w", encoding="utf-8") as f:
    f.write(printable_html)

print("Saved presentacion_imprimible.html with all 10 slides.")

# Export to PDF using Edge Headless
pdf_out_path = r"C:\Users\Drewg\OneDrive\Escritorio\AlDia_Landingpage\Presentacion_Avance1_Analisis_Datos_Web.pdf"
edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

cmd = [
    edge_exe,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    f"--print-to-pdf={pdf_out_path}",
    "--print-to-pdf-no-header",
    "http://localhost:8000/presentacion_imprimible.html"
]

print("Executing Edge headless to generate PDF...")
res = subprocess.run(cmd, capture_output=True, text=True)
print(f"Edge exited with code: {res.returncode}")

# Verify with PyMuPDF
if os.path.exists(pdf_out_path):
    doc = pymupdf.open(pdf_out_path)
    print(f"SUCCESS! Generated PDF: {pdf_out_path}")
    print(f"Total Pages: {len(doc)}")
    for i in range(len(doc)):
        page = doc[i]
        print(f"Page {i+1} rect: {page.rect}")
else:
    print("PDF was not created!")