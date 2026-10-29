import streamlit as st
import streamlit.components.v1 as components
import json

# ==============================================================================
# 1. CONFIGURACIÓN GENERAL Y FAVICON
# ==============================================================================
st.set_page_config(
    page_title="Portafolio // Sistemas e Interfaces Multimodales",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

def render_clean_html(html_str: str):
    compact = "".join(line.strip() for line in html_str.splitlines() if line.strip())
    st.markdown(compact, unsafe_allow_html=True)

# ==============================================================================
# 2. CATÁLOGO MAESTRO (19 APLICACIONES // LENGUAJE LACÓNICO)
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
        "uso": "Digitalización automática de formularios y cheques bancarios.",
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
# 3. ESTILOS BASE Y AMBIENTACIÓN CÓSMICA
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
    max-width: 1360px !important;
    padding-top: 0.8rem !important;
    padding-bottom: 2rem !important;
    margin: 0 auto !important;
}

.header-deck {
    text-align: center;
    margin-bottom: 1.2rem;
}

.brand-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.28em;
    color: #cbd5e1;
    text-transform: uppercase;
}

.hero-title {
    font-size: clamp(1.8rem, 3.2vw, 2.7rem);
    font-weight: 700;
    color: #ffffff;
    line-height: 1.2;
    margin: 0.2rem 0;
    letter-spacing: -0.02em;
    text-shadow: 0 0 25px rgba(56, 189, 248, 0.35);
}

