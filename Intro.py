import streamlit as st
import streamlit.components.v1 as components

# ============================================================
# CONFIGURACIÓN GENERAL DEL PORTAFOLIO
# ============================================================
st.set_page_config(
    page_title="Krov Industries // Portafolio de Inteligencia Artificial",
    page_icon="⚜",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# ESTADO DE NAVEGACIÓN Y SEGUIMIENTO EN SESIÓN
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
        "titulo": "Detector de Objetos en Tiempo Real",
        "cat": "Visión Artificial",
        "url": "https://yolozz.streamlit.app",
        "icon": "🎯",
        "proposito": "Identifica, localiza con cajas delimitadoras y cuantifica hasta 80 tipos de objetos en vivo o por fotos.",
        "codigo": "Modelo ultraliviano PyTorch YOLOv5 (yolov5su) con inferencia en microsegundos, filtrado IoU y aviso acústico en AudioContext.",
        "uso": "Inventarios de almacenes en segundos, monitoreo de aforo en locales y asistencia visual en movilidad.",
        "badge_color": "#ffd700"
    },
    {
        "id": 2,
        "titulo": "Generador de Nube de Palabras",
        "cat": "Texto y Semántica",
        "url": "https://wordcloudz.streamlit.app",
        "icon": "☁️",
        "proposito": "Condensa textos densos en una imagen donde el tamaño de cada palabra refleja su relevancia real.",
        "codigo": "Limpieza léxica con Regex y Counter en Python, exclusión de conectores (stopwords) en español/inglés y renderizado en WordCloud con siluetas.",
        "uso": "Auditoría de comentarios de usuarios, síntesis de artículos largos y análisis de encuestas abiertas.",
        "badge_color": "#38bdf8"
    },
    {
        "id": 3,
        "titulo": "Reconocedor de Dígitos Ópticos",
        "cat": "Redes Neuronales",
        "url": "https://mnistz.streamlit.app",
        "icon": "✍️",
        "proposito": "Clasifica con precisión matemática cualquier número del 0 al 9 dibujado a mano alzada.",
        "codigo": "Lienzo táctil Canvas, recorte automático centrado con Pillow (28x28 Lanczos) y clasificación probabilística con redes CNN en Keras/TensorFlow.",
        "uso": "Digitalización de formularios censales, lectura de cheques bancarios y validación de códigos postales.",
        "badge_color": "#a855f7"
    },
    {
        "id": 4,
        "titulo": "Análisis Contextual de Imagen",
        "cat": "Visión Multimodal",
        "url": "https://visionz.streamlit.app",
        "icon": "👁️",
        "proposito": "Describe cualquier imagen con una narrativa profunda, respondiendo preguntas específicas sobre el contexto.",
        "codigo": "Codificación segura Base64 e integración en streaming de tokens con el modelo multimodal GPT-4o de OpenAI.",
        "uso": "Peritajes de aseguradoras para evaluar daños de autos, inspección de obras civiles y accesibilidad visual.",
        "badge_color": "#00f0ff"
    },
    {
        "id": 5,
        "titulo": "Traductor de Voz a Audio",
        "cat": "Voz y Acústica",
        "url": "https://traductorz.streamlit.app",
        "icon": "🎙️",
        "proposito": "Escucha lo que dices por el micrófono, lo traduce de inmediato y lo pronuncia en otro idioma con acento natural.",
        "codigo": "Captura continua con la API Web Speech mediante puentes Bokeh, traducción multilingüe con Google Translate y síntesis gTTS.",
        "uso": "Conversaciones cara a cara entre personas de distintos idiomas, atención a turistas y aprendizaje de pronunciación.",
        "badge_color": "#ec4899"
    },
    {
        "id": 6,
        "titulo": "Detector de Presencia y Postura",
        "cat": "Visión Artificial",
        "url": "https://teachablez.streamlit.app",
        "icon": "🛡️",
        "proposito": "Verifica si hay una persona frente a la pantalla y analiza su postura física sin enviar imágenes a internet.",
        "codigo": "Ejecución 100% en el navegador con TensorFlow.js y PoseNet, validación geométrica de rasgos faciales y esqueleto articular.",
        "uso": "Corrección ergonómica en oficinas, control de aforo en salas privadas y activación de quioscos interactivos.",
        "badge_color": "#00ff88"
    },
    {
        "id": 7,
        "titulo": "Espacio de Humor y Bienestar",
        "cat": "Interacción Lúdica",
        "url": "https://bendover.streamlit.app",
        "icon": "🐇",
        "proposito": "Despeja la mente en jornadas intensas con efectos interactivos y chistes narrados con voz propia.",
        "codigo": "Motor físico de partículas y fuegos artificiales en Canvas, cursor animado sensible a la velocidad y síntesis de voz Web Speech.",
        "uso": "Pausas activas en empresas de desarrollo, descanso visual y reducción de la fatiga laboral.",
        "badge_color": "#fb923c"
    },
    {
        "id": 8,
        "titulo": "Compañero de Conversación Empático",
        "cat": "Interacción Humana",
        "url": "https://sentimentz.streamlit.app",
        "icon": "🤖",
        "proposito": "Escucha tus pensamientos y te ofrece orientación calmada, reflexiva y con voz amigable.",
        "codigo": "Clasificador semántico de emociones, avatar robótico sincronizado por estados en Lottie y síntesis de voz en español e inglés.",
        "uso": "Bitácora personal de desahogo, apoyo en momentos de estrés y clarificación mental antes de tomar decisiones.",
        "badge_color": "#c084fc"
    },
    {
        "id": 9,
        "titulo": "Espejo Mágico de Lectura",
        "cat": "Óptica y Traducción",
        "url": "https://ocryaudioz.streamlit.app",
        "icon": "🪞",
        "proposito": "Lee textos de fotos o carteles y los proyecta en un visor 3D con traducción y lectura en voz alta.",
        "codigo": "Realce de bordes con filtros bilaterales y CLAHE en OpenCV, extracción de texto con Tesseract OCR y renderizado con perspectiva 3D.",
        "uso": "Traducción de menús y letreros en viajes internacionales y asistencia a personas con problemas de lectura.",
        "badge_color": "#f43f5e"
    },
    {
        "id": 10,
        "titulo": "Reconocimiento Óptico por Cámara",
        "cat": "Óptica y Documentos",
        "url": "https://lectorz.streamlit.app",
        "icon": "📷",
        "proposito": "Usa la cámara web como un escáner que convierte papel o pantallas en texto editable al instante.",
        "codigo": "Interpolación bicúbica 2x para nitidez tipográfica, inversión automática de pantallas oscuras y doble pasada Tesseract PSM 3/6.",
        "uso": "Extracción de párrafos de libros de biblioteca, archivo de recibos de compra y notas de pizarra.",
        "badge_color": "#e11d48"
    },
    {
        "id": 11,
        "titulo": "Interfaces Multimodales Sensoriales",
        "cat": "Sistemas Sensoriales",
        "url": "https://sussusamogus.streamlit.app",
        "icon": "✦",
        "proposito": "Laboratorio de diseño que demuestra interacción simultánea por vista, oído y tacto real.",
        "codigo": "Generación procedural de ondas de sonido con struct/wave, vibración física con la API Navigator del navegador y pulsos ópticos en pantalla.",
        "uso": "Diseño de alertas críticas en vehículos modernos, periféricos de videojuegos y software accesible para discapacidad motriz.",
        "badge_color": "#c5a059"
    },
    {
        "id": 12,
        "titulo": "Tablero de Bocetos Creativos",
        "cat": "Visión Creativa",
        "url": "https://drawrecogz.streamlit.app",
        "icon": "🎨",
        "proposito": "Dibuja lo que quieras sobre un lienzo digital y recibe una interpretación crítica de tu arte.",
        "codigo": "Pizarra vectorial de dibujo con figuras geométricas, normalización matricial sobre fondo blanco y análisis visual con GPT-4o-mini.",
        "uso": "Lluvia de ideas en agencias de diseño, conceptualización inicial de wireframes y entrenamiento artístico.",
        "badge_color": "#ff007f"
    },
    {
        "id": 13,
        "titulo": "Asesor de Documentos PDF (RAG)",
        "cat": "Texto y Documentos",
        "url": "https://chatpdfz.streamlit.app",
        "icon": "💬",
        "proposito": "Sube cualquier archivo PDF y hazle preguntas para que responda con la información exacta del documento.",
        "codigo": "Indexación semántica RAG con PyPDF2, generación de embeddings de OpenAI, almacenamiento vectorial en memoria con FAISS y síntesis precisa.",
        "uso": "Consulta veloz de contratos legales extensos, manuales de equipos técnicos y guías de estudio universitario.",
        "badge_color": "#0ea5e9"
    },
    {
        "id": 14,
        "titulo": "Analizador Tonal y Emocional",
        "cat": "Texto y Semántica",
        "url": "https://textanalysiz.streamlit.app",
        "icon": "⚖️",
        "proposito": "Examina si un mensaje es positivo, tenso, formal o muy subjetivo antes de que lo envíes.",
        "codigo": "Motor semántico en español con reglas léxicas para intensificadores y negaciones, trazado de curva emocional con Plotly y medidores SVG.",
        "uso": "Revisión de correos corporativos delicados, ajuste de comunicados de prensa y moderación de servicio al cliente.",
        "badge_color": "#ffd700"
    },
    {
        "id": 15,
        "titulo": "Deductor de Sistemas Físicos",
        "cat": "Redes y Física",
        "url": "https://histinfz.streamlit.app",
        "icon": "⚡",
        "proposito": "Dibuja un esquema de ingeniería o poleas y obtén las ecuaciones y leyes mecánicas que lo rigen.",
        "codigo": "Plano digital estilo CAD en Canvas, extracción de relaciones de acoplamiento y formulación física estructurada con GPT-4o-mini.",
        "uso": "Resolución de ejercicios de física para estudiantes de ingeniería, verificación de prototipos mecánicos y diseño conceptual.",
        "badge_color": "#00f6ff"
    },
    {
        "id": 16,
        "titulo": "Taller de Cuentos Ilustrados",
        "cat": "Visión Creativa",
        "url": "https://ejemplohistinfz.streamlit.app",
        "icon": "📖",
        "proposito": "Dibuja un personaje o garabato y la inteligencia artificial creará un cuento infantil original a partir de él.",
        "codigo": "Recepción de trazos en lienzo lúdico, compresión visual e inferencia narrativa con GPT-4o-mini para redactar historias infantiles con valores.",
        "uso": "Actividades de lectoescritura en colegios, estímulo de la imaginación en niños y creación de cuentos para dormir en familia.",
        "badge_color": "#06d6a0"
    }
]

