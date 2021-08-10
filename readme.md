# Restaurant API 

## App Setup 
```
git clone <link to repo>
cd restaurant_api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp env.example .env  # add corresponding values to DEBUG and SECRET_KEY values
./manage.py migrate
./manage.py runserver
```

## Run tests 
```
./manage.py test
```