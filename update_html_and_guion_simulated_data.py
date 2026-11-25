import re

html_path = r"c:\Users\Drewg\OneDrive\Escritorio\AlDia_Landingpage\diapositivas_analisis_datos_web.html"
with open(html_path, "r", encoding="utf-8") as f:
    html_code = f.read()

# 1. Update Slide 5 in HTML
old_s5_target = """              <div style="display: flex; justify-content: space-between; font-size: 0.78rem; color: var(--text-dim);">
                <span>👥 Objetivo: Prospección ToFU</span>
                <span>📈 Medición: Meta Business Suite</span>
              </div>"""

new_s5_replacement = """              <div style="background: rgba(15, 61, 46, 0.06); border: 1px solid var(--border-card); border-radius: 8px; padding: 0.5rem 0.8rem; margin-bottom: 0.8rem; font-size: 0.78rem;">
                <strong style="color: var(--accent-coral);">📊 Métricas del Post (Meta Business Suite):</strong>
                <div style="display: flex; justify-content: space-between; margin-top: 0.35rem; color: var(--text-main); font-weight: 700;">
                  <span>👁️ 780 Impresiones</span>
                  <span>👥 450 Alcance</span>
                  <span>💬 52 Interacciones</span>
                  <span style="color: var(--accent-coral);">🔗 22 Clics Enlace (CTR 2.82%)</span>
                </div>
              </div>
              <div style="display: flex; justify-content: space-between; font-size: 0.78rem; color: var(--text-dim);">
                <span>👥 Objetivo: Prospección ToFU</span>
                <span>📈 Medición: Meta Business Suite</span>
              </div>"""

if old_s5_target in html_code:
    html_code = html_code.replace(old_s5_target, new_s5_replacement)
    print("Updated Slide 5 in HTML")
else:
    print("Could not find Slide 5 target in HTML")

# 2. Update Slide 7 in HTML
old_s7_table = """            <table class="kpi-table" style="height: 100%;">
              <thead>
                <tr>
                  <th>KPI en Redes</th>
                  <th>Definición / Cálculo</th>
                  <th>Objetivo Analítico</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Alcance (Reach)</strong></td>
                  <td>Cuentas únicas que visualizaron los posts.</td>
                  <td>Evaluar amplitud del embudo en la fase de descubrimiento (ToFU).</td>
                </tr>
                <tr>
                  <td><strong>Impresiones</strong></td>
                  <td>Exposiciones totales de las publicaciones.</td>
                  <td>Medir frecuencia de repetición del mensaje en el público objetivo.</td>
                </tr>
                <tr>
                  <td><strong>Tasa de Engagement</strong></td>
                  <td><span class="formula-tag">(Interacciones / Alcance) * 100</span></td>
                  <td>Detectar si la problemática de productos vencidos genera empatía y debate.</td>
                </tr>
                <tr style="background: rgba(56, 189, 248, 0.08);">
                  <td>
                    <span class="kpi-star" style="background: rgba(56, 189, 248, 0.2); color: #38bdf8; border-color: #38bdf8;">⭐ KPI CLAVE</span><br>
                    <strong style="color: #38bdf8;">CTR en Enlace Saliente</strong>
                  </td>
                  <td>
                    <span class="formula-tag">
                      (Clics al Sitio Web / Impresiones) * 100
                    </span>
                  </td>
                  <td><strong>El puente multicanal:</strong> un "like" no descarga la app; el clic saliente demuestra intención real.</td>
                </tr>
              </tbody>
            </table>"""

new_s7_table = """            <table class="kpi-table" style="height: 100%;">
              <thead>
                <tr>
                  <th style="width: 25%;">KPI Facebook</th>
                  <th style="width: 28%;">Definición / Cálculo</th>
                  <th style="width: 22%;">Dato Registrado</th>
                  <th style="width: 25%;">Objetivo Analítico</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Alcance (Reach)</strong></td>
                  <td>Cuentas únicas que visualizaron los posts.</td>
                  <td><strong style="color: var(--text-main);">450 cuentas</strong></td>
                  <td>Amplitud inicial del embudo (ToFU).</td>
                </tr>
                <tr>
                  <td><strong>Impresiones</strong></td>
                  <td>Exposiciones totales de las publicaciones.</td>
                  <td><strong style="color: var(--text-main);">780 impactos</strong> (1.73x)</td>
                  <td>Frecuencia del mensaje en bodegas.</td>
                </tr>
                <tr>
                  <td><strong>Tasa de Engagement</strong></td>
                  <td><span class="formula-tag">(52 interacc. / 450) * 100</span></td>
                  <td><strong style="color: var(--accent-coral);">11.55%</strong></td>
                  <td>Interés y comentarios en comerciantes.</td>
                </tr>
                <tr style="background: rgba(201, 58, 34, 0.08);">
                  <td>
                    <span class="kpi-star" style="background: rgba(201, 58, 34, 0.2); color: var(--accent-coral); border-color: var(--accent-coral);">⭐ KPI CLAVE</span><br>
                    <strong style="color: var(--accent-coral);">CTR Enlace Saliente</strong>
                  </td>
                  <td>
                    <span class="formula-tag">
                      (22 clics / 780 impr.) * 100
                    </span>
                  </td>
                  <td><strong style="color: var(--accent-coral); font-size: 0.95rem;">2.82%</strong> (22 clics)</td>
                  <td><strong>Puente Multicanal:</strong> visitas enviadas a GitHub Pages.</td>
                </tr>
              </tbody>
            </table>"""

