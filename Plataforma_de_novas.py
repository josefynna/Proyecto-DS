import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import numpy as np
import io
import random
import openpyxl 



def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def set_custom_styles():
    custom_css = """
    <style>
    /* Estilos para el texto "Selecciona una sección" (radio button parent) */
    /* La clase br351g era para el 'p' de "Selecciona una sección" */
    .st-emotion-cache-br351g p {
        color: white !important;
    }

    /* Estilos para el texto de las opciones de radio (¿Qué es una nova?, Curvas de luz, Clasificación) */
    /* Apuntamos al div padre con la clase stRadio para mayor especificidad y al p con la clase 10c9vv9 */
    .stRadio .st-emotion-cache-10c9vv9 p {
        color: white !important;
    }

    /* Estilos para los encabezados de los expanders (Observaciones del cielo, ¿Qué causa la explosión?) */
    .stExpanderHeader {
        color: white !important;
    }

    /* Estilos para los títulos (incluyendo los generados por st.title()) */
    h1, .stApp h1, .block-container h1, .css-10trblm {
        color: white !important;
    }

    /* --- SOLUCIÓN REFORZADA PARA BOTONES DE ACTIVIDAD (Actividad 1, Actividad 2) --- */

    /* Apunta al botón Streamlit en general, para el fondo y el borde */
    /* stButton es una clase más genérica que engloba el botón */
    .stButton > button {
        background-color: rgb(30, 30, 40) !important; /* Fondo oscuro del botón */
        border: 1px solid rgba(250, 250, 250, 0.2) !important; /* Borde sutil */
        border-radius: 0.5rem !important;
        padding: 0.25rem 0.75rem !important;
        line-height: 1.6 !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        margin: 0px !important;
        width: 100% !important;
        /* IMPORTANTE: No establecemos aquí el color del texto, lo haremos más abajo */
    }

    /* Estilo al pasar el ratón por encima (hover) para los botones de actividad */
    .stButton > button:hover {
        background-color: rgb(50, 50, 60) !important; /* Un poco más claro al pasar el ratón */
    }

    /* CRUCIAL: Apuntar al texto DENTRO del botón de actividad */
    /* Esta regla es MUY ESPECÍFICA para el párrafo 'p' que contiene el texto del botón,
       que, como vimos, tiene la clase 10c9vv9 y está dentro de un 'button' que a su vez
       está dentro de un '.stButton' */
    .stButton > button .st-emotion-cache-10c9vv9 p {
        color: white !important; /* ¡FUERZA EL TEXTO DEL BOTÓN A SER BLANCO! */
    }

    /* Intento adicional si el anterior no funciona: apunta directamente a la etiqueta */
    .stButton > button p.st-emotion-cache-10c9vv9 {
        color: white !important; /* Intento alternativo para el texto del botón */
    }

    /* FIX: Textos de st.write y st.markdown que no toman el color */
    /* Target common Streamlit text elements */
    .stMarkdown p, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown span,
    .stText p, .stAlert p, .stSuccess p, .stError p, .stWarning p,
    .stInfo p, .stForm > div > div > label > div > span {
        color: white !important;
    }

    /* Specific fix for radio button labels which might be rendered differently */
    .stRadio label > div > span {
        color: white !important;
    }

    /* Specific fix for st.subheader in Actividad 1 and similar */
    .stApp .st-emotion-cache-1g88p9b h3 { /* This is a common class for st.subheader */
        color: white !important;
    }

    /* Specific fix for the text input label in Actividad 1 */
    .stTextInput label p {
        color: white !important;
    }

    /* ************************************************* */
    /* REGLAS PARA TÍTULOS ESPECÍFICOS DE ACTIVIDAD 1 */
    /* ************************************************* */

    /* Para st.header (que usualmente se renderiza como h1) */
    .block-container h1 {
        color: white !important;
    }

    /* Para st.subheader (que usualmente se renderiza como h3) */
    .block-container h3 {
        color: white !important;
    }

    /* Regla más general para texto dentro del contenedor principal de la aplicación */
    .stApp div[data-testid="stVerticalBlock"] h1,
    .stApp div[data-testid="stVerticalBlock"] h2,
    .stApp div[data-testid="stVerticalBlock"] h3,
    .stApp div[data-testid="stVerticalBlock"] p,
    .stApp div[data-testid="stVerticalBlock"] span {
        color: white !important;
    }

    /* ************************************************* */
    /* NUEVAS REGLAS PARA BOTONES DE DESCARGA */
    /* ************************************************* */
    /* Apuntamos al botón que contiene el data-testid="stDownloadButton" */
    div[data-testid="stDownloadButton"] > button {
        background-color: rgb(40, 40, 50) !important; /* Un color de fondo oscuro para el botón de descarga */
        color: #cccccc !important; /* Un gris claro para el texto del botón de descarga */
        border: 1px solid rgba(250, 250, 250, 0.2) !important; /* Borde sutil */
    }

    /* Efecto hover para el botón de descarga */
    div[data-testid="stDownloadButton"] > button:hover {
        background-color: rgb(60, 60, 70) !important; /* Ligeramente más claro al pasar el ratón */
        color: white !important; /* Texto blanco al pasar el ratón */
    }

    /* Para asegurar que el icono dentro del botón de descarga también sea visible */
    div[data-testid="stDownloadButton"] > button .st-emotion-cache-10c9vv9 svg {
        fill: #cccccc !important; /* Color del icono */
    }

    /* Para el texto dentro del botón de descarga */
    div[data-testid="stDownloadButton"] > button p {
        color: #cccccc !important; /* Asegura que el texto sea gris claro */
    }
    div[data-testid="stDownloadButton"] > button p:hover {
        color: white !important; /* Texto blanco al pasar el ratón */
    }

    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

def add_logo(logo_path):
    """
    Agrega un logo redondo en la esquina superior derecha de la aplicación Streamlit.
    """
    with open(logo_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    
    st.markdown(
        f"""
        <style>
            .logo-container {{
                position: fixed;
                top: 60px;   /* ¡Aumentado a 60px para bajarlo más! */
                right: 40px; /* Mantenemos 40px desde la derecha */
                z-index: 1000; 
            }}
            .logo-container img {{
                width: 100px;  
                height: 100px; 
                border-radius: 50%; 
                object-fit: cover; 
            }}
        </style>
        <div class="logo-container">
            <img src="data:image/png;base64,{encoded_string}">
        </div>
        """,
        unsafe_allow_html=True
    )
def actividad_1():
    """
    Actividad 1: Brillo Estelar
    Se divide en subsecciones manejadas por botones.
    """

    # 1) Acceso a los datos
    datos = st.session_state.get('datos')
    if datos is None:
        st.error("No se encontraron datos en st.session_state. Carga el CSV antes de continuar.")
        return

    # 2) Título general
    st.markdown(
        "<h2 style='font-family:Times New Roman; color:#cccccc;'>"
        "Actividad 1: Brillo Estelar</h2>",
        unsafe_allow_html=True
    )

    # 3) Crear/recuperar el estado de la subsección
    if 'subsec_a1' not in st.session_state:
        st.session_state.subsec_a1 = 'Introducción'

    # 4) Menú tipo “botonera” (puedes cambiar los nombres o el número de botones)
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Introducción"):
            st.session_state.subsec_a1 = 'Introducción'

    with col2:
        if st.button("Graficando"):
            st.session_state.subsec_a1 = 'Graficando'

    with col3:
        if st.button("Interpretación de los Datos"):
            st.session_state.subsec_a1 = 'Interpretación de los Datos'

    # 5) Mostrar la subsección correspondiente
    subsec = st.session_state.subsec_a1

    if subsec == 'Introducción':
        st.subheader("Introducción")
        st.write("Cuando miramos al cielo, observamos muchos objetos brillantes, la mayoría de los cuales son estrellas. No todas las estrellas brillan de la misma manera, por lo que es natural preguntarse: ¿existen estrellas que brillan más que otras?¿las estrellas más brillantes están más cerca de la Tierra?¿Cuál es la estrella más cercana a la Tierra? ¿hay más estrellas de las que podemos ver?")
        with st.expander("Explicación teórica", expanded=True):
            st.markdown("""
        <p style='font-family:"Times New Roman"; color:#f0f0f0'>
        Se conoce como <strong>brillo</strong> o <strong>flujo luminoso</strong> de una estrella a la cantidad de luminosidad que emite un objeto radiante que llega a la Tierra.  
        La <em>magnitud aparente</em> nos permite clasificar estrellas según ese brillo aparente.  
        Sin embargo, no refleja el brillo real, que depende de la distancia y el tamaño del astro.
        </p>
        """, unsafe_allow_html=True)
        
        # --- CAMBIO 5: Descarga a XLSX ---
        # Convertir DataFrame a un buffer de Bytes para XLSX
        output = io.BytesIO()
        datos.to_excel(output, index=False, engine='openpyxl')
        processed_data = output.getvalue()
        
        st.download_button(
            label="⬇️ Descargar Datos (XLSX)",
            data=processed_data,
            file_name="nova_estudiante.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        # --- FIN CAMBIO 5 ---

        st.image("mgnitude.png", caption="Brillo Relativo", use_container_width=True)

    elif subsec == 'Graficando':
        st.header("Visualizaciones")
        st.markdown("Utilizando los datos que te entregamos previamente, construye un gráfico de dispersión considerando como variable dependiente el brillo y como variable independiente la magnitud aparente.)")
        fig, ax = plt.subplots()
        # --- HOMOGENEIZAR GRÁFICOS: COLORES Y FONDOS ---
        # Colores de los puntos: ya 'skyblue'
        ax.scatter(datos['magnitud'], datos['flujo'], marker='*', alpha=0.7, color='skyblue') 
        
        # Fondo del área del gráfico (plot area)
        ax.set_facecolor("#262730") # Un gris oscuro
        # Fondo de la figura completa (fuera del área del gráfico)
        fig.patch.set_facecolor("#0e1117") # Un negro muy oscuro
        
        # Color de las etiquetas de los ejes, títulos y ticks
        ax.set_xlabel("Magnitud Aparente (mag)", color='white') 
        ax.set_ylabel(r"Flujo Observado (W/$\mathrm{m}^2$)", color='white')
        ax.set_title("Curva de luz: Flujo vs. Magnitud", color='white')
        
        # Color de los ticks de los ejes
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        
        # Color de las líneas de los bordes del gráfico
        ax.spines['left'].set_color('white')
        ax.spines['bottom'].set_color('white')
        ax.spines['right'].set_color('white')
        ax.spines['top'].set_color('white')
        # --- FIN HOMOGENEIZAR GRÁFICOS ---
        
        st.pyplot(fig)

        with st.expander("Pregunta 1", expanded=True):
                st.markdown("### ¿Cuál es la relación entre el brillo y la magnitud aparente?")
        opciones = [
        "A) Mientras mayor es el brillo, mayor es la magnitud aparente.",
        "B) Mientras menor es el brillo, mayor es la magnitud aparente.",
        "C) No hay relación entre el brillo y la magnitud aparente.",
        "D) Brillo y magnitud aparente son equivalentes."
    ]
        seleccion = st.radio("Selecciona una opción:", opciones, key="alternativas_brillo_magnitud")

        # Verificación de la respuesta
        if st.button("Verificar respuesta"):
            if seleccion == opciones[1]:  # Respuesta correcta: B
                st.success("¡Correcto! Mientras menor es el brillo, mayor es la magnitud aparente.")
            else:
                st.error("Respuesta incorrecta. Intenta nuevamente. Recuerda que la magnitud aparente es inversamente proporcional al brillo.")
        
        comentario_usuario = st.text_input(
        label="Considerando las funciones trabajadas en clases, ¿Con qué función crees podrías modelar esta situación? Argumenta tu respuesta considerando características del gráfico.",
        placeholder="Escribe aquí...",
        key="comentario_usuario_graficos"
    )

    # Verificar si el usuario escribió algo
        if comentario_usuario:
            st.markdown("Respuesta: La relación entre el flujo y magnitud aparente está definida por una función logarítmica inversa, dado que la relación no es lineal y cuando una variable aumenta la otra disminuye. ")
        

    elif subsec == 'Interpretación de los Datos':
        st.subheader("Datos en tabla")
        if {'astro', 'magnitud', 'flujo'}.issubset(datos.columns):
            st.dataframe(datos[['astro', 'magnitud', 'flujo']])
        else:
            st.warning("No se encontró la columna 'astro' en los datos.")
        estrella_mas_brillo = datos.loc[datos['flujo'].idxmax(), 'astro']
        estrella_menos_brillo = datos.loc[datos['flujo'].idxmin(), 'astro']

        opciones_mas_brillo = random.sample(datos['astro'].tolist(), k=3)  # 3 opciones adicionales
        if estrella_mas_brillo not in opciones_mas_brillo:
            opciones_mas_brillo.append(estrella_mas_brillo)  # Asegurarse de incluir la respuesta correcta
        random.shuffle(opciones_mas_brillo)

        opciones_menos_brillo = random.sample(datos['astro'].tolist(), k=3)  # 3 opciones adicionales
        if estrella_menos_brillo not in opciones_menos_brillo:
            opciones_menos_brillo.append(estrella_menos_brillo)  # Asegurarse de incluir la respuesta correcta
        random.shuffle(opciones_menos_brillo)

        st.markdown("### Pregunta 2: ¿Cuál estrella tiene más brillo?")
        respuesta_mas_brillo = st.radio("Selecciona la estrella más brillante:", opciones_mas_brillo, key="estrella_mas_brillo")

    # Verificación de la respuesta
        if st.button("Verificar respuesta de más brillo"):
            if respuesta_mas_brillo == estrella_mas_brillo:
                st.success(f"¡Correcto! La estrella más brillante es {estrella_mas_brillo}.")
            else:
                st.error(f"Incorrecto. La estrella más brillante es {estrella_mas_brillo}.")

    # Pregunta: ¿Qué estrella tiene menos brillo?
        st.markdown("### Pregunta 3: ¿Cuál estrella tiene menos brillo?")
        respuesta_menos_brillo = st.radio("Selecciona la estrella menos brillante:", opciones_menos_brillo, key="estrella_menos_brillo")

    # Verificación de la respuesta
        if st.button("Verificar respuesta de menos brillo"):
            if respuesta_menos_brillo == estrella_menos_brillo:
                st.success(f"¡Correcto! La estrella menos brillante es {estrella_menos_brillo}.")
            else:
                st.error(f"Incorrecto. La estrella menos brillante es {estrella_menos_brillo}.")
        st.markdown("""
        <h4 style='color:white;'>Clasificación según Hiparco</h4>
        <p style='color:white;'>
        Hiparco categorizó a las estrellas según el brillo observado. Utilizó la <strong>magnitud aparente</strong> para crear seis categorías, 
        mucho antes de que Norman Pogson descubriera que había una relación matemática entre ellas. La siguiente tabla muestra 
        la categorización observada:
        </p>
        """, unsafe_allow_html=True)

    # Tabla de Hiparco
        hiparco_df = pd.DataFrame({
    "Magnitud": [1, 2, 3, 4, 5, 6],
    "Factor de Brillo": [2.52, 6.310, 15.851, 39.818, 100.022, 251.257]
})
        st.dataframe(hiparco_df, use_container_width=True)

def descargar_datos_xlsx(datos, nombre_archivo="datos_nova.xlsx"):
    """
    Permite a los usuarios descargar un archivo XLSX.
    """
    output = io.BytesIO()
    datos.to_excel(output, index=False, engine='openpyxl')
    processed_data = output.getvalue()
    st.download_button(
        label="⬇️ Descargar Datos (XLSX)",
        data=processed_data,
        file_name=nombre_archivo,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

def simulacion_curva_luz():
    st.markdown("<h3 style='font-family:\"Times New Roman\"; color:#cccccc;'>Simulación de Curva de Luz</h3>", unsafe_allow_html=True)
    
    st.markdown("""
    <p style='color:white;'>
    Explora cómo la magnitud aparente de una nova varía con el tiempo, utilizando el parámetro t3.
    """, unsafe_allow_html=True)

    m_peak = st.slider("Magnitud Aparente Inicial (pico de brillo)", min_value=-5.0, max_value=10.0, value=0.0, step=0.1)
    t3_value = st.slider("Valor de t3 (días para decaer 3 magnitudes)", min_value=1, max_value=200, value=50, step=1)
    tiempo_total = st.slider("Tiempo total de simulación (días)", min_value=10, max_value=500, value=100, step=10)

    t = np.linspace(0, tiempo_total, 500)
    
    if t3_value > 0: 
        decay_rate_coefficient = 3.0 / np.log10(t3_value + 1)
    else: 
        decay_rate_coefficient = 0 

    magnitud = m_peak + decay_rate_coefficient * np.log10(t + 1)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(t, magnitud, color='skyblue', linewidth=2)
    
    # --- HOMOGENEIZAR GRÁFICOS: COLORES Y FONDOS ---
    ax.set_xlabel("Tiempo (días)", color='white') 
    ax.set_ylabel("Magnitud Aparente (mag)", color='white')
    ax.set_title("Curva de Luz de Nova Simulada", color='white')
    ax.invert_yaxis() 
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Fondo del área del gráfico
    ax.set_facecolor("#262730") 
    # Fondo de la figura completa
    fig.patch.set_facecolor("#0e1117") 

    # Color de los ticks y labels de los ejes
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    
    # Color de las líneas de los bordes del gráfico
    ax.spines['left'].set_color('white')
    ax.spines['bottom'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['top'].set_color('white')
    # --- FIN HOMOGENEIZAR GRÁFICOS ---

    st.pyplot(fig)

    st.markdown(f"""
    <p style='color:white;'>
    Con una magnitud inicial de <strong>{m_peak}</strong> y un t3 de <strong>{t3_value}</strong> días,
    la nova tardaría <strong>{t3_value}</strong> días en decaer 3 magnitudes,
    alcanzando una magnitud de <strong>{m_peak + 3:.1f}</strong> en ese punto.
    </p>
    """, unsafe_allow_html=True)

def actividad_2():
    
    st.markdown("<h2 style='font-family:\"Times New Roman\"; color:white;'>Actividad 2</h2>", unsafe_allow_html=True)

    if 'act2_section' not in st.session_state:
        st.session_state.act2_section = '¿Qué es una nova?' 

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("¿Qué es una nova?", key="nova_que"):
            st.session_state.act2_section = '¿Qué es una nova?'
    with col2:
        if st.button("Curvas de luz", key="nova_curva"):
            st.session_state.act2_section = 'Curvas de luz'
    with col3:
        if st.button("Clasificación", key="nova_clasificacion"):
            st.session_state.act2_section = 'Clasificación'

    with col4:
        if st.button("Actividad",key="act_nova"):
            st.session_state.act2_section="Actividad"


    st.markdown("---") 

    if st.session_state.act2_section == "¿Qué es una nova?":
         st.markdown("""
          <p style='color:white;'>
         Durante el siglo XI d.C., en China, las personas que dedicaban
         su vida a la astronomía observaron una estrella que apareció durante un tiempo
         y luego desapareció. Por esta característica la nombraron “estrella invitada” o
         “estrella nueva”. Así, a cada estrella nueva que aparecía en el cielo le llamaban “Nova”. Hoy sabemos
         que su aparición se debe a una explosión de una estrellas binarias.
        </p>
         """,unsafe_allow_html=True)
         with st.expander("¿Qué causa la explosión?"):
              st.markdown("""
              <p style='color:white;'>
              La estrella más masiva “absorbe” gas de su compañera, creando un disco de gas alrededor del sistema, el
              cual explota cuando ese material alcanza una masa y temperatura crítica.
              </p>
              """,unsafe_allow_html=True )

              st.markdown("""
              <p style='color:white;'>
              Luego de la explosión, el sistema vuelve a su estado estable, comenzando el ciclo de acreción de gas nuevamente.
              Las novas pueden ser eventos recurrentes, a diferencia de las supernovas, que marcan el fin de una estrella masiva.
             </p>
              """,unsafe_allow_html=True )

    elif st.session_state.act2_section == "Curvas de luz":
        st.markdown("""
        <p style='color:white;'>
        Una <strong>curva de luz</strong> es un gráfico que muestra cómo el brillo de un objeto celeste, como una nova, 
        cambia con el tiempo. Para las novas, es común observar un aumento rápido en el brillo seguido de un decaimiento 
        más gradual. El parámetro <strong>t3</strong> es crucial para clasificar las novas, ya que representa 
        el tiempo (en días) que tarda la nova en disminuir su brillo en 3 magnitudes desde su pico máximo.
        </p>
        </p>
        """, unsafe_allow_html=True)

        simulacion_curva_luz()


    elif st.session_state.act2_section == "Clasificación":
        st.markdown("""
        <p style='color:white;'>
        Clasificamos de la siguiente manera:
        </p>

        <table style='color:white;'>
            <tr><th>Categoría</th><th>Denominación</th><th>t₃ decaimiento (días)</th></tr>
            <tr><td>Muy lenta</td><td>Nc</td><td>>150</td></tr>
            <tr><td>Lenta</td><td>Nb</td><td>100–150</td></tr>
            <tr><td>Rápida</td><td>Na</td><td>1–100</td></tr>
        </table>
        """, unsafe_allow_html=True)

    elif st.session_state.act2_section=="Actividad":
        st.markdown("""
        <p style= 'color:white;'>
        Usando los datos de que se entregan a continuación, constuye un gráfico de dispersión considerando como variable 
        dependiente la magnitud aparente y como variable independiente el tiempo desde erupción.
        </p>
        """, unsafe_allow_html=True)

        archivos = {
            "NOVA Cplac": "NOVA_Cplac.csv",
            "NOVA Sco 2023": "NOVA_Sco 2023.csv",
            "NOVA Sgr 202331": "NOVA_Sgr20231.csv",
            "NOVA V603": "NOVA_V603.csv"
        }

        
        # Permitir al usuario seleccionar una Nova
        nova_seleccionada = st.selectbox(
            "Selecciona una Nova para graficar:",
            list(archivos.keys())
        )

        if nova_seleccionada:
            archivo_seleccionado = archivos[nova_seleccionada]
            st.markdown(f"<h4 style='color:#cccccc;'>Datos de {nova_seleccionada}</h4>", unsafe_allow_html=True)
            try:
                datos = pd.read_csv(archivo_seleccionado, sep=';', usecols=[0, 1], names=["Tiempo", "Magnitud"], skiprows=1)
                datos["Tiempo"] = datos["Tiempo"].str.replace(',', '.', regex=False).astype(float)
                datos["Magnitud"] = datos["Magnitud"].str.replace(',', '.', regex=False).astype(float)

                st.dataframe(datos)
                
                descargar_datos_xlsx(datos, nombre_archivo=f"{nova_seleccionada.replace(' ', '_')}.xlsx")

                # Generar el gráfico de dispersión
                st.markdown(f"<h4 style='color:#cccccc;'>Gráfico de Dispersión para {nova_seleccionada}</h4>", unsafe_allow_html=True)
                fig, ax = plt.subplots(figsize=(10, 6))
                # --- HOMOGENEIZAR GRÁFICOS: COLORES Y FONDOS ---
                ax.scatter(datos["Tiempo"], datos["Magnitud"], color='skyblue', s=50, alpha=0.8) 
                
                # Fondo del área del gráfico
                ax.set_facecolor("#262730") 
                # Fondo de la figura completa
                fig.patch.set_facecolor("#0e1117") 

                # Color de las etiquetas de los ejes, títulos y ticks
                ax.set_xlabel("Tiempo (días)", color='white')
                ax.set_ylabel("Magnitud Aparente (mag)", color='white')
                ax.set_title(f"Curva de Luz de {nova_seleccionada}", color='white')
                ax.invert_yaxis() 
                ax.grid(True, linestyle='--', alpha=0.7)
                
                # Color de los ticks de los ejes
                ax.tick_params(axis='x', colors='white')
                ax.tick_params(axis='y', colors='white')
                
                # Color de las líneas de los bordes del gráfico
                ax.spines['left'].set_color('white')
                ax.spines['bottom'].set_color('white')
                ax.spines['right'].set_color('white')
                ax.spines['top'].set_color('white')
                # --- FIN HOMOGENEIZAR GRÁFICOS ---

                st.pyplot(fig)

            except FileNotFoundError:
                st.warning(f"Archivo {archivo_seleccionado} no encontrado.")
            except Exception as e:
                st.error(f"Ocurrió un error al procesar el archivo {archivo_seleccionado}: {e}")
             
             #pregunta sobre el decaimiento de una nova
        st.markdown("""
        <hr style='border:1px solid #444;'>
        <p style='color:white;'>
        Según la curva de luz de la nova mostrada, ¿cómo clasificarías su tipo de decaimiento?
        </p>
        """, unsafe_allow_html=True)

        Alternativas = [
            "A) Rápido: pierde su brillo muy rápidamente en pocos días.", 
            "B) Lento: Su brillo disminuye de forma gradual y tarda más en perder magnitud.", 
            "C) Muy lento: Su brillo permanece durante una década o más antes de comenzar a desvanecerse lentamente." 
        ]       
        respuesta_decaimiento = st.radio(
            "Selecciona el tipo de decaimiento:",
            Alternativas,
            key="pregunta_tipo_decaimiento" 
        )
        if st.button("Verificar tipo de decaimiento", key="boton_decaimiento"):
            if nova_seleccionada == "NOVA Sco 2023" and respuesta_decaimiento == Alternativas[0]:
                st.success("Correcto")
                st.markdown("<p style='color:white;'>Si bien la curva varía, al principio la curva desciende bruscamente por lo que se clasifica como Rápida.</p>", unsafe_allow_html=True) 
            elif nova_seleccionada == "NOVA Sgr 202331" and respuesta_decaimiento == Alternativas[1]: # Corregida la respuesta esperada a "Lento"
                st.success("Correcto") # Si ahora es la correcta
                st.markdown("<p style='color:white;'>El gráfico muestra un descenso gradual del brillo, por lo que se clasifica como Lenta.</p>", unsafe_allow_html=True) # Mensaje de éxito para "Lento"
            elif nova_seleccionada == "NOVA Cplac" and respuesta_decaimiento == Alternativas[2]:
                st.success("Correcto")
                st.markdown("<p style='color:white;'>El gráfico muestra un descenso gradual del brillo, extendido en el tiempo, clasificándose como Muy Lenta.</p>", unsafe_allow_html=True) 
            elif nova_seleccionada == "NOVA V603" and respuesta_decaimiento == Alternativas[0]:
                st.success("Correcto")
                st.markdown("<p style='color:white;'>Se observa una caída brusca de brillo después del pico de la curva de luz.</p>", unsafe_allow_html=True)

            else:
                st.error("Respuesta incorrecta. Observa con más detalle la curva de luz.") 
                st.markdown("""
                <p style='color:white;'>
                Recuerda que un decaimiento rápido se refleja en una caída abrupta del brillo en pocos días (1-100), un decaimiento lento mantiene
                el brillo alto por más tiempo antes de atenuarse (100-150) y un decaimiento muy lento cuando el brillo se mantiene por mas tiempo que la categoría anterior (mayor a 150).
                </p>
                """, unsafe_allow_html=True) 

        st.markdown("""
        <p style= 'color:white;'>
        ¿Qué relación existe entre el tiempo y el brillo?
        </p>
        """, unsafe_allow_html=True)

        opciones_respuesta = [
            "A) A medida que pasa el tiempo, el brillo de la nova aumenta constantemente.",
            "B) El brillo de la nova disminuye con el tiempo.",
            "C) No hay una relación clara entre el tiempo y el brillo."
        ]

        respuesta_usuario = st.radio(
            "Selecciona la opción que mejor describe la relación observada:",
            opciones_respuesta,
            key="pregunta_brillo_tiempo" 
        )

        if st.button("Ver respuesta", key="boton_respuesta_brillo"):
            if respuesta_usuario == opciones_respuesta[1]: 
                st.success("¡Respuesta Correcta!")
                st.markdown("""
                <p style='color:white;'>
                El gráfico de dispersión muestra claramente que, una vez que la nova "explota", el brillo de esta disminuye conforme el tiempo
                transcurrido. La relación matemática que existe entre la magnitud aparente y el tiempo transcurrido es logarítmica, es decir, 
                el brillo decrece de forma logarítmica.
                </p>
                """, unsafe_allow_html=True) 
            else:
                st.error("Respuesta Incorrecta. Inténtalo de nuevo.")
                st.markdown("""
                <p style='color:white;'>
                Observa con atención el eje Y (Magnitud Aparente) del gráfico. Recuerda que en astronomía,
                los valores más bajos de magnitud significan un objeto más brillante, y los valores más altos
                significan un objeto menos brillante. Mira cómo cambian los puntos a medida que el tiempo (eje X) avanza.
                </p>
                """, unsafe_allow_html=True)



def main():
    set_background("fondo.png")
    set_custom_styles()
    add_logo("ciras.jpg") 

    st.title("Plataforma Interactiva para el estudio de Novas")

    # Modificado para cargar datos solo si no existen y manejar errores
    if 'datos' not in st.session_state:
        try:
            st.session_state.datos = pd.read_csv("nova_estudiante.csv")
            st.success("Datos iniciales cargados exitosamente.")
        except FileNotFoundError:
            st.error("Error: El archivo 'nova_estudiante.csv' no se encontró. Asegúrate de que esté en el mismo directorio que tu script.")
            st.session_state.datos = None # Asegurarse de que sea None si hay un error
        except Exception as e:
            st.error(f"Ocurrió un error al cargar los datos iniciales: {e}")
            st.session_state.datos = None


    if 'page' not in st.session_state:
        st.session_state.page = 'Actividad 1'  

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Actividad 1: Brillo Estelar"):
            st.session_state.page = 'Actividad 1'

    with col2:
        if st.button("Actividad 2: Novas"):
            st.session_state.page = 'Actividad 2'

    if st.session_state.page == 'Actividad 1':
        # Solo llama a actividad_1 si los datos se cargaron correctamente
        if st.session_state.datos is not None:
            actividad_1()
        else:
            st.warning("No se pudieron cargar los datos para la Actividad 1. Por favor, verifica el archivo 'nova_estudiante.csv'.")

    elif st.session_state.page == 'Actividad 2':
        actividad_2()


if __name__ == "__main__":
    main()




