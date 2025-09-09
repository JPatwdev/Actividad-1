import streamlit as st  
import pandas as pd  
import altair as alt


st.markdown('# Actividad Número 1')

st.text('En esta oportunidad contamos la evolucion económica de tres complejos hoteleros entre los años 1993, 1994, y 1995')
df = pd.DataFrame()
df['Hawaiian Club'] = None
df['French Riviera'] = None
df['Bahamas Beach'] = None

# añadimos filas por su nombre de fila
df.loc['1993'] = [450000, 225000, 245000]
df.loc['1994'] = [475000, 240000 , 255000]
df.loc['1995'] = [390000, 205000 , 345000]

st.dataframe(df)
st.markdown("**Como podemos evidenciar en el siguiente gráfico, se han utilizado las herramientas visuales erróneas** ")
st.image("Imagen1.gif", caption="Gráfico anterior, con errores visuales")

errores = ["Mala selección de gráfico: En gráficos que se narran a travez del tiempo, se deben utilizar gráficos de columnas agrupadas en donde las leyendas estén bien definidas.", "Error de categorización: La categorización o labels están mal definidos, según la teoría en un gráfico de barra el tiempo debe estar en el eje X.", "Formato 3D poco recomendable: Se recomienda utilziar gráficos 2D."]
error = st.radio("Errores analizados en este Dataframe:", errores)


st.bar_chart(df,color = ["#fd0", "#f0f", "#04f"] ,stack=False)

# Soluciones 

st.markdown('**Para corregir este error nos basamos en que los graficos para visualizar los datos deben tener componentes lógicos en su presentación, primeramente los gráficos deben facilitar la compresión de la información que se va a presentar y resumir de forma dinámica aquellos hallazgos.**')
st.markdown('**Segundo, los colores deben diferenciarse dentro de sus tonalidades, el color de las categorias el tamaño de las letras y demas deben ser claras para poder llegar a mejores hallazgos y claridad dentro del análisis.**')
st.markdown('**Por ultimo, el tipo de grafico debe ser especificado por las caracteristicas del dataframe llegando a estas conclusiones:**')
solu = ["Los gráficos que se basan en una temporalidad deben tener el componente tiempo en el eje X", "Las leyendas deben estar claras, en sus definicines e igualmente en sus colores", "Este gráfico se compone de dos variables categóricas y una numérica, por ende estas variables de ven mejor representados en gráficos de barras agrupados."]
sol = st.radio("Soluciones analizados para este Dataframe:", solu)


# Anáslisis Descriptivo
st.markdown("### Análisis Descriptivo")
st.write(df.describe())
st.markdown("#### ingresos promedio")
st.markdown("El ingreso promedio de de Hawaiian Club es:  **483.333**")
st.markdown("El ingreso promedio de de French Rivera es:  **223.333**")
st.markdown("El ingreso promedio de de Bahamas Beach es:  **281.666**")
# Anáslisis Descriptivo
st.markdown("#### Análisis de Tendencias")
st.markdown("**Hawaiian Club a pesar de ser el que más dinero ha generado, su tendencia es negativa**")
st.markdown("**French Rivera manitiene su tendencia en un mismo nivel**")
st.markdown("**Bahamas Beach es quien mantiene una tendencia muy positiva en el rango de estos tres años**")

# =====================
# 5. Crecimiento interanual (ahora en gráfico lineal)
# =====================
st.subheader("📊 Crecimiento Interanual (%)")

df_growth = df.pct_change().fillna(0) * 100
df_growth_reset = df_growth.reset_index().rename(columns={"index": "Año"})
df_growth_melt = df_growth_reset.melt(id_vars="Año", var_name="Lugar", value_name="Crecimiento (%)")

growth_chart = alt.Chart(df_growth_melt).mark_line(point=True).encode(
    x="Año:N",
    y="Crecimiento (%):Q",
    color="Lugar:N",
    tooltip=["Año", "Lugar", "Crecimiento (%)"]
).properties(width=600, height=400)

st.altair_chart(growth_chart, use_container_width=True)

st.markdown("**En conclusión:**")


st.markdown("**Hawaiian Club lidera en ingresos, pero pierde fuerza. French Riviera tiene movimientos similares a Hawaiian (posibles competidores directos). Bahamas Beach es el lugar con mayor crecimiento y aumento de participación → tendencia positiva clara.**")
