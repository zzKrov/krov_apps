import streamlit as st
import streamlit.components.v1 as components

# ==============================================================================
# 1. CONFIGURACIÓN GENERAL
# ==============================================================================
st.set_page_config(
    page_title="Portafolio // Sistemas e Interfaces",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

def render_clean_html(html_str: str):
    compact = "\n".join(line.strip() for line in html_str.splitlines() if line.strip())
    st.markdown(compact, unsafe_allow_html=True)

# ==============================================================================
# 2. ESTADO DE SESIÓN
# ==============================================================================
if "selected_id" not in st.session_state:
    st.session_state.selected_id = 1

if "visited_apps" not in st.session_state:
    st.session_state.visited_apps = set()

# ==============================================================================
# 3. PALETA DE DOMINIOS (ESPECTRO AZUL, PÚRPURA Y PLATINO)
# ==============================================================================
DOMINIOS = {
    "Visión y Óptica":           {"color": "#38bdf8"},
    "IoT y Ciberfísica":         {"color": "#22d3ee"},
    "Lenguaje y RAG":            {"color": "#818cf8"},
    "Voz y Acústica":            {"color": "#c084fc"},
    "Redes y Modelado":          {"color": "#8b5cf6"},
    "Interacción y Creatividad": {"color": "#6366f1"}
}

# ==============================================================================
# 4. CATÁLOGO MAESTRO (19 APLICACIONES)
# ==============================================================================
CATALOGO = [
    {
        "id": 1,
        "titulo": "Detector de Objetos",
        "cat": "Visión y Óptica",
        "url": "https://yolozz.streamlit.app",
        "icon": "🎯",
        "svg_type": "vision",
        "desc": "Detecta y cuenta 80 clases comunes de objetos en imágenes o video en vivo.",
        "uso": "Control de aforo y logística de inventarios.",
        "color": DOMINIOS["Visión y Óptica"]["color"]
    },
    {
        "id": 2,
        "titulo": "Nube de Palabras",
        "cat": "Lenguaje y RAG",
        "url": "https://wordcloudz.streamlit.app",
        "icon": "☁️",
        "svg_type": "text",
        "desc": "Composición visual donde los términos más frecuentes destacan por tamaño.",
        "uso": "Análisis rápido de encuestas y reseñas.",
        "color": DOMINIOS["Lenguaje y RAG"]["color"]
    },
    {
        "id": 3,
        "titulo": "Reconocedor de Dígitos",
        "cat": "Redes y Modelado",
        "url": "https://mnistz.streamlit.app",
        "icon": "✍️",
        "svg_type": "neural",
        "desc": "Clasifica números del 0 al 9 dibujados a mano sobre un lienzo digital.",
        "uso": "Digitalización de formularios y cheques bancarios.",
        "color": DOMINIOS["Redes y Modelado"]["color"]
    },
    {
        "id": 4,
        "titulo": "Análisis de Imagen",
        "cat": "Visión y Óptica",
        "url": "https://visionz.streamlit.app",
        "icon": "👁️",
        "svg_type": "vision",
        "desc": "Genera una descripción detallada de los elementos y contexto de cualquier foto.",
        "uso": "Documentación técnica e inspección de daños.",
        "color": DOMINIOS["Visión y Óptica"]["color"]
    },
    {
        "id": 5,
        "titulo": "Traductor de Voz",
        "cat": "Voz y Acústica",
        "url": "https://traductorz.streamlit.app",
        "icon": "🎙️",
        "svg_type": "audio",
        "desc": "Escucha por micrófono, traduce el mensaje y lo reproduce en voz alta.",
        "uso": "Atención multilingüe en ventanilla y viajes.",
        "color": DOMINIOS["Voz y Acústica"]["color"]
    },
    {
        "id": 6,
        "titulo": "Detector de Postura",
        "cat": "Visión y Óptica",
        "url": "https://teachablez.streamlit.app",
        "icon": "🛡️",
        "svg_type": "vision",
        "desc": "Evalúa postura y presencia física desde la cámara local sin subir video a la red.",
        "uso": "Supervisión ergonómica y quioscos sin contacto.",
        "color": DOMINIOS["Visión y Óptica"]["color"]
    },
    {
        "id": 7,
        "titulo": "Espacio de Bienestar",
        "cat": "Interacción y Creatividad",
        "url": "https://bendover.streamlit.app",
        "icon": "🐇",
        "svg_type": "creative",
        "desc": "Entorno relajante con partículas reactivas al cursor y síntesis de voz.",
        "uso": "Pausas activas y reducción de fatiga cognitiva.",
        "color": DOMINIOS["Interacción y Creatividad"]["color"]
    },
    {
        "id": 8,
        "titulo": "Conversación Guiada",
        "cat": "Interacción y Creatividad",
        "url": "https://sentimentz.streamlit.app",
        "icon": "🤖",
        "svg_type": "text",
        "desc": "Diálogo asistido con análisis del estado de ánimo y respuestas estructuradas.",
        "uso": "Bitácoras personales y redacción formal.",
        "color": DOMINIOS["Interacción y Creatividad"]["color"]
    },
    {
        "id": 9,
        "titulo": "Extractor de Texto 3D",
        "cat": "Visión y Óptica",
        "url": "https://ocryaudioz.streamlit.app",
        "icon": "🪞",
        "svg_type": "vision",
        "desc": "Extrae texto de documentos físicos y lo proyecta sobre un plano tridimensional.",
        "uso": "Lectura y traducción de impresos y letreros.",
        "color": DOMINIOS["Visión y Óptica"]["color"]
    },
    {
        "id": 10,
        "titulo": "Lector por Cámara",
        "cat": "Visión y Óptica",
        "url": "https://lectorz.streamlit.app",
        "icon": "📷",
        "svg_type": "vision",
        "desc": "Transforma capturas de cámara web en fragmentos de texto editables.",
        "uso": "Transcripción rápida de libros y recibos de compra.",
        "color": DOMINIOS["Visión y Óptica"]["color"]
    },
    {
        "id": 11,
        "titulo": "Interfaces Sensoriales",
        "cat": "Voz y Acústica",
        "url": "https://sussusamogus.streamlit.app",
        "icon": "✦",
        "svg_type": "audio",
        "desc": "Señalización coordinada mediante destellos visuales, tonos y vibración física.",
        "uso": "Cabinas de control y señalética accesible.",
        "color": DOMINIOS["Voz y Acústica"]["color"]
    },
    {
        "id": 12,
        "titulo": "Tablero de Bocetos",
        "cat": "Interacción y Creatividad",
        "url": "https://drawrecogz.streamlit.app",
        "icon": "🎨",
        "svg_type": "creative",
        "desc": "Lienzo de dibujo vectorial con evaluación e interpretación automática de trazos.",
        "uso": "Lluvia de ideas visual y prototipado temprano.",
        "color": DOMINIOS["Interacción y Creatividad"]["color"]
    },
    {
        "id": 13,
        "titulo": "Consulta sobre PDF",
        "cat": "Lenguaje y RAG",
        "url": "https://chatpdfz.streamlit.app",
        "icon": "💬",
        "svg_type": "text",
        "desc": "Responde preguntas basándose con precisión en el texto de un archivo PDF.",
        "uso": "Revisión ágil de contratos y manuales extensos.",
        "color": DOMINIOS["Lenguaje y RAG"]["color"]
    },
    {
        "id": 14,
        "titulo": "Analizador de Tono",
        "cat": "Lenguaje y RAG",
        "url": "https://textanalysiz.streamlit.app",
        "icon": "⚖️",
        "svg_type": "text",
        "desc": "Evalúa neutralidad, subjetividad y carga emocional en comunicaciones escritas.",
        "uso": "Revisión de mensajes corporativos delicados.",
        "color": DOMINIOS["Lenguaje y RAG"]["color"]
    },
    {
        "id": 15,
        "titulo": "Modelador Físico",
        "cat": "Redes y Modelado",
        "url": "https://histinfz.streamlit.app",
        "icon": "⚡",
        "svg_type": "neural",
        "desc": "Calcula relaciones de equilibrio estático a partir de esquemas de fuerzas.",
        "uso": "Apoyo académico en física y validación de palancas.",
        "color": DOMINIOS["Redes y Modelado"]["color"]
    },
    {
        "id": 16,
        "titulo": "Relatos Ilustrados",
        "cat": "Interacción y Creatividad",
        "url": "https://ejemplohistinfz.streamlit.app",
        "icon": "📖",
        "svg_type": "creative",
        "desc": "Elabora historias infantiles estructuradas a partir de un dibujo manual.",
        "uso": "Fomento de lectura y dinámicas educativas.",
        "color": DOMINIOS["Interacción y Creatividad"]["color"]
    },
    {
        "id": 17,
        "titulo": "Telemetría IoT",
        "cat": "IoT y Ciberfísica",
        "url": "https://receptz.streamlit.app",
        "icon": "📡",
        "svg_type": "iot",
        "desc": "Lectura en tiempo real de temperatura, humedad y presión conectada a un gemelo Wokwi.",
        "uso": "Supervisión ambiental y salas de servidores.",
        "color": DOMINIOS["IoT y Ciberfísica"]["color"]
    },
    {
        "id": 18,
        "titulo": "Control de Actuadores",
        "cat": "IoT y Ciberfísica",
        "url": "https://sendcmqttz.streamlit.app",
        "icon": "⚡",
        "svg_type": "iot",
        "desc": "Mando remoto para encendido de luces y calibración angular de servomotores.",
        "uso": "Domótica distribuida y control de compuertas.",
        "color": DOMINIOS["IoT y Ciberfísica"]["color"]
    },
    {
        "id": 19,
        "titulo": "Control por Voz IoT",
        "cat": "IoT y Ciberfísica",
        "url": "https://ctrlvoicez.streamlit.app",
        "icon": "🎙️",
        "svg_type": "audio",
        "desc": "Operación manos libres de hardware mediante órdenes orales en lenguaje natural.",
        "uso": "Accesibilidad en talleres y cabinas de mando.",
        "color": DOMINIOS["IoT y Ciberfísica"]["color"]
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
    max-width: 1280px !important;
    padding-top: 1rem !important;
    padding-bottom: 3.5rem !important;
    margin: 0 auto !important;
}

.header-deck {
    text-align: center;
    margin-bottom: 1.3rem;
}

.brand-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.22em;
    color: #cbd5e1;
    text-transform: uppercase;
}

.hero-title {
    font-size: clamp(1.8rem, 3.2vw, 2.6rem);
    font-weight: 700;
    color: #ffffff;
    line-height: 1.2;
    margin: 0.3rem 0;
    letter-spacing: -0.02em;
}

.hero-sub {
    color: #94a3b8;
    font-size: 0.92rem;
    max-width: 660px;
    margin: 0 auto;
}

.audit-bar {
    background: rgba(10, 16, 32, 0.95);
    border: 1px solid rgba(203, 213, 225, 0.16);
    border-radius: 30px;
    padding: 8px 18px;
    margin-bottom: 1.4rem;
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

.inspector-card {
    background: linear-gradient(145deg, rgba(12, 18, 38, 0.98) 0%, rgba(7, 10, 22, 0.98) 100%);
    border: 1px solid rgba(203, 213, 225, 0.2);
    border-radius: 12px;
    padding: 22px;
    box-shadow: 0 10px 35px rgba(0, 0, 0, 0.7);
    margin-bottom: 1rem;
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

div.stButton > button {
    border-radius: 6px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    background: rgba(14, 20, 38, 0.95) !important;
    color: #e2e8f0 !important;
    border: 1px solid rgba(203, 213, 225, 0.22) !important;
    padding: 0.55rem 1rem !important;
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
# 6. CANVAS GPU LIGERO (PARTÍCULAS EN TONOS AZUL, PÚRPURA Y PLATINO)
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
# 7. GENERADORES HUD GRÁFICOS
# ==============================================================================
def generar_svg_hud(tipo: str, color_hex: str):
    if tipo == "iot":
        return f"""
        <div style="background:rgba(8,14,30,0.96); border:1px solid {color_hex}55; border-radius:10px; padding:12px; text-align:center;">
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_hex}; letter-spacing:0.12em; margin-bottom:4px;">NODO TELEMÉTRICO</div>
            <svg width="200" height="145" viewBox="0 0 200 145">
                <circle cx="100" cy="72" r="52" fill="none" stroke="rgba(203,213,225,0.15)" stroke-width="1" stroke-dasharray="4 4"/>
                <circle cx="100" cy="72" r="34" fill="none" stroke="{color_hex}" stroke-width="1.2" opacity="0.4"/>
                <circle cx="100" cy="72" r="18" fill="none" stroke="#cbd5e1" stroke-width="1.2" stroke-dasharray="6 4"/>
                <circle cx="100" cy="72" r="5" fill="#38bdf8"/>
                <text x="100" y="136" font-family="'JetBrains Mono'" font-size="8.5" fill="#cbd5e1" text-anchor="middle">MQTT ACTIVO</text>
            </svg>
        </div>
        """
    elif tipo == "vision":
        return f"""
        <div style="background:rgba(8,14,30,0.96); border:1px solid {color_hex}55; border-radius:10px; padding:12px; text-align:center;">
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_hex}; letter-spacing:0.12em; margin-bottom:4px;">CANAL ÓPTICO</div>
            <svg width="200" height="145" viewBox="0 0 200 145">
                <rect x="15" y="12" width="170" height="120" fill="none" stroke="rgba(203,213,225,0.15)" stroke-width="1" rx="6"/>
                <circle cx="100" cy="72" r="44" fill="none" stroke="{color_hex}" stroke-width="1.2" stroke-dasharray="8 5" opacity="0.6"/>
                <rect x="68" y="42" width="64" height="60" fill="none" stroke="{color_hex}" stroke-width="1.2"/>
                <text x="100" y="76" font-family="'JetBrains Mono'" font-size="8.5" fill="#f1f5f9" text-anchor="middle">DETECCIÓN</text>
            </svg>
        </div>
        """
    elif tipo == "audio":
        return f"""
        <div style="background:rgba(8,14,30,0.96); border:1px solid {color_hex}55; border-radius:10px; padding:12px; text-align:center;">
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_hex}; letter-spacing:0.12em; margin-bottom:4px;">FRECUENCIA AUDIBLE</div>
            <svg width="200" height="145" viewBox="0 0 200 145">
                <circle cx="100" cy="68" r="40" fill="none" stroke="#cbd5e1" stroke-width="1" opacity="0.3"/>
                <g transform="translate(62, 68)">
                    <rect x="0" y="-22" width="6" height="44" rx="2" fill="{color_hex}"/>
                    <rect x="14" y="-32" width="6" height="64" rx="2" fill="#38bdf8"/>
                    <rect x="28" y="-40" width="6" height="80" rx="2" fill="{color_hex}"/>
                    <rect x="42" y="-28" width="6" height="56" rx="2" fill="#c084fc"/>
                    <rect x="56" y="-18" width="6" height="36" rx="2" fill="#cbd5e1"/>
                </g>
                <text x="100" y="134" font-family="'JetBrains Mono'" font-size="8.5" fill="#cbd5e1" text-anchor="middle">SÍNTESIS</text>
            </svg>
        </div>
        """
    elif tipo == "neural":
        return f"""
        <div style="background:rgba(8,14,30,0.96); border:1px solid {color_hex}55; border-radius:10px; padding:12px; text-align:center;">
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_hex}; letter-spacing:0.12em; margin-bottom:4px;">INFERENCIA NEURONAL</div>
            <svg width="200" height="145" viewBox="0 0 200 145">
                <circle cx="100" cy="72" r="48" fill="none" stroke="rgba(203,213,225,0.15)" stroke-width="1" stroke-dasharray="8 6"/>
                <line x1="45" y1="45" x2="100" y2="58" stroke="{color_hex}" stroke-width="1.2"/>
                <line x1="45" y1="98" x2="100" y2="86" stroke="{color_hex}" stroke-width="1.2"/>
                <line x1="100" y1="58" x2="155" y2="72" stroke="#38bdf8" stroke-width="1.2"/>
                <line x1="100" y1="86" x2="155" y2="72" stroke="#38bdf8" stroke-width="1.2"/>
                <circle cx="45" cy="45" r="5" fill="#050811" stroke="{color_hex}" stroke-width="1.5"/>
                <circle cx="45" cy="98" r="5" fill="#050811" stroke="{color_hex}" stroke-width="1.5"/>
                <circle cx="100" cy="58" r="6" fill="#050811" stroke="#38bdf8" stroke-width="1.5"/>
                <circle cx="100" cy="86" r="6" fill="#050811" stroke="#38bdf8" stroke-width="1.5"/>
                <circle cx="155" cy="72" r="7" fill="#050811" stroke="#cbd5e1" stroke-width="2"/>
                <text x="100" y="136" font-family="'JetBrains Mono'" font-size="8.5" fill="#cbd5e1" text-anchor="middle">CLASIFICACIÓN</text>
            </svg>
        </div>
        """
    else:
        return f"""
        <div style="background:rgba(8,14,30,0.96); border:1px solid {color_hex}55; border-radius:10px; padding:12px; text-align:center;">
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_hex}; letter-spacing:0.12em; margin-bottom:4px;">MODELADO SEMÁNTICO</div>
            <svg width="200" height="145" viewBox="0 0 200 145">
                <path d="M 25 40 Q 65 15, 100 55 T 175 40" fill="none" stroke="{color_hex}" stroke-width="1.5"/>
                <path d="M 25 72 Q 65 100, 100 72 T 175 72" fill="none" stroke="#cbd5e1" stroke-width="1.5"/>
                <circle cx="50" cy="30" r="4" fill="#38bdf8"/>
                <circle cx="100" cy="72" r="6" fill="{color_hex}"/>
                <circle cx="150" cy="40" r="4" fill="#cbd5e1"/>
                <text x="100" y="134" font-family="'JetBrains Mono'" font-size="8.5" fill="#cbd5e1" text-anchor="middle">RECUPERACIÓN</text>
            </svg>
        </div>
        """

# ==============================================================================
# 8. ENCABEZADO Y PROGRESO DE AUDITORÍA
# ==============================================================================
total_apps = len(CATALOGO)
visitadas_count = len(st.session_state.visited_apps)
progreso_pct = int((visitadas_count / total_apps) * 100)

render_clean_html(f"""
<div class="header-deck">
    <div class="brand-label">Portafolio de Sistemas</div>
    <div class="hero-title">Interfaces Multimodales</div>
    <div class="hero-sub">Colección de 19 aplicaciones en visión por computador, modelos de lenguaje, IoT y acústica.</div>
</div>

<div class="audit-bar">
    <div style="display:flex; justify-content:space-between; align-items:center; font-family:'JetBrains Mono'; font-size:0.75rem;">
        <span style="color:#cbd5e1;">PROGRESO DE REVISIÓN</span>
        <span style="color:#38bdf8; font-weight:600;">{visitadas_count} de {total_apps} revisadas ({progreso_pct}%)</span>
    </div>
    <div class="progress-track">
        <div class="progress-fill" style="width: {max(4, progreso_pct)}%;"></div>
    </div>
</div>
""")

# ==============================================================================
# 9. FLUJO DE NAVEGACIÓN INTUITIVO
# ==============================================================================
tab_estacion, tab_matriz = st.tabs(["Estación de Inspección", "Directorio Completo"])

# ==============================================================================
# PESTAÑA 1: MASTER-DETAIL / ESTACIÓN DE TRABAJO
# ==============================================================================
with tab_estacion:
    c_filter, c_search = st.columns([1, 1.4], gap="medium")
    with c_filter:
        categorias = ["Todas las áreas"] + list(DOMINIOS.keys())
        cat_filtro = st.selectbox("Dominio técnico:", categorias, label_visibility="collapsed")
    with c_search:
        busqueda = st.text_input("Filtrar:", placeholder="Buscar por nombre o palabra clave...", label_visibility="collapsed")

    apps_visibles = [
        app for app in CATALOGO
        if (cat_filtro == "Todas las áreas" or app["cat"] == cat_filtro)
        and (
            not busqueda
            or busqueda.lower() in app["titulo"].lower()
            or busqueda.lower() in app["desc"].lower()
            or busqueda.lower() in app["uso"].lower()
        )
    ]

    if not apps_visibles:
        st.info("Sin coincidencias con el criterio de búsqueda.")
        apps_visibles = CATALOGO

    ids_visibles = [a["id"] for a in apps_visibles]
    if st.session_state.selected_id not in ids_visibles:
        st.session_state.selected_id = ids_visibles[0]

    app_actual = APP_MAP[st.session_state.selected_id]
    esta_revisada = app_actual["id"] in st.session_state.visited_apps

    col_lista, col_detalle = st.columns([1, 1.25], gap="large")

    with col_lista:
        st.caption(f"Aplicaciones disponibles: {len(apps_visibles)}")
        
        opciones_nombres = [f"#{a['id']:02d} — {a['icon']} {a['titulo']}" for a in apps_visibles]
        idx_actual = ids_visibles.index(st.session_state.selected_id)
        
        nuevo_idx = st.selectbox(
            "Seleccionar aplicación:",
            options=range(len(apps_visibles)),
            format_func=lambda i: opciones_nombres[i],
            index=idx_actual,
            label_visibility="collapsed"
        )
        if nuevo_idx != idx_actual:
            st.session_state.selected_id = ids_visibles[nuevo_idx]
            st.rerun()

        st.write("")
        
        # Tarjetas compactas en la lista
        for item in apps_visibles:
            es_activa = item["id"] == st.session_state.selected_id
            check_txt = "✓" if item["id"] in st.session_state.visited_apps else "○"
            borde_izq = f"3px solid {item['color']}" if es_activa else "1px solid rgba(255,255,255,0.06)"
            fondo_card = "rgba(18, 26, 52, 0.95)" if es_activa else "rgba(10, 16, 32, 0.75)"
            
            c_info, c_sel = st.columns([3.5, 1])
            with c_info:
                st.markdown(f"""
                <div style="background:{fondo_card}; border-left:{borde_izq}; border-radius:6px; padding:8px 12px; margin-bottom:6px;">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-weight:600; font-size:0.88rem; color:#ffffff;">{item['icon']} {item['titulo']}</span>
                        <span style="font-family:'JetBrains Mono'; font-size:0.7rem; color:{item['color']};">{check_txt}</span>
                    </div>
                    <div style="font-size:0.78rem; color:#94a3b8; margin-top:2px;">{item['desc']}</div>
                </div>
                """, unsafe_allow_html=True)
            with c_sel:
                st.write("")
                if st.button("Ver", key=f"btn_sel_{item['id']}", use_container_width=True):
                    st.session_state.selected_id = item["id"]
                    st.rerun()

    with col_detalle:
        badge_status = (
            '<span style="color:#2dd4bf; background:rgba(45,212,191,0.12); border:1px solid rgba(45,212,191,0.3); border-radius:6px; padding:3px 8px; font-family:\'JetBrains Mono\'; font-size:0.72rem;">✓ Verificada</span>'
            if esta_revisada
            else '<span style="color:#94a3b8; background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.14); border-radius:6px; padding:3px 8px; font-family:\'JetBrains Mono\'; font-size:0.72rem;">○ Pendiente</span>'
        )

        st.markdown(f"""
        <div class="inspector-card" style="border-top: 3px solid {app_actual['color']};">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                <div>
                    <span class="chip-tag" style="background:{app_actual['color']}22; color:{app_actual['color']}; border:1px solid {app_actual['color']}55;">
                        {app_actual['icon']} {app_actual['cat']}
                    </span>
                    <span style="font-family:'JetBrains Mono'; font-size:0.75rem; color:#cbd5e1; margin-left:8px;">
                        #{app_actual['id']:02d} / {total_apps:02d}
                    </span>
                </div>
                <div>{badge_status}</div>
            </div>
            
            <div style="font-size:1.6rem; font-weight:700; color:#ffffff; margin-bottom:8px;">{app_actual['titulo']}</div>
            
            <div style="font-size:0.95rem; color:#e2e8f0; line-height:1.55; margin-bottom:14px;">
                {app_actual['desc']}
            </div>
            
            <div style="background:rgba(56,189,248,0.06); border-left:3px solid {app_actual['color']}; border-radius:6px; padding:10px 14px; margin-bottom:14px;">
                <div style="font-family:'JetBrains Mono'; font-size:0.7rem; color:{app_actual['color']}; text-transform:uppercase; font-weight:600; margin-bottom:2px;">Uso Práctico</div>
                <div style="font-size:0.88rem; color:#cbd5e1;">{app_actual['uso']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        render_clean_html(generar_svg_hud(app_actual["svg_type"], app_actual["color"]))

        st.write("")
        
        col_link, col_check = st.columns([1.6, 1.2], gap="small")
        with col_link:
            st.link_button("Abrir aplicación ↗", app_actual["url"], use_container_width=True)
        with col_check:
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
    st.caption("Visión panorámica de las 19 soluciones desarrolladas.")

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
<div style="text-align:center; padding:1.8rem 0; border-top:1px solid rgba(203,213,225,0.12); margin-top:2rem;">
    <div style="font-family:'JetBrains Mono'; font-size:0.74rem; letter-spacing:0.2em; color:#cbd5e1; text-transform:uppercase;">
        PORTAFOLIO DE SISTEMAS E INTERFACES MULTIMODALES
    </div>
    <div style="font-size:0.8rem; color:#64748b; margin-top:4px;">
        19 aplicaciones desplegadas sobre Streamlit Cloud
    </div>
</div>
""")
