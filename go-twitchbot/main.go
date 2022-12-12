package main

import (
	"database/sql"
	"fmt"
	cf "go-twitchbot/commands/catfacts"
	df "go-twitchbot/commands/dogfacts"
	il "go-twitchbot/commands/islive"
	nj "go-twitchbot/commands/norris"
	"log"
	"os"
	"strings"

	"github.com/gempir/go-twitch-irc/v3"
	"github.com/joho/godotenv"
	_ "github.com/mattn/go-sqlite3"
	chatbot "github.com/vikpe/twitch-chatbot"
)

type Twitchcommand struct {
	id          int
	bottrigger  string
	botresponse string
}

func main() {
	// init database
	db, errDB := sql.Open("sqlite3", "textcommands.db")
	if errDB != nil {
		log.Println(errDB)
	}

	statement, errDB := db.Prepare("CREATE TABLE IF NOT EXISTS commands (id INTEGER PRIMARY KEY, bottrigger VARCHAR(64), botresponse VARCHAR(64) )")
	if errDB != nil {
		log.Println("Error in creating table")
	} else {
		log.Println("Successfully created the commands table")
	}
	statement.Exec()

	// init
	err := godotenv.Load()
	check(err)

	username := "botsenth545"
	oauth := os.Getenv("TWITCH_OAUTH_TOKEN")
	channel := "absenth762"
	commandPrefix := '!'

	myBot := chatbot.NewChatbot(username, oauth, channel, commandPrefix)

	// event callbacks
	myBot.OnStarted = func() { fmt.Println("chatbot started") }
	myBot.OnConnected = func() { fmt.Println("chatbot connected") }
	myBot.OnStopped = func(sig os.Signal) {
		fmt.Println(fmt.Sprintf("chatbot stopped (%s)", sig))
	}

	// command handlers
	myBot.AddCommand("joke", func(cmd chatbot.Command, msg twitch.PrivateMessage) {
		myBot.Say(nj.Norris())
	})

	myBot.AddCommand("catfact", func(cmd chatbot.Command, msg twitch.PrivateMessage) {
		myBot.Say(cf.Catfacts())
	})

	myBot.AddCommand("dogfact", func(cmd chatbot.Command, msg twitch.PrivateMessage) {
		myBot.Say(df.Dogfacts())
	})

	myBot.AddCommand("live", func(cmd chatbot.Command, msg twitch.PrivateMessage) {
		if !chatbot.IsBroadcaster(msg.User) {
			myBot.Reply(msg, "Only Absenth762 can announce the stream.")
			return
		}

		il.Islive()
		myBot.Reply(msg, "I have announced the stream.")
	})

	myBot.AddCommand("newcommand", func(cmd chatbot.Command, msg twitch.PrivateMessage) {
		if !chatbot.IsBroadcaster(msg.User) {
			myBot.Reply(msg, "Only Absenth762 can create newcommands.")
			return
		}

		Addtrigger(db, cmd.ArgsToString())
		myBot.Reply(msg, fmt.Sprintf("I have added the %s command", cmd.ArgsToString()))
	})

	myBot.AddCommand("delcommand", func(cmd chatbot.Command, msg twitch.PrivateMessage) {
		if !chatbot.IsBroadcaster(msg.User) {
			myBot.Reply(msg, "Only Absenth762 can remove commands.")
			return
		}

		Deltrigger(db, cmd.ArgsToString())
		myBot.Reply(msg, fmt.Sprintf("I have removed the %s command", cmd.ArgsToString()))
	})

	myBot.AddCommand("updatecommand", func(cmd chatbot.Command, msg twitch.PrivateMessage) {
		if !chatbot.IsBroadcaster(msg.User) {
			myBot.Reply(msg, "Only Absenth762 can update commands.")
			return
		}

		Updatetrigger(db, cmd.ArgsToString())
		myBot.Reply(msg, fmt.Sprintf("I have updated the %s command", cmd.ArgsToString()))
	})

	rows, _ := db.Query("SELECT bottrigger, botresponse FROM commands")
	var tempCommand Twitchcommand
	for rows.Next() {
		rows.Scan(&tempCommand.bottrigger, &tempCommand.botresponse)
		myBot.AddCommand(tempCommand.bottrigger, func(cmd chatbot.Command, msg twitch.PrivateMessage) {
			myBot.Say(tempCommand.botresponse)
		})

	}

	myBot.Start() // blocking operation
}

func Addtrigger(db *sql.DB, trigger string) string {
	split := strings.Split(trigger, " ")
	btrigger, bresponse := split[0], split[1:]
	bresponse2 := strings.Join(bresponse, " ")

	statement, err := db.Prepare("INSERT INTO commands (bottrigger, botresponse) VALUES (?, ?)")

	check(err)

	_, err = statement.Exec(btrigger, bresponse2)

	check(err)

	response := ("Sucessfully created the command")
	return response
}

func Deltrigger(db *sql.DB, trigger string) string {
	split := strings.Split(trigger, " ")
	btrigger := split[0]
	statement, err := db.Prepare("delete from commands where bottrigger=?")

	check(err)

	_, err = statement.Exec(btrigger)

	check(err)

	response := ("Sucessfully deleted the command")
	return response
}

func Updatetrigger(db *sql.DB, trigger string) string {
	statement, err := db.Prepare("update commands set botresponse=? where bottrigger=?")
	split := strings.Split(trigger, " ")
	btrigger, bresponse := split[0], split[1:]
	bresponse2 := strings.Join(bresponse, " ")

	check(err)

	_, err = statement.Exec(bresponse2, btrigger)

	check(err)

	response := ("Successfully updated the command")
	return response
}

func check(err error) {
	if err != nil {
		log.Fatal(err)
	}
}
