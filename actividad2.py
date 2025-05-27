import streamlit as st
import pandas as pd


def main():
    st.title("Plataforma interactiva para el estudio de novas")
    st.header("Actividad 2. Modelando la explosión de una nova")

    st.subheader("¿Qué es una Nova?")
    st.markdown("""
    Durante el siglo XI d.C., en China, las personas que dedicaban 
    su vida a la astronomía observaron una estrella que apareció durante un tiempo
    y luego desapareció. Por esta característica la nombraron “estrella invitada” o 
    “estrella nueva”. Así, a cada estrella nueva que aparecía en el cielo le llamaban “Nova”.
    """)

    st.subheader("Explosiones recurrentes")
    st.markdown("""
    Ahora que la comunidad astronómica tiene más información respecto a la naturaleza de esos
    objetos, sabemos que su aparición se produce por la explosión de una estrella. Actualmente
    se les llama Novas a la explosión que ocurre en estrellas binarias debido a que la estrella
    más masiva “absorbe” gas de su compañera, creando un disco de gas alrededor del sistema, el 
    cual explota cuando ese material alcanza una masa y temperatura crítica.
    """)

    st.markdown("""
    Luego de la explosión, el sistema vuelve a su estado estable, comenzando el ciclo de acreción de gas nuevamente.
    Las novas pueden ser eventos recurrentes, a diferencia de las supernovas, que marcan el fin de una estrella masiva.
    """)

    st.subheader("Curvas de luz y clasificación")
    st.markdown("""
    Para analizar el comportamiento del brillo de las estrellas en función del tiempo, la comunidad
    astronómica utiliza una herramienta gráfica llamada **curva de luz**, la cual representa el brillo de
    un objeto en función del tiempo. Esta herramienta permite clasificar a las novas según la
    tasa de decaimiento de su brillo desde la erupción, usando el parámetro **t₃**: el tiempo que tardan
    en disminuir su brillo en 3 magnitudes.

    La siguiente tabla proporciona la clasificación de las novas de acuerdo a este criterio:
    """)

    # Descomenta si tienes una tabla para mostrar
    # df = pd.read_csv("clasificacion_novas.csv")
    # st.dataframe(df)

    
if __name__=="__main__":
    main()