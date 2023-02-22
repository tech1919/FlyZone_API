# FlyZone Main API

This API act as the main backend of the FlyZone Project. It is build with FastAPI framework, using SqlAlchemy as its ORM.

As can be seen in the `requirements.txt` file, this API depends on other python packages:


1. [fastrank](https://github.com/tech1919/fastapi-rank.git) - the main ranking system of the application
2. [fastauth](https://github.com/tech1919/fastapi-auth-cognito.git) - ready to use authentication and authorization system
3. [fastevents](https://github.com/tech1919/fastapi-events.git) - the main events and loggin system for this application

Every package for the list above is installed on top of this API and create its own dependency tables. In that way, this API repo stay light weight and very modular.

> ## Run Development Environment

For using this project, you must have the following dependencies:

1. Docker Desktop
2. Python (recommended)
3. Visual Studio Code (recommended)


Configure environment variables in an `.env` file at the [root directory](.):
```
# example .env file

# API
API_LOCAL_PORT=8000
API_NAME=FlyZone Backend

# POSTGRES ans PGADMIN
POSTGRES_USER=username
POSTGRES_PASSWORD=password
POSTGRES_DB=flyzone
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
PGADMIN_PORT=5050

# COGNITO
COGNITO_REGION=
COGNITO_POOL_ID=
COGNITO_CLIENT_ID=
```

Compose the environment by running the following command:
```bash
docker compose -f "docker-compose.dev.yml" up -d --build
```

This command should spin-up Three services:

- api - FastAPI service with all the routes at [localhost:8000](http://localhost:8000/docs)
- pgadmin - pgadmin is an admin panel for managing a postgres database. it should show in [localhost:5050](http://localhost:5050/). to connect, simply enter the info:

    - Email : ${POSTGRES_USER}@admin.com
    - Password : ${POSTGRES_PASSWORD}
- postgres - the database using postgres service and running on port 5432.


> ## CI/CD

TBD (Ofry)