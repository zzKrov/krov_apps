import streamlit as st
import streamlit.components.v1 as components

# ============================================================
# CONFIGURACIÓN GENERAL DEL PORTAFOLIO
# ============================================================
st.set_page_config(
    page_title="Krov Industries // Portafolio",
    page_icon="⚜",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# FUNCIÓN LIMPIADORA (CERO FUGAS DE CÓDIGO HTML)
# ============================================================
def render_clean_html(html_str: str):
    compact = "\n".join(line.strip() for line in html_str.splitlines() if line.strip())
    st.markdown(compact, unsafe_allow_html=True)

# ============================================================
# ESTADO DE SESIÓN
# ============================================================
if "carousel_idx" not in st.session_state:
    st.session_state.carousel_idx = 0

if "visited_apps" not in st.session_state:
    st.session_state.visited_apps = set()

# ============================================================
# CATÁLOGO DE LAS 16 APLICACIONES DE KROV INDUSTRIES
# ============================================================
CATALOGO = [
    {
        "id": 1,
        "titulo": "Detector de Objetos en Vivo",
        "cat": "Visión Artificial",
        "url": "https://yolozz.streamlit.app",
        "icon": "🎯",
        "svg_type": "vision",
        "proposito": "Encuadra y cuenta en tiempo real lo que aparece ante tu cámara o en fotos: personas, autos, sillas, computadores y hasta 80 clases comunes.",
        "codigo": "Ejecuta el modelo ultraliviano YOLOv5 de PyTorch a decenas de cuadros por segundo. Utiliza filtros matemáticos para evitar cajas duplicadas y aviso acústico armónico.",
        "uso": "Inventarios de almacenes en segundos, monitoreo de aforo en accesos y asistencia visual para personas con baja visión.",
        "color": "#ffd700"
    },
    {
        "id": 2,
        "titulo": "Generador de Nube de Palabras",
        "cat": "Texto y Semántica",
        "url": "https://wordcloudz.streamlit.app",
        "icon": "☁️",
        "svg_type": "text",
        "proposito": "Convierte documentos extensos en una composición visual donde las palabras más importantes resaltan en tamaño proporcional según su frecuencia real.",
        "codigo": "Limpia el texto con expresiones regulares en Python, descarta automáticamente conectores en español o inglés y genera siluetas con la biblioteca WordCloud.",
        "uso": "Descubrir qué opinan los clientes en cientos de reseñas, resumir informes extensos y analizar discursos.",
        "color": "#38bdf8"
    },
    {
        "id": 3,
        "titulo": "Reconocedor de Dígitos Ópticos",
        "cat": "Redes Neuronales",
        "url": "https://mnistz.streamlit.app",
        "icon": "✍️",
        "svg_type": "neural",
        "proposito": "Un lienzo donde dibujas un número a mano alzada del 0 al 9 y una red neuronal predice exactamente cuál dibujaste y su porcentaje de certeza.",
        "codigo": "Aísla el trazo con una caja límite en Pillow, lo centra con márgenes proporcionales (28×28 Lanczos) y clasifica probabilidades con redes convolucionales en Keras/TensorFlow.",
        "uso": "Digitalización automática de cheques bancarios, clasificación postal y procesamiento de formularios censales.",
        "color": "#a855f7"
    },
    {
        "id": 4,
        "titulo": "Análisis Contextual de Imagen",
        "cat": "Visión Multimodal",
        "url": "https://visionz.streamlit.app",
        "icon": "👁️",
        "svg_type": "vision",
        "proposito": "Sube cualquier imagen y la inteligencia artificial te entregará una descripción minuciosa y profesional de todo lo que ocurre en la escena.",
        "codigo": "Convierte la imagen a cadenas seguras en base64 y realiza una conexión directa por streaming con el modelo GPT-4o de OpenAI para recibir respuestas palabra por palabra.",
        "uso": "Peritaje de vehículos chocados para aseguradoras, inspección de grietas en obras civiles y audiodescripción accesible.",
        "color": "#00f0ff"
    },
    {
        "id": 5,
        "titulo": "Traductor de Voz a Audio",
        "cat": "Voz y Acústica",
        "url": "https://traductorz.streamlit.app",
        "icon": "🎙️",
        "svg_type": "audio",
        "proposito": "Habla por el micrófono de tu computador o teléfono; el sistema escucha tus palabras, las traduce al idioma elegido y las pronuncia en voz alta.",
        "codigo": "Aprovecha el motor nativo Web Speech del navegador mediante puentes Bokeh, traduce con servidores de Google y sintetiza voz con gTTS modulando acentos por país.",
        "uso": "Comunicarse sin barreras durante viajes internacionales, atender turistas en ventanillas y practicar pronunciación.",
        "color": "#ec4899"
    },
    {
        "id": 6,
        "titulo": "Detector de Presencia y Postura",
        "cat": "Visión Artificial",
        "url": "https://teachablez.streamlit.app",
        "icon": "🛡️",
        "svg_type": "vision",
        "proposito": "Monitorea si hay un ser humano frente a la pantalla y revisa su postura física sin enviar ningún fotograma a internet, protegiendo tu privacidad.",
        "codigo": "Corre íntegramente en tu navegador con TensorFlow.js y PoseNet sobre un lienzo Canvas. Valida fotogramas consecutivos analizando ojos, nariz y articulaciones corporales.",
        "uso": "Corregir malas posturas ergonómicas frente a la pantalla, activar quioscos interactivos y registrar aforo seguro.",
        "color": "#00ff88"
    },
    {
        "id": 7,
        "titulo": "Espacio de Humor y Bienestar",
        "cat": "Interacción Lúdica",
        "url": "https://bendover.streamlit.app",
        "icon": "🐇",
        "svg_type": "creative",
        "proposito": "Zona de relajación visual donde un conejo juguetón sigue tu ratón desatando estelas de fuego artificial, mientras cuenta chistes con voz sintetizada.",
        "codigo": "Construido en JavaScript puro sobre Canvas con física de partículas fluida en GPU. Utiliza la API nativa de voz del navegador para narrar chistes aleatorios sin demoras de red.",
        "uso": "Pausas activas durante jornadas laborales extenuantes, descanso mental y reducción de la fatiga frente al monitor.",
        "color": "#fb923c"
    },
    {
        "id": 8,
        "titulo": "Compañero de Conversación Empático",
        "cat": "Interacción Humana",
        "url": "https://sentimentz.streamlit.app",
        "icon": "🤖",
        "svg_type": "text",
        "proposito": "Un confidente digital con el que puedes compartir si tuviste un día tenso o un gran logro, recibiendo palabras de apoyo serenas y constructivas.",
        "codigo": "Evalúa el tono de tu mensaje con clasificadores semánticos nativos y sincroniza el estado de ánimo con un robot animado en Lottie, acompañado de voz sintetizada multilingüe.",
        "uso": "Diario emocional interactivo, reflexión tras jornadas de estrés y acompañamiento para clarificar ideas.",
        "color": "#c084fc"
    },
    {
        "id": 9,
        "titulo": "Espejo Mágico de Lectura",
        "cat": "Óptica y Traducción",
        "url": "https://ocryaudioz.streamlit.app",
        "icon": "🪞",
        "svg_type": "vision",
        "proposito": "Captura fotos de documentos, letreros o libros y proyéctalos en un visor 3D que resalta el texto, lo traduce y te lo lee en voz alta.",
        "codigo": "Filtra sombras y ruido en OpenCV con ecualización adaptativa CLAHE. Extrae letras con Tesseract OCR y anima el texto sobre una superficie 3D reactiva al movimiento.",
        "uso": "Entender letreros o menús en alfabetos extranjeros durante viajes y digitalizar lecturas para personas con fatiga visual.",
        "color": "#f43f5e"
    },
    {
        "id": 10,
        "titulo": "Reconocimiento Óptico por Cámara",
        "cat": "Óptica y Documentos",
        "url": "https://lectorz.streamlit.app",
        "icon": "📷",
        "svg_type": "vision",
        "proposito": "Transforma la cámara web de tu computador en un escáner instantáneo que extrae párrafos completos de libros o pantallas con solo tomar una foto.",
        "codigo": "Aplica una ampliación bicúbica al doble de resolución para mejorar la nitidez, invierte automáticamente fondos oscuros y extrae métricas de caracteres y palabras.",
        "uso": "Copiar citas textuales de libros físicos sin escribirlas a mano y registrar recibos de compra impresos.",
        "color": "#e11d48"
    },
    {
        "id": 11,
        "titulo": "Interfaces Multimodales Sensoriales",
        "cat": "Sistemas Sensoriales",
        "url": "https://sussusamogus.streamlit.app",
        "icon": "✦",
        "svg_type": "audio",
        "proposito": "Laboratorio interactivo que demuestra cómo una aplicación puede comunicarse a la vez mediante destellos de luz, sonidos armónicos y vibración física.",
        "codigo": "Genera ondas de sonido puras en la memoria RAM con Python, hace vibrar teléfonos móviles reales mediante la API Navigator y dispara pulsos ópticos en pantalla.",
        "uso": "Diseñar cabinas de automóviles inteligentes con alertas sonoras y táctiles, controles de videojuegos y software accesible.",
        "color": "#c5a059"
    },
    {
        "id": 12,
        "titulo": "Tablero de Bocetos Creativos",
        "cat": "Visión Creativa",
        "url": "https://drawrecogz.streamlit.app",
        "icon": "🎨",
        "svg_type": "creative",
        "proposito": "Dibuja bosquejos a mano alzada con múltiples herramientas geométricas y recibe una crítica artística e interpretación de tu obra por IA.",
        "codigo": "Pizarra de dibujo digital con soporte de trazo libre, rectángulos, círculos y polígonos. Exporta la imagen sobre fondo blanco y la analiza mediante GPT-4o-mini de OpenAI.",
        "uso": "Lluvia de ideas visual en estudios de diseño, dibujo recreativo y conceptualización temprana de interfaces.",
        "color": "#ff007f"
    },
    {
        "id": 13,
        "titulo": "Asesor de Documentos PDF (RAG)",
        "cat": "Texto y Documentos",
        "url": "https://chatpdfz.streamlit.app",
        "icon": "💬",
        "svg_type": "text",
        "proposito": "Sube cualquier archivo PDF (manual, contrato o libro) y hazle preguntas directas: el sistema te responderá únicamente con lo que dice el documento.",
        "codigo": "Aplica la técnica RAG (Generación Aumentada por Recuperación): trocea el PDF, calcula vectores semánticos con OpenAI Embeddings, busca coincidencias con FAISS y sintetiza con GPT-4o-mini.",
        "uso": "Revisar contratos legales extensos sin leer cientos de páginas, estudiar manuales técnicos y resumir artículos científicos.",
        "color": "#0ea5e9"
    },
    {
        "id": 14,
        "titulo": "Analizador Tonal y Emocional",
        "cat": "Texto y Semántica",
        "url": "https://textanalysiz.streamlit.app",
        "icon": "⚖️",
        "svg_type": "text",
        "proposito": "Examina la actitud de tus escritos antes de enviarlos: descubre si tu mensaje suena positivo, enojado, neutral o con excesiva carga subjetiva.",
        "codigo": "Motor léxico en español nativo con más de 40 reglas semánticas para intensificadores y negaciones. Grafica la evolución del ánimo frase por frase con Plotly y medidores SVG.",
        "uso": "Pulir correos corporativos antes de negociaciones delicadas, medir el impacto de comunicados de prensa y moderar soporte al cliente.",
        "color": "#ffd700"
    },
    {
        "id": 15,
        "titulo": "Deductor de Sistemas Físicos",
        "cat": "Redes y Física",
        "url": "https://histinfz.streamlit.app",
        "icon": "⚡",
        "svg_type": "neural",
        "proposito": "Traza esquemas mecánicos, poleas, palancas o circuitos en un plano estilo ingeniería y recibe la formulación matemática de su equilibrio físico.",
        "codigo": "Lienzo técnico vectorial asistido por visión artificial. El modelo traduce las formas geométricas en: límites del sistema, mecánica de fuerzas acopladas y proyección cinemática.",
        "uso": "Resolver ejercicios de física para estudiantes universitarios, validar prototipos de maquinaria y estudiar sistemas de fuerza.",
        "color": "#00f6ff"
    },
    {
        "id": 16,
        "titulo": "Taller de Cuentos Ilustrados",
        "cat": "Visión Creativa",
        "url": "https://ejemplohistinfz.streamlit.app",
        "icon": "📖",
        "svg_type": "creative",
        "proposito": "Un espacio mágico donde niños o educadores dibujan un personaje y la inteligencia artificial inventa un cuento infantil con moraleja inspirado en el dibujo.",
        "codigo": "Convierte los garabatos infantiles en imágenes digitales limpias y solicita a GPT-4o-mini una narrativa dulce, estructurada con título, aventura y desenlace formativo en español natural.",
        "uso": "Estimular el hábito de lectura en escuelas primarias, juegos creativos familiares y dinámicas pedagógicas infantiles.",
        "color": "#06d6a0"
    }
]

# ============================================================
# ESTILOS CSS ULTRA OPTIMIZADOS (GPU COMPOSITING PURO)
# ============================================================
render_clean_html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,500;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;600;700&family=JetBrains+Mono:wght@400;600;700&display=swap');

html, body, [data-testid="stAppViewContainer"], .stApp {
    background: transparent !important;
    background-color: transparent !important;
    color: #f1f5f9 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    overflow-x: hidden;
    touch-action: manipulation;
}

body {
    background-color: #030407 !important;
}

[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stSidebar"], section[data-testid="stSidebar"] { display: none !important; }

.block-container {
    max-width: 1200px !important;
    padding-top: 1rem !important;
    padding-bottom: 3.5rem !important;
    margin: 0 auto !important;
    position: relative;
    z-index: 10;
}

.brand-signature {
    text-align: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.76rem;
    letter-spacing: 0.28em;
    color: #ffd700;
    text-transform: uppercase;
    text-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
}

.main-title {
    font-family: 'Spectral', Georgia, serif;
    font-size: clamp(2rem, 3.8vw, 3.2rem);
    font-weight: 700;
    text-align: center;
    color: #ffffff;
    line-height: 1.1;
    margin-bottom: 0.2rem;
    text-shadow: 0 0 25px rgba(255, 215, 0, 0.4), 0 0 50px rgba(0, 240, 255, 0.25);
}

.sub-lead {
    text-align: center;
    color: #94a3b8;
    font-size: 0.95rem;
    max-width: 760px;
    margin: 0 auto 1.2rem auto;
    line-height: 1.5;
}

/* Indicadores Superiores */
.stat-pill {
    background: rgba(12, 16, 26, 0.94);
    border: 1px solid rgba(255, 215, 0, 0.25);
    border-radius: 8px;
    padding: 10px 12px;
    text-align: center;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.7);
    transform: translateZ(0);
}

/* Barra de progreso líquida ultra liviana */
.lava-progress-frame {
    background: rgba(12, 16, 26, 0.94);
    border: 1px solid rgba(255, 215, 0, 0.28);
    border-radius: 30px;
    padding: 6px 14px;
    margin-bottom: 1.2rem;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.8);
    transform: translateZ(0);
}

