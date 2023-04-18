# General info
API for shorting given urls.

## Running the app for development
1. Clone this repository
2. Create `.env` file
    ```
    SECRET_KEY='secret_key'
    DB_NAME='url_shortener'
    DB_HOST='localhost'
    DB_USER='username'
    DB_PASS='password'
    DB_PORT=1234
    ```
3. Install requirements  
    ```
    python -m pip install -r requirements_dev.txt
    ```
    or
    ```
    pipenv install --dev
    ```
4. Run dev server  
    ```
    uvicorn app.main:app --reload
    ```
5. Test db can be run with docker
    ```
    docker-compose up -d
    ```

## Usage
After running application you can check docs under `127.0.0.1:8000/docs`

## Requirements
- Python 3.10
- docker
- docker-compose