.hero-sub {
    color: #94a3b8;
    font-size: 0.92rem;
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
# 4. CANVAS GPU DE ALTA EFICIENCIA (FONDO PLASMA NEÓN)
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
        const scale = pWin.innerWidth < 768 ? 0.45 : 0.65;
        let w = canvas.width = Math.floor(pWin.innerWidth * scale);
        let h = canvas.height = Math.floor(pWin.innerHeight * scale);

        pWin.addEventListener('resize', () => {
            w = canvas.width = Math.floor(pWin.innerWidth * scale);
            h = canvas.height = Math.floor(pWin.innerHeight * scale);
        });

        const orbs = [
            { x: w * 0.15, y: h * 0.25, r: 190 * scale, vx: 0.35, vy: 0.25, color: 'rgba(37, 99, 235, 0.25)' },
            { x: w * 0.85, y: h * 0.35, r: 210 * scale, vx: -0.3, vy: 0.35, color: 'rgba(56, 189, 248, 0.22)' },
            { x: w * 0.5,  y: h * 0.85, r: 180 * scale, vx: 0.25, vy: -0.3, color: 'rgba(124, 58, 237, 0.20)' }
        ];

        const pColors = ['#38bdf8', '#818cf8', '#c084fc', '#93c5fd', '#cbd5e1'];
        const pCount = pWin.innerWidth < 768 ? 14 : 22;
        const particles = [];
        for (let i = 0; i < pCount; i++) {
            particles.push({
                x: Math.random() * w,
                y: Math.random() * h,
                r: Math.random() * 1.5 + 0.6,
                vx: (Math.random() - 0.5) * 0.4,
                vy: (Math.random() - 0.5) * 0.4,
                color: pColors[i % pColors.length]
            });
        }

        function loop() {
            ctx.fillStyle = '#04060d';
            ctx.fillRect(0, 0, w, h);

            ctx.globalCompositeOperation = 'screen';
            for (let b of orbs) {
                b.x += b.vx;
                b.y += b.vy;
                if (b.x < -40 || b.x > w + 40) b.vx *= -1;
                if (b.y < -40 || b.y > h + 40) b.vy *= -1;

                const g = ctx.createRadialGradient(b.x, b.y, 2, b.x, b.y, b.r);
                g.addColorStop(0, b.color);
                g.addColorStop(1, 'rgba(4, 6, 13, 0)');
                ctx.beginPath();
                ctx.arc(b.x, b.y, b.r, 0, Math.PI * 2);
                ctx.fillStyle = g;
                ctx.fill();
            }

            ctx.globalCompositeOperation = 'lighter';
            for (let i = 0; i < particles.length; i++) {
                const p = particles[i];
                p.x += p.vx;
                p.y += p.vy;
                if (p.x < 0) p.x = w;
                if (p.x > w) p.x = 0;
                if (p.y < 0) p.y = h;
                if (p.y > h) p.y = 0;

                ctx.beginPath();
                ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
                ctx.fillStyle = p.color;
                ctx.fill();
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
# 5. ENCABEZADO Y AUDITORÍA MAESTRA
# ==============================================================================
render_clean_html("""
<div class="header-deck">
    <div class="brand-label">Portafolio de Sistemas</div>
    <div class="hero-title">Interfaces Multimodales</div>
    <div class="hero-sub">19 aplicaciones de visión artificial, modelos de lenguaje, telemetría IoT y acústica.</div>
</div>
""")

tab_estacion, tab_matriz = st.tabs(["Estación de Inspección Paternoster", "Directorio Completo"])

# ==============================================================================
# PESTAÑA 1: PATERNOSTER DRAGGABLE SHELF + WORKSTATION LATERAL
# ==============================================================================
with tab_estacion:
    # Componente integrado de alta reactividad con física de arrastre y eyección de botón
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

            .deck-wrapper {{
                display: flex;
                gap: 24px;
                width: 100%;
                height: 620px;
                padding: 6px;
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
                margin-bottom: 12px;
                padding-bottom: 10px;
                border-bottom: 1px solid rgba(255, 255, 255, 0.08);
                font-family: 'JetBrains Mono', monospace;
                font-size: 0.74rem;
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
                box-shadow: 0 0 25px rgba(56, 189, 248, 0.2), inset 0 0 15px rgba(56, 189, 248, 0.1);
                z-index: 2;
            }}

            .paternoster-track {{
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                will-change: transform;
            }}

            .shelf-card {{
                position: relative;
                height: 86px;
                margin-bottom: 10px;
                background: rgba(12, 19, 38, 0.88);
                border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 8px;
                padding: 12px 16px;
                display: flex;
                align-items: center;
                justify-content: space-between;
                transition: opacity 0.15s ease, transform 0.15s ease, filter 0.15s ease;
                transform-origin: center center;
            }}

            .shelf-card-info {{
                flex: 1;
                padding-right: 12px;
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
                font-size: 0.8rem;
                color: #94a3b8;
                margin-top: 3px;
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
            }}

            /* --- BOTÓN «VER» EYECTADO LATERALMENTE --- */
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
                transition: transform 0.24s cubic-bezier(0.175, 0.885, 0.32, 1.275), opacity 0.2s ease;
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

            /* --- ESTACIÓN DE INSPECCIÓN LATERAL (WORKSTATION) --- */
            .workstation-container {{
                flex: 1.05;
                background: linear-gradient(145deg, rgba(12, 18, 38, 0.98) 0%, rgba(6, 10, 22, 0.98) 100%);
                border: 1px solid rgba(56, 189, 248, 0.28);
                border-top: 3px solid #38bdf8;
                border-radius: 14px;
                padding: 24px;
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
                margin-bottom: 8px;
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
                font-size: 1.65rem;
                font-weight: 700;
                color: #ffffff;
                margin: 4px 0 8px 0;
            }}

            .workstation-desc {{
                font-size: 0.94rem;
                color: #cbd5e1;
                line-height: 1.5;
                margin-bottom: 12px;
            }}

            .workstation-box {{
                background: rgba(56, 189, 248, 0.06);
                border-left: 3px solid #38bdf8;
                border-radius: 6px;
                padding: 10px 14px;
                margin-bottom: 14px;
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
                padding: 12px;
                display: flex;
                align-items: center;
                justify-content: center;
                margin-bottom: 16px;
                box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.8);
            }}

            .action-deck {{
                display: flex;
                gap: 12px;
            }}

            .btn-primary {{
                flex: 1.6;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 45%, #7c3aed 100%);
                color: #ffffff;
                text-decoration: none;
                font-family: 'JetBrains Mono', monospace;
                font-weight: 700;
                font-size: 0.88rem;
                border-radius: 6px;
                padding: 12px;
                box-shadow: 0 0 20px rgba(37, 99, 235, 0.5);
                border: 1px solid rgba(226, 232, 240, 0.25);
                transition: all 0.2s ease;
            }}

            .btn-primary:hover {{
                box-shadow: 0 0 30px rgba(56, 189, 248, 0.7);
                transform: translateY(-1px);
            }}

            .btn-verify {{
                flex: 1.1;
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
        </style>
        </head>
        <body>

        <div class="deck-wrapper">
            <!-- ESTANTE PATERNOSTER -->
            <div class="paternoster-container">
                <div class="paternoster-header">
                    <span style="color:#cbd5e1;">ESTANTE PATERNOSTER // ENLACE CINEMÁTICO</span>
                    <span id="paternoster-status" style="color:#38bdf8;">ARRASTRE O GIRO ↕</span>
                </div>
                
                <div class="paternoster-viewport" id="viewport">
                    <div class="paternoster-aperture"></div>
                    <div class="paternoster-track" id="track"></div>
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
                        <div style="font-size:0.88rem; color:#cbd5e1;" id="ws-uso">Control de aforo y logística de inventario.</div>
                    </div>
                </div>

                <div class="workstation-hud" id="ws-hud"></div>

                <div class="action-deck">
                    <a href="#" target="_blank" class="btn-primary" id="ws-link">Abrir Aplicación ↗</a>
                    <button class="btn-verify" id="ws-btn-verify" onclick="toggleVerification()">Marcar Verificada</button>
                </div>
            </div>
        </div>

        <script>
        const APPS = {APPS_JSON};
        const CARD_HEIGHT = 96; // 86px + 10px margen
        let currentY = 0;
        let isDragging = false;
        let startY = 0;
        let startScrollY = 0;
        let focusedIndex = 0;
        let verifiedApps = new Set(JSON.parse(localStorage.getItem('krov_verified_apps') || '[]'));

        const track = document.getElementById('track');
        const viewport = document.getElementById('viewport');
        const vpHeight = viewport.clientHeight || 510;
        const centerOffset = (vpHeight / 2) - (CARD_HEIGHT / 2);

        // Construcción DOM de tarjetas en el estante
        APPS.forEach((app, idx) => {{
            const card = document.createElement('div');
            card.className = 'shelf-card';
            card.id = `card-${{idx}}`;

            const info = document.createElement('div');
            info.className = 'shelf-card-info';
            info.innerHTML = `
                <div class="shelf-card-title">
                    <span>${{app.icon}}</span> <span>${{app.titulo}}</span>
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
            track.appendChild(card);
        }});

        function updateCardsVisuals() {{
            const cards = track.children;
            let closestIdx = 0;
            let closestDist = Infinity;

            for (let i = 0; i < cards.length; i++) {{
                const card = cards[i];
                const cardCenter = (i * CARD_HEIGHT) + currentY + (CARD_HEIGHT / 2);
                const viewportCenter = vpHeight / 2;
                const dist = Math.abs(viewportCenter - cardCenter);
                const normalizedDist = dist / (vpHeight / 2);

                if (dist < closestDist) {{
                    closestDist = dist;
                    closestIdx = i;
                }}

                // Profundidad de campo: opacidad, escala y desenfoque relativos al foco
                const opacity = Math.max(0.18, 1 - (normalizedDist * 0.78));
                const scale = Math.max(0.86, 1 - (normalizedDist * 0.14));
                const blur = Math.min(2.5, normalizedDist * 1.8);

                card.style.opacity = opacity;
                card.style.transform = `scale(${{scale}})`;
                card.style.filter = `blur(${{blur}}px)`;

                // Eyección lateral del botón de inspección
                const btn = document.getElementById(`btn-ver-${{i}}`);
                if (btn) {{
                    if (dist < (CARD_HEIGHT / 2)) {{
                        btn.classList.add('visible');
                    }} else {{
                        btn.classList.remove('visible');
                    }}
                }}
            }}

            if (closestIdx !== focusedIndex) {{
                focusedIndex = closestIdx;
                updateWorkstation(APPS[focusedIndex]);
            }}
        }}

        function setTrackPosition(y) {{
            const minY = -((APPS.length - 1) * CARD_HEIGHT) + centerOffset;
            const maxY = centerOffset;
            currentY = Math.max(minY, Math.min(maxY, y));
            track.style.transform = `translateY(${{currentY}}px)`;
            updateCardsVisuals();
        }}

        function snapToIndex(idx) {{
            focusedIndex = Math.max(0, Math.min(APPS.length - 1, idx));
            const targetY = -(focusedIndex * CARD_HEIGHT) + centerOffset;
            setTrackPosition(targetY);
        }}

        // Gestores de arrastre continuo con ratón (Pointer Events)
        viewport.addEventListener('pointerdown', (e) => {{
            isDragging = true;
            startY = e.clientY;
            startScrollY = currentY;
            viewport.setPointerCapture(e.pointerId);
        }});

        viewport.addEventListener('pointermove', (e) => {{
            if (!isDragging) return;
            const dy = e.clientY - startY;
            setTrackPosition(startScrollY + dy);
        }});

        viewport.addEventListener('pointerup', (e) => {{
            if (!isDragging) return;
            isDragging = false;
            viewport.releasePointerCapture(e.pointerId);
            snapToIndex(focusedIndex);
        }});

        viewport.addEventListener('wheel', (e) => {{
            e.preventDefault();
            setTrackPosition(currentY - (e.deltaY * 0.7));
            snapToIndex(focusedIndex);
        }}, {{ passive: false }});

        // Actualización reactiva de la estación de trabajo lateral
        function updateWorkstation(app) {{
            document.getElementById('ws-cat').innerText = app.cat.toUpperCase();
            document.getElementById('ws-cat').style.color = app.color;
            document.getElementById('ws-counter').innerText = `#${{String(app.id).padStart(2, '0')}} / 19`;
            document.getElementById('ws-title').innerText = app.titulo;
            document.getElementById('ws-desc').innerText = app.desc;
            document.getElementById('ws-uso').innerText = app.uso;
            document.getElementById('ws-link').href = app.url;

            const ws = document.getElementById('workstation');
            ws.style.borderTopColor = app.color;
            document.getElementById('ws-box').style.borderLeftColor = app.color;
            document.getElementById('ws-box-lbl').style.color = app.color;

            const btnVerify = document.getElementById('ws-btn-verify');
            if (verifiedApps.has(app.id)) {{
                btnVerify.innerText = '✓ Verificada';
                btnVerify.classList.add('checked');
            }} else {{
                btnVerify.innerText = 'Marcar Verificada';
                btnVerify.classList.remove('checked');
            }}

            renderHUD(app.svg_type, app.color);
        }}

        function toggleVerification() {{
            const currentApp = APPS[focusedIndex];
            if (verifiedApps.has(currentApp.id)) {{
                verifiedApps.delete(currentApp.id);
            }} else {{
                verifiedApps.add(currentApp.id);
            }}
            localStorage.setItem('krov_verified_apps', JSON.stringify(Array.from(verifiedApps)));
            updateWorkstation(currentApp);
        }}

        // Generador de HUDs hiper-saturados
        function renderHUD(type, color) {{
            const hudContainer = document.getElementById('ws-hud');
            if (type === 'iot') {{
                hudContainer.innerHTML = `
                    <svg width="220" height="145" viewBox="0 0 220 145">
                        <style>
                            .spin-r {{ transform-origin: 110px 72px; animation: rClock 10s linear infinite; }}
                            .pulse-w {{ animation: pW 1.8s ease-in-out infinite alternate; }}
                            @keyframes rClock {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}
                            @keyframes pW {{ 0% {{ opacity: 0.3; r: 35px; }} 100% {{ opacity: 0.9; r: 52px; }} }}
                        </style>
                        <circle cx="110" cy="72" r="54" fill="none" stroke="rgba(203,213,225,0.15)" stroke-width="1" stroke-dasharray="4 4"/>
                        <circle class="pulse-w" cx="110" cy="72" r="45" fill="none" stroke="${{color}}" stroke-width="1.4"/>
                        <circle class="spin-r" cx="110" cy="72" r="28" fill="none" stroke="#cbd5e1" stroke-width="1.2" stroke-dasharray="6 4"/>
                        <circle cx="110" cy="72" r="6" fill="#38bdf8"/>
                        <text x="110" y="138" font-family="'JetBrains Mono'" font-size="8.5" fill="#cbd5e1" text-anchor="middle">MQTT NODO ENLACE PERSISTENTE</text>
                    </svg>
                `;
            }} else if (type === 'vision') {{
                hudContainer.innerHTML = `
                    <svg width="220" height="145" viewBox="0 0 220 145">
                        <style>
                            .sweep {{ animation: swY 2.4s ease-in-out infinite alternate; }}
                            .rot-c {{ transform-origin: 110px 72px; animation: rClock 12s linear infinite; }}
                            @keyframes swY {{ 0% {{ transform: translateY(18px); }} 100% {{ transform: translateY(124px); }} }}
                        </style>
                        <rect x="15" y="14" width="190" height="116" fill="none" stroke="rgba(203,213,225,0.18)" stroke-width="1" rx="6"/>
                        <circle class="rot-c" cx="110" cy="72" r="42" fill="none" stroke="${{color}}" stroke-width="1.3" stroke-dasharray="8 5"/>
                        <rect x="78" y="42" width="64" height="60" fill="none" stroke="${{color}}" stroke-width="1.2"/>
                        <line class="sweep" x1="18" y1="0" x2="202" y2="0" stroke="${{color}}" stroke-width="1.6"/>
                        <text x="110" y="76" font-family="'JetBrains Mono'" font-size="8.5" fill="#ffffff" text-anchor="middle">TRACKING ÓPTICO</text>
                    </svg>
                `;
            }} else if (type === 'audio') {{
                hudContainer.innerHTML = `
                    <svg width="220" height="145" viewBox="0 0 220 145">
                        <style>
                            .b1 {{ transform-origin: bottom; animation: bS 0.9s ease-in-out infinite alternate; }}
                            .b2 {{ transform-origin: bottom; animation: bS 0.7s ease-in-out infinite 0.2s alternate; }}
                            @keyframes bS {{ 0% {{ transform: scaleY(0.3); }} 100% {{ transform: scaleY(1.2); }} }}
                        </style>
                        <circle cx="110" cy="68" r="40" fill="none" stroke="#cbd5e1" stroke-width="1" opacity="0.25"/>
                        <g transform="translate(62, 68)">
                            <rect class="b1" x="0" y="-20" width="7" height="40" rx="2" fill="${{color}}"/>
                            <rect class="b2" x="16" y="-30" width="7" height="60" rx="2" fill="#38bdf8"/>
                            <rect class="b1" x="32" y="-38" width="7" height="76" rx="2" fill="${{color}}"/>
                            <rect class="b2" x="48" y="-26" width="7" height="52" rx="2" fill="#c084fc"/>
                            <rect class="b1" x="64" y="-16" width="7" height="32" rx="2" fill="#cbd5e1"/>
                        </g>
                        <text x="110" y="136" font-family="'JetBrains Mono'" font-size="8.5" fill="#cbd5e1" text-anchor="middle">SÍNTESIS ACÚSTICA HARMONIC</text>
                    </svg>
                `;
            }} else {{
                hudContainer.innerHTML = `
                    <svg width="220" height="145" viewBox="0 0 220 145">
                        <style>
                            .rot-n {{ transform-origin: 110px 72px; animation: rClock 16s linear infinite; }}
                            .pul-n {{ animation: pW 2s ease-in-out infinite alternate; }}
                        </style>
                        <circle class="rot-n" cx="110" cy="72" r="50" fill="none" stroke="rgba(203,213,225,0.18)" stroke-width="1" stroke-dasharray="8 6"/>
                        <circle class="pul-n" cx="110" cy="72" r="28" fill="none" stroke="${{color}}" stroke-width="1.3"/>
                        <circle cx="110" cy="72" r="6" fill="#38bdf8"/>
                        <text x="110" y="136" font-family="'JetBrains Mono'" font-size="8.5" fill="#cbd5e1" text-anchor="middle">RED TENSORES CLASIFICACIÓN</text>
                    </svg>
                `;
            }}
        }}

        // Inicialización inmediata en el índice 0
        snapToIndex(0);
        </script>
        </body>
        </html>
        """,
        height=640
    )

# ==============================================================================
# PESTAÑA 2: DIRECTORIO COMPLETO EN MATRIZ (19 APLICACIONES)
# ==============================================================================
with tab_matriz:
    st.caption("Visión panorámica de las 19 aplicaciones desarrolladas.")

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
<div style="text-align:center; padding:1.5rem 0; border-top:1px solid rgba(203,213,225,0.12); margin-top:1.5rem;">
    <div style="font-family:'JetBrains Mono'; font-size:0.72rem; letter-spacing:0.2em; color:#cbd5e1; text-transform:uppercase;">
        PORTAFOLIO DE SISTEMAS E INTERFACES MULTIMODALES
    </div>
    <div style="font-size:0.8rem; color:#64748b; margin-top:4px;">
        19 aplicaciones desplegadas sobre Streamlit Cloud
    </div>
</div>
""")
