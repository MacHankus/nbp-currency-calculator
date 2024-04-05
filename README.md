# Description
It is a simple application made with python, react and postgresql database.
Application is ment to calculate values from one currency to other.
Main tool used for calculation is [NBP API](https://api.nbp.pl/#info).

# How to use it
From root folder run
```
docker-compose -f docker-compose.dev.yaml up
```
After containers are started you can explore docs made for API under http://localhost:9000/docs .
UI will be available under http://localhost:9003.
There is one endpoint that calculates value of target currency depending on given curerncy and its amount and one endpoint which gives history of exchanges.
Each exchange is persisted in DB inside public.exchange_history table.

Frontend presents simple form to calculate currency and retrieve exchanges history.

DB Migration is called before API starts, so database schama is prepared.
DB will be available by host=localhost, port=9001, dbname=currency, username=postgres, password=postgres.


