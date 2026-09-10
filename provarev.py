import json
import os
import time

import pandas as pd
import streamlit as st


# ==============================================================================
# CONFIGURAÇÃO GERAL DA PÁGINA
# ==============================================================================

st.set_page_config(
    page_title="Projeto Streamlit + POO",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ==============================================================================
# 1. MODELO — ENTIDADE DO DOMÍNIO
# ==============================================================================

class Tarefa:

    def __init__(
        self,
        id: int,
        titulo: str,
        descricao: str,
        concluida: bool = False,
    ):
        self.id = id
        self.titulo = titulo.strip().title()
        self.descricao = descricao.strip()
        self.concluida = concluida

    def to_dict(self) -> dict:
        """Converte o objeto em dicionário para salvar no JSON."""
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "concluida": self.concluida,
        }

    @classmethod
    def from_dict(cls, dados: dict) -> "Tarefa":
        """Converte um dicionário do JSON de volta para um objeto Tarefa."""
        return cls(
            id=dados["id"],
            titulo=dados["titulo"],
            descricao=dados["descricao"],
            concluida=dados["concluida"],
        )

    def __str__(self) -> str:
        status = "✅" if self.concluida else "⏳"
        return f"{status} [{self.id}] {self.titulo}"


# ==============================================================================
# 2. DAO — PERSISTÊNCIA E ACESSO AOS DADOS
# ==============================================================================

class TarefaDAO:

    def __init__(self, arquivo_path: str = "tarefas.json"):
        self.arquivo_path = arquivo_path
        self._tarefas: list[Tarefa] = []
        self._proximo_id = 1
        self._carregar_arquivo()

    def _salvar_arquivo(self):
        """Grava todos os objetos no arquivo JSON."""
        dados_dict = [t.to_dict() for t in self._tarefas]

        with open(
            self.arquivo_path,
            "w",
            encoding="utf-8",
        ) as arquivo:
            json.dump(
                dados_dict,
                arquivo,
                indent=4,
                ensure_ascii=False,
            )

    def _carregar_arquivo(self):
        """Lê o JSON e transforma os dados novamente em objetos Tarefa."""

        if not os.path.exists(self.arquivo_path):
            self._tarefas = []
            return

        try:
            with open(
                self.arquivo_path,
                "r",
                encoding="utf-8",
            ) as arquivo:

                dados_dict = json.load(arquivo)

                self._tarefas = [
                    Tarefa.from_dict(item)
                    for item in dados_dict
                ]

                if self._tarefas:
                    self._proximo_id = (
                        max(t.id for t in self._tarefas) + 1
                    )

        except (json.JSONDecodeError, FileNotFoundError):
            self._tarefas = []

    def inserir(self, tarefa: Tarefa) -> Tarefa:
        tarefa.id = self._proximo_id
        self._proximo_id += 1

        self._tarefas.append(tarefa)
        self._salvar_arquivo()

        return tarefa

    def listar(self) -> list[Tarefa]:
        return self._tarefas

    def buscar_por_id(self, id: int) -> Tarefa | None:
        for tarefa in self._tarefas:
            if tarefa.id == id:
                return tarefa

        return None

    def excluir(self, id: int) -> bool:
        tarefa = self.buscar_por_id(id)

        if tarefa:
            self._tarefas.remove(tarefa)
            self._salvar_arquivo()
            return True

        return False

    def salvar_alteracoes(self):
        self._salvar_arquivo()


# ==============================================================================
# 3. SERVICE — REGRAS DE NEGÓCIO
# ==============================================================================

