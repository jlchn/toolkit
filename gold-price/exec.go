package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/PuerkitoBio/goquery"
)

func fetch() string {
	resp, err := http.Get("http://www.dyhjw.com/hjtd/")
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != 200 {
		log.Fatalf("Status code error: %d %s", resp.StatusCode, resp.Status)
	}
	doc, err := goquery.NewDocumentFromReader(resp.Body)
	if err != nil {
		log.Fatal(err)
	}
	price := doc.Find("div.price_bd span.last").Text()
	fmt.Println(price)
	return price
}

func alert(alertOverSource string, alertOverReceiver string, text string) {

	requestBody, err := json.Marshal(map[string]string{
		"source":   alertOverSource,
		"receiver": alertOverReceiver,
		"content":  "Gold price today: " + text,
		"title":    text,
	})

	if err != nil {
		log.Fatalln(err)
	}

	response, err := http.Post("https://api.alertover.com/v1/alert", "application/json", bytes.NewBuffer(requestBody))

	if err != nil {
		log.Fatalln(err)
	}

	defer response.Body.Close()

}

func main() {

	if len(os.Args) != 3 {
		panic("alertover credential must be provided!")
	}

	price := fetch()
	alert(os.Args[1], os.Args[2], price)
}
