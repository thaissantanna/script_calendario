"""
Script para geração de calendário operacional com feriados do Rio de Janeiro
"""

import os
import locale
import logging
import calendar
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.easter import easter
import pandas as pd
import holidays
from holidays.countries import Brazil
from typing import List, Tuple


# Configurações globais
CONFIG = {
    "caminho_base": r"{SEU CAMINHO AQUI}",
    "formato_data": "%d/%m/%Y",
    "colunas": ["DATA", "ANOMES", "SEMANA", "DIA_SEMANA", "FL_SAZ", "FL_FER"],
    "nome_arquivo": "{NOME DO ARQUIVO}"
}

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('calendario.log'), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)


def configurar_localidade():
    """Configura o locale para português do Brasil com fallback"""
    try:
        locale.setlocale(locale.LC_TIME, "Portuguese_Brazil.1252")
    except locale.Error:
        try:
            locale.setlocale(locale.LC_TIME, "pt_BR.utf8")
        except locale.Error:
            logger.warning(
                "⚠ Locale português não disponível. Usando padrão do sistema.")


class FeriadosRJ(Brazil):
    """Classe estendida de feriados brasileiros com especificidades do RJ"""

    TRADUCAO_FERIADOS = {
        "Universal Fraternization Day": "Ano Novo",
        "Good Friday": "Sexta-Feira Santa",
        "Tiradentes' Day": "Dia de Tiradentes",
        "Saint George's Day": "Dia de São Jorge",
        "Labor Day": "Dia do Trabalhador",
        "Worker's Day": "Dia do Trabalhador",
        "Independence Day": "Independência do Brasil",
        "Our Lady of Aparecida": "Dia de Nossa Senhora Aparecida",
        "All Souls' Day": "Finados",
        "Republic Proclamation Day": "Proclamação da República",
        "National Day of Zumbi and Black Awareness": "Dia Nacional de Zumbi e da Consciência Negra",
        "Christmas Day": "Natal",
        "Corpus Christi": "Corpus Christi",
    }

    def __init__(self, **kwargs):
        """Inicializa com configurações específicas do RJ"""
        kwargs["language"] = "pt"
        kwargs["subdiv"] = "RJ"
        super().__init__(**kwargs)

        ano = self.years.pop()
        self._add_feriados_municipais(ano)
        self._add_feriados_calculados(ano)

    def _add_feriados_municipais(self, ano: int):
        """Adiciona feriados municipais fixos"""
        self[date(ano, 1, 20)] = "Dia de São Sebastião (Padroeiro do RJ)"
        self[date(ano, 3, 1)] = "Aniversário da Cidade do Rio de Janeiro"

    def _add_feriados_calculados(self, ano: int):
        """Calcula feriados móveis baseados na Páscoa"""
        data_pascoa = easter(ano)
        self[data_pascoa - timedelta(days=48)] = "Carnaval"
        self[data_pascoa - timedelta(days=47)] = "Carnaval"
        self[data_pascoa - timedelta(days=2)] = "Sexta-Feira Santa"
        self[data_pascoa + timedelta(days=60)] = "Corpus Christi"

    def get(self, data: date) -> str:
        """Retorna feriado traduzido"""
        nome_feriado = super().get(data)
        return self.TRADUCAO_FERIADOS.get(nome_feriado, nome_feriado)


def criar_estrutura_diretorios(ano: int, mes: int) -> str:
    """Cria estrutura de diretórios e retorna caminho completo do arquivo"""
    nome_pasta = os.path.join(CONFIG["caminho_base"], f"{ano}{mes:02d}")

    if not os.path.isabs(CONFIG["caminho_base"]):
        raise ValueError("❌ Caminho base deve ser absoluto")

    os.makedirs(nome_pasta, exist_ok=True)
    return os.path.join(nome_pasta, CONFIG["nome_arquivo"])


def gerar_dados_calendario(ano: int, mes: int) -> List[Tuple]:
    """Gera os dados do calendário para o mês especificado"""
    feriados_rj = FeriadosRJ(years=ano)
    ultimo_dia = calendar.monthrange(ano, mes)[1]
    anomes = date(ano, mes, 1).strftime(CONFIG["formato_data"])

    dados = []
    semana_do_mes = 1

    for dia in range(1, ultimo_dia + 1):
        data_atual = date(ano, mes, dia)
        timestamp = pd.Timestamp(data_atual)
        nome_feriado = feriados_rj.get(data_atual)

        dia_semana = (timestamp.weekday() + 2) % 7 or 7  # 1=Dom, 7=Sáb

        dados.append((data_atual.strftime(CONFIG["formato_data"]),
                      anomes,
                      semana_do_mes,
                      dia_semana,
                      nome_feriado if nome_feriado else "",
                      1 if nome_feriado else 0))

        # Atualiza contador de semanas
        if dia_semana == 1 and dia > 1:
            semana_do_mes += 1

    return dados


def validar_arquivo_gerado(nome_arquivo: str):
    """Realiza validações básicas do arquivo gerado"""
    if not os.path.exists(nome_arquivo):
        raise FileNotFoundError(f"❌ Arquivo {nome_arquivo} não foi criado!")

    if os.path.getsize(nome_arquivo) < 1024:
        raise ValueError("⚠ Arquivo gerado parece estar vazio ou corrompido!")


def main():
    """Fluxo principal de execução"""
    try:
        configurar_localidade()
        print("\n===================================")
        print("🚀 Iniciando geração de calendário")
        print("===================================\n")

        hoje = datetime.today()
        data_alvo = hoje.replace(day=1) + relativedelta(months=1)
        ano, mes = data_alvo.year, data_alvo.month

        print(f"📅 Processando mês alvo: {mes:02d}/{ano}")

        nome_arquivo = criar_estrutura_diretorios(ano, mes)
        dados = gerar_dados_calendario(ano, mes)

        df = pd.DataFrame(dados, columns=CONFIG["colunas"])
        df.to_excel(nome_arquivo, index=False)

        validar_arquivo_gerado(nome_arquivo)

        print("\n===================================")
        print(f"✅ Arquivo gerado com sucesso!")
        print(f"📂 Caminho: {nome_arquivo}")
        print("===================================\n")

    except Exception as e:
        print("\n❌ ERRO CRÍTICO! Execução abortada!")
        print("Detalhes do erro: ", str(e))
        print("===================================\n")
        logger.error(f"Erro na execução: {str(e)}", exc_info=True)
        raise


if __name__ == "__main__":
    main()
