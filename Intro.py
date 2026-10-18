import streamlit as st

# ============================================================
# CONFIGURACIÓN GENERAL (SIN IMÁGENES — REGLA 10.1)
# ============================================================
st.set_page_config(
    page_title="Aplicaciones de Inteligencia Artificial // Krov Industries",
    page_icon="⚜",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------------------------------------------------------
# ESTADO DE NAVEGACIÓN Y SEGUIMIENTO DE PROGRESO
# ------------------------------------------------------------
if "carousel_idx" not in st.session_state:
    st.session_state.carousel_idx = 0

if "visited_apps" not in st.session_state:
    st.session_state.visited_apps = set()

# ============================================================
# ESTILOS VISUALES: LÁMPARA DE LAVA, EFECTOS 3D Y RESPLANDOR
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,500;0,700;1,400&family=JetBrains+Mono:wght@400;600;700&display=swap');

html, body, [data-testid="stAppViewContainer"], .stApp {
    background-color: #05060a !important;
    color: #e5e7eb !important;
    font-family: 'Spectral', Georgia, serif !important;
    overflow-x: hidden;
}

[data-testid="stHeader"] { background: transparent !important; }

/* Fondo continuo estilo lámpara de lava acelerado por GPU */
.stApp {
    background:
        radial-gradient(circle at 15% 20%, rgba(212, 175, 55, 0.15) 0%, transparent 40%),
        radial-gradient(circle at 85% 30%, rgba(56, 189, 248, 0.16) 0%, transparent 45%),
        radial-gradient(circle at 50% 85%, rgba(168, 85, 247, 0.14) 0%, transparent 45%),
        linear-gradient(135deg, #05060a 0%, #0c0f17 50%, #05060a 100%) !important;
    background-size: 200% 200% !important;
    animation: portfolioLava 16s ease infinite alternate !important;
}

@keyframes portfolioLava {
    0% { background-position: 0% 0%; }
    50% { background-position: 100% 100%; }
    100% { background-position: 0% 100%; }
}

.brand-signature {
    text-align: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.2em;
    color: #d4af37;
    text-transform: uppercase;
}

.main-title {
    font-family: 'Spectral', serif;
    font-size: 2.3rem;
    font-weight: 700;
    text-align: center;
    background: linear-gradient(90deg, #ffffff 0%, #d4af37 50%, #38bdf8 100%);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: goldPulse 8s linear infinite;
    margin-bottom: 0.2rem;
}

@keyframes goldPulse {
    to { background-position: 200% center; }
}

.sub-lead {
    text-align: center;
    color: #94a3b8;
    font-size: 0.95rem;
    margin-bottom: 1.4rem;
}

/* Barra de progreso de flujo líquido */
.lava-progress-bar {
    width: 100%;
    height: 10px;
    background: rgba(255, 255, 255, 0.08);
    border-radius: 6px;
    overflow: hidden;
    position: relative;
    box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.8);
    margin-bottom: 1.6rem;
}

.lava-progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #d4af37, #f59e0b, #38bdf8, #a855f7);
    background-size: 300% 100%;
    animation: lavaFlow 4s linear infinite;
    border-radius: 6px;
    box-shadow: 0 0 15px rgba(212, 175, 55, 0.8);
    transition: width 0.4s ease;
}

@keyframes lavaFlow {
    0% { background-position: 0% 50%; }
    100% { background-position: 300% 50%; }
}

/* Tarjeta del carrusel con efecto de perspectiva del espejo mágico */
.carousel-card {
    background: rgba(10, 13, 22, 0.85);
    border: 1px solid rgba(212, 175, 55, 0.35);
    border-radius: 12px;
    padding: 26px 30px;
    box-shadow: 0 15px 45px rgba(0, 0, 0, 0.7), 0 0 25px rgba(212, 175, 55, 0.1);
    backdrop-filter: blur(14px);
    transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
    margin-bottom: 1rem;
}

.carousel-card:hover {
    transform: perspective(900px) rotateX(1.5deg) translateY(-3px);
    border-color: #d4af37;
    box-shadow: 0 20px 55px rgba(0, 0, 0, 0.8), 0 0 35px rgba(212, 175, 55, 0.25);
}

.cat-badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #38bdf8;
    background: rgba(56, 189, 248, 0.1);
    border: 1px solid rgba(56, 189, 248, 0.25);
    border-radius: 4px;
    padding: 3px 8px;
    display: inline-block;
    margin-bottom: 10px;
}

