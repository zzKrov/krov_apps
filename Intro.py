import streamlit as st
import streamlit.components.v1 as components

# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================
st.set_page_config(
    page_title="Portafolio de Aplicaciones // Sistemas e Interfaces",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

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
# CATÁLOGO DE APLICACIONES (LENGUAJE SOBRIO Y LACONICO)
# ============================================================
CATALOGO = [
    {
        "id": 1,
        "titulo": "Detector de Objetos en Vivo",
        "cat": "Visión Artificial",
        "url": "https://yolozz.streamlit.app",
        "icon": "🎯",
        "svg_type": "vision",
        "proposito": "Detección y conteo de objetos en tiempo real mediante cámara web o imágenes estáticas para 80 clases estándar.",
        "codigo": "Inferencia con modelo YOLOv5, filtrado de solapamiento mediante supresión de no máximos (NMS) y emisión de alertas auditivas.",
        "uso": "Control de aforo, gestión de inventarios y asistencia visual.",
        "color": "#38bdf8"
    },
    {
        "id": 2,
        "titulo": "Generador de Nube de Palabras",
        "cat": "Texto y Semántica",
        "url": "https://wordcloudz.streamlit.app",
        "icon": "☁️",
        "svg_type": "text",
        "proposito": "Representación visual de términos clave ponderados según su frecuencia relativa en textos extensos.",
        "codigo": "Limpieza léxica con expresiones regulares, supresión de palabras vacías (stop words) y composición gráfica con WordCloud.",
        "uso": "Análisis de encuestas, resumen de opiniones y exploración documental.",
        "color": "#60a5fa"
    },
    {
        "id": 3,
        "titulo": "Reconocedor de Dígitos Ópticos",
        "cat": "Redes Neuronales",
        "url": "https://mnistz.streamlit.app",
        "icon": "✍️",
        "svg_type": "neural",
        "proposito": "Lienzo de dibujo manual para clasificación de dígitos numéricos (0-9) con cálculo de certidumbre probabilística.",
        "codigo": "Normalización de imagen a 28×28 píxeles mediante Pillow y clasificación por red convolucional sobre dataset MNIST.",
        "uso": "Digitalización de formularios manuscritos y procesamiento de documentos bancarios.",
        "color": "#818cf8"
    },
    {
        "id": 4,
        "titulo": "Análisis Contextual de Imagen",
        "cat": "Visión Multimodal",
        "url": "https://visionz.streamlit.app",
        "icon": "👁️",
        "svg_type": "vision",
        "proposito": "Generación automática de descripciones contextuales y estructuradas a partir de imágenes cargadas.",
        "codigo": "Codificación en base64 y consulta por flujo continuo (streaming) a modelos de visión multimodal de OpenAI.",
        "uso": "Inspección técnica, documentación de daños y accesibilidad descriptiva.",
        "color": "#0284c7"
    },
    {
        "id": 5,
        "titulo": "Traductor de Voz a Audio",
        "cat": "Voz y Acústica",
        "url": "https://traductorz.streamlit.app",
        "icon": "🎙️",
        "svg_type": "audio",
        "proposito": "Recepción de voz por micrófono, traducción instantánea a idiomas seleccionados y reproducción sintetizada.",
        "codigo": "Captura con Web Speech API, traducción automática y síntesis auditiva parametrizada con gTTS.",
        "uso": "Atención multilingüe a usuarios y asistencia de pronunciación en idiomas extranjeros.",
        "color": "#a78bfa"
    },
    {
        "id": 6,
        "titulo": "Detector de Presencia y Postura",
        "cat": "Visión Artificial",
        "url": "https://teachablez.streamlit.app",
        "icon": "🛡️",
        "svg_type": "vision",
        "proposito": "Seguimiento corporal y evaluación postural en el cliente local sin transmisión de video a servidores externos.",
        "codigo": "Inferencia con TensorFlow.js y PoseNet sobre HTML5 Canvas, evaluando posiciones de articulaciones clave.",
        "uso": "Supervisión ergonómica frente a pantallas y quioscos interactivos sin contacto.",
        "color": "#2dd4bf"
    },
    {
        "id": 7,
        "titulo": "Espacio de Pausa y Bienestar",
        "cat": "Interacción Lúdica",
        "url": "https://bendover.streamlit.app",
        "icon": "🐇",
        "svg_type": "creative",
        "proposito": "Entorno interactivo con seguimiento del cursor mediante partículas visuales y síntesis de voz.",
        "codigo": "Simulación física de partículas en JavaScript sobre Canvas 2D y lectura vocal mediante SpeechSynthesis API.",
        "uso": "Pausas activas y reducción de la fatiga cognitiva durante sesiones prolongadas.",
        "color": "#6366f1"
    },
    {
        "id": 8,
        "titulo": "Asistente Conversacional Guiado",
        "cat": "Interacción Humana",
        "url": "https://sentimentz.streamlit.app",
        "icon": "🤖",
        "svg_type": "text",
        "proposito": "Interacción textual con análisis de polaridad afectiva y retroalimentación adaptativa.",
        "codigo": "Clasificación léxica de sentimiento, sincronización con animaciones Lottie y síntesis de voz multilingüe.",
        "uso": "Bitácoras guiadas, registro de ánimo y apoyo en redacción reflexiva.",
        "color": "#818cf8"
    },
    {
        "id": 9,
        "titulo": "Visor y Extractor de Texto en 3D",
        "cat": "Óptica y Traducción",
        "url": "https://ocryaudioz.streamlit.app",
        "icon": "🪞",
        "svg_type": "vision",
        "proposito": "Captura fotográfica de documentos con proyección de texto sobre superficie tridimensional, traducción y lectura.",
        "codigo": "Normalización de contraste con CLAHE en OpenCV, motor de extracción Tesseract OCR y renderizado interactivo.",
        "uso": "Lectura asistida de impresos y comprensión de señalética en lenguas extranjeras.",
        "color": "#38bdf8"
    },
    {
        "id": 10,
        "titulo": "Digitalizador Óptico por Cámara",
        "cat": "Óptica y Documentos",
        "url": "https://lectorz.streamlit.app",
        "icon": "📷",
        "svg_type": "vision",
        "proposito": "Conversión directa de capturas de cámara web en fragmentos de texto editables y exportables.",
        "codigo": "Interpolación bicúbica para realce tipográfico, binarización adaptable y análisis de caracteres.",
        "uso": "Transcripción ágil de fragmentos bibliográficos y registro de recibos impresos.",
        "color": "#0ea5e9"
    },
    {
        "id": 11,
        "titulo": "Interfaces Multisensoriales",
        "cat": "Sistemas Sensoriales",
        "url": "https://sussusamogus.streamlit.app",
        "icon": "✦",
        "svg_type": "audio",
        "proposito": "Demostración de señalización coordinada mediante estímulos ópticos, tonos sinusoidales y vibración háptica.",
        "codigo": "Generación matemática de tonos en memoria, integración de la Vibration API del navegador y pulsos CSS.",
        "uso": "Señalética accesible, cabinas de control y validación de notificaciones periféricas.",
        "color": "#4f46e5"
    },
    {
        "id": 12,
        "titulo": "Tablero de Bocetos y Evaluación",
        "cat": "Visión Creativa",
        "url": "https://drawrecogz.streamlit.app",
        "icon": "🎨",
        "svg_type": "creative",
        "proposito": "Pizarra de dibujo digital con herramientas geométricas e interpretación de trazos asistida por IA.",
        "codigo": "Entorno vectorial sobre Canvas con exportación rasterizada y evaluación estructural mediante modelos multimodales.",
        "uso": "Prototipado rápido de diagramas, conceptualización y educación visual.",
        "color": "#93c5fd"
    },
    {
        "id": 13,
        "titulo": "Consulta Documental PDF (RAG)",
        "cat": "Texto y Documentos",
        "url": "https://chatpdfz.streamlit.app",
        "icon": "💬",
        "svg_type": "text",
        "proposito": "Extracción y resolución de consultas precisas sobre documentos PDF técnicos o contractuales.",
        "codigo": "Segmentación textual, generación de vectores semánticos, búsqueda de similitud con FAISS y respuesta con GPT-4o-mini.",
        "uso": "Revisión ágil de manuales de ingeniería, pliegos contractuales e informes de investigación.",
        "color": "#0284c7"
    },
    {
        "id": 14,
        "titulo": "Analizador Tonal de Mensajes",
        "cat": "Texto y Semántica",
        "url": "https://textanalysiz.streamlit.app",
        "icon": "⚖️",
        "svg_type": "text",
        "proposito": "Evaluación del tono formal, neutralidad y sesgo subjetivo en comunicaciones escritas antes de su envío.",
        "codigo": "Análisis léxico con reglas gramaticales para modificadores e intensificadores, con gráficos de dispersión de sentimiento.",
        "uso": "Moderación de comunicaciones corporativas, atención al cliente y redacción técnica.",
        "color": "#38bdf8"
    },
    {
        "id": 15,
        "titulo": "Modelador de Sistemas Físicos",
        "cat": "Redes y Física",
        "url": "https://histinfz.streamlit.app",
        "icon": "⚡",
        "svg_type": "neural",
        "proposito": "Esquematización de diagramas mecánicos y deducción de ecuaciones de equilibrio de fuerzas.",
        "codigo": "Reconocimiento geométrico de diagramas de cuerpo libre y deducción de condiciones estáticas acopladas.",
        "uso": "Enseñanza de física aplicada y validación conceptual de mecanismos simples.",
        "color": "#60a5fa"
    },
    {
        "id": 16,
        "titulo": "Generador de Relatos Ilustrados",
        "cat": "Visión Creativa",
        "url": "https://ejemplohistinfz.streamlit.app",
        "icon": "📖",
        "svg_type": "creative",
        "proposito": "Elaboración de narrativas breves y estructuradas a partir de bocetos e ilustraciones ingresadas.",
        "codigo": "Procesamiento de bosquejos gráficos y estructuración de historias en tres actos con modelos de lenguaje natural.",
        "uso": "Fomento a la lectura, dinámicas educativas y ejercicios de expresión temprana.",
        "color": "#818cf8"
    }
]

# ============================================================
# ESTILOS MIDNIGHT / GALAXY BLUE
# ============================================================
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
    background-color: #060913 !important;
}

