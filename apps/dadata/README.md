# DaData

Получаем данные с помощью HTTP-Agent

Официальная документация доступна [тут](https://dadata.ru/api/balance/)

Привязать к хосту шаблон `DaData` и поправить значения макросов:
- `{$DADATA_TOKEN}` - значение HTTP-заголовка `Authorization` (i.e.: `Token SuperSecretMagicToken1234567890987654321`)
- `{$DADATA_SECRET}` - значение HTTP-заголовка `X-Secret` (i.e.: `123qweasdzxc456rtyfghvbn789525d03a302d4b`)

Значения для макросов брать у разрабов проекта.
