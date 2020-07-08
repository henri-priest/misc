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

    type Message struct {
	    "2020-02-13": {
		"1. open": "2144.9900",
	        "2. high": "2170.2800",
		"3. low": "2142.0000",
		"4. close": "2149.8700",
		"5. adjusted close": "2149.8700",
		"6. volume": "3031791",
		"7. dividend amount": "0.0000",
		"8. split coefficient": "1.0000"
	      }
    {
    var out string

    json.Unmarshal([]byte(responseString), &out)
    fmt.Print(out)

    //fmt.Println("sleeping...")
    //time.Sleep(time.Second * 5)

}
