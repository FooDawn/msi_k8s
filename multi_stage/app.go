package main

import (
    "fmt"
    "log"
    "net/http"
)

func main() {
    fmt.Println("Hello, World!")
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Hello, you've requested: %s\nFor more go to localhost:5001 or localhost:8080", r.URL.Path[1:])
    })

    log.Fatal(http.ListenAndServe(":5002", nil))
}

