package main

import (
    "io/ioutil"
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
    //var days string = os.Getenv("NDAYS")

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
    //fmt.Println(responseString)
    r := csv.NewReader(strings.NewReader(responseString))

    for i := 0; i <=5; i++ {
        record, err := r.Read()
        //if err == io.EOF {
        //    break
        //}
        if err != nil {
            log.Fatal(err)
        }
        fmt.Println(record[4])
    }

    //fmt.Println("sleeping...")
    //time.Sleep(time.Second * 5)

}
