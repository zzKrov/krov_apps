import streamlit as st
import streamlit.components.v1 as components

# ==============================================================================
# 1. CONFIGURACIÓN GENERAL
# ==============================================================================
st.set_page_config(
    page_title="Portafolio de Sistemas e Interfaces Multimodales",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

def render_clean_html(html_str: str):
    compact = "\n".join(line.strip() for line in html_str.splitlines() if line.strip())
    st.markdown(compact, unsafe_allow_html=True)

# ==============================================================================
# 2. ESTADO DE SESIÓN Y GESTIÓN DE AUDITORÍA
# ==============================================================================
if "carousel_idx" not in st.session_state:
    st.session_state.carousel_idx = 0

if "visited_apps" not in st.session_state:
    st.session_state.visited_apps = set()

# ==============================================================================
# 3. MATRIZ CROMÁTICA ARMÓNICA (AZULES, PÚRPURAS Y PLATINO)
# ==============================================================================
# Cada dominio cuenta con un tono exclusivo dentro del espectro frío/galáctico:
CATEGORY_PALETTE = {
    "Visión por Computador":       {"color": "#38bdf8", "border": "#38bdf8", "tag": "Cian Eléctrico"},
    "Visión Multimodal":           {"color": "#0ea5e9", "border": "#0ea5e9", "tag": "Azul Zafiro"},
    "Óptica y Documentos":         {"color": "#93c5fd", "border": "#93c5fd", "tag": "Platino Glacial"},
    "Óptica y Análisis 3D":        {"color": "#60a5fa", "border": "#60a5fa", "tag": "Azul Cerúleo"},
    "Sistemas IoT y Telemetría":   {"color": "#22d3ee", "border": "#22d3ee", "tag": "Cian Digital"},
    "Actuación Ciberfísica":       {"color": "#3b82f6", "border": "#3b82f6", "tag": "Cobalto Estelar"},
    "Interfaces Vocales IoT":      {"color": "#c084fc", "border": "#c084fc", "tag": "Violeta Vocal"},
    "Acústica y Traducción":       {"color": "#a855f7", "border": "#a855f7", "tag": "Púrpura Acústico"},
    "Modelos de Lenguaje (RAG)":   {"color": "#818cf8", "border": "#818cf8", "tag": "Índigo Vectorial"},
    "Procesamiento de Lenguaje":   {"color": "#a78bfa", "border": "#a78bfa", "tag": "Lavanda Amatista"},
    "Redes Neuronales":            {"color": "#8b5cf6", "border": "#8b5cf6", "tag": "Púrpura Real"},
    "Modelado Físico y Tensor":    {"color": "#7dd3fc", "border": "#7dd3fc", "tag": "Azul Hielo"},
    "Diseño y Visión Creativa":    {"color": "#d8b4fe", "border": "#d8b4fe", "tag": "Lila Platino"},
    "Sistemas Multisensoriales":   {"color": "#7c3aed", "border": "#7c3aed", "tag": "Violeta Imperial"},
    "Interacción y Bienestar":     {"color": "#6366f1", "border": "#6366f1", "tag": "Cobalto Profundo"},
    "Interacción Humana":          {"color": "#a855f7", "border": "#a855f7", "tag": "Orquídea Cósmica"}
}

# ==============================================================================
# 4. CATÁLOGO MAESTRO (19 APLICACIONES COMPLETAS)
# ==============================================================================
CATALOGO = [
    {
        "id": 1,
        "titulo": "Detector de Objetos en Vivo",
        "cat": "Visión por Computador",
        "url": "https://yolozz.streamlit.app",
        "icon": "🎯",
        "svg_type": "vision",
        "proposito": "Detección y conteo de entidades en tiempo real mediante cámara web con soporte para 80 clases estandarizadas.",
        "codigo": "Inferencia YOLOv5 en cliente, supresión de no máximos (NMS) adaptativa y señales acústicas de confirmación.",
        "uso": "Control de aforo, logística de bodegas y asistencia a personas con discapacidad visual.",
        "color": CATEGORY_PALETTE["Visión por Computador"]["color"]
    },
    {
        "id": 2,
        "titulo": "Generador de Nube de Palabras",
        "cat": "Procesamiento de Lenguaje",
        "url": "https://wordcloudz.streamlit.app",
        "icon": "☁️",
        "svg_type": "text",
        "proposito": "Composición gráfica de términos preponderantes ponderados por su densidad de frecuencia léxica.",
        "codigo": "Filtrado con expresiones regulares, supresión multilingüe de stop-words y distribución espacial con WordCloud.",
        "uso": "Auditoría de reseñas de clientes, minería de opiniones y síntesis de discursos.",
        "color": CATEGORY_PALETTE["Procesamiento de Lenguaje"]["color"]
    },
    {
        "id": 3,
        "titulo": "Reconocedor de Dígitos Ópticos",
        "cat": "Redes Neuronales",
        "url": "https://mnistz.streamlit.app",
        "icon": "✍️",
        "svg_type": "neural",
        "proposito": "Lienzo de dibujo para clasificación instantánea de dígitos manuscritos (0-9) con cálculo de certidumbre.",
        "codigo": "Aislamiento por bounding box en Pillow, normalización a 28×28 píxeles e inferencia convolucional profunda.",
        "uso": "Procesamiento de comprobantes de pago, digitalización postal y formularios censales.",
        "color": CATEGORY_PALETTE["Redes Neuronales"]["color"]
    },
    {
        "id": 4,
        "titulo": "Análisis Contextual de Imagen",
        "cat": "Visión Multimodal",
        "url": "https://visionz.streamlit.app",
        "icon": "👁️",
        "svg_type": "vision",
        "proposito": "Evaluación semántica de escenas fotográficas para generación de reportes periciales estructurados.",
        "codigo": "Codificación Base64 en memoria y conexión continua por streaming con modelos multimodales GPT-4o.",
        "uso": "Inspección de daños para aseguradoras, peritaje de obras civiles y accesibilidad inclusiva.",
        "color": CATEGORY_PALETTE["Visión Multimodal"]["color"]
    },
    {
        "id": 5,
        "titulo": "Traductor de Voz a Audio",
        "cat": "Acústica y Traducción",
        "url": "https://traductorz.streamlit.app",
        "icon": "🎙️",
        "svg_type": "audio",
        "proposito": "Captura vocal por micrófono, traducción instantánea a idiomas de destino y síntesis de voz fonética.",
        "codigo": "Web Speech API integrada mediante puentes Bokeh, motor de traducción Google Translate y síntesis con gTTS.",
        "uso": "Atención turística internacional en ventanilla y práctica de pronunciación idiomática.",
        "color": CATEGORY_PALETTE["Acústica y Traducción"]["color"]
    },
    {
        "id": 6,
        "titulo": "Detector de Presencia y Postura",
        "cat": "Visión por Computador",
        "url": "https://teachablez.streamlit.app",
        "icon": "🛡️",
        "svg_type": "vision",
        "proposito": "Monitoreo corporal y análisis postural en el navegador sin transmitir flujos de video externos.",
        "codigo": "Inferencia local en cliente con TensorFlow.js y PoseNet sobre HTML5 Canvas, evaluando articulaciones axiales.",
        "uso": "Supervisión ergonómica laboral, seguridad industrial y quioscos sin contacto táctil.",
        "color": CATEGORY_PALETTE["Visión por Computador"]["color"]
    },
    {
        "id": 7,
        "titulo": "Espacio de Pausa y Bienestar",
        "cat": "Interacción y Bienestar",
        "url": "https://bendover.streamlit.app",
        "icon": "🐇",
        "svg_type": "creative",
        "proposito": "Entorno antiestrés con seguimiento de cursor mediante física de partículas dinámicas y síntesis vocal.",
        "codigo": "Simulador cinemático en JavaScript acelerado por Canvas 2D y generación vocal local por SpeechSynthesis.",
        "uso": "Pausas activas en turnos prolongados y disminución de fatiga mental frente a monitores.",
        "color": CATEGORY_PALETTE["Interacción y Bienestar"]["color"]
    },
    {
        "id": 8,
        "titulo": "Asistente Conversacional Guiado",
        "cat": "Interacción Humana",
        "url": "https://sentimentz.streamlit.app",
        "icon": "🤖",
        "svg_type": "text",
        "proposito": "Plataforma de diálogo asistido con detección del tono anímico del usuario y respuestas adaptativas.",
        "codigo": "Clasificador léxico de sentimiento, sincronización de estados con animación vectorial Lottie y voz guiada.",
        "uso": "Bitácoras emocionales reflexivas y soporte estructurado para redacción bajo estrés.",
        "color": CATEGORY_PALETTE["Interacción Humana"]["color"]
    },
    {
        "id": 9,
        "titulo": "Visor y Extractor de Texto en 3D",
        "cat": "Óptica y Análisis 3D",
        "url": "https://ocryaudioz.streamlit.app",
        "icon": "🪞",
        "svg_type": "vision",
        "proposito": "Captura documental con proyección tridimensional interactiva del texto extraído, traducción y lectura.",
        "codigo": "Filtros adaptativos CLAHE en OpenCV, extracción óptica por Tesseract OCR y renderizado sobre plano 3D.",
        "uso": "Traducción de letreros en idiomas extranjeros y digitalización para personas con baja agudeza visual.",
        "color": CATEGORY_PALETTE["Óptica y Análisis 3D"]["color"]
    },
    {
        "id": 10,
        "titulo": "Digitalizador Óptico por Cámara",
        "cat": "Óptica y Documentos",
        "url": "https://lectorz.streamlit.app",
        "icon": "📷",
        "svg_type": "vision",
        "proposito": "Conversión inmediata de documentos físicos capturados por cámara web en texto editable y exportable.",
        "codigo": "Ampliación bicúbica al doble de resolución, umbralización adaptable Otsu y cálculo métrico de densidad tipográfica.",
        "uso": "Copia instantánea de citas bibliográficas e indexación rápida de facturas físicas.",
        "color": CATEGORY_PALETTE["Óptica y Documentos"]["color"]
    },
    {
        "id": 11,
        "titulo": "Interfaces Multisensoriales",
        "cat": "Sistemas Multisensoriales",
        "url": "https://sussusamogus.streamlit.app",
        "icon": "✦",
        "svg_type": "audio",
        "proposito": "Laboratorio de señalización simultánea mediante impulsos ópticos, frecuencias acústicas puras y vibración háptica.",
        "codigo": "Síntesis matemática de ondas sinusoidales en RAM, modulación CSS y enlace con la Vibration API del dispositivo.",
        "uso": "Alertas para cabinas de control, señalética crítica accesible y consolas de monitoreo.",
        "color": CATEGORY_PALETTE["Sistemas Multisensoriales"]["color"]
    },
    {
        "id": 12,
        "titulo": "Tablero de Bocetos y Evaluación",
        "cat": "Diseño y Visión Creativa",
        "url": "https://drawrecogz.streamlit.app",
        "icon": "🎨",
        "svg_type": "creative",
        "proposito": "Pizarra de bosquejado técnico y artístico con evaluación automática del trazo mediante modelos de lenguaje.",
        "codigo": "Lienzo vectorial en Canvas, exportación de mapas de bits sin pérdidas y evaluación visual con GPT-4o-mini.",
        "uso": "Prototipado ágil de interfaces, dinámicas de conceptualización gráfica y talleres educativos.",
        "color": CATEGORY_PALETTE["Diseño y Visión Creativa"]["color"]
    },
    {
        "id": 13,
        "titulo": "Consulta Documental PDF (RAG)",
        "cat": "Modelos de Lenguaje (RAG)",
        "url": "https://chatpdfz.streamlit.app",
        "icon": "💬",
        "svg_type": "text",
        "proposito": "Extracción y resolución de consultas precisas sobre expedientes PDF extensos mediante recuperación vectorial.",
        "codigo": "Chunking jerárquico, cálculo de embeddings en OpenAI, indexación de similitud con FAISS y síntesis fundamentada.",
        "uso": "Auditoría de pliegos contractuales, estudio de manuales de ingeniería y síntesis de literatura científica.",
        "color": CATEGORY_PALETTE["Modelos de Lenguaje (RAG)"]["color"]
    },
    {
        "id": 14,
        "titulo": "Analizador Tonal de Mensajes",
        "cat": "Procesamiento de Lenguaje",
        "url": "https://textanalysiz.streamlit.app",
        "icon": "⚖️",
        "svg_type": "text",
        "proposito": "Diagnóstico de neutralidad, carga subjetiva y polaridad emocional en redacción corporativa antes de su envío.",
        "codigo": "Algoritmo léxico en español con más de 40 reglas para cuantificadores, negaciones y trazado visual con Plotly.",
        "uso": "Supervisión de comunicaciones corporativas, mediación en servicio al cliente y redacción técnica.",
        "color": CATEGORY_PALETTE["Procesamiento de Lenguaje"]["color"]
    },
    {
        "id": 15,
        "titulo": "Modelador de Sistemas Físicos",
        "cat": "Modelado Físico y Tensor",
        "url": "https://histinfz.streamlit.app",
        "icon": "⚡",
        "svg_type": "neural",
        "proposito": "Esquematización técnica de mecanismos, poleas y palancas con deducción de ecuaciones de equilibrio estático.",
        "codigo": "Reconocimiento geométrico asistido por visión artificial, acoplamiento de momentos y formulación analítica.",
        "uso": "Validación de prototipos mecánicos iniciales y pedagogía en ciencias físicas e ingeniería.",
        "color": CATEGORY_PALETTE["Modelado Físico y Tensor"]["color"]
    },
    {
        "id": 16,
        "titulo": "Generador de Relatos Ilustrados",
        "cat": "Diseño y Visión Creativa",
        "url": "https://ejemplohistinfz.streamlit.app",
        "icon": "📖",
        "svg_type": "creative",
        "proposito": "Transformación de bocetos manuales en narrativas literarias infantiles estructuradas con sentido pedagógico.",
        "codigo": "Vectorización y limpieza de bocetos, articulación de trama en tres actos con GPT-4o-mini en español neutro.",
        "uso": "Fomento lector en etapas escolares primarias, dinámicas lúdicas y fomento de expresión temprana.",
        "color": CATEGORY_PALETTE["Diseño y Visión Creativa"]["color"]
    },
    {
        "id": 17,
        "titulo": "Telemetría y Monitor IoT",
        "cat": "Sistemas IoT y Telemetría",
        "url": "https://receptz.streamlit.app",
        "icon": "📡",
        "svg_type": "iot",
        "proposito": "Monitor en tiempo real de temperatura, humedad, presión y tiempo activo sincronizado con gemelo digital en Wokwi.",
        "codigo": "Pasarela persistente en segundo plano mediante Paho MQTT, deserialización de tramas JSON y actualización en memoria.",
        "uso": "Supervisión de estaciones meteorológicas, salas de servidores y monitoreo de confort higrotérmico.",
        "color": CATEGORY_PALETTE["Sistemas IoT y Telemetría"]["color"]
    },
    {
        "id": 18,
        "titulo": "Controlador de Actuadores IoT",
        "cat": "Actuación Ciberfísica",
        "url": "https://sendcmqttz.streamlit.app",
        "icon": "⚡",
        "svg_type": "iot",
        "proposito": "Consola remota para gobierno de hardware: conmutación digital de matrices LED y posicionamiento de servomotores (0°-180°).",
        "codigo": "Despacho asíncrono sobre socket persistente hacia nodo ESP32, bitácora de auditoría y gemelo digital incrustado.",
        "uso": "Domótica distribuida, control de compuertas y conmutación de potencia en entornos de laboratorio.",
        "color": CATEGORY_PALETTE["Actuación Ciberfísica"]["color"]
    },
    {
        "id": 19,
        "titulo": "Control por Voz para IoT",
        "cat": "Interfaces Vocales IoT",
        "url": "https://ctrlvoicez.streamlit.app",
        "icon": "🎙️",
        "svg_type": "audio",
        "proposito": "Comando manos libres en lenguaje natural que transforma órdenes de voz en acciones físicas sobre microcontroladores.",
        "codigo": "Captura en cliente por Web Speech API, enrutador semántico de intención y publicación inmediata de tópicos MQTT.",
        "uso": "Accesibilidad para operarios en líneas de montaje, cabinas de control y automatización sin contacto.",
        "color": CATEGORY_PALETTE["Interfaces Vocales IoT"]["color"]
    }
]

# ==============================================================================
# 5. ESTILOS CSS REFINADOS (GALAXY & PLATINUM)
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
    max-width: 1260px !important;
    padding-top: 1rem !important;
    padding-bottom: 3.5rem !important;
    margin: 0 auto !important;
    position: relative;
    z-index: 10;
}

