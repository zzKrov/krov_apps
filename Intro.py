import streamlit as st
import streamlit.components.v1 as components
import json

# ==============================================================================
# 1. CONFIGURACIÓN GENERAL Y FAVICON
# ==============================================================================
st.set_page_config(
    page_title="Juan David Segura // Interfaces Multimodales",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

def render_clean_html(html_str: str):
    compact = "".join(line.strip() for line in html_str.splitlines() if line.strip())
    st.markdown(compact, unsafe_allow_html=True)

# ==============================================================================
# 2. CATÁLOGO MAESTRO (19 APLICACIONES)
# ==============================================================================
CATALOGO = [
    {
        "id": 1,
        "titulo": "Detector de Objetos",
        "cat": "Visión y Óptica",
        "url": "https://yolozz.streamlit.app",
        "icon": "🎯",
        "svg_type": "vision",
        "desc": "Encuadra y cuantifica 80 clases comunes de objetos en imágenes o video en vivo.",
        "uso": "Control de aforo y logística de inventario en bodegas.",
        "color": "#38bdf8"
    },
    {
        "id": 2,
        "titulo": "Nube de Palabras",
        "cat": "Lenguaje y RAG",
        "url": "https://wordcloudz.streamlit.app",
        "icon": "☁️",
        "svg_type": "text",
        "desc": "Composición gráfica ponderada según la densidad de frecuencia léxica del texto.",
        "uso": "Extracción rápida de conceptos preponderantes en encuestas.",
        "color": "#818cf8"
    },
    {
        "id": 3,
        "titulo": "Dígitos Ópticos",
        "cat": "Redes y Modelado",
        "url": "https://mnistz.streamlit.app",
        "icon": "✍️",
        "svg_type": "neural",
        "desc": "Reconocimiento y clasificación de números manuscritos del 0 al 9 sobre lienzo.",
        "uso": "Digitalización automática de formularios y comprobantes bancarios.",
        "color": "#8b5cf6"
    },
    {
        "id": 4,
        "titulo": "Análisis Contextual",
        "cat": "Visión y Óptica",
        "url": "https://visionz.streamlit.app",
        "icon": "👁️",
        "svg_type": "vision",
        "desc": "Evaluación semántica y redacción técnica estructurada de cualquier escena fotográfica.",
        "uso": "Inspección pericial de siniestros para aseguradoras.",
        "color": "#38bdf8"
    },
    {
        "id": 5,
        "titulo": "Traductor de Voz",
        "cat": "Voz y Acústica",
        "url": "https://traductorz.streamlit.app",
        "icon": "🎙️",
        "svg_type": "audio",
        "desc": "Captura vocal por micrófono, traducción instantánea y reproducción fonética.",
        "uso": "Atención multilingüe presencial en ventanillas de servicio.",
        "color": "#c084fc"
    },
    {
        "id": 6,
        "titulo": "Detector de Postura",
        "cat": "Visión y Óptica",
        "url": "https://teachablez.streamlit.app",
        "icon": "🛡️",
        "svg_type": "vision",
        "desc": "Monitoreo corporal y presencia axial desde cámara web sin transmisión a la nube.",
        "uso": "Supervisión ergonómica laboral y quioscos sin contacto.",
        "color": "#38bdf8"
    },
    {
        "id": 7,
        "titulo": "Pausa y Bienestar",
        "cat": "Interacción y Creatividad",
        "url": "https://bendover.streamlit.app",
        "icon": "🐇",
        "svg_type": "creative",
        "desc": "Entorno antiestrés con partículas reactivas al cursor y síntesis auditiva.",
        "uso": "Pausas activas y reducción de la fatiga en pantalla.",
        "color": "#6366f1"
    },
    {
        "id": 8,
        "titulo": "Conversación Guiada",
        "cat": "Interacción y Creatividad",
        "url": "https://sentimentz.streamlit.app",
        "icon": "🤖",
        "svg_type": "text",
        "desc": "Diálogo asistido con análisis del estado afectivo y respuestas adaptativas.",
        "uso": "Bitácoras personales y redacción formal bajo presión.",
        "color": "#6366f1"
    },
    {
        "id": 9,
        "titulo": "Visor de Texto 3D",
        "cat": "Visión y Óptica",
        "url": "https://ocryaudioz.streamlit.app",
        "icon": "🪞",
        "svg_type": "vision",
        "desc": "Extracción óptica de texto y proyección interactiva sobre plano tridimensional.",
        "uso": "Lectura asistida de señalética física en lenguas extranjeras.",
        "color": "#38bdf8"
    },
    {
        "id": 10,
        "titulo": "Digitalizador Óptico",
        "cat": "Visión y Óptica",
        "url": "https://lectorz.streamlit.app",
        "icon": "📷",
        "svg_type": "vision",
        "desc": "Conversión inmediata de capturas de cámara web en fragmentos de texto editables.",
        "uso": "Transcripción ágil de citas y registro de recibos impresos.",
        "color": "#38bdf8"
    },
    {
        "id": 11,
        "titulo": "Interfaces Sensoriales",
        "cat": "Voz y Acústica",
        "url": "https://sussusamogus.streamlit.app",
        "icon": "✦",
        "svg_type": "audio",
        "desc": "Señalización multisensorial con pulsos de luz, tonos audibles y vibración háptica.",
        "uso": "Cabinas de advertencia industrial y accesibilidad táctil.",
        "color": "#c084fc"
    },
    {
        "id": 12,
        "titulo": "Tablero de Bocetos",
        "cat": "Interacción y Creatividad",
        "url": "https://drawrecogz.streamlit.app",
        "icon": "🎨",
        "svg_type": "creative",
        "desc": "Pizarra de dibujo digital con interpretación visual de esquemas geométricos.",
        "uso": "Conceptualización de diagramas y prototipado temprano.",
        "color": "#6366f1"
    },
    {
        "id": 13,
        "titulo": "Consulta sobre PDF",
        "cat": "Lenguaje y RAG",
        "url": "https://chatpdfz.streamlit.app",
        "icon": "💬",
        "svg_type": "text",
        "desc": "Resolución de consultas precisas sustentadas en el contenido de un archivo PDF.",
        "uso": "Auditoría de contratos extensos y manuales de ingeniería.",
        "color": "#818cf8"
    },
    {
        "id": 14,
        "titulo": "Analizador de Tono",
        "cat": "Lenguaje y RAG",
        "url": "https://textanalysiz.streamlit.app",
        "icon": "⚖️",
        "svg_type": "text",
        "desc": "Diagnóstico de neutralidad, carga subjetiva y polaridad emocional de mensajes.",
        "uso": "Revisión formal de comunicaciones corporativas delicadas.",
        "color": "#818cf8"
    },
    {
        "id": 15,
        "titulo": "Modelador Físico",
        "cat": "Redes y Modelado",
        "url": "https://histinfz.streamlit.app",
        "icon": "⚡",
        "svg_type": "neural",
        "desc": "Deducción de ecuaciones de equilibrio estático a partir de esquemas de fuerzas.",
        "uso": "Validación conceptual de mecanismos simples y palancas.",
        "color": "#8b5cf6"
    },
    {
        "id": 16,
        "titulo": "Relatos Ilustrados",
        "cat": "Interacción y Creatividad",
        "url": "https://ejemplohistinfz.streamlit.app",
        "icon": "📖",
        "svg_type": "creative",
        "desc": "Generación de historias estructuradas a partir de personajes dibujados a mano.",
        "uso": "Fomento de la lectura y dinámicas escolares creativas.",
        "color": "#6366f1"
    },
    {
        "id": 17,
        "titulo": "Telemetría IoT",
        "cat": "IoT y Ciberfísica",
        "url": "https://receptz.streamlit.app",
        "icon": "📡",
        "svg_type": "iot",
        "desc": "Monitoreo en tiempo real de temperatura, humedad y presión con gemelo Wokwi.",
        "uso": "Supervisión ambiental y control de salas de servidores.",
        "color": "#22d3ee"
    },
    {
        "id": 18,
        "titulo": "Control de Actuadores",
        "cat": "Actuación y Hardware",
        "url": "https://sendcmqttz.streamlit.app",
        "icon": "⚡",
        "svg_type": "iot",
        "desc": "Mando remoto para activación de matrices LED y posicionamiento angular de servos.",
        "uso": "Automatización distribuida y control de compuertas.",
        "color": "#3b82f6"
    },
    {
        "id": 19,
        "titulo": "Control por Voz IoT",
        "cat": "Voz y Acústica",
        "url": "https://ctrlvoicez.streamlit.app",
        "icon": "🎙️",
        "svg_type": "audio",
        "desc": "Operación manos libres de hardware mediante locuciones en lenguaje natural.",
        "uso": "Comando en cabinas industriales y entornos asistivos.",
        "color": "#c084fc"
    }
]

APPS_JSON = json.dumps(CATALOGO)

# ==============================================================================
# 3. ESTILOS Y CABECERA ANIMADA (JUAN DAVID SEGURA)
# ==============================================================================
render_clean_html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

html, body, [data-testid="stAppViewContainer"], .stApp {
    background: transparent !important;
    background-color: transparent !important;
    color: #e2e8f0 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    overflow-x: hidden;
}

body {
    background-color: #04060d !important;
}

[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stSidebar"], section[data-testid="stSidebar"] { display: none !important; }

.block-container {
    max-width: 1380px !important;
    padding-top: 1rem !important;
    padding-bottom: 2rem !important;
    margin: 0 auto !important;
}

/* Cabecera Cinética de Autor */
.header-deck {
    text-align: center;
    margin-bottom: 1.1rem;
}

.author-signature {
    font-family: 'JetBrains Mono', monospace;
    font-size: clamp(0.95rem, 1.5vw, 1.25rem);
    font-weight: 700;
    letter-spacing: 0.38em;
    text-transform: uppercase;
    background: linear-gradient(90deg, #94a3b8 0%, #ffffff 25%, #38bdf8 55%, #c084fc 80%, #94a3b8 100%);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shimmerSignature 6s linear infinite;
    filter: drop-shadow(0 0 16px rgba(56, 189, 248, 0.4));
    margin-bottom: 0.25rem;
}

@keyframes shimmerSignature {
    0% { background-position: 0% 50%; }
    100% { background-position: 200% 50%; }
}

.hero-title {
    font-size: clamp(1.8rem, 3.2vw, 2.7rem);
    font-weight: 700;
    color: #ffffff;
    line-height: 1.15;
    margin: 0.15rem 0 0.35rem 0;
    letter-spacing: -0.025em;
    text-shadow: 0 0 25px rgba(56, 189, 248, 0.35);
}

.hero-sub {
    color: #94a3b8;
    font-size: 0.9rem;
    max-width: 680px;
    margin: 0 auto;
}

.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(290px, 1fr));
    gap: 14px;
    margin-top: 14px;
}

.grid-card {
    background: rgba(8, 14, 28, 0.95);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-top: 3px solid #38bdf8;
    border-radius: 8px;
    padding: 16px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.6);
    transition: transform 0.2s ease, border-color 0.2s ease;
}

