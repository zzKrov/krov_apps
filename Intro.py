import streamlit as st
import streamlit.components.v1 as components

# ============================================================
# CONFIGURACIÓN GENERAL DEL PORTAFOLIO
# ============================================================
st.set_page_config(
    page_title="Krov Industries // Portafolio Maestro de IA",
    page_icon="⚜",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# FUNCIÓN LIMPIADORA PARA EVITAR FUGAS DE HTML COMO CÓDIGO
# ============================================================
def render_clean_html(html_str: str):
    """
    Elimina cualquier indentación o espacio inicial por línea.
    Esto impide que el motor CommonMark de Streamlit interprete
    las etiquetas HTML como bloques de código preformateado.
    """
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
        "proposito": "Encuadra y cuenta en tiempo real lo que aparece ante tu cámara o en fotos subidas: personas, autos, sillas, computadores y hasta 80 clases comunes.",
        "codigo": "Ejecuta el modelo ultraliviano YOLOv5 de PyTorch a decenas de cuadros por segundo. Utiliza filtros matemáticos para evitar cajas duplicadas y un sintetizador de audio web que emite un tono suave al identificar novedades.",
        "uso": "Hacer inventarios en tiendas en segundos, contar aforo en accesos y brindar asistencia visual para personas con baja visión.",
        "color": "#ffd700"
    },
    {
        "id": 2,
        "titulo": "Generador de Nube de Palabras",
        "cat": "Texto y Semántica",
        "url": "https://wordcloudz.streamlit.app",
        "icon": "☁️",
        "svg_type": "text",
        "proposito": "Convierte documentos extensos en una composición artística donde las palabras más importantes resaltan en tamaño gigante según su frecuencia real.",
        "codigo": "Limpia el texto con expresiones regulares en Python, descarta automáticamente conectores y preposiciones en español o inglés, y dibuja siluetas geométricas con la biblioteca WordCloud y paletas cromáticas personalizadas.",
        "uso": "Descubrir de inmediato qué opinan los clientes en cientos de reseñas, resumir informes extensos y analizar discursos políticos.",
        "color": "#38bdf8"
    },
    {
        "id": 3,
        "titulo": "Reconocedor de Dígitos Ópticos",
        "cat": "Redes Neuronales",
        "url": "https://mnistz.streamlit.app",
        "icon": "✍️",
        "svg_type": "neural",
        "proposito": "Un lienzo donde dibujas un número a mano alzada del 0 al 9 y una red neuronal predice exactamente cuál dibujaste y qué porcentaje de certeza tiene.",
        "codigo": "Aísla tu trazo mediante una caja límite en Pillow, lo centra con márgenes proporcionales y lo reduce a una matriz de 28×28 píxeles. Luego, una red convolucional en Keras/TensorFlow evalúa las probabilidades de cada cifra.",
        "uso": "Digitalización automática de cheques bancarios, clasificación de códigos postales en correspondencia y lectura de planillas de votación.",
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
        "codigo": "Convierte la imagen a cadenas digitales en base64 y realiza una conexión directa por streaming con el modelo GPT-4o de OpenAI, recibiendo la interpretación palabra por palabra en tiempo real.",
        "uso": "Peritaje de vehículos chocados para aseguradoras, inspección de grietas en obras civiles y generación de audiodescripciones para no videntes.",
        "color": "#00f0ff"
    },
    {
        "id": 5,
        "titulo": "Traductor de Voz a Audio",
        "cat": "Voz y Acústica",
        "url": "https://traductorz.streamlit.app",
        "icon": "🎙️",
        "svg_type": "audio",
        "proposito": "Habla por el micrófono de tu computador o teléfono; el sistema escucha tus palabras, las traduce al idioma de tu preferencia y las lee en voz alta.",
        "codigo": "Aprovecha el motor nativo Web Speech del navegador mediante un puente en Bokeh, traduce el texto con los servidores de Google y genera la locución con la biblioteca gTTS con modulación de acentos por país.",
        "uso": "Comunicarse sin barreras durante viajes al extranjero, atender turistas en ventanillas de servicio y practicar pronunciación de idiomas.",
        "color": "#ec4899"
    },
    {
        "id": 6,
        "titulo": "Detector de Presencia y Postura",
        "cat": "Visión Artificial",
        "url": "https://teachablez.streamlit.app",
        "icon": "🛡️",
        "svg_type": "vision",
        "proposito": "Monitorea si hay un ser humano frente a la pantalla y revisa su postura física sin enviar ningún video a servidores externos, protegiendo tu privacidad.",
        "codigo": "Corre íntegramente en tu navegador con TensorFlow.js y PoseNet sobre un lienzo Canvas. Valida dos cuadros consecutivos revisando ojos, nariz y articulaciones antes de confirmar la presencia.",
        "uso": "Corregir malas posturas frente al computador, activar pantallas automáticas al acercarse un usuario y registrar aforo seguro en oficinas.",
        "color": "#00ff88"
    },
    {
        "id": 7,
        "titulo": "Espacio de Humor y Bienestar",
        "cat": "Interacción Lúdica",
        "url": "https://bendover.streamlit.app",
        "icon": "🐇",
        "svg_type": "creative",
        "proposito": "Una zona de relajación visual donde un conejo juguetón sigue tu ratón desatando estelas de fuego artificial, mientras cuenta chistes con voz sintetizada.",
        "codigo": "Construido en JavaScript puro sobre Canvas con física de partículas acelerada por GPU. Utiliza la API interna del navegador para narrar chistes aleatorios sin demoras ni consumo de datos móviles.",
        "uso": "Pausas activas durante jornadas laborales extenuantes, desconexión mental y reducción de la fatiga frente a pantallas.",
        "color": "#fb923c"
    },
    {
        "id": 8,
        "titulo": "Compañero de Conversación Empático",
        "cat": "Interacción Humana",
        "url": "https://sentimentz.streamlit.app",
        "icon": "🤖",
        "svg_type": "text",
        "proposito": "Un confidente digital con el que puedes compartir si tuviste un día tenso o un gran logro, recibiendo palabras de apoyo serenas y orientadoras.",
        "codigo": "Evalúa el tono de tu mensaje con clasificadores semánticos nativos y sincroniza el estado de ánimo con un robot animado en Lottie, acompañado de voz sintetizada en español con opción de traducción.",
        "uso": "Diario emocional personal, reflexión tras jornadas de estrés y acompañamiento interactivo para aclarar ideas.",
        "color": "#c084fc"
    },
    {
        "id": 9,
        "titulo": "Espejo Mágico de Lectura",
        "cat": "Óptica y Traducción",
        "url": "https://ocryaudioz.streamlit.app",
        "icon": "🪞",
        "svg_type": "vision",
        "proposito": "Captura fotos de documentos, letreros o libros y proyéctalos dentro de un espejo 3D que resalta el texto, lo traduce y te lo lee en voz alta.",
        "codigo": "Filtra sombras y ruido con OpenCV mediante ecualización adaptativa CLAHE. Luego extrae las letras con el motor Tesseract OCR y anima el texto sobre una superficie 3D que reacciona al movimiento del ratón.",
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
        "codigo": "Aplica una ampliación bicúbica al doble de resolución para mejorar la nitidez de las letras pequeñas, invierte automáticamente fondos oscuros y ejecuta un análisis de conteo de palabras y caracteres.",
        "uso": "Copiar citas textuales de libros físicos sin tener que escribirlas a mano y registrar recibos de compra impresos.",
        "color": "#e11d48"
    },
    {
        "id": 11,
        "titulo": "Interfaces Multimodales Sensoriales",
        "cat": "Sistemas Sensoriales",
        "url": "https://sussusamogus.streamlit.app",
        "icon": "✦",
        "svg_type": "audio",
        "proposito": "Un laboratorio interactivo que demuestra cómo una aplicación moderna puede comunicarse a la vez mediante destellos de luz, sonidos armónicos y vibración física.",
        "codigo": "Genera archivos de sonido senoidal en la memoria RAM con Python puro, hace vibrar teléfonos móviles reales mediante la API de navegación y dispara pulsos neón que iluminan toda la interfaz.",
        "uso": "Diseñar cabinas de automóviles inteligentes con alertas sonoras y táctiles, controles de videojuegos y sistemas para personas con limitaciones sensoriales.",
        "color": "#c5a059"
    },
    {
        "id": 12,
        "titulo": "Tablero de Bocetos Creativos",
        "cat": "Visión Creativa",
        "url": "https://drawrecogz.streamlit.app",
        "icon": "🎨",
        "svg_type": "creative",
        "proposito": "Dibuja figuras, objetos o bosquejos a mano alzada con múltiples herramientas y recibe una crítica constructiva e interpretación de tu obra.",
        "codigo": "Pizarra de dibujo digital con soporte de trazo libre, rectángulos, círculos y polígonos. Exporta la imagen sobre fondo blanco y la somete al análisis crítico del modelo GPT-4o-mini de OpenAI.",
        "uso": "Lluvia de ideas visual en estudios de diseño, dibujo recreativo y análisis temprano de prototipos en interfaces.",
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
        "codigo": "Aplica la técnica RAG (Generación Aumentada por Recuperación): trocea el PDF en párrafos pequeños, calcula vectores semánticos con OpenAI Embeddings, busca coincidencias con FAISS y sintetiza la respuesta con GPT-4o-mini.",
        "uso": "Revisar contratos legales extensos sin leer cientos de páginas, estudiar manuales de maquinaria y resumir artículos científicos.",
        "color": "#0ea5e9"
    },
    {
        "id": 14,
        "titulo": "Analizador Tonal y Emocional",
        "cat": "Texto y Semántica",
        "url": "https://textanalysiz.streamlit.app",
        "icon": "⚖️",
        "svg_type": "text",
        "proposito": "Examina la actitud de tus escritos antes de enviarlos: descubre si tu mensaje suena positivo, enojado, neutral o con demasiada carga emocional.",
        "codigo": "Motor léxico en español nativo con más de 40 reglas semánticas para intensificadores y negaciones. Grafica la evolución del ánimo frase por frase con Plotly y medidores animados en SVG.",
        "uso": "Pulir correos corporativos antes de negociaciones delicadas, medir el impacto de comunicados de prensa y moderar mensajes de soporte.",
        "color": "#ffd700"
    },
    {
        "id": 15,
        "titulo": "Deductor de Sistemas Físicos",
        "cat": "Redes y Física",
        "url": "https://histinfz.streamlit.app",
        "icon": "⚡",
        "svg_type": "neural",
        "proposito": "Traza esquemas mecánicos, poleas, palancas o circuitos en un plano estilo ingeniería y recibe la formulación matemática de su equilibrio.",
        "codigo": "Lienzo técnico vectorial asistido por visión artificial. El modelo de razonamiento traduce las formas geométricas en tres apartados: límites del sistema, mecánica de fuerzas acopladas y proyección cinemática.",
        "uso": "Resolver ejercicios de física para estudiantes universitarios, validar prototipos de maquinaria y estudiar sistemas de transmisión de fuerza.",
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
        "uso": "Estimular el hábito de lectura en escuelas primarias, juegos creativos entre padres e hijos y dinámicas pedagógicas infantiles.",
        "color": "#06d6a0"
    }
]