.brand-signature {
    text-align: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.74rem;
    letter-spacing: 0.28em;
    color: #cbd5e1;
    text-transform: uppercase;
}

.main-title {
    font-size: clamp(2rem, 3.4vw, 2.9rem);
    font-weight: 700;
    text-align: center;
    color: #ffffff;
    line-height: 1.15;
    margin: 0.4rem 0 0.3rem 0;
    letter-spacing: -0.02em;
    text-shadow: 0 0 25px rgba(99, 102, 241, 0.25);
}

.sub-lead {
    text-align: center;
    color: #94a3b8;
    font-size: 0.95rem;
    max-width: 760px;
    margin: 0 auto 1.4rem auto;
    line-height: 1.55;
}

/* Indicadores de Auditoría */
.stat-pill {
    border-radius: 8px;
    padding: 10px 14px;
    text-align: center;
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.55);
}

.stat-pill-silver {
    background: rgba(14, 20, 36, 0.94);
    border: 1px solid rgba(203, 213, 225, 0.28);
}

.stat-pill-cyan {
    background: rgba(10, 20, 42, 0.94);
    border: 1px solid rgba(56, 189, 248, 0.32);
}

.stat-pill-purple {
    background: rgba(18, 14, 38, 0.94);
    border: 1px solid rgba(168, 85, 247, 0.32);
}