class TarefaService:

    def __init__(self, dao: TarefaDAO):
        self.dao = dao

    def cadastrar(
        self,
        titulo: str,
        descricao: str,
    ) -> Tarefa:

        if not titulo.strip():
            raise ValueError(
                "O título não pode estar vazio."
            )

        if len(titulo.strip()) < 3:
            raise ValueError(
                "O título precisa ter no mínimo 3 caracteres."
            )

        nova_tarefa = Tarefa(
            id=0,
            titulo=titulo,
            descricao=descricao,
        )

        return self.dao.inserir(nova_tarefa)

    def listar_todas(self) -> list[Tarefa]:
        return self.dao.listar()

    def alternar_status(self, id: int):

        tarefa = self.dao.buscar_por_id(id)

        if not tarefa:
            raise ValueError(
                "Tarefa não encontrada."
            )

        tarefa.concluida = not tarefa.concluida
        self.dao.salvar_alteracoes()

    def remover(self, id: int):

        if not self.dao.excluir(id):
            raise ValueError(
                "Não foi possível excluir a tarefa."
            )


# ==============================================================================
# 4. PROGRAMA 1 — GERENCIADOR DE TAREFAS POO
# ==============================================================================

def pagina_gerenciador_tarefas(service: TarefaService):

    st.title("⚡ Gerenciador de Tarefas — POO")

    st.caption(
        "Sistema de tarefas integrado com arquitetura em camadas"
    )

    # --------------------------------------------------------------------------
    # SIDEBAR
    # --------------------------------------------------------------------------

    st.sidebar.header("⚙️ Painel do Gerenciador")

    modo_visualizacao = st.sidebar.radio(
        "Modo de Exibição",
        ["Completo", "Compacto"],
        key="tarefas_modo_visualizacao",
    )

    mostrar_ajuda = st.sidebar.checkbox(
        "Mostrar ajuda",
        value=False,
        key="tarefas_mostrar_ajuda",
    )

    if mostrar_ajuda:
        st.sidebar.info(
            "Preencha o formulário para salvar dados "
            "no arquivo JSON."
        )

    # --------------------------------------------------------------------------
    # ABAS
    # --------------------------------------------------------------------------

    tab_cadastrar, tab_listar, tab_comandos = st.tabs(
        [
            "➕ Cadastrar",
            "📋 Listar Tarefas",
            "📖 Guia do Streamlit",
        ]
    )

    # --------------------------------------------------------------------------
    # ABA CADASTRAR
    # --------------------------------------------------------------------------

    with tab_cadastrar:

        st.subheader("Formulário de Cadastro")

        with st.form(
            "form_tarefa_principal",
            clear_on_submit=True,
        ):

            titulo = st.text_input(
                "Título da Tarefa",
                placeholder="Ex: Estudar POO para o IFRN",
            )

            descricao = st.text_area(
                "Descrição",
                placeholder="Detalhes da tarefa...",
            )

            submetido = st.form_submit_button(
                "Salvar Registro"
            )

            if submetido:

                try:
                    service.cadastrar(
                        titulo,
                        descricao,
                    )

                    st.success(
                        "Tarefa cadastrada com sucesso!"
                    )

                except ValueError as erro:

                    st.error(str(erro))

    # --------------------------------------------------------------------------
    # ABA LISTAR
    # --------------------------------------------------------------------------

    with tab_listar:

        st.subheader("Minhas Tarefas Cadastradas")

        tarefas = service.listar_todas()

        if not tarefas:

            st.warning(
                "Nenhuma tarefa cadastrada até o momento."
            )

        else:

            for tarefa in tarefas:

                if modo_visualizacao == "Completo":

                    col_info, col_status, col_del = st.columns(
                        [3, 1, 1]
                    )

                    with col_info:

                        st.markdown(
                            f"**{tarefa}**"
                        )

                        if tarefa.descricao:
                            st.caption(
                                tarefa.descricao
                            )

                    with col_status:

                        rotulo = (
                            "Desfazer"
                            if tarefa.concluida
                            else "Concluir"
                        )

                        if st.button(
                            rotulo,
                            key=f"status_tarefa_{tarefa.id}",
                        ):

                            service.alternar_status(
                                tarefa.id
                            )

                            st.rerun()

                    with col_del:

                        if st.button(
                            "Excluir",
                            key=f"excluir_tarefa_{tarefa.id}",
                        ):

                            service.remover(
                                tarefa.id
                            )

                            st.rerun()

                    st.divider()

                else:

                    st.write(str(tarefa))

    # --------------------------------------------------------------------------
    # ABA GUIA DOS COMANDOS
    # --------------------------------------------------------------------------

    with tab_comandos:

        st.subheader(
            "Resumo dos Comandos Usados"
        )

        st.code(
            """
# Configuração
st.set_page_config(
    page_title="App",
    layout="wide"
)

# Entradas
st.text_input("Rótulo")
st.text_area("Rótulo")

# Formulário
with st.form("nome_form"):
    st.form_submit_button("Enviar")

# Layout
st.sidebar.radio(
    "Navegação",
    ["A", "B"],
    key="meu_radio"
)

st.tabs(["Aba 1", "Aba 2"])
st.columns([2, 1])
st.divider()

# Feedback
st.success("Sucesso")
st.error("Erro")

# Estado
st.session_state["chave"] = valor

# Recarregar
st.rerun()
            """,
            language="python",
        )