if old_s7_table in html_code:
    html_code = html_code.replace(old_s7_table, new_s7_table)
    print("Updated Slide 7 in HTML")
else:
    print("Could not find Slide 7 target in HTML")

# 3. Update Slide 8 in HTML
old_s8_block = """            <!-- Síntesis de Métricas Registradas -->
            <div style="display: flex; flex-direction: column; gap: 0.9rem;">
              <div class="content-box">
                <div class="box-title">📊 Datos Registrados en la Prueba Inicial</div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.6rem; font-size: 0.82rem;">
                  <div style="background: rgba(3, 13, 18, 0.6); padding: 0.5rem; border-radius: 6px; border: 1px solid var(--border-card);">
                    <div style="color: var(--cyan-neon); font-size: 1.25rem; font-weight: 900;">8</div>
                    <div style="color: var(--text-muted);">Usuarios en Tiempo Real</div>
                  </div>
                  <div style="background: rgba(3, 13, 18, 0.6); padding: 0.5rem; border-radius: 6px; border: 1px solid var(--border-card);">
                    <div style="color: #38bdf8; font-size: 1.25rem; font-weight: 900;">38%</div>
                    <div style="color: var(--text-muted);">Tráfico Perú (Target)</div>
                  </div>
                  <div style="background: rgba(3, 13, 18, 0.6); padding: 0.5rem; border-radius: 6px; border: 1px solid var(--border-card);">
                    <div style="color: var(--accent-amber); font-size: 1.25rem; font-weight: 900;">1m 32s</div>
                    <div style="color: var(--text-muted);">Permanencia Media</div>
                  </div>
                  <div style="background: rgba(3, 13, 18, 0.6); padding: 0.5rem; border-radius: 6px; border: 1px solid var(--border-card);">
                    <div style="color: #4ade80; font-size: 1.25rem; font-weight: 900;">4</div>
                    <div style="color: var(--text-muted);">Pruebas Bot Simulador</div>
                  </div>
                </div>
              </div>

              <div class="content-box highlight">
                <div class="box-title">🔄 Análisis Comparativo Multicanal</div>
                <ul class="feature-list" style="font-size: 0.82rem;">
                  <li class="feature-item">
                    <span class="icon">🔹</span>
                    <span><strong>Facebook:</strong> Cumplió su rol de atracción masiva de bajo costo generando el 40% del flujo de entrada inicial.</span>
                  </li>
                  <li class="feature-item">
                    <span class="icon">🔹</span>
                    <span><strong>Landing Page:</strong> Retuvo la atención técnica; los usuarios dedicaron más de 1 minuto a interactuar con las alertas y la calculadora.</span>
                  </li>
                </ul>
              </div>
            </div>"""

