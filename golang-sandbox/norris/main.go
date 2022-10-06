package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

// URL: https://api.chucknorris.io/jokes/random?category=dev

type data struct {
	Created_at  string `json:'created_at'`
	Icon_url    string `json:'icon_url`
	ID          string `json:'id'`
	Uploaded_at string `json:'uploaded_at'`
	Url         string `json:'url'`
	Value       string `json:'value'`
}

func main() {
	url := "https://api.chucknorris.io/jokes/random?category=dev"

	resp, getErr := http.Get(url)
	if getErr != nil {
		log.Fatal(getErr)
	}

	body, readErr := ioutil.ReadAll(resp.Body)
	if readErr != nil {
		log.Fatal(readErr)
	}

	data_obj := data{}

	jsonErr := json.Unmarshal(body, &data_obj)
	if jsonErr != nil {
		log.Fatal(jsonErr)
	}

	fmt.Println(data_obj.Value)

}