.stat-pill-sapphire {
    background: rgba(12, 18, 44, 0.94);
    border: 1px solid rgba(96, 165, 250, 0.32);
}

/* Barra de Progreso Líquida */
.lava-progress-frame {
    background: rgba(10, 16, 32, 0.94);
    border: 1px solid rgba(203, 213, 225, 0.2);
    border-radius: 30px;
    padding: 6px 14px;
    margin-bottom: 1.4rem;
    box-shadow: 0 4px 18px rgba(0, 0, 0, 0.6);
}

.lava-progress-bar {
    width: 100%;
    height: 8px;
    background: rgba(255, 255, 255, 0.08);
    border-radius: 6px;
    overflow: hidden;
}

.lava-progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #1d4ed8, #3b82f6, #38bdf8, #cbd5e1, #a855f7, #6366f1, #1d4ed8);
    background-size: 260% 100%;
    animation: galaxyStream 4.5s linear infinite;
    border-radius: 6px;
    box-shadow: 0 0 12px rgba(129, 140, 248, 0.5);
    transition: width 0.3s ease;
}

@keyframes galaxyStream {
    0% { background-position: 0% 50%; }
    100% { background-position: 260% 50%; }
}

/* Tarjeta Principal del Carrusel */
.carousel-card {
    background: linear-gradient(145deg, rgba(12, 18, 38, 0.96) 0%, rgba(7, 10, 22, 0.98) 100%);
    border: 1px solid rgba(203, 213, 225, 0.18);
    border-radius: 12px;
    padding: 22px 26px;
    box-shadow: 0 14px 40px rgba(0, 0, 0, 0.75);
    margin-bottom: 0.8rem;
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.card-top-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
    flex-wrap: wrap;
    gap: 8px;
}