.lava-progress-bar {
    width: 100%;
    height: 10px;
    background: rgba(255, 255, 255, 0.08);
    border-radius: 8px;
    overflow: hidden;
}

.lava-progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #ffd700, #ff007f, #00f0ff, #00ff88, #ffd700);
    background-size: 200% 100%;
    animation: fastLava 4s linear infinite;
    border-radius: 8px;
    box-shadow: 0 0 12px rgba(255, 215, 0, 0.8);
    transition: width 0.35s ease;
    will-change: background-position, width;
}

@keyframes fastLava {
    0% { background-position: 0% 50%; }
    100% { background-position: 200% 50%; }
}

/* Tarjeta Principal del Carrusel (Sin backdrop-filter para 60 FPS garantizados) */
.carousel-card {
    background: linear-gradient(145deg, rgba(14, 18, 30, 0.96) 0%, rgba(6, 8, 14, 0.98) 100%);
    border: 1px solid rgba(255, 215, 0, 0.35);
    border-top: 3px solid #ffd700;
    border-radius: 12px;
    padding: 22px 26px;
    box-shadow: 0 15px 45px rgba(0, 0, 0, 0.85), 0 0 25px rgba(255, 215, 0, 0.15);
    margin-bottom: 0.8rem;
    position: relative;
    overflow: hidden;
    transform: translateZ(0);
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
    letter-spacing: 0.12em;
    text-transform: uppercase;
    font-weight: 700;
    border-radius: 6px;
    padding: 3px 9px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
}

