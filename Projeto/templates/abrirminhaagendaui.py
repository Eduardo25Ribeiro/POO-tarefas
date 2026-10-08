import streamlit as st
from service import Service
import time

class AbrirMinhaAgendaUI:
    def main():
        st.header("Abrir Minha Agenda")
        data = st.text_input("Informe a data no formato dd/mm/aaaa")
        horario_inicio = st.text_input("Informe o horário inicial no formato HH:MM")
        horario_fim = st.text_input("Informe o horário final no formato HH:MM")
        intervalo = st.text_input("Informe o intervalo entre os horários (min)")
        if st.button("Abrir Agenda"):
            Service.horario_abrir_minha_agenda(data, horario_inicio, horario_fim, int(intervalo), st.session_state["usuario_id"])
            st.success("Horários inseridos com sucesso")
            time.sleep(2)
            st.rerun()