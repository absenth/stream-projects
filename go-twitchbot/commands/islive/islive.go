package islive

import (
	"github.com/gtuk/discordwebhook"
	"log"
	"os"
)

func Islive() {
	url := os.Getenv("DISCORD_WEBHOOK_URL")
	var username = "Botsenth545"
	var content = "Absenth762 just went live on Twitch\n\n Watch live >> https://twitch.tv/absenth762"

	message := discordwebhook.Message{
		Username: &username,
		Content:  &content,
	}

	err := discordwebhook.SendMessage(url, message)
	if err != nil {
		log.Fatal(err)
	}
}
