# Real Estate Site

This site is a simple real estate listing with filter by town or settlement and price. Based on Flask with SQLite and SQLAlchemy. Script for export from json also available.


# How to Install

Python 3.6 and libraries from **requirements.txt** should be installed. Use virtual environment tool, for example **virtualenv**.

```bash

virtualenv virtualenv_folder_name
source virtualenv_folder_name/bin/activate
python3.6 -m pip install -r requirements.txt
```

Put host, port, debug mode and path to database to .env file.

```bash
HOST=127.0.0.1
PORT=5000
FLASK_DEBUG=TRUE
DB_FILE=DB_FILE
```

FLASK_DEBUG environment variable Flask loads by itself, but for PORT loading we should use python-dotenv package.

To create new database launch interactive Python shell

```bash
python3
```

and run:

```python
from app import db
db.create_all()
```

Database will be created in the **db** dir. Then, export data from **ads.json** with run **import.py**. If you do it with clean database, all entries from json will be inserted. Further export (after adding or deleting or changing entries in your json file) merges new data and existing database (inserts or hides or updates entries respectively).


# Quickstart

Run **server.py**.

```bash

$ python server.py

 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with inotify reloader
 * Debugger is active!

```

Goto [http://127.0.0.1:5000/ ](http://127.0.0.1:5000/ )


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