new_s8_block = """            <!-- Síntesis de Métricas Registradas y Comparativa -->
            <div style="display: flex; flex-direction: column; gap: 0.8rem;">
              <div class="content-box">
                <div class="box-title">📊 Evidencia GA4 + Meta Business Suite</div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; font-size: 0.8rem;">
                  <div style="background: rgba(15, 61, 46, 0.05); padding: 0.45rem; border-radius: 6px; border: 1px solid var(--border-card);">
                    <div style="color: var(--cyan-neon); font-size: 1.15rem; font-weight: 900;">8 Activos</div>
                    <div style="color: var(--text-muted); font-size: 0.74rem;">GA4 Real-Time (3 Perú - Target)</div>
                  </div>
                  <div style="background: rgba(15, 61, 46, 0.05); padding: 0.45rem; border-radius: 6px; border: 1px solid var(--border-card);">
                    <div style="color: var(--accent-coral); font-size: 1.15rem; font-weight: 900;">20 Sesiones</div>
                    <div style="color: var(--text-muted); font-size: 0.74rem;">De 22 clics Facebook (90.9% efect.)</div>
                  </div>
                  <div style="background: rgba(15, 61, 46, 0.05); padding: 0.45rem; border-radius: 6px; border: 1px solid var(--border-card);">
                    <div style="color: var(--accent-amber); font-size: 1.15rem; font-weight: 900;">1m 32s</div>
                    <div style="color: var(--text-muted); font-size: 0.74rem;">Permanencia Media en Web</div>
                  </div>
                  <div style="background: rgba(15, 61, 46, 0.05); padding: 0.45rem; border-radius: 6px; border: 1px solid var(--border-card);">
                    <div style="color: #16a34a; font-size: 1.15rem; font-weight: 900;">15.0% CR ⭐</div>
                    <div style="color: var(--text-muted); font-size: 0.74rem;">3 Conversiones CTA de Tráfico Social</div>
                  </div>
                </div>
              </div>

              <div class="content-box highlight">
                <div class="box-title">🔄 Embudo Comparativo Multicanal (Funnel)</div>
                <div style="font-size: 0.78rem; display: flex; flex-direction: column; gap: 0.35rem; color: var(--text-main);">
                  <div><strong>1. ToFU (Facebook):</strong> 780 Impresiones → 450 Cuentas Alcanzadas (11.55% Engagement).</div>
                  <div><strong>2. Tráfico Saliente:</strong> 22 Clics en Enlace (2.82% CTR) hacia GitHub Pages.</div>
                  <div><strong>3. MoFU (Landing GA4):</strong> 20 Sesiones registradas con 1m 32s de permanencia.</div>
                  <div><strong>4. BoFU (Conversión Web):</strong> 3 Conversiones en Botón CTA / Simulador (15.0% CR).</div>
                </div>
              </div>
            </div>"""

if old_s8_block in html_code:
    html_code = html_code.replace(old_s8_block, new_s8_block)
    print("Updated Slide 8 in HTML")
else:
    print("Could not find Slide 8 target in HTML")

# 4. Update Speaker Notes Drawer in HTML for Slide 7 & 8
old_notes_s7 = """          <p>1. <strong>Alcance Orgánico:</strong> Cuentas únicas que visualizaron los posts en su feed.<br>
          2. <strong>Impresiones Totales:</strong> Frecuencia total de exposición de las piezas gráficas.<br>
          3. <strong>Tasa de Engagement:</strong> (Interacciones / Alcance) * 100.<br>
          4. <strong>CTR en Enlace Saliente (Outbound Click-Through Rate) – EL KPI ESTRELLA:</strong> (Clics al sitio web / Impresiones) * 100.</p>
          <p>Un 'Me gusta' en un post es una métrica de vanidad que no genera ingresos. El CTR saliente es el indicador que valida si Facebook cumple su rol de empujar al usuario a la web para descargar la aplicación."</p>"""

new_notes_s7 = """          <p>1. <strong>Alcance Orgánico:</strong> 450 cuentas únicas alcanzadas en grupos de bodegueros y minimarkets.<br>
          2. <strong>Impresiones Totales:</strong> 780 impactos (frecuencia promedio de 1.73x).<br>
          3. <strong>Tasa de Engagement:</strong> 11.55% (52 interacciones totales: 34 likes, 11 comentarios y 7 compartidos).<br>
          4. <strong>CTR en Enlace Saliente (Outbound CTR) – EL KPI ESTRELLA:</strong> 2.82% con 22 clics directos hacia la landing page.</p>
          <p>Un 'Me gusta' es una métrica de vanidad. Los 22 comerciantes que hicieron clic son los que demuestran interés genuino y alimentan la base de conversión de la web."</p>"""

old_notes_s8 = """          • Al contrastar ambos canales: Facebook demostró alta capacidad de atracción inicial, mientras que la Landing Page concentró el tiempo de análisis (sesiones promedio superiores a 1 minuto y medio). El 40% del tráfico inicial provino de enlaces de prueba derivados de redes sociales."</p>"""

new_notes_s8 = """          • Al contrastar ambos canales: De los 22 clics generados en Facebook, Google Analytics 4 registró con precisión 20 sesiones en la web (una efectividad de redirección del 90.9%).<br>
          • Los usuarios dedicaron una media de 1m 32s explorando el simulador de vencimientos y 3 de ellos completaron la conversión haciendo clic en el CTA de descarga, logrando una Tasa de Conversión (CR) de tráfico social del 15.0%."</p>"""

if old_notes_s7 in html_code:
    html_code = html_code.replace(old_notes_s7, new_notes_s7)
    print("Updated Slide 7 Speaker Notes in HTML")

if old_notes_s8 in html_code:
    html_code = html_code.replace(old_notes_s8, new_notes_s8)
    print("Updated Slide 8 Speaker Notes in HTML")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_code)

print("HTML presentation updated successfully!")

