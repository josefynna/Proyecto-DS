import streamlit as st
import pandas as pd




def actividad_1():
    st.markdown("<h1 style='font-family:\"Times New Roman\";'>Plataforma interactiva para el estudio de novas</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-family:\"Times New Roman\";'>Actividad 1</h2>", unsafe_allow_html=True)

    with st.expander("Observaciones del cielo"):
        st.markdown("""
        <p style='font-family:"Times New Roman";'>
        Cuando miramos al cielo, observamos muchos objetos brillantes, la mayoría de los cuales son estrellas. No todas las 
        estrellas brillan de la misma manera, por lo que es natural preguntarse: ¿existen estrellas que brillan más que otras?¿las estrellas más brillantes están más cerca de la Tierra?
        ¿Cuál es la estrella más cercana a la Tierra? ¿hay más estrellas de las que podemos ver?
        </p>
        <p style='font-family:"Times New Roman";'>
        Se conoce como <strong>brillo</strong> o <strong>flujo luminoso</strong> de una estrella a la cantidad de luminosidad que viene de un objeto radiante y que llega a la Tierra. De esta forma, el brillo se relaciona con la percepción de qué tan brillante se ve una estrella desde la Tierra. La <em>magnitud aparente</em> nos permite clasificar estrellas a partir de su brillo. Es importante mencionar que la magnitud aparente no entrega información del brillo real del astro, ya que esa característica depende de la distancia y tamaño del objeto.
        </p>
        """, unsafe_allow_html=True)

    st.markdown("<h3 style='font-family:\"Times New Roman\"; color:#444;'>Nuestro Objetivo</h3>", unsafe_allow_html=True)
    st.markdown("<div style='font-family:\"Times New Roman\";'>Modelar el comportamiento del brillo en novas reales, clasificar los eventos según su decaimiento (t₃), y permitir su uso en" \
    " clases de matemática y física.</div>", unsafe_allow_html=True)




def actividad_2():
    st.header("Actividad 2. Modelando la explosión de una nova")
    menu=st.radio("Selecciona una sección", ["¿Qué es una nova?","Curvas de luz","Clasificación"])

    if menu=="¿Qué es una nova?":
         st.markdown("""
         Durante el siglo XI d.C., en China, las personas que dedicaban 
         su vida a la astronomía observaron una estrella que apareció durante un tiempo
         y luego desapareció. Por esta característica la nombraron “estrella invitada” o 
         “estrella nueva”. Así, a cada estrella nueva que aparecía en el cielo le llamaban “Nova”. Hoy sabemos
         que su aparición se debe a una explosión de una estrellas binarias.
         """) 
         with st.expander("¿Qué causa la explosión?"):
              st.markdown("""
              La estrella más masiva “absorbe” gas de su compañera, creando un disco de gas alrededor del sistema, el 
              cual explota cuando ese material alcanza una masa y temperatura crítica.
              """)

              st.markdown("""
              Luego de la explosión, el sistema vuelve a su estado estable, comenzando el ciclo de acreción de gas nuevamente.
              Las novas pueden ser eventos recurrentes, a diferencia de las supernovas, que marcan el fin de una estrella masiva.
              """)
         
    
    elif menu=="Curvas de luz":
        st.markdown("""
        La curva de luz es una herramienta gráfica, que representa el brillo de
        un objeto en función del tiempo. Esta herramienta permite clasificar a las novas según la
        tasa de decaimiento de su brillo desde la erupción, usando el parámetro **t₃**: el tiempo que tardan
        en disminuir su brillo en 3 magnitudes.
        """)

    elif menu=="Clasificación":
        st.markdown("""
        Clasificamos de la siguiente manera 
                    
        | Categoría   | Denominación | t₃ decaimineto (días) |
        |-------------|--------------|-----------------------|
        | Muy lenta   |     Nc       | >150                  |
        | Lenta       |     Nb       | 100-150               |
        | Rápida      |     Na       | 1-100                 |
        
                    """)


def main():
    st.sidebar.title("Navegación")
    seleccion=st.sidebar.radio("Elige una actividad", ["Actividad 1: Brillo Estelar", "Actividad 2: Novas"])
    
    if seleccion.startswith("Actividad 1"):
       actividad_1()

    else:
        actividad_2()
  




    # Descomenta si tienes una tabla para mostrar
    # df = pd.read_csv("clasificacion_novas.csv")
    # st.dataframe(df)

    
if __name__=="__main__":
    main()