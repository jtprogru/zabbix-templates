# zabbix-templates

Кастомные шаблоны для Zabbix.

Шаблоны в формате XML для версии Zabbix =<5.0.

Шаблоны в формате YAML для версии Zabbix =>5.2.

Скрипт-конвертер сделан на Python 3.9. Перед запуском установить зависимости.
```bash
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python xml2yaml.py /path/to/file.xml /path/to/file.yaml

```


- TODO: Придумать автоимпорт в zabbix;
- TODO: Сделать версионирование;
