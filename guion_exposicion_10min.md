# Guión Oficial de Exposición – Avance 1: Estrategia Digital y Analítica Web Multicanal
**Curso:** Análisis de Datos Web (Ciclo 2026-II)  
**Institución:** Instituto de Educación Superior Zegel  
**Sesión:** Sesión 05 – Avance 1 Grupal  
**Proyecto:** AlDía – Plataforma Inteligente de Control de Vencimientos e Inventarios para Pequeños Comercios  
**Duración Total Estimada:** 10:30 a 11:00 minutos  
**Formato:** Exposición grupal con diapositivas panorámicas (16:9) y ronda de preguntas aleatorias del docente.

---

## 👥 Reparto de Roles y Cronograma Minuto a Minuto

| Lámina | Título Temático | Tiempo Parcial | Tiempo Acumulado | Expositor Sugerido |
| :---: | :--- | :---: | :---: | :---: |
| **L1** | Portada y Presentación del Proyecto | 0:45 min | 0:00 – 0:45 | Expositor 1 (Líder / Host) |
| **L2** | Propuesta del Aplicativo Móvil y Embudo Multicanal | 1:00 min | 0:45 – 1:45 | Expositor 1 |
| **L3** | Landing Page en WordPress y Hosting Gratuito | 1:15 min | 1:45 – 3:00 | Expositor 2 (Técnico Web) |
| **L4** | Integración Técnica con Google Site Kit (GA4 & GSC) | 1:15 min | 3:00 – 4:15 | Expositor 2 |
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
> *Nuestro proyecto se titula **'Estrategia Digital y Analítica Web Multicanal'**, enfocado en el despliegue técnico y la medición de telemetría para **AlDía**, una solución digital diseñada para microcomercios.*
> 
> *El alcance de este primer hito comprende la implementación de una Landing Page en WordPress bajo un entorno de hosting gratuito, la conexión de analítica avanzada mediante el plugin oficial **Google Site Kit** enlazando Google Analytics 4 y Google Search Console, y la apertura de una **Fanpage en Facebook** como canal social de atracción. A lo largo de los próximos 10 minutos demostraremos cómo estructuramos el embudo de conversión, qué KPIs hemos seleccionado bajo rigor metodológico y los primeros datos de telemetría recopilados. Doy paso a la sustentación de la propuesta."*

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
> 2. *En el medio (**Middle of Funnel**), el interesado aterriza en nuestra Landing Page, donde encuentra la propuesta de valor, el simulador interactivo y la explicación de beneficios.*
> 3. *En el fondo (**Bottom of Funnel**), se produce la conversión primaria: el clic en el botón de llamada a la acción (CTA) para **'Descargar App'** o activar la prueba gratuita."*

---

### LÁMINA 3: Landing Page en WordPress en Hosting Gratuito (1:45 – 3:00 min)
* **Objetivo:** Justificar la infraestructura técnica, el hosting libre de costo y la arquitectura persuasiva AIDA.
* **Acción en pantalla:** Mostrar la captura de la Landing Page destacando el Hero Section y el botón CTA visible sin scroll.

> *"[Avanzar a Lámina 3]*  
> *Pasando a la infraestructura técnica, cumpliendo con la rúbrica del curso desplegamos la Landing Page sobre el CMS **WordPress**, alojada en un servidor de hosting gratuito (utilizando **InfinityFree / AccuWebHosting**) con soporte PHP y MySQL, además de contar con réplicas activas en Vercel y GitHub Pages.*
> 
> *La arquitectura de la página se diseñó bajo el principio clásico de persuasión **AIDA**:*
> * * **Atención:** En el Hero Section superior, con un titular de alto impacto emocional: *'Deja de botar plata por productos vencidos'* y una píldora orientada al nicho: *'Para bodegas y minimarkets'*.*
> * * **Interés:** Mostrando un mockup fidedigno del smartphone con las alertas de canje y remate preventivo.*
> * * **Deseo:** Mediante una calculadora interactiva de ahorro donde el bodeguero calcula cuántos cientos de soles rescata al mes.*
> * * **Acción:** Ubicando el botón principal **CTA ('Quiero probarlo gratis / Descargar App')** visible inmediatamente en el primer pantallazo, tanto en desktop como en dispositivos móviles, sin necesidad de hacer scroll.*
> 
> *La página es 100% responsiva, optimizada para conexiones móviles 3G y 4G habituales en los comerciantes peruanos."*

---

### LÁMINA 4: Integración Técnica de Analítica con Google Site Kit (3:00 – 4:15 min)
* **Objetivo:** Sustentar el uso de Google Site Kit como conector oficial y la configuración de GA4 y Search Console.
* **Acción en pantalla:** Señalar la captura de WordPress con Site Kit verificado y el flujo de datos de GA4 (ID: G-84W4NXCRFJ).

