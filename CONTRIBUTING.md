# Contributing

## Environment setup for development

1. Create virtual environment
2. Install packages in requirements.txt file
3. For testing install requests

On windows create a env.bat file in the parent folder. The contents of the bat file are:

```bat
set FLASK_APP=app/main.py
set FLASK_ENV=development
```

Before starting the application run the bat script on terminal: `env.bat`
Once the environment variables are set, start the application using `flask run`.