[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stSidebar"], section[data-testid="stSidebar"] { display: none !important; }

.block-container {
    max-width: 1200px !important;
    padding-top: 1.2rem !important;
    padding-bottom: 3.5rem !important;
    margin: 0 auto !important;
    position: relative;
    z-index: 10;
}

.brand-signature {
    text-align: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.76rem;
    letter-spacing: 0.22em;
    color: #38bdf8;
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
}

.sub-lead {
    text-align: center;
    color: #94a3b8;
    font-size: 0.95rem;
    max-width: 740px;
    margin: 0 auto 1.4rem auto;
    line-height: 1.55;
}

/* Indicadores de métrica */
.stat-pill {
    background: rgba(10, 17, 36, 0.94);
    border: 1px solid rgba(56, 189, 248, 0.22);
    border-radius: 8px;
    padding: 10px 12px;
    text-align: center;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.5);
}

/* Barra de progreso de revisión */
.lava-progress-frame {
    background: rgba(10, 17, 36, 0.94);
    border: 1px solid rgba(56, 189, 248, 0.25);
    border-radius: 30px;
    padding: 6px 14px;
    margin-bottom: 1.2rem;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.6);
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
    background: linear-gradient(90deg, #1d4ed8, #3b82f6, #38bdf8, #818cf8, #1d4ed8);
    background-size: 200% 100%;
    animation: galaxyStream 4s linear infinite;
    border-radius: 6px;
    box-shadow: 0 0 10px rgba(56, 189, 248, 0.6);
    transition: width 0.3s ease;
}

