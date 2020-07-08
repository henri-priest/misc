package main

import (
    "io/ioutil"
    "strconv"
    //"io"
    "fmt"
    "os"
    "log"
    "net/http"
    "encoding/csv"
    "strings"
    //"time"
)

func main() {
    fmt.Println("Querying Stock API...")
    var symbol  string = os.Getenv("SYMBOL")
    var days string = os.Getenv("NDAYS")

    site := fmt.Sprintf("https://www.alphavantage.co/query?apikey=1123&function=TIME_SERIES_DAILY_ADJUSTED&symbol=%s&datatype=csv", symbol)
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
    r := csv.NewReader(strings.NewReader(responseString))

    max, err := strconv.Atoi(days)
    var total float32 = 0;
    for i := 0; i <= max; i++ {
        record, err := r.Read()
        if err != nil {
            log.Fatal(err)
        }
        fmt.Println(record[4])
        if i > 0 {
            value, err := strconv.ParseFloat(record[4], 32)
            if err != nil {
               log.Fatal(err)
            }
            total += float32(value)
        }
    }

    total = total / float32(max)
    fmt.Println(total)

    //fmt.Println("sleeping...")
    //time.Sleep(time.Second * 5)

}
