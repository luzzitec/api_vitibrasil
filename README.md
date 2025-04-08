# 🍇 API Vitibrasil

API desenvolvida para expor dados públicos da vitivinicultura brasileira, extraídos automaticamente do site da Embrapa.

> Projeto desenvolvido como parte do **Tech Challenge - Fase 1** da pós-graduação em Machine Learning Engineering.

---

## 🚀 Deploy da API

Acesse a documentação interativa (Swagger UI):

📎 [https://api-vitibrasil-6s6h.onrender.com/docs](https://api-vitibrasil-6s6h.onrender.com/docs)

---

## 📊 Endpoints disponíveis

| Método | Rota                         | Descrição                             |
|--------|------------------------------|----------------------------------------|
| `GET`  | `/api/producao`              | Retorna os dados anuais de produção vitivinícola extraídos da Embrapa |

Exemplo de chamada direta:
https://api-vitibrasil-6s6h.onrender.com/api/producao
---

## 🧠 Funcionalidades

- 🔎 Extração automatizada de dados do site oficial da Embrapa
- 📈 Conversão dos dados em `DataFrame` com `pandas`
- ⚙️ Exposição dos dados via API REST com `FastAPI`
- ☁️ Deploy gratuito com `Render`

---

## 🧱 Estrutura do Projeto
api-embrapa/
│
├── api/
│   ├── main.py                  # Inicializa a aplicação FastAPI
│   ├── routes/
│   │   └── producao.py          # Define rotas da API
│   └── services/
│       └── scraper.py           # Realiza scraping dos dados da Embrapa
│
├── requirements.txt             # Dependências do projeto
├── start.sh                     # Script de inicialização para deploy
├── render.yaml                  # Configuração do serviço no Render
└── README.md                    # Este documento
---

## 🖥 Tecnologias utilizadas

- [Python 3.13](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Pandas](https://pandas.pydata.org/)
- [Render (Free Tier)](https://render.com/)

---

## 📌 Como executar localmente

```bash
# Clonar o repositório
git clone https://github.com/luzzitec/api_vitibrasil.git
cd api_vitibrasil

# Criar e ativar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Rodar localmente
uvicorn api.main:app --reload
---

## 💾 Como consumir os dados

Os dados da produção vitivinícola disponibilizados nesta API podem ser:

- 🔁 Integrados a **sistemas externos**, como Power BI, Tableau, Google Data Studio ou qualquer cliente HTTP
- 📥 Baixados diretamente como JSON e CSV através do endpoint: