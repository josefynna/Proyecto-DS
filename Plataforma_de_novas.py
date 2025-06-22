import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt 
import numpy as np 
import io 

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

import streamlit as st # Asegúrate de que esta línea esté al inicio de tu script

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


    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)


def actividad_1():
    st.markdown("<h2 style='font-family:\"Times New Roman\";color:#cccccc;'>Actividad 1</h2>", unsafe_allow_html=True)


    with st.expander("Observaciones del cielo"):
        st.markdown("""
        <p style='font-family:"Times New Roman";color:#f0f0f0;'>
        Cuando miramos al cielo, observamos muchos objetos brillantes, la mayoría de los cuales son estrellas. No todas las
        estrellas brillan de la misma manera, por lo que es natural preguntarse: ¿existen estrellas que brillan más que otras?¿las estrellas más brillantes están más cerca de la Tierra?
        ¿Cuál es la estrella más cercana a la Tierra? ¿hay más estrellas de las que podemos ver?
        </p>
        <p style='font-family:"Times New Roman"; color:#f0f0f0'>
        Se conoce como <strong>brillo</strong> o <strong>flujo luminoso</strong> de una estrella a la cantidad de luminosidad que viene de un objeto radiante y que llega a la Tierra. De esta forma, el brillo se relaciona con la percepción de qué tan brillante se ve una estrella desde la Tierra. La <em>magnitud aparente</em> nos permite clasificar estrellas a partir de su brillo. Es importante mencionar que la magnitud aparente no entrega información del brillo real del astro, ya que esa característica depende de la distancia y tamaño del objeto.
        </p>
        """, unsafe_allow_html=True)

        st.image("mgnitude.png", caption="Brillo Relativo", use_container_width=True)


    st.markdown("<h3 style='font-family:\"Times New Roman\"; color:#cccccc;'>Nuestro Objetivo</h3>", unsafe_allow_html=True)
    st.markdown("<div style='font-family:\"Times New Roman\";color:#f0f0f0;'>Modelar el comportamiento del brillo en novas reales, clasificar los eventos según su decaimiento (t₃), y permitir su uso en" \
    " clases de matemática y física.</div>", unsafe_allow_html=True)

    datos = cargar_datos_programador_csv()
    if datos is not None:
        st.dataframe(datos)
        descargar_datos_csv(datos)

    


def cargar_datos_programador_csv():
    """
    Carga los datos desde un archivo CSV
    """
    archivo = "nova_estudiante.csv"
    try:
        datos = pd.read_csv("nova_estudiante.csv")
        st.success(f"Datos cargados exitosamente desde {archivo}.")
        return datos
    except FileNotFoundError:
        st.error(f"El archivo '{archivo}' no se encontró. Asegúrate de que esté en la misma carpeta que este script.")
        return None
    except Exception as e:
        st.error(f"Ocurrió un error al cargar los datos: {e}")
        return None
    
    
def descargar_datos_csv(datos, nombre_archivo="nova_estudiante.csv"):
    """
    Permite a los usuarios descargar un archivo CSV.
    """
    buffer = io.StringIO()
    datos.to_csv(buffer, index=False)
    
    # Obtener el contenido del buffer como texto
    contenido_csv = buffer.getvalue()

    st.download_button(
        label="Descargar archivo CSV",
        data=contenido_csv,  # ✅ ahora es un string válido
        file_name=nombre_archivo,
        mime="text/csv"
    )
