/**
 * ALDÍA - Core Application Logic
 * Maneja la interactividad del simulador de celular, la calculadora de ahorro,
 * el acordeón de FAQ, el modal de registro y el menú móvil.
 */

document.addEventListener('DOMContentLoaded', () => {
  // ===========================================================================
  // 1. HEADER SCROLL & MOBILE MENU
  // ===========================================================================
  const header = document.querySelector('.site-header');
  const mobileToggle = document.querySelector('.mobile-toggle');
  const navMenu = document.querySelector('.nav-menu');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 30) {
      header.classList.add('is-scrolled');
    } else {
      header.classList.remove('is-scrolled');
    }
  });

  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', () => {
      navMenu.classList.toggle('is-mobile-open');
    });

    // Cerrar al hacer click en un enlace
    navMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('is-mobile-open');
      });
    });
  }

  // ===========================================================================
  // 2. SIMULADOR INTERACTIVO DEL SMARTPHONE (MOCKUP)
  // ===========================================================================
  const phoneBtnStock = document.getElementById('phoneBtnStock');
  const phoneToast = document.getElementById('phoneToast');
  const phoneCards = document.querySelectorAll('.phone-card');

  function showPhoneToast(msg) {
    if (!phoneToast) return;
    phoneToast.textContent = msg;
    phoneToast.classList.add('show');
    setTimeout(() => {
      phoneToast.classList.remove('show');
    }, 2800);
  }

  if (phoneBtnStock) {
    let checkedState = false;
    phoneBtnStock.addEventListener('click', () => {
      checkedState = !checkedState;
      if (checkedState) {
        phoneBtnStock.classList.add('is-checked');
        phoneBtnStock.innerHTML = `✓ ¡Lote Confirmado (3 unids)!`;
        showPhoneToast('✅ Stock auditado en 5 segundos sin frenar la caja.');
      } else {
        phoneBtnStock.classList.remove('is-checked');
        phoneBtnStock.innerHTML = `¿Aún te queda stock?`;
        showPhoneToast('🔄 Pregunta de checklist rápido restablecida.');
      }

      if (window.trackEvent) {
        window.trackEvent('phone_demo_interacted', {
          action: 'stock_button_click',
          state: checkedState ? 'audited' : 'reset'
        });
      }
    });
  }

  phoneCards.forEach(card => {
    card.addEventListener('click', () => {
      const cardType = card.getAttribute('data-card-type') || 'alerta';
      if (cardType === 'canje') {
        showPhoneToast('📦 Solicitud de canje lista para enviar al repartidor.');
      } else if (cardType === 'remate') {
        showPhoneToast('🏷️ Cartel de remate generado: 20% de descuento sugerido.');
      } else if (cardType === 'salvada') {
        showPhoneToast('💰 ¡S/ 480 que no se fueron a la basura este mes!');
      }

      if (window.trackEvent) {
        window.trackEvent('phone_demo_interacted', {
          action: 'card_clicked',
          card_type: cardType
        });
      }
    });
  });

  // ===========================================================================
  // 3. CALCULADORA DINÁMICA DE PLATA SALVADA
  // ===========================================================================
  const bizTypeButtons = document.querySelectorAll('.btn-biz-type');
  const salesSlider = document.getElementById('monthlySalesSlider');
  const salesDisplay = document.getElementById('salesValueDisplay');
  const monthlySavedDisplay = document.getElementById('monthlySavedDisplay');
  const yearlySavedDisplay = document.getElementById('yearlySavedDisplay');
  const btnCalcCta = document.getElementById('btnCalcCta');

  let currentBizFactor = 0.045; // 4.5% de pérdida promedio por vencimientos
  let currentBizName = 'Bodega de barrio';

  function updateCalculation() {
    const salesAmount = parseInt(salesSlider.value, 10);
    salesDisplay.textContent = `S/ ${salesAmount.toLocaleString('es-PE')}`;

    // Pérdida estimada sin AlDía (4.5% - 6% del inventario)
    // AlDía rescata aprox el 85% de esa pérdida mediante canje oportuno y remates
    const estimatedLoss = salesAmount * currentBizFactor;
    const monthlySaved = Math.round(estimatedLoss * 0.85);
    const yearlySaved = monthlySaved * 12;

    monthlySavedDisplay.textContent = `S/ ${monthlySaved.toLocaleString('es-PE')}`;
    yearlySavedDisplay.textContent = `S/ ${yearlySaved.toLocaleString('es-PE')}`;
  }

  bizTypeButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      bizTypeButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      currentBizName = btn.getAttribute('data-biz-name') || 'Comercio';
      currentBizFactor = parseFloat(btn.getAttribute('data-factor')) || 0.045;
      updateCalculation();

      if (window.trackEvent) {
        window.trackEvent('calculator_biz_change', {
          biz_type: currentBizName,
          sales_volume: salesSlider.value
        });
      }
    });
  });

  if (salesSlider) {
    salesSlider.addEventListener('input', () => {
      updateCalculation();
    });

    salesSlider.addEventListener('change', () => {
      if (window.trackEvent) {
        window.trackEvent('calculator_slider_adjusted', {
          biz_type: currentBizName,
          sales_volume: salesSlider.value,
          monthly_saved: monthlySavedDisplay.textContent
        });
      }
    });

    // Iniciar cálculo
    updateCalculation();
  }

  if (btnCalcCta) {
    btnCalcCta.addEventListener('click', () => {
      openLeadModal(`Calculadora: ${currentBizName} - ${monthlySavedDisplay.textContent}/mes`);
      if (window.trackEvent) {
        window.trackEvent('calc_cta_clicked', {
          biz_type: currentBizName,
          saved_value: monthlySavedDisplay.textContent
        });
      }
    });
  }

  // ===========================================================================
  // 4. ACORDEÓN DE PREGUNTAS FRECUENTES (FAQ)
  // ===========================================================================
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach(item => {
    const questionBtn = item.querySelector('.faq-question');
    questionBtn.addEventListener('click', () => {
      const isOpen = item.classList.contains('is-open');

      // Cerrar otros para mantener limpieza
      faqItems.forEach(otherItem => otherItem.classList.remove('is-open'));

      if (!isOpen) {
        item.classList.add('is-open');
        const questionText = questionBtn.querySelector('span').textContent;

        if (window.trackEvent) {
          window.trackEvent('faq_opened', {
            question: questionText
          });
        }
      }
    });
  });

  // ===========================================================================
  // 5. MODAL DE CAPTURA DE LEADS (PRUÉBALO GRATIS)
  // ===========================================================================
  const modalOverlay = document.getElementById('leadModal');
  const modalCloseBtn = document.getElementById('modalCloseBtn');
  const leadForm = document.getElementById('leadForm');
  const modalSuccess = document.getElementById('modalSuccess');
  const modalSourceField = document.getElementById('modalSource');
  const whatsappDirectBtn = document.getElementById('whatsappDirectBtn');

  function openLeadModal(source = 'general') {
    if (!modalOverlay) return;
    if (modalSourceField) modalSourceField.value = source;
    modalOverlay.classList.add('is-active');
    document.body.style.overflow = 'hidden';

    if (window.trackEvent) {
      window.trackEvent('modal_opened', { source });
    }
  }

  function closeLeadModal() {
    if (!modalOverlay) return;
    modalOverlay.classList.remove('is-active');
    document.body.style.overflow = '';
  }

  // Triggers para abrir modal
  document.querySelectorAll('[data-open-modal]').forEach(trigger => {
    trigger.addEventListener('click', (e) => {
      e.preventDefault();
      const source = trigger.getAttribute('data-modal-source') || 'cta_button';
      openLeadModal(source);
    });
  });

  if (modalCloseBtn) {
    modalCloseBtn.addEventListener('click', closeLeadModal);
  }

  if (modalOverlay) {
    modalOverlay.addEventListener('click', (e) => {
      if (e.target === modalOverlay) {
        closeLeadModal();
      }
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modalOverlay.classList.contains('is-active')) {
        closeLeadModal();
      }
    });
  }

  // Envío del formulario
  if (leadForm) {
    leadForm.addEventListener('submit', (e) => {
      e.preventDefault();

      const formData = {
        name: document.getElementById('leadName').value.trim(),
        phone: document.getElementById('leadPhone').value.trim(),
        bizName: document.getElementById('leadBizName').value.trim(),
        bizType: document.getElementById('leadBizType').value,
        district: document.getElementById('leadDistrict').value.trim(),
        source: modalSourceField ? modalSourceField.value : 'web'
      };

      // 1. Enviar evento a Analytics / Google Site Kit
      if (window.trackEvent) {
        window.trackEvent('generate_lead', {
          event_category: 'lead_generation',
          event_label: formData.bizType,
          lead_business_type: formData.bizType,
          lead_city: formData.district,
          lead_source: formData.source
        });
      }

      // 2. Guardar localmente
      try {
        const storedLeads = JSON.parse(localStorage.getItem('aldia_leads') || '[]');
        storedLeads.push({ ...formData, submittedAt: new Date().toISOString() });
        localStorage.setItem('aldia_leads', JSON.stringify(storedLeads));
      } catch (err) {
        console.error('Error saving local lead:', err);
      }

      // 3. Preparar enlace personalizado a WhatsApp
      const cleanPhone = formData.phone.replace(/\D/g, '');
      const whatsappMsg = encodeURIComponent(
        `¡Hola equipo de AlDía! 👋\n` +
        `Mi nombre es ${formData.name} de "${formData.bizName}" (${formData.bizType} en ${formData.district}).\n` +
        `Quiero activar mi prueba gratis de 14 días para dejar de botar plata por productos vencidos.`
      );
      
      const whatsappURL = `https://wa.me/51999999999?text=${whatsappMsg}`;
      if (whatsappDirectBtn) {
        whatsappDirectBtn.href = whatsappURL;
      }

      // 4. Mostrar pantalla de éxito
      leadForm.style.display = 'none';
      if (modalSuccess) {
        modalSuccess.style.display = 'block';
      }
    });
  }

  // ===========================================================================
  // 6. SIMULADOR INTERACTIVO DE WHATSAPP BOT (MODO DEMO)
  // ===========================================================================
  const waTriggerBtn = document.getElementById('waTriggerBtn');
  const waChatWindow = document.getElementById('waChatWindow');
  const waCloseBtn = document.getElementById('waCloseBtn');
  const waBody = document.getElementById('waBody');
  const waOptionsWrap = document.getElementById('waOptionsWrap');
  const waTypingIndicator = document.getElementById('waTypingIndicator');
  const waResetBtn = document.getElementById('waResetBtn');
  const waInitialTime = document.getElementById('waInitialTime');

  function getCurrentTimeStr() {
    const now = new Date();
    let hours = now.getHours();
    const minutes = now.getMinutes().toString().padStart(2, '0');
    const ampm = hours >= 12 ? 'pm' : 'am';
    hours = hours % 12 || 12;
    return `${hours}:${minutes} ${ampm}`;
  }

  if (waInitialTime) {
    waInitialTime.textContent = getCurrentTimeStr();
  }

  function toggleWaChat() {
    if (!waChatWindow) return;
    const isOpen = waChatWindow.classList.toggle('is-open');
    waChatWindow.setAttribute('aria-hidden', !isOpen);
    waChatWindow.style.display = isOpen ? 'flex' : 'none';

    if (isOpen) {
      if (window.trackEvent) {
        window.trackEvent('whatsapp_bot_opened');
      }
      setTimeout(() => {
        waBody.scrollTop = waBody.scrollHeight;
      }, 100);
    }
  }

  if (waTriggerBtn) {
    waTriggerBtn.addEventListener('click', toggleWaChat);
  }

  if (waCloseBtn) {
    waCloseBtn.addEventListener('click', toggleWaChat);
  }

  function appendUserMsg(text) {
    const userMsg = document.createElement('div');
    userMsg.className = 'wa-msg from-user';
    userMsg.innerHTML = `${text}<span class="wa-time">${getCurrentTimeStr()}</span>`;
    waBody.insertBefore(userMsg, waTypingIndicator);
    waBody.scrollTop = waBody.scrollHeight;
  }

  function appendBotMsg(htmlContent, delay = 900, callback = null) {
    waTypingIndicator.style.display = 'inline-flex';
    waBody.scrollTop = waBody.scrollHeight;

    setTimeout(() => {
      waTypingIndicator.style.display = 'none';
      const botMsg = document.createElement('div');
      botMsg.className = 'wa-msg from-bot';
      botMsg.innerHTML = `${htmlContent}<span class="wa-time">${getCurrentTimeStr()}</span>`;
      waBody.insertBefore(botMsg, waTypingIndicator);
      waBody.scrollTop = waBody.scrollHeight;

      if (callback) callback();
    }, delay);
  }

  function handleWaBotAction(action, btnText) {
    appendUserMsg(btnText);
    waOptionsWrap.style.display = 'none';

    if (window.trackEvent) {
      window.trackEvent('whatsapp_bot_action', {
        action_name: action,
        label: btnText
      });
    }

    if (action === 'foto_guia') {
      appendBotMsg(
        `📸 <strong>¡Guía física procesada con IA!</strong><br><br>` +
        `🏢 <em>Distribuidora Gloria S.A.</em><br>` +
        `📦 <strong>24 Yogurts Fresa 1L (Lote 12/11)</strong><br>` +
        `📅 Vencimiento: En 9 días.<br><br>` +
        `🚦 <strong>Semáforo Preventivo AlDía:</strong> He programado tu alerta para pedir el canje 5 días antes con el repartidor. ¡Cero pérdidas aseguradas! ✅`,
        1000,
        showFollowUpOptions
      );
    } else if (action === 'ver_canjes') {
      appendBotMsg(
        `📦 <strong>Tus canjes prioritarios de esta semana:</strong><br><br>` +
        `1. 🍞 <strong>Bimbo:</strong> 6 Panes Blanco (Lote 08/11) - Repartidor pasa <strong>MAÑANA</strong>.<br>` +
        `2. 🧀 <strong>Laive:</strong> 3 Quesos Edam (Lote 11/11).<br><br>` +
        `💡 <em>Sugerencia AlDía:</em> Separa estos productos en una caja hoy para entregárselos al camión sin demoras.`,
        900,
        showFollowUpOptions
      );
    } else if (action === 'remate_jamon') {
      appendBotMsg(
        `🏷️ <strong>Alerta de Remate Preventivo activada:</strong><br><br>` +
        `• 8 Jamones 200g (Lote 06/11) vencen en 3 días.<br>` +
        `• Precio normal: S/ 4.50<br>` +
        `• <strong>Precio con 22% de descuento: S/ 3.50</strong><br><br>` +
        `¡Al rematar hoy recuperas tu capital en vez de botarlo a la basura cuando caduque! 💰`,
        900,
        showFollowUpOptions
      );
    } else if (action === 'asesor_humano') {
      appendBotMsg(
        `👋 <strong>¡Excelente decisión!</strong><br><br>` +
        `Un asesor especializado en bodegas y minimarkets de AlDía te atenderá de inmediato por WhatsApp.<br><br>` +
        `<a href="https://wa.me/51999999999?text=Hola%20AlD%C3%ADa,%20vengo%20del%20demo%20del%20bot%20y%20quiero%20activar%20mi%20prueba%20gratis" target="_blank" rel="noopener" class="wa-real-chat-btn" style="margin-top:0.4rem; display:inline-flex;">` +
        `Abrir chat de WhatsApp real 📲</a>`,
        700,
        showFollowUpOptions
      );
    }
  }

  function showFollowUpOptions() {
    setTimeout(() => {
      const followUp = document.createElement('div');
      followUp.className = 'wa-options-wrap';
      followUp.style.marginTop = '0.5rem';
      followUp.innerHTML = `
        <button type="button" class="wa-option-btn" style="background-color: #ffd54a; color: #0f3d2e; border-color: #0f3d2e;" data-open-modal data-modal-source="whatsapp_bot_cta">
          ⭐ Quiero activar mi prueba gratis de 14 días
        </button>
        <button type="button" class="wa-option-btn" id="btnRestartOptions">
          🔄 Probar otra opción del bot
        </button>
      `;
      waBody.insertBefore(followUp, waTypingIndicator);
      waBody.scrollTop = waBody.scrollHeight;

      // Listener para el botón de prueba gratis dentro del bot
      const btnTrial = followUp.querySelector('[data-open-modal]');
      if (btnTrial) {
        btnTrial.addEventListener('click', () => {
          openLeadModal('whatsapp_bot_simulator');
        });
      }

      // Listener para volver a ver las opciones
      const btnRestart = followUp.querySelector('#btnRestartOptions');
      if (btnRestart) {
        btnRestart.addEventListener('click', resetWaChat);
      }
    }, 400);
  }

  function resetWaChat() {
    const allMsgs = waBody.querySelectorAll('.wa-msg:not(:first-of-type)');
    allMsgs.forEach(m => m.remove());
    const extraWraps = waBody.querySelectorAll('.wa-options-wrap:not(#waOptionsWrap)');
    extraWraps.forEach(w => w.remove());
    waOptionsWrap.style.display = 'flex';
    waBody.scrollTop = 0;

    if (window.trackEvent) {
      window.trackEvent('whatsapp_bot_reset');
    }
  }

  if (waResetBtn) {
    waResetBtn.addEventListener('click', resetWaChat);
  }

  // Delegación de eventos para las opciones del bot
  if (waOptionsWrap) {
    waOptionsWrap.querySelectorAll('.wa-option-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const action = btn.getAttribute('data-action');
        const text = btn.textContent.trim();
        handleWaBotAction(action, text);
      });
    });
  }
});

