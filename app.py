import streamlit as st
"""
def main():
    st.markdown("<h1 style='font-family:\"Times New Roman\";'>Proyecto de desarrollo de software</h1>", unsafe_allow_html=True)

    st.markdown("<h2 style='font-family:\"Times New Roman\";'>Actividad 1</h2>", unsafe_allow_html=True)

    st.text("Cuando miramos al cielo, observamos muchos objetos brillantes, la mayoría de los cuales son estrellas. No todas las estrellas brillan de la misma manera, por lo que es natural preguntarse ¿existen estrellas que brillan más que otras? ¿las estrellas más brillantes están más cerca de la Tierra?  ¿Cuál es la estrella más cercana a la Tierra? y ¿hay más estrellas de las que podemos ver?")
    st.text("Se conoce como brillo o flujo luminoso de una estrella a la cantidad de luminosidad que viene de un objeto radiante y que llega a la Tierra. De esta forma, el brillo se relaciona con la percepción de qué tan brillante se ve una estrella desde la Tierra. La magnitud aparente nos permite clasificar estrellas a partir de su brillo. Según su brillo se le asigna un valor a cada estrella. Es importante mencionar que la magnitud aparente no entrega información del brillo real del astro, ya que esa característica depende de la distancia y tamaño del objeto.")

    st.markdown("<h3 style='font-family:\"Times New Roman\"; color:#444;'>Nuestro Objetivo</h3>", unsafe_allow_html=True)

    st.markdown("<div style='font-family:\"Times New Roman\";'>Modelar el comportamiento del brillo en novas reales, clasificar los eventos según su decaimiento (t3), y permitir su uso en clases de matemática y física.</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
"""
def main():
    st.markdown("<h1 style='font-family:\"Times New Roman\";'>Proyecto de desarrollo de software</h1>", unsafe_allow_html=True)

    with st.expander("Actividad 1"):
        st.markdown("<h2 style='font-family:\"Times New Roman\";'>Actividad 1</h2>", unsafe_allow_html=True)

        st.markdown("""
        <p style='font-family:"Times New Roman";'>
        Cuando miramos al cielo, observamos muchos objetos brillantes, la mayoría de los cuales son estrellas. No todas las estrellas brillan de la misma manera, por lo que es natural preguntarse: ¿existen estrellas que brillan más que otras? ¿las estrellas más brillantes están más cerca de la Tierra? ¿Cuál es la estrella más cercana a la Tierra? ¿hay más estrellas de las que podemos ver?
        </p>
        <p style='font-family:"Times New Roman";'>
        Se conoce como <strong>brillo</strong> o <strong>flujo luminoso</strong> de una estrella a la cantidad de luminosidad que viene de un objeto radiante y que llega a la Tierra. De esta forma, el brillo se relaciona con la percepción de qué tan brillante se ve una estrella desde la Tierra. La <em>magnitud aparente</em> nos permite clasificar estrellas a partir de su brillo...
        </p>
        """, unsafe_allow_html=True)

    st.markdown("<h3 style='font-family:\"Times New Roman\"; color:#444;'>Nuestro Objetivo</h3>", unsafe_allow_html=True)

    st.markdown("<div style='font-family:\"Times New Roman\";'>Modelar el comportamiento del brillo en novas reales, clasificar los eventos según su decaimiento (t3), y permitir su uso en clases de matemática y física.</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()