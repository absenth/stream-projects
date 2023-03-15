package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"

	"github.com/bwmarrin/discordgo"
)

var (
	Token     string
	BotPrefix string

	config *configStruct
)

type configStruct struct {
	Token     string `json : "Token"`
	BotPrefix string `json : "BotPrefix"`
}

func ReadConfig() error {
	fmt.Println("Reading config file...")
	file, err := ioutil.ReadFile("./config.json")

	if err != nil {
		fmt.Println(err.Error())
		return err
	}

	fmt.Println(string(file))

	err = json.Unmarshal(file, &config)

	if err != nil {
		fmt.Println(err.Error())
		return err
	}
	Token = config.Token
	BotPrefix = config.BotPrefix

	return nil

}

var BotId string
var goBot *discordgo.Session

func Start() {
	goBot, err := discordgo.New("Bot " + config.Token)

	if err != nil {
		fmt.Println(err.Error())
		return
	}

	u, err := goBot.User("@me")

	if err != nil {
		fmt.Println(err.Error())
		return
	}

	BotId = u.ID

	goBot.AddHandler(messageHandler)

	err = goBot.Open()

	if err != nil {
		fmt.Println(err.Error())
		return
	}
	fmt.Println("Bot is running !")
}

func messageHandler(s *discordgo.Session, m *discordgo.MessageCreate) {
	if m.Author.ID == BotId {
		return
	}

	if m.Content == BotPrefix+"ping" {
		_, _ = s.ChannelMessageSend(m.ChannelID, "pong")
	}
}

func main() {
	err := ReadConfig()

	if err != nil {
		fmt.Println(err.Error())
		return
	}

	Start()

	<-make(chan struct{})
	return
}
