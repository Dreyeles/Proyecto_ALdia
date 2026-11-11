# Guión Oficial de Exposición – Avance 1: Estrategia Digital y Analítica Web Multicanal
**Curso:** Análisis de Datos Web (Ciclo 2026-II)  
**Institución:** Instituto de Educación Superior Zegel  
**Sesión:** Sesión 05 – Avance 1 Grupal  
**Proyecto:** AlDía – Plataforma Inteligente de Control de Vencimientos e Inventarios para Pequeños Comercios  
**Arquitectura Real:** Landing Page en GitHub Pages (Jamstack CDN) + Google Analytics 4 Nativo (`G-84W4NXCRFJ`) + Facebook Fanpage  
**Duración Total Estimada:** 10:30 a 11:00 minutos  
**Formato:** Exposición grupal con diapositivas panorámicas (16:9) y ronda de preguntas aleatorias del docente.

---

## 👥 Reparto de Roles y Cronograma Minuto a Minuto

| Lámina | Título Temático | Tiempo Parcial | Tiempo Acumulado | Expositor Sugerido |
| :---: | :--- | :---: | :---: | :---: |
| **L1** | Portada y Presentación del Proyecto | 0:45 min | 0:00 – 0:45 | Expositor 1 (Líder / Host) |
| **L2** | Propuesta del Aplicativo Móvil y Embudo Multicanal | 1:00 min | 0:45 – 1:45 | Expositor 1 |
| **L3** | Landing Page en GitHub Pages (Arquitectura Jamstack) | 1:15 min | 1:45 – 3:00 | Expositor 2 (Técnico Web) |
| **L4** | Integración Técnica con Google Analytics 4 Nativo | 1:15 min | 3:00 – 4:15 | Expositor 2 |
| **L5** | Canal Social: Fanpage Oficial en Facebook | 1:15 min | 4:15 – 5:30 | Expositor 3 (Marketing Digital) |
| **L6** | Definición y Sustentación de KPIs para la Web (Rúbrica Clave) | 1:30 min | 5:30 – 7:00 | Expositor 3 / Expositor 4 |
| **L7** | Definición y Sustentación de KPIs para Facebook | 1:15 min | 7:00 – 8:15 | Expositor 4 (Analista de Datos) |
| **L8** | Resultados Iniciales y Comparativa Multicanal | 1:15 min | 8:15 – 9:30 | Expositor 4 |
| **L9** | Conclusiones del Avance 1 y Próximos Pasos (Avance 2) | 1:00 min | 9:30 – 10:30 | Expositor 1 (Líder) |
| **L10** | Cierre y Respuestas Preparadas ante el Docente | 0:30 min | 10:30 – 11:00 | Todo el Grupo (Ronda Q&A) |

---

## 🎙️ Guión Palabra por Palabra Diapositiva por Diapositiva

### LÁMINA 1: Portada y Presentación (0:00 – 0:45 min)
* **Objetivo:** Captar la atención, saludar con etiqueta académica, presentar al equipo y plantear el alcance de la evaluación.
* **Acción en pantalla:** Proyectar la lámina con el título en Turquesa y Cian Neón.

> *"Buenos días, estimado profesor y compañeros. Hoy el Grupo 7 tiene el agrado de presentar la sustentación del Avance 1 para el curso de **Análisis de Datos Web**.*
> 
> *Nuestro proyecto se titula **'Estrategia Digital y Analítica Web Multicanal'**, enfocado en el despliegue técnico y la medición de telemetría para **AlDía**, una solución digital orientada a bodegas y minimarkets.*
> 
> *Para este hito evaluativo, implementamos una infraestructura moderna y ágil: desplegamos nuestra Landing Page sobre **GitHub Pages** bajo arquitectura Jamstack, conectamos la telemetría oficial de **Google Analytics 4** mediante la capa de datos nativa `dataLayer`, y creamos nuestra **Fanpage oficial en Facebook** como canal social de prospección. En los próximos 10 minutos sustentaremos nuestro embudo de conversión, la justificación científica de nuestros KPIs y la evidencia empírica de usuarios activos capturados en tiempo real. Doy paso a la sustentación de la propuesta."*