@keyframes galaxyStream {
    0% { background-position: 0% 50%; }
    100% { background-position: 200% 50%; }
}

/* Tarjeta Principal */
.carousel-card {
    background: linear-gradient(145deg, rgba(12, 20, 42, 0.96) 0%, rgba(7, 12, 26, 0.98) 100%);
    border: 1px solid rgba(56, 189, 248, 0.28);
    border-top: 3px solid #38bdf8;
    border-radius: 12px;
    padding: 22px 26px;
    box-shadow: 0 14px 40px rgba(0, 0, 0, 0.75), 0 0 20px rgba(56, 189, 248, 0.12);
    margin-bottom: 0.8rem;
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
    letter-spacing: 0.1em;
    text-transform: uppercase;
    font-weight: 600;
    border-radius: 6px;
    padding: 3px 9px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
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
    color: #38bdf8;
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
    background: rgba(5, 9, 20, 0.7);
    border-left: 3px solid #60a5fa;
    border-radius: 6px;
    padding: 10px 14px;
    font-size: 0.9rem;
    color: #cbd5e1;
    line-height: 1.55;
    margin-bottom: 10px;
}

.use-box {
    background: rgba(56, 189, 248, 0.08);
    border-left: 3px solid #38bdf8;
    border-radius: 6px;
    padding: 10px 14px;
    font-size: 0.9rem;
    color: #f1f5f9;
    line-height: 1.55;
}

/* Botones de navegación */
div.stButton > button {
    border-radius: 6px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    background: rgba(12, 20, 42, 0.92) !important;
    color: #e2e8f0 !important;
    border: 1px solid rgba(56, 189, 248, 0.3) !important;
    padding: 0.65rem 1.2rem !important;
    transition: all 0.2s ease !important;
}

div.stButton > button:hover {
    border-color: #38bdf8 !important;
    color: #38bdf8 !important;
    box-shadow: 0 0 16px rgba(56, 189, 248, 0.35) !important;
}

/* Botón de enlace a la app */
div[data-testid="stLinkButton"] > a {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: 100% !important;
    background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 50%, #0284c7 100%) !important;
    color: #ffffff !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    border-radius: 6px !important;
    padding: 0.7rem 1.2rem !important;
    text-decoration: none !important;
    box-shadow: 0 0 18px rgba(37, 99, 235, 0.45) !important;
    transition: all 0.2s ease !important;
}

