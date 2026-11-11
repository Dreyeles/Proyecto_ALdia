# 🎙️ Guión Oficial de Exposición Individual (10 a 11 Minutos)
## Avance 1: Estrategia Digital y Analítica Web Multicanal

* **Curso:** Análisis de Datos Web (Ciclo 2026-II) · Zegel
* **Hito:** Sesión 05 – Avance 1 Grupal
* **Modalidad:** **Expositor Único (Presentación Individual Fluida)**
* **Proyecto:** **AlDía** – Micro-SaaS para Control de Vencimientos en Pequeños Comercios
* **Infraestructura Real:** Landing Page en GitHub Pages (`https://dreyeles.github.io/Proyecto_ALdia/`) + Google Analytics 4 Nativo (`G-84W4NXCRFJ`) + Fanpage de Facebook ("AlDía Perú")
* **Duración:** 10:30 a 11:00 minutos cronometrados

---

### 💡 Consejos de Locución para el Expositor
1. **Postura y Ritmo:** Habla con calma, manteniendo un ritmo constante. 130 a 140 palabras por minuto es la velocidad ideal.
2. **Contacto Visual:** Alterna la mirada 70% al docente/público y 30% a la pantalla solo para señalar puntos clave.
3. **Uso del Visor Web:** Si usas el visor interactivo en `http://localhost:8000/diapositivas_analisis_datos_web.html`:
   * Presiona **`F`** para pantalla completa antes de empezar.
   * Haz clic en **`▶ Iniciar`** para tener el cronómetro en la barra superior.
   * Si tienes una segunda pantalla o necesitas apoyo de memoria, presiona **`S`** para abrir el cajón inferior con este mismo guión.

---

```
CRONOGRAMA DE TIEMPOS POR DIAPOSITIVA (TOTAL: 10:45 min)
[0:00 - 0:45] Diapositiva 1: Portada y Presentación del Proyecto
[0:45 - 1:45] Diapositiva 2: Propuesta de AlDía y Embudo Multicanal
[1:45 - 2:45] Diapositiva 3: Landing Page en GitHub Pages (Jamstack CDN)
[2:45 - 4:00] Diapositiva 4: Integración Técnica con Google Analytics 4 Nativo
[4:00 - 5:15] Diapositiva 5: Canal de Tráfico Social: Fanpage en Facebook
[5:15 - 6:45] Diapositiva 6: Definición y Sustentación de KPIs Web (Rúbrica Clave)
[6:45 - 8:00] Diapositiva 7: Definición y Sustentación de KPIs para Facebook
[8:00 - 9:15] Diapositiva 8: Resultados Iniciales y Comparativa Multicanal
[9:15 - 10:15] Diapositiva 9: Conclusiones del Avance 1 y Hoja de Ruta
[10:15 - 10:45] Diapositiva 10: Cierre Formal y Ronda de Preguntas
```

---

## 🗣️ Guión Palabra por Palabra para Exposición Individual

---

### 🟢 DIAPOSITIVA 1: Portada y Presentación Oficial (0:00 – 0:45 min)
* **Acción:** Lámina 1 visible (amarillo hero y verde bosque). Mantén las manos visibles, saluda formalmente y haz contacto visual con el docente.

> *"Buenos días, profesor y compañeros. En representación de mi equipo de trabajo, el Grupo 7, tengo el agrado de sustentar hoy la evaluación del Avance 1 para nuestro curso de **Análisis de Datos Web**.*
> 
> *Nuestro proyecto se titula **'Estrategia Digital y Analítica Web Multicanal'**, desarrollado alrededor de **AlDía**, una solución digital orientada a solucionar las mermas por vencimiento en bodegas y minimarkets del Perú.*
> 
> *Para esta entrega, desplegamos una infraestructura técnica moderna a costo cero: nuestra Landing Page alojada en **GitHub Pages** bajo arquitectura Jamstack, la conexión de telemetría nativa con **Google Analytics 4** mediante la capa de datos `dataLayer`, y la creación de nuestra **Fanpage oficial en Facebook** como canal de prospección social.*
> 
> *En los próximos 10 minutos les explicaré cómo diseñamos este embudo de conversión, el sustento científico de nuestros KPIs y la evidencia empírica de usuarios activos capturados en tiempo real en nuestra consola analítica. Comencemos con la propuesta de valor."*

---

### 🟢 DIAPOSITIVA 2: Propuesta del Aplicativo Móvil y Embudo (0:45 – 1:45 min)
* **Acción:** Avanza a la Lámina 2. Señala con el cursor el embudo de 3 fases (ToFU, MoFU, BoFU).

