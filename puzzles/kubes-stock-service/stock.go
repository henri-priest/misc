package main

import (
    "io/ioutil"
    "fmt"
    "os"
    "net/http"
)

func main() {
    fmt.Println("Querying Stock API...")
    var symbol  string = os.Getenv("SYMBOL")
    //var days string = os.Getenv("NDAYS")
    site := fmt.Sprintf("https://www.alphavantage.co/query?apikey=1123&function=TIME_SERIES_DAILY_ADJUSTED&symbol=%s", symbol)
    fmt.Println(site)
    res, err := http.Get(site)

    if err != nil {
        panic(err)
    }

    defer res.Body.Close()
    body, err := ioutil.ReadAll(res.Body)
    fmt.Println(body)

}
