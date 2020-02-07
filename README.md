# SETUP

1. This project can be set up with `conda`.
2. Run `conda env create -f environment.yml`.
3. Note, in case you use browser plugins like NoScript: The application requires JavaScript for Resolve to work!

# RUNNING (development)

Linux
-----
```
export FLASK_APP=flaskapp
export FLASK_ENV=development
flask init-db
flask run
```

Windows (cmd)
-------
```
set FLASK_APP=flaskapp
set FLASK_ENV=development
flask init-db
flask run
```

Windows (powershell)
-------
```
$env:FLASK_APP = "flaskapp"
$env:FLASK_ENV = "development"
flask init-db
flask run
```

Note: `flask init-db` will create the necessary tables. If they already exist, they will be deleted an re-created.

# RUNNING (testing)

All OS
-----
```
pip install '.[test]'
coverage run -m pytest
coverage report
```

# RUNNING (production)

Linux
-----
```
export FLASK_APP=flaskapp
flask init-db
flask run
```

Windows (cmd)
-------
```
set FLASK_APP=flaskapp
flask init-db
flask run
```

Windows (powershell)
-------
```
$env:FLASK_APP = "flaskapp"
flask init-db
flask run
```

Note: Setting FLASK_ENV is not necessary here. If it is already set, clear it!