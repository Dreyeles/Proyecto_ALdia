import os
import subprocess
import mistune
import pymupdf

md_path = r"c:\Users\Drewg\OneDrive\Escritorio\AlDia_Landingpage\guion_exposicion_individual_10min.md"
with open(md_path, "r", encoding="utf-8") as f:
    md_text = f.read()

# Convert markdown to HTML using mistune
html_body = mistune.html(md_text)

doc_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Guión Oficial de Exposición Individual - AlDía (Zegel 2026-II)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <style>
    @page {{
      size: A4;
      margin: 18mm 16mm 18mm 16mm;
    }}
    *, *::before, *::after {{
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
      box-sizing: border-box;
    }}
    body {{
      font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      font-size: 10.5pt;
      line-height: 1.55;
      color: #0F3D2E;
      background: #FFFFFF;
      margin: 0;
      padding: 0;
    }}
    h1 {{
      font-size: 19pt;
      color: #0F3D2E;
      margin-top: 0;
      margin-bottom: 4px;
      border-bottom: 3px solid #FFD54A;
      padding-bottom: 6px;
    }}
    h2 {{
      font-size: 13pt;
      color: #C93A22;
      margin-top: 0;
      margin-bottom: 12px;
    }}
    h3 {{
      font-size: 11.5pt;
      color: #0F3D2E;
      background: #FFF6E0;
      border-left: 4px solid #FFD54A;
      padding: 6px 10px;
      margin-top: 18px;
      margin-bottom: 8px;
      page-break-after: avoid;
    }}
    blockquote {{
      background: #FFFDF8;
      border-left: 4px solid #0F3D2E;
      margin: 8px 0 14px 0;
      padding: 10px 14px;
      border-radius: 0 8px 8px 0;
      font-size: 10pt;
      line-height: 1.55;
      color: #1A382E;
    }}
    blockquote p {{
      margin-bottom: 6px;
    }}
    blockquote p:last-child {{
      margin-bottom: 0;
    }}
    strong {{
      color: #0F3D2E;
      font-weight: 700;
    }}
    em {{
      color: #C93A22;
    }}
    code {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 9pt;
      background: #F1F5F3;
      padding: 2px 5px;
      border-radius: 4px;
      color: #C93A22;
    }}
    pre {{
      background: #0F3D2E;
      color: #FFD54A;
      padding: 10px 14px;
      border-radius: 6px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 8.5pt;
      line-height: 1.4;
      margin: 10px 0;
      page-break-inside: avoid;
    }}
    ul, ol {{
      margin-top: 4px;
      margin-bottom: 10px;
      padding-left: 20px;
    }}
    li {{
      margin-bottom: 4px;
    }}
    hr {{
      border: none;
      border-top: 1px dashed #CBD5E1;
      margin: 16px 0;
    }}
  </style>
</head>
<body>
  {html_body}
</body>
</html>
"""

guion_html_path = r"c:\Users\Drewg\OneDrive\Escritorio\AlDia_Landingpage\guion_imprimible.html"
with open(guion_html_path, "w", encoding="utf-8") as f:
    f.write(doc_html)

guion_pdf_path = r"C:\Users\Drewg\OneDrive\Escritorio\AlDia_Landingpage\Guion_Exposicion_Individual_AlDia.pdf"
edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

cmd = [
    edge_exe,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    f"--print-to-pdf={guion_pdf_path}",
    "--print-to-pdf-no-header",
    "http://localhost:8000/guion_imprimible.html"
]

res = subprocess.run(cmd, capture_output=True, text=True)
print(f"Guion PDF Edge code: {res.returncode}")

if os.path.exists(guion_pdf_path):
    doc = pymupdf.open(guion_pdf_path)
    print(f"SUCCESS! Generated Guion PDF: {guion_pdf_path} ({len(doc)} pages)")
else:
    print("Guion PDF was not created!")