# ==============================================================================
# 5. PROGRAMA 2 — GUIA COMPLETO DO STREAMLIT
# ==============================================================================

def pagina_guia_streamlit():

    st.title("🚀 Guia Completo do Streamlit")

    st.write(
        "Exemplos dos principais componentes "
        "do Streamlit."
    )

    menu = st.sidebar.radio(
        "Escolha uma Categoria:",
        [
            "1. Textos e Mídia",
            "2. Entradas de Dados",
            "3. Layout e Organização",
            "4. Mensagens de Feedback",
            "5. Dados e Gráficos",
            "6. Session State",
        ],
        key="guia_categoria",
    )

    st.sidebar.divider()

    st.sidebar.caption(
        "Guia de referência rápida do Streamlit."
    )

    # ==========================================================================
    # CATEGORIA 1
    # ==========================================================================

    if menu == "1. Textos e Mídia":

        st.header(
            "📌 1. Textos e Elementos Visuais"
        )

        st.subheader(
            "Títulos e Subtítulos"
        )

        st.code(
            """
st.title("Título Principal")
st.header("Cabeçalho")
st.subheader("Subcabeçalho")
st.caption("Legenda")
            """
        )

        st.subheader(
            "Exibição de Texto"
        )

        st.markdown(
            "Texto em **negrito**, "
            "*itálico* e links."
        )

        st.text(
            "Texto puro sem formatação."
        )

        st.subheader(
            "Código e Fórmulas"
        )

        st.code(
            "def hello():\n"
            "    print('Olá, Streamlit!')",
            language="python",
        )

        st.latex(
            r"e^{i\pi} + 1 = 0"
        )

    # ==========================================================================
    # CATEGORIA 2
    # ==========================================================================

    elif menu == "2. Entradas de Dados":

        st.header(
            "📥 2. Entradas de Dados"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.subheader(
                "Inputs de Texto e Números"
            )

            st.text_input(
                "Campo de Texto",
                value="Digite aqui...",
                key="guia_texto",
            )

            st.text_input(
                "Campo de Senha",
                type="password",
                key="guia_senha",
            )

            st.text_area(
                "Área de Texto",
                key="guia_textarea",
            )

            st.number_input(
                "Entrada Numérica",
                min_value=0,
                max_value=100,
                value=25,
                key="guia_numero",
            )

        with col2:

            st.subheader(
                "Seletores e Sliders"
            )

            st.selectbox(
                "Caixa de Seleção",
                [
                    "Opção A",
                    "Opção B",
                    "Opção C",
                ],
                key="guia_selectbox",
            )

            st.multiselect(
                "Múltipla Escolha",
                [
                    "Python",
                    "Java",
                    "C++",
                    "SQL",
                ],
                key="guia_multiselect",
            )

            st.slider(
                "Barra Deslizante",
                min_value=0,
                max_value=100,
                value=50,
                key="guia_slider",
            )

            st.checkbox(
                "Caixa de Seleção",
                key="guia_checkbox",
            )

        st.divider()

        st.subheader(
            "Formulários"
        )

        with st.form(
            "guia_formulario",
            clear_on_submit=True,
        ):

            f_nome = st.text_input(
                "Nome no Form"
            )

            f_email = st.text_input(
                "E-mail no Form"
            )

            botao_form = st.form_submit_button(
                "Enviar Formulário"
            )

            if botao_form:

                st.success(
                    f"Formulário enviado! Nome: {f_nome}"
                )

    # ==========================================================================
    # CATEGORIA 3
    # ==========================================================================

    elif menu == "3. Layout e Organização":

        st.header(
            "📐 3. Layout e Estrutura de Tela"
        )

        st.subheader(
            "Colunas"
        )

        c1, c2, c3 = st.columns(
            [1, 2, 1]
        )

        with c1:
            st.info(
                "Coluna 1"
            )

        with c2:
            st.info(
                "Coluna 2"
            )

        with c3:
            st.info(
                "Coluna 3"
            )

        st.subheader(
            "Abas"
        )

        aba1, aba2 = st.tabs(
            [
                "Aba Principal",
                "Aba Secundária",
            ]
        )

        with aba1:
            st.write(
                "Conteúdo da primeira aba."
            )

        with aba2:
            st.write(
                "Conteúdo da segunda aba."
            )

        st.subheader(
            "Expansor"
        )

        with st.expander(
            "Clique para expandir/recolher"
        ):

            st.write(
                "Conteúdo escondido dentro "
                "do expansor."
            )

        st.subheader(
            "Container"
        )

        container = st.container(
            border=True
        )

        container.write(
            "Texto dentro de um container."
        )

    # ==========================================================================
    # CATEGORIA 4
    # ==========================================================================

    elif menu == "4. Mensagens de Feedback":

        st.header(
            "🔔 4. Notificações e Status"
        )

        st.subheader(
            "Caixas de Alerta"
        )

        st.success(
            "st.success(): Operação realizada!"
        )

        st.info(
            "st.info(): Informação útil."
        )

        st.warning(
            "st.warning(): Mensagem de aviso."
        )

        st.error(
            "st.error(): Erro detectado."
        )

        st.subheader(
            "Barra de Progresso e Spinner"
        )

        if st.button(
            "Executar Processo Demorado",
            key="guia_processo",
        ):

            with st.spinner(
                "Processando dados..."
            ):

                progresso = st.progress(0)

                for i in range(100):

                    time.sleep(0.01)

                    progresso.progress(
                        i + 1
                    )

            st.balloons()

            st.toast(
                "Processo concluído!",
                icon="🎉",
            )

    # ==========================================================================
    # CATEGORIA 5
    # ==========================================================================

    elif menu == "5. Dados e Gráficos":

        st.header(
            "📊 5. Visualização de Dados"
        )

        dados = pd.DataFrame(
            {
                "Categoria": [
                    "A",
                    "B",
                    "C",
                    "D",
                ],
                "Valores": [
                    10,
                    25,
                    15,
                    30,
                ],
            }
        )

        col1, col2 = st.columns(2)

        with col1:

            st.subheader(
                "Métrica"
            )

            st.metric(
                label="Total de Vendas",
                value="R$ 1.250,00",
                delta="+12%",
            )

            st.subheader(
                "Tabela de Dados"
            )

            st.dataframe(
                dados,
                use_container_width=True,
            )

        with col2:

            st.subheader(
                "Gráficos"
            )

            st.line_chart(
                dados.set_index(
                    "Categoria"
                )
            )

            st.bar_chart(
                dados.set_index(
                    "Categoria"
                )
            )

    # ==========================================================================
    # CATEGORIA 6
    # ==========================================================================

    elif menu == "6. Session State":

        st.header(
            "🧠 6. Gerenciamento de Estado"
        )

        st.write(
            "O Streamlit executa novamente o script "
            "a cada interação. O session_state permite "
            "manter valores entre essas execuções."
        )

        if "contador_guia" not in st.session_state:

            st.session_state.contador_guia = 0

        col1, col2, col3 = st.columns(3)

        with col1:

            if st.button(
                "➕ Incrementar",
                key="contador_incrementar",
            ):

                st.session_state.contador_guia += 1

                st.rerun()

        with col2:

            if st.button(
                "➖ Decrementar",
                key="contador_decrementar",
            ):

                st.session_state.contador_guia -= 1

                st.rerun()

        with col3:

            if st.button(
                "🔄 Resetar",
                key="contador_resetar",
            ):

                st.session_state.contador_guia = 0

                st.rerun()

        st.markdown(
            f"### Valor Atual: "
            f"`{st.session_state.contador_guia}`"
        )


# ==============================================================================
# 6. PROGRAMA 3 — GUIA DE MENUS
# ==============================================================================

def pagina_guia_menus():

    st.title(
        "🧩 Guia de Menus no Streamlit"
    )

    st.write(
        "Escolha um tipo de menu para testar."
    )

    estilo_menu = st.radio(
        "Escolha o tipo de menu:",
        [
            "1. Vertical na Sidebar",
            "2. Horizontal com Abas",
            "3. Horizontal com Botões",
            "4. streamlit-option-menu",
        ],
        horizontal=True,
        key="estilo_menu_principal",
    )

    st.divider()

    # ==========================================================================
    # MENU 1 — SIDEBAR
    # ==========================================================================

    if estilo_menu == "1. Vertical na Sidebar":

        st.subheader(
            "📍 Menu Vertical na Barra Lateral"
        )

        opcao_sidebar = st.sidebar.radio(
            "Navegação Principal",
            [
                "Home",
                "Relatórios",
                "Configurações",
                "Perfil",
            ],
            key="menu_sidebar_exemplo",
        )

        st.info(
            "Veja o menu na barra lateral esquerda 👈"
        )

        if opcao_sidebar == "Home":

            st.write(
                "### 🏠 Página Inicial"
            )

            st.write(
                "Conteúdo da tela de início."
            )

        elif opcao_sidebar == "Relatórios":

            st.write(
                "### 📊 Painel de Relatórios"
            )

            st.write(
                "Gráficos e tabelas ficam aqui."
            )

        elif opcao_sidebar == "Configurações":

            st.write(
                "### ⚙️ Configurações"
            )

            st.write(
                "Preferências e parâmetros."
            )

        elif opcao_sidebar == "Perfil":

            st.write(
                "### 👤 Perfil"
            )

            st.write(
                "Informações da conta."
            )

    # ==========================================================================
    # MENU 2 — TABS
    # ==========================================================================

    elif estilo_menu == "2. Horizontal com Abas":

        st.subheader(
            "📍 Menu Horizontal usando st.tabs"
        )

        aba1, aba2, aba3, aba4 = st.tabs(
            [
                "🏠 Home",
                "📊 Relatórios",
                "⚙️ Configurações",
                "👤 Perfil",
            ]
        )

        with aba1:

            st.write(
                "### Conteúdo da Aba Home"
            )

            st.success(
                "Você está na página inicial!"
            )

        with aba2:

            st.write(
                "### Conteúdo dos Relatórios"
            )

            st.metric(
                "Vendas Totais",
                "R$ 45.000,00",
                "+15%",
            )

        with aba3:

            st.write(
                "### Configurações"
            )

            st.checkbox(
                "Notificações por E-mail",
                key="menu_notificacoes",
            )

        with aba4:

            st.write(
                "### Perfil"
            )

            st.text_input(
                "Nome",
                value="Eduardo",
                key="menu_nome",
            )

    # ==========================================================================
    # MENU 3 — BOTÕES
    # ==========================================================================

    elif estilo_menu == "3. Horizontal com Botões":

        st.subheader(
            "📍 Menu Horizontal com Botões"
        )

        if "pagina_atual" not in st.session_state:

            st.session_state.pagina_atual = "Home"

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            if st.button(
                "🏠 Home",
                use_container_width=True,
                key="menu_btn_home",
            ):

                st.session_state.pagina_atual = "Home"

                st.rerun()

        with col2:

            if st.button(
                "📊 Relatórios",
                use_container_width=True,
                key="menu_btn_relatorios",
            ):

                st.session_state.pagina_atual = "Relatórios"

                st.rerun()

        with col3:

            if st.button(
                "⚙️ Configurações",
                use_container_width=True,
                key="menu_btn_configuracoes",
            ):

                st.session_state.pagina_atual = "Configurações"

                st.rerun()

        with col4:

            if st.button(
                "👤 Perfil",
                use_container_width=True,
                key="menu_btn_perfil",
            ):

                st.session_state.pagina_atual = "Perfil"

                st.rerun()

        st.divider()

        pagina = st.session_state.pagina_atual

        st.markdown(
            f"#### PÁGINA ATUAL: `{pagina}`"
        )

        if pagina == "Home":

            st.write(
                "Conteúdo da tela inicial."
            )

        elif pagina == "Relatórios":

            st.write(
                "Exibindo relatórios atualizados."
            )

        elif pagina == "Configurações":

            st.write(
                "Painel de ajustes."
            )

        elif pagina == "Perfil":

            st.write(
                "Dados da conta do usuário."
            )

    # ==========================================================================
    # MENU 4 — STREAMLIT OPTION MENU
    # ==========================================================================

    elif estilo_menu == "4. streamlit-option-menu":

        st.subheader(
            "📍 Menu com streamlit-option-menu"
        )

        st.caption(
            "Requer instalação da biblioteca "
            "streamlit-option-menu."
        )

        try:

            from streamlit_option_menu import option_menu

            menu_horiz = option_menu(
                menu_title=None,
                options=[
                    "Home",
                    "Relatórios",
                    "Configurações",
                ],
                icons=[
                    "house",
                    "bar-chart",
                    "gear",
                ],
                default_index=0,
                orientation="horizontal",
                styles={
                    "container": {
                        "padding": "0!important",
                        "background-color": "#fafafa",
                    },
                    "icon": {
                        "color": "orange",
                        "font-size": "18px",
                    },
                    "nav-link": {
                        "font-size": "15px",
                        "text-align": "center",
                        "margin": "0px",
                        "--hover-color": "#eee",
                    },
                    "nav-link-selected": {
                        "background-color": "#02ab21",
                    },
                },
            )

            st.write(
                f"Você selecionou: "
                f"**{menu_horiz}**"
            )

        except ImportError:

            st.error(
                "A biblioteca "
                "'streamlit-option-menu' "
                "não está instalada."
            )

            st.code(
                "pip install streamlit-option-menu",
                language="bash",
            )


# ==============================================================================
# 7. MENU PRINCIPAL DO PROJETO
# ==============================================================================

def main():

    # --------------------------------------------------------------------------
    # SESSION STATE DO DAO
    # --------------------------------------------------------------------------

    if "tarefa_dao" not in st.session_state:

        st.session_state.tarefa_dao = TarefaDAO()

    dao = st.session_state.tarefa_dao

    service = TarefaService(dao)

    # --------------------------------------------------------------------------
    # MENU PRINCIPAL
    # --------------------------------------------------------------------------

    st.sidebar.divider()

    st.sidebar.header(
        "🧩 Projeto Principal"
    )

    pagina_principal = st.sidebar.radio(
        "Escolha o módulo:",
        [
            "⚡ Gerenciador de Tarefas POO",
            "🚀 Guia Completo do Streamlit",
            "🧩 Guia de Menus",
        ],
        key="menu_principal_aplicacao",
    )

    st.sidebar.divider()

    st.sidebar.caption(
        "Projeto desenvolvido com Python + Streamlit + POO"
    )

    # --------------------------------------------------------------------------
    # RENDERIZAÇÃO
    # --------------------------------------------------------------------------

    if pagina_principal == "⚡ Gerenciador de Tarefas POO":

        pagina_gerenciador_tarefas(service)

    elif pagina_principal == "🚀 Guia Completo do Streamlit":

        pagina_guia_streamlit()

    elif pagina_principal == "🧩 Guia de Menus":

        pagina_guia_menus()


# ==============================================================================
# 8. EXECUÇÃO
# ==============================================================================

if __name__ == "__main__":
    main()