div[data-testid="stLinkButton"] > a:hover {
    box-shadow: 0 0 25px rgba(56, 189, 248, 0.6) !important;
}

/* Directorio de tarjetas */
.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 14px;
    margin-top: 10px;
}

.grid-card {
    background: rgba(10, 16, 34, 0.95);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-top: 2px solid #38bdf8;
    border-radius: 8px;
    padding: 14px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.5);
    transition: transform 0.2s ease, border-color 0.2s ease;
}

.grid-card:hover {
    transform: translateY(-2px);
    border-color: #38bdf8;
    box-shadow: 0 6px 20px rgba(56, 189, 248, 0.2);
}

.grid-card-link {
    display: inline-block;
    width: 100%;
    text-align: center;
    background: rgba(56, 189, 248, 0.12);
    border: 1px solid rgba(56, 189, 248, 0.35);
    color: #38bdf8;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    font-weight: 600;
    padding: 8px;
    border-radius: 4px;
    text-decoration: none;
    transition: all 0.2s ease;
    margin-top: 8px;
}

.grid-card-link:hover {
    background: #38bdf8;
    color: #060913;
    box-shadow: 0 0 14px rgba(56, 189, 248, 0.5);
}
</style>
""")

# ============================================================
# CANVAS GALAXY BLUE CON FONDO OPTIMIZADO POR GPU
# ============================================================
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
            canvas.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:0;background:#060913;';
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

        // Orbes cósmicos de color azul zafiro, cian celeste e índigo estelar
        const orbs = [
            { x: w * 0.15, y: h * 0.25, r: 180 * scale, vx: 0.5, vy: 0.4, color: 'rgba(37, 99, 235, 0.22)' },
            { x: w * 0.85, y: h * 0.35, r: 200 * scale, vx: -0.4, vy: 0.5, color: 'rgba(56, 189, 248, 0.20)' },
            { x: w * 0.5, y: h * 0.8, r: 170 * scale, vx: 0.4, vy: -0.5, color: 'rgba(99, 102, 241, 0.18)' },
            { x: w * 0.2, y: h * 0.75, r: 160 * scale, vx: -0.4, vy: -0.4, color: 'rgba(129, 140, 248, 0.15)' }
        ];

        const pCount = pWin.innerWidth < 768 ? 16 : 26;
        const particles = [];
        for (let i = 0; i < pCount; i++) {
            particles.push({
                x: Math.random() * w,
                y: Math.random() * h,
                r: Math.random() * 1.4 + 0.8,
                vx: (Math.random() - 0.5) * 0.5,
                vy: (Math.random() - 0.5) * 0.5,
                color: ['#38bdf8', '#818cf8', '#60a5fa', '#93c5fd'][i % 4]
            });
        }

        function loop() {
            ctx.fillStyle = '#060913';
            ctx.fillRect(0, 0, w, h);

            ctx.globalCompositeOperation = 'screen';
            for (let b of orbs) {
                b.x += b.vx;
                b.y += b.vy;
                if (b.x < -30 || b.x > w + 30) b.vx *= -1;
                if (b.y < -30 || b.y > h + 30) b.vy *= -1;

                const g = ctx.createRadialGradient(b.x, b.y, 2, b.x, b.y, b.r);
                g.addColorStop(0, b.color);
                g.addColorStop(1, 'rgba(6, 9, 19, 0)');
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
                        ctx.strokeStyle = `rgba(56, 189, 248, ${0.28 * (1 - d2 / 3800)})`;
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
# ELEMENTOS VECTORIALES HUD EN PALETA GALÁCTICA
# ============================================================
def generar_svg_emblema():
    return """
    <div style="display:flex; justify-content:center; align-items:center; margin-bottom:8px;">
    <svg width="86" height="86" viewBox="0 0 100 100" style="filter: drop-shadow(0 0 12px rgba(56,189,248,0.45));">
        <style>
            .spin-cw { transform-origin: 50px 50px; animation: rClock 14s linear infinite; will-change: transform; }
            .spin-ccw { transform-origin: 50px 50px; animation: rCounter 9s linear infinite; will-change: transform; }
            .pulse-core { transform-origin: 50px 50px; animation: rPulse 2.4s ease-in-out infinite alternate; will-change: transform; }
            @keyframes rClock { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
            @keyframes rCounter { 0% { transform: rotate(360deg); } 100% { transform: rotate(0deg); } }
            @keyframes rPulse { 0% { transform: scale(0.94); opacity: 0.85; } 100% { transform: scale(1.06); opacity: 1; } }
        </style>
        <circle class="spin-cw" cx="50" cy="50" r="44" fill="none" stroke="#38bdf8" stroke-width="1.6" stroke-dasharray="10 6 3 6"/>
        <circle class="spin-ccw" cx="50" cy="50" r="34" fill="none" stroke="#818cf8" stroke-width="1.3" stroke-dasharray="8 5 12 5" opacity="0.85"/>
        <polygon class="spin-cw" points="50,22 57,34 70,34 60,42 63,55 50,47 37,55 40,42 30,34 43,34" fill="none" stroke="#60a5fa" stroke-width="1" opacity="0.75"/>
        <g class="pulse-core">
            <circle cx="50" cy="50" r="13" fill="rgba(56,189,248,0.18)" stroke="#38bdf8" stroke-width="1.6"/>
            <text x="50" y="54" font-size="13" font-family="'JetBrains Mono', monospace" font-weight="bold" fill="#e0f2fe" text-anchor="middle">✦</text>
        </g>
    </svg>
    </div>
    """

def generar_svg_hud(tipo: str, color_hex: str):
    if tipo == "vision":
        return f"""
        <div style="background:rgba(9,15,32,0.96); border:1px solid {color_hex}55; border-radius:10px; padding:14px; text-align:center; box-shadow:0 6px 20px rgba(0,0,0,0.6);">
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_hex}; letter-spacing:0.16em; margin-bottom:6px;">MODO ÓPTICO ACTIVO</div>
            <svg width="220" height="170" viewBox="0 0 220 170">
                <style>
                    .laser-sweep {{ animation: sweepY 2.8s ease-in-out infinite alternate; will-change: transform; }}
                    .spin-reticle {{ transform-origin: 110px 85px; animation: rClock 14s linear infinite; will-change: transform; }}
                    @keyframes sweepY {{ 0% {{ transform: translateY(15px); }} 100% {{ transform: translateY(145px); }} }}
                </style>
                <rect x="5" y="5" width="210" height="160" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="1" rx="6"/>
                <circle class="spin-reticle" cx="110" cy="85" r="54" fill="none" stroke="{color_hex}" stroke-width="1.3" stroke-dasharray="10 6 4 6" opacity="0.6"/>
                <circle cx="110" cy="85" r="26" fill="none" stroke="#60a5fa" stroke-width="1" stroke-dasharray="5 3"/>
                <rect x="65" y="40" width="90" height="90" fill="none" stroke="{color_hex}" stroke-width="1.3" stroke-dasharray="8 6"/>
                <path d="M 60 48 L 60 36 L 72 36" fill="none" stroke="{color_hex}" stroke-width="2"/>
                <path d="M 160 48 L 160 36 L 148 36" fill="none" stroke="{color_hex}" stroke-width="2"/>
                <path d="M 60 122 L 60 134 L 72 134" fill="none" stroke="{color_hex}" stroke-width="2"/>
                <path d="M 160 122 L 160 134 L 148 134" fill="none" stroke="{color_hex}" stroke-width="2"/>
                <line class="laser-sweep" x1="10" y1="0" x2="210" y2="0" stroke="{color_hex}" stroke-width="1.8" opacity="0.8"/>
                <text x="110" y="89" font-family="'JetBrains Mono'" font-size="9" fill="#e2e8f0" text-anchor="middle">ANÁLISIS DE CUADRO</text>
            </svg>
        </div>
        """
    elif tipo == "audio":
        return f"""
        <div style="background:rgba(9,15,32,0.96); border:1px solid {color_hex}55; border-radius:10px; padding:14px; text-align:center; box-shadow:0 6px 20px rgba(0,0,0,0.6);">
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_hex}; letter-spacing:0.16em; margin-bottom:6px;">ESPECTRO AUDITIVO</div>
            <svg width="220" height="170" viewBox="0 0 220 170">
                <style>
                    .bar1 {{ transform-origin: bottom; animation: bScale 0.9s ease-in-out infinite alternate; will-change: transform; }}
                    .bar2 {{ transform-origin: bottom; animation: bScale 0.7s ease-in-out infinite 0.2s alternate; will-change: transform; }}
                    .bar3 {{ transform-origin: bottom; animation: bScale 1.1s ease-in-out infinite 0.4s alternate; will-change: transform; }}
                    @keyframes bScale {{ 0% {{ transform: scaleY(0.3); }} 100% {{ transform: scaleY(1.15); }} }}
                </style>
                <circle cx="110" cy="80" r="48" fill="none" stroke="{color_hex}" stroke-width="1.2" opacity="0.3"/>
                <circle cx="110" cy="80" r="26" fill="none" stroke="#60a5fa" stroke-width="1" stroke-dasharray="4 3"/>
                <g transform="translate(55, 80)">
                    <rect class="bar1" x="0" y="-30" width="7" height="60" rx="3" fill="{color_hex}"/>
                    <rect class="bar2" x="16" y="-38" width="7" height="76" rx="3" fill="#60a5fa"/>
                    <rect class="bar3" x="32" y="-48" width="7" height="96" rx="3" fill="{color_hex}"/>
                    <rect class="bar1" x="48" y="-40" width="7" height="80" rx="3" fill="#818cf8"/>
                    <rect class="bar2" x="64" y="-30" width="7" height="60" rx="3" fill="{color_hex}"/>
                    <rect class="bar3" x="80" y="-44" width="7" height="88" rx="3" fill="#38bdf8"/>
                    <rect class="bar1" x="96" y="-24" width="7" height="48" rx="3" fill="{color_hex}"/>
                </g>
                <text x="110" y="154" font-family="'JetBrains Mono'" font-size="9" fill="#94a3b8" text-anchor="middle">SÍNTESIS CONTINUA</text>
            </svg>
        </div>
        """
    elif tipo == "neural":
        return f"""
        <div style="background:rgba(9,15,32,0.96); border:1px solid {color_hex}55; border-radius:10px; padding:14px; text-align:center; box-shadow:0 6px 20px rgba(0,0,0,0.6);">
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_hex}; letter-spacing:0.16em; margin-bottom:6px;">PROCESAMIENTO NEURONAL</div>
            <svg width="220" height="170" viewBox="0 0 220 170">
                <style>
                    .syn-fire {{ animation: sPulse 1.6s ease-in-out infinite alternate; will-change: opacity; }}
                    .cad-spin {{ transform-origin: 110px 85px; animation: rClock 18s linear infinite; will-change: transform; }}
                    @keyframes sPulse {{ 0% {{ opacity: 0.35; stroke-width: 1; }} 100% {{ opacity: 1; stroke-width: 2; }} }}
                </style>
                <circle class="cad-spin" cx="110" cy="85" r="60" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.2" stroke-dasharray="10 8"/>
                <line class="syn-fire" x1="40" y1="45" x2="110" y2="60" stroke="{color_hex}"/>
                <line class="syn-fire" x1="40" y1="85" x2="110" y2="85" stroke="#60a5fa"/>
                <line class="syn-fire" x1="40" y1="125" x2="110" y2="110" stroke="{color_hex}"/>
                <line class="syn-fire" x1="110" y1="60" x2="180" y2="85" stroke="#818cf8"/>
                <line class="syn-fire" x1="110" y1="110" x2="180" y2="85" stroke="{color_hex}"/>
                <circle cx="40" cy="45" r="7" fill="#060913" stroke="{color_hex}" stroke-width="1.8"/>
                <circle cx="40" cy="85" r="7" fill="#060913" stroke="{color_hex}" stroke-width="1.8"/>
                <circle cx="40" cy="125" r="7" fill="#060913" stroke="{color_hex}" stroke-width="1.8"/>
                <circle cx="110" cy="60" r="8" fill="#060913" stroke="#60a5fa" stroke-width="1.8"/>
                <circle cx="110" cy="110" r="8" fill="#060913" stroke="#60a5fa" stroke-width="1.8"/>
                <circle cx="180" cy="85" r="10" fill="#060913" stroke="#38bdf8" stroke-width="2"/>
                <text x="110" y="154" font-family="'JetBrains Mono'" font-size="9" fill="#94a3b8" text-anchor="middle">MATRIZ CONVOLUCIONAL</text>
            </svg>
        </div>
        """
    elif tipo == "text":
        return f"""
        <div style="background:rgba(9,15,32,0.96); border:1px solid {color_hex}55; border-radius:10px; padding:14px; text-align:center; box-shadow:0 6px 20px rgba(0,0,0,0.6);">
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_hex}; letter-spacing:0.16em; margin-bottom:6px;">EXTRACCIÓN SEMÁNTICA</div>
            <svg width="220" height="170" viewBox="0 0 220 170">
                <style>
                    .data-flow {{ stroke-dasharray: 6 4; animation: fDash 2.8s linear infinite; will-change: stroke-dashoffset; }}
                    @keyframes fDash {{ 0% {{ stroke-dashoffset: 0; }} 100% {{ stroke-dashoffset: -40; }} }}
                </style>
                <path class="data-flow" d="M 15 45 Q 70 20, 110 60 T 205 45" fill="none" stroke="{color_hex}" stroke-width="1.6"/>
                <path class="data-flow" d="M 15 85 Q 70 120, 110 85 T 205 85" fill="none" stroke="#60a5fa" stroke-width="1.6"/>
                <path class="data-flow" d="M 15 125 Q 70 100, 110 115 T 205 125" fill="none" stroke="#818cf8" stroke-width="1.6"/>
                <circle cx="55" cy="35" r="5" fill="#060913" stroke="{color_hex}" stroke-width="1.8"/>
                <circle cx="110" cy="85" r="7" fill="#060913" stroke="#60a5fa" stroke-width="1.8"/>
                <circle cx="165" cy="120" r="5" fill="#060913" stroke="#818cf8" stroke-width="1.8"/>
                <text x="110" y="154" font-family="'JetBrains Mono'" font-size="9" fill="#94a3b8" text-anchor="middle">ÍNDICE VECTORIAL</text>
            </svg>
        </div>
        """
    else:
        return f"""
        <div style="background:rgba(9,15,32,0.96); border:1px solid {color_hex}55; border-radius:10px; padding:14px; text-align:center; box-shadow:0 6px 20px rgba(0,0,0,0.6);">
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_hex}; letter-spacing:0.16em; margin-bottom:6px;">COMPOSICIÓN GRÁFICA</div>
            <svg width="220" height="170" viewBox="0 0 220 170">
                <style>
                    .prism-spin {{ transform-origin: 110px 80px; animation: rClock 14s linear infinite; will-change: transform; }}
                </style>
                <polygon class="prism-spin" points="110,32 148,108 72,108" fill="rgba(56,189,248,0.12)" stroke="{color_hex}" stroke-width="1.6"/>
                <circle class="prism-spin" cx="110" cy="80" r="24" fill="none" stroke="#60a5fa" stroke-width="1.2" stroke-dasharray="6 4"/>
                <circle cx="48" cy="42" r="3" fill="#38bdf8"/>
                <circle cx="172" cy="50" r="3" fill="#818cf8"/>
                <circle cx="160" cy="128" r="3" fill="#60a5fa"/>
                <circle cx="58" cy="118" r="3" fill="#93c5fd"/>
                <text x="110" y="152" font-family="'JetBrains Mono'" font-size="9" fill="#94a3b8" text-anchor="middle">CANVAS DINÁMICO</text>
            </svg>
        </div>
        """

# ============================================================
# CABECERA Y MÉTRICAS
# ============================================================
render_clean_html(generar_svg_emblema())
render_clean_html('<div class="brand-signature">Sistemas e Interfaces Interactivas</div>')
render_clean_html('<div class="main-title">Portafolio de Aplicaciones</div>')
render_clean_html('<div class="sub-lead">Catálogo de 16 desarrollos en visión por computador, modelos de lenguaje, procesamiento acústico y análisis sensorial.</div>')

total_apps = len(CATALOGO)
visitadas_count = len(st.session_state.visited_apps)
progreso_pct = int((visitadas_count / total_apps) * 100)

s1, s2, s3, s4 = st.columns(4)
with s1:
    render_clean_html(f'<div class="stat-pill"><div style="font-size:0.68rem; color:#94a3b8; font-family:\'JetBrains Mono\';">TOTAL APLICACIONES</div><div style="font-size:1.5rem; font-weight:700; color:#ffffff;">{total_apps}</div></div>')
with s2:
    render_clean_html(f'<div class="stat-pill"><div style="font-size:0.68rem; color:#94a3b8; font-family:\'JetBrains Mono\';">EXPLORADAS</div><div style="font-size:1.5rem; font-weight:700; color:#38bdf8;">{visitadas_count} de {total_apps}</div></div>')
with s3:
    render_clean_html(f'<div class="stat-pill"><div style="font-size:0.68rem; color:#94a3b8; font-family:\'JetBrains Mono\';">COBERTURA</div><div style="font-size:1.5rem; font-weight:700; color:#818cf8;">{progreso_pct}%</div></div>')
with s4:
    categorias_unicas = len(set(a["cat"] for a in CATALOGO))
    render_clean_html(f'<div class="stat-pill"><div style="font-size:0.68rem; color:#94a3b8; font-family:\'JetBrains Mono\';">ÁREAS TEMÁTICAS</div><div style="font-size:1.5rem; font-weight:700; color:#60a5fa;">{categorias_unicas}</div></div>')

st.write("")

render_clean_html(f"""
<div class="lava-progress-frame">
    <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono'; font-size:0.72rem; margin-bottom:5px; padding:0 4px;">
        <span style="color:#94a3b8;">PROGRESO DE EXPLORACIÓN</span>
        <span style="color:#38bdf8; font-weight:600;">{visitadas_count} de {total_apps} revisadas ({progreso_pct}%)</span>
    </div>
    <div class="lava-progress-bar">
        <div class="lava-progress-fill" style="width: {max(5, progreso_pct)}%;"></div>
    </div>
