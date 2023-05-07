### REST API
In this project you will find a Dockerfile and docker-compose.yml. The last file specified starts the API container for the ToDo list

### Application Prerequisites
- Docker

P.S. You can install Docker Toolbox if you have an older Windows release than Windows 10.

### How to run
1. clone this repo `git clone https://github.com/To-n-y/todo-api.git [<dir_name>]`
2. Go to the folder with the command `cd <dir_name>`
3. Make .env file:
   - make a copy of the template of .env file `cp .env.template .env`
   - assign actual values to all fields.
4. To mount the database, go to Docker and then do: Settings -> Resources -> FileSharing. Add db folder and push Apply & Restart
5. Run containers `docker-compose up` or `make run_container`;
6. When the project is running, go to `localhost:80` and check if you see 'Not Found'. If you have installed Docker Toolbox, go to `http://192.168.100.14:80`
7. Go to localhost:80/toDoList or check the postman collection.
