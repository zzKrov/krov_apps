import streamlit as st
import streamlit.components.v1 as components

# ==============================================================================
# 1. CONFIGURACIÓN GENERAL Y FAVICON
# ==============================================================================
st.set_page_config(
    page_title="Portafolio // Sistemas e Interfaces",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Compactador estricto para evitar fugas de código Markdown (<pre><code>)
def render_clean_html(html_str: str):
    compact = "".join(line.strip() for line in html_str.splitlines() if line.strip())
    st.markdown(compact, unsafe_allow_html=True)

# ==============================================================================
# 2. ESTADO DE SESIÓN
# ==============================================================================
if "selected_id" not in st.session_state:
    st.session_state.selected_id = 1

if "visited_apps" not in st.session_state:
    st.session_state.visited_apps = set()

# ==============================================================================
# 3. PALETA POR DOMINIO (AZULES, PÚRPURAS Y PLATINO)
# ==============================================================================
DOMINIOS = {
    "Visión y Óptica":           {"color": "#38bdf8", "tag": "Cian Eléctrico"},
    "IoT y Ciberfísica":         {"color": "#22d3ee", "tag": "Cian Digital"},
    "Actuación y Hardware":      {"color": "#3b82f6", "tag": "Zafiro Estelar"},
    "Lenguaje y RAG":            {"color": "#818cf8", "tag": "Índigo Vectorial"},
    "Voz y Acústica":            {"color": "#c084fc", "tag": "Violeta Vocal"},
    "Redes y Modelado":          {"color": "#8b5cf6", "tag": "Púrpura Real"},
    "Interacción y Creatividad": {"color": "#6366f1", "tag": "Cobalto Profundo"}
}

# ==============================================================================
# 4. CATÁLOGO MAESTRO (19 APLICACIONES // LENGUAJE LACÓNICO)
# ==============================================================================
CATALOGO = [
    {
        "id": 1,
        "titulo": "Detector de Objetos",
        "cat": "Visión y Óptica",
        "url": "https://yolozz.streamlit.app",
        "icon": "🎯",
        "svg_type": "vision",
        "desc": "Encuadra y cuantifica 80 clases comunes de objetos en video e imágenes.",
        "uso": "Control de aforo y logística de inventario.",
        "color": DOMINIOS["Visión y Óptica"]["color"]
    },
    {
        "id": 2,
        "titulo": "Nube de Palabras",
        "cat": "Lenguaje y RAG",
        "url": "https://wordcloudz.streamlit.app",
        "icon": "☁️",
        "svg_type": "text",
        "desc": "Composición gráfica ponderada según la frecuencia léxica del texto.",
        "uso": "Extracción rápida de conceptos clave en reseñas.",
        "color": DOMINIOS["Lenguaje y RAG"]["color"]
    },
    {
        "id": 3,
        "titulo": "Dígitos Ópticos",
        "cat": "Redes y Modelado",
        "url": "https://mnistz.streamlit.app",
        "icon": "✍️",
        "svg_type": "neural",
        "desc": "Reconocimiento de números manuscritos del 0 al 9 trazados en pantalla.",
        "uso": "Digitalización de formularios y comprobantes bancarios.",
        "color": DOMINIOS["Redes y Modelado"]["color"]
    },
    {
        "id": 4,
        "titulo": "Análisis Contextual",
        "cat": "Visión y Óptica",
        "url": "https://visionz.streamlit.app",
        "icon": "👁️",
        "svg_type": "vision",
        "desc": "Evaluación semántica y redacción técnica descriptiva de cualquier escena.",
        "uso": "Inspección pericial de daños e informes de aseguradoras.",
        "color": DOMINIOS["Visión y Óptica"]["color"]
    },
    {
        "id": 5,
        "titulo": "Traductor de Voz",
        "cat": "Voz y Acústica",
        "url": "https://traductorz.streamlit.app",
        "icon": "🎙️",
        "svg_type": "audio",
        "desc": "Captura vocal por micrófono, traducción inmediata y reproducción fonética.",
        "uso": "Comunicación multilingüe en ventanillas de servicio.",
        "color": DOMINIOS["Voz y Acústica"]["color"]
    },
    {
        "id": 6,
        "titulo": "Detector de Postura",
        "cat": "Visión y Óptica",
        "url": "https://teachablez.streamlit.app",
        "icon": "🛡️",
        "svg_type": "vision",
        "desc": "Monitoreo corporal en cliente sin subir video a servidores externos.",
        "uso": "Supervisión ergonómica e interfaces sin contacto físico.",
        "color": DOMINIOS["Visión y Óptica"]["color"]
    },
    {
        "id": 7,
        "titulo": "Pausa y Bienestar",
        "cat": "Interacción y Creatividad",
        "url": "https://bendover.streamlit.app",
        "icon": "🐇",
        "svg_type": "creative",
        "desc": "Entorno antiestrés con partículas reactivas al cursor y síntesis de voz.",
        "uso": "Pausas activas y reducción de la fatiga en pantalla.",
        "color": DOMINIOS["Interacción y Creatividad"]["color"]
    },
    {
        "id": 8,
        "titulo": "Conversación Guiada",
        "cat": "Interacción y Creatividad",
        "url": "https://sentimentz.streamlit.app",
        "icon": "🤖",
        "svg_type": "text",
        "desc": "Diálogo interactivo con detección de tono anímico y retroalimentación serena.",
        "uso": "Bitácoras personales y redacción asistida bajo estrés.",
        "color": DOMINIOS["Interacción y Creatividad"]["color"]
    },
    {
        "id": 9,
        "titulo": "Visor de Texto 3D",
        "cat": "Visión y Óptica",
        "url": "https://ocryaudioz.streamlit.app",
        "icon": "🪞",
        "svg_type": "vision",
        "desc": "Extracción óptica de texto y proyección interactiva sobre plano tridimensional.",
        "uso": "Traducción y lectura de señalética o menús físicos.",
        "color": DOMINIOS["Visión y Óptica"]["color"]
    },
    {
        "id": 10,
        "titulo": "Digitalizador Óptico",
        "cat": "Visión y Óptica",
        "url": "https://lectorz.streamlit.app",
        "icon": "📷",
        "svg_type": "vision",
        "desc": "Conversión inmediata de capturas de cámara web en texto editable.",
        "uso": "Transcripción ágil de citas y archivo de facturas impresas.",
        "color": DOMINIOS["Visión y Óptica"]["color"]
    },
    {
        "id": 11,
        "titulo": "Interfaces Sensoriales",
        "cat": "Voz y Acústica",
        "url": "https://sussusamogus.streamlit.app",
        "icon": "✦",
        "svg_type": "audio",
        "desc": "Señalización mediante pulsos de luz, tonos audibles y vibración física.",
        "uso": "Sistemas de advertencia para cabinas y accesibilidad sensorial.",
        "color": DOMINIOS["Voz y Acústica"]["color"]
    },
    {
        "id": 12,
        "titulo": "Tablero de Bocetos",
        "cat": "Interacción y Creatividad",
        "url": "https://drawrecogz.streamlit.app",
        "icon": "🎨",
        "svg_type": "creative",
        "desc": "Lienzo de dibujo digital con interpretación visual automática de formas.",
        "uso": "Conceptualización gráfica y lluvia de ideas tempranas.",
        "color": DOMINIOS["Interacción y Creatividad"]["color"]
    },
    {
        "id": 13,
        "titulo": "Consulta sobre PDF",
        "cat": "Lenguaje y RAG",
        "url": "https://chatpdfz.streamlit.app",
        "icon": "💬",
        "svg_type": "text",
        "desc": "Resolución de preguntas basándose estrictamente en el contenido de un archivo PDF.",
        "uso": "Auditoría de contratos y estudio de manuales de ingeniería.",
        "color": DOMINIOS["Lenguaje y RAG"]["color"]
    },
    {
        "id": 14,
        "titulo": "Analizador de Tono",
        "cat": "Lenguaje y RAG",
        "url": "https://textanalysiz.streamlit.app",
        "icon": "⚖️",
        "svg_type": "text",
        "desc": "Diagnóstico de neutralidad, carga subjetiva y polaridad emocional de mensajes.",
        "uso": "Revisión formal de comunicaciones corporativas.",
        "color": DOMINIOS["Lenguaje y RAG"]["color"]
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
        "color": DOMINIOS["Redes y Modelado"]["color"]
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
        "color": DOMINIOS["Interacción y Creatividad"]["color"]
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
        "color": DOMINIOS["IoT y Ciberfísica"]["color"]
    },
    {
        "id": 18,
        "titulo": "Control de Actuadores",
        "cat": "Actuación y Hardware",
        "url": "https://sendcmqttz.streamlit.app",
        "icon": "⚡",
        "svg_type": "iot",
        "desc": "Mando remoto para activación de matrices LED y servomotores angulares.",
        "uso": "Automatización distribuida y control de compuertas.",
        "color": DOMINIOS["Actuación y Hardware"]["color"]
    },
    {
        "id": 19,
        "titulo": "Control por Voz IoT",
        "cat": "Voz y Acústica",
        "url": "https://ctrlvoicez.streamlit.app",
        "icon": "🎙️",
        "svg_type": "audio",
        "desc": "Operación manos libres de hardware mediante locuciones en lenguaje natural.",
        "uso": "Comando seguro en cabinas industriales y accesibilidad.",
        "color": DOMINIOS["Voz y Acústica"]["color"]
    }
]

APP_MAP = {app["id"]: app for app in CATALOGO}

# ==============================================================================
# 5. ESTILOS CSS REFINADOS
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
    background-color: #050811 !important;
}

