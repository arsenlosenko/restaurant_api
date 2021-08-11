# Restaurant API 

## App Setup 
```
git clone <link to repo>
cd restaurant_api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp env.example .env  # add corresponding values to DEBUG and SECRET_KEY values
./manage.py migrate
./manage.py runserver
```

## App Usage

When all the steps from previous entry were made, API will be available from the browser via this link - http://127.0.0.1:8000/api/restaurants/

Endpoints and corresponding requests are listed below:
* POST /api/restaurants/ - create a new restaurant entry, payload should be `{"name": "<name_of_therestaurant>"}`
* GET /api/restaurants/  - get list of all restaurants saved in the database
* GET /api/restaurants/<id>/  - get information about a specific restaurant
* PUT /api/restaurants/<id>/  - change the infromation about restaurant, by recreating a new resource, payload is the same as with the POST request
* PATCH /api/restaurants/<id>/  - change the infromation about restaurant, by modifying an existing resource, payload is the same as with the POST request
* DELETE /api/restaurants/<id>/  - delete a specific entry
* GET /api/restaurants/random/  - get random restaurant entry 


## Run tests 
```
./manage.py test
```