.cat-badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    font-weight: 600;
    border-radius: 6px;
    padding: 4px 10px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
}

.id-badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.74rem;
    color: #cbd5e1;
    background: rgba(203, 213, 225, 0.1);
    border: 1px solid rgba(203, 213, 225, 0.22);
    border-radius: 6px;
    padding: 3px 8px;
    margin-left: 8px;
}

.visited-badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: #2dd4bf;
    background: rgba(45, 212, 191, 0.12);
    border: 1px solid rgba(45, 212, 191, 0.35);
    border-radius: 6px;
    padding: 3px 9px;
}

.card-title {
    font-size: clamp(1.4rem, 2.4vw, 1.9rem);
    font-weight: 700;
    color: #ffffff;
    line-height: 1.25;
    margin-bottom: 12px;
}

.section-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 3px;
    font-weight: 600;
}

.section-text {
    font-size: 0.95rem;
    line-height: 1.55;
    color: #e2e8f0;
    margin-bottom: 10px;
}

.code-box {
    background: rgba(4, 7, 18, 0.75);
    border-left: 3px solid #cbd5e1;
    border-radius: 6px;
    padding: 10px 14px;
    font-size: 0.9rem;
    color: #cbd5e1;
    line-height: 1.55;
    margin-bottom: 10px;
}

.use-box {
    border-radius: 6px;
    padding: 10px 14px;
    font-size: 0.9rem;
    color: #f1f5f9;
    line-height: 1.55;
}

/* Botones de Control */
div.stButton > button {
    border-radius: 6px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    background: rgba(14, 20, 38, 0.92) !important;
    color: #e2e8f0 !important;
    border: 1px solid rgba(203, 213, 225, 0.25) !important;
    padding: 0.65rem 1.2rem !important;
    transition: all 0.2s ease !important;
}

div.stButton > button:hover {
    border-color: #38bdf8 !important;
    color: #ffffff !important;
    box-shadow: 0 0 16px rgba(56, 189, 248, 0.35) !important;
}

/* Enlaces Directos */
div[data-testid="stLinkButton"] > a {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: 100% !important;
    background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 40%, #7c3aed 75%, #c084fc 100%) !important;
    color: #ffffff !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    border-radius: 6px !important;
    padding: 0.7rem 1.2rem !important;
    text-decoration: none !important;
    box-shadow: 0 0 18px rgba(99, 102, 241, 0.45) !important;
    transition: all 0.2s ease !important;
    border: 1px solid rgba(226, 232, 240, 0.25) !important;
}

div[data-testid="stLinkButton"] > a:hover {
    box-shadow: 0 0 25px rgba(192, 132, 252, 0.6) !important;
    transform: translateY(-1px) !important;
}

/* Matriz de Aplicaciones */
.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 14px;
    margin-top: 10px;
}

.grid-card {
    background: rgba(10, 15, 30, 0.95);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-top: 3px solid #38bdf8;
    border-radius: 8px;
    padding: 14px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.5);
    transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
}

.grid-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 22px rgba(0, 0, 0, 0.7);
}

