# Copilot Telegram Bot

Um bot do Telegram integrado com o GitHub Copilot CLI para assistência inteligente via chat.

## Pré-requisitos

- Python 3.8+
- pip (Python Package Manager)
- Token de Bot do Telegram (obtenha em @BotFather no Telegram)

## Instalação

1. Clone ou navegue para o diretório do projeto:
   ```bash
   cd copilot-telegram-bot
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure as variáveis de ambiente:
   ```bash
   cp .env.example .env
   ```

4. Edite o arquivo `.env` com suas credenciais:
   ```
   TELEGRAM_TOKEN=seu_token_aqui
   FLASK_HOST=127.0.0.1
   FLASK_PORT=5000
   DATABASE_PATH=./data/bot.db
   ```

## Uso

Para iniciar o bot:

```bash
python main.py
```

O bot iniciará e estará pronto para receber mensagens.

## Arquitetura

- **bot/**: Lógica do bot Telegram
- **server/**: API Flask para webhooks e endpoints
- **agents/**: Configuração dos agentes Copilot
- **database/**: Camada de dados e persistência
- **config.py**: Configuração centralizada
- **main.py**: Ponto de entrada da aplicação

## Desenvolvimento

Para contribuir ou estender funcionalidades:

1. Adicione novos handlers em `bot/telegram_bot.py`
2. Implemente endpoints da API em `server/api.py`
3. Configure agentes em `agents/config.json`
4. Atualize banco de dados em `database/`

## Licença

Este projeto é licenciado sob a MIT License.