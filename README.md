# SmartBot

Бот для ответа на типичные вопросы в чате Telegram и в социальной сети VK.

Пример бота [для VK](https://vk.com/xkcd_comics_fun) (нажать "Написать сообщение") и для [Telegram.](https://t.me/DevmanBot_bot)

## Установка
```
git clone https://github.com/j0hntv/SmartBot.git
```
- Необходимые библиотеки:
```
pip install -r requirements.txt
```
или
```
pip3 install -r requirements.txt
```
## Переменные окружения
На машине должны быть доступны следующие переменные окружения:
```
TELEGRAM_BOT_TOKEN=<your telegram bot token>
CHAT_ID_TO_SEND_LOGS=<your telegram chat id>
GOOGLE_PROJECT_ID=<your google project id>
GOOGLE_APPLICATION_CREDENTIALS="path to json-file"
```
## Обучение бота
Что понадобится:
- [Создать аккаунт в DialogFlow](https://dialogflow.com/docs/getting-started/create-account)
- [Создать проект в DialogFlow](https://dialogflow.com/docs/getting-started/first-agent)
- JSON файл с обучающими фразами, [пример.](https://github.com/j0hntv/SmartBot/blob/master/questions.json) 

Для обучения бота у агента DialogFlow должны быть права доступа Администратор Dialogflow API. (В Google Cloud Platform раздел "IAM и администрирование".)
```
python3 train.py <json-файл с обучающими фразами>
```
## Запуск
- Телеграм-бот:
```
python3 telegrambot.py
```
- VK-бот:
```
python3 vkbot.py
```
Готово!

Сделано в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/modules/)