.visited-badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: #00ff88;
    background: rgba(0, 255, 136, 0.12);
    border: 1px solid rgba(0, 255, 136, 0.4);
    border-radius: 6px;
    padding: 3px 9px;
    display: inline-block;
}

.card-title {
    font-family: 'Spectral', Georgia, serif;
    font-size: clamp(1.5rem, 2.6vw, 2.1rem);
    font-weight: 700;
    color: #ffffff;
    line-height: 1.2;
    margin-bottom: 10px;
    text-shadow: 0 0 15px rgba(255, 255, 255, 0.18);
}

.section-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #ffd700;
    margin-bottom: 3px;
    font-weight: 700;
}

.section-text {
    font-size: 0.96rem;
    line-height: 1.55;
    color: #f1f5f9;
    margin-bottom: 10px;
}

.code-box {
    background: rgba(0, 0, 0, 0.6);
    border-left: 3px solid #00f0ff;
    border-radius: 6px;
    padding: 10px 14px;
    font-size: 0.92rem;
    color: #cbd5e1;
    line-height: 1.55;
    margin-bottom: 10px;
}

.use-box {
    background: rgba(255, 215, 0, 0.08);
    border-left: 3px solid #ffd700;
    border-radius: 6px;
    padding: 10px 14px;
    font-size: 0.92rem;
    color: #f8fafc;
    line-height: 1.55;
}

