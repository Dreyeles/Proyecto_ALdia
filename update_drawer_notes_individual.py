import re

html_path = r"c:\Users\Drewg\OneDrive\Escritorio\AlDia_Landingpage\diapositivas_analisis_datos_web.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_notes_js = """      const speakerNotes = {
        1: `
          <span class="cue">[Lámina 1: Portada y Presentación · 0:00 - 0:45 min]</span>
          <p>"Buenos días, profesor y compañeros. En representación de mi equipo de trabajo, el Grupo 7, tengo el agrado de sustentar hoy la evaluación del Avance 1 para nuestro curso de <strong>Análisis de Datos Web</strong>.</p>
          <p>Nuestro proyecto se titula <strong>'Estrategia Digital y Analítica Web Multicanal'</strong>, desarrollado alrededor de <strong>AlDía</strong>, una solución digital orientada a solucionar las mermas por vencimiento en bodegas y minimarkets del Perú.</p>
          <p>Para esta entrega, desplegamos una infraestructura técnica moderna a costo cero: nuestra Landing Page alojada en <strong>GitHub Pages</strong> bajo arquitectura Jamstack, la conexión de telemetría nativa con <strong>Google Analytics 4</strong> mediante la capa de datos <code>dataLayer</code>, y la creación de nuestra <strong>Fanpage oficial en Facebook</strong> como canal de prospección social.</p>
          <p>En los próximos 10 minutos les explicaré cómo diseñamos este embudo de conversión, el sustento científico de nuestros KPIs y la evidencia empírica de usuarios activos capturados en tiempo real en nuestra consola analítica. Comencemos con la propuesta de valor."</p>
        `,
        2: `
          <span class="cue">[Lámina 2: Propuesta y Embudo · 0:45 - 1:45 min]</span>
          <p>"Para entender la analítica, primero debemos conocer el negocio. En el Perú, las bodegas y minimarkets bajo el régimen NRUS pierden entre <strong>350 y 600 soles mensuales</strong> en mercadería vencida simplemente porque pierden la ventana de canje con proveedores como Bimbo, Gloria o distribuidores de embutidos.</p>
          <p>Los sistemas POS tradicionales fracasan en este rubro porque en hora punta un bodeguero no tiene tiempo de pistolear cada producto. <strong>AlDía</strong> soluciona esto con visión artificial: el comerciante le toma una foto a la guía de remisión física y el aplicativo crea un <strong>semáforo de alertas automáticas</strong> que le avisa 8 días antes cuándo vence el plazo de canje.</p>
          <p>Para captar a estos comerciantes y medir su interés, diseñamos un <strong>Embudo de Conversión Multicanal</strong> de tres etapas:<br>
          1. <strong>Top of Funnel (Atracción en Facebook):</strong> Generamos conciencia del dolor sobre pérdidas por mermas.<br>
          2. <strong>Middle of Funnel (Consideración en la Landing Page):</strong> Aterrizan en nuestra web en GitHub Pages para explorar la propuesta y la calculadora de ahorro.<br>
          3. <strong>Bottom of Funnel (Conversión Final):</strong> La micro-conversión primaria: el clic en el botón CTA para <strong>'Descargar App'</strong> o activar la prueba gratuita de 14 días."</p>
        `,
        3: `
          <span class="cue">[Lámina 3: Landing Page en GitHub Pages · 1:45 - 2:45 min]</span>
          <p>"En la arquitectura web tomamos una decisión de ingeniería estratégica. Descartamos hostings compartidos tradicionales con WordPress porque sufren de lentitud en bases de datos MySQL y caídas por límites de memoria PHP. En su lugar, desplegamos la Landing Page en <strong>GitHub Pages</strong> bajo arquitectura <strong>Jamstack: JavaScript, APIs y Markup</strong>.</p>
          <p>Nuestra web está 100% activa en producción en el dominio oficial: <strong><code>https://dreyeles.github.io/Proyecto_ALdia/</code></strong> con certificado SSL HTTPS nativo.</p>
          <p>Elegimos esta infraestructura por tres razones determinantes:<br>
          1. <strong>Velocidad Sub-Segundo:</strong> Carga en menos de <strong>800 milisegundos</strong> en redes móviles 3G/4G, evitando el rebote prematuro.<br>
          2. <strong>Disponibilidad del 99.9% en CDN Global:</strong> Sin caídas de base de datos ni límites de CPU.<br>
          3. <strong>Estructura AIDA Responsiva:</strong> Diseño móvil optimizado 'Above the fold': el titular y el botón de acción principal son visibles sin hacer scroll."</p>
        `,
        4: `
          <span class="cue">[Lámina 4: Telemetría con GA4 Nativo · 2:45 - 4:00 min]</span>
          <p>"Para la captura científica de métricas, integramos <strong>Google Analytics 4</strong> de forma nativa mediante la librería oficial <code>gtag.js</code>, vinculada a nuestro flujo con ID de medición <strong><code>G-84W4NXCRFJ</code></strong>.</p>
          <p>Al inyectar la etiqueta directamente en el código fuente, eliminamos intermediarios que ralentizan la web y tenemos <strong>control total sobre la capa de datos (<code>window.dataLayer</code>)</strong>.</p>
          <p>Estructuramos la medición en el modelo de <strong>Eventos y Parámetros</strong> de GA4:<br>
          • <strong>Evento Maestro:</strong> <code>click_cta_download</code>, al presionar el botón de descarga.<br>
          • <strong>Eventos de Consideración:</strong> Interacciones con el simulador de vencimientos y la calculadora de ahorro.<br>
          • <strong>Medición Mejorada (Enhanced Measurement):</strong> Vistas de página, clics salientes y profundidad de desplazamiento (scroll depth al 25%, 50% y 90%)."</p>
        `,
        5: `
          <span class="cue">[Lámina 5: Fanpage en Facebook · 4:00 - 5:15 min]</span>
          <p>"Para alimentar la parte superior de nuestro embudo (ToFU), activamos el canal de atracción social: <strong>nuestra Fanpage oficial en Facebook 'AlDía Perú – App para Bodegas'</strong>.</p>
          <p>Facebook es el canal idóneo porque nuestro Buyer Persona (dueños de bodegas de 30 a 55 años en distritos como SJL, Comas o Los Olivos) participa activamente en grupos de comercio minorista.</p>
          <p>En la Fanpage configuramos el botón CTA <strong>'Visitar sitio web'</strong> hacia GitHub Pages y una estrategia de contenidos sobre el dolor de canjes con proveedores (Bimbo y Gloria) con enlaces UTM.</p>
          <p>En nuestra prueba inicial en Meta Business Suite registramos: <strong>780 impresiones totales</strong>, <strong>450 cuentas alcanzadas</strong>, <strong>52 interacciones</strong> (34 likes, 11 comentarios, 7 compartidos) y <strong>22 clics salientes en el enlace</strong> que iniciaron el tráfico hacia la landing page."</p>
        `,
        6: `
          <span class="cue">[Lámina 6: KPIs de la Web (Rúbrica Clave) · 5:15 - 6:45 min]</span>
          <p>"Llegamos a la rúbrica técnica medular: <strong>la definición y sustento de los KPIs para la Landing Page</strong>. Dejamos de lado métricas de vanidad y seleccionamos 5 KPIs con justificación analítica:</p>
          <p>1. <strong>Usuarios Únicos y Sesiones:</strong> Evalúa el volumen neto de personas atraídas y la recurrencia.<br>
          2. <strong>Tasa de Interacción (Engagement Rate) en GA4:</strong> En GA4 reemplaza al antiguo 'rebote'. Una sesión es interactuada si dura más de 10 segundos, genera un evento de conversión o visita múltiples pantallas. Meta: superar el 60%.<br>
          3. <strong>Tiempo Medio de Interacción:</strong> Mide la retención real del mensaje y uso de la calculadora.<br>
          4. <strong>Tasa de Conversión a Descarga (CR) – NUESTRO KPI MAESTRO:</strong> (Clics en Descargar / Sesiones Totales) * 100. En B2B micro-SaaS el benchmark es de 3% a 7%.<br>
          5. <strong>Canales de Adquisición:</strong> Desglosa el porcentaje de tráfico derivado de Facebook frente a accesos directos."</p>
        `,
        7: `
          <span class="cue">[Lámina 7: KPIs de Facebook · 6:45 - 8:00 min]</span>
          <p>"Para la Fanpage de Facebook establecimos los KPIs cuantitativos homólogos medidos en Meta Business Suite:</p>
          <p>1. <strong>Alcance Orgánico (Reach):</strong> 450 cuentas únicas alcanzadas en grupos comerciales.<br>
          2. <strong>Impresiones Totales:</strong> 780 visualizaciones del post (frecuencia de 1.73 impactos por persona).<br>
          3. <strong>Tasa de Engagement del Post:</strong> 11.55% producto de 52 interacciones debatiendo las mermas.<br>
          4. <strong>CTR en Enlace Saliente (Outbound CTR) – EL KPI ESTRELLA:</strong> 2.82% con 22 clics directos hacia la landing page (dentro del benchmark B2B de 1.5% a 3.2%).</p>
          <p>Aplicamos el principio analítico: un 'Me gusta' es una métrica de vanidad que no genera ingresos. Los 22 comerciantes que hicieron clic en el enlace demuestran intención real y alimentan el embudo de conversión."</p>
        `,
        8: `
          <span class="cue">[Lámina 8: Resultados Iniciales y Comparativa · 8:00 - 9:15 min]</span>
          <p>"Presentamos la evidencia empírica que valida la <strong>sincronía técnica entre ambos canales</strong>:</p>
          <p>• En la captura real de <strong>Google Analytics 4 (ID: G-84W4NXCRFJ)</strong> observan <strong>8 usuarios activos simultáneos en tiempo real</strong>, con 3 usuarios concentrados en Perú dentro de nuestro público objetivo.<br>
          • Al cruzar los datos: de los <strong>22 clics generados en Facebook</strong>, GA4 registró con precisión <strong>20 sesiones en la web</strong> (una efectividad de redirección del 90.9%).<br>
          • <strong>Retención en la Web:</strong> Permanencia media de <strong>1 minuto y 32 segundos</strong> explorando la solución.<br>
          • <strong>Conversión Final (CR):</strong> Se registraron <strong>3 eventos de conversión</strong> en el botón CTA procedentes de este tráfico, logrando una <strong>Tasa de Conversión Web del 15.0%</strong>.<br>
          • El embudo funcionó de punta a punta: 450 alcanzados → 22 clics → 20 sesiones en GA4 → 3 conversiones."</p>
        `,
        9: `
          <span class="cue">[Lámina 9: Conclusiones y Próximos Pasos · 9:15 - 10:15 min]</span>
          <p>"Para cerrar este primer avance evaluativo, presentamos tres conclusiones y nuestra hoja de ruta:</p>
          <p>1. <strong>Validación de la Arquitectura Jamstack:</strong> Alojar en GitHub Pages con GA4 nativo es técnicamente superior a un hosting tradicional: carga sub-segundo (&lt;800ms), 99.9% de disponibilidad, costo cero y despliegue continuo con Git.<br>
          2. <strong>Trazabilidad Validada:</strong> La capa dataLayer transmite los eventos en tiempo real sin latencias ni pérdidas.<br>
          3. <strong>Complementariedad Multicanal:</strong> Facebook atrae el volumen ToFU y la Landing Page retiene y convierte.</p>
          <p>Para el <strong>Avance 2</strong> ejecutaremos <strong>Pruebas A/B</strong> en el botón CTA y construiremos un <strong>Dashboard interactivo en Looker Studio</strong> unificando GA4 con Meta Insights."</p>
        `,
        10: `
          <span class="cue">[Lámina 10: Cierre y Preguntas · 10:15 - 11:00 min]</span>
          <p>"Agradezco sinceramente su tiempo y atención, profesor y compañeros. Con esto doy por concluida la sustentación del Avance 1 de nuestro equipo y quedo a su entera disposición para responder las preguntas que tenga a bien realizar. Muchas gracias."</p>
          <p><em>[Consultar el banco de 4 respuestas técnicas ante preguntas del docente].</em></p>
        `
      };"""

pattern = re.compile(r'const speakerNotes = \{.*?\};', re.DOTALL)
if pattern.search(content):
    content = pattern.sub(new_notes_js, content, count=1)
    print("Replaced speakerNotes in HTML successfully!")
else:
    print("Could not find speakerNotes in HTML!")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

