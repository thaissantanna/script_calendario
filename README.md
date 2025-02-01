## 📆 Gerador de Calendário

Bem-vindo ao **Gerador de Calendário**, um script Python que cria calendários personalizados para o Rio de Janeiro, incluindo feriados nacionais, estaduais e municipais! 🚀

---

## 📋 Visão Geral

Este script automatiza a criação de um arquivo Excel contendo:

✅ Datas do próximo mês  
✅ Identificação de feriados  
✅ Semana do mês e dia da semana  
✅ Sinalização de feriados fixos e móveis  
✅ Diretório estruturado automaticamente  

Útil para auxiliar em projetos onde é importante saber os feriados dos meses! 📊

---

## 🛠 Requisitos

Antes de rodar o script, instale as dependências necessárias:

```bash
pip install pandas holidays python-dateutil openpyxl
```

---

## 🚀 Como Executar

1️⃣ **Configure o diretório base**:  
   No arquivo `script_calendario.py`, edite a variável `CONFIG["caminho_base"]` para definir onde os arquivos serão salvos.

2️⃣ **Rode o script:**

```bash
python script_calendario.py
```

O arquivo **SEU_ARQUIVO.xlsx** será criado na pasta correspondente ao mês seguinte, no formato `YYYYMM`.

Exemplo: Se estamos em janeiro de 2025, o arquivo será salvo em `202502/NOME_DO_ARQUIVO.xlsx`.

---

## 📜 Estrutura dos Dados

Ajuste as colunas de acordo com as suas necessidades, mas lembre-se de modificar o código correspondente!  

| DATA       | ANOMES | SEMANA | DIA_SEMANA | FL_SAZ         | FL_FER |
|------------|--------|--------|------------|----------------|--------|
| 01/02/2025 | 202502 | 1      | 7 (Sáb)    | Carnaval       | 1      |
| 02/02/2025 | 202502 | 1      | 1 (Dom)    |                | 0      |
| 03/02/2025 | 202502 | 2      | 2 (Seg)    |                | 0      |

---

## ⚙️ Funcionalidades

✅ Identifica feriados fixos e móveis  
✅ Trata exceções e erros automaticamente  
✅ Cria diretórios automaticamente caso não existam  
✅ Exporta os dados para Excel com estrutura organizada  

---

## 🔍 Exemplo de Saída no Terminal

```
===================================
🚀 Iniciando geração de calendário
📅 Processando mês alvo: 02/2025
✅ Arquivo gerado com sucesso!
📂 Caminho: SEU_CAMINHO/202502/NOME_DO_ARQUIVO.xlsx
===================================
```

---

## 🛠 Possíveis Erros e Soluções

### 1️⃣ Erro de Locale

❌ `locale.Error: unsupported locale setting`

✅ No Windows, tente adicionar `Portuguese_Brazil.1252`.  
✅ No Linux/Mac, tente `pt_BR.utf8`.

### 2️⃣ Arquivo não gerado

❌ `FileNotFoundError: Arquivo não foi criado!`

✅ Verifique se o diretório base foi configurado corretamente.

### 3️⃣ Bibliotecas não encontradas

❌ `ModuleNotFoundError: No module named 'holidays'`

✅ Rode:

```bash
pip install -r requirements.txt
```

---

## 📌 Contribuição

Quer melhorar o projeto? Faça um fork, contribua e envie um PR! 🛠💡

---

## 📧 Contato

✉ Se tiver dúvidas ou sugestões, entre em contato!  
🔹 **Autor:** Thais Sant'Anna
🔹 [GitHub](https://github.com/thaissantanna)  

🚀 Feito para facilitar sua vida e otimizar processos!