[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stSidebar"], section[data-testid="stSidebar"] { display: none !important; }

.block-container {
    max-width: 1300px !important;
    padding-top: 1rem !important;
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
    letter-spacing: 0.24em;
    color: #cbd5e1;
    text-transform: uppercase;
}

.hero-title {
    font-size: clamp(1.8rem, 3.2vw, 2.5rem);
    font-weight: 700;
    color: #ffffff;
    line-height: 1.2;
    margin: 0.2rem 0;
    letter-spacing: -0.02em;
}

.hero-sub {
    color: #94a3b8;
    font-size: 0.9rem;
    max-width: 660px;
    margin: 0 auto;
}

/* Barra de Auditoría Compacta */
.audit-bar {
    background: rgba(10, 16, 32, 0.95);
    border: 1px solid rgba(203, 213, 225, 0.16);
    border-radius: 20px;
    padding: 8px 18px;
    margin-bottom: 1.2rem;
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.5);
}

.progress-track {
    width: 100%;
    height: 6px;
    background: rgba(255, 255, 255, 0.08);
    border-radius: 6px;
    overflow: hidden;
    margin-top: 6px;
}

.progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #1d4ed8, #3b82f6, #38bdf8, #818cf8);
    border-radius: 6px;
    transition: width 0.3s ease;
}

