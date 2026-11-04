# Guía de Seguimiento y Métricas con Google (Site Kit / Analytics / Tag Manager) para AlDía

Esta landing page ha sido estructurada y programada con un sistema completo de **seguimiento de interacciones de usuarios** para que puedas medir con exactitud cómo reaccionan los interesados, dueños de bodegas y minimarkets al producto **AlDía**.

---

## 🎯 ¿Qué interacciones se rastrean automáticamente?

El archivo [`analytics.js`](analytics.js) y [`app.js`](app.js) capturan cada micro-interacción y las envían tanto a la capa de datos de Google (`window.dataLayer`) como a Google Analytics 4 (`gtag`):

| Nombre del Evento | ¿Cuándo se activa? | Datos que envía |
| :--- | :--- | :--- |
| `generate_lead` | Cuando el usuario completa y envía el formulario de prueba gratis. | `lead_business_type`, `lead_city`, `lead_source` |
| `phone_demo_interacted` | Al interactuar con el celular demo (tarjetas de Canje, Remate, o botón "¿Aún te queda stock?"). | `action`, `card_type`, `state` |
| `calculator_slider_adjusted` | Cuando el usuario mueve la barra de compras mensuales para ver cuánto dinero salvará. | `biz_type`, `sales_volume`, `monthly_saved` |
| `calculator_biz_change` | Cuando cambia entre Bodega, Minimarket o Ferretería. | `biz_type`, `sales_volume` |
| `calc_cta_clicked` | Al presionar "Salvar esta plata en mi negocio" desde la calculadora. | `biz_type`, `saved_value` |
| `faq_opened` | Al desplegar una duda frecuente en el acordeón de preguntas. | `question` |
| `whatsapp_floating_clicked` | Al hacer clic en el botón flotante de WhatsApp. | `source: 'floating_button'` |
| `scroll_depth` | Al hacer scroll y pasar hitos de la página (25%, 50%, 75%, 90%). | `percent_scrolled` |
| `user_time_on_page` | Tiempo de lectura real (activado a los 30s, 60s y 120s). | `seconds_spent` |

---

## 🚀 Cómo activar tu cuenta de Google Analytics 4 (GA4)

1. Ingresa a [analytics.google.com](https://analytics.google.com/) con tu cuenta de Google.
2. Crea una propiedad para **AlDía Landing Page** y añade un flujo de datos web (Web Stream).
3. Google te dará un **ID de medición**, que tiene este formato: `G-XXXXXXXXXX`.
4. Abre el archivo [`analytics.js`](analytics.js) en la línea 13:
   ```javascript
   const GA_MEASUREMENT_ID = 'G-XXXXXXXXXX'; // <- Pega aquí tu código real
   ```
5. ¡Listo! Todo el sistema cargará automáticamente las etiquetas oficiales de Google y empezará a enviar los datos.

---

## 🔍 Si usas WordPress con "Google Site Kit"

Si planeas subir esta landing page dentro de un sitio en WordPress donde tienes instalado el plugin oficial **Site Kit by Google**:
1. El plugin Site Kit inyecta automáticamente la etiqueta general de GA4 en el `<head>`.
2. Como nuestra landing ya dispara los eventos hacia `window.dataLayer` y `window.gtag`, **Site Kit los detectará de forma nativa** sin necesidad de añadir plugins adicionales.

---

## 🧪 Cómo probar que los eventos están funcionando localmente

1. Abre el archivo [`index.html`](index.html) en tu navegador (Google Chrome, Edge, Brave o Firefox).
2. Abre las herramientas de desarrollador presionando `F12` o clic derecho -> **Inspeccionar**.
3. Selecciona la pestaña **Consola** (Console).
4. Interactúa con la página:
   * Haz clic en las tarjetas del celular (Canje, Remate, Plata Salvada).
   * Mueve el slider de la calculadora.
   * Abre una pregunta de FAQ.
   * Abre el modal y llena el formulario.
5. Verás en la consola los mensajes estilizados de seguimiento en tiempo real:
   ```text
   [AlDía Analytics] phone_demo_interacted { action: 'card_clicked', card_type: 'canje' }
   [AlDía Analytics] calculator_slider_adjusted { sales_volume: '15000', ... }
   [AlDía Analytics] generate_lead { lead_business_type: 'Bodega de barrio', ... }
   ```
6. Cuando conectes tu ID de GA4, estos mismos eventos aparecerán en tiempo real en el panel de **Google Analytics > Informes > Tiempo Real**.

