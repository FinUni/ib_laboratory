### presentations
#### если надо добавить презентацию:
* кладём её в папочку presentations [иначе проблема с доступами]
* запускаем файл add_presentation.py, ```FILE_NAME = name_of_presentation.pptx```


#### если надо удалить презентацию:
* кладём её в папочку presentations [иначе проблема с доступами]
* запускаем файл delete_presentation.py, ```FILE_NAME = name_of_presentation.pptx```

### Calendars

#### Google Calendar

* Для авторизации через сервис необходимо достать файл .json из пункта Credentials в Google Console [```https://console.cloud.google.com/```]
* Путь к файлу прописать в параметре `flow` 


## TODO: 
* дебаг проблем с доступом в презентациях
* почему чтобы удалить презу её сначала надо куда-то положить? разобрать доступы