/* Tarjeta del Inspector */
.inspector-card {
    background: linear-gradient(145deg, rgba(12, 18, 38, 0.98) 0%, rgba(7, 10, 22, 0.98) 100%);
    border: 1px solid rgba(203, 213, 225, 0.18);
    border-radius: 12px;
    padding: 22px;
    box-shadow: 0 10px 35px rgba(0, 0, 0, 0.7);
    margin-bottom: 0.8rem;
}

.chip-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    text-transform: uppercase;
    font-weight: 600;
    border-radius: 6px;
    padding: 3px 9px;
    display: inline-block;
}

/* Estilo del Paternoster Track */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(8, 14, 28, 0.85) !important;
    border: 1px solid rgba(203, 213, 225, 0.15) !important;
    border-radius: 10px !important;
    padding: 10px !important;
}

/* Botones Nativos */
div.stButton > button {
    border-radius: 6px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    background: rgba(14, 20, 38, 0.95) !important;
    color: #e2e8f0 !important;
    border: 1px solid rgba(203, 213, 225, 0.22) !important;
    padding: 0.5rem 0.9rem !important;
    transition: all 0.2s ease !important;
}

div.stButton > button:hover {
    border-color: #38bdf8 !important;
    color: #ffffff !important;
}

div[data-testid="stLinkButton"] > a {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: 100% !important;
    background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 45%, #7c3aed 100%) !important;
    color: #ffffff !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    border-radius: 6px !important;
    padding: 0.68rem 1.2rem !important;
    text-decoration: none !important;
    box-shadow: 0 0 16px rgba(37, 99, 235, 0.45) !important;
    border: 1px solid rgba(226, 232, 240, 0.25) !important;
}

div[data-testid="stLinkButton"] > a:hover {
    box-shadow: 0 0 25px rgba(56, 189, 248, 0.6) !important;
}

.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 14px;
    margin-top: 10px;
}

