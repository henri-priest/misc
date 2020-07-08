package main

import (
    "io/ioutil"
    "strconv"
    "fmt"
    "os"
    "log"
    //"html"
    "net/http"
    "encoding/csv"
    "strings"
    //"time"
)

func main() {
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        value := query()
        fmt.Fprintf(w, value)
    })
    log.Fatal(http.ListenAndServe(":8080", nil))
}

func query() string{
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
    var total float64 = 0;
    for i := 0; i <= max; i++ {
        record, err := r.Read()
        if err != nil {
            log.Fatal(err)
        }
        if i > 0 {
            value, err := strconv.ParseFloat(record[4], 64)
            fmt.Printf("Date = %s, Close price = %f\n", record[0], value)
            if err != nil {
               log.Fatal(err)
            }
            total += value
        }
    }

    total = total / float64(max)
    fmt.Printf("Final average = %f\n", total)
    strAv := strconv.FormatFloat(total, 'f', -1, 64)
    if err != nil {
        log.Fatal(err)
     }

    ret := symbol + " data=[], average = " + strAv
    return ret

    //fmt.Println("sleeping...")
    //time.Sleep(time.Second * 5)

}
