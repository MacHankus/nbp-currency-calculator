# Description
It is a simple application made with python, react and postgresql database.
Application is ment to calculate values from one currency to other.
Main tool used for calculation is [NBP API](https://api.nbp.pl/#info).

# How to use it
From root folder run
```
docker-compose -f docker-compose.dev.yaml up
```
After containers are started you can explore docs made for API.
DB Migration is called before API starts.
Then in the browser go to http://localhost:9000/docs to explore backend API. 
There is one endpoint that calculates value of target currency depending on given curerncy and its amount.
More details under the docs and `schema` section.
Each request is persisted in DB inside public.request_history table.

DB will be available by host=localhost, port=9001, dbname=currency, username=postgres, password=postgres.


Fronted :
**WORK IN PROGRESS**
Code for frontend is inside repository, container is still not working. 
Fronted is able to show basic form but not working yet.