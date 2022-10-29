package dogfacts

import (
	"encoding/json"
	"io/ioutil"
	"log"
	"net/http"
)

// URL: https://https://dog-api.kinduff.com/api/facts

type data struct {
	Facts []string `json:'facts'`
}

func Dogfacts() string {
	url := "https://dog-api.kinduff.com/api/facts"

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

	//fmt.Println("fact", data_obj.Facts[0])
	fact := data_obj.Facts[0]
	return fact
}
