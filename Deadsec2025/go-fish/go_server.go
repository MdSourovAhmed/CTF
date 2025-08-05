package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
)

type RequestBody struct {
	Req string `json:"request"`
	Username string `json:"username"`
	Password string `json:"password"`
	Token string `json:"token"`
}

func goHandler(w http.ResponseWriter, r *http.Request) {
	log.Printf("Received request from %s: %s %s", r.RemoteAddr, r.Method, r.URL.Path)

	if r.Method != http.MethodPost {
		http.Error(w, "Method Not Allowed", http.StatusMethodNotAllowed)
		log.Printf("Rejected: Method %s not allowed", r.Method)
		return
	}

	body, err := ioutil.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "Error reading request body", http.StatusInternalServerError)
		log.Printf("Error reading body: %v", err)
		return
	}
	defer r.Body.Close()

	var reqBody RequestBody
	err = json.Unmarshal(body, &reqBody)
	if err != nil {
		fmt.Fprint(w, "Error!")
		return
	}

	if reqBody.Req == "givemeflagpls" {
		flagContent, err := os.ReadFile("flag.txt")
		if err != nil {
			http.Error(w, "Error reading flag file, please contact admins", http.StatusInternalServerError)
			return
		}
		fmt.Fprint(w, string(flagContent))
	} else if reqBody.Req == "login" {
		if reqBody.Username == "admin" && reqBody.Password != reqBody.Password {
			fmt.Fprint(w, reqBody.Token)
		} else {
			fmt.Fprint(w, "Wrong username and/or password")
		}
	} else {
		http.Error(w, "Unknown action", http.StatusInternalServerError)
	}
}

func main() {
	http.HandleFunc("/go", goHandler)
	port := ":8080"
	log.Printf("Golang server starting on port %s", port)
	log.Fatal(http.ListenAndServe(port, nil))
}

