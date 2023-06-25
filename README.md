Lumberjack Client
=================

Installable Django app.  Includes handlers to send logs to the Lumberjack server.

[Lumberjack Server](https://github.com/edjchapman/lumberjack)

# Installation

1. Install into project:

    ```
    pip install git+https://github.com/edjchapman/django-lumberjack-client.git@1.0.0 
    ```
2. Add "lumberjack" to your INSTALLED_APPS:

    ``` 
    INSTALLED_APPS = [
        ...
        'lumberjack',
    ]
    ```
3. Point the Django exception mail_admins handler to the Lumberjack exception handler:

   ```python
    # https://docs.djangoproject.com/en/dev/topics/logging/#examples
   
   LOGGING = {
      'handlers': {
           'mail_admins': {
               'level': 'ERROR',
               'class': 'lumberjack.handlers.ExceptionHandler',
           },
       },
   }
   ```
4. Configure the destination and description for logs to be sent to the server in the main Django conf
   ```python
   LUMBERJACK_URL = 'https://lumberjack-server-url.com/api/'
   PROJECT_NAME = 'PROJECT_NAME'
   APPENV = 'PRODUCTION'
   APP_LOCATION = 'LONDON'
   ```

# Development

## Setup Environment
```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run tests
```shell
source venv/bin/activate
python -m run_tests
```

## Install on a locally running Django project
```shell
pip install --editable /path/to/django-lumberjack-client
```

# Release
1. Increment version number in setup.py
2. Commit and push changes.
3. Create release on GitHub with the version number.
4. The release can then be installed into Django projects like this:
    ``` 
    git+https://github.com/edjchapman/django-lumberjack-client.git@{tag_or_branch}
    ```
