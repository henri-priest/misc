# Kubernetes Stock Lookup webservice

...

## Setup

```git clone git@github.com:henri-priest/misc.git```

```cd misc/puzzles/kubes-stock-service```

### Test stock API

```export API_KEY=123ABC```

```export SYMBOL=AMZN```

```export NDAYS=3```

```curl -s "https://www.alphavantage.co/query?apikey=$API_KEY&function=TIME_SERIES_DAILY_ADJUSTED&symbol=$SYMBOL"```

### Test Go code

```go run stock.go```

### Test Go code and run in local Docker container

```docker build --tag go-web-app:1.0 .```

```export API_KEY=123ABC; export SYMBOL=AMZN; export NDAYS=3```

```docker run --env API_KEY=$API_KEY --env SYMBOL=$SYMBOL --env NDAYS=$NDAYS  --publish 8080:8080 --detach --name go-web-app:1.0```

### Publish container

```docker build --tag go-web-app:1.0 .```

```docker tag go-web-app:1.0 hpriest445/go-web-app:1.0```

```docker push hpriest445/go-web-app:1.0```

### Run in Minikube

```minikube start --driver=docker```


### Publish Kubernetes manifest

...

## Final test- Run in clean Linux VM

...