# ============================================================
# ESTILOS VISUALES: OBSIDIANA, ORO LÍQUIDO, NEÓN Y VIDRIO
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,400;0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');

html, body, [data-testid="stAppViewContainer"], .stApp {
    background: transparent !important;
    background-color: transparent !important;
    color: #f1f5f9 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    overflow-x: hidden;
}

body {
    background-color: #030407 !important;
}

[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stSidebar"], section[data-testid="stSidebar"] { display: none !important; }

/* Contenedor principal con respiración simétrica */
.block-container {
    max-width: 1200px !important;
    padding-top: 1.5rem !important;
    padding-bottom: 4rem !important;
    margin: 0 auto !important;
    position: relative;
    z-index: 10;
}

.brand-signature {
    text-align: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.76rem;
    letter-spacing: 0.3em;
    color: #d4af37;
    text-transform: uppercase;
    margin-bottom: 4px;
    text-shadow: 0 0 14px rgba(212, 175, 55, 0.4);
}

.main-title {
    font-family: 'Spectral', Georgia, serif;
    font-size: clamp(2.2rem, 4.5vw, 3.4rem);
    font-weight: 700;
    text-align: center;
    color: #ffffff;
    line-height: 1.1;
    margin-bottom: 0.3rem;
    text-shadow: 0 0 35px rgba(212, 175, 55, 0.35), 0 0 70px rgba(0, 240, 255, 0.2);
}

.sub-lead {
    text-align: center;
    color: #94a3b8;
    font-size: 1rem;
    max-width: 780px;
    margin: 0 auto 1.6rem auto;
    line-height: 1.6;
}

/* Barra de progreso de flujo líquido */
.lava-progress-frame {
    background: rgba(15, 20, 32, 0.85);
    border: 1px solid rgba(212, 175, 55, 0.25);
    border-radius: 30px;
    padding: 6px 12px;
    margin-bottom: 1.6rem;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.8), inset 0 1px 0 rgba(255, 255, 255, 0.1);
}

