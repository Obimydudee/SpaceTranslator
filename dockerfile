FROM python:3.13-slim

WORKDIR /spaceTranslator

COPY src/app.py .
COPY src/requirements.txt .
ADD src/cogs /spaceTranslator/cogs
ADD src/Utils /spaceTranslator/Utils

RUN pip install -r requirements.txt

ENV Space=DiscordBotTokenHere
ENV BotID=DiscordBotIDHere

CMD [ "python3", "app.py" ]
