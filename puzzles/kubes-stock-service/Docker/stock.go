package main

import (
    "io/ioutil"
    "fmt"
    "os"
    "log"
    "net/http"
    "encoding/json"
    //"time"
)

func main() {
    fmt.Println("Querying Stock API...")
    var symbol  string = os.Getenv("SYMBOL")
    //var days string = os.Getenv("NDAYS")

    site := fmt.Sprintf("https://www.alphavantage.co/query?apikey=1123&function=TIME_SERIES_DAILY_ADJUSTED&symbol=%s", symbol)
    fmt.Println(site)

    res, err := http.Get(site)
    if err != nil {
        log.Fatal(err)
    }
    defer res.Body.Close()

    content, err := ioutil.ReadAll(res.Body)
    if err != nil {
        log.Fatal(err)
    }

    responseString := string(content)
    //fmt.Println(responseString)

    var out map[string]interface{}

    json.Unmarshal([]byte(responseString), &out)
    for i := range out["Time Series (Daily)"].(map[string]interface{}) {
        fmt.Println(i)
    }

    //fmt.Println("sleeping...")
    //time.Sleep(time.Second * 5)

}