.lava-progress-bar {
    width: 100%;
    height: 12px;
    background: rgba(255, 255, 255, 0.06);
    border-radius: 10px;
    overflow: hidden;
    position: relative;
}

.lava-progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #d4af37, #f59e0b, #00f0ff, #a855f7, #ffd700);
    background-size: 300% 100%;
    animation: lavaFlow 4s linear infinite;
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(212, 175, 55, 0.9);
    transition: width 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes lavaFlow {
    0% { background-position: 0% 50%; }
    100% { background-position: 300% 50%; }
}

/* Tarjeta principal del carrusel con perspectiva 3D */
.carousel-card {
    background: linear-gradient(145deg, rgba(16, 20, 34, 0.92) 0%, rgba(8, 10, 18, 0.98) 100%);
    border: 1px solid rgba(212, 175, 55, 0.35);
    border-top: 3px solid #d4af37;
    border-radius: 14px;
    padding: 26px 32px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8), 0 0 30px rgba(212, 175, 55, 0.15);
    backdrop-filter: blur(18px);
    transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
    margin-bottom: 1.2rem;
    position: relative;
    overflow: hidden;
}

.carousel-card:hover {
    transform: translateY(-3px);
    border-color: #ffd700;
    box-shadow: 0 25px 70px rgba(0, 0, 0, 0.9), 0 0 45px rgba(212, 175, 55, 0.3);
}