# ============================================================
# ESTILOS CSS: OBSIDIANA PROFUNDA, NEÓN Y RESPLANDOR
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
}

body {
    background-color: #020306 !important;
}

[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stSidebar"], section[data-testid="stSidebar"] { display: none !important; }

.block-container {
    max-width: 1200px !important;
    padding-top: 1.2rem !important;
    padding-bottom: 4rem !important;
    margin: 0 auto !important;
    position: relative;
    z-index: 10;
}

.brand-signature {
    text-align: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    letter-spacing: 0.3em;
    color: #ffd700;
    text-transform: uppercase;
    text-shadow: 0 0 15px rgba(255, 215, 0, 0.6);
}

.main-title {
    font-family: 'Spectral', Georgia, serif;
    font-size: clamp(2.2rem, 4.2vw, 3.4rem);
    font-weight: 700;
    text-align: center;
    color: #ffffff;
    line-height: 1.1;
    margin-bottom: 0.2rem;
    text-shadow: 0 0 35px rgba(255, 215, 0, 0.45), 0 0 70px rgba(0, 240, 255, 0.3);
}

.sub-lead {
    text-align: center;
    color: #94a3b8;
    font-size: 1rem;
    max-width: 780px;
    margin: 0 auto 1.4rem auto;
    line-height: 1.6;
}

/* Indicadores Superiores */
.stat-pill {
    background: rgba(12, 16, 28, 0.88);
    border: 1px solid rgba(255, 215, 0, 0.25);
    border-radius: 8px;
    padding: 12px 14px;
    text-align: center;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.7);
    transition: transform 0.25s ease, border-color 0.25s ease;
}

