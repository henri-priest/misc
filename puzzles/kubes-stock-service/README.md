# Kubernetes Stock Lookup webservice

...

## Setup/Dev (Windows 10)

```git clone https://github.com/henri-priest/misc.git```

```cd misc/puzzles/kubes-stock-service```

### Test stock API

```set API_KEY=123ABC```

```set SYMBOL=AMZN```

```set NDAYS=3```

```curl -s "https://www.alphavantage.co/query?apikey=%API_KEY%&function=TIME_SERIES_DAILY_ADJUSTED&symbol=%SYMBOL%"```

### Test Go code

```go run stock.go```

### Test Go code and run in local Docker container

```docker run ...```


### Publish container

```docker push ...```

### Run in Minikube

```minikube start --driver=docker```


### Publish Kubernetes manifest

...

## Final test- Run in clean Linux VM

...
