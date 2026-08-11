import streamlit as st

from retangulo import Retangulo


class RetanguloUI:

    @staticmethod
    def main():
        st.header("Cálculos com retângulo")

        base = st.number_input("Base", min_value=0.0)
        altura = st.number_input("Altura", min_value=0.0)

        if st.button("Calcular"):
            r = Retangulo(base, altura)

            st.write(f"Área: {r.area()}")
            st.write(f"Perímetro: {r.perimetro()}")
            st.write(f"Diagonal: {r.diagonal()}")