> *"[Avanzar a Lámina 4]*  
> *Para la recolección científica de datos, la rúbrica exige telemetría oficial. Implementamos el plugin **Google Site Kit**, que es la suite oficial de Google para WordPress.*
> 
> *¿Por qué Site Kit? Porque resuelve la integración técnica con máxima seguridad: inyecta las etiquetas oficiales en el `<head>` sin alterar el código fuente del tema, evitando conflictos tras actualizaciones.*
> 
> *A través de Site Kit conectamos dos herramientas fundamentales:*
> 1. * **Google Analytics 4 (GA4):** Con nuestro ID de medición oficial **`G-84W4NXCRFJ`** y flujo de datos activo. GA4 opera bajo un modelo centrado en **Eventos y Parámetros**, superando el antiguo esquema de páginas vistas de Universal Analytics.*
> 2. * **Google Search Console:** Para monitorear la indexación orgánica, impresiones en el motor de búsqueda y términos de consulta.*
> 
> *Asimismo, configuramos la capa de datos (`window.dataLayer`) para registrar micro-interacciones: cuando un usuario hace clic en el botón de descarga, prueba el simulador o abre el bot, se despacha un evento personalizado con trazabilidad total."*

---

### LÁMINA 5: Canal de Tráfico Social: Fanpage en Facebook (4:15 – 5:30 min)
* **Objetivo:** Presentar la estrategia social, branding de la página y generación de tráfico saliente hacia la web.
* **Acción en pantalla:** Mostrar la captura de la Fanpage de Facebook, foto de perfil, portada y post promocional.

> *"[Avanzar a Lámina 5]*  
> *Ninguna analítica web funciona sin tráfico. Como canal orgánico de atracción social, creamos la **Fanpage oficial en Facebook: 'AlDía Perú – App para Bodegas'**.*
> 
> *Facebook es el canal idóneo porque nuestro Buyer Persona (dueños de minimarkets y bodegueros de 30 a 55 años en zonas como Lima Norte o Lima Este) utiliza activamente esta red social en sus tiempos muertos y pertenece a grupos comerciales locales.*
> 
> *Configuramos la página con:*
> * *Identidad visual corporativa, información de contacto y botón principal de llamada a la acción configurado como **'Usar aplicación' / 'Más información'**, apuntando directamente al dominio de nuestra Landing Page.*
> * *Estrategia de publicaciones enfocada en aportar valor: infografías sobre las políticas de canje de proveedores y videos cortos demostrativos.*
> * *Uso de enlaces rastreables con parámetros UTM para que en Google Analytics podamos diferenciar con exactitud qué publicaciones generaron más visitas y conversiones."*

---

### LÁMINA 6: Definición y Sustentación de KPIs para la Web (5:30 – 7:00 min) ⭐ RÚBRICA CLAVE
* **Objetivo:** Sustentar con alto rigor técnico los KPIs web seleccionados, desestimando métricas de vanidad.
* **Acción en pantalla:** Explicar la tabla comparativa de KPIs Web, fórmulas y justificación analítica.

> *"[Avanzar a Lámina 6]*  
> *Llegamos a uno de los puntos medulares evaluados en esta entrega: **la selección técnica de los Indicadores Clave de Rendimiento (KPIs) para la Landing Page**.*
> 
> *Como especialistas en analítica, descartamos las 'métricas de vanidad' (como simples visitas brutas) y seleccionamos 5 KPIs estratégicos:*
> 
> 1. * **Usuarios Únicos y Sesiones:** Mide el volumen real de comerciantes alcanzados y la frecuencia de retorno.*
> 2. * **Tasa de Interacción (Engagement Rate) en GA4:** En Google Analytics 4, la antigua 'tasa de rebote' fue superada por el Engagement Rate. Una sesión se considera interactuada si dura más de 10 segundos, genera un evento de conversión o visualiza 2 o más páginas. En una landing de producto, nuestra meta es un Engagement Rate **superior al 60%**.*
> 3. * **Tiempo Medio de Interacción:** Nos revela si el usuario realmente leyó la propuesta de valor y utilizó la calculadora de ahorro o si abandonó de inmediato.*
> 4. * **Tasa de Conversión a Descarga (CR) – NUESTRO KPI MAESTRO:** Se calcula como:  
>    $$\text{CR} = \left(\frac{\text{Clics en Descargar App}}{\text{Total de Sesiones}}\right) \times 100$$  
>    En el sector SaaS B2B, un benchmark saludable oscila entre el 3% y el 7%. Este indicador define el éxito financiero del embudo.*
> 5. * **Canales de Adquisición:** Analiza el porcentaje de visitas provenientes de Social (Facebook) frente a Tráfico Directo y Orgánico, evaluando la rentabilidad de cada canal."*