def simulacion_curva_luz():
    st.markdown("<h3 style='font-family:\"Times New Roman\"; color:#cccccc;'>Simulación de Curva de Luz</h3>", unsafe_allow_html=True)
    st.markdown("""
    <p style='color:white;'>
    Explora cómo la magnitud aparente de una nova varía con el tiempo, utilizando el parámetro t3.
    </p>
    """, unsafe_allow_html=True)

    m_peak = st.slider("Magnitud Aparente Inicial (pico de brillo)", min_value=-5.0, max_value=10.0, value=0.0, step=0.1)
    t3_value = st.slider("Valor de t3 (días para decaer 3 magnitudes)", min_value=1, max_value=200, value=50, step=1)
    tiempo_total = st.slider("Tiempo total de simulación (días)", min_value=10, max_value=500, value=100, step=10)

    # Generar puntos de tiempo
    t = np.linspace(0, tiempo_total, 500)

    # Calcular la magnitud aparente
    magnitud = m_peak + (3 / t3_value) * t

    magnitud[magnitud < m_peak] = m_peak

    # Graficar la curva de luz
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(t, magnitud, color='skyblue', linewidth=2)
    ax.set_xlabel("Tiempo (días)", color='white')
    ax.set_ylabel("Magnitud Aparente", color='white')
    ax.set_title("Curva de Luz de Nova Simulada", color='white')
    ax.invert_yaxis() # La magnitud aparente se invierte: valores más bajos son más brillantes
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_facecolor("#262730") # Fondo del gráfico oscuro
    fig.patch.set_facecolor("#0e1117") # Fondo de la figura oscuro

    # Color de los ticks y labels de los ejes
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.spines['left'].set_color('white')
    ax.spines['bottom'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['top'].set_color('white')


    st.pyplot(fig)

    st.markdown(f"""
    <p style='color:white;'>
    Con una magnitud inicial de <strong>{m_peak}</strong> y un $t_3$ de <strong>{t3_value}</strong> días,
    la nova tardaría <strong>{t3_value}</strong> días en decaer 3 magnitudes,
    alcanzando una magnitud de <strong>{m_peak + 3:.1f}</strong> en ese punto.
    </p>
    """, unsafe_allow_html=True)

def actividad_2():
    
    st.markdown("<h2 style='font-family:\"Times New Roman\"; color:white;'>Actividad 2</h2>", unsafe_allow_html=True)

    # Inicializar el estado de sesión para la sub-navegación de la actividad 2
    if 'act2_section' not in st.session_state:
        st.session_state.act2_section = '¿Qué es una nova?' # Sección por defecto

    # Crear columnas para los botones
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


    st.markdown("---") # Añadir una línea horizontal para separación

    # Mostrar contenido basado en el botón seleccionado
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
        La curva de luz es una herramienta gráfica, que representa el brillo de
        un objeto en función del tiempo. Esta herramienta permite clasificar a las novas según la
        tasa de decaimiento de su brillo desde la erupción, usando el parámetro **t₃**: el tiempo que tardan
        en disminuir su brillo en 3 magnitudes.
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
                descargar_datos_csv(datos, nombre_archivo=archivo_seleccionado)

                # Generar el gráfico de dispersión
                st.markdown(f"<h4 style='color:#cccccc;'>Gráfico de Dispersión para {nova_seleccionada}</h4>", unsafe_allow_html=True)
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.scatter(datos["Tiempo"], datos["Magnitud"], color='lightcoral', s=50, alpha=0.8)
                ax.set_xlabel("Tiempo (días)", color='white')
                ax.set_ylabel("Magnitud Aparente", color='white')
                ax.set_title(f"Curva de Luz de {nova_seleccionada}", color='white')
                ax.invert_yaxis() # Magnitudes más bajas son más brillantes
                ax.grid(True, linestyle='--', alpha=0.7)
                ax.set_facecolor("#262730") # Fondo del gráfico oscuro
                fig.patch.set_facecolor("#0e1117") # Fondo de la figura oscuro

                # Color de los ticks y labels de los ejes
                ax.tick_params(axis='x', colors='white')
                ax.tick_params(axis='y', colors='white')
                ax.spines['left'].set_color('white')
                ax.spines['bottom'].set_color('white')
                ax.spines['right'].set_color('white')
                ax.spines['top'].set_color('white')

                st.pyplot(fig)

            except FileNotFoundError:
                st.warning(f"Archivo {archivo_seleccionado} no encontrado.")
            except Exception as e:
                st.error(f"Ocurrió un error al procesar el archivo {archivo_seleccionado}: {e}")
             
             #pregunta sobre el decaimiento de una nova
        st.markdown("""
        <hr style='border:1px solid #444;'>
        <p style='color:white;'>
        Según la curva de kuz de la nova mostrada, ¿cómo clasificarías su tipo de decaimiento?
        </p>
        """, unsafe_allow_html=True)

        #alternativas(opciones)
        Alternativas = [
            "A) Rapido: pierde su brillo en muy rapidamente en muy pocos dias.",
            "B) Lento: Su brillo disminuye de forma gradual y tarda mas en perder magnitud.",
            "C) muy lento: Su brillo permanece durante una decada o mas antes de comenzar a desvanecerse lentamente."
        ]       
        respuesta_tipo = st.radio(
            "Selecciona el tipo de decaimiento:",
            Alternativas,
            key="pregunta_tipo_decaimiento" 
        )

        if st.button("Verificar tipo de decaimiento", key="boton_decaimiento"):
            if nova_seleccionada == "NOVA Sco 2023" and respuesta_tipo == Alternativas[0]:
                st.success("Correcto, la NOVA Sco 2023 presenta un decaimiento rápido.")
            elif nova_seleccionada == "NOVA Sgr 202331" and respuesta_tipo == Alternativas[0]:
                st.success("Correcto, la NOVA Sgr 202331 presenta un decaimiento rapido.")
            elif nova_seleccionada == "NOVA Cplac" and respuesta_tipo == Alternativas[2]:
                st.success("Correcto, la NOVA Cplac presenta un decaimiento lento.")
            elif nova_seleccionada == "Nova V603" and respuesta_tipo == Alternativas[0]:
                st.succes("Correcto, la NOVA V603 presenta un decaimiento rapido")
            else:
                st.error("Respuesta incorrecta. Observa con mas detalle la curva de luz.")
                st.markdown("""
                <p style='color:white;'>
                Recuerda que un decaimiento rápido se refleja en una caída abrupta del brillo en pocos días (1-100), un decaimiento lento mantiene
                el brillo alto por más tiempo antes de atenuarse (100-150) y un decaimiento mas lento cuando el brillo se mantiene por mas tiempo que la categoria anterior (mayor a 150).
                </p>
                """, unsafe_allow_html=True)

        st.markdown("""
        <p style= 'color:white;'>
        ¿Qué relación existe entre el tiempo y el brillo?
        </p>
        """, unsafe_allow_html=True)

        # Opciones de respuesta
        opciones_respuesta = [
            "A) A medida que pasa el tiempo, el brillo de la nova aumenta constantemente.",
            "B) El brillo de la nova disminuye con el tiempo.",
            "C) No hay una relación clara entre el tiempo y el brillo."
        ]

        # Radio button para que el usuario seleccione una respuesta
        respuesta_usuario = st.radio(
            "Selecciona la opción que mejor describe la relación observada:",
            opciones_respuesta,
            key="pregunta_brillo_tiempo" # Clave única para este widget
        )

        # Lógica para mostrar la retroalimentación
        if st.button("Ver respuesta", key="boton_respuesta_brillo"):
            if respuesta_usuario == opciones_respuesta[1]: # Opción B es la correcta
                st.success("¡Respuesta Correcta!")
                st.markdown("""
                <p style='color:white;'>
                El gráfico de dispersión muestra claramente que, una vez que la nova "explota", el brillo de esta disminuye confome el tiempo
                transcurrido, la relación matemática que existe entre la magnitud aparente y el teimpo transcurrido es logarítmica, es decir, 
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


    st.title("Plataforma Interactiva para el estudio de Novas")

    # Usar st.session_state para mantener el estado de la página seleccionada
    if 'page' not in st.session_state:
        st.session_state.page = 'Actividad 1' # Página inicial

    col1, col2 = st.columns(2) # Puedes ajustar el número de columnas según cuántos botones quieras

    with col1:
        if st.button("Actividad 1: Brillo Estelar"):
            st.session_state.page = 'Actividad 1'

    with col2:
        if st.button("Actividad 2: Novas"):
            st.session_state.page = 'Actividad 2'

    # Mostrar el contenido según la página seleccionada
    if st.session_state.page == 'Actividad 1':
        actividad_1()
    elif st.session_state.page == 'Actividad 2':
        actividad_2()


if __name__ == "__main__":
    main()




    # Descomenta si tienes una tabla para mostrar
    # df = pd.read_csv("clasificacion_novas.csv")
    # st.dataframe(df)