/* Botones de navegación */
div.stButton > button {
    border-radius: 6px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    background: rgba(14, 18, 30, 0.92) !important;
    color: #f1f5f9 !important;
    border: 1px solid rgba(255, 215, 0, 0.35) !important;
    padding: 0.65rem 1.2rem !important;
    transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease !important;
    transform: translateZ(0);
}

div.stButton > button:hover {
    transform: translateY(-2px) !important;
    border-color: #ffd700 !important;
    color: #ffd700 !important;
    box-shadow: 0 0 20px rgba(255, 215, 0, 0.45) !important;
}

/* Botón de enlace principal para abrir la app */
div[data-testid="stLinkButton"] > a {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: 100% !important;
    background: linear-gradient(135deg, #ffd700 0%, #ff007f 50%, #00f0ff 100%) !important;
    color: #020306 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 700 !important;
    font-size: 0.9rem !important;
    letter-spacing: 0.03em !important;
    border-radius: 6px !important;
    padding: 0.7rem 1.2rem !important;
    text-decoration: none !important;
    box-shadow: 0 0 20px rgba(255, 215, 0, 0.5) !important;
    transition: transform 0.2s ease, box-shadow 0.2s ease !important;
    transform: translateZ(0);
}

div[data-testid="stLinkButton"] > a:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 0 35px rgba(0, 240, 255, 0.8) !important;
    color: #ffffff !important;
}

/* Cuadrícula CSS pura de alto rendimiento para el directorio */
.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 14px;
    margin-top: 10px;
}

.grid-card {
    background: rgba(12, 15, 24, 0.95);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-top: 2px solid #ffd700;
    border-radius: 8px;
    padding: 14px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.6);
    transform: translateZ(0);
    transition: transform 0.2s ease, border-color 0.2s ease;
}

.grid-card:hover {
    transform: translateY(-3px);
    border-color: #ffd700;
    box-shadow: 0 8px 25px rgba(255, 215, 0, 0.25);
}

.grid-card-link {
    display: inline-block;
    width: 100%;
    text-align: center;
    background: rgba(255, 215, 0, 0.12);
    border: 1px solid rgba(255, 215, 0, 0.35);
    color: #ffd700;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    font-weight: 700;
    padding: 8px;
    border-radius: 4px;
    text-decoration: none;
    transition: all 0.2s ease;
    margin-top: 8px;
}

