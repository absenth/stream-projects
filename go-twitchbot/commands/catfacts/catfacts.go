package catfacts

import (
	"encoding/json"
	"io/ioutil"
	"log"
	"net/http"
)

// URL: https://catfact.ninja/fact

type data struct {
	Fact   string `json:'fact'`
	Length int    `json:'length'`
}

func Catfacts() string {
	url := "https://catfact.ninja/fact"

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

	// fmt.Println("fact", data_obj.Fact)
	fact := data_obj.Fact
	return fact
}