.grid-card {
    background: rgba(10, 16, 32, 0.95);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-top: 3px solid #38bdf8;
    border-radius: 8px;
    padding: 16px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.5);
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
# 6. CANVAS GPU LIGERO (PARTÍCULAS SIN IMPACTO EN RENDIMIENTO)
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
            canvas.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:0;background:#050811;';
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
            { x: w * 0.15, y: h * 0.25, r: 180 * scale, vx: 0.4, vy: 0.3, color: 'rgba(37, 99, 235, 0.2)' },
            { x: w * 0.85, y: h * 0.35, r: 200 * scale, vx: -0.3, vy: 0.4, color: 'rgba(56, 189, 248, 0.18)' },
            { x: w * 0.5,  y: h * 0.85, r: 170 * scale, vx: 0.3, vy: -0.4, color: 'rgba(124, 58, 237, 0.16)' }
        ];

        const pColors = ['#38bdf8', '#818cf8', '#c084fc', '#93c5fd', '#cbd5e1'];
        const pCount = pWin.innerWidth < 768 ? 14 : 22;
        const particles = [];
        for (let i = 0; i < pCount; i++) {
            particles.push({
                x: Math.random() * w,
                y: Math.random() * h,
                r: Math.random() * 1.4 + 0.6,
                vx: (Math.random() - 0.5) * 0.4,
                vy: (Math.random() - 0.5) * 0.4,
                color: pColors[i % pColors.length]
            });
        }

        function loop() {
            ctx.fillStyle = '#050811';
            ctx.fillRect(0, 0, w, h);

            ctx.globalCompositeOperation = 'screen';
            for (let b of orbs) {
                b.x += b.vx;
                b.y += b.vy;
                if (b.x < -30 || b.x > w + 30) b.vx *= -1;
                if (b.y < -30 || b.y > h + 30) b.vy *= -1;

                const g = ctx.createRadialGradient(b.x, b.y, 2, b.x, b.y, b.r);
                g.addColorStop(0, b.color);
                g.addColorStop(1, 'rgba(5, 8, 17, 0)');
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
# 7. GENERADORES HUD COMPACTOS
# ==============================================================================
def generar_svg_hud(tipo: str, color_hex: str):
    if tipo == "iot":
        return f"""
        <div style="background:rgba(8,14,30,0.96); border:1px solid {color_hex}55; border-radius:10px; padding:12px; text-align:center;">
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_hex}; letter-spacing:0.12em; margin-bottom:4px;">NODO TELEMÉTRICO</div>
            <svg width="200" height="140" viewBox="0 0 200 140">
                <circle cx="100" cy="70" r="50" fill="none" stroke="rgba(203,213,225,0.15)" stroke-width="1" stroke-dasharray="4 4"/>
                <circle cx="100" cy="70" r="32" fill="none" stroke="{color_hex}" stroke-width="1.2" opacity="0.4"/>
                <circle cx="100" cy="70" r="16" fill="none" stroke="#cbd5e1" stroke-width="1.2" stroke-dasharray="6 4"/>
                <circle cx="100" cy="70" r="5" fill="#38bdf8"/>
                <text x="100" y="132" font-family="'JetBrains Mono'" font-size="8.5" fill="#cbd5e1" text-anchor="middle">MQTT ACTIVO</text>
            </svg>
        </div>
        """
    elif tipo == "vision":
        return f"""
        <div style="background:rgba(8,14,30,0.96); border:1px solid {color_hex}55; border-radius:10px; padding:12px; text-align:center;">
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_hex}; letter-spacing:0.12em; margin-bottom:4px;">CANAL ÓPTICO</div>
            <svg width="200" height="140" viewBox="0 0 200 140">
                <rect x="15" y="10" width="170" height="115" fill="none" stroke="rgba(203,213,225,0.15)" stroke-width="1" rx="6"/>
                <circle cx="100" cy="68" r="42" fill="none" stroke="{color_hex}" stroke-width="1.2" stroke-dasharray="8 5" opacity="0.6"/>
                <rect x="68" y="38" width="64" height="60" fill="none" stroke="{color_hex}" stroke-width="1.2"/>
                <text x="100" y="72" font-family="'JetBrains Mono'" font-size="8.5" fill="#f1f5f9" text-anchor="middle">DETECCIÓN</text>
            </svg>
        </div>
        """
    elif tipo == "audio":
        return f"""
        <div style="background:rgba(8,14,30,0.96); border:1px solid {color_hex}55; border-radius:10px; padding:12px; text-align:center;">
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_hex}; letter-spacing:0.12em; margin-bottom:4px;">FRECUENCIA AUDIBLE</div>
            <svg width="200" height="140" viewBox="0 0 200 140">
                <circle cx="100" cy="66" r="38" fill="none" stroke="#cbd5e1" stroke-width="1" opacity="0.3"/>
                <g transform="translate(62, 66)">
                    <rect x="0" y="-20" width="6" height="40" rx="2" fill="{color_hex}"/>
                    <rect x="14" y="-30" width="6" height="60" rx="2" fill="#38bdf8"/>
                    <rect x="28" y="-38" width="6" height="76" rx="2" fill="{color_hex}"/>
                    <rect x="42" y="-26" width="6" height="52" rx="2" fill="#c084fc"/>
                    <rect x="56" y="-16" width="6" height="32" rx="2" fill="#cbd5e1"/>
                </g>
                <text x="100" y="130" font-family="'JetBrains Mono'" font-size="8.5" fill="#cbd5e1" text-anchor="middle">SÍNTESIS</text>
            </svg>
        </div>
        """
    elif tipo == "neural":
        return f"""
        <div style="background:rgba(8,14,30,0.96); border:1px solid {color_hex}55; border-radius:10px; padding:12px; text-align:center;">
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_hex}; letter-spacing:0.12em; margin-bottom:4px;">INFERENCIA NEURONAL</div>
            <svg width="200" height="140" viewBox="0 0 200 140">
                <circle cx="100" cy="68" r="46" fill="none" stroke="rgba(203,213,225,0.15)" stroke-width="1" stroke-dasharray="8 6"/>
                <line x1="45" y1="42" x2="100" y2="55" stroke="{color_hex}" stroke-width="1.2"/>
                <line x1="45" y1="94" x2="100" y2="81" stroke="{color_hex}" stroke-width="1.2"/>
                <line x1="100" y1="55" x2="155" y2="68" stroke="#38bdf8" stroke-width="1.2"/>
                <line x1="100" y1="81" x2="155" y2="68" stroke="#38bdf8" stroke-width="1.2"/>
                <circle cx="45" cy="42" r="5" fill="#050811" stroke="{color_hex}" stroke-width="1.5"/>
                <circle cx="45" cy="94" r="5" fill="#050811" stroke="{color_hex}" stroke-width="1.5"/>
                <circle cx="100" cy="55" r="6" fill="#050811" stroke="#38bdf8" stroke-width="1.5"/>
                <circle cx="100" cy="81" r="6" fill="#050811" stroke="#38bdf8" stroke-width="1.5"/>
                <circle cx="155" cy="68" r="7" fill="#050811" stroke="#cbd5e1" stroke-width="2"/>
                <text x="100" y="132" font-family="'JetBrains Mono'" font-size="8.5" fill="#cbd5e1" text-anchor="middle">CLASIFICACIÓN</text>
            </svg>
        </div>
        """
    else:
        return f"""
        <div style="background:rgba(8,14,30,0.96); border:1px solid {color_hex}55; border-radius:10px; padding:12px; text-align:center;">
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_hex}; letter-spacing:0.12em; margin-bottom:4px;">MODELADO SEMÁNTICO</div>
            <svg width="200" height="140" viewBox="0 0 200 140">
                <path d="M 25 38 Q 65 15, 100 52 T 175 38" fill="none" stroke="{color_hex}" stroke-width="1.5"/>
                <path d="M 25 68 Q 65 96, 100 68 T 175 68" fill="none" stroke="#cbd5e1" stroke-width="1.5"/>
                <circle cx="50" cy="28" r="4" fill="#38bdf8"/>
                <circle cx="100" cy="68" r="6" fill="{color_hex}"/>
                <circle cx="150" cy="38" r="4" fill="#cbd5e1"/>
                <text x="100" y="130" font-family="'JetBrains Mono'" font-size="8.5" fill="#cbd5e1" text-anchor="middle">RECUPERACIÓN</text>
            </svg>
        </div>
        """

# ==============================================================================
# 8. ENCABEZADO Y AUDITORÍA
# ==============================================================================
total_apps = len(CATALOGO)
visitadas_count = len(st.session_state.visited_apps)
progreso_pct = int((visitadas_count / total_apps) * 100)

render_clean_html(f"""
<div class="header-deck">
    <div class="brand-label">Portafolio de Sistemas</div>
    <div class="hero-title">Interfaces Multimodales</div>
    <div class="hero-sub">Colección de 19 aplicaciones en visión artificial, modelos de lenguaje, IoT y acústica.</div>
</div>

<div class="audit-bar">
    <div style="display:flex; justify-content:space-between; align-items:center; font-family:'JetBrains Mono'; font-size:0.75rem;">
        <span style="color:#cbd5e1;">PROGRESO DE AUDITORÍA</span>
        <span style="color:#38bdf8; font-weight:600;">{visitadas_count} de {total_apps} revisadas ({progreso_pct}%)</span>
    </div>
    <div class="progress-track">
        <div class="progress-fill" style="width: {max(4, progreso_pct)}%;"></div>
    </div>
</div>
""")

# ==============================================================================
# 9. NAVEGACIÓN PRINCIPAL
# ==============================================================================
tab_estacion, tab_matriz = st.tabs(["Estación de Inspección", "Directorio Completo"])

# ==============================================================================
# PESTAÑA 1: ESTANTE PATERNOSTER + WORKSTATION LATERAL
# ==============================================================================
with tab_estacion:
    c_dom, c_busq = st.columns([1, 1.4], gap="medium")
    with c_dom:
        categorias = ["Todos los dominios"] + list(DOMINIOS.keys())
        cat_filtro = st.selectbox("Dominio:", categorias, label_visibility="collapsed")
    with c_busq:
        busqueda = st.text_input("Filtrar:", placeholder="Buscar por palabra clave...", label_visibility="collapsed")

    apps_visibles = [
        app for app in CATALOGO
        if (cat_filtro == "Todos los dominios" or app["cat"] == cat_filtro)
        and (
            not busqueda
            or busqueda.lower() in app["titulo"].lower()
            or busqueda.lower() in app["desc"].lower()
            or busqueda.lower() in app["uso"].lower()
        )
    ]

    if not apps_visibles:
        st.info("Sin coincidencias.")
        apps_visibles = CATALOGO

    ids_visibles = [a["id"] for a in apps_visibles]
    if st.session_state.selected_id not in ids_visibles:
        st.session_state.selected_id = ids_visibles[0]

    idx_actual = ids_visibles.index(st.session_state.selected_id)
    app_actual = APP_MAP[st.session_state.selected_id]
    esta_revisada = app_actual["id"] in st.session_state.visited_apps

    # Disposición Master-Detail: Estante Paternoster a la izquierda, Workstation a la derecha
    col_paternoster, col_workstation = st.columns([1, 1.25], gap="large")

    # --------------------------------------------------------------------------
    # ESTANTE PATERNOSTER (CONTENIDO CON ALTURA FIJA // SIN DESPLAZAR PÁGINA)
    # --------------------------------------------------------------------------
    with col_paternoster:
        # Barra de control del carrusel giratorio
        c_prev, c_pos, c_next = st.columns([1.1, 1.4, 1.1])
        with c_prev:
            if st.button("▲ Anterior", use_container_width=True):
                nuevo_idx = (idx_actual - 1) % len(ids_visibles)
                st.session_state.selected_id = ids_visibles[nuevo_idx]
                st.rerun()
        with c_pos:
            st.markdown(f"""
            <div style="text-align:center; padding-top:6px; font-family:'JetBrains Mono'; font-size:0.75rem; color:#cbd5e1;">
                Ítem <b style="color:#38bdf8;">{idx_actual + 1:02d}</b> / {len(ids_visibles):02d}
            </div>
            """, unsafe_allow_html=True)
        with c_next:
            if st.button("Siguiente ▼", use_container_width=True):
                nuevo_idx = (idx_actual + 1) % len(ids_visibles)
                st.session_state.selected_id = ids_visibles[nuevo_idx]
                st.rerun()

        # Contenedor deslizante de altura fija (500px) con scroll interno fluido
        with st.container(height=490):
            for item in apps_visibles:
                es_activa = item["id"] == st.session_state.selected_id
                check_icon = "✓" if item["id"] in st.session_state.visited_apps else "○"
                borde = f"2px solid {item['color']}" if es_activa else "1px solid rgba(255,255,255,0.08)"
                fondo = "rgba(16, 24, 48, 0.98)" if es_activa else "rgba(9, 14, 28, 0.85)"
                color_txt = "#ffffff" if es_activa else "#cbd5e1"

                c_card, c_act = st.columns([3.6, 1])
                with c_card:
                    render_clean_html(f"""
                    <div style="background:{fondo}; border:{borde}; border-radius:8px; padding:10px 12px; margin-bottom:6px;">
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <span style="font-weight:600; font-size:0.88rem; color:{color_txt};">{item['icon']} {item['titulo']}</span>
                            <span style="font-family:'JetBrains Mono'; font-size:0.72rem; color:{item['color']};">{check_icon}</span>
                        </div>
                        <div style="font-size:0.78rem; color:#94a3b8; margin-top:2px;">{item['desc']}</div>
                    </div>
                    """)
                with c_act:
                    st.write("")
                    btn_label = "● Ver" if es_activa else "Ver"
                    if st.button(btn_label, key=f"pater_{item['id']}", use_container_width=True):
                        st.session_state.selected_id = item["id"]
                        st.rerun()

    # --------------------------------------------------------------------------
    # ESTACIÓN DE TRABAJO (WORKSTATION LATERAL)
    # --------------------------------------------------------------------------
    with col_workstation:
        badge_status = (
            '<span style="color:#2dd4bf; background:rgba(45,212,191,0.12); border:1px solid rgba(45,212,191,0.3); border-radius:6px; padding:3px 8px; font-family:\'JetBrains Mono\'; font-size:0.72rem;">✓ Verificada</span>'
            if esta_revisada
            else '<span style="color:#94a3b8; background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.14); border-radius:6px; padding:3px 8px; font-family:\'JetBrains Mono\'; font-size:0.72rem;">○ Pendiente</span>'
        )

        # Ficha concisa con HTML purgado para evitar fugas de código
        render_clean_html(f"""
        <div class="inspector-card" style="border-top: 3px solid {app_actual['color']};">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                <div>
                    <span class="chip-tag" style="background:{app_actual['color']}20; color:{app_actual['color']}; border:1px solid {app_actual['color']}55;">
                        {app_actual['icon']} {app_actual['cat']}
                    </span>
                    <span style="font-family:'JetBrains Mono'; font-size:0.75rem; color:#cbd5e1; margin-left:8px;">
                        #{app_actual['id']:02d} / {total_apps:02d}
                    </span>
                </div>
                <div>{badge_status}</div>
            </div>
            <div style="font-size:1.55rem; font-weight:700; color:#ffffff; margin-bottom:6px;">{app_actual['titulo']}</div>
            <div style="font-size:0.92rem; color:#e2e8f0; line-height:1.55; margin-bottom:12px;">{app_actual['desc']}</div>
            <div style="background:rgba(56,189,248,0.06); border-left:3px solid {app_actual['color']}; border-radius:6px; padding:10px 14px; margin-bottom:10px;">
                <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{app_actual['color']}; text-transform:uppercase; font-weight:600; margin-bottom:2px;">Uso Práctico</div>
                <div style="font-size:0.86rem; color:#cbd5e1;">{app_actual['uso']}</div>
            </div>
        </div>
        """)

        # Visor HUD SVG dinámico
        render_clean_html(generar_svg_hud(app_actual["svg_type"], app_actual["color"]))

        st.write("")
        
        # Acciones principales
        c_link, c_check = st.columns([1.6, 1.2], gap="small")
        with c_link:
            st.link_button("Abrir aplicación ↗", app_actual["url"], use_container_width=True)
        with c_check:
            lbl_btn = "✓ Desmarcar" if esta_revisada else "Marcar revisada"
            if st.button(lbl_btn, use_container_width=True):
                if esta_revisada:
                    st.session_state.visited_apps.remove(app_actual["id"])
                else:
                    st.session_state.visited_apps.add(app_actual["id"])
                st.rerun()

# ==============================================================================
# PESTAÑA 2: DIRECTORIO COMPLETO EN MATRIZ (19 TARJETAS)
# ==============================================================================
with tab_matriz:
    st.caption("Visión panorámica de las 19 aplicaciones desarrolladas.")

    grid_cards_html = ['<div class="grid-container">']
    for item in CATALOGO:
        item_visitado = item["id"] in st.session_state.visited_apps
        simbolo_visita = "✓ Revisada" if item_visitado else "○ Pendiente"
        color_visita = "#2dd4bf" if item_visitado else "#94a3b8"

        grid_cards_html.append(f"""
        <div class="grid-card" style="border-top-color:{item['color']};">
            <div>
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                    <span style="font-size:1.2rem;">{item['icon']}</span>
                    <span style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_visita}; font-weight:600;">{simbolo_visita}</span>
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