.grid-card:hover {
    transform: translateY(-2px);
    border-color: #38bdf8;
}

.grid-link {
    display: block;
    width: 100%;
    text-align: center;
    border-radius: 4px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    font-weight: 600;
    padding: 8px;
    text-decoration: none;
    margin-top: 10px;
}
</style>
""")

# ==============================================================================
# 4. CANVAS GPU DE ORBES FLOTANTES DE ALTA VISIBILIDAD
# ==============================================================================
components.html(
    """
    <script>
    (function() {
        const pWin = window.parent;
        const pDoc = pWin.document;
        if (pWin.__GALAXY_BG_ACTIVE__) return;
        pWin.__GALAXY_BG_ACTIVE__ = true;

        let canvas = pDoc.getElementById('galaxy-blue-canvas');
        if (!canvas) {
            canvas = pDoc.createElement('canvas');
            canvas.id = 'galaxy-blue-canvas';
            canvas.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:0;background:#04060d;';
            pDoc.body.prepend(canvas);
        }

        const ctx = canvas.getContext('2d', { alpha: false });
        const scale = pWin.innerWidth < 768 ? 0.5 : 0.7;
        let w = canvas.width = Math.floor(pWin.innerWidth * scale);
        let h = canvas.height = Math.floor(pWin.innerHeight * scale);

        pWin.addEventListener('resize', () => {
            w = canvas.width = Math.floor(pWin.innerWidth * scale);
            h = canvas.height = Math.floor(pWin.innerHeight * scale);
        });

        // 5 Grandes orbes de plasma flotantes
        const orbs = [
            { x: w * 0.15, y: h * 0.25, r: 280 * scale, vx: 0.35, vy: 0.25, baseH: 220, color: 'rgba(37, 99, 235, 0.38)' },
            { x: w * 0.85, y: h * 0.35, r: 320 * scale, vx: -0.3, vy: 0.35, baseH: 195, color: 'rgba(56, 189, 248, 0.35)' },
            { x: w * 0.5,  y: h * 0.85, r: 290 * scale, vx: 0.25, vy: -0.3, baseH: 275, color: 'rgba(168, 85, 247, 0.32)' },
            { x: w * 0.2,  y: h * 0.75, r: 260 * scale, vx: -0.25, vy: -0.25, baseH: 260, color: 'rgba(192, 132, 252, 0.30)' },
            { x: w * 0.8,  y: h * 0.8,  r: 270 * scale, vx: 0.2,  vy: -0.35, baseH: 185, color: 'rgba(34, 211, 238, 0.32)' }
        ];

        const pColors = ['#38bdf8', '#818cf8', '#c084fc', '#93c5fd', '#cbd5e1'];
        const pCount = pWin.innerWidth < 768 ? 16 : 24;
        const particles = [];
        for (let i = 0; i < pCount; i++) {
            particles.push({
                x: Math.random() * w,
                y: Math.random() * h,
                r: Math.random() * 1.5 + 0.7,
                vx: (Math.random() - 0.5) * 0.45,
                vy: (Math.random() - 0.5) * 0.45,
                color: pColors[i % pColors.length]
            });
        }

        let hyperspaceShift = 0;

        function loop() {
            ctx.fillStyle = '#04060d';
            ctx.fillRect(0, 0, w, h);

            const isHyperspace = Boolean(pWin.__GALAXY_HYPERSPACE__);
            if (isHyperspace) {
                hyperspaceShift = (hyperspaceShift + 0.6) % 360;
            }

            ctx.globalCompositeOperation = 'screen';
            for (let b of orbs) {
                b.x += b.vx;
                b.y += b.vy;
                if (b.x < -80 || b.x > w + 80) b.vx *= -1;
                if (b.y < -80 || b.y > h + 80) b.vy *= -1;

                let c = b.color;
                if (isHyperspace) {
                    const currentH = (b.baseH + hyperspaceShift) % 360;
                    c = `hsla(${currentH}, 90%, 55%, 0.42)`;
                }

                const g = ctx.createRadialGradient(b.x, b.y, 4, b.x, b.y, b.r);
                g.addColorStop(0, c);
                g.addColorStop(1, 'rgba(4, 6, 13, 0)');
                ctx.beginPath();
                ctx.arc(b.x, b.y, b.r, 0, Math.PI * 2);
                ctx.fillStyle = g;
                ctx.fill();
            }

            ctx.globalCompositeOperation = 'lighter';
            const speedMult = isHyperspace ? 1.6 : 1.0;
            for (let i = 0; i < particles.length; i++) {
                const p = particles[i];
                p.x += p.vx * speedMult;
                p.y += p.vy * speedMult;
                if (p.x < 0) p.x = w;
                if (p.x > w) p.x = 0;
                if (p.y < 0) p.y = h;
                if (p.y > h) p.y = 0;

                ctx.beginPath();
                ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
                ctx.fillStyle = isHyperspace ? `hsla(${hyperspaceShift + (i * 15)}, 85%, 65%, 0.8)` : p.color;
                ctx.fill();

                for (let j = i + 1; j < particles.length; j++) {
                    const p2 = particles[j];
                    const dx = p.x - p2.x;
                    const dy = p.y - p2.y;
                    const d2 = dx * dx + dy * dy;
                    if (d2 < 4500) {
                        ctx.beginPath();
                        ctx.moveTo(p.x, p.y);
                        ctx.lineTo(p2.x, p2.y);
                        let strokeCol = `rgba(56, 189, 248, ${0.28 * (1 - d2 / 4500)})`;
                        if (isHyperspace) {
                            strokeCol = `hsla(${hyperspaceShift}, 85%, 65%, ${0.45 * (1 - d2 / 4500)})`;
                        }
                        ctx.strokeStyle = strokeCol;
                        ctx.lineWidth = 0.65;
                        ctx.stroke();
                    }
                }
            }

            ctx.globalCompositeOperation = 'source-over';
            requestAnimationFrame(loop);
        }
        loop();
    })();
    </script>
    """,
    height=0,
    width=0
)

# ==============================================================================
# 5. CABECERA LIMPIA
# ==============================================================================
render_clean_html("""
<div class="header-deck">
    <div class="author-signature">Juan David Segura</div>
    <div class="hero-title">Interfaces Multimodales</div>
    <div class="hero-sub">19 aplicaciones interactivas en visión artificial, modelos de lenguaje, telemetría IoT y acústica.</div>