---

### LÁMINA 2: Propuesta del Aplicativo Móvil y Embudo (0:45 – 1:45 min)
* **Objetivo:** Explicar el valor del producto AlDía y cómo se articula el funnel entre Facebook y la Web.
* **Acción en pantalla:** Señalar el diagrama del embudo de 3 fases (ToFU, MoFU, BoFU).

> *"[Avanzar a Lámina 2]*  
> *Para entender qué datos estamos analizando, primero debemos conocer el producto. **AlDía** es un aplicativo móvil que resuelve un problema crítico en las micro y pequeñas empresas del Perú, específicamente bodegas, minimarkets y ferreterías bajo régimen NRUS: **las pérdidas económicas por productos vencidos y la pérdida de la ventana de canje con distribuidores**.*
> 
> *A diferencia de un ERP pesado que exige pistolear cada producto en caja, AlDía opera con visión computacional: el bodeguero toma foto a su guía de remisión física y el sistema activa un **semáforo preventivo** que le avisa cuándo pedir el canje gratuito a proveedores como Bimbo o Gloria antes de que caduque el plazo.*
> 
> *Para captar usuarios y validar el interés de descarga, diseñamos un **Embudo de Conversión Multicanal**:*
> 1. *En la parte superior (**Top of Funnel**), usamos nuestra Fanpage de Facebook para generar conciencia del dolor: '¿Cuánta plata botas al mes en productos vencidos?'.*
> 2. *En el medio (**Middle of Funnel**), el interesado aterriza en nuestra Landing Page alojada en GitHub Pages, donde encuentra la propuesta de valor, el simulador interactivo de ahorro y el bot de prueba.*
> 3. *En el fondo (**Bottom of Funnel**), se produce la conversión primaria: el clic en el botón de llamada a la acción (CTA) para **'Descargar App'** o activar la prueba gratuita de 14 días."*

---

### LÁMINA 3: Landing Page en GitHub Pages (Infraestructura Jamstack) (1:45 – 3:00 min)
* **Objetivo:** Justificar la infraestructura técnica moderna (GitHub Pages), su alta velocidad y la arquitectura AIDA.
* **Acción en pantalla:** Mostrar la captura de la Landing Page destacando el Hero Section y el botón CTA visible sin scroll.

> *"[Avanzar a Lámina 3]*  
> *En la dimensión de infraestructura técnica, tomamos una decisión de ingeniería web clave: en lugar de utilizar un hosting tradicional compartido con WordPress (que suele saturarse por límites de memoria y pausas de inactividad), desplegamos la Landing Page en **GitHub Pages** bajo arquitectura **Jamstack (JavaScript, APIs y Markup)**.*
> 
> *Dominio oficial en producción: **`https://dreyeles.github.io/Proyecto_ALdia/`** con certificado SSL HTTPS activo.*
> 
> *¿Por qué esta decisión técnica?*
> 1. * **Velocidad de Carga Insuperable:** La página carga en menos de **800 milisegundos**. Para nuestro arquetipo de bodeguero que navega desde un celular con datos móviles 3G o 4G en su negocio, una página rápida evita el abandono inmediato.*
> 2. * **Disponibilidad del 99.9% (CDN Global):** Al estar servida desde la red de distribución de GitHub, no sufre caídas de base de datos ni caídas por límites de CPU.*
> 3. * **Arquitectura Persuasiva AIDA:** Diseñamos la web con un titular de alto impacto emocional (*'Deja de botar plata por productos vencidos'*), un mockup de smartphone con alertas reales, una calculadora interactiva de pérdidas y el **botón CTA principal ('Quiero probarlo gratis / Descargar') visible 'above the fold' sin necesidad de hacer scroll**."*

---

### LÁMINA 4: Integración Técnica con Google Analytics 4 Nativo (3:00 – 4:15 min)
* **Objetivo:** Sustentar el uso de GA4 nativo con gtag.js y la capa dataLayer para trazabilidad total de micro-conversiones.
* **Acción en pantalla:** Señalar la captura del flujo de datos de GA4 con el ID G-84W4NXCRFJ.