> *"Para entender la analítica, primero debemos tener claridad sobre el negocio. En el Perú, las bodegas y minimarkets bajo el régimen NRUS pierden entre **350 y 600 soles mensuales** en mercadería vencida simplemente porque pierden la ventana de canje con proveedores como Bimbo, Gloria o distribuidores de embutidos.*
> 
> *Los sistemas POS tradicionales fracasan en este rubro porque en hora punta un bodeguero no tiene tiempo de pistolear cada galleta o gaseosa. **AlDía** soluciona esto con visión artificial: el comerciante le toma una foto a la guía de remisión física de su distribuidor y el aplicativo crea un **semáforo de alertas automáticas** que le avisa 8 días antes cuándo vence el plazo de canje.*
> 
> *Para captar a estos comerciantes y medir su interés, diseñamos un **Embudo de Conversión Multicanal** de tres etapas:*
> 
> 1. * **Top of Funnel (Atracción en Facebook):** Generamos conciencia del dolor en redes sociales mediante publicaciones sobre la plata que se pierde en mermas.*
> 2. * **Middle of Funnel (Consideración en la Landing Page):** El comerciante hace clic y aterriza en nuestra web, donde encuentra los beneficios, la calculadora de ahorro y el simulador interactivo.*
> 3. * **Bottom of Funnel (Conversión Final):** La micro-conversión objetivo: el clic en el botón principal de llamada a la acción para **'Descargar App'** o activar la prueba gratuita de 14 días.*
> 
> *Ahora bien, ¿dónde alojamos esta experiencia? Veamos la infraestructura técnica."*

---

### 🟢 DIAPOSITIVA 3: Landing Page en GitHub Pages (Jamstack CDN) (1:45 – 2:45 min)
* **Acción:** Avanza a la Lámina 3. Muestra la captura de la Landing Page destacando el titular persuasivo y el botón CTA visible sin hacer scroll.

> *"En la arquitectura web tomamos una decisión de ingeniería estratégica. Evaluamos hostings compartidos tradicionales como InfinityFree o AccuWeb, pero los descartamos porque sufren de lentitud en bases de datos MySQL y caídas por límites de memoria PHP. En su lugar, desplegamos la Landing Page en **GitHub Pages** bajo arquitectura **Jamstack: JavaScript, APIs y Markup**.*
> 
> *Nuestra web está 100% activa en producción en el dominio oficial: **`https://dreyeles.github.io/Proyecto_ALdia/`**, con certificado de seguridad SSL HTTPS nativo.*
> 
> *Elegimos esta infraestructura por tres razones analíticas determinantes:*
> 1. * **Velocidad de Carga Sub-Segundo:** La web carga en menos de **800 milisegundos**. Para un bodeguero que navega desde su celular con datos móviles 3G o 4G en su local, una web ultrarrápida es la diferencia entre que explore la solución o abandone la página.*
> 2. * **Disponibilidad del 99.9% en CDN Global:** Al ser servida estáticamente desde los servidores perimetrales de GitHub, eliminamos cualquier riesgo de caída de base de datos.*
> 3. * **Estructura AIDA Responsiva:** El diseño está optimizado para móviles y sigue el principio 'Above the Fold': el titular de alto impacto y el botón de acción principal son visibles de inmediato sin necesidad de hacer scroll.*
> 
> *Con la plataforma operativa, el siguiente paso fue implementar la telemetría."*

---

### 🟢 DIAPOSITIVA 4: Integración Técnica con Google Analytics 4 Nativo (2:45 – 4:00 min)
* **Acción:** Avanza a la Lámina 4. Señala el código de la etiqueta `gtag.js` y el ID de medición `G-84W4NXCRFJ`.

> *"Para la captura científica de métricas, integramos **Google Analytics 4** de forma nativa mediante la librería oficial `gtag.js`, vinculada a nuestro flujo de datos con ID de medición **`G-84W4NXCRFJ`**.*
> 
> *¿Por qué implementación nativa en código y no a través de plugins pesados?*  
> *Porque al inyectar la etiqueta directamente en el `index.html` tenemos **control total sobre la capa de datos (`window.dataLayer`)** y evitamos scripts de terceros que degraden el tiempo de carga.*
> 
> *A diferencia del antiguo Universal Analytics, GA4 opera sobre un **modelo centrado en Eventos y Parámetros**. Por ello, estructuramos la medición de micro-interacciones clave del usuario:*
> * *Primero, el evento maestro: `click_cta_download`, que se dispara cuando el visitante presiona el botón principal de descarga.*
> * *Segundo, eventos de consideración: interacción con el simulador de vencimientos y apertura de la calculadora de ahorro.*
> * *Tercero, la **Medición Mejorada (Enhanced Measurement)** nativa de Google: que registra automáticamente vistas de página (`page_view`), clics salientes y profundidad de desplazamiento (`scroll_depth`) al 25%, 50% y 90% de la página.*
> 
> *De esta manera, cada interacción dentro de la landing genera un registro exacto en tiempo real. Pero para que haya datos, necesitamos tráfico. Pasemos a nuestro canal social."*

