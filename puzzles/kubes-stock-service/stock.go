package main

import (
    "fmt"
    "os"
    //"strings"
    //"net/url"
)

func main() {
    fmt.Println("Querying Stock API...")
    var symbol  string = os.Getenv("SYMBOL")
    //var days string = os.Getenv("NDAYS")
    url := fmt.Sprintf("https://www.alphavantage.co/query?apikey=1123function=TIME_SERIES_DAILY_ADJUSTED&symbol=%s", symbol)
    fmt.Println(url)
    //res, err := url.Parse(s)
}