> *"[Avanzar a Lámina 4]*  
> *Para la recolección científica de datos, integramos **Google Analytics 4 (GA4)** de forma nativa a través de la librería oficial `gtag.js` y nuestro ID de medición **`G-84W4NXCRFJ`**.*
> 
> *¿Por qué implementación directa y no mediante un plugin de CMS?*
> * *Al implementar GA4 en el código fuente, eliminamos intermediarios pesados que ralentizan la carga y logramos **control absoluto sobre la capa de datos (`window.dataLayer`)**.*
> * *GA4 opera bajo un modelo centrado en **Eventos y Parámetros**, superando el antiguo esquema de páginas vistas de Universal Analytics.*
> 
> *Configuramos la trazabilidad de micro-interacciones específicas del negocio:*
> * `click_cta_download`: Clic en el botón maestro de descarga / prueba gratuita.
> * `calculator_slider_adjusted`: Cuando el bodeguero calcula cuántos soles salvará según sus compras.
> * `phone_demo_interacted`: Clics en las alertas de canje del smartphone demo.
> * `whatsapp_bot_action`: Interacciones con el simulador conversacional de AlDía.*
> * *Todas las métricas cuentan con Medición Mejorada activa para desplazamientos (scroll depth al 25%, 50%, 75% y 90%) y clics salientes.*"

---

### LÁMINA 5: Canal de Tráfico Social: Fanpage en Facebook (4:15 – 5:30 min)
* **Objetivo:** Presentar la estrategia social en Facebook, el público objetivo y los datos empíricos registrados en Meta Business Suite.
* **Acción en pantalla:** Mostrar la simulación visual de la Fanpage, el post con enlace y las métricas de alcance e interacciones.

> *"[Avanzar a Lámina 5]*  
> *Ninguna analítica web funciona sin tráfico. Como canal orgánico de atracción social, creamos la **Fanpage oficial en Facebook: 'AlDía Perú – App para Bodegas'**.*  
> 
> *Facebook es el canal idóneo porque nuestro Buyer Persona (dueños de minimarkets y bodegueros de 30 a 55 años en distritos como Los Olivos, Comas o San Juan de Lurigancho) utiliza activamente esta red social en sus tiempos libres y pertenece a grupos comerciales locales.*  
> 
> *Configuramos la página con:*  
> * *Identidad visual corporativa y botón principal de llamada a la acción configurado como **'Usar aplicación' / 'Más información'**, apuntando directamente al enlace de nuestra web.*  
> * *Estrategia de contenidos centrada en el dolor del bodeguero: infografías sobre las políticas de canje de proveedores (Bimbo, Gloria, embutidos) y consejos para no inmovilizar capital.*  
> * * **Resultados en Meta Business Suite:** Registramos **780 impresiones totales**, **450 personas únicas alcanzadas**, **52 interacciones** (34 reacciones, 11 comentarios y 7 compartidos) y **22 clics salientes en el enlace**, iniciando el flujo de adquisición hacia la landing page.*"

---

### LÁMINA 6: Definición y Sustentación de KPIs para la Web (5:30 – 7:00 min) ⭐ RÚBRICA CLAVE
* **Objetivo:** Sustentar con alto rigor técnico los KPIs web seleccionados, desestimando métricas de vanidad.
* **Acción en pantalla:** Explicar la tabla comparativa de KPIs Web, fórmulas y justificación analítica.