.card-top-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 14px;
    flex-wrap: wrap;
    gap: 8px;
}

.cat-badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.14em;
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
    border: 1px solid rgba(0, 255, 136, 0.35);
    border-radius: 6px;
    padding: 4px 10px;
    display: inline-block;
}

.card-title {
    font-family: 'Spectral', Georgia, serif;
    font-size: clamp(1.6rem, 3vw, 2.2rem);
    font-weight: 700;
    color: #ffffff;
    line-height: 1.2;
    margin-bottom: 14px;
    text-shadow: 0 0 20px rgba(255, 255, 255, 0.15);
}

.section-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #d4af37;
    margin-bottom: 4px;
    font-weight: 700;
}

.section-text {
    font-size: 0.98rem;
    line-height: 1.65;
    color: #e2e8f0;
    margin-bottom: 14px;
}

.code-box {
    background: rgba(0, 0, 0, 0.45);
    border-left: 3px solid #00f0ff;
    border-radius: 6px;
    padding: 12px 16px;
    font-size: 0.92rem;
    color: #cbd5e1;
    line-height: 1.6;
    margin-bottom: 14px;
}

.use-box {
    background: rgba(212, 175, 55, 0.08);
    border-left: 3px solid #ffd700;
    border-radius: 6px;
    padding: 12px 16px;
    font-size: 0.92rem;
    color: #f1f5f9;
    line-height: 1.6;
}

/* Botones de navegación y acción */
div.stButton > button {
    border-radius: 8px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.86rem !important;
    font-weight: 600 !important;
    background: rgba(18, 22, 38, 0.88) !important;
    color: #f1f5f9 !important;
    border: 1px solid rgba(212, 175, 55, 0.35) !important;
    padding: 0.75rem 1.4rem !important;
    transition: all 0.25s ease !important;
}