.stat-pill:hover {
    transform: translateY(-2px);
    border-color: #ffd700;
    box-shadow: 0 0 25px rgba(255, 215, 0, 0.4);
}

/* Barra de progreso líquida */
.lava-progress-frame {
    background: rgba(12, 16, 28, 0.88);
    border: 1px solid rgba(255, 215, 0, 0.3);
    border-radius: 30px;
    padding: 6px 14px;
    margin-bottom: 1.5rem;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.8), inset 0 1px 0 rgba(255, 255, 255, 0.1);
}

.lava-progress-bar {
    width: 100%;
    height: 12px;
    background: rgba(255, 255, 255, 0.08);
    border-radius: 10px;
    overflow: hidden;
}

.lava-progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #ffd700, #ff007f, #00f0ff, #00ff88, #ffd700);
    background-size: 300% 100%;
    animation: lavaFlow 3.5s linear infinite;
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(255, 215, 0, 0.9);
    transition: width 0.45s ease;
}

@keyframes lavaFlow {
    0% { background-position: 0% 50%; }
    100% { background-position: 300% 50%; }
}

/* Tarjeta Principal del Carrusel */
.carousel-card {
    background: linear-gradient(145deg, rgba(14, 18, 32, 0.94) 0%, rgba(6, 8, 16, 0.98) 100%);
    border: 1px solid rgba(255, 215, 0, 0.35);
    border-top: 3px solid #ffd700;
    border-radius: 12px;
    padding: 24px 28px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.85), 0 0 35px rgba(255, 215, 0, 0.2);
    margin-bottom: 1rem;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(16px);
}

.card-top-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 12px;
    flex-wrap: wrap;
    gap: 8px;
}

.cat-badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.74rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    font-weight: 700;
    border-radius: 6px;
    padding: 4px 10px;
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
    padding: 4px 10px;
    display: inline-block;
}

.card-title {
    font-family: 'Spectral', Georgia, serif;
    font-size: clamp(1.6rem, 2.8vw, 2.2rem);
    font-weight: 700;
    color: #ffffff;
    line-height: 1.2;
    margin-bottom: 12px;
    text-shadow: 0 0 20px rgba(255, 255, 255, 0.2);
}

.section-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #ffd700;
    margin-bottom: 4px;
    font-weight: 700;
}

.section-text {
    font-size: 1rem;
    line-height: 1.6;
    color: #f1f5f9;
    margin-bottom: 12px;
}

.code-box {
    background: rgba(0, 0, 0, 0.55);
    border-left: 3px solid #00f0ff;
    border-radius: 6px;
    padding: 12px 16px;
    font-size: 0.94rem;
    color: #cbd5e1;
    line-height: 1.6;
    margin-bottom: 12px;
}

.use-box {
    background: rgba(255, 215, 0, 0.08);
    border-left: 3px solid #ffd700;
    border-radius: 6px;
    padding: 12px 16px;
    font-size: 0.94rem;
    color: #f8fafc;
    line-height: 1.6;
}

/* Botones de navegación */
div.stButton > button {
    border-radius: 6px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.86rem !important;
    font-weight: 600 !important;
    background: rgba(18, 22, 38, 0.9) !important;
    color: #f1f5f9 !important;
    border: 1px solid rgba(255, 215, 0, 0.35) !important;
    padding: 0.75rem 1.4rem !important;
    transition: all 0.25s ease !important;
}

