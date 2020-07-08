package main

import (
    "fmt"
    "os"
    //"strings"
    //"net/url"
)

func main() {
    fmt.Println("Querying Stock API...")
    fmt.Println("Stock:", os.Getenv("SYMBOL"))
    fmt.Println("Days:", os.Getenv("NDAYS"))
    //s := "postgres://user:pass@host.com:5432/path?k=v#f"
    //res, err := url.Parse(s)
}