.grid-card-link {
    display: inline-block;
    width: 100%;
    text-align: center;
    border-radius: 4px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    font-weight: 600;
    padding: 8px;
    text-decoration: none;
    transition: all 0.2s ease;
    margin-top: 8px;
    border: 1px solid transparent;
}
</style>
""")

# ==============================================================================
# 6. CANVAS GPU CÓSMICO (PARTÍCULAS AZUL, PÚRPURA Y PLATINO)
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
            { x: w * 0.15, y: h * 0.25, r: 180 * scale, vx: 0.5, vy: 0.4, color: 'rgba(37, 99, 235, 0.22)' },
            { x: w * 0.85, y: h * 0.35, r: 200 * scale, vx: -0.4, vy: 0.5, color: 'rgba(56, 189, 248, 0.20)' },
            { x: w * 0.5,  y: h * 0.85, r: 170 * scale, vx: 0.4, vy: -0.5, color: 'rgba(124, 58, 237, 0.20)' },
            { x: w * 0.2,  y: h * 0.75, r: 160 * scale, vx: -0.4, vy: -0.4, color: 'rgba(192, 132, 252, 0.16)' },
            { x: w * 0.75, y: h * 0.8,  r: 150 * scale, vx: 0.3, vy: -0.3, color: 'rgba(203, 213, 225, 0.10)' }
        ];

        const pColors = ['#38bdf8', '#818cf8', '#c084fc', '#93c5fd', '#e2e8f0', '#a78bfa', '#60a5fa'];
        const pCount = pWin.innerWidth < 768 ? 18 : 28;
        const particles = [];
        for (let i = 0; i < pCount; i++) {
            particles.push({
                x: Math.random() * w,
                y: Math.random() * h,
                r: Math.random() * 1.5 + 0.7,
                vx: (Math.random() - 0.5) * 0.5,
                vy: (Math.random() - 0.5) * 0.5,
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

                for (let j = i + 1; j < particles.length; j++) {
                    const p2 = particles[j];
                    const dx = p.x - p2.x;
                    const dy = p.y - p2.y;
                    const d2 = dx * dx + dy * dy;
                    if (d2 < 3800) {
                        ctx.beginPath();
                        ctx.moveTo(p.x, p.y);
                        ctx.lineTo(p2.x, p2.y);
                        ctx.strokeStyle = `rgba(203, 213, 225, ${0.25 * (1 - d2 / 3800)})`;
                        ctx.lineWidth = 0.6;
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
# 7. GENERADORES VECTORIALES HUD (INCLUYENDO NODO IOT)
# ==============================================================================
def generar_svg_emblema():
    return """
    <div style="display:flex; justify-content:center; align-items:center; margin-bottom:8px;">
    <svg width="86" height="86" viewBox="0 0 100 100" style="filter: drop-shadow(0 0 14px rgba(129,140,248,0.45));">
        <style>
            .spin-cw { transform-origin: 50px 50px; animation: rClock 15s linear infinite; will-change: transform; }
            .spin-ccw { transform-origin: 50px 50px; animation: rCounter 10s linear infinite; will-change: transform; }
            .pulse-core { transform-origin: 50px 50px; animation: rPulse 2.4s ease-in-out infinite alternate; will-change: transform; }
            @keyframes rClock { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
            @keyframes rCounter { 0% { transform: rotate(360deg); } 100% { transform: rotate(0deg); } }
            @keyframes rPulse { 0% { transform: scale(0.93); opacity: 0.85; } 100% { transform: scale(1.07); opacity: 1; } }
        </style>
        <circle class="spin-cw" cx="50" cy="50" r="44" fill="none" stroke="#cbd5e1" stroke-width="1.4" stroke-dasharray="10 6 3 6" opacity="0.85"/>
        <circle class="spin-ccw" cx="50" cy="50" r="34" fill="none" stroke="#38bdf8" stroke-width="1.4" stroke-dasharray="8 5 12 5" opacity="0.9"/>
        <polygon class="spin-cw" points="50,22 57,34 70,34 60,42 63,55 50,47 37,55 40,42 30,34 43,34" fill="none" stroke="#c084fc" stroke-width="1.1" opacity="0.8"/>
        <g class="pulse-core">
            <circle cx="50" cy="50" r="13" fill="rgba(56,189,248,0.18)" stroke="#cbd5e1" stroke-width="1.6"/>
            <text x="50" y="54" font-size="13" font-family="'JetBrains Mono', monospace" font-weight="bold" fill="#ffffff" text-anchor="middle">✦</text>
        </g>
    </svg>
    </div>
    """

def generar_svg_hud(tipo: str, color_hex: str):
    if tipo == "iot":
        return f"""
        <div style="background:rgba(8,14,30,0.96); border:1px solid {color_hex}55; border-radius:10px; padding:14px; text-align:center; box-shadow:0 6px 20px rgba(0,0,0,0.6);">
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_hex}; letter-spacing:0.16em; margin-bottom:6px;">NODO CIBERFÍSICO // MQTT</div>
            <svg width="220" height="170" viewBox="0 0 220 170">
                <style>
                    .iot-pulse {{ animation: rPulse 1.8s ease-in-out infinite alternate; will-change: transform; }}
                    .spin-rad {{ transform-origin: 110px 85px; animation: rClock 12s linear infinite; will-change: transform; }}
                </style>
                <circle cx="110" cy="85" r="62" fill="none" stroke="rgba(203,213,225,0.15)" stroke-width="1" stroke-dasharray="4 4"/>
                <circle cx="110" cy="85" r="42" fill="none" stroke="{color_hex}" stroke-width="1.2" opacity="0.4"/>
                <circle class="spin-rad" cx="110" cy="85" r="24" fill="none" stroke="#cbd5e1" stroke-width="1.2" stroke-dasharray="8 6"/>
                <path d="M 110 30 L 110 48" stroke="{color_hex}" stroke-width="2"/>
                <path d="M 110 122 L 110 140" stroke="{color_hex}" stroke-width="2"/>
                <path d="M 55 85 L 73 85" stroke="#cbd5e1" stroke-width="2"/>
                <path d="M 147 85 L 165 85" stroke="#cbd5e1" stroke-width="2"/>
                <circle class="iot-pulse" cx="110" cy="85" r="10" fill="none" stroke="{color_hex}" stroke-width="2"/>
                <circle cx="110" cy="85" r="4" fill="#38bdf8"/>
                <text x="110" y="156" font-family="'JetBrains Mono'" font-size="9" fill="#cbd5e1" text-anchor="middle">MQTT QOS 1 PERSISTENTE</text>
            </svg>
        </div>
        """
    elif tipo == "vision":
        return f"""
        <div style="background:rgba(8,14,30,0.96); border:1px solid {color_hex}55; border-radius:10px; padding:14px; text-align:center; box-shadow:0 6px 20px rgba(0,0,0,0.6);">
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_hex}; letter-spacing:0.16em; margin-bottom:6px;">MODO ÓPTICO ACTIVO</div>
            <svg width="220" height="170" viewBox="0 0 220 170">
                <style>
                    .laser-sweep {{ animation: sweepY 2.8s ease-in-out infinite alternate; will-change: transform; }}
                    .spin-reticle {{ transform-origin: 110px 85px; animation: rClock 14s linear infinite; will-change: transform; }}
                    @keyframes sweepY {{ 0% {{ transform: translateY(15px); }} 100% {{ transform: translateY(145px); }} }}
                </style>
                <rect x="5" y="5" width="210" height="160" fill="none" stroke="rgba(203,213,225,0.18)" stroke-width="1" rx="6"/>
                <circle class="spin-reticle" cx="110" cy="85" r="54" fill="none" stroke="{color_hex}" stroke-width="1.3" stroke-dasharray="10 6 4 6" opacity="0.7"/>
                <circle cx="110" cy="85" r="26" fill="none" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="5 3"/>
                <rect x="65" y="40" width="90" height="90" fill="none" stroke="{color_hex}" stroke-width="1.3" stroke-dasharray="8 6"/>
                <path d="M 60 48 L 60 36 L 72 36" fill="none" stroke="#cbd5e1" stroke-width="1.8"/>
                <path d="M 160 48 L 160 36 L 148 36" fill="none" stroke="#cbd5e1" stroke-width="1.8"/>
                <path d="M 60 122 L 60 134 L 72 134" fill="none" stroke="#cbd5e1" stroke-width="1.8"/>
                <path d="M 160 122 L 160 134 L 148 134" fill="none" stroke="#cbd5e1" stroke-width="1.8"/>
                <line class="laser-sweep" x1="10" y1="0" x2="210" y2="0" stroke="{color_hex}" stroke-width="1.8" opacity="0.85"/>
                <text x="110" y="89" font-family="'JetBrains Mono'" font-size="9" fill="#f1f5f9" text-anchor="middle">ANÁLISIS DE CUADRO</text>
            </svg>
        </div>
        """
    elif tipo == "audio":
        return f"""
        <div style="background:rgba(8,14,30,0.96); border:1px solid {color_hex}55; border-radius:10px; padding:14px; text-align:center; box-shadow:0 6px 20px rgba(0,0,0,0.6);">
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_hex}; letter-spacing:0.16em; margin-bottom:6px;">ESPECTRO AUDITIVO</div>
            <svg width="220" height="170" viewBox="0 0 220 170">
                <style>
                    .bar1 {{ transform-origin: bottom; animation: bScale 0.9s ease-in-out infinite alternate; will-change: transform; }}
                    .bar2 {{ transform-origin: bottom; animation: bScale 0.7s ease-in-out infinite 0.2s alternate; will-change: transform; }}
                    .bar3 {{ transform-origin: bottom; animation: bScale 1.1s ease-in-out infinite 0.4s alternate; will-change: transform; }}
                    @keyframes bScale {{ 0% {{ transform: scaleY(0.3); }} 100% {{ transform: scaleY(1.15); }} }}
                </style>
                <circle cx="110" cy="80" r="48" fill="none" stroke="#cbd5e1" stroke-width="1.1" opacity="0.35"/>
                <circle cx="110" cy="80" r="26" fill="none" stroke="{color_hex}" stroke-width="1.1" stroke-dasharray="4 3"/>
                <g transform="translate(55, 80)">
                    <rect class="bar1" x="0" y="-30" width="7" height="60" rx="3" fill="#cbd5e1"/>
                    <rect class="bar2" x="16" y="-38" width="7" height="76" rx="3" fill="{color_hex}"/>
                    <rect class="bar3" x="32" y="-48" width="7" height="96" rx="3" fill="#38bdf8"/>
                    <rect class="bar1" x="48" y="-40" width="7" height="80" rx="3" fill="{color_hex}"/>
                    <rect class="bar2" x="64" y="-30" width="7" height="60" rx="3" fill="#c084fc"/>
                    <rect class="bar3" x="80" y="-44" width="7" height="88" rx="3" fill="#cbd5e1"/>
                    <rect class="bar1" x="96" y="-24" width="7" height="48" rx="3" fill="{color_hex}"/>
                </g>
                <text x="110" y="154" font-family="'JetBrains Mono'" font-size="9" fill="#cbd5e1" text-anchor="middle">SÍNTESIS CONTINUA</text>
            </svg>
        </div>
        """
    elif tipo == "neural":
        return f"""
        <div style="background:rgba(8,14,30,0.96); border:1px solid {color_hex}55; border-radius:10px; padding:14px; text-align:center; box-shadow:0 6px 20px rgba(0,0,0,0.6);">
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_hex}; letter-spacing:0.16em; margin-bottom:6px;">PROCESAMIENTO NEURONAL</div>
            <svg width="220" height="170" viewBox="0 0 220 170">
                <style>
                    .syn-fire {{ animation: sPulse 1.6s ease-in-out infinite alternate; will-change: opacity; }}
                    .cad-spin {{ transform-origin: 110px 85px; animation: rClock 18s linear infinite; will-change: transform; }}
                    @keyframes sPulse {{ 0% {{ opacity: 0.35; stroke-width: 1; }} 100% {{ opacity: 1; stroke-width: 2.2; }} }}
                </style>
                <circle class="cad-spin" cx="110" cy="85" r="60" fill="none" stroke="rgba(203,213,225,0.18)" stroke-width="1.2" stroke-dasharray="10 8"/>
                <line class="syn-fire" x1="40" y1="45" x2="110" y2="60" stroke="{color_hex}"/>
                <line class="syn-fire" x1="40" y1="85" x2="110" y2="85" stroke="#cbd5e1"/>
                <line class="syn-fire" x1="40" y1="125" x2="110" y2="110" stroke="{color_hex}"/>
                <line class="syn-fire" x1="110" y1="60" x2="180" y2="85" stroke="#38bdf8"/>
                <line class="syn-fire" x1="110" y1="110" x2="180" y2="85" stroke="{color_hex}"/>
                <circle cx="40" cy="45" r="7" fill="#050811" stroke="{color_hex}" stroke-width="1.8"/>
                <circle cx="40" cy="85" r="7" fill="#050811" stroke="#cbd5e1" stroke-width="1.8"/>
                <circle cx="40" cy="125" r="7" fill="#050811" stroke="{color_hex}" stroke-width="1.8"/>
                <circle cx="110" cy="60" r="8" fill="#050811" stroke="#38bdf8" stroke-width="1.8"/>
                <circle cx="110" cy="110" r="8" fill="#050811" stroke="{color_hex}" stroke-width="1.8"/>
                <circle cx="180" cy="85" r="10" fill="#050811" stroke="#cbd5e1" stroke-width="2"/>
                <text x="110" y="154" font-family="'JetBrains Mono'" font-size="9" fill="#cbd5e1" text-anchor="middle">MATRIZ CONVOLUCIONAL</text>
            </svg>
        </div>
        """
    elif tipo == "text":
        return f"""
        <div style="background:rgba(8,14,30,0.96); border:1px solid {color_hex}55; border-radius:10px; padding:14px; text-align:center; box-shadow:0 6px 20px rgba(0,0,0,0.6);">
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_hex}; letter-spacing:0.16em; margin-bottom:6px;">EXTRACCIÓN SEMÁNTICA</div>
            <svg width="220" height="170" viewBox="0 0 220 170">
                <style>
                    .data-flow {{ stroke-dasharray: 6 4; animation: fDash 2.8s linear infinite; will-change: stroke-dashoffset; }}
                    @keyframes fDash {{ 0% {{ stroke-dashoffset: 0; }} 100% {{ stroke-dashoffset: -40; }} }}
                </style>
                <path class="data-flow" d="M 15 45 Q 70 20, 110 60 T 205 45" fill="none" stroke="{color_hex}" stroke-width="1.7"/>
                <path class="data-flow" d="M 15 85 Q 70 120, 110 85 T 205 85" fill="none" stroke="#cbd5e1" stroke-width="1.7"/>
                <path class="data-flow" d="M 15 125 Q 70 100, 110 115 T 205 125" fill="none" stroke="#38bdf8" stroke-width="1.7"/>
                <circle cx="55" cy="35" r="5" fill="#050811" stroke="{color_hex}" stroke-width="1.8"/>
                <circle cx="110" cy="85" r="7" fill="#050811" stroke="#cbd5e1" stroke-width="1.8"/>
                <circle cx="165" cy="120" r="5" fill="#050811" stroke="#38bdf8" stroke-width="1.8"/>
                <text x="110" y="154" font-family="'JetBrains Mono'" font-size="9" fill="#cbd5e1" text-anchor="middle">ÍNDICE VECTORIAL</text>
            </svg>
        </div>
        """
    else:
        return f"""
        <div style="background:rgba(8,14,30,0.96); border:1px solid {color_hex}55; border-radius:10px; padding:14px; text-align:center; box-shadow:0 6px 20px rgba(0,0,0,0.6);">
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_hex}; letter-spacing:0.16em; margin-bottom:6px;">COMPOSICIÓN GRÁFICA</div>
            <svg width="220" height="170" viewBox="0 0 220 170">
                <style>
                    .prism-spin {{ transform-origin: 110px 80px; animation: rClock 14s linear infinite; will-change: transform; }}
                </style>
                <polygon class="prism-spin" points="110,32 148,108 72,108" fill="rgba(192,132,252,0.12)" stroke="{color_hex}" stroke-width="1.6"/>
                <circle class="prism-spin" cx="110" cy="80" r="24" fill="none" stroke="#cbd5e1" stroke-width="1.2" stroke-dasharray="6 4"/>
                <circle cx="48" cy="42" r="3" fill="#38bdf8"/>
                <circle cx="172" cy="50" r="3" fill="{color_hex}"/>
                <circle cx="160" cy="128" r="3" fill="#cbd5e1"/>
                <circle cx="58" cy="118" r="3" fill="#818cf8"/>
                <text x="110" y="152" font-family="'JetBrains Mono'" font-size="9" fill="#cbd5e1" text-anchor="middle">CANVAS DINÁMICO</text>
            </svg>
        </div>
        """

# ==============================================================================
# 8. CABECERA MAESTRA Y AUDITORÍA EN TIEMPO REAL
# ==============================================================================
render_clean_html(generar_svg_emblema())
render_clean_html('<div class="brand-signature">Sistemas e Interfaces Multimodales</div>')
render_clean_html('<div class="main-title">Portafolio de Aplicaciones</div>')
render_clean_html('<div class="sub-lead">Catálogo de 19 desarrollos en visión por computador, modelos de lenguaje, interfaces ciberfísicas IoT y acústica aplicada.</div>')

total_apps = len(CATALOGO)
visitadas_count = len(st.session_state.visited_apps)
progreso_pct = int((visitadas_count / total_apps) * 100)

s1, s2, s3, s4 = st.columns(4)
with s1:
    render_clean_html(f'<div class="stat-pill stat-pill-silver"><div style="font-size:0.68rem; color:#cbd5e1; font-family:\'JetBrains Mono\';">TOTAL APLICACIONES</div><div style="font-size:1.5rem; font-weight:700; color:#ffffff;">{total_apps}</div></div>')
with s2:
    render_clean_html(f'<div class="stat-pill stat-pill-cyan"><div style="font-size:0.68rem; color:#38bdf8; font-family:\'JetBrains Mono\';">VERIFICADAS</div><div style="font-size:1.5rem; font-weight:700; color:#38bdf8;">{visitadas_count} de {total_apps}</div></div>')
with s3:
    render_clean_html(f'<div class="stat-pill stat-pill-purple"><div style="font-size:0.68rem; color:#c084fc; font-family:\'JetBrains Mono\';">COBERTURA</div><div style="font-size:1.5rem; font-weight:700; color:#c084fc;">{progreso_pct}%</div></div>')
with s4:
    categorias_unicas = len(set(a["cat"] for a in CATALOGO))
    render_clean_html(f'<div class="stat-pill stat-pill-sapphire"><div style="font-size:0.68rem; color:#93c5fd; font-family:\'JetBrains Mono\';">ÁREAS TÉCNICAS</div><div style="font-size:1.5rem; font-weight:700; color:#93c5fd;">{categorias_unicas}</div></div>')

st.write("")

# Barra de progreso líquida
render_clean_html(f"""
<div class="lava-progress-frame">
    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono'; font-size:0.72rem; margin-bottom:5px; padding:0 4px;">
        <span style="color:#cbd5e1;">PROGRESO DE EXPLORACIÓN</span>
        <span style="color:#38bdf8; font-weight:600;">{visitadas_count} de {total_apps} verificadas ({progreso_pct}%)</span>
    </div>
    <div class="lava-progress-bar">
        <div class="lava-progress-fill" style="width: {max(5, progreso_pct)}%;"></div>
    </div>
