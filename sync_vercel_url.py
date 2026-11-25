import os
import re
import subprocess

files_to_update = [
    r"c:\Users\Drewg\OneDrive\Escritorio\AlDia_Landingpage\diapositivas_analisis_datos_web.html",
    r"c:\Users\Drewg\OneDrive\Escritorio\AlDia_Landingpage\build_pptx.py",
    r"c:\Users\Drewg\OneDrive\Escritorio\AlDia_Landingpage\guion_exposicion_individual_10min.md",
    r"c:\Users\Drewg\OneDrive\Escritorio\AlDia_Landingpage\guion_exposicion_10min.md"
]

old_url = "https://dreyeles.github.io/Proyecto_ALdia/"
new_url = "https://aldia-peru.vercel.app/"

old_url_short = "dreyeles.github.io/Proyecto_ALdia/"
new_url_short = "aldia-peru.vercel.app/"

for file_path in files_to_update:
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace URLs
        updated = content.replace(old_url, new_url)
        updated = updated.replace(old_url_short, new_url_short)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(updated)
        print(f"Updated URLs in {os.path.basename(file_path)}")

# 1. Rebuild PPTX
print("Rebuilding PPTX...")
subprocess.run(["python", r"c:\Users\Drewg\OneDrive\Escritorio\AlDia_Landingpage\build_pptx.py"], check=True)

# 2. Rebuild Presentation PDF
print("Rebuilding Presentation PDF...")
subprocess.run(["python", r"c:\Users\Drewg\OneDrive\Escritorio\AlDia_Landingpage\generate_pdf_presentation.py"], check=True)

# 3. Rebuild Guion PDF
print("Rebuilding Guion PDF...")
subprocess.run(["python", r"c:\Users\Drewg\OneDrive\Escritorio\AlDia_Landingpage\generate_pdf_guion.py"], check=True)

print("All files synchronized with Vercel URL successfully!")