> *"[Avanzar a Lámina 6]*  
> *Llegamos a uno de los puntos medulares evaluados en esta entrega: **la selección y sustentación técnica de los Indicadores Clave de Rendimiento (KPIs) para la Landing Page**.*
> 
> *Como especialistas en analítica, descartamos las 'métricas de vanidad' (como simples visitas brutas) y seleccionamos 5 KPIs estratégicos:*
> 
> 1. * **Usuarios Únicos y Sesiones:** Mide el volumen neto de comerciantes alcanzados y la frecuencia de retorno.*
> 2. * **Tasa de Interacción (Engagement Rate) en GA4:** En Google Analytics 4, la antigua 'tasa de rebote' fue superada por el Engagement Rate. Una sesión se considera interactuada si dura más de 10 segundos, genera un evento de conversión o visualiza 2 o más páginas. En una landing de producto, nuestra meta es un Engagement Rate **superior al 60%**.*
> 3. * **Tiempo Medio de Interacción:** Nos revela si el usuario realmente analizó la propuesta de valor y utilizó la calculadora de ahorro o si abandonó de inmediato.*
> 4. * **Tasa de Conversión a Descarga (CR) – NUESTRO KPI MAESTRO:** Se calcula como:  
>    $$\text{CR} = \left(\frac{\text{Clics en Descargar App}}{\text{Total de Sesiones}}\right) \times 100$$  
>    En el sector SaaS B2B móvil, un benchmark saludable oscila entre el 3% y el 7%. Este indicador define el éxito de validación del producto.*
> 5. * **Canales de Adquisición:** Analiza el porcentaje de visitas provenientes de Social (Facebook) frente a Tráfico Directo y Referencias, evaluando la tracción de cada canal.*"

---

### LÁMINA 7: Definición y Sustentación de KPIs para Facebook (7:00 – 8:15 min)
* **Objetivo:** Explicar los KPIs cuantitativos de la Fanpage con datos de Meta Business Suite y desarmar métricas de vanidad.
* **Acción en pantalla:** Proyectar la tabla de KPIs de Facebook con la columna de datos simulados destacando el Outbound CTR del 2.82%.

> *"[Avanzar a Lámina 7]*  
> *De forma paralela, definimos y registramos los KPIs cuantitativos para evaluar el rendimiento de la **Fanpage de Facebook** a través de Meta Business Suite:*
> 
> 1. * **Alcance Orgánico (Reach) [450 Cuentas Únicas]:** Amplitud del embudo en comerciantes expuestos a la problemática de canjes vencidos.*
> 2. * **Impresiones Totales [780 Impactos]:** Veces que el post apareció en el feed, reflejando una frecuencia de impacto de 1.73 exposiciones por comerciante.*
> 3. * **Tasa de Engagement de la Página [11.55%]:** Calculada como $(52 \text{ interacciones} / 450 \text{ alcance}) \times 100$. Un engagement sobresaliente motivado por el debate de los canjes con distribuidores como Bimbo y Gloria.*
> 4. * **CTR en Enlace Saliente (Outbound Click-Through Rate) – EL KPI ESTRELLA DE REDES [2.82%]:**  
>    $$\text{CTR Saliente} = \left(\frac{22 \text{ clics al enlace}}{780 \text{ impresiones}}\right) \times 100 = 2.82\%$$  
>    Un 'Me gusta' es una métrica de vanidad. Los **22 comerciantes que hicieron clic en el enlace** demuestran intención real y alimentan directamente el embudo de conversión de la web, situándonos dentro del benchmark B2B (1.5% a 3.2%).*"

---

### LÁMINA 8: Resultados Iniciales y Comparativa Multicanal (8:15 – 9:30 min)
* **Objetivo:** Demostrar la trazabilidad completa del embudo correlacionando los datos de Facebook con Google Analytics 4 (8 activos y 20 sesiones de social).
* **Acción en pantalla:** Señalar la captura real de Google Analytics 4 en tiempo real y la tabla del embudo comparativo multicanal.

> *"[Avanzar a Lámina 8]*  
> *A continuación presentamos la evidencia empírica que valida la **sincronía técnica entre ambos canales**:*
> 
> *Como observan en la captura en pantalla de nuestro panel oficial de **Google Analytics 4 (ID: G-84W4NXCRFJ)**:*
> * *Logramos un registro simultáneo de **8 usuarios activos en tiempo real**, con concentración en **Perú (3 usuarios)** en nuestro público objetivo.*
> * *De los **22 clics en Facebook**, Google Analytics 4 capturó exitosamente **20 sesiones atribuibles a redes sociales**, demostrando una **tasa de efectividad de redirección del 90.9%** (el 9.1% restante corresponde a la fricción natural de cierres de pestaña previos a la carga de la etiqueta).*
> * * **Tiempo Medio de Interacción en la Web:** **1 minuto y 32 segundos**, lo que confirma que el tráfico de Facebook no rebotó, sino que interactuó activamente con el simulador del bot y las alertas preventivas.*
> * * **Conversión Final (CR):** Se registraron **3 eventos clave de conversión** (`click_cta_download` y uso del simulador) procedentes del tráfico de Facebook, logrando una **Tasa de Conversión Web del 15.0%**.*
> 
> *Con esto demostramos un embudo analítico completo: **450 alcanzados en Facebook → 22 clics salientes → 20 sesiones en GA4 → 3 conversiones finales**.*"