.visited-badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: #10b981;
    background: rgba(16, 185, 129, 0.1);
    border: 1px solid rgba(16, 185, 129, 0.3);
    border-radius: 4px;
    padding: 3px 8px;
    display: inline-block;
    margin-left: 8px;
}

.card-title {
    font-size: 1.8rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 8px;
}

.card-desc {
    font-size: 1.05rem;
    line-height: 1.6;
    color: #cbd5e1;
    margin-bottom: 14px;
}

div.stButton > button {
    border-radius: 6px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.85rem !important;
    transition: all 0.25s ease !important;
}

div.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 0 25px rgba(212, 175, 55, 0.4) !important;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# CATÁLOGO DE LAS 16 APLICACIONES
# ============================================================
CATALOGO = [
    {"id": 1, "titulo": "Detector de Objetos (YOLOv5)", "cat": "Visión", "desc": "Detección de 80 clases en tiempo real con filtrado de certeza e IoU.", "rec": "Combínalo con Detector de Presencia para discriminar humanos de objetos."},
    {"id": 2, "titulo": "Nube de Palabras", "cat": "Texto", "desc": "Extracción semántica y representación proporcional de frecuencias léxicas.", "rec": "Pruébalo junto al Analizador de Tono para evaluar el sesgo emocional."},
    {"id": 3, "titulo": "Reconocedor de Dígitos", "cat": "Redes Neuronales", "desc": "Clasificador óptico 0-9 con lienzo ampliado y cálculo probabilístico.", "rec": "Complementa con Tablero de Bocetos para deducir figuras complejas."},
    {"id": 4, "titulo": "Análisis de Imagen con IA", "cat": "Visión Multimodal", "desc": "Descripción contextual detallada de fotografías mediante GPT-4o.", "rec": "Ideal para contrastar la salida de OCR con una interpretación narrativa."},
    {"id": 5, "titulo": "Traductor de Voz a Audio", "cat": "Voz", "desc": "Reconocimiento oral continuo, traducción multilingüe y síntesis vocal.", "rec": "Combínalo con Espejo Mágico si requieres traducir texto impreso."},
    {"id": 6, "titulo": "Detector de Presencia", "cat": "Visión", "desc": "Monitoreo corporal y facial con confirmación estricta y conteo exacto.", "rec": "Útil junto a YOLOv5 para verificación de aforo y posturas."},
    {"id": 7, "titulo": "Espacio de Humor", "cat": "Interacción", "desc": "Lienzo de partículas interactivas con reproducción oral de chistes.", "rec": "Excelente complemento del Compañero de Conversación para distenderte."},
    {"id": 8, "titulo": "Compañero de Conversación", "cat": "Interacción", "desc": "Asistencia empática en español nativo con avatar animado y síntesis oral.", "rec": "Úsalo con Analizador de Tono para reflexionar sobre tu redacción."},
    {"id": 9, "titulo": "Espejo Mágico de Lectura", "cat": "Óptica", "desc": "Extracción de texto impreso con realce CLAHE, traducción y espejo 3D.", "rec": "Enlázalo con Traductor de Voz para alternar entre texto y habla."},
    {"id": 10, "titulo": "Reconocimiento Óptico (Cámara)", "cat": "Óptica", "desc": "Lectura directa por webcam con inversión de contraste y recuento léxico.", "rec": "Útil previo a la carga de documentos extensos en el sistema RAG."},
    {"id": 12, "titulo": "Interfaces Multimodales", "cat": "Interacción", "desc": "Laboratorio de canales sensoriales visuales, auditivos y táctiles.", "rec": "Aporta fundamentos para el diseño sensorial en asistentes virtuales."},
    {"id": 13, "titulo": "Tablero de Bocetos", "cat": "Visión Multimodal", "desc": "Lienzo de dibujo libre asistido por GPT-4o-mini para deducir bocetos.", "rec": "Alternativa creativa frente a la clasificación matemática de dígitos."},
    {"id": 14, "titulo": "Consulta de Documentos PDF", "cat": "Texto", "desc": "Interrogación documental indexada por FAISS mediante generación RAG.", "rec": "Procesa textos extensos tras una visualización inicial con Nube de Palabras."},
    {"id": 15, "titulo": "Analizador de Tono", "cat": "Texto", "desc": "Evaluación de polaridad, subjetividad y trayectoria emocional por oraciones.", "rec": "Optimiza la redacción antes de compartir propuestas formales."},
    {"id": 16, "titulo": "Deducción de Sistemas", "cat": "Redes Neuronales", "desc": "Formalización geométrica y deducción mecanicista de esquemas físicos.", "rec": "Combínalo con Tablero de Bocetos para extrapolar leyes mecánicas."},
    {"id": 17, "titulo": "Generador de Cuentos", "cat": "Visión Multimodal", "desc": "Dibuja un personaje o escena y la IA construirá una narrativa infantil.", "rec": "Ideal para estimular la creatividad narrativa a partir de dibujos."}
]

