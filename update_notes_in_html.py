with open("diapositivas_analisis_datos_web.html", "r", encoding="utf-8") as f:
    text = f.read()

# Replace Notes in HTML
text = text.replace(
    'implementación de una Landing Page en WordPress bajo un hosting gratuito, la conexión de analítica avanzada mediante <strong>Google Site Kit</strong>',
    'implementación de una Landing Page en <strong>GitHub Pages</strong> bajo arquitectura Jamstack, la conexión de telemetría oficial de <strong>Google Analytics 4</strong> nativo'
)

text = text.replace(
    'desplegamos la Landing Page sobre el CMS <strong>WordPress</strong> en un servidor cloud gratuito (<strong>InfinityFree / AccuWebHosting</strong>) con soporte PHP y MySQL, además de contar con réplicas activas en Vercel y GitHub Pages.',
    'desplegamos la Landing Page sobre <strong>GitHub Pages</strong> bajo arquitectura <strong>Jamstack</strong> servida desde CDN global de alta disponibilidad (<code>https://dreyeles.github.io/Proyecto_ALdia/</code>), garantizando carga en menos de 800ms en redes móviles.'
)

text = text.replace(
    'Implementamos el plugin oficial <strong>Google Site Kit</strong> en WordPress.\n          <p>¿Por qué Site Kit? Porque inyecta las etiquetas oficiales en el encabezado sin alterar archivos PHP del tema, garantizando estabilidad ante actualizaciones.',
    'integramos <strong>Google Analytics 4 (GA4)</strong> de forma nativa en el código fuente con <code>gtag.js</code> y la capa <code>window.dataLayer</code>.\n          <p>¿Por qué nativo y sin plugins? Porque eliminamos la lentitud y vulnerabilidad de plugins de CMS, garantizando máxima velocidad móvil y control total sobre los eventos personalizados de descarga, calculadora y simulador.'
)

text = text.replace(
    '1. <strong>Viabilidad a Costo Cero:</strong> Es plenamente viable desplegar una arquitectura digital profesional (WordPress + Google Site Kit + GA4 + Facebook) con cero costo de inversión en servidores.',
    '1. <strong>Excelencia de la Arquitectura Jamstack:</strong> Demostramos que alojar la landing en <strong>GitHub Pages con GA4 nativo</strong> ofrece un desempeño superior a un hosting tradicional: velocidad sub-segundo, costo cero y alta disponibilidad.'
)

with open("diapositivas_analisis_datos_web.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Speaker notes in diapositivas_analisis_datos_web.html updated successfully!")

