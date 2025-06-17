import streamlit as st
import pandas as pd
import base64
import matplotlib as plt 

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
def cargar_datos_programador_csv():
    """
    Carga los datos desde un archivo CSV
    """
    archivo = "nova_estudiante.csv"
    try:
        datos = pd.read_csv(nova_estudiante.csv)
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
    buffer.seek(0)

    st.download_button(
        label="Descargar archivo CSV",
        data=buffer,
        file_name=nombre_archivo,
        mime="text/csv",)
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
    menu=st.radio("Selecciona una sección", ["¿Qué es una nova?","Curvas de luz","Clasificación"])



    if menu=="¿Qué es una nova?":
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

    elif menu=="Curvas de luz":
        st.markdown("""
        <p style='color:white;'>
        La curva de luz es una herramienta gráfica, que representa el brillo de
        un objeto en función del tiempo. Esta herramienta permite clasificar a las novas según la
        tasa de decaimiento de su brillo desde la erupción, usando el parámetro **t₃**: el tiempo que tardan
        en disminuir su brillo en 3 magnitudes.
        </p>
        """, unsafe_allow_html=True)

    elif menu=="Clasificación":
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


def main():
    set_background("fondo.png")

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
