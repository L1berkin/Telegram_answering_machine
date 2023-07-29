# Автоответчик telegram

Автоответчик на время отпуска :) [подробнее](https://medium.com/@jiayu./automatic-replies-for-telegram-85075f28321)

1. Зарегистрировать приложение в [API telegram](https://my.telegram.org/apps) ([документация](https://core.telegram.org/api/obtaining_api_id))

2. Заполнить переменные в .env file:
```
API_ID={цифровой номер}
API_HASH={hash строка}
PHONE={номер телефона}
SESSION_FILE={название существующего файла сессии}
PASSWORD={пароль от аккаунта}
TPPROXY={домен прокси}
PPORT={порт, например 443}
PKEY={пароль от прокси}
```
Файл сессии появляется после первого запуска с ручной авторизацией в терминале. Перед первым запуском прописать все переменные в коде. А потом использовать, например, в докере.
3. Стартануть докер-контейнер
`docker-compose -f "docker-compose.yml" up -d --build`