.grid-card-link:hover {
    background: #ffd700;
    color: #020306;
    box-shadow: 0 0 15px rgba(255, 215, 0, 0.6);
}
</style>
""")

# ============================================================
# CANVAS GPU LIGERO (BÚFER DOWNSAMPLEADO: 60 FPS FIJOS EN MÓVIL)
# ============================================================
components.html(
    """
    <script>
    (function() {
        const pWin = window.parent;
        const pDoc = pWin.document;
        if (pWin.__KROV_LIGHTNING_BG__) return;
        pWin.__KROV_LIGHTNING_BG__ = true;

        let canvas = pDoc.getElementById('krov-light-canvas');
        if (!canvas) {
            canvas = pDoc.createElement('canvas');
            canvas.id = 'krov-light-canvas';
            canvas.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:0;background:#030407;';
            pDoc.body.prepend(canvas);
        }

        const ctx = canvas.getContext('2d', { alpha: false });
        const isMobile = pWin.innerWidth < 768;
        // Búfer reducido al 50% en móvil y 65% en PC: disminuye la tasa de relleno por 4x sin perder brillo
        const scale = isMobile ? 0.45 : 0.65;
        let w = canvas.width = Math.floor(pWin.innerWidth * scale);
        let h = canvas.height = Math.floor(pWin.innerHeight * scale);

        pWin.addEventListener('resize', () => {
            w = canvas.width = Math.floor(pWin.innerWidth * scale);
            h = canvas.height = Math.floor(pWin.innerHeight * scale);
        });

        // 4 Orbes de plasma saturados
        const orbs = [
            { x: w * 0.15, y: h * 0.25, r: 180 * scale, vx: 0.7, vy: 0.5, color: 'rgba(255, 215, 0, 0.22)' },
            { x: w * 0.85, y: h * 0.35, r: 200 * scale, vx: -0.6, vy: 0.6, color: 'rgba(0, 240, 255, 0.20)' },
            { x: w * 0.5, y: h * 0.8, r: 170 * scale, vx: 0.6, vy: -0.6, color: 'rgba(255, 0, 127, 0.18)' },
            { x: w * 0.2, y: h * 0.75, r: 160 * scale, vx: -0.5, vy: -0.5, color: 'rgba(0, 255, 136, 0.16)' }
        ];

        // Partículas estelares reducidas (16 en móvil, 28 en PC)
        const pCount = isMobile ? 16 : 28;
        const particles = [];
        for (let i = 0; i < pCount; i++) {
            particles.push({
                x: Math.random() * w,
                y: Math.random() * h,
                r: Math.random() * 1.5 + 0.8,
                vx: (Math.random() - 0.5) * 0.6,
                vy: (Math.random() - 0.5) * 0.6,
                color: ['#ffd700', '#00f0ff', '#ff007f', '#00ff88'][i % 4]
            });
        }

        function loop() {
            ctx.fillStyle = '#030407';
            ctx.fillRect(0, 0, w, h);

            // 1. Orbes de plasma en modo pantalla
            ctx.globalCompositeOperation = 'screen';
            for (let b of orbs) {
                b.x += b.vx;
                b.y += b.vy;
                if (b.x < -40 || b.x > w + 40) b.vx *= -1;
                if (b.y < -40 || b.y > h + 40) b.vy *= -1;

                const g = ctx.createRadialGradient(b.x, b.y, 2, b.x, b.y, b.r);
                g.addColorStop(0, b.color);
                g.addColorStop(1, 'rgba(3,4,7,0)');
                ctx.beginPath();
                ctx.arc(b.x, b.y, b.r, 0, Math.PI * 2);
                ctx.fillStyle = g;
                ctx.fill();
            }

            // 2. Partículas estelares rápidas
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

                // Conexiones láser optimizadas por distancia cuadrática
                for (let j = i + 1; j < particles.length; j++) {
                    const p2 = particles[j];
                    const dx = p.x - p2.x;
                    const dy = p.y - p2.y;
                    const d2 = dx * dx + dy * dy;
                    if (d2 < 4200) {
                        ctx.beginPath();
                        ctx.moveTo(p.x, p.y);
                        ctx.lineTo(p2.x, p2.y);
                        ctx.strokeStyle = `rgba(0, 240, 255, ${0.3 * (1 - d2 / 4200)})`;
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

# ============================================================
# GENERADOR DE SVGS ANIMADOS LIGEROS (GPU-ACCELERATED)
# ============================================================
def generar_svg_emblema():
    """Giroscopio animado puramente vectorial mediante transformaciones CSS de GPU."""
    return """
    <div style="display:flex; justify-content:center; align-items:center; margin-bottom:8px;">
    <svg width="90" height="90" viewBox="0 0 100 100" style="filter: drop-shadow(0 0 12px rgba(255,215,0,0.6));">
        <style>
            .spin-cw { transform-origin: 50px 50px; animation: rClock 10s linear infinite; will-change: transform; }
            .spin-ccw { transform-origin: 50px 50px; animation: rCounter 7s linear infinite; will-change: transform; }
            .pulse-core { transform-origin: 50px 50px; animation: rPulse 2s ease-in-out infinite alternate; will-change: transform; }
            @keyframes rClock { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
            @keyframes rCounter { 0% { transform: rotate(360deg); } 100% { transform: rotate(0deg); } }
            @keyframes rPulse { 0% { transform: scale(0.92); opacity: 0.8; } 100% { transform: scale(1.08); opacity: 1; } }
        </style>
        <circle class="spin-cw" cx="50" cy="50" r="44" fill="none" stroke="#ffd700" stroke-width="1.8" stroke-dasharray="12 6 3 6"/>
        <circle class="spin-ccw" cx="50" cy="50" r="34" fill="none" stroke="#00f0ff" stroke-width="1.5" stroke-dasharray="8 5 15 5" opacity="0.85"/>
        <polygon class="spin-cw" points="50,20 57,33 71,33 60,42 64,55 50,47 36,55 40,42 29,33 43,33" fill="none" stroke="#ff007f" stroke-width="1" opacity="0.75"/>
        <g class="pulse-core">
            <circle cx="50" cy="50" r="14" fill="rgba(255,215,0,0.2)" stroke="#ffd700" stroke-width="1.8"/>
            <text x="50" y="55" font-size="15" font-family="'Spectral', serif" font-weight="bold" fill="#ffffff" text-anchor="middle">⚜</text>
        </g>
    </svg>
    </div>
    """

def generar_svg_hud(tipo: str, color_hex: str):
    """Visores HUD animados en tiempo real sin filtros pesados."""
    if tipo == "vision":
        return f"""
        <div style="background:rgba(10,14,24,0.96); border:1px solid {color_hex}55; border-radius:10px; padding:14px; text-align:center; box-shadow:0 8px 25px rgba(0,0,0,0.8);">
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_hex}; letter-spacing:0.18em; margin-bottom:6px;">● CANAL ÓPTICO ACTIVO</div>
            <svg width="220" height="170" viewBox="0 0 220 170" style="filter: drop-shadow(0 0 8px {color_hex}44);">
                <style>
                    .laser-sweep {{ animation: sweepY 2.5s ease-in-out infinite alternate; will-change: transform; }}
                    .spin-reticle {{ transform-origin: 110px 85px; animation: rClock 12s linear infinite; will-change: transform; }}
                    @keyframes sweepY {{ 0% {{ transform: translateY(15px); }} 100% {{ transform: translateY(145px); }} }}
                </style>
                <rect x="5" y="5" width="210" height="160" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1" rx="6"/>
                <circle class="spin-reticle" cx="110" cy="85" r="55" fill="none" stroke="{color_hex}" stroke-width="1.4" stroke-dasharray="10 6 4 6" opacity="0.6"/>
                <circle cx="110" cy="85" r="28" fill="none" stroke="#00f0ff" stroke-width="1" stroke-dasharray="5 3"/>
                <rect x="65" y="40" width="90" height="90" fill="none" stroke="{color_hex}" stroke-width="1.5" stroke-dasharray="8 6"/>
                <!-- Haces angulares -->
                <path d="M 60 50 L 60 35 L 75 35" fill="none" stroke="{color_hex}" stroke-width="2"/>
                <path d="M 160 50 L 160 35 L 145 35" fill="none" stroke="{color_hex}" stroke-width="2"/>
                <path d="M 60 120 L 60 135 L 75 135" fill="none" stroke="{color_hex}" stroke-width="2"/>
                <path d="M 160 120 L 160 135 L 145 135" fill="none" stroke="{color_hex}" stroke-width="2"/>
                <!-- Línea de escaneo láser -->
                <line class="laser-sweep" x1="10" y1="0" x2="210" y2="0" stroke="{color_hex}" stroke-width="2" opacity="0.85"/>
                <text x="110" y="89" font-family="'JetBrains Mono'" font-size="9" fill="#ffffff" text-anchor="middle">TRACKING [99.4%]</text>
            </svg>
        </div>
        """
    elif tipo == "audio":
        return f"""
        <div style="background:rgba(10,14,24,0.96); border:1px solid {color_hex}55; border-radius:10px; padding:14px; text-align:center; box-shadow:0 8px 25px rgba(0,0,0,0.8);">
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_hex}; letter-spacing:0.18em; margin-bottom:6px;">● ESPECTRO ACÚSTICO // HÁPTICO</div>
            <svg width="220" height="170" viewBox="0 0 220 170" style="filter: drop-shadow(0 0 8px {color_hex}44);">
                <style>
                    .bar1 {{ transform-origin: bottom; animation: bScale 0.8s ease-in-out infinite alternate; will-change: transform; }}
                    .bar2 {{ transform-origin: bottom; animation: bScale 0.6s ease-in-out infinite 0.2s alternate; will-change: transform; }}
                    .bar3 {{ transform-origin: bottom; animation: bScale 1.0s ease-in-out infinite 0.4s alternate; will-change: transform; }}
                    @keyframes bScale {{ 0% {{ transform: scaleY(0.25); }} 100% {{ transform: scaleY(1.2); }} }}
                </style>
                <circle cx="110" cy="80" r="50" fill="none" stroke="{color_hex}" stroke-width="1.2" opacity="0.3"/>
                <circle cx="110" cy="80" r="28" fill="none" stroke="#00f0ff" stroke-width="1" stroke-dasharray="4 3"/>
                <g transform="translate(55, 80)">
                    <rect class="bar1" x="0" y="-30" width="7" height="60" rx="3" fill="{color_hex}"/>
                    <rect class="bar2" x="16" y="-40" width="7" height="80" rx="3" fill="#00f0ff"/>
                    <rect class="bar3" x="32" y="-50" width="7" height="100" rx="3" fill="{color_hex}"/>
                    <rect class="bar1" x="48" y="-42" width="7" height="84" rx="3" fill="#ff007f"/>
                    <rect class="bar2" x="64" y="-32" width="7" height="64" rx="3" fill="{color_hex}"/>
                    <rect class="bar3" x="80" y="-46" width="7" height="92" rx="3" fill="#00ff88"/>
                    <rect class="bar1" x="96" y="-25" width="7" height="50" rx="3" fill="{color_hex}"/>
                </g>
                <text x="110" y="156" font-family="'JetBrains Mono'" font-size="9" fill="#cbd5e1" text-anchor="middle">587.33 Hz HARMONIC SYNC</text>
            </svg>
        </div>
        """
    elif tipo == "neural":
        return f"""
        <div style="background:rgba(10,14,24,0.96); border:1px solid {color_hex}55; border-radius:10px; padding:14px; text-align:center; box-shadow:0 8px 25px rgba(0,0,0,0.8);">
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_hex}; letter-spacing:0.18em; margin-bottom:6px;">● SINÁPSIS Y DEDUCCIÓN CAD</div>
            <svg width="220" height="170" viewBox="0 0 220 170" style="filter: drop-shadow(0 0 8px {color_hex}44);">
                <style>
                    .syn-fire {{ animation: sPulse 1.5s ease-in-out infinite alternate; will-change: opacity; }}
                    .cad-spin {{ transform-origin: 110px 85px; animation: rClock 16s linear infinite; will-change: transform; }}
                    @keyframes sPulse {{ 0% {{ opacity: 0.3; stroke-width: 1; }} 100% {{ opacity: 1; stroke-width: 2.2; }} }}
                </style>
                <circle class="cad-spin" cx="110" cy="85" r="62" fill="none" stroke="rgba(255,255,255,0.14)" stroke-width="1.2" stroke-dasharray="10 8"/>
                <line class="syn-fire" x1="40" y1="45" x2="110" y2="60" stroke="{color_hex}"/>
                <line class="syn-fire" x1="40" y1="85" x2="110" y2="85" stroke="#00f0ff"/>
                <line class="syn-fire" x1="40" y1="125" x2="110" y2="110" stroke="{color_hex}"/>
                <line class="syn-fire" x1="110" y1="60" x2="180" y2="85" stroke="#ff007f"/>
                <line class="syn-fire" x1="110" y1="110" x2="180" y2="85" stroke="{color_hex}"/>
                <circle cx="40" cy="45" r="8" fill="#020306" stroke="{color_hex}" stroke-width="1.8"/>
                <circle cx="40" cy="85" r="8" fill="#020306" stroke="{color_hex}" stroke-width="1.8"/>
                <circle cx="40" cy="125" r="8" fill="#020306" stroke="{color_hex}" stroke-width="1.8"/>
                <circle cx="110" cy="60" r="9" fill="#020306" stroke="#00f0ff" stroke-width="1.8"/>
                <circle cx="110" cy="110" r="9" fill="#020306" stroke="#00f0ff" stroke-width="1.8"/>
                <circle cx="180" cy="85" r="11" fill="#020306" stroke="#ffd700" stroke-width="2"/>
                <text x="110" y="156" font-family="'JetBrains Mono'" font-size="9" fill="#cbd5e1" text-anchor="middle">EQUILIBRIO TENSOR V2.4</text>
            </svg>
        </div>
        """
    elif tipo == "text":
        return f"""
        <div style="background:rgba(10,14,24,0.96); border:1px solid {color_hex}55; border-radius:10px; padding:14px; text-align:center; box-shadow:0 8px 25px rgba(0,0,0,0.8);">
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_hex}; letter-spacing:0.18em; margin-bottom:6px;">● MOTOR LÉXICO // RAG SEMÁNTICO</div>
            <svg width="220" height="170" viewBox="0 0 220 170" style="filter: drop-shadow(0 0 8px {color_hex}44);">
                <style>
                    .data-flow {{ stroke-dasharray: 6 4; animation: fDash 2.5s linear infinite; will-change: stroke-dashoffset; }}
                    @keyframes fDash {{ 0% {{ stroke-dashoffset: 0; }} 100% {{ stroke-dashoffset: -40; }} }}
                </style>
                <path class="data-flow" d="M 15 45 Q 70 20, 110 60 T 205 45" fill="none" stroke="{color_hex}" stroke-width="1.8"/>
                <path class="data-flow" d="M 15 85 Q 70 120, 110 85 T 205 85" fill="none" stroke="#00f0ff" stroke-width="1.8"/>
                <path class="data-flow" d="M 15 125 Q 70 100, 110 115 T 205 125" fill="none" stroke="#ff007f" stroke-width="1.8"/>
                <circle cx="55" cy="35" r="6" fill="#030407" stroke="{color_hex}" stroke-width="1.8"/>
                <circle cx="110" cy="85" r="8" fill="#030407" stroke="#00f0ff" stroke-width="1.8"/>
                <circle cx="165" cy="120" r="6" fill="#030407" stroke="#ff007f" stroke-width="1.8"/>
                <text x="110" y="156" font-family="'JetBrains Mono'" font-size="9" fill="#cbd5e1" text-anchor="middle">FAISS VECTOR MATCH [100%]</text>
            </svg>
        </div>
        """
    else:
        return f"""
        <div style="background:rgba(10,14,24,0.96); border:1px solid {color_hex}55; border-radius:10px; padding:14px; text-align:center; box-shadow:0 8px 25px rgba(0,0,0,0.8);">
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_hex}; letter-spacing:0.18em; margin-bottom:6px;">● PRISMA CREATIVO & NARRATIVO</div>
            <svg width="220" height="170" viewBox="0 0 220 170" style="filter: drop-shadow(0 0 8px {color_hex}44);">
                <style>
                    .prism-spin {{ transform-origin: 110px 80px; animation: rClock 12s linear infinite; will-change: transform; }}
                </style>
                <polygon class="prism-spin" points="110,30 150,110 70,110" fill="rgba(255,0,127,0.15)" stroke="{color_hex}" stroke-width="1.8"/>
                <circle class="prism-spin" cx="110" cy="80" r="26" fill="none" stroke="#00f0ff" stroke-width="1.2" stroke-dasharray="6 4"/>
                <circle cx="45" cy="40" r="3" fill="#ffd700"/>
                <circle cx="175" cy="48" r="3.5" fill="#00ff88"/>
                <circle cx="165" cy="130" r="3" fill="#ff007f"/>
                <circle cx="55" cy="120" r="3.5" fill="#00f0ff"/>
                <text x="110" y="152" font-family="'JetBrains Mono'" font-size="9" fill="#cbd5e1" text-anchor="middle">GENERADOR NARRATIVO ACTIVO</text>
            </svg>
        </div>
        """

# ============================================================
# CABECERA MAESTRA Y MÉTRICAS
# ============================================================
render_clean_html(generar_svg_emblema())
render_clean_html('<div class="brand-signature">Krov Industries · Plataforma de Aplicaciones</div>')
render_clean_html('<div class="main-title">Interfaces Multimodales</div>')
render_clean_html('<div class="sub-lead">16 soluciones prácticas de visión artificial, modelos de lenguaje, procesamiento acústico y redes neuronales diseñadas para interactuar de forma natural y veloz.</div>')

# Métricas Globales
total_apps = len(CATALOGO)
visitadas_count = len(st.session_state.visited_apps)
progreso_pct = int((visitadas_count / total_apps) * 100)

s1, s2, s3, s4 = st.columns(4)
with s1:
    render_clean_html(f'<div class="stat-pill"><div style="font-size:0.68rem; color:#94a3b8; font-family:\'JetBrains Mono\';">TOTAL APLICACIONES</div><div style="font-size:1.6rem; font-weight:700; color:#ffffff;">{total_apps}</div></div>')
with s2:
    render_clean_html(f'<div class="stat-pill"><div style="font-size:0.68rem; color:#94a3b8; font-family:\'JetBrains Mono\';">EXPLORADAS</div><div style="font-size:1.6rem; font-weight:700; color:#00ff88;">{visitadas_count} de {total_apps}</div></div>')
with s3:
    render_clean_html(f'<div class="stat-pill"><div style="font-size:0.68rem; color:#94a3b8; font-family:\'JetBrains Mono\';">PROGRESO</div><div style="font-size:1.6rem; font-weight:700; color:#ffd700;">{progreso_pct}%</div></div>')
with s4:
    categorias_unicas = len(set(a["cat"] for a in CATALOGO))
    render_clean_html(f'<div class="stat-pill"><div style="font-size:0.68rem; color:#94a3b8; font-family:\'JetBrains Mono\';">DOMINIOS</div><div style="font-size:1.6rem; font-weight:700; color:#00f0ff;">{categorias_unicas}</div></div>')

st.write("")

# Barra de progreso líquida
render_clean_html(f"""
<div class="lava-progress-frame">
    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono'; font-size:0.72rem; margin-bottom:5px; padding:0 4px;">
        <span style="color:#94a3b8;">AUDITORÍA DE REVISIÓN</span>
        <span style="color:#ffd700; font-weight:700;">{visitadas_count} de {total_apps} verificadas ({progreso_pct}%)</span>
    </div>
    <div class="lava-progress-bar">
        <div class="lava-progress-fill" style="width: {max(5, progreso_pct)}%;"></div>
    </div>
</div>
""")

# ============================================================
# FILTRADO Y SELECTOR DIRECTO DE APLICACIÓN
# ============================================================
c_search, c_filter = st.columns([1.5, 1], gap="medium")
with c_search:
    termino_busqueda = st.text_input(
        "Buscar por función o tecnología:",
        placeholder="Ej: YOLO, OCR, voz, PDF, dibujo, MNIST...",
        label_visibility="collapsed"
    )
with c_filter:
    todas_cats = ["Todas las áreas"] + sorted(list(set(a["cat"] for a in CATALOGO)))
    cat_seleccionada = st.selectbox("Filtrar por dominio:", todas_cats, label_visibility="collapsed")

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
    st.info("Sin coincidencias para ese filtro. Restableciendo...")
    filtradas = CATALOGO

st.session_state.carousel_idx = max(0, min(st.session_state.carousel_idx, len(filtradas) - 1))
app_actual = filtradas[st.session_state.carousel_idx]
esta_visitada = app_actual["id"] in st.session_state.visited_apps

# Selector desplegable inmediato para saltar directo a cualquier app
nombres_apps = [f"#{a['id']:02d} - {a['titulo']}" for a in filtradas]
idx_seleccionado = st.selectbox(
    "Selector rápido de aplicación:",
    options=range(len(filtradas)),
    format_func=lambda i: nombres_apps[i],
    index=st.session_state.carousel_idx,
    label_visibility="collapsed"
)
if idx_seleccionado != st.session_state.carousel_idx:
    st.session_state.carousel_idx = idx_seleccionado
    st.rerun()

# ============================================================
# CARRUSEL CON DESCRIPCIÓN Y HUD SVG ANIMADO
# ============================================================
badge_visita_html = '<span class="visited-badge">✓ Explorada</span>' if esta_visitada else '<span style="font-family:\'JetBrains Mono\'; font-size:0.72rem; color:#94a3b8; background:rgba(255,255,255,0.08); padding:3px 8px; border-radius:6px;">○ Pendiente</span>'

col_desc, col_hud = st.columns([1.5, 0.9], gap="medium")

with col_desc:
    html_card = f"""
    <div class="carousel-card">
        <div class="card-top-row">
            <div>
                <span class="cat-badge" style="background:{app_actual['color']}22; border:1px solid {app_actual['color']}66; color:{app_actual['color']};">
                    {app_actual['icon']} {app_actual['cat']}
                </span>
                <span style="font-family:'JetBrains Mono'; font-size:0.74rem; color:#94a3b8; margin-left:8px;">
                    APP #{app_actual['id']:02d} DE {total_apps:02d}
                </span>
            </div>
            <div>{badge_visita_html}</div>
        </div>
        <div class="card-title">{app_actual['titulo']}</div>
        <div class="section-label">Propósito y Función</div>
        <div class="section-text">{app_actual['proposito']}</div>
        <div class="section-label">Arquitectura y Código Subyacente</div>
        <div class="code-box">⚙️ {app_actual['codigo']}</div>
        <div class="section-label">Aplicación Práctica Real</div>
        <div class="use-box">💡 <b>Impacto operativo:</b> {app_actual['uso']}</div>
    </div>
    """
    render_clean_html(html_card)

with col_hud:
    render_clean_html(generar_svg_hud(app_actual["svg_type"], app_actual["color"]))

# Controles de navegación y llamada a la acción
col_ant, col_visitar, col_toggle, col_sig = st.columns([1, 1.6, 1.4, 1], gap="small")

with col_ant:
    if st.button("← Anterior", use_container_width=True):
        st.session_state.carousel_idx = (st.session_state.carousel_idx - 1) % len(filtradas)
        st.rerun()

with col_visitar:
    st.link_button(f"Abrir {app_actual['titulo'].split()[0]} en Vivo ↗", app_actual["url"], use_container_width=True)

with col_toggle:
    btn_lbl = "✓ Desmarcar" if esta_visitada else "Marcar como explorada"
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

# ============================================================
# DIRECTORIO GENERAL COMPLETO (CSS GRID EN 1 SOLO BLOQUE)
# ============================================================
st.markdown("### Directorio General de Acceso Inmediato")
st.markdown("<p style='color:#94a3b8; font-size:0.88rem; margin-top:-8px;'>Haz clic en el enlace de cualquier aplicación para abrirla directamente en una nueva pestaña.</p>", unsafe_allow_html=True)

# Construcción de la cuadrícula de 16 aplicaciones en una sola pasada de alto rendimiento
grid_cards_html = ['<div class="grid-container">']
for item in CATALOGO:
    item_visitado = item["id"] in st.session_state.visited_apps
    simbolo_visita = "✓ Explorada" if item_visitado else "○ Pendiente"
    color_visita = "#00ff88" if item_visitado else "#94a3b8"

    grid_cards_html.append(f"""
    <div class="grid-card" style="border-top-color:{item['color']};">
        <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                <span style="font-size:1.2rem;">{item['icon']}</span>
                <span style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_visita}; font-weight:700;">{simbolo_visita}</span>
            </div>
            <div style="font-weight:700; font-size:0.92rem; color:#ffffff; min-height:40px; line-height:1.25;">{item['titulo']}</div>
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{item['color']}; margin:3px 0 6px 0; text-transform:uppercase;">{item['cat']}</div>
            <p style="font-size:0.8rem; color:#94a3b8; line-height:1.4; margin-bottom:8px;">{item['proposito'][:78]}...</p>
        </div>
        <a href="{item['url']}" target="_blank" class="grid-card-link">Lanzar Aplicación ↗</a>
    </div>
    """)
grid_cards_html.append('</div>')

render_clean_html("".join(grid_cards_html))

# Pie de página
st.write("")
render_clean_html("""
<div style="text-align:center; padding:1.8rem 0; border-top:1px solid rgba(255,255,255,0.08); margin-top:2rem;">
    <div style="font-family:'JetBrains Mono'; font-size:0.75rem; letter-spacing:0.2em; color:#ffd700; text-transform:uppercase;">
        KROV INDUSTRIES · DIVISION OF ARTIFICIAL INTELLIGENCE & CYBERNETICS
    </div>
    <div style="font-size:0.8rem; color:#64748b; margin-top:4px;">
        16 Aplicaciones Multimodales en Línea sobre Streamlit Cloud
    </div>
</div>
""")
