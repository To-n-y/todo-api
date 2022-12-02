### REST API
В этом проекте вы найдёте Dockerfile и docker-compose.yaml. Последний указанный файл запускает контейнер API для списка ToDo.

### Предварительные требования использования приложения
- Docker

P.S. Можно установить Docker Toolbox, если у вас Windows более раннего выпуска, нежели Windows 10.

### Запуск приложения 
1. Склонируйте репозиторий `git clone https://github.com/To-n-y/todo-api.git [<dir_name>]`;
2. Перейдите в папку командой `cd <dir_name>`;
3. Создайте файл конфигураций .env:
   - сделайте копию шаблона файла .env `cp .env.template .env`;
   - присвойте актуальные значения всем полям.
4. Чтобы примонтировать базу данных, зайдите в Docker и далее Settings -> Resources -> FileSharing. Добавьте папку db и нажмите Apply & Restart
5. Запустите контейнеры `docker-compose up -d`;
6. Когда проект будет запущен, перейдите на `localhost:80` и проверьте, что видите надпись 'Not Found'. Если вы установили Docker Toolbox, перейдите по адресу `http://192.168.100.14:80`.

Отлично! Всё работает.