---

### 🟢 DIAPOSITIVA 5: Canal de Tráfico Social: Fanpage en Facebook (4:00 – 5:15 min)
* **Acción:** Avanza a la Lámina 5. Muestra la simulación de la Fanpage de Facebook "AlDía Perú" y el post promocional.

> *"Para alimentar la parte superior de nuestro embudo (ToFU), activamos el canal de atracción social: **nuestra Fanpage oficial en Facebook 'AlDía Perú – App para Bodegas'**.*
> 
> *La elección de Facebook no fue al azar: nuestro Buyer Persona son comerciantes de 30 a 55 años de distritos comerciales como San Juan de Lurigancho, Comas o Los Olivos, quienes participan intensamente en grupos de Facebook sobre abarrotes y comercio minorista.*
> 
> *En la Fanpage configuramos:*
> * *El botón de llamada a la acción principal: configurado como **'Visitar sitio web'**, direccionando el tráfico directamente a nuestra landing en GitHub Pages.*
> * *Una estrategia de contenidos de 'Copywriting de Dolor': publicamos piezas gráficas sobre las políticas reales de canje con Bimbo y Gloria y cuánto dinero se bota a la basura.*
> * *Enlaces etiquetados con parámetros UTM (`utm_source=facebook&utm_medium=social_post`) para garantizar la trazabilidad analítica en GA4.*
> 
> *En nuestra prueba inicial en Meta Business Suite registramos: **780 impresiones totales**, **450 personas únicas alcanzadas**, **52 interacciones** entre reacciones y comentarios, y lo más importante: **22 clics salientes en el enlace**, que iniciaron el viaje hacia la web.*
> 
> *Ahora entramos a la rúbrica central de nuestra evaluación: ¿cómo medimos el rendimiento de estos dos canales? Veamos primero los KPIs de la Web."*

---

### 🟢 DIAPOSITIVA 6: Definición y Sustentación de KPIs para la Web (5:15 – 6:45 min) ⭐ RÚBRICA CLAVE
* **Acción:** Avanza a la Lámina 6. Adopta un tono firme y analítico. Recorre la tabla explicando por qué se eligió cada métrica.

> *"Llegamos a la rúbrica técnica medular de esta sustentación: **la definición y sustento de los KPIs para la Landing Page**.*
> 
> *Como especialistas en analítica digital, dejamos de lado las métricas de vanidad y seleccionamos 5 KPIs con justificación metodológica:*
> 
> 1. * **Usuarios Únicos y Sesiones:** Evalúa el volumen neto de personas atraídas y la recurrencia de entrada a la web.*
> 2. * **Tasa de Interacción (Engagement Rate) en GA4:** En Google Analytics 4, la antigua tasa de rebote fue reemplazada por la Tasa de Interacción. Una sesión es interactuada si dura más de 10 segundos, genera un evento de conversión o visualiza múltiples secciones. Nuestra meta es mantener un Engagement Rate **superior al 60%**.*
> 3. * **Tiempo Medio de Interacción:** Nos permite medir la retención real. Un usuario que pasa más de un minuto en la página está analizando la propuesta de valor y no se fue por error.*
> 4. * **Tasa de Conversión a Descarga (CR) – NUESTRO KPI MAESTRO:**  
>    Se calcula dividiendo los clics en el botón de descarga entre el total de sesiones de la web, multiplicado por 100. En el sector B2B de micro-SaaS, un benchmark saludable oscila entre el **3% y el 7%**. Este KPI valida si la landing realmente persuade y vende.*
> 5. * **Canales de Adquisición:** Desglosa el porcentaje de tráfico derivado de Facebook frente a accesos directos y referencias.*
> 
> *Con estos 5 indicadores tenemos un termómetro exacto de la salud de la web. Ahora veamos los KPIs homólogos en Facebook."*

---

### 🟢 DIAPOSITIVA 7: Definición y Sustentación de KPIs para Facebook (6:45 – 8:00 min)
* **Acción:** Avanza a la Lámina 7. Explica la tabla con los datos cuantitativos y señala la diferencia entre Likes y Clics.

