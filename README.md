# JSON WEB TOKEN

How to use a JSON web Token with Flask.

## Start app:

The app must start with a simply command:

```
py main.py
```

Because is a didactic code and I'm not going to use enviroment vars.

## Endpoints:

All start with http://localhost:5000/api

create token:

1. http://localhost:5000/api/login

- parameters:
    - username: "maucoder" // must be this to work
    - password: str, int, etc... // all works

2. http://localhost:5000/api/verify/token

To validate our token

- parameters:
    - Authorization:
        - type: bareer token

3. http://localhost:5000/api/github/users

Get all users from a country.

- Parameters:
    - "country": some country // Colombia, Venezuela, etc...
    - Auth:
        - type: bareer token, getted in first endpoint.

## Thanks!

This is only an example of my own projects and learning, thank you for take your time using this API. See you at next time.