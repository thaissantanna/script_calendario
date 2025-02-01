📆 Gerador de Calendário

Bem-vindo ao Gerador de Calendário, um script Python que cria calendários personalizados para o Rio de Janeiro, incluindo feriados nacionais, estaduais e municipais! 🚀

📋 Visão Geral

Este script automatiza a criação de um arquivo Excel contendo:
✅ Datas do próximo mês
✅ Identificação de feriados
✅ Semana do mês e dia da semana
✅ Sinalização de feriados fixos e móveis
✅ Diretório estruturado automaticamente

Util para auxiliar em projetos aonde é importante saber os feriados dos meses! 📊

🛠 Requisitos

Antes de rodar o script, instale as dependências necessárias:

pip install pandas holidays python-dateutil openpyxl

🚀 Como Executar

Configure o diretório base: No arquivo script_calendario.py, edite a variável CONFIG["caminho_base"] para definir onde os arquivos serão salvos.

Rode o script:

python script_calendario.py

O arquivo SEU ARQUIVO será criado na pasta correspondente ao mês seguinte, no formato YYYYMM.

Exemplo: Se estamos em janeiro de 2025, o arquivo será salvo em 202502/NOME DO ARQUIVO.xlsx.

📜 Estrutura dos Dados

Ajuste as colunas de acordo com as suas necessidades de retorno,
Mas lembre-se de ajustar o código também!

⚙️ Funcionalidades

✅ Identifica feriados fixos e móveis
✅ Trata exceções e erros automaticamente
✅ Cria diretórios automaticamente caso não existam
✅ Exporta os dados para Excel com estrutura organizada

🔍 Exemplo de Saída no Terminal

===================================
🚀 Iniciando geração de calendário
===================================
📅 Processando mês alvo: 02/2025
✅ Arquivo gerado com sucesso!
📂 Caminho: SEU CAMINHO
===================================

🛠 Possíveis Erros e Soluções

1️⃣ Erro de Locale

❌ locale.Error: unsupported locale setting
✅ No Windows, tente adicionar Portuguese_Brazil.1252. No Linux/Mac, tente pt_BR.utf8.

2️⃣ Arquivo não gerado

❌ FileNotFoundError: Arquivo não foi criado!
✅ Verifique se o diretório base foi configurado corretamente.

3️⃣ Bibliotecas não encontradas

❌ ModuleNotFoundError: No module named 'holidays'
✅ Rode pip install -r requirements.txt para instalar as dependências.

📌 Contribuição

Quer melhorar o projeto? Forke, contribua e envie um PR! 🛠💡

📧 Contato

✉ Se tiver dúvidas ou sugestões, entre em contato!

🔹 Autor: "Thais Sant'Anna"🔹 https://github.com/thaissantanna

🚀 Feito para facilitar sua vida e otimizar processos!