package main

import (
	"fmt"
	"io"
	"net/http"
	"strings"
)

func whatismyip(w http.ResponseWriter, r *http.Request) {
	ip := strings.Split(r.RemoteAddr, ":")[0]
	io.WriteString(w, ip)
	fmt.Println(ip)
}

func main() {
	http.HandleFunc("/", whatismyip)
	http.ListenAndServe(":8080", nil)
}
