import streamlit as st
opcoes = {
    "A1": 220,
    "A1_mini": 150,
    "P1P": 160,
    "P1S": 160,
    "X1_carbon": 200,
    "H2D": 250,
    "H2_PRO": 250
}

st.title("Calculadora de Impressão 3D")

modelo = st.selectbox("Escolha a impressora", list(opcoes.keys()))
pot = opcoes[modelo]

t_min = st.number_input("Tempo de impressão (min)", min_value=0.0)
g = st.number_input("Peso da peça (g)", min_value=0.0)
preco_kwh = st.number_input("Preço kWh recomendado(0.80--0.90)", min_value=0.5)
preco_kg = st.number_input("Preço do filamento (R$/kg)", min_value=0.0)
margem = st.slider("Margem de lucro", 1.2, 3.0, 2.5)
custo_energia = (pot * t_min / 60 * preco_kwh) / 1000
custo_material = (g / 1000) * preco_kg

custo_total = custo_energia + custo_material
preco_venda = custo_total * margem
lucro = preco_venda - custo_total

st.subheader("Resultado")
st.write("Custo total:", round(custo_total, 2))
st.write("Preço venda:", round(preco_venda, 2))
st.write("Lucro:", round(lucro, 2))