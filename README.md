# Rapid Quotes ~ [![Python3-shield]](https://www.python.org/) [![version-shield]]() [![license-shield]]() [![flask-require-shield]]()

### Deployment Commands
``` bash
set FLASK_CONFIG=development
set SECRET_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
python manage.py runserver
pause
```

```bash
## (Environment Arg) ~ FLASK_CONFIG = [development | production | testing]  (View - ./core/config.py)
## (Environment Arg) ~ SECRET_KEY = "A long Random Hard to Guess String (Symbols/Alpha/Numbers) (View - ./core/config.py)
```

[version-shield]: https://img.shields.io/badge/version---dev-yellowgreen.svg "dev"
[Python3-shield]: https://img.shields.io/badge/Python3%2B-3.6-blue.svg "Python3+"
[license-shield]: https://img.shields.io/badge/license-MIT-lightgrey.svg "License"
[flask-require-shield]: https://img.shields.io/badge/requires-Flask%201.0%2B-yellow.svg "Flask"