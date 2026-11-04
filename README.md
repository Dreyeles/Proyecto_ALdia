# AlDía – Plataforma Inteligente de Control de Vencimientos e Inventarios

> **Eslogan oficial:** *"Tu negocio y mercadería, siempre al día."*

Bienvenido al repositorio central de **AlDía**, una solución digital ágil diseñada para pequeños comercios tradicionales (minimarkets, bodegas y ferreterías) que buscan erradicar las pérdidas por productos vencidos, optimizar sus inventarios y dejar atrás los cuadernos manuales sin la complejidad ni el alto costo de un ERP corporativo.

---

## 📌 Ficha Técnica del Proyecto

* **Proyecto:** AlDía (Plataforma Web y Móvil)
* **Curso / Unidad Didáctica:** Metodologías Ágiles de Innovación
* **Hito Evaluativo:** Avance 1 – Identificación de problemática, segmentación integral, arquetipo de cliente, hipótesis de solución y alineación con ODS.
* **Modelo de Negocio:** Micro-SaaS B2B accesible (Suscripción de S/ 39 a S/ 59 PEN mensuales).

---

## 🎯 Síntesis Ejecutiva del Proyecto AlDía

| Dimensión | Enfoque Estratégico de AlDía |
| :--- | :--- |
| **Problema Central** | Pérdidas económicas por falta de control de inventarios, cuadernos manuales, desconocimiento de existencias y merma directa por productos vencidos y pérdida de la ventana de canje con distribuidores. |
| **Segmento Objetivo** | Micro y Pequeñas Empresas (MYPES) comerciales minoristas bajo régimen **NRUS** en zonas urbanas de Perú (minimarkets, bodegas, boticas y ferreterías familiares). |
| **Solución Innovadora** | Plataforma ligera que no exige registrar cada venta en caja: automatiza ingresos por foto de guías o facturas electrónicas, descuenta lotes bajo regla FEFO y audita stock en checklists de 1 minuto. |
| **Propuesta de Valor** | Evitar que los pequeños comerciantes boten dinero a la basura por productos caducados, maximizando el canje gratuito con proveedores y liquidando mercadería a tiempo. |
| **Impacto Sostenible** | Reducción directa del desperdicio de alimentos (**ODS 12**), impulso a la productividad de las microempresas (**ODS 8**) y democratización de la innovación tecnológica (**ODS 9**). |

---

## ⚡ Los 3 Pilares Operativos de AlDía (Baja Fricción)

```
[ INGRESO SIN ESFUERZO ]          [ CONTROL INTELIGENTE ]          [ SALIDA Y AUDITORÍA ]
Foto a Guía Física (IA/OCR)    ──>  Semáforo Preventivo AlDía   ──>  Regla FEFO Automática
o Factura Electrónica (PDF/XML)     • Zona de Canje (7-15 días)      + Checklist Rápido de 1 Min
                                    • Zona de Remate (3-5 días)      (Sin invadir el cobro en caja)
```

1. **Entrada sin Tipeo Manual:** Registro automático de lotes mediante visión computacional (cámara del celular a guías de reparto impresas) o lectura directa de facturas electrónicas en PDF/XML.
2. **Semáforo Preventivo de Alertas:** Notificaciones oportunas para solicitar el canje gratuito al proveedor (Bimbo, lácteos, embutidos) antes de que venza el plazo, o activar precios de liquidación en tienda.
3. **Salida Automatizada y Auditoría Ágil:** Descuenta ventas según el lote más antiguo (First Expired, First Out) y realiza preguntas automáticas de 10 segundos (*"¿Aún te queda stock de este lote?"*) por excepción.

---

## 📂 Estructura y Navegación de la Documentación

Todos los módulos del proyecto se encuentran documentados a detalle en la carpeta `docs/`:

1. **[01. Propuesta de Valor y Definición Estratégica](docs/01_propuesta_de_valor.md):**
   * Planteamiento de la propuesta de valor, justificación del nombre **AlDía** y delimitación del problema.
2. **[02. Arquetipo de Cliente 1 - Daniel Ibarcena (Ferretería / Sucesor)](docs/02_arquetipo_daniel_ibarcena.md):**
   * Perfil del joven contador (29 años, Los Olivos) que busca modernizar el negocio familiar de su padre, digitalizar el cuaderno y evitar capital inmovilizado.
3. **[03. Estrategia Técnica y Operativa de Baja Fricción](docs/03_estrategia_tecnica_y_operativa.md):**
   * Arquitectura del sistema, flujo de OCR para guías físicas, procesamiento de facturas electrónicas y regla FEFO.
4. **[04. Segmentación Integral de Mercado y Alineación con los ODS](docs/04_segmentacion_b2b_y_ods.md):**
   * Desarrollo de las 4 variables de segmentación (Geográfica, Demográfica, Psicográfica y Conductual).
   * Segmentación B2B firmográfica (MYPES, NRUS) y justificación de impacto para los **ODS 8, 9 y 12**.
5. **[05. Arquetipo de Cliente 2 - María Fernández (Minimarket / Perecibles)](docs/05_arquetipo_maria_fernandez.md):**
   * Perfil de la dueña de minimarket (38 años, Los Olivos) que enfrenta mermas por vencimientos y pérdida de canjes con repartidores.
6. **[06. Guía y Transcripción de la Presentación PPT](docs/06_guia_presentacion_ppt.md):**
   * Guion y estructura diapositiva por diapositiva del entregable evaluativo Avance 1.

---

## 🖥️ Material de Presentación Generado (Avance 1)

* **Diapositivas listas para exposición:** [`Avance1_Metodologias_Agiles_Innovacion.pptx`](Avance1_Metodologias_Agiles_Innovacion.pptx)
* **Formato:** Pantalla panorámica 16:9, estilo visual moderno con contenedores, tarjetas de datos y colores temáticos alineados a la rúbrica oficial (cumple los 20/20 puntos).
* **Script de Generación:** [`generate_ppt.py`](generate_ppt.py) (permite recompilar la presentación automáticamente tras cualquier ajuste).