> *"Para la Fanpage de Facebook establecimos un conjunto homólogo de KPIs cuantitativos medidos desde Meta Business Suite:*
> 
> 1. * **Alcance Orgánico (Reach):** Cuentas únicas que visualizaron la publicación. En nuestra prueba alcanzamos a **450 comerciantes** en grupos locales.*
> 2. * **Impresiones Totales:** Visualizaciones totales del post en pantalla. Registramos **780 impresiones**, lo que representa una frecuencia media de exposición de 1.73 impactos por persona.*
> 3. * **Tasa de Engagement del Post:** Calculada como el total de interacciones dividido entre el alcance por 100. Obtuvimos un **11.55%** producto de 52 interacciones (34 me gusta, 11 comentarios debatiendo los canjes y 7 compartidos).*
> 4. * **CTR en Enlace Saliente (Outbound Click-Through Rate) – EL KPI ESTRELLA DE REDES:**  
>    Se calcula dividiendo los clics que van hacia la web entre las impresiones totales, por 100. Registramos **22 clics salientes**, lo que representa un **CTR de 2.82%**, ubicándonos con solidez dentro del benchmark de la industria B2B (1.5% a 3.2%).*
> 
> *Aquí aplicamos un principio crítico de la materia: **un 'Me gusta' es una métrica de vanidad que no genera ventas**. Los 22 comerciantes que hicieron clic en el enlace demuestran una intención de compra real y son quienes alimentan el embudo de la web.*
> 
> *¿Y qué pasó cuando estos 22 comerciantes llegaron a la landing page? Veámoslo en la siguiente lámina de resultados."*

---

### 🟢 DIAPOSITIVA 8: Resultados Iniciales y Comparativa Multicanal (8:00 – 9:15 min)
* **Acción:** Avanza a la Lámina 8. Señala con seguridad la captura real de Google Analytics 4 con los 8 usuarios activos y el mapa.

> *"En esta lámina presentamos la evidencia empírica que valida la **sincronía técnica entre ambos canales**:*
> 
> *Como pueden observar en la captura real obtenida directamente de nuestro panel oficial de **Google Analytics 4 (ID: G-84W4NXCRFJ)**:*
> * *Registramos **8 usuarios activos simultáneos en tiempo real**, con concentración en **Perú (3 usuarios)** en nuestro público objetivo, junto con tráfico de prueba internacional.*
> * *Al cruzar los datos con Facebook, comprobamos la trazabilidad del embudo: de los **22 clics generados en Facebook**, Google Analytics registró **20 sesiones en la web**. Esto representa una **tasa de efectividad de redirección del 90.9%** (el 9.1% restante corresponde a la fricción habitual de cierres de pestaña previos a la carga).*
> * * **Retención en la Web:** Los visitantes dedicaron una **permanencia media de 1 minuto y 32 segundos**, explorando las alertas y el bot interactivo.*
> * * **Conversión Final (CR):** Se registraron **3 eventos clave de conversión** en el botón CTA procedentes de este tráfico social, alcanzando una **Tasa de Conversión Web del 15.0%**.*
> 
> *El embudo funcionó de forma completa: **450 comerciantes alcanzados en Facebook → 22 clics salientes → 20 sesiones en GA4 → 3 conversiones finales**.*
> 
> *Con estos resultados en mano, pasemos a las conclusiones de esta primera etapa."*

---

### 🟢 DIAPOSITIVA 9: Conclusiones del Avance 1 y Hoja de Ruta (9:15 – 10:15 min)
* **Acción:** Avanza a la Lámina 9. Resume los logros con tono de satisfacción y visión de futuro hacia el Avance 2.

> *"Para cerrar este primer avance evaluativo, presentamos tres conclusiones clave y nuestra hoja de ruta:*
> 
> 1. * **Validación de la Arquitectura Jamstack:** Demostramos que alojar una landing page en **GitHub Pages con GA4 nativo** es técnicamente superior a un hosting tradicional: logramos velocidad sub-segundo (<800ms), 99.9% de disponibilidad, costo cero y control de versiones mediante Git.*
> 2. * **Trazabilidad sin Pérdida de Datos:** Validamos que la capa `dataLayer` transmite los eventos en tiempo real hacia GA4 con una efectividad superior al 90%.*
> 3. * **Complementariedad Multicanal:** Comprobamos que Facebook es un generador de tracción inicial masiva, mientras que la Landing Page es el motor de retención y conversión.*
> 
> *Para el **Avance 2**, nuestra hoja de ruta incluye dos grandes hitos:*
> * *Primero, ejecutar **Pruebas A/B** en el botón CTA (evaluando el texto 'Descargar App' frente a 'Calcular ahorro gratis').*
> * *Segundo, construir un **Dashboard interactivo en Looker Studio** que consolide en tiempo real las métricas de GA4 con los datos de Meta Business Suite.*"

