# Hashr
## Setup
1. Clone the repository:
    ```sh
    $ git clone https://github.com/teodorvoicencu/hashr.git
    $ cd hashr
    ```
2. Make sure you have docker installed or install it from [here](https://www.docker.com/get-started/).

3. Build the containers `docker-compose build`.

4. Start the containers `docker-compose up -d`.

5. Apply the migrations by running `docker-compose run web python manage.py migrate`.

6. Load the fixture data with `docker-compose run web python manage.py loaddata`.

7. The server should be running on `localhost:8000`.

## Common Tasks

| Task               | Command                                                              |
| ------------------ | ---------------------------------------------------------------------|
| Build the server   | `docker-compose build`                                               |
| Start the server   | `docker-compose up -d`                                               |
| Restart the server | `docker-compose restart`                                             |
| View server logs   | `docker-compose logs <container>`                                    |
| List containers    | `docker-compose ps`                                                  |
| Run tests          | `docker-compose run web python manage.py test --pattern="*_tests.py"`|
| Run black          | `docker-compose run web black --config ./pyproject.toml .`           |
| Run isort          | `docker-compose run web isort .`                                     |
| Run flake8         | `docker-compose run web flake8 .`                                    |