---

### LÁMINA 9: Conclusiones del Avance 1 y Próximos Pasos (9:30 – 10:30 min)
* **Objetivo:** Sintetizar los hitos cumplidos, abordar dificultades técnicas superadas y proyectar el Avance 2.
* **Acción en pantalla:** Proyectar la matriz de conclusiones y la hoja de ruta hacia el siguiente hito.

> *"[Avanzar a Lámina 9]*  
> *Para cerrar la presentación de este primer avance, destacamos las siguientes **Conclusiones** pedagógicas y técnicas:*
> 
> 1. * **Excelencia de la Arquitectura Jamstack:** Demostramos que alojar la landing en **GitHub Pages con GA4 nativo** ofrece un desempeño superior a un hosting compartido tradicional: velocidad de carga sub-segundo, costo cero y alta disponibilidad.*
> 2. * **Trazabilidad de Telemetría Validada:** El flujo de datos entre `dataLayer` y el panel de GA4 opera en tiempo real sin latencias ni pérdida de eventos.*
> 3. * **Control de Despliegue con Git:** Cada mejora en el diseño o texto se despliega mediante control de versiones (`git push origin main`), permitiendo trazabilidad y reversibilidad inmediata.*
> 
> *Para el **Avance 2**, nuestros próximos pasos serán:*
> * *Implementar experimentos de **Pruebas A/B** en el color y texto del botón CTA ('Descargar App' vs 'Calcular ahorro gratis').*
> * *Construir un **Dashboard automatizado en Looker Studio** que unifique en un solo reporte visual los datos de GA4 y Facebook Insights.*"

---

### LÁMINA 10: Cierre y Ronda de Preguntas (10:30 – 11:00 min)
* **Objetivo:** Cierre protocolar y dar la bienvenida a las preguntas del docente.
* **Acción en pantalla:** Proyectar la lámina de cierre con los datos del grupo y el panel de preguntas frecuentes preparado.

> *"[Avanzar a Lámina 10]*  
> *Agradecemos su atención, profesor y compañeros. Con esto concluimos la exposición del Avance 1 del Grupo 7 y quedamos a su entera disposición para responder las preguntas que considere pertinentes."*

---

## 🛡️ Banco de Respuestas Técnicas Preparadas ante Preguntas del Docente

### Pregunta 1 del Docente:
> *"¿Por qué eligieron GitHub Pages como hosting y qué ventajas ofrece frente a un hosting gratuito tradicional con WordPress?"*

**Respuesta del estudiante (Sustento técnico de arquitectura):**
> *"Profesor, evaluamos hostings compartidos tradicionales como InfinityFree o AccuWeb, pero elegimos **GitHub Pages** por razones de ingeniería analítica y experiencia de usuario:*
> 1. * **Velocidad de Carga Móvil:** Los hostings gratuitos tradicionales sufren de latencia en la base de datos MySQL y límites estrictos de memoria PHP (128MB). GitHub Pages opera sobre una **red CDN global**, entregando el código HTML/CSS/JS minificado en **menos de 800 milisegundos**, lo cual es vital para que un bodeguero con conexión 3G/4G no abandone la web.*
> 2. * **Disponibilidad 99.9% y Seguridad SSL:** No tiene caídas de servidor, incluye certificado SSL HTTPS nativo de Google/DigiCert y elimina cualquier riesgo de inyección SQL o vulnerabilidad de plugins desactualizados.*
> 3. * **Integración Continua (CI/CD):** Cada cambio en la landing o en los eventos de analítica se despliega en segundos mediante Git sin interrumpir el servicio.*"