</div>
""")

# ==============================================================================
# 9. FILTRADO Y SELECTOR INTUITIVO
# ==============================================================================
c_search, c_filter = st.columns([1.5, 1], gap="medium")
with c_search:
    termino_busqueda = st.text_input(
        "Buscar aplicación:",
        placeholder="Ej: YOLO, IoT, actuadores, voz, PDF, Wokwi, MNIST...",
        label_visibility="collapsed"
    )
with c_filter:
    todas_cats = ["Todas las áreas"] + sorted(list(set(a["cat"] for a in CATALOGO)))
    cat_seleccionada = st.selectbox("Filtrar por categoría:", todas_cats, label_visibility="collapsed")

filtradas = [
    app for app in CATALOGO
    if (cat_seleccionada == "Todas las áreas" or app["cat"] == cat_seleccionada)
    and (
        not termino_busqueda
        or termino_busqueda.lower() in app["titulo"].lower()
        or termino_busqueda.lower() in app["proposito"].lower()
        or termino_busqueda.lower() in app["codigo"].lower()
        or termino_busqueda.lower() in app["uso"].lower()
    )
]

if not filtradas:
    st.info("Sin coincidencias para los criterios indicados.")
    filtradas = CATALOGO

st.session_state.carousel_idx = max(0, min(st.session_state.carousel_idx, len(filtradas) - 1))
app_actual = filtradas[st.session_state.carousel_idx]
esta_visitada = app_actual["id"] in st.session_state.visited_apps

nombres_apps = [f"#{a['id']:02d} — {a['titulo']} ({a['cat']})" for a in filtradas]
idx_seleccionado = st.selectbox(
    "Seleccionar aplicación:",
    options=range(len(filtradas)),
    format_func=lambda i: nombres_apps[i],
    index=st.session_state.carousel_idx,
    label_visibility="collapsed"
)
if idx_seleccionado != st.session_state.carousel_idx:
    st.session_state.carousel_idx = idx_seleccionado
    st.rerun()

# ==============================================================================
# 10. FICHA TÉCNICA PRINCIPAL Y HUD INTERACTIVO
# ==============================================================================
badge_visita_html = (
    '<span class="visited-badge">✓ Verificada</span>'
    if esta_visitada
    else '<span style="font-family:\'JetBrains Mono\'; font-size:0.72rem; color:#cbd5e1; background:rgba(203,213,225,0.08); padding:3px 8px; border-radius:6px; border:1px solid rgba(203,213,225,0.2);">○ Pendiente</span>'
)

col_desc, col_hud = st.columns([1.5, 0.9], gap="medium")

with col_desc:
    html_card = f"""
    <div class="carousel-card" style="border-top:3px solid {app_actual['color']}; box-shadow:0 14px 40px rgba(0,0,0,0.75), 0 0 24px {app_actual['color']}22;">
        <div class="card-top-row">
            <div>
                <span class="cat-badge" style="background:{app_actual['color']}20; border:1px solid {app_actual['color']}66; color:{app_actual['color']};">
                    {app_actual['icon']} {app_actual['cat']}
                </span>
                <span class="id-badge">
                    APLICACIÓN #{app_actual['id']:02d} DE {total_apps:02d}
                </span>
            </div>
            <div>{badge_visita_html}</div>
        </div>
        <div class="card-title">{app_actual['titulo']}</div>
        <div class="section-label" style="color:{app_actual['color']};">Descripción Funcional</div>
        <div class="section-text">{app_actual['proposito']}</div>
        <div class="section-label" style="color:#cbd5e1;">Arquitectura Subyacente</div>
        <div class="code-box">⚙️ {app_actual['codigo']}</div>
        <div class="section-label" style="color:{app_actual['color']};">Impacto Operativo</div>
        <div class="use-box" style="background:{app_actual['color']}12; border-left:3px solid {app_actual['color']};">
            💡 <b>Uso práctico:</b> {app_actual['uso']}
        </div>
    </div>
    """
    render_clean_html(html_card)

with col_hud:
    render_clean_html(generar_svg_hud(app_actual["svg_type"], app_actual["color"]))

# Controles de Flujo de Verificación
col_ant, col_visitar, col_toggle, col_sig = st.columns([1, 1.6, 1.4, 1], gap="small")

with col_ant:
    if st.button("← Anterior", use_container_width=True):
        st.session_state.carousel_idx = (st.session_state.carousel_idx - 1) % len(filtradas)
        st.rerun()

with col_visitar:
    st.link_button(f"Abrir {app_actual['titulo'].split()[0]} ↗", app_actual["url"], use_container_width=True)

with col_toggle:
    btn_lbl = "✓ Desmarcar" if esta_visitada else "Marcar como verificada"
    if st.button(btn_lbl, use_container_width=True):
        if esta_visitada:
            st.session_state.visited_apps.remove(app_actual["id"])
        else:
            st.session_state.visited_apps.add(app_actual["id"])
        st.rerun()

with col_sig:
    if st.button("Siguiente →", use_container_width=True):
        st.session_state.carousel_idx = (st.session_state.carousel_idx + 1) % len(filtradas)
        st.rerun()

st.write("")
st.divider()

# ==============================================================================
# 11. MATRIZ GENERAL COMPLETA (19 APLICACIONES)
# ==============================================================================
st.markdown("### Directorio de Acceso y Evaluación")
st.markdown(
    "<p style='color:#cbd5e1; font-size:0.88rem; margin-top:-8px;'>Navegación directa con codificación cromática en gamas fría y platino.</p>",
    unsafe_allow_html=True
)

grid_cards_html = ['<div class="grid-container">']
for item in CATALOGO:
    item_visitado = item["id"] in st.session_state.visited_apps
    simbolo_visita = "✓ Verificada" if item_visitado else "○ Pendiente"
    color_visita = "#2dd4bf" if item_visitado else "#94a3b8"

    grid_cards_html.append(f"""
    <div class="grid-card" style="border-top-color:{item['color']};">
        <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                <span style="font-size:1.15rem;">{item['icon']}</span>
                <span style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_visita}; font-weight:600;">{simbolo_visita}</span>
            </div>
            <div style="font-weight:700; font-size:0.92rem; color:#ffffff; min-height:40px; line-height:1.25;">{item['titulo']}</div>
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{item['color']}; margin:3px 0 6px 0; text-transform:uppercase; font-weight:600;">
                ● {item['cat']}
            </div>
            <p style="font-size:0.8rem; color:#94a3b8; line-height:1.4; margin-bottom:8px;">{item['proposito'][:78]}...</p>
        </div>
        <a href="{item['url']}" target="_blank" class="grid-card-link"
           style="background:{item['color']}18; border-color:{item['color']}55; color:{item['color']};">
            Abrir aplicación ↗
        </a>
    </div>
    """)
grid_cards_html.append('</div>')

render_clean_html("".join(grid_cards_html))

st.write("")
render_clean_html("""
<div style="text-align:center; padding:1.8rem 0; border-top:1px solid rgba(203,213,225,0.14); margin-top:2rem;">
    <div style="font-family:'JetBrains Mono'; font-size:0.74rem; letter-spacing:0.2em; color:#cbd5e1; text-transform:uppercase;">
        PORTAFOLIO DE SISTEMAS E INTERFACES MULTIMODALES
    </div>
    <div style="font-size:0.8rem; color:#64748b; margin-top:4px;">
        19 aplicaciones desplegadas sobre Streamlit Cloud
    </div>
</div>
""")