div.stButton > button:hover {
    transform: translateY(-2px) !important;
    border-color: #ffd700 !important;
    color: #ffd700 !important;
    box-shadow: 0 0 25px rgba(212, 175, 55, 0.5) !important;
}

/* Botón de enlace principal para abrir la app */
div[data-testid="stLinkButton"] > a {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: 100% !important;
    background: linear-gradient(135deg, #ffd700 0%, #f59e0b 50%, #00f0ff 100%) !important;
    color: #05060a !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 700 !important;
    font-size: 0.92rem !important;
    letter-spacing: 0.04em !important;
    border-radius: 8px !important;
    padding: 0.75rem 1.4rem !important;
    text-decoration: none !important;
    box-shadow: 0 0 25px rgba(212, 175, 55, 0.5) !important;
    transition: all 0.25s ease !important;
}

div[data-testid="stLinkButton"] > a:hover {
    transform: translateY(-2px) scale(1.02) !important;
    box-shadow: 0 0 40px rgba(0, 240, 255, 0.8) !important;
    color: #000000 !important;
}

/* Tarjetas pequeñas de la cuadrícula interactiva */
.grid-card {
    background: rgba(12, 15, 26, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 8px;
    padding: 14px;
    text-align: left;
    transition: all 0.25s ease;
    cursor: pointer;
    margin-bottom: 12px;
}

.grid-card:hover {
    transform: translateY(-3px);
    border-color: #ffd700;
    box-shadow: 0 8px 25px rgba(212, 175, 55, 0.25);
}

.stat-pill {
    background: rgba(14, 18, 30, 0.85);
    border: 1px solid rgba(212, 175, 55, 0.2);
    border-radius: 8px;
    padding: 14px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# FONDO PROCEDURAL LÍQUIDO ORO Y NEÓN EN CANVAS GPU (CERO LAG)
# ============================================================
components.html(
    """
    <script>
    (function() {
        const pWin = window.parent;
        const pDoc = pWin.document;
        if (pWin.__KROV_MASTER_PORTFOLIO__) return;
        pWin.__KROV_MASTER_PORTFOLIO__ = true;

        let canvas = pDoc.getElementById('krov-portfolio-canvas');
        if (!canvas) {
            canvas = pDoc.createElement('canvas');
            canvas.id = 'krov-portfolio-canvas';
            canvas.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:0;background:#030407;';
            pDoc.body.prepend(canvas);
        }

        const ctx = canvas.getContext('2d');
        let w = canvas.width = pWin.innerWidth;
        let h = canvas.height = pWin.innerHeight;

        pWin.addEventListener('resize', () => {
            w = canvas.width = pWin.innerWidth;
            h = canvas.height = pWin.innerHeight;
        });

        // Orbes fluidos en órbita continua
        const orbs = [
            { x: w * 0.15, y: h * 0.2, r: 320, vx: 0.45, vy: 0.35, color: 'rgba(212, 175, 55, 0.14)' },
            { x: w * 0.85, y: h * 0.3, r: 350, vx: -0.35, vy: 0.4, color: 'rgba(0, 240, 255, 0.12)' },
            { x: w * 0.5, y: h * 0.8, r: 300, vx: 0.4, vy: -0.4, color: 'rgba(168, 85, 247, 0.11)' },
            { x: w * 0.2, y: h * 0.75, r: 280, vx: -0.3, vy: -0.35, color: 'rgba(255, 0, 127, 0.08)' }
        ];

        // Partículas estelares reactivas
        const stars = [];
        for (let i = 0; i < 55; i++) {
            stars.push({
                x: Math.random() * w,
                y: Math.random() * h,
                r: Math.random() * 1.8 + 0.6,
                vx: (Math.random() - 0.5) * 0.3,
                vy: (Math.random() - 0.5) * 0.3,
                alpha: Math.random() * 0.6 + 0.2
            });
        }

        function loop() {
            ctx.clearRect(0, 0, w, h);
            ctx.fillStyle = '#030407';
            ctx.fillRect(0, 0, w, h);

            // 1. Dibujar orbes de luz líquida
            ctx.globalCompositeOperation = 'screen';
            for (let b of orbs) {
                b.x += b.vx;
                b.y += b.vy;
                if (b.x < -120 || b.x > w + 120) b.vx *= -1;
                if (b.y < -120 || b.y > h + 120) b.vy *= -1;

                const g = ctx.createRadialGradient(b.x, b.y, 10, b.x, b.y, b.r);
                g.addColorStop(0, b.color);
                g.addColorStop(1, 'transparent');
                ctx.beginPath();
                ctx.arc(b.x, b.y, b.r, 0, Math.PI * 2);
                ctx.fillStyle = g;
                ctx.fill();
            }

            // 2. Dibujar partículas de brillo estelar
            ctx.globalCompositeOperation = 'lighter';
            for (let s of stars) {
                s.x += s.vx;
                s.y += s.vy;
                if (s.x < 0) s.x = w;
                if (s.x > w) s.x = 0;
                if (s.y < 0) s.y = h;
                if (s.y > h) s.y = 0;

                ctx.beginPath();
                ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
                ctx.fillStyle = `rgba(212, 175, 55, ${s.alpha})`;
                ctx.shadowBlur = 6;
                ctx.shadowColor = '#ffd700';
                ctx.fill();
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
# CABECERA Y MÉTRICAS GLOBALES
# ============================================================
st.markdown('<div class="brand-signature">Krov Industries · Plataforma de Aplicaciones</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">Ecosistema de Inteligencia Artificial</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-lead">16 soluciones prácticas de visión artificial, modelos de lenguaje, procesamiento acústico y redes neuronales diseñadas para interactuar de forma natural.</div>', unsafe_allow_html=True)

# Métricas rápidas
total_apps = len(CATALOGO)
visitadas_count = len(st.session_state.visited_apps)
progreso_pct = int((visitadas_count / total_apps) * 100)

s1, s2, s3, s4 = st.columns(4)
with s1:
    st.markdown(f'<div class="stat-pill"><div style="font-size:0.7rem; color:#94a3b8; font-family:\'JetBrains Mono\';">TOTAL APLICACIONES</div><div style="font-size:1.8rem; font-weight:700; color:#ffffff;">{total_apps}</div></div>', unsafe_allow_html=True)
with s2:
    st.markdown(f'<div class="stat-pill"><div style="font-size:0.7rem; color:#94a3b8; font-family:\'JetBrains Mono\';">EXPLORADAS</div><div style="font-size:1.8rem; font-weight:700; color:#00ff88;">{visitadas_count} de {total_apps}</div></div>', unsafe_allow_html=True)
with s3:
    st.markdown(f'<div class="stat-pill"><div style="font-size:0.7rem; color:#94a3b8; font-family:\'JetBrains Mono\';">PROGRESO</div><div style="font-size:1.8rem; font-weight:700; color:#ffd700;">{progreso_pct}%</div></div>', unsafe_allow_html=True)
with s4:
    categorias_unicas = len(set(a["cat"] for a in CATALOGO))
    st.markdown(f'<div class="stat-pill"><div style="font-size:0.7rem; color:#94a3b8; font-family:\'JetBrains Mono\';">DOMINIOS TÉCNICOS</div><div style="font-size:1.8rem; font-weight:700; color:#00f0ff;">{categorias_unicas}</div></div>', unsafe_allow_html=True)

st.write("")

# Barra de progreso líquida
st.markdown(
    f"""
    <div class="lava-progress-frame">
        <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono'; font-size:0.74rem; margin-bottom:6px; padding:0 4px;">
            <span style="color:#94a3b8;">SEGUIMIENTO DE AUDITORÍA</span>
            <span style="color:#ffd700; font-weight:700;">{visitadas_count} / {total_apps} aplicaciones verificadas ({progreso_pct}%)</span>
        </div>
        <div class="lava-progress-bar">
            <div class="lava-progress-fill" style="width: {max(4, progreso_pct)}%;"></div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# FILTRADO Y BÚSQUEDA EN TIEMPO REAL
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

# Lista filtrada
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
    st.info("No se encontraron aplicaciones con ese criterio. Restableciendo listado...")
    filtradas = CATALOGO

st.session_state.carousel_idx = max(0, min(st.session_state.carousel_idx, len(filtradas) - 1))
app_actual = filtradas[st.session_state.carousel_idx]
esta_visitada = app_actual["id"] in st.session_state.visited_apps

# ============================================================
# CARRUSEL INTERACTIVO PRINCIPAL
# ============================================================
badge_visita_html = '<span class="visited-badge">✓ Explorada</span>' if esta_visitada else '<span style="font-family:\'JetBrains Mono\'; font-size:0.72rem; color:#94a3b8; background:rgba(255,255,255,0.06); padding:4px 10px; border-radius:6px;">○ Pendiente</span>'

st.markdown(
    f"""
    <div class="carousel-card">
        <div class="card-top-row">
            <div>
                <span class="cat-badge" style="background:{app_actual['badge_color']}18; border:1px solid {app_actual['badge_color']}55; color:{app_actual['badge_color']};">
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
    """,
    unsafe_allow_html=True
)

# Fila de control del carrusel: Navegación + Lanzador en vivo
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
# CUADRÍCULA COMPLETA DE NAVEGACIÓN DIRECTA (16 APLICACIONES)
# ============================================================
st.markdown("### Directorio General de Acceso Inmediato")
st.markdown("<p style='color:#94a3b8; font-size:0.9rem; margin-top:-8px;'>Haz clic en cualquier aplicación para examinarla en el visor principal o pulsa su enlace para abrirla directamente en una nueva pestaña.</p>", unsafe_allow_html=True)

cols_grid = st.columns(4)
for i, item in enumerate(CATALOGO):
    col = cols_grid[i % 4]
    item_visitado = item["id"] in st.session_state.visited_apps
    simbolo_visita = "✓" if item_visitado else "○"
    color_visita = "#00ff88" if item_visitado else "#94a3b8"

    with col:
        with st.container(border=True):
            st.markdown(
                f"""
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                    <span style="font-size:1.25rem;">{item['icon']}</span>
                    <span style="font-family:'JetBrains Mono'; font-size:0.7rem; color:{color_visita}; font-weight:700;">{simbolo_visita} #{item['id']:02d}</span>
                </div>
                <div style="font-weight:700; font-size:0.95rem; color:#ffffff; min-height:44px; line-height:1.25;">{item['titulo']}</div>
                <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{item['badge_color']}; margin:4px 0 8px 0; text-transform:uppercase;">{item['cat']}</div>
                <p style="font-size:0.8rem; color:#94a3b8; line-height:1.4; min-height:48px;">{item['proposito'][:78]}...</p>
                """,
                unsafe_allow_html=True
            )
            c_btn1, c_btn2 = st.columns([1, 1])
            with c_btn1:
                if st.button("Ver detalle", key=f"sel_app_{item['id']}", use_container_width=True):
                    # Localiza el índice en el conjunto filtrado o restablece si no está
                    if item in filtradas:
                        st.session_state.carousel_idx = filtradas.index(item)
                    else:
                        st.session_state.carousel_idx = CATALOGO.index(item)
                    st.rerun()
            with c_btn2:
                st.link_button("Abrir ↗", item["url"], use_container_width=True)

# Pie de página Krov Industries
st.write("")
st.markdown(
    """
    <div style="text-align:center; padding:2rem 0; border-top:1px solid rgba(255,255,255,0.08); margin-top:2rem;">
        <div style="font-family:'JetBrains Mono'; font-size:0.75rem; letter-spacing:0.2em; color:#d4af37; text-transform:uppercase;">
            KROV INDUSTRIES · DIVISION OF ARTIFICIAL INTELLIGENCE & CYBERNETICS
        </div>
        <div style="font-size:0.82rem; color:#64748b; margin-top:6px;">
            Despliegue unificado de interfaces en Streamlit Cloud · Arquitecturas cliente-servidor híbridas
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