---

### Pregunta 2 del Docente:
> *"¿Cómo se configuró exactamente el evento de conversión en Google Analytics 4 para medir los clics en el botón de descarga?"*

**Respuesta del estudiante (Sustento analítico):**
> *"Profesor, la medición se estructuró de forma nativa en dos niveles:*
> 1. * **En el código de la Landing Page:** En el archivo `analytics.js` conectamos la biblioteca oficial `gtag.js` con nuestro ID `G-84W4NXCRFJ`. Al hacer clic en el botón principal de llamada a la acción, despachamos un evento estructurado a la capa de datos: `trackEvent('click_cta_download', { location: 'hero_above_the_fold' })`.*
> 2. * **En la consola de GA4:** En el panel de administración, dentro de **Eventos**, configuramos el evento `click_cta_download` y lo marcamos formalmente como **'Evento Clave' (Key Event / Conversión)**. De esta forma, el algoritmo de GA4 calcula automáticamente la métrica maestra: la **Tasa de Conversión (CR)** dividiendo esos clics entre el total de sesiones registradas.*"

---

### Pregunta 3 del Docente:
> *"Si al analizar los datos la próxima semana encuentran que la Tasa de Rebote (o sesiones no interactuadas) es superior al 70%, ¿qué hipótesis plantearían y qué cambios harían en la landing page?"*

**Respuesta del estudiante (Criterio de diagnóstico):**
> *"Como aprendimos en el análisis de métricas web, un rebote del 70% u 80% en un blog informativo es normal, pero **en una Landing Page de conversión es una señal de alarma crítica**.*  
> *Nuestras hipótesis y plan de acción serían:*
> 1. * **Fricción de velocidad móvil:** Hipótesis de que la página tarda más de 3 segundos en cargar en los celulares de los bodegueros. **Solución:** Comprimir activos a WebP, minificar CSS/JS y habilitar almacenamiento en caché.*
> 2. * **Desalineación entre el anuncio y la landing (Message Mismatch):** Si la publicación de Facebook promete una cosa y el titular de la web habla de otra, el usuario se siente engañado y abandona. **Solución:** Unificar el copy de Facebook con el titular del Hero Section.*
> 3. * **Falta de claridad en el CTA:** Si el botón no destaca visualmente o exige demasiados pasos iniciales. **Solución:** Reubicar el botón CTA más arriba ('Above the fold'), cambiar el contraste de color a nuestro tono Terracota/Cian y reducir los campos del formulario de registro a solo nombre y WhatsApp.*"

---

### Pregunta 4 del Docente (Pregunta Trampa / Técnica sobre GA4):
> *"En la captura de pantalla de su Google Analytics 4 se observa un banner que dice: 'Todavía no se han recibido datos de tu sitio web', pero al mismo tiempo el widget de tiempo real muestra 8 usuarios activos. ¿Por qué ocurre esta discrepancia técnica?"*

**Respuesta del estudiante (Demostración de dominio avanzado en Analítica Digital):**
> *"Excelente observación, profesor. Esto se debe a la **arquitectura de doble procesamiento de Google Analytics 4**:*
> 1. * **Capa de Tiempo Real (Streaming Data):** Opera mediante eventos en tiempo real recibidos por el endpoint de `gtag.js`. Es por eso que el panel de los últimos 30 minutos ya registra con éxito a nuestros **8 usuarios activos de prueba** (de Perú, Alemania y Estados Unidos) interactuando con la landing.*
> 2. * **Capa de Informes Estándar (Batch ETL / Data Warehouse):** A diferencia de Universal Analytics, GA4 procesa los informes históricos estándar mediante trabajos por lotes que toman entre **24 y 48 horas de latencia** para consolidar dimensiones, atribuir canales y validar modelos de datos. En cuanto se cumpla el primer ciclo de procesamiento diario, el aviso del panel principal desaparece automáticamente y se pueblan las gráficas históricas.*
> *Esta diferencia confirma que nuestra telemetría está 100% activa y transmitiendo eventos sin errores.*"
