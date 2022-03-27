## Dependencies
* Django

## Setting up

##### Clone the repo

```
$ git clone https://github.com/Andreyinweb/superDogs.git
$ cd superDogs
```

##### Initialize a virtualenv

```
$ python3 -m venv env_dog
$ . env_dog/bin/activate 
or
env_dog\Scripts\activate
```

##### Install the dependencies

```
$ cd superdog
$ pip install -r requirements.txt
```

##### Create the database

```
$ python3 manage.py migrate
```

## Running the server

```
$ python3 manage.py runserver
