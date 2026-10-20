import streamlit as st
from datetime import datetime
from service import Service


class RegistrarAtendimentoUI:
    @staticmethod
    def main():
        st.header("Registrar Atendimento")
        horarios = Service.atendimento_horarios_profissional(st.session_state["usuario_id"])
        if not horarios:
            st.write("Nenhum serviço agendado para atendimento.")
            return

        horario = st.selectbox("Informe o horário", horarios, format_func=str)
        data = st.date_input("Data do atendimento", value=horario.get_data().date())
        hora = st.time_input("Horário do atendimento", value=horario.get_data().time())
        queixa_principal = st.text_input("Queixa principal")
        historico_saude = st.text_area("Histórico de saúde")
        avaliacao = st.text_area("Avaliação clínica")
        prescricao = st.text_area("Prescrição de exames e medicamentos")

        servicos = Service.servico_listar()
        if not servicos:
            st.write("Nenhum serviço cadastrado.")
            return
        servicos_realizados = st.multiselect("Serviços realizados", servicos, format_func=str)
        quantidades = {}
        for servico in servicos_realizados:
            quantidades[servico.get_id()] = st.number_input(
                f"Quantidade de {servico.get_descricao()}",
                min_value=1,
                step=1,
                value=1,
                key=f"qtd_{servico.get_id()}",
            )
        total = sum(servico.get_valor() * quantidades[servico.get_id()] for servico in servicos_realizados)
        st.write(f"Total: R$ {total:.2f}")

        if st.button("Registrar atendimento"):
            if not queixa_principal:
                st.error("Informe a queixa principal.")
                return
            if not servicos_realizados:
                st.error("Selecione ao menos um serviço realizado.")
                return
            data_atendimento = datetime.combine(data, hora)
            id_atendimento = Service.atendimento_inserir(
                data_atendimento,
                queixa_principal,
                historico_saude,
                avaliacao,
                prescricao,
                horario.get_id(),
                total,
                False,
            )
            for servico in servicos_realizados:
                Service.atendimentoitem_inserir(
                    id_atendimento,
                    servico.get_id(),
                    quantidades[servico.get_id()],
                    servico.get_valor(),
                )
            st.success("Atendimento registrado com sucesso!")
