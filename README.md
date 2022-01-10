# Running the app
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
`python -m pip install -r requirements.txt`
4. Run dev server  
`python manage.py runserver`
5. Or run app with docker
`docker-compose up -d`

# Requirements
- Python 3.9.9
- docker
- docker-compose

# Django admin
Admin page is under `127.0.0.1:8000/_/admin` url
