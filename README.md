# Twitter topics

#image of current status https://imgur.com/a/vLqnnik


## Requirements
1. `npm install`
2. `npm install axios --save`
2. `pip install -r requirements.txt`
3. `pip install searchtweets`
4. `pip install -U python-dotenv`
5. `sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs`
6. `pip install psycopg2-binary`
7. `pip install Flask-SQLAlchemy==2.1`
8. `pip install azure-ai-textanalytics==5.2.0b1`

## API's used
1. Microsoft textanalytics
2. twitter API

## Setup
1. Run `echo "DANGEROUSLY_DISABLE_HOST_CHECK=true" > .env.development.local` in the project directory
2. `sudo service postgresql initdb` initialize the postgresql database
3. `sudo service postgresql start` start postgresql
4. `sudo -u postgres createuser --superuser $USER`
5. `sudo -u postgres createdb $USER`


## Run Application
1. Run command in terminal (in your project directory): `python app.py`
2. Run command in another terminal, `cd` into the project directory, and run `npm run start`
3. Preview web page in browser '/'

## Deploy to Heroku

1. Create a Heroku app: `heroku create --buildpack heroku/python`
2. Add nodejs buildpack: `heroku buildpacks:add --index 1 heroku/nodejs`
3. Push to Heroku: `git push heroku main`