---

### LÁMINA 7: Definición y Sustentación de KPIs para Facebook (7:00 – 8:15 min)
* **Objetivo:** Explicar los KPIs de la Fanpage y diferenciar interacciones superficiales de clics cualificados.
* **Acción en pantalla:** Proyectar la tabla de KPIs de Facebook Insights destacando el Outbound CTR.

> *"[Avanzar a Lámina 7]*  
> *De forma paralela, definimos los KPIs específicos para evaluar el rendimiento de la **Fanpage de Facebook** a través de Meta Business Suite:*
> 
> 1. * **Alcance Orgánico (Reach):** Número de cuentas individuales únicas que visualizaron nuestras publicaciones en su feed.*
> 2. * **Impresiones Totales:** Veces totales que el contenido se mostró en pantalla (mide frecuencia de repetición).*
> 3. * **Tasa de Engagement de la Página:** Calculada como el total de interacciones (reacciones, comentarios y compartidos) dividido entre el alcance total multiplicado por 100. Nos indica si el mensaje conecta con el dolor del bodeguero.*
> 4. * **CTR en Enlace Saliente (Outbound Click-Through Rate) – EL KPI ESTRELLA DE REDES:**  
>    $$\text{CTR Saliente} = \left(\frac{\text{Clics hacia la Landing Page}}{\text{Impresiones del Post}}\right) \times 100$$  
>    Un 'Me gusta' en un post es positivo, pero no descarga la aplicación. El CTR saliente es el indicador que valida si Facebook cumple su rol de empujar al usuario al siguiente nivel del embudo."*

---

### LÁMINA 8: Resultados Iniciales y Comparativa Multicanal (8:15 – 9:30 min)
* **Objetivo:** Mostrar los datos reales capturados en GA4 (8 usuarios activos) y contrastar la efectividad entre canales.
* **Acción en pantalla:** Señalar la captura real de Google Analytics con el panel de tiempo real y distribución geográfica.

> *"[Avanzar a Lámina 8]*  
> *A continuación presentamos la evidencia empírica registrada en nuestras plataformas de telemetría:*
> 
> *Como observan en la captura en pantalla obtenida directamente de nuestro panel oficial de **Google Analytics 4 (ID: G-84W4NXCRFJ)**:*
> * *Logramos un registro de **8 usuarios activos simultáneos en tiempo real**, con concentración en **Perú (3 usuarios)**, además de tráfico de prueba internacional.*
> * *Se registraron eventos automáticos de desplazamiento (`scroll_depth`), interacción con el bot interactivo (`whatsapp_bot_opened`) y visitas al Hero Section.*
> 
> *Al contrastar ambos canales en la **Comparativa Multicanal**:*
> * * **Facebook** demostró alta capacidad de alcance inicial y bajo costo de atracción.*
> * * **La Landing Page** concentró el tiempo de análisis (con sesiones promedio de permanencia superiores a 1 minuto y medio en usuarios que interactuaron con la calculadora).*
> * *El **40% de las sesiones registradas** fueron derivadas directamente desde los enlaces publicados en Facebook y pruebas controladas, confirmando la sincronía del embudo."*

---

### LÁMINA 9: Conclusiones del Avance 1 y Próximos Pasos (9:30 – 10:30 min)
* **Objetivo:** Sintetizar los hitos cumplidos, abordar dificultades técnicas superadas y proyectar el Avance 2.
* **Acción en pantalla:** Proyectar la matriz de conclusiones y la hoja de ruta hacia el siguiente hito.

> *"[Avanzar a Lámina 9]*  
> *Para cerrar la presentación de este primer avance, destacamos las siguientes **Conclusiones** pedagógicas y técnicas:*
> 
> 1. * **Viabilidad de Infraestructura a Costo Cero:** Demostramos que es plenamente viable desplegar una arquitectura digital profesional (WordPress + Google Site Kit + GA4 + Facebook) con costo cero de inversión en servidores, ideal para prototipado ágil.*
> 2. * **Trazabilidad de Telemetría Validada:** El flujo de datos entre la etiqueta web y el panel de GA4 opera sin pérdidas ni latencias.*
> 3. * **Dificultades Superadas:** Los hostings gratuitos presentan limitaciones severas de memoria PHP (Memory Limit de 128MB) y pausas de inactividad. Superamos esto optimizando el peso de las imágenes a formato WebP, evitando plugins pesados innecesarios y manteniendo una réplica estática de respaldo.*
> 
> *Para el **Avance 2**, nuestros próximos pasos serán:*
> * *Implementar experimentos de **Pruebas A/B** en el color y texto del botón CTA.*
> * *Construir un **Dashboard automatizado en Looker Studio** que unifique en un solo reporte visual los datos de GA4 y Facebook Insights."*

