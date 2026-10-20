import pandas as pd
import streamlit as st
from service import Service


class PagarAtendimentoUI:
    @staticmethod
    def main():
        st.header("Pagar Atendimento")
        id_cliente = st.session_state["usuario_id"]
        atendimentos = []
        for atendimento in Service.atendimento_listar():
            horario = Service.horario_listar_id(atendimento.get_id_horario())
            if horario is not None and horario.get_id_cliente() == id_cliente:
                atendimentos.append(atendimento)

        if not atendimentos:
            st.write("Nenhum atendimento encontrado.")
            return

        st.dataframe(
            pd.DataFrame([
                {
                    "id": atendimento.get_id(),
                    "data": atendimento.get_data(),
                    "queixa principal": atendimento.get_queixa_principal(),
                    "total": atendimento.get_total(),
                    "pago": atendimento.get_pago(),
                }
                for atendimento in atendimentos
            ]),
            hide_index=True,
        )

        pendentes = [atendimento for atendimento in atendimentos if not atendimento.get_pago()]
        if not pendentes:
            st.write("Todos os atendimentos já foram pagos.")
            return

        atendimento = st.selectbox(
            "Selecione o atendimento para pagar",
            pendentes,
            format_func=lambda obj: f"{obj.get_id()} - {obj.get_data().strftime('%d/%m/%Y %H:%M')} - R$ {obj.get_total():.2f}",
        )
        forma = st.selectbox("Forma de pagamento", ["Dinheiro", "Pix", "Cartão"])
        if st.button("Pagar atendimento"):
            Service.atendimento_pagar(atendimento.get_id(), forma)
            st.success("Pagamento realizado. Atendimento finalizado.")