# ============================================================
# CABECERA Y SEGUIMIENTO DE PROGRESO LÍQUIDO
# ============================================================
st.markdown('<div class="brand-signature">Krov Industries · Directorio</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">Aplicaciones de Inteligencia Artificial.</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-lead">Catálogo unificado de visión artificial, modelos de lenguaje y sistemas multimodales</div>', unsafe_allow_html=True)

# Barra de progreso de flujo de lava
progreso_pct = int((len(st.session_state.visited_apps) / len(CATALOGO)) * 100)
st.markdown(
    f"""
    <div style="max-width: 650px; margin: 0 auto;">
        <div style="display:flex; justify-content:space-between; font-family:'JetBrains Mono'; font-size:0.75rem; margin-bottom:4px;">
            <span style="color:#94a3b8;">APLICACIONES EXPLORADAS</span>
            <span style="color:#d4af37; font-weight:700;">{len(st.session_state.visited_apps)} de {len(CATALOGO)} ({progreso_pct}%)</span>
        </div>
        <div class="lava-progress-bar">
            <div class="lava-progress-fill" style="width: {progreso_pct}%;"></div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Filtro y Búsqueda
c_srch, c_fltr = st.columns([1.5, 1], gap="medium")
with c_srch:
    busqueda = st.text_input("Buscar por función o término:", placeholder="Ej: OCR, voz, PDF, dibujo...", label_visibility="collapsed")
with c_fltr:
    cat_sel = st.selectbox("Categoría:", ["Todas", "Visión", "Voz", "Texto", "Redes Neuronales", "Visión Multimodal", "Interacción", "Óptica"], label_visibility="collapsed")

filtrados = [
    p for p in CATALOGO
    if (cat_sel == "Todas" or p["cat"] == cat_sel)
    and (not busqueda or busqueda.lower() in p["titulo"].lower() or busqueda.lower() in p["desc"].lower())
]

if not filtrados:
    st.info("Sin coincidencias. Restableciendo filtro...")
    filtrados = CATALOGO

st.session_state.carousel_idx = max(0, min(st.session_state.carousel_idx, len(filtrados) - 1))
app_actual = filtrados[st.session_state.carousel_idx]
visitada = app_actual["id"] in st.session_state.visited_apps

# ============================================================
# TARJETA DEL CARRUSEL INTERACTIVO (SIN IMÁGENES)
# ============================================================
badge_visit = '<span class="visited-badge">✓ Explorada</span>' if visitada else ""

st.markdown(
    f"""
    <div class="carousel-card">
        <span class="cat-badge">{app_actual["cat"]}</span>{badge_visit}
        <div class="card-title">{app_actual["titulo"]}</div>
        <div class="card-desc">{app_actual["desc"]}</div>
        <div style="background:rgba(255,255,255,0.04); border-left:3px solid #d4af37; border-radius:4px; padding:10px 14px; font-size:0.92rem; color:#cbd5e1;">
            <b>Recomendación:</b> {app_actual["rec"]}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Navegación del carrusel y botón de explorar
c_ant, c_acc, c_sig = st.columns([1, 1.4, 1])

with c_ant:
    if st.button("← Anterior", use_container_width=True):
        st.session_state.carousel_idx = (st.session_state.carousel_idx - 1) % len(filtrados)
        st.rerun()

with c_acc:
    lbl_btn = "Revisar aplicación" if not visitada else "Revisada (Enlace pendiente)"
    if st.button(lbl_btn, use_container_width=True):
        st.session_state.visited_apps.add(app_actual["id"])
        st.rerun()

with c_sig:
    if st.button("Siguiente →", use_container_width=True):
        st.session_state.carousel_idx = (st.session_state.carousel_idx + 1) % len(filtrados)
        st.rerun()