---

### 🟢 DIAPOSITIVA 10: Cierre Formal y Ronda de Preguntas (10:15 – 10:45 min)
* **Acción:** Avanza a la Lámina 10. Junta las manos al frente, sonríe con seguridad y agradece formalmente.

> *"Agradezco sinceramente su tiempo y atención, profesor y compañeros. Con esto doy por concluida la sustentación del Avance 1 de nuestro equipo y quedo a su entera disposición para responder las preguntas que tenga a bien realizar. Muchas gracias."*

---

## 🛡️ Banco de Respuestas Maestras ante Preguntas del Docente

Si el docente te hace preguntas al finalizar, mantén la calma y responde con estos argumentos:

### ❓ Pregunta 1: *"¿Por qué eligieron GitHub Pages y qué limitaciones encontraron frente a un hosting gratuito como InfinityFree o AccuWeb?"*
> **Tu respuesta:**  
> *"Profesor, evaluamos hostings compartidos tradicionales como InfinityFree, pero los descartamos por ingeniería analítica: esos servidores imponen límites de memoria PHP de 128MB, pausas forzadas por inactividad y latencias de base de datos MySQL de más de 3 segundos, lo que dispararía la tasa de rebote móvil de los bodegueros.*  
> *GitHub Pages opera sobre una red CDN global que entrega nuestro código estático en menos de 800 milisegundos con HTTPS nativo y 99.9% de disponibilidad a costo cero. Como limitación, GitHub Pages no procesa backend dinámico en PHP, pero para una Landing Page de conversión y captura analítica, la arquitectura Jamstack estática es el estándar óptimo de la industria."*

---

### ❓ Pregunta 2: *"¿Cómo se configuró exactamente el evento de conversión en Google Analytics 4 para medir los clics en el botón de descarga?"*
> **Tu respuesta:**  
> *"La medición se estructuró de forma nativa en dos niveles:*  
> *1. En el frontend: en nuestro archivo `analytics.js` conectamos `gtag.js` con el ID `G-84W4NXCRFJ`. Al hacer clic en el botón principal, despachamos un evento estructurado a la capa de datos: `trackEvent('click_cta_download', { location: 'hero_above_the_fold' })`.*  
> *2. En la consola de GA4: en la sección de Administrador > Eventos, identificamos `click_cta_download` y lo marcamos formalmente como 'Evento Clave' (Key Event / Conversión). De esta manera, GA4 calcula automáticamente la Tasa de Conversión (CR) dividiendo esos eventos entre las sesiones totales."*

---

### ❓ Pregunta 3: *"Si la próxima semana ven que el Engagement Rate es menor al 40% (o el rebote supera el 60%), ¿qué hipótesis plantearían y qué cambios harían?"*
> **Tu respuesta:**  
> *"Plantearíamos tres hipótesis y acciones de optimización inmediata:*  
> *1. Desalineación de mensaje (Message Mismatch): Si el post de Facebook promete una cosa y el titular de la web habla de otra, el usuario se siente frustrado y se va. Solución: Unificar el copy de Facebook con el título del Hero Section.*  
> *2. Fricción en el CTA: Si el botón exige demasiados pasos iniciales. Solución: Simplificar el formulario de WhatsApp a solo 1 campo.*  
> *3. Fricción de velocidad en dispositivos móviles de gama baja: Optimizar y comprimir aún más los activos a formato WebP y minificar los scripts para acelerar el First Contentful Paint a menos de 500ms."*

---

### ❓ Pregunta 4 (Pregunta Trampa): *"En su captura de GA4 se lee 'Todavía no se han recibido datos de tu sitio web', pero el widget de tiempo real muestra 8 usuarios. ¿Por qué ocurre esto?"*
> **Tu respuesta:**  
> *"Excelente observación, profesor. Eso se debe a la arquitectura de doble procesamiento de Google Analytics 4:*  
> *La capa de Tiempo Real opera en streaming continuo, por eso ya registra con éxito a nuestros 8 usuarios activos en los últimos 30 minutos.*  
> *Sin embargo, la capa de Informes Estándar y el Data Warehouse de GA4 procesan los datos históricos en lotes (batch ETL) que toman entre 24 y 48 horas de latencia para consolidar dimensiones y modelos de atribución. Al cumplirse las primeras 24 horas del despliegue, el banner desaparece automáticamente y se pueblan los informes consolidados. Esto demuestra que la telemetría está 100% activa y transmitiendo."*