div.stButton > button:hover {
    transform: translateY(-2px) !important;
    border-color: #ffd700 !important;
    color: #ffd700 !important;
    box-shadow: 0 0 25px rgba(255, 215, 0, 0.5) !important;
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
    font-size: 0.92rem !important;
    letter-spacing: 0.04em !important;
    border-radius: 6px !important;
    padding: 0.75rem 1.4rem !important;
    text-decoration: none !important;
    box-shadow: 0 0 25px rgba(255, 215, 0, 0.6) !important;
    transition: all 0.25s ease !important;
}

div[data-testid="stLinkButton"] > a:hover {
    transform: translateY(-2px) scale(1.02) !important;
    box-shadow: 0 0 45px rgba(0, 240, 255, 0.9) !important;
    color: #ffffff !important;
}
</style>
""")

# ============================================================
# FONDO HIPERSATURADO DE PLASMA Y CONSTELACIONES LÁSER
# ============================================================
components.html(
    """
    <script>
    (function() {
        const pWin = window.parent;
        const pDoc = pWin.document;
        if (pWin.__KROV_FLASHY_BG__) return;
        pWin.__KROV_FLASHY_BG__ = true;

        let canvas = pDoc.getElementById('krov-flashy-canvas');
        if (!canvas) {
            canvas = pDoc.createElement('canvas');
            canvas.id = 'krov-flashy-canvas';
            canvas.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:0;background:#020306;';
            pDoc.body.prepend(canvas);
        }

        const ctx = canvas.getContext('2d');
        let w = canvas.width = pWin.innerWidth;
        let h = canvas.height = pWin.innerHeight;

        pWin.addEventListener('resize', () => {
            w = canvas.width = pWin.innerWidth;
            h = canvas.height = pWin.innerHeight;
        });

        let mouse = { x: w * 0.5, y: h * 0.5 };
        pWin.addEventListener('mousemove', (e) => {
            mouse.x = e.clientX;
            mouse.y = e.clientY;
        });

        // 5 Orbes de plasma hipersaturado
        const orbs = [
            { x: w * 0.15, y: h * 0.25, r: 340, vx: 0.55, vy: 0.45, color: 'rgba(255, 215, 0, 0.22)' },
            { x: w * 0.85, y: h * 0.35, r: 360, vx: -0.45, vy: 0.5, color: 'rgba(0, 240, 255, 0.20)' },
            { x: w * 0.5, y: h * 0.8, r: 320, vx: 0.5, vy: -0.45, color: 'rgba(255, 0, 127, 0.18)' },
            { x: w * 0.2, y: h * 0.75, r: 300, vx: -0.4, vy: -0.4, color: 'rgba(0, 255, 136, 0.16)' },
            { x: w * 0.75, y: h * 0.85, r: 330, vx: 0.4, vy: 0.4, color: 'rgba(168, 85, 247, 0.18)' }
        ];

        // 65 Partículas estelares conectadas por haces láser
        const particles = [];
        for (let i = 0; i < 65; i++) {
            particles.push({
                x: Math.random() * w,
                y: Math.random() * h,
                r: Math.random() * 2.2 + 0.8,
                vx: (Math.random() - 0.5) * 0.7,
                vy: (Math.random() - 0.5) * 0.7,
                color: ['#ffd700', '#00f0ff', '#ff007f', '#00ff88'][Math.floor(Math.random() * 4)]
            });
        }

        function loop() {
            ctx.clearRect(0, 0, w, h);
            ctx.fillStyle = '#020306';
            ctx.fillRect(0, 0, w, h);

            // 1. Dibujar orbes de plasma líquido en blend screen
            ctx.globalCompositeOperation = 'screen';
            for (let b of orbs) {
                b.x += b.vx;
                b.y += b.vy;
                if (b.x < -100 || b.x > w + 100) b.vx *= -1;
                if (b.y < -100 || b.y > h + 100) b.vy *= -1;

                const g = ctx.createRadialGradient(b.x, b.y, 10, b.x, b.y, b.r);
                g.addColorStop(0, b.color);
                g.addColorStop(1, 'transparent');
                ctx.beginPath();
                ctx.arc(b.x, b.y, b.r, 0, Math.PI * 2);
                ctx.fillStyle = g;
                ctx.fill();
            }

            // 2. Dibujar red de constelaciones y líneas láser
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
                ctx.shadowBlur = 10;
                ctx.shadowColor = p.color;
                ctx.fill();

                // Conexión entre partículas cercanas
                for (let j = i + 1; j < particles.length; j++) {
                    const p2 = particles[j];
                    const dist = Math.hypot(p.x - p2.x, p.y - p2.y);
                    if (dist < 110) {
                        ctx.beginPath();
                        ctx.moveTo(p.x, p.y);
                        ctx.lineTo(p2.x, p2.y);
                        ctx.strokeStyle = `rgba(0, 240, 255, ${0.35 * (1 - dist / 110)})`;
                        ctx.lineWidth = 0.7;
                        ctx.stroke();
                    }
                }

                // Haces reactivos que siguen al cursor
                const mouseDist = Math.hypot(p.x - mouse.x, p.y - mouse.y);
                if (mouseDist < 140) {
                    ctx.beginPath();
                    ctx.moveTo(p.x, p.y);
                    ctx.lineTo(mouse.x, mouse.y);
                    ctx.strokeStyle = `rgba(255, 215, 0, ${0.6 * (1 - mouseDist / 140)})`;
                    ctx.lineWidth = 1.0;
                    ctx.stroke();
                }
            }
            ctx.shadowBlur = 0;
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
# GENERADOR DE SVGS ANIMADOS PARA EL ENCABEZADO Y EL HUD
# ============================================================
def generar_svg_emblema():
    """Emblema heráldico y giroscopio cibernético animado en SVG."""
    return """
    <div style="display:flex; justify-content:center; align-items:center; margin-bottom:10px;">
    <svg width="110" height="110" viewBox="0 0 120 120">
        <defs>
            <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#ffd700" />
                <stop offset="50%" stop-color="#ff8800" />
                <stop offset="100%" stop-color="#00f0ff" />
            </linearGradient>
            <filter id="glow">
                <feGaussianBlur stdDeviation="3.5" result="coloredBlur"/>
                <feMerge>
                    <feMergeNode in="coloredBlur"/>
                    <feMergeNode in="SourceGraphic"/>
                </feMerge>
            </filter>
        </defs>
        <style>
            .spin-cw { transform-origin: 60px 60px; animation: spinClock 10s linear infinite; }
            .spin-ccw { transform-origin: 60px 60px; animation: spinCounter 7s linear infinite; }
            .pulse-core { transform-origin: 60px 60px; animation: corePulse 2s ease-in-out infinite alternate; }
            @keyframes spinClock { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
            @keyframes spinCounter { 0% { transform: rotate(360deg); } 100% { transform: rotate(0deg); } }
            @keyframes corePulse { 0% { transform: scale(0.9); opacity: 0.8; } 100% { transform: scale(1.15); opacity: 1; } }
        </style>
        <!-- Anillo exterior con muescas radar -->
        <circle class="spin-cw" cx="60" cy="60" r="54" fill="none" stroke="url(#goldGrad)" stroke-width="2" stroke-dasharray="14 8 4 8" filter="url(#glow)"/>
        <!-- Anillo interior contra-rotatorio -->
        <circle class="spin-ccw" cx="60" cy="60" r="42" fill="none" stroke="#00f0ff" stroke-width="1.8" stroke-dasharray="10 6 20 6" opacity="0.85"/>
        <!-- Cuadrante octagonal -->
        <polygon class="spin-cw" points="60,24 69,39 86,39 73,50 78,66 60,56 42,66 47,50 34,39 51,39" fill="none" stroke="#ff007f" stroke-width="1.2" opacity="0.7"/>
        <!-- Núcleo brillante ⚜ -->
        <g class="pulse-core">
            <circle cx="60" cy="60" r="16" fill="rgba(255,215,0,0.18)" stroke="#ffd700" stroke-width="2" filter="url(#glow)"/>
            <text x="60" y="66" font-size="18" font-family="'Spectral', serif" font-weight="bold" fill="#ffffff" text-anchor="middle">⚜</text>
        </g>
    </svg>
    </div>
    """

def generar_svg_hud(tipo: str, color_hex: str):
    """Genera visores interactivos en SVG animados para cada categoría en el carrusel."""
    if tipo == "vision":
        # Retícula óptica con barrido de radar y caja delimitadora
        return f"""
        <div style="background:rgba(8,12,24,0.92); border:1px solid {color_hex}55; border-radius:10px; padding:18px; text-align:center; box-shadow:0 10px 30px rgba(0,0,0,0.8);">
            <div style="font-family:'JetBrains Mono'; font-size:0.7rem; color:{color_hex}; letter-spacing:0.18em; margin-bottom:8px;">● CANAL ÓPTICO ACTIVO</div>
            <svg width="240" height="200" viewBox="0 0 240 200">
                <defs>
                    <linearGradient id="scanBeam" x1="0%" y1="0%" x2="0%" y2="100%">
                        <stop offset="0%" stop-color="{color_hex}" stop-opacity="0"/>
                        <stop offset="50%" stop-color="{color_hex}" stop-opacity="0.8"/>
                        <stop offset="100%" stop-color="{color_hex}" stop-opacity="0"/>
                    </linearGradient>
                </defs>
                <style>
                    .laser-sweep {{ animation: sweepY 2.8s ease-in-out infinite alternate; }}
                    .spin-reticle {{ transform-origin: 120px 100px; animation: spinRet 12s linear infinite; }}
                    .box-pulse {{ animation: boxBlink 1.8s ease-in-out infinite alternate; }}
                    @keyframes sweepY {{ 0% {{ y: 15; }} 100% {{ y: 175; }} }}
                    @keyframes spinRet {{ 0% {{ transform: rotate(0deg); }} 100% {{ transform: rotate(360deg); }} }}
                    @keyframes boxBlink {{ 0% {{ stroke-opacity: 0.4; }} 100% {{ stroke-opacity: 1; }} }}
                </style>
                <rect x="5" y="5" width="230" height="190" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1" rx="8"/>
                <circle class="spin-reticle" cx="120" cy="100" r="65" fill="none" stroke="{color_hex}" stroke-width="1.5" stroke-dasharray="12 8 6 8" opacity="0.6"/>
                <circle cx="120" cy="100" r="35" fill="none" stroke="#00f0ff" stroke-width="1.2" stroke-dasharray="6 4"/>
                <rect class="box-pulse" x="65" y="45" width="110" height="110" fill="none" stroke="{color_hex}" stroke-width="2"/>
                <!-- Esquinas del objetivo -->
                <path d="M 60 55 L 60 40 L 75 40" fill="none" stroke="{color_hex}" stroke-width="2.5"/>
                <path d="M 180 55 L 180 40 L 165 40" fill="none" stroke="{color_hex}" stroke-width="2.5"/>
                <path d="M 60 145 L 60 160 L 75 160" fill="none" stroke="{color_hex}" stroke-width="2.5"/>
                <path d="M 180 145 L 180 160 L 165 160" fill="none" stroke="{color_hex}" stroke-width="2.5"/>
                <!-- Haz de escaneo láser -->
                <rect class="laser-sweep" x="10" y="20" width="220" height="4" fill="url(#scanBeam)"/>
                <text x="120" y="105" font-family="'JetBrains Mono'" font-size="10" fill="#ffffff" text-anchor="middle">TRACKING [99.4%]</text>
            </svg>
        </div>
        """
    elif tipo == "audio":
        # Espectro de ondas y rizos sónicos
        return f"""
        <div style="background:rgba(8,12,24,0.92); border:1px solid {color_hex}55; border-radius:10px; padding:18px; text-align:center; box-shadow:0 10px 30px rgba(0,0,0,0.8);">
            <div style="font-family:'JetBrains Mono'; font-size:0.7rem; color:{color_hex}; letter-spacing:0.18em; margin-bottom:8px;">● ESPECTRO ACÚSTICO // HÁPTICO</div>
            <svg width="240" height="200" viewBox="0 0 240 200">
                <style>
                    .bar1 {{ animation: bounce 0.9s ease-in-out infinite alternate; }}
                    .bar2 {{ animation: bounce 0.7s ease-in-out infinite 0.2s alternate; }}
                    .bar3 {{ animation: bounce 1.1s ease-in-out infinite 0.4s alternate; }}
                    .bar4 {{ animation: bounce 0.8s ease-in-out infinite 0.1s alternate; }}
                    .bar5 {{ animation: bounce 1.0s ease-in-out infinite 0.3s alternate; }}
                    .wave-ripple {{ transform-origin: 120px 100px; animation: expandWave 2.2s ease-out infinite; }}
                    @keyframes bounce {{ 0% {{ transform: scaleY(0.3); }} 100% {{ transform: scaleY(1.3); }} }}
                    @keyframes expandWave {{ 0% {{ r: 20; opacity: 0.9; }} 100% {{ r: 85; opacity: 0; }} }}
                </style>
                <circle class="wave-ripple" cx="120" cy="100" r="20" fill="none" stroke="{color_hex}" stroke-width="1.8"/>
                <circle class="wave-ripple" cx="120" cy="100" r="20" fill="none" stroke="#00f0ff" stroke-width="1.5" style="animation-delay: 0.8s;"/>
                <!-- Barras de ecualizador -->
                <g transform="translate(60, 100)">
                    <rect class="bar1" x="0" y="-35" width="8" height="70" rx="4" fill="{color_hex}"/>
                    <rect class="bar2" x="18" y="-45" width="8" height="90" rx="4" fill="#00f0ff"/>
                    <rect class="bar3" x="36" y="-60" width="8" height="120" rx="4" fill="{color_hex}"/>
                    <rect class="bar4" x="54" y="-50" width="8" height="100" rx="4" fill="#ff007f"/>
                    <rect class="bar5" x="72" y="-40" width="8" height="80" rx="4" fill="{color_hex}"/>
                    <rect class="bar2" x="90" y="-55" width="8" height="110" rx="4" fill="#00ff88"/>
                    <rect class="bar1" x="108" y="-30" width="8" height="60" rx="4" fill="{color_hex}"/>
                </g>
                <text x="120" y="185" font-family="'JetBrains Mono'" font-size="10" fill="#cbd5e1" text-anchor="middle">587.33 Hz HARMONIC SYNC</text>
            </svg>
        </div>
        """
    elif tipo == "neural":
        # Red neuronal y engranajes cinemáticos CAD
        return f"""
        <div style="background:rgba(8,12,24,0.92); border:1px solid {color_hex}55; border-radius:10px; padding:18px; text-align:center; box-shadow:0 10px 30px rgba(0,0,0,0.8);">
            <div style="font-family:'JetBrains Mono'; font-size:0.7rem; color:{color_hex}; letter-spacing:0.18em; margin-bottom:8px;">● SINÁPSIS Y DEDUCCIÓN CAD</div>
            <svg width="240" height="200" viewBox="0 0 240 200">
                <style>
                    .syn-fire {{ animation: synPulse 1.6s ease-in-out infinite alternate; }}
                    .cad-spin {{ transform-origin: 120px 100px; animation: spinRet 16s linear infinite; }}
                    @keyframes synPulse {{ 0% {{ opacity: 0.3; stroke-width: 1; }} 100% {{ opacity: 1; stroke-width: 2.5; }} }}
                </style>
                <circle class="cad-spin" cx="120" cy="100" r="75" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="1.5" stroke-dasharray="14 10"/>
                <!-- Enlaces sinápticos -->
                <line class="syn-fire" x1="45" y1="50" x2="120" y2="70" stroke="{color_hex}"/>
                <line class="syn-fire" x1="45" y1="100" x2="120" y2="100" stroke="#00f0ff"/>
                <line class="syn-fire" x1="45" y1="150" x2="120" y2="130" stroke="{color_hex}"/>
                <line class="syn-fire" x1="120" y1="70" x2="195" y2="100" stroke="#ff007f"/>
                <line class="syn-fire" x1="120" y1="130" x2="195" y2="100" stroke="{color_hex}"/>
                <!-- Nodos -->
                <circle cx="45" cy="50" r="9" fill="#020306" stroke="{color_hex}" stroke-width="2"/>
                <circle cx="45" cy="100" r="9" fill="#020306" stroke="{color_hex}" stroke-width="2"/>
                <circle cx="45" cy="150" r="9" fill="#020306" stroke="{color_hex}" stroke-width="2"/>
                <circle cx="120" cy="70" r="11" fill="#020306" stroke="#00f0ff" stroke-width="2"/>
                <circle cx="120" cy="130" r="11" fill="#020306" stroke="#00f0ff" stroke-width="2"/>
                <circle cx="195" cy="100" r="13" fill="#020306" stroke="#ffd700" stroke-width="2.5"/>
                <text x="120" y="185" font-family="'JetBrains Mono'" font-size="10" fill="#cbd5e1" text-anchor="middle">EQUILIBRIO TENSOR V2.4</text>
            </svg>
        </div>
        """
    elif tipo == "text":
        # Matriz semántica y flujo de datos
        return f"""
        <div style="background:rgba(8,12,24,0.92); border:1px solid {color_hex}55; border-radius:10px; padding:18px; text-align:center; box-shadow:0 10px 30px rgba(0,0,0,0.8);">
            <div style="font-family:'JetBrains Mono'; font-size:0.7rem; color:{color_hex}; letter-spacing:0.18em; margin-bottom:8px;">● MOTOR LÉXICO // RAG SEMÁNTICO</div>
            <svg width="240" height="200" viewBox="0 0 240 200">
                <style>
                    .data-flow {{ stroke-dasharray: 8 6; animation: flowDash 3s linear infinite; }}
                    .pulse-node {{ animation: nodeBlink 1.4s ease-in-out infinite alternate; }}
                    @keyframes flowDash {{ 0% {{ stroke-dashoffset: 0; }} 100% {{ stroke-dashoffset: -50; }} }}
                    @keyframes nodeBlink {{ 0% {{ fill: #020306; }} 100% {{ fill: {color_hex}; }} }}
                </style>
                <path class="data-flow" d="M 20 50 Q 80 20, 120 70 T 220 50" fill="none" stroke="{color_hex}" stroke-width="2"/>
                <path class="data-flow" d="M 20 100 Q 80 140, 120 100 T 220 100" fill="none" stroke="#00f0ff" stroke-width="2"/>
                <path class="data-flow" d="M 20 150 Q 80 120, 120 140 T 220 150" fill="none" stroke="#ff007f" stroke-width="2"/>
                <circle class="pulse-node" cx="60" cy="40" r="7" stroke="{color_hex}" stroke-width="2"/>
                <circle class="pulse-node" cx="120" cy="100" r="9" stroke="#00f0ff" stroke-width="2"/>
                <circle class="pulse-node" cx="180" cy="145" r="7" stroke="#ff007f" stroke-width="2"/>
                <text x="120" y="185" font-family="'JetBrains Mono'" font-size="10" fill="#cbd5e1" text-anchor="middle">FAISS VECTOR MATCH [100%]</text>
            </svg>
        </div>
        """
    else:
        # Creativo / Prisma de Fantasía
        return f"""
        <div style="background:rgba(8,12,24,0.92); border:1px solid {color_hex}55; border-radius:10px; padding:18px; text-align:center; box-shadow:0 10px 30px rgba(0,0,0,0.8);">
            <div style="font-family:'JetBrains Mono'; font-size:0.7rem; color:{color_hex}; letter-spacing:0.18em; margin-bottom:8px;">● PRISMA CREATIVO & NARRATIVO</div>
            <svg width="240" height="200" viewBox="0 0 240 200">
                <style>
                    .prism-spin {{ transform-origin: 120px 95px; animation: spinRet 14s linear infinite; }}
                    .twinkle {{ animation: starGlow 1.5s ease-in-out infinite alternate; }}
                    @keyframes starGlow {{ 0% {{ opacity: 0.3; transform: scale(0.8); }} 100% {{ opacity: 1; transform: scale(1.2); }} }}
                </style>
                <polygon class="prism-spin" points="120,35 170,125 70,125" fill="rgba(255,0,127,0.15)" stroke="{color_hex}" stroke-width="2"/>
                <circle class="prism-spin" cx="120" cy="95" r="30" fill="none" stroke="#00f0ff" stroke-width="1.5" stroke-dasharray="8 6"/>
                <circle class="twinkle" cx="45" cy="45" r="3.5" fill="#ffd700"/>
                <circle class="twinkle" cx="195" cy="55" r="4" fill="#00ff88"/>
                <circle class="twinkle" cx="185" cy="155" r="3.5" fill="#ff007f"/>
                <circle class="twinkle" cx="55" cy="145" r="4.5" fill="#00f0ff"/>
                <text x="120" y="175" font-family="'JetBrains Mono'" font-size="10" fill="#cbd5e1" text-anchor="middle">GENERADOR NARRATIVO ACTIVO</text>
            </svg>
        </div>
        """

# ============================================================
# CABECERA MAESTRA CON EMBLEMA SVG ANIMADO
# ============================================================
render_clean_html(generar_svg_emblema())
render_clean_html('<div class="brand-signature">Krov Industries · Plataforma de Aplicaciones</div>')
render_clean_html('<div class="main-title">Ecosistema de Inteligencia Artificial</div>')
render_clean_html('<div class="sub-lead">16 soluciones prácticas de visión por computador, modelos de lenguaje, procesamiento acústico y redes neuronales diseñadas para interactuar de forma natural.</div>')

# Métricas Globales
total_apps = len(CATALOGO)
visitadas_count = len(st.session_state.visited_apps)
progreso_pct = int((visitadas_count / total_apps) * 100)

s1, s2, s3, s4 = st.columns(4)
with s1:
    render_clean_html(f'<div class="stat-pill"><div style="font-size:0.7rem; color:#94a3b8; font-family:\'JetBrains Mono\';">TOTAL APLICACIONES</div><div style="font-size:1.8rem; font-weight:700; color:#ffffff;">{total_apps}</div></div>')
with s2:
    render_clean_html(f'<div class="stat-pill"><div style="font-size:0.7rem; color:#94a3b8; font-family:\'JetBrains Mono\';">EXPLORADAS</div><div style="font-size:1.8rem; font-weight:700; color:#00ff88;">{visitadas_count} de {total_apps}</div></div>')
with s3:
    render_clean_html(f'<div class="stat-pill"><div style="font-size:0.7rem; color:#94a3b8; font-family:\'JetBrains Mono\';">PROGRESO</div><div style="font-size:1.8rem; font-weight:700; color:#ffd700;">{progreso_pct}%</div></div>')
with s4:
    categorias_unicas = len(set(a["cat"] for a in CATALOGO))
    render_clean_html(f'<div class="stat-pill"><div style="font-size:0.7rem; color:#94a3b8; font-family:\'JetBrains Mono\';">DOMINIOS TÉCNICOS</div><div style="font-size:1.8rem; font-weight:700; color:#00f0ff;">{categorias_unicas}</div></div>')

st.write("")

# Barra de progreso líquida
render_clean_html(f"""
<div class="lava-progress-frame">
    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono'; font-size:0.74rem; margin-bottom:6px; padding:0 4px;">
        <span style="color:#94a3b8;">AUDITORÍA DE REVISIÓN</span>
        <span style="color:#ffd700; font-weight:700;">{visitadas_count} de {total_apps} aplicaciones verificadas ({progreso_pct}%)</span>
    </div>
    <div class="lava-progress-bar">
        <div class="lava-progress-fill" style="width: {max(5, progreso_pct)}%;"></div>
    </div>
</div>
""")

# ============================================================
# FILTROS Y BÚSQUEDA
# ============================================================
c_search, c_filter = st.columns([1.6, 1], gap="medium")
with c_search:
    termino_busqueda = st.text_input(
        "Buscar por función, palabra clave o tecnología:",
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

# ============================================================
# CARRUSEL CON DESCRIPCIÓN Y HUD SVG ANIMADO
# ============================================================
badge_visita_html = '<span class="visited-badge">✓ Explorada</span>' if esta_visitada else '<span style="font-family:\'JetBrains Mono\'; font-size:0.72rem; color:#94a3b8; background:rgba(255,255,255,0.08); padding:4px 10px; border-radius:6px;">○ Pendiente</span>'

col_desc, col_hud = st.columns([1.5, 0.9], gap="medium")

with col_desc:
    html_card = f"""
    <div class="carousel-card">
        <div class="card-top-row">
            <div>
                <span class="cat-badge" style="background:{app_actual['color']}22; border:1px solid {app_actual['color']}66; color:{app_actual['color']};">
                    {app_actual['icon']} {app_actual['cat']}
                </span>
                <span style="font-family:'JetBrains Mono'; font-size:0.75rem; color:#94a3b8; margin-left:8px;">
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
# DIRECTORIO GENERAL COMPLETO (16 APLICACIONES)
# ============================================================
st.markdown("### Directorio de Acceso Rápido")
st.markdown("<p style='color:#94a3b8; font-size:0.9rem; margin-top:-8px;'>Haz clic en cualquier aplicación para seleccionarla en el carrusel superior o pulsa su botón de enlace directo para lanzarla en una nueva pestaña.</p>", unsafe_allow_html=True)

cols_grid = st.columns(4)
for i, item in enumerate(CATALOGO):
    col = cols_grid[i % 4]
    item_visitado = item["id"] in st.session_state.visited_apps
    simbolo_visita = "✓" if item_visitado else "○"
    color_visita = "#00ff88" if item_visitado else "#94a3b8"

    with col:
        with st.container(border=True):
            card_grid_html = f"""
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                <span style="font-size:1.25rem;">{item['icon']}</span>
                <span style="font-family:'JetBrains Mono'; font-size:0.7rem; color:{color_visita}; font-weight:700;">{simbolo_visita} #{item['id']:02d}</span>
            </div>
            <div style="font-weight:700; font-size:0.95rem; color:#ffffff; min-height:44px; line-height:1.25;">{item['titulo']}</div>
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{item['color']}; margin:4px 0 8px 0; text-transform:uppercase;">{item['cat']}</div>
            <p style="font-size:0.8rem; color:#94a3b8; line-height:1.4; min-height:48px;">{item['proposito'][:78]}...</p>
            """
            render_clean_html(card_grid_html)

            c_btn1, c_btn2 = st.columns([1, 1])
            with c_btn1:
                if st.button("Detalle", key=f"sel_app_{item['id']}", use_container_width=True):
                    if item in filtradas:
                        st.session_state.carousel_idx = filtradas.index(item)
                    else:
                        st.session_state.carousel_idx = CATALOGO.index(item)
                    st.rerun()
            with c_btn2:
                st.link_button("Abrir ↗", item["url"], use_container_width=True)

# Pie de página
st.write("")
render_clean_html("""
<div style="text-align:center; padding:2rem 0; border-top:1px solid rgba(255,255,255,0.08); margin-top:2rem;">
    <div style="font-family:'JetBrains Mono'; font-size:0.75rem; letter-spacing:0.2em; color:#ffd700; text-transform:uppercase;">
        KROV INDUSTRIES · DIVISION OF ARTIFICIAL INTELLIGENCE & CYBERNETICS
    </div>
    <div style="font-size:0.82rem; color:#64748b; margin-top:6px;">
        16 Aplicaciones Multimodales en Línea sobre Streamlit Cloud
    </div>
</div>
""")