</div>
""")

# ============================================================
# FILTRADO Y SELECTOR DIRECTO
# ============================================================
c_search, c_filter = st.columns([1.5, 1], gap="medium")
with c_search:
    termino_busqueda = st.text_input(
        "Buscar aplicación:",
        placeholder="Ej: YOLO, OCR, voz, PDF, dibujo, MNIST...",
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

nombres_apps = [f"#{a['id']:02d} — {a['titulo']}" for a in filtradas]
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

# ============================================================
# CARRUSEL CON DESCRIPCIÓN Y HUD
# ============================================================
badge_visita_html = '<span class="visited-badge">✓ Revisada</span>' if esta_visitada else '<span style="font-family:\'JetBrains Mono\'; font-size:0.72rem; color:#94a3b8; background:rgba(255,255,255,0.06); padding:3px 8px; border-radius:6px;">○ Pendiente</span>'

col_desc, col_hud = st.columns([1.5, 0.9], gap="medium")

with col_desc:
    html_card = f"""
    <div class="carousel-card">
        <div class="card-top-row">
            <div>
                <span class="cat-badge" style="background:{app_actual['color']}22; border:1px solid {app_actual['color']}55; color:{app_actual['color']};">
                    {app_actual['icon']} {app_actual['cat']}
                </span>
                <span style="font-family:'JetBrains Mono'; font-size:0.74rem; color:#94a3b8; margin-left:8px;">
                    ÍTEM #{app_actual['id']:02d} DE {total_apps:02d}
                </span>
            </div>
            <div>{badge_visita_html}</div>
        </div>
        <div class="card-title">{app_actual['titulo']}</div>
        <div class="section-label">Descripción</div>
        <div class="section-text">{app_actual['proposito']}</div>
        <div class="section-label">Arquitectura y Métodos</div>
        <div class="code-box">⚙️ {app_actual['codigo']}</div>
        <div class="section-label">Casos de Uso</div>
        <div class="use-box">💡 <b>Aplicación práctica:</b> {app_actual['uso']}</div>
    </div>
    """
    render_clean_html(html_card)

with col_hud:
    render_clean_html(generar_svg_hud(app_actual["svg_type"], app_actual["color"]))

col_ant, col_visitar, col_toggle, col_sig = st.columns([1, 1.6, 1.4, 1], gap="small")

with col_ant:
    if st.button("← Anterior", use_container_width=True):
        st.session_state.carousel_idx = (st.session_state.carousel_idx - 1) % len(filtradas)
        st.rerun()

with col_visitar:
    st.link_button(f"Abrir {app_actual['titulo'].split()[0]} ↗", app_actual["url"], use_container_width=True)

with col_toggle:
    btn_lbl = "✓ Desmarcar" if esta_visitada else "Marcar como revisada"
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
# DIRECTORIO GENERAL COMPLETO
# ============================================================
st.markdown("### Directorio de Acceso Directo")
st.markdown("<p style='color:#94a3b8; font-size:0.88rem; margin-top:-8px;'>Acceso inmediato a cualquiera de las herramientas disponibles.</p>", unsafe_allow_html=True)

grid_cards_html = ['<div class="grid-container">']
for item in CATALOGO:
    item_visitado = item["id"] in st.session_state.visited_apps
    simbolo_visita = "✓ Revisada" if item_visitado else "○ Pendiente"
    color_visita = "#2dd4bf" if item_visitado else "#94a3b8"

    grid_cards_html.append(f"""
    <div class="grid-card" style="border-top-color:{item['color']};">
        <div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                <span style="font-size:1.15rem;">{item['icon']}</span>
                <span style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{color_visita}; font-weight:600;">{simbolo_visita}</span>
            </div>
            <div style="font-weight:700; font-size:0.92rem; color:#ffffff; min-height:40px; line-height:1.25;">{item['titulo']}</div>
            <div style="font-family:'JetBrains Mono'; font-size:0.68rem; color:{item['color']}; margin:3px 0 6px 0; text-transform:uppercase;">{item['cat']}</div>
            <p style="font-size:0.8rem; color:#94a3b8; line-height:1.4; margin-bottom:8px;">{item['proposito'][:78]}...</p>
        </div>
        <a href="{item['url']}" target="_blank" class="grid-card-link">Abrir aplicación ↗</a>
    </div>
    """)
grid_cards_html.append('</div>')

render_clean_html("".join(grid_cards_html))

st.write("")
render_clean_html("""
<div style="text-align:center; padding:1.8rem 0; border-top:1px solid rgba(255,255,255,0.08); margin-top:2rem;">
    <div style="font-family:'JetBrains Mono'; font-size:0.74rem; letter-spacing:0.18em; color:#38bdf8; text-transform:uppercase;">
        PORTAFOLIO DE SISTEMAS E INTERFACES MULTIMODALES
    </div>
    <div style="font-size:0.8rem; color:#64748b; margin-top:4px;">
        16 aplicaciones desplegadas sobre Streamlit Cloud
    </div>
</div>
""")
