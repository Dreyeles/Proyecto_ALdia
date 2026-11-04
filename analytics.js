/**
 * ALDÍA - Google Analytics 4, Tag Manager & Google Site Kit Tracking Helper
 * 
 * Este archivo centraliza el envío de eventos de interacción para que puedas
 * visualizarlos en tiempo real en:
 * - Google Analytics 4 (Eventos en tiempo real)
 * - Google Tag Manager (DataLayer events)
 * - Google Site Kit (para métricas de tráfico y conversiones)
 */

// =============================================================================
// CONFIGURACIÓN: ID oficial de Google Analytics 4 vinculado a AlDía
// =============================================================================
const GA_MEASUREMENT_ID = 'G-84W4NXCRFJ';

// Inicialización de dataLayer y gtag seguro
window.dataLayer = window.dataLayer || [];
if (typeof window.gtag !== 'function') {
  window.gtag = function () {
    window.dataLayer.push(arguments);
  };
}

/**
 * Función universal para despachar eventos a GA4 y Google Tag Manager
 * @param {string} eventName - Nombre del evento (ej: 'generate_lead', 'cta_click')
 * @param {object} eventParams - Parámetros adicionales
 */
function trackEvent(eventName, eventParams = {}) {
  const payload = {
    event: eventName,
    timestamp: new Date().toISOString(),
    ...eventParams
  };

  // 1. Enviar a dataLayer (Compatible con Google Tag Manager y Site Kit)
  window.dataLayer.push(payload);

  // 2. Enviar a gtag si está disponible
  if (typeof window.gtag === 'function') {
    window.gtag('event', eventName, eventParams);
  }

  // 3. Logger en consola para que puedas verificar que funciona abriendo F12
  console.log(
    `%c[AlDía Analytics]%c ${eventName}`,
    'background: #0f3d2e; color: #ffd54a; font-weight: bold; padding: 2px 6px; border-radius: 4px;',
    'color: #c93a22; font-weight: bold;',
    eventParams
  );
}

// =============================================================================
// RASTREO AUTOMÁTICO DE INTERACCIONES Y PROFUNDIDAD DE SCROLL
// =============================================================================
document.addEventListener('DOMContentLoaded', () => {
  // 1. Scroll Depth Tracking (25%, 50%, 75%, 90%)
  const scrollMilestones = [25, 50, 75, 90];
  const reachedMilestones = new Set();

  window.addEventListener('scroll', () => {
    const scrollPercent = Math.round(
      ((window.scrollY + window.innerHeight) / document.documentElement.scrollHeight) * 100
    );

    scrollMilestones.forEach(milestone => {
      if (scrollPercent >= milestone && !reachedMilestones.has(milestone)) {
        reachedMilestones.add(milestone);
        trackEvent('scroll_depth', {
          percent_scrolled: milestone
        });
      }
    });
  }, { passive: true });

  // 2. Tiempo de lectura y permanencia
  [30, 60, 120].forEach(seconds => {
    setTimeout(() => {
      trackEvent('user_time_on_page', {
        seconds_spent: seconds
      });
    }, seconds * 1000);
  });
});

// Exportar globalmente
window.trackEvent = trackEvent;

