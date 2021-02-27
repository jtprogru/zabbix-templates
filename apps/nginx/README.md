# Nginx status code from Access Log by Zabbix Active

Шаблон собран на базе регулярных выражений.

На хосте, к которому прикрепляется шаблон необходимо поправить макрос `{$ACCESS_LOG}` в котором указывается полный путь до `access_log`а.

При этом `access_log` должен имен JSON-формат, например вот такой:

```
# Logging configuration
log_format main '{"@timestamp":"$time_iso8601",'
                '"@source":"$server_addr",'
                '"hostname":"$hostname",'
                '"ip":"$http_x_forwarded_for",'
                '"client":"$remote_addr",'
                '"request_method":"$request_method",'
                '"scheme":"$scheme",'
                '"domain":"$server_name",'
                '"referer":"$http_referer",'
                '"request":"$request_uri",'
                '"args":"$args",'
                '"size":$body_bytes_sent,'
                '"status": $status,'
                '"responsetime":$request_time,'
                '"upstreamtime":"$upstream_response_time",'
                '"upstreamaddr":"$upstream_addr",'
                '"http_user_agent":"$http_user_agent",'
                '}';
```

- TODO: Научиться считать 99, 95, 90, 80 и 75 перцентиль;
- TODO: Научиться триггерить на процент 5xx;