---

### LÁMINA 10: Cierre y Ronda de Preguntas (10:30 – 11:00 min)
* **Objetivo:** Cierre protocolar y dar la bienvenida a las preguntas del docente.
* **Acción en pantalla:** Proyectar la lámina de cierre con los datos del grupo y el panel de preguntas frecuentes preparado.

> *"[Avanzar a Lámina 10]*  
> *Agradecemos su atención, profesor y compañeros. Con esto concluimos la exposición del Avance 1 del Grupo 7 y quedamos a su entera disposición para responder las preguntas que considere pertinentes."*

---

## 🛡️ Banco de Respuestas Técnicas Preparadas ante Preguntas del Docente

### Pregunta 1 del Docente:
> *"¿Por qué eligieron ese hosting gratuito y qué limitaciones encontraron al instalar WordPress y Google Site Kit?"*

**Respuesta del estudiante (Sustento técnico):**
> *"Elegimos **InfinityFree / AccuWebHosting** porque ofrece soporte nativo para bases de datos MySQL, versiones modernas de PHP 8.x y compatibilidad con el instalador Softaculous para WordPress, además de no insertar publicidad invasiva en el sitio.*  
> *Entre las limitaciones técnicas más importantes encontramos:*
> 1. * **Límite de memoria PHP y CPU (Resource Limits):** Los servidores gratuitos bloquean procesos que consumen más de 60 segundos de ejecución. Por eso desactivamos cron jobs pesados de WordPress y usamos solo el plugin oficial Google Site Kit.*
> 2. * **Restricciones de cURL y llamadas a APIs externas:** En algunos hostings gratuitos, las llamadas entrantes de Google a veces sufren retardos para autenticar OAuth. Para solventarlo, realizamos la verificación mediante el registro DNS y vinculación directa del ID `G-84W4NXCRFJ`.*
> 3. * **Certificado SSL:** Para asegurar que Google Analytics registre el tráfico bajo protocolo seguro `https://`, activamos el certificado SSL gratuito provisto por el panel de control."*

---

### Pregunta 2 del Docente:
> *"¿Cómo se configuró exactamente el evento de conversión en Google Site Kit o en GA4 para medir los clics en el botón de descarga?"*

**Respuesta del estudiante (Sustento analítico):**
> *"Profesor, la medición se estructuró en dos niveles complementarios:*
> 1. * **A nivel de Google Site Kit:** El plugin inyecta el script global de Google Analytics (`gtag.js`) en todas las páginas de WordPress, lo que activa la **Medición Mejorada (Enhanced Measurement)** para desplazamientos, descargas de archivos y clics de salida.*
> 2. * **A nivel de GA4 personalizado:** Como el botón CTA ('Descargar App / Probar gratis') es un disparador clave en nuestro embudo, le asignamos un identificador y evento en la capa de datos (`dataLayer.push`). En el panel de GA4, ingresamos a **Administrar > Eventos > Crear Evento**, capturando el parámetro `event_name = 'generate_lead'` o `click_cta_download` cuando el `link_url` coincide con la descarga. Finalmente, marcamos ese evento como **'Evento Clave' (Key Event / Conversión)** para que aparezca en el informe de tasa de conversión."*

---

### Pregunta 3 del Docente:
> *"Si al analizar los datos la próxima semana encuentran que la Tasa de Rebote (o sesiones no interactuadas) es superior al 70%, ¿qué hipótesis plantearían y qué cambios harían en la Landing Page?"*

**Respuesta del estudiante (Criterio de diagnóstico):**
> *"Como aprendimos en el análisis de métricas web, un rebote del 70% u 80% en un blog informativo es normal, pero **en una Landing Page de conversión es una señal de alarma crítica**.*  
> *Nuestras hipótesis y plan de acción serían:*
> 1. * **Fricción de velocidad móvil:** Hipótesis de que la página tarda más de 3 segundos en cargar en los celulares de los bodegueros. **Solución:** Comprimir activos, minificar CSS/JS y habilitar almacenamiento en caché.*
> 2. * **Desalineación entre el anuncio y la landing (Message Mismatch):** Si la publicación de Facebook promete una cosa y el titular de la web habla de otra, el usuario se siente engañado y abandona. **Solución:** Unificar el copy de Facebook con el titular del Hero Section.*
> 3. * **Falta de claridad en el CTA:** Si el botón no destaca visualmente o exige demasiados pasos iniciales. **Solución:** Reubicar el botón CTA más arriba ('Above the fold'), cambiar el contraste de color a nuestro tono Terracota/Cian y reducir los campos del formulario de registro a solo nombre y WhatsApp."*