</div>
""")

tab_estacion, tab_matriz = st.tabs(["Estación de Inspección", "Directorio"])

# ==============================================================================
# PESTAÑA 1: PATERNOSTER INFINITO CON ANIMACIÓN DE ARRASTRE DISUELTA
# ==============================================================================
with tab_estacion:
    components.html(
        f"""
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="utf-8">
        <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
        <style>
            * {{ box-sizing: border-box; margin: 0; padding: 0; user-select: none; }}
            html, body {{
                background: transparent;
                color: #e2e8f0;
                font-family: 'Plus Jakarta Sans', sans-serif;
                overflow: hidden;
                width: 100%;
                height: 100%;
            }}

            /* --- BARRA DE PROGRESO DE AUDITORÍA --- */
            .audit-header-bar {{
                background: rgba(10, 16, 32, 0.95);
                border: 1px solid rgba(203, 213, 225, 0.18);
                border-radius: 20px;
                padding: 8px 18px;
                margin-bottom: 12px;
                box-shadow: 0 4px 18px rgba(0, 0, 0, 0.5);
                display: flex;
                flex-direction: column;
                gap: 6px;
            }}

            .audit-bar-top {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                font-family: 'JetBrains Mono', monospace;
                font-size: 0.74rem;
            }}

            .progress-track {{
                width: 100%;
                height: 7px;
                background: rgba(255, 255, 255, 0.08);
                border-radius: 6px;
                overflow: hidden;
                position: relative;
            }}

            .progress-fill {{
                height: 100%;
                background: linear-gradient(90deg, #1d4ed8, #3b82f6, #38bdf8, #818cf8, #c084fc, #1d4ed8);
                background-size: 260% 100%;
                animation: liquidStream 4s linear infinite;
                border-radius: 6px;
                transition: width 0.35s cubic-bezier(0.16, 1, 0.3, 1);
                box-shadow: 0 0 12px rgba(56, 189, 248, 0.6);
            }}

            @keyframes liquidStream {{
                0% {{ background-position: 0% 50%; }}
                100% {{ background-position: 260% 50%; }}
            }}

            /* --- CONTENEDOR MASTER-DETAIL --- */
            .deck-wrapper {{
                display: flex;
                gap: 24px;
                width: 100%;
                height: 600px;
            }}

            /* --- ESTANTE PATERNOSTER ENSANCHADO --- */
            .paternoster-container {{
                flex: 1.35;
                position: relative;
                background: linear-gradient(145deg, rgba(9, 14, 28, 0.95) 0%, rgba(5, 8, 18, 0.98) 100%);
                border: 1px solid rgba(56, 189, 248, 0.22);
                border-radius: 14px;
                padding: 16px;
                display: flex;
                flex-direction: column;
                box-shadow: 0 12px 35px rgba(0, 0, 0, 0.7);
                overflow: hidden;
            }}

            .paternoster-header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 10px;
                padding-bottom: 8px;
                border-bottom: 1px solid rgba(255, 255, 255, 0.08);
                font-family: 'JetBrains Mono', monospace;
                font-size: 0.72rem;
            }}

            .paternoster-viewport {{
                flex: 1;
                position: relative;
                overflow: hidden;
                cursor: grab;
                touch-action: none;
            }}

            .paternoster-viewport:active {{
                cursor: grabbing;
            }}

            /* Animación sutil de sugerencia de arrastre (se disuelve tras 2 ciclos) */
            .drag-hint-pill {{
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                z-index: 50;
                pointer-events: none;
                display: flex;
                align-items: center;
                gap: 8px;
                background: rgba(8, 14, 28, 0.88);
                border: 1px solid rgba(56, 189, 248, 0.5);
                border-radius: 20px;
                padding: 8px 16px;
                font-family: 'JetBrains Mono', monospace;
                font-size: 0.75rem;
                font-weight: 600;
                color: #38bdf8;
                box-shadow: 0 0 25px rgba(56, 189, 248, 0.4);
                animation: dragHintFloat 2.6s ease-in-out 2 forwards;
            }}

            @keyframes dragHintFloat {{
                0%   {{ transform: translate(-50%, -50%); opacity: 0; }}
                20%  {{ transform: translate(-50%, -65%); opacity: 0.9; }}
                50%  {{ transform: translate(-50%, -35%); opacity: 0.9; }}
                80%  {{ transform: translate(-50%, -50%); opacity: 0.9; }}
                100% {{ transform: translate(-50%, -50%); opacity: 0; }}
            }}

            .paternoster-aperture {{
                position: absolute;
                top: 50%;
                left: 0;
                right: 0;
                height: 96px;
                transform: translateY(-50%);
                border: 1px solid rgba(56, 189, 248, 0.45);
                border-left: 4px solid #38bdf8;
                border-radius: 10px;
                pointer-events: none;
                box-shadow: 0 0 25px rgba(56, 189, 248, 0.25), inset 0 0 15px rgba(56, 189, 248, 0.1);
                z-index: 2;
            }}

            .shelf-card {{
                position: absolute;
                left: 0;
                right: 0;
                height: 86px;
                background: rgba(12, 19, 38, 0.92);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 8px;
                padding: 12px 18px;
                display: flex;
                align-items: center;
                justify-content: space-between;
                transition: opacity 0.15s ease, filter 0.15s ease;
                transform-origin: center center;
                will-change: transform, opacity;
            }}

            .shelf-card-info {{
                flex: 1;
                padding-right: 14px;
            }}

            .shelf-card-title {{
                font-weight: 700;
                font-size: 0.95rem;
                color: #ffffff;
                display: flex;
                align-items: center;
                gap: 8px;
            }}

            .shelf-card-desc {{
                font-size: 0.78rem;
                color: #94a3b8;
                margin-top: 3px;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
            }}

            .ejected-btn {{
                position: absolute;
                right: -6px;
                top: 50%;
                transform: translateY(-50%) translateX(25px);
                opacity: 0;
                pointer-events: none;
                background: linear-gradient(135deg, #0284c7 0%, #2563eb 60%, #7c3aed 100%);
                color: #ffffff;
                border: 1px solid rgba(56, 189, 248, 0.7);
                border-radius: 6px;
                padding: 10px 18px;
                font-family: 'JetBrains Mono', monospace;
                font-weight: 700;
                font-size: 0.78rem;
                letter-spacing: 0.08em;
                cursor: pointer;
                box-shadow: 0 0 20px rgba(56, 189, 248, 0.6);
                transition: transform 0.28s cubic-bezier(0.175, 0.885, 0.32, 1.275), opacity 0.22s ease;
                z-index: 10;
            }}

            .ejected-btn.visible {{
                transform: translateY(-50%) translateX(0);
                opacity: 1;
                pointer-events: auto;
            }}

            .ejected-btn:hover {{
                box-shadow: 0 0 30px rgba(56, 189, 248, 0.9);
                filter: brightness(1.15);
            }}

            /* --- ESTACIÓN LATERAL DE INSPECCIÓN --- */
            .workstation-container {{
                flex: 1.05;
                background: linear-gradient(145deg, rgba(12, 18, 38, 0.98) 0%, rgba(6, 10, 22, 0.98) 100%);
                border: 1px solid rgba(56, 189, 248, 0.28);
                border-top: 3px solid #38bdf8;
                border-radius: 14px;
                padding: 22px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                box-shadow: 0 12px 35px rgba(0, 0, 0, 0.75);
                position: relative;
            }}

            .workstation-top {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 6px;
            }}

            .chip-cat {{
                font-family: 'JetBrains Mono', monospace;
                font-size: 0.72rem;
                padding: 4px 10px;
                border-radius: 6px;
                font-weight: 600;
                text-transform: uppercase;
                background: rgba(56, 189, 248, 0.15);
                border: 1px solid rgba(56, 189, 248, 0.4);
                color: #38bdf8;
            }}

            .workstation-title {{
                font-size: 1.6rem;
                font-weight: 700;
                color: #ffffff;
                margin: 4px 0 6px 0;
            }}

            .workstation-desc {{
                font-size: 0.92rem;
                color: #cbd5e1;
                line-height: 1.5;
                margin-bottom: 10px;
            }}

            .workstation-box {{
                background: rgba(56, 189, 248, 0.06);
                border-left: 3px solid #38bdf8;
                border-radius: 6px;
                padding: 9px 12px;
                margin-bottom: 12px;
            }}

            .workstation-box-lbl {{
                font-family: 'JetBrains Mono', monospace;
                font-size: 0.68rem;
                color: #38bdf8;
                text-transform: uppercase;
                font-weight: 700;
                margin-bottom: 2px;
            }}

            .workstation-hud {{
                background: rgba(5, 9, 20, 0.95);
                border: 1px solid rgba(56, 189, 248, 0.25);
                border-radius: 10px;
                padding: 10px;
                display: flex;
                align-items: center;
                justify-content: center;
                margin-bottom: 14px;
                box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.8);
            }}

            .action-deck {{
                display: flex;
                gap: 12px;
            }}

            .btn-primary {{
                flex: 1.5;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 45%, #7c3aed 100%);
                color: #ffffff;
                text-decoration: none;
                font-family: 'JetBrains Mono', monospace;
                font-weight: 700;
                font-size: 0.86rem;
                border-radius: 6px;
                padding: 12px;
                box-shadow: 0 0 20px rgba(37, 99, 235, 0.5);
                border: 1px solid rgba(226, 232, 240, 0.25);
                cursor: pointer;
                transition: all 0.2s ease;
            }}

            .btn-primary:hover {{
                box-shadow: 0 0 30px rgba(56, 189, 248, 0.7);
                transform: translateY(-1px);
            }}

            .btn-verify {{
                flex: 1.2;
                background: rgba(14, 20, 38, 0.95);
                color: #e2e8f0;
                border: 1px solid rgba(203, 213, 225, 0.25);
                border-radius: 6px;
                padding: 12px;
                font-family: 'JetBrains Mono', monospace;
                font-weight: 600;
                font-size: 0.8rem;
                cursor: pointer;
                transition: all 0.2s ease;
            }}

            .btn-verify:hover {{
                border-color: #38bdf8;
                color: #ffffff;
            }}

            .btn-verify.checked {{
                background: rgba(45, 212, 191, 0.15);
                border-color: #2dd4bf;
                color: #2dd4bf;
            }}

            /* Modal de finalización (19/19) */
            .modal-overlay {{
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                background: rgba(4, 6, 13, 0.85);
                backdrop-filter: blur(8px);
                display: none;
                align-items: center;
                justify-content: center;
                z-index: 1000;
            }}

            .modal-overlay.active {{
                display: flex;
            }}

            .modal-card {{
                background: linear-gradient(145deg, #0d152d 0%, #060913 100%);
                border: 1px solid #38bdf8;
                border-radius: 14px;
                padding: 28px 32px;
                max-width: 500px;
                text-align: center;
                box-shadow: 0 0 45px rgba(56, 189, 248, 0.45);
                animation: popIn 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            }}

            @keyframes popIn {{
                0% {{ transform: scale(0.85); opacity: 0; }}
                100% {{ transform: scale(1); opacity: 1; }}
            }}

            .modal-icon {{
                font-size: 2.4rem;
                margin-bottom: 8px;
            }}

            .modal-title {{
                font-family: 'Plus Jakarta Sans', sans-serif;
                font-size: 1.35rem;
                font-weight: 700;
                color: #ffffff;
                margin-bottom: 8px;
            }}

            .modal-body {{
                font-size: 0.9rem;
                color: #cbd5e1;
                line-height: 1.6;
                margin-bottom: 20px;
            }}

            .modal-btn {{
                background: linear-gradient(135deg, #0284c7 0%, #2563eb 50%, #7c3aed 100%);
                color: #ffffff;
                border: 1px solid rgba(56, 189, 248, 0.6);
                border-radius: 6px;
                padding: 10px 24px;
                font-family: 'JetBrains Mono', monospace;
                font-size: 0.85rem;
                font-weight: 700;
                cursor: pointer;
                box-shadow: 0 0 20px rgba(56, 189, 248, 0.5);
                transition: all 0.2s ease;
            }}

            .modal-btn:hover {{
                box-shadow: 0 0 30px rgba(56, 189, 248, 0.8);
                transform: translateY(-1px);
            }}
        </style>
        </head>
        <body>

        <!-- MODAL DE FINALIZACIÓN -->
        <div class="modal-overlay" id="completion-modal">
            <div class="modal-card">
                <div class="modal-icon">💠</div>
                <div class="modal-title">Inspección Completada</div>
                <div class="modal-body">
                    Las <strong>19 aplicaciones</strong> del portafolio han sido verificadas con éxito. Todos los sistemas de visión, modelos de lenguaje, telemetría IoT y actuadores se encuentran validados.
                </div>
                <button class="modal-btn" onclick="dismissModal()">Aceptar y Continuar</button>
            </div>
        </div>

        <!-- BARRA MAESTRA DE AUDITORÍA -->
        <div class="audit-header-bar">
            <div class="audit-bar-top">
                <span style="color:#cbd5e1; font-weight:700;">PROGRESO</span>
                <span id="audit-stats-text" style="color:#38bdf8; font-weight:700;">00 / 19 (0%)</span>
            </div>
            <div class="progress-track">
                <div class="progress-fill" id="audit-progress-fill" style="width: 4%;"></div>
            </div>
        </div>

        <div class="deck-wrapper">
            <!-- ESTANTE PATERNOSTER -->
            <div class="paternoster-container">
                <div class="paternoster-header">
                    <span style="color:#cbd5e1;">CATÁLOGO</span>
                    <span id="paternoster-counter" style="color:#38bdf8;">01 / 19</span>
                </div>
                
                <div class="paternoster-viewport" id="viewport">
                    <!-- Animación sutil de sugerencia de arrastre -->
                    <div class="drag-hint-pill" id="drag-hint">
                        <span>↕</span> <span>Deslizar</span>
                    </div>

                    <div class="paternoster-aperture"></div>
                    <div id="cards-container"></div>
                </div>
            </div>

            <!-- ESTACIÓN LATERAL -->
            <div class="workstation-container" id="workstation">
                <div>
                    <div class="workstation-top">
                        <span class="chip-cat" id="ws-cat">VISIÓN</span>
                        <span style="font-family:'JetBrains Mono'; font-size:0.76rem; color:#cbd5e1;" id="ws-counter">#01 / 19</span>
                    </div>
                    <div class="workstation-title" id="ws-title">Detector de Objetos</div>
                    <div class="workstation-desc" id="ws-desc">Encuadra y cuantifica 80 clases comunes de objetos en imágenes o video en vivo.</div>
                    <div class="workstation-box" id="ws-box">
                        <div class="workstation-box-lbl" id="ws-box-lbl">USO PRÁCTICO</div>
                        <div style="font-size:0.86rem; color:#cbd5e1;" id="ws-uso">Control de aforo y logística de inventario.</div>
                    </div>
                </div>

                <div class="workstation-hud" id="ws-hud"></div>

                <div class="action-deck">
                    <button class="btn-primary" id="ws-btn-open" onclick="handleOpenApp()">Abrir Aplicación ↗</button>
                    <button class="btn-verify" id="ws-btn-verify" onclick="handleToggleVerify()">Marcar como vista</button>
                </div>
            </div>
        </div>

        <script>
        const APPS = {APPS_JSON};
        const TOTAL_APPS = APPS.length;
        const CARD_HEIGHT = 96;
        const LOOP_HEIGHT = TOTAL_APPS * CARD_HEIGHT;

        let currentScrollY = 0;
        let isDragging = false;
        let startY = 0;
        let startScrollY = 0;
        let focusedIndex = 0;
        let focusTimer = null;
        let hasShownCelebrationModal = false;
        let verifiedApps = new Set(JSON.parse(localStorage.getItem('krov_audit_seen') || '[]'));

        const viewport = document.getElementById('viewport');
        const cardsContainer = document.getElementById('cards-container');
        const vpHeight = viewport.clientHeight || 470;
        const centerOffset = (vpHeight / 2) - (CARD_HEIGHT / 2);

        // Construcción DOM de tarjetas
        APPS.forEach((app, idx) => {{
            const card = document.createElement('div');
            card.className = 'shelf-card';
            card.id = `card-${{idx}}`;

            const info = document.createElement('div');
            info.className = 'shelf-card-info';
            info.innerHTML = `
                <div class="shelf-card-title">
                    <span>${{app.icon}}</span> <span>${{app.titulo}}</span>
                    <span id="check-tag-${{app.id}}" style="font-size:0.72rem; color:${{app.color}}; margin-left:auto; font-family:'JetBrains Mono';">
                        ${{verifiedApps.has(app.id) ? '✓ VISTA' : '○'}}
                    </span>
                </div>
                <div class="shelf-card-desc">${{app.desc}}</div>
            `;

            const btnVer = document.createElement('button');
            btnVer.className = 'ejected-btn';
            btnVer.id = `btn-ver-${{idx}}`;
            btnVer.innerHTML = 'Ver ➔';
            btnVer.onclick = (e) => {{
                e.stopPropagation();
                snapToIndex(idx);
            }};

            card.appendChild(info);
            card.appendChild(btnVer);
            card.onclick = () => snapToIndex(idx);
            cardsContainer.appendChild(card);
        }});

        // --- PATERNOSTER INFINITO CONTINUO ---
        function updatePaternosterShelf() {{
            const cards = cardsContainer.children;
            let closestIdx = 0;
            let closestDist = Infinity;

            for (let i = 0; i < TOTAL_APPS; i++) {{
                const card = cards[i];
                const rawPos = (i * CARD_HEIGHT) + currentScrollY;

                let delta = (((rawPos % LOOP_HEIGHT) + LOOP_HEIGHT) % LOOP_HEIGHT);
                if (delta > LOOP_HEIGHT / 2) {{
                    delta -= LOOP_HEIGHT;
                }}

                const yPos = centerOffset + delta;
                const dist = Math.abs(delta);
                const normDist = dist / (vpHeight / 2);

                if (dist < closestDist) {{
                    closestDist = dist;
                    closestIdx = i;
                }}

                const opacity = Math.max(0.12, 1 - (normDist * 0.85));
                const scale = Math.max(0.85, 1 - (normDist * 0.15));
                const blur = Math.min(2.5, normDist * 2);

                card.style.transform = `translateY(${{yPos}}px) scale(${{scale}})`;
                card.style.opacity = opacity;
                card.style.filter = `blur(${{blur}}px)`;
            }}

            clearTimeout(focusTimer);
            hideAllEjectedButtons();

            if (closestIdx !== focusedIndex) {{
                focusedIndex = closestIdx;
                updateWorkstation(APPS[focusedIndex]);
            }}

            focusTimer = setTimeout(() => {{
                const activeBtn = document.getElementById(`btn-ver-${{focusedIndex}}`);
                if (activeBtn) {{
                    activeBtn.classList.add('visible');
                }}
            }}, 260);
        }}

        function hideAllEjectedButtons() {{
            const btns = document.querySelectorAll('.ejected-btn');
            btns.forEach(b => b.classList.remove('visible'));
        }}

        function snapToIndex(idx) {{
            let diff = idx - focusedIndex;
            if (diff > TOTAL_APPS / 2) diff -= TOTAL_APPS;
            if (diff < -TOTAL_APPS / 2) diff += TOTAL_APPS;

            currentScrollY -= diff * CARD_HEIGHT;
            updatePaternosterShelf();
        }}

        function dismissHint() {{
            const hint = document.getElementById('drag-hint');
            if (hint) {{
                hint.style.transition = 'opacity 0.35s ease';
                hint.style.opacity = '0';
                setTimeout(() => hint.remove(), 400);
            }}
        }}

        viewport.addEventListener('pointerdown', (e) => {{
            isDragging = true;
            startY = e.clientY;
            startScrollY = currentScrollY;
            viewport.setPointerCapture(e.pointerId);
            clearTimeout(focusTimer);
            hideAllEjectedButtons();
            dismissHint();
        }});

        viewport.addEventListener('pointermove', (e) => {{
            if (!isDragging) return;
            const dy = e.clientY - startY;
            currentScrollY = startScrollY + dy;
            updatePaternosterShelf();
        }});

        viewport.addEventListener('pointerup', (e) => {{
            if (!isDragging) return;
            isDragging = false;
            viewport.releasePointerCapture(e.pointerId);
            snapToIndex(focusedIndex);
        }});

        viewport.addEventListener('wheel', (e) => {{
            e.preventDefault();
            currentScrollY -= e.deltaY * 0.75;
            updatePaternosterShelf();
            snapToIndex(focusedIndex);
            dismissHint();
        }}, {{ passive: false }});

        window.addEventListener('keydown', (e) => {{
            if (e.key === 'ArrowUp') {{
                snapToIndex((focusedIndex - 1 + TOTAL_APPS) % TOTAL_APPS);
                dismissHint();
            }} else if (e.key === 'ArrowDown') {{
                snapToIndex((focusedIndex + 1) % TOTAL_APPS);
                dismissHint();
            }}
        }});

        // --- FLUJO DE AUDITORÍA ---
        function markAppAsSeen(id) {{
            if (!verifiedApps.has(id)) {{
                verifiedApps.add(id);
                localStorage.setItem('krov_audit_seen', JSON.stringify(Array.from(verifiedApps)));
                const checkTag = document.getElementById(`check-tag-${{id}}`);
                if (checkTag) checkTag.innerHTML = '✓ VISTA';
                updateAuditProgressBar();
            }}
        }}

        function handleOpenApp() {{
            const currentApp = APPS[focusedIndex];
            markAppAsSeen(currentApp.id);
            window.open(currentApp.url, '_blank');
            updateWorkstation(currentApp);
        }}

        function handleToggleVerify() {{
            const currentApp = APPS[focusedIndex];
            if (verifiedApps.has(currentApp.id)) {{
                verifiedApps.delete(currentApp.id);
                const checkTag = document.getElementById(`check-tag-${{currentApp.id}}`);
                if (checkTag) checkTag.innerHTML = '○';
            }} else {{
                verifiedApps.add(currentApp.id);
                const checkTag = document.getElementById(`check-tag-${{currentApp.id}}`);
                if (checkTag) checkTag.innerHTML = '✓ VISTA';
            }}
            localStorage.setItem('krov_audit_seen', JSON.stringify(Array.from(verifiedApps)));
            updateAuditProgressBar();
            updateWorkstation(currentApp);
        }}

        function updateAuditProgressBar() {{
            const count = verifiedApps.size;
            const pct = Math.round((count / TOTAL_APPS) * 100);
            document.getElementById('audit-stats-text').innerText = `${{String(count).padStart(2, '0')}} / ${{TOTAL_APPS}} (${{pct}}%)`;
            document.getElementById('audit-progress-fill').style.width = `${{Math.max(4, pct)}}%`;

            if (count === TOTAL_APPS) {{
                if (window.parent) {{
                    window.parent.__GALAXY_HYPERSPACE__ = true;
                }}
                if (!hasShownCelebrationModal) {{
                    document.getElementById('completion-modal').classList.add('active');
                    hasShownCelebrationModal = true;
                }}
            }} else {{
                if (window.parent) {{
                    window.parent.__GALAXY_HYPERSPACE__ = false;
                }}
            }}
        }}

        function dismissModal() {{
            document.getElementById('completion-modal').classList.remove('active');
        }}

        function updateWorkstation(app) {{
            document.getElementById('paternoster-counter').innerText = `${{String(app.id).padStart(2, '0')}} / ${{TOTAL_APPS}}`;
            document.getElementById('ws-cat').innerText = app.cat.toUpperCase();
            document.getElementById('ws-cat').style.color = app.color;
            document.getElementById('ws-counter').innerText = `#${{String(app.id).padStart(2, '0')}} / ${{TOTAL_APPS}}`;
            document.getElementById('ws-title').innerText = app.titulo;
            document.getElementById('ws-desc').innerText = app.desc;
            document.getElementById('ws-uso').innerText = app.uso;

            const ws = document.getElementById('workstation');
            ws.style.borderTopColor = app.color;
            document.getElementById('ws-box').style.borderLeftColor = app.color;
            document.getElementById('ws-box-lbl').style.color = app.color;

            const btnVerify = document.getElementById('ws-btn-verify');
            if (verifiedApps.has(app.id)) {{
                btnVerify.innerText = '✓ Marcada como vista';
                btnVerify.classList.add('checked');
            }} else {{
                btnVerify.innerText = 'Marcar como vista';
                btnVerify.classList.remove('checked');
            }}

            renderHUD(app.svg_type, app.color);
        }}

        function renderHUD(type, color) {{
            const hudContainer = document.getElementById('ws-hud');
            if (type === 'iot') {{
                hudContainer.innerHTML = `
                    <svg width="220" height="135" viewBox="0 0 220 135">
                        <style>
                            .spin-r {{ transform-origin: 110px 68px; animation: rClock 10s linear infinite; }}
                            .pulse-w {{ animation: pW 1.8s ease-in-out infinite alternate; }}
                            @keyframes rClock {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}
                            @keyframes pW {{ 0% {{ opacity: 0.3; r: 35px; }} 100% {{ opacity: 0.9; r: 50px; }} }}
                        </style>
                        <circle cx="110" cy="68" r="52" fill="none" stroke="rgba(203,213,225,0.15)" stroke-width="1" stroke-dasharray="4 4"/>
                        <circle class="pulse-w" cx="110" cy="68" r="45" fill="none" stroke="${{color}}" stroke-width="1.4"/>
                        <circle class="spin-r" cx="110" cy="68" r="26" fill="none" stroke="#cbd5e1" stroke-width="1.2" stroke-dasharray="6 4"/>
                        <circle cx="110" cy="68" r="5" fill="#38bdf8"/>
                        <text x="110" y="128" font-family="'JetBrains Mono'" font-size="8" fill="#cbd5e1" text-anchor="middle">MQTT NODO ENLACE PERSISTENTE</text>
                    </svg>
                `;
            }} else if (type === 'vision') {{
                hudContainer.innerHTML = `
                    <svg width="220" height="135" viewBox="0 0 220 135">
                        <style>
                            .sw {{ animation: swY 2.4s ease-in-out infinite alternate; }}
                            .rc {{ transform-origin: 110px 68px; animation: rClock 12s linear infinite; }}
                            @keyframes swY {{ 0% {{ transform: translateY(16px); }} 100% {{ transform: translateY(118px); }} }}
                        </style>
                        <rect x="18" y="12" width="184" height="110" fill="none" stroke="rgba(203,213,225,0.18)" stroke-width="1" rx="6"/>
                        <circle class="rc" cx="110" cy="68" r="40" fill="none" stroke="${{color}}" stroke-width="1.3" stroke-dasharray="8 5"/>
                        <rect x="78" y="38" width="64" height="60" fill="none" stroke="${{color}}" stroke-width="1.2"/>
                        <line class="sw" x1="20" y1="0" x2="200" y2="0" stroke="${{color}}" stroke-width="1.6"/>
                        <text x="110" y="72" font-family="'JetBrains Mono'" font-size="8.5" fill="#ffffff" text-anchor="middle">TRACKING ÓPTICO</text>
                    </svg>
                `;
            }} else if (type === 'audio') {{
                hudContainer.innerHTML = `
                    <svg width="220" height="135" viewBox="0 0 220 135">
                        <style>
                            .b1 {{ transform-origin: bottom; animation: bS 0.9s ease-in-out infinite alternate; }}
                            .b2 {{ transform-origin: bottom; animation: bS 0.7s ease-in-out infinite 0.2s alternate; }}
                            @keyframes bS {{ 0% {{ transform: scaleY(0.3); }} 100% {{ transform: scaleY(1.2); }} }}
                        </style>
                        <circle cx="110" cy="65" r="38" fill="none" stroke="#cbd5e1" stroke-width="1" opacity="0.25"/>
                        <g transform="translate(64, 65)">
                            <rect class="b1" x="0" y="-18" width="6" height="36" rx="2" fill="${{color}}"/>
                            <rect class="b2" x="15" y="-28" width="6" height="56" rx="2" fill="#38bdf8"/>
                            <rect class="b1" x="30" y="-36" width="6" height="72" rx="2" fill="${{color}}"/>
                            <rect class="b2" x="45" y="-24" width="6" height="48" rx="2" fill="#c084fc"/>
                            <rect class="b1" x="60" y="-14" width="6" height="28" rx="2" fill="#cbd5e1"/>
                        </g>
                        <text x="110" y="128" font-family="'JetBrains Mono'" font-size="8.5" fill="#cbd5e1" text-anchor="middle">SÍNTESIS ACÚSTICA HARMONIC</text>
                    </svg>
                `;
            }} else {{
                hudContainer.innerHTML = `
                    <svg width="220" height="135" viewBox="0 0 220 135">
                        <style>
                            .rn {{ transform-origin: 110px 68px; animation: rClock 16s linear infinite; }}
                            .pn {{ animation: pW 2s ease-in-out infinite alternate; }}
                        </style>
                        <circle class="rn" cx="110" cy="68" r="48" fill="none" stroke="rgba(203,213,225,0.18)" stroke-width="1" stroke-dasharray="8 6"/>
                        <circle class="pn" cx="110" cy="68" r="26" fill="none" stroke="${{color}}" stroke-width="1.3"/>
                        <circle cx="110" cy="68" r="5" fill="#38bdf8"/>
                        <text x="110" y="128" font-family="'JetBrains Mono'" font-size="8.5" fill="#cbd5e1" text-anchor="middle">RED TENSORES VECTORIAL</text>
                    </svg>
                `;
            }}
        }}

        // Inicialización del estante en el primer ítem
        updatePaternosterShelf();
        updateAuditProgressBar();
        snapToIndex(0);
        </script>
        </body>
        </html>
        """,
        height=685
    )

# ==============================================================================
# PESTAÑA 2: DIRECTORIO COMPLETO
# ==============================================================================
with tab_matriz:
    grid_cards_html = ['<div class="grid-container">']
    for item in CATALOGO:
        grid_cards_html.append(f"""
        <div class="grid-card" style="border-top-color:{item['color']};">
            <div>
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                    <span style="font-size:1.25rem;">{item['icon']}</span>
                    <span style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{item['color']}; font-weight:700;">#{item['id']:02d}</span>
                </div>
                <div style="font-weight:700; font-size:0.95rem; color:#ffffff; line-height:1.25; margin-bottom:4px;">{item['titulo']}</div>
                <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{item['color']}; margin-bottom:8px; text-transform:uppercase;">● {item['cat']}</div>
                <p style="font-size:0.82rem; color:#94a3b8; line-height:1.45; margin-bottom:10px;">{item['desc']}</p>
            </div>
            <a href="{item['url']}" target="_blank" class="grid-link"
               style="background:{item['color']}18; border:1px solid {item['color']}44; color:{item['color']};">
                Abrir aplicación ↗
            </a>
        </div>
        """)
    grid_cards_html.append('</div>')

    render_clean_html("".join(grid_cards_html))

st.write("")
render_clean_html("""
<div style="text-align:center; padding:1.2rem 0; border-top:1px solid rgba(203,213,225,0.12); margin-top:1.2rem;">
    <div style="font-family:'JetBrains Mono'; font-size:0.72rem; letter-spacing:0.25em; color:#cbd5e1; text-transform:uppercase;">
        JUAN DAVID SEGURA · PORTAFOLIO DE SISTEMAS E INTERFACES MULTIMODALES
    </div>
    <div style="font-size:0.8rem; color:#64748b; margin-top:4px;">
        19 aplicaciones desplegadas sobre Streamlit Cloud
    </div>
</div>
""")
