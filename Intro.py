import streamlit as st

# ============================================================
# CONFIGURACIÓN GENERAL (PORTAFOLIO CENTRAL — SIN IMÁGENES)
# ============================================================
st.set_page_config(
    page_title="Aplicaciones de Inteligencia Artificial // Krov Industries",
    page_icon="⚜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# LÍNEA BASE VISUAL: GEOMETRÍA ARQUITECTÓNICA PURA (ZERO IMAGES)
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,400;0,600;0,700;1,400&family=JetBrains+Mono:wght@400;500;700&display=swap');

html, body, [data-testid="stAppViewContainer"], .stApp {
    background-color: #050609 !important;
    color: #e5e7eb !important;
    font-family: 'Spectral', Georgia, serif !important;
    overflow-x: hidden;
}

[data-testid="stHeader"] { background: transparent !important; }

/* 1. Malla continua de gradientes dorados y obsidiana */
.stApp {
    background: linear-gradient(135deg, #050609 0%, #0d1017 30%, #17140a 60%, #08090d 100%) !important;
    background-size: 300% 300% !important;
    animation: goldMesh 20s ease infinite alternate !important;
}

@keyframes goldMesh {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* 2. Fluidos orgánicos ambientales */
.ambient-glow-1 {
    position: fixed;
    top: 10%;
    left: -120px;
    width: 550px;
    height: 550px;
    background: radial-gradient(circle, rgba(212, 175, 55, 0.12) 0%, rgba(56, 189, 248, 0.03) 55%, transparent 70%);
    border-radius: 40% 60% 70% 30% / 50% 60% 40% 50%;
    filter: blur(90px);
    animation: driftAmb1 22s infinite alternate ease-in-out;
    pointer-events: none;
    z-index: 0;
}

.ambient-glow-2 {
    position: fixed;
    bottom: 5%;
    right: -100px;
    width: 580px;
    height: 580px;
    background: radial-gradient(circle, rgba(56, 189, 248, 0.1) 0%, rgba(212, 175, 55, 0.03) 55%, transparent 70%);
    border-radius: 60% 40% 50% 50% / 40% 50% 60% 50%;
    filter: blur(95px);
    animation: driftAmb2 25s infinite alternate ease-in-out;
    pointer-events: none;
    z-index: 0;
}

@keyframes driftAmb1 {
    0% { transform: translate(0, 0) scale(1); }
    50% { transform: translate(120px, 70px) scale(1.12); }
    100% { transform: translate(30px, 130px) scale(0.95); }
}

@keyframes driftAmb2 {
    0% { transform: translate(0, 0) scale(1); }
    50% { transform: translate(-110px, -80px) scale(1.15); }
    100% { transform: translate(-20px, -120px) scale(0.92); }
}

.brand-signature {
    text-align: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.2em;
    color: #d4af37;
    text-transform: uppercase;
    margin-bottom: 2px;
}

.main-title {
    font-family: 'Spectral', serif;
    font-size: 2.3rem;
    font-weight: 700;
    text-align: center;
    color: #ffffff;
    margin-bottom: 0.3rem;
    text-shadow: 0 0 30px rgba(212, 175, 55, 0.35);
}

.sub-lead {
    text-align: center;
    color: #94a3b8;
    font-size: 0.98rem;
    max-width: 780px;
    margin: 0 auto 1.8rem auto;
    line-height: 1.6;
}

/* Tarjeta destacada del carrusel (Geométrica sin imágenes) */
.project-card {
    background: rgba(11, 14, 22, 0.88);
    border: 1px solid rgba(212, 175, 55, 0.35);
    border-radius: 12px;
    padding: 30px;
    box-shadow: 0 15px 45px rgba(0, 0, 0, 0.7), 0 0 25px rgba(212, 175, 55, 0.1);
    backdrop-filter: blur(16px);
    transition: transform 0.3s ease, border-color 0.3s ease;
    margin-bottom: 1.2rem;
}

.category-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #38bdf8;
    background: rgba(56, 189, 248, 0.1);
    border: 1px solid rgba(56, 189, 248, 0.3);
    border-radius: 4px;
    padding: 3px 8px;
    display: inline-block;
    margin-bottom: 12px;
}

.project-title {
    font-family: 'Spectral', serif;
    font-size: 1.8rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 8px;
}

.project-desc {
    font-size: 1.05rem;
    line-height: 1.7;
    color: #cbd5e1;
    margin-bottom: 20px;
}

/* Recomendaciones cruzadas */
.recom-box {
    background: rgba(18, 22, 34, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-left: 3px solid #d4af37;
    border-radius: 6px;
    padding: 12px 16px;
    margin-top: 10px;
}

div.stButton > button {
    border-radius: 6px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.05em !important;
    transition: all 0.25s ease !important;
}
</style>

<div class="ambient-glow-1"></div>
<div class="ambient-glow-2"></div>
""", unsafe_allow_html=True)

# ============================================================
# CATÁLOGO DE LAS 16 APLICACIONES (AUDITADO Y DOCUMENTADO)
# ============================================================
CATALOGO = [
    {
        "id": 1,
        "titulo": "Detector de Objetos (YOLOv5)",
        "categoria": "Visión por Computadora",
        "descripcion": "Inferencia de detección visual en tiempo real para 80 clases de objetos mediante redes convolucionales YOLOv5, con telemetría de confianza y filtros de superposición.",
        "url": "",
        "recomendacion": "Combínalo con el Detector de Presencia para verificar si las siluetas corresponden a usuarios humanos o a objetos inanimados."
    },
    {
        "id": 2,
        "titulo": "Generador de Nube de Palabras",
        "categoria": "Analítica de Texto",
        "descripcion": "Extracción semántica y cálculo de frecuencias léxicas que produce una representación gráfica proporcional con filtrado gramatical y siluetas personalizadas.",
        "url": "",
        "recomendacion": "Úsalo junto con el Analizador de Tono y Emociones para evaluar el trasfondo anímico de las palabras más repetidas."
    },
    {
        "id": 3,
        "titulo": "Reconocedor de Dígitos",
        "categoria": "Redes Neuronales",
        "descripcion": "Clasificador óptico de números manuscritos del 0 al 9 entrenado sobre MNIST, con lienzo de dibujo simétrico y cálculo de probabilidades por categoría.",
        "url": "",
        "recomendacion": "Pruébalo con el Tablero Creativo de Bocetos si deseas interpretar figuras complejas más allá de números individuales."
    },
    {
        "id": 4,
        "titulo": "Análisis de Imagen con GPT-4o",
        "categoria": "Visión Multimodal",
        "descripcion": "Descripción contextual profunda y respuesta a preguntas analíticas sobre fotografías o esquemas técnicos mediante modelos multimodales avanzados.",
        "url": "",
        "recomendacion": "Resulta ideal para contrastar la salida técnica del OCR con una interpretación narrativa de alto nivel."
    },
    {
        "id": 5,
        "titulo": "Traductor de Voz a Audio",
        "categoria": "Voz y Lenguaje",
        "descripcion": "Captura continua por micrófono, traducción instantánea entre ocho idiomas y síntesis vocal con modulación de acentos territoriales.",
        "url": "",
        "recomendacion": "Se complementa con el Espejo Mágico si requieres traducir textos físicos impresos en lugar de frases orales."
    },
    {
        "id": 6,
        "titulo": "Detector de Presencia y Postura",
        "categoria": "Visión por Computadora",
        "descripcion": "Identificación de siluetas humanas y puntos articulares faciales y corporales mediante PoseNet, con conteo estricto y confirmación por fotogramas.",
        "url": "",
        "recomendacion": "Excelente adición al Detector YOLOv5 para aplicaciones de control de aforo y postura física."
    },
    {
        "id": 7,
        "titulo": "Espacio de Ánimo y Humor",
        "categoria": "Interacción y Bienestar",
        "descripcion": "Lienzo interactivo de partículas reactivas al cursor con un repertorio dinámico de más de cien chistes reproducidos por voz sintetizada.",
        "url": "",
        "recomendacion": "Funciona en sintonía con el Compañero de Conversación para distender momentos de fatiga mental."
    },
    {
        "id": 8,
        "titulo": "Compañero de Conversación",
        "categoria": "Asistencia Empática",
        "descripcion": "Asistente emocional con clasificación de intenciones en español nativo, retroalimentación afectiva, avatar holográfico y voz de apoyo.",
        "url": "",
        "recomendacion": "Combínalo con el Analizador de Tono para entender la estructura gramatical de lo que estás expresando."
    },
    {
        "id": 9,
        "titulo": "Espejo Mágico de Lectura",
        "categoria": "Óptica y Traducción",
        "descripcion": "Reconocimiento de texto en documentos impresos con realce de contraste CLAHE, traducción y espejo 3D interactivo con haz de barrido.",
        "url": "",
        "recomendacion": "Enlázalo con el Traductor de Voz para alternar entre fuentes de entrada escritas y habladas."
    },
    {
        "id": 10,
        "titulo": "Reconocimiento Óptico (Cámara)",
        "categoria": "Visión por Computadora",
        "descripcion": "Extracción directa de caracteres desde la cámara web con inversión de contraste y métricas en vivo de recuento léxico.",
        "url": "",
        "recomendacion": "Útil como paso previo antes de procesar documentos extensos en el sistema RAG de PDFs."
    },
    {
        "id": 12,
        "titulo": "Explorador de Interfaces Multimodales",
        "categoria": "Interacción Sensorial",
        "descripcion": "Laboratorio conceptual sobre modalidades de interacción visual, auditiva y háptica en entornos de usuario modernos.",
        "url": "",
        "recomendacion": "Aporta fundamentos teóricos para el diseño de interfaces en el Compañero de Conversación."
    },
    {
        "id": 13,
        "titulo": "Tablero Creativo de Bocetos",
        "categoria": "Visión Multimodal",
        "descripcion": "Lienzo de dibujo libre asistido por GPT-4o-mini para deducir creativamente el concepto y significado de ilustraciones rápidas.",
        "url": "",
        "recomendacion": "Es el complemento lúdico perfecto frente al análisis puramente matemático del Reconocedor de Dígitos."
    },
    {
        "id": 14,
        "titulo": "Interrogación Documental RAG",
        "categoria": "Analítica de Texto",
        "descripcion": "Sistema de Generación Aumentada por Recuperación que divide documentos PDF en fragmentos indexados por FAISS para resolver preguntas precisas.",
        "url": "",
        "recomendacion": "Utilízalo tras procesar artículos clave con la Nube de Palabras para profundizar en párrafos específicos."
    },
    {
        "id": 15,
        "titulo": "Analizador de Tono y Emociones",
        "categoria": "Analítica de Texto",
        "descripcion": "Evaluación cuantitativa de polaridad, subjetividad y trayectoria emocional frase por frase con radares pentagonales y sugerencias de estilo.",
        "url": "",
        "recomendacion": "Potencia la redacción de correos y discursos antes de presentarlos a una audiencia."
    },
    {
        "id": 16,
        "titulo": "Deducción Topológica de Sistemas",
        "categoria": "Redes Neuronales",
        "descripcion": "Lienzo de diagramación geométrica que extrapola leyes mecanicistas de conservación y acoplamiento de campos sobre esquemas físicos.",
        "url": "",
        "recomendacion": "Combínalo con el Tablero de Bocetos para pasar de la deducción de objetos a la física teórica."
    },
    {
        "id": 17,
        "titulo": "Generador de Historias Infantiles",
        "categoria": "Visión Multimodal",
        "descripcion": "Plataforma de dibujo que identifica los trazos del usuario e inventa relatos creativos y adaptados para niños a partir de lo dibujado.",
        "url": "",
        "recomendacion": "Un excelente punto de partida interactivo para estimular la imaginación creativa."
    }
]

# ============================================================
# ESTADO DEL CARRUSEL Y FILTRADO
# ============================================================
if "carousel_index" not in st.session_state:
    st.session_state.carousel_index = 0

st.markdown('<div class="brand-signature">Krov Industries · Directorio de Sistemas</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">Aplicaciones de Inteligencia Artificial.</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-lead">'
    'Colección integrada de modelos neuronales, visión por computadora, procesamiento de lenguaje y herramientas multimodales.'
    '</div>',
    unsafe_allow_html=True
)

# CONTROLES DE DESCUBRIMIENTO: BÚSQUEDA Y CATEGORÍAS
c_search, c_filter = st.columns([1.5, 1], gap="medium")
with c_search:
    search_query = st.text_input("Buscar proyecto por palabra clave o función:", placeholder="Ejemplo: YOLO, voz, PDF, OCR...")
with c_filter:
    categories = ["Todas", "Visión por Computadora", "Voz y Lenguaje", "Analítica de Texto", "Redes Neuronales", "Visión Multimodal"]
    selected_cat = st.selectbox("Filtrar por categoría funcional:", categories)

# Filtrado dinámico del catálogo
filtered_projects = [
    p for p in CATALOGO
    if (selected_cat == "Todas" or p["categoria"] == selected_cat)
    and (not search_query or search_query.lower() in p["titulo"].lower() or search_query.lower() in p["descripcion"].lower())
]

if not filtered_projects:
    st.info("No se encontraron aplicaciones con los criterios seleccionados. Restablece el filtro o la búsqueda.")
    filtered_projects = CATALOGO

# Asegurar que el índice permanezca dentro de los límites
st.session_state.carousel_index = max(0, min(st.session_state.carousel_index, len(filtered_projects) - 1))
current_proj = filtered_projects[st.session_state.carousel_index]

# ============================================================
# CARRUSEL INTERACTIVO (100% LIBRE DE IMÁGENES)
# ============================================================
st.markdown('<div class="project-card">', unsafe_allow_html=True)
st.markdown(f'<div class="category-tag">{current_proj["categoria"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="project-title">{current_proj["titulo"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="project-desc">{current_proj["descripcion"]}</div>', unsafe_allow_html=True)

st.markdown(
    f"""
    <div class="recom-box">
        <div style="font-family:'JetBrains Mono'; font-size:0.75rem; color:#d4af37; font-weight:700; margin-bottom:2px;">
            SISTEMA RECOMENDADO RELACIONADO:
        </div>
        <div style="font-size:0.95rem; color:#e2e8f0;">
            {current_proj["recomendacion"]}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

# NAVEGACIÓN Y ACCIÓN DE ENLACE (TODOS LOS DESTINOS EN BLANCO SEGÚN LA ESPECIFICACIÓN)
c_prev, c_action, c_next = st.columns([1, 1.4, 1])

with c_prev:
    if st.button("← Proyecto anterior", use_container_width=True):
        st.session_state.carousel_index = (st.session_state.carousel_index - 1) % len(filtered_projects)
        st.rerun()

with c_action:
    # Si la URL es cadena vacía "", se muestra el estado inactivo según la regla 10.3
    if current_proj["url"].strip():
        st.link_button("Abrir aplicación", current_proj["url"], use_container_width=True)
    else:
        st.button("Enlace pendiente", disabled=True, use_container_width=True)

with c_next:
    if st.button("Siguiente proyecto →", use_container_width=True):
        st.session_state.carousel_index = (st.session_state.carousel_index + 1) % len(filtered_projects)
        st.rerun()

st.caption(f"Visualizando {st.session_state.carousel_index + 1} de {len(filtered_projects)} aplicaciones catalogadas.")
