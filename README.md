# Description
It is a simple application made with python, react and postgresql database.
Application is ment to calculate values from one currency to other.
Main tool used for calculation is [NBP API](https://api.nbp.pl/#info).

# How to use it
From root folder run
```
docker-compose -f docker-compose.dev.yaml up
```

Then in the browser go to http://localhost:9000/docs to explore backend api.
DB will be available by host=localhost, port=9001, dbname=currency, username=postgres, password=postgres.
