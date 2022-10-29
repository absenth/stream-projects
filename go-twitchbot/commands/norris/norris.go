package norris

import (
	"encoding/json"
	"io/ioutil"
	"log"
	"net/http"
)

type data struct {
	Created_at  string `json:'created_at'`
	Icon_url    string `json:'icon_url`
	ID          string `json:'id'`
	Uploaded_at string `json:'uploaded_at'`
	Url         string `json:'url'`
	Value       string `json:'value'`
}

func Norris() string {

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

	// fmt.Println(data_obj.Value)
	joke := data_obj.Value
	return joke
}
