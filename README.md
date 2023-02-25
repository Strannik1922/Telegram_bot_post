# Telegram_bot_post

## Описание:
https://t.me/ivan_shaman_bot - telegram бот, который при старте запросит номер телефона клиента, отправит запрос на приемщик и отпишется клиенту в боте об успехе.

Когда добавили бота, отображается Start, при клике на webhook уходит соответствующий запрос, если это именно первый Start, то отправляем через https://core.telegram.org/bots/api#sendmessage сообщение “Привет, а дай номер”. Через reply_markup добавляем кнопку с параметром request_contact, чтобы при клике на нее отправлялся номер клиента на webhook.

Если нам приходит номер(клик по кнопке пункта 4), то отправляем его POST запросом на https://s1-nova.ru/app/private_test_python/

## Установка и запуск проекта на локальном компьютере:

#### 1. Клонируйте репозиторий:
```bash
git clone git@github.com:Strannik1922/Map_of_Nizhny_Novgorod.git
```

#### 2. Создайте и активируйте виртуальную среду:
```bash
python -m python venv
source python/Scripts/activate
```

#### 3. Обновить pip:
```bash
python -m pip install --upgrade pip
```

#### 4. Импорт requirements.txt
```bash
pip install -r requirements.txt
```
## Использование бота:

#### 1. Активируйте бота командой:
```bash
/start
```
#### 2. После успешной активации введите команду:
```bash
/number
```

#### 3. Нажмите на  появившуюся кнопку:
```bash
"ОТПРАВИТЬ НОМЕР"
```

## Токен вашего бота:

#### 1. Создайте файл config.py и поместите туда свой токен telegram бота:
```bash
token = '...'
```