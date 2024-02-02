
# Task Manager

The Task Manager Django app is a user-friendly tool for organizing tasks efficiently. With features like task creation, updating, and deletion, users can manage their workload effortlessly. The app includes an authentication system to safeguard user data. Prioritization options help users focus on critical tasks, while filtering by priority and completion status streamlines task organization. The responsive design ensures accessibility across devices. Overall, the Task Manager offers a seamless experience, enabling users to stay organized and productive in their personal and professional endeavors.


Getting started
---------------

Create a virtual enviroment to work inside.

```bash
$ python -m venv .venv
```

Activate virtual environment

```bash
$ .venv/Scripts/activate

```



Clone repository 

```bash
$ git clone {{repo name }}
```



Install requirements file.

```bash
$ pip install -r requirements.txt
```


Change directory to *task_manager*

```bash
$ cd task_manager
```


add migration

```bash
$ python manage.py makemigration
$ pyhon manage.py migrate
$ python manage.py createsuperuser
```


Start server

```bash
$ python mange.py runserver
```

API route 

```bash
//for tasks http request
$ http://localhost:8000/taskapi/v1

//get all tasks
$http://localhost:8000

//get a task
$http://localhost:8000/details/{task.id}

//login route
$http://localhost:8000/login

//signup route
$http://localhost:8000/singup

//for admin panel
$ http://localhost:8000/admin
```
