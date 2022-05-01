# For Twitch EventSub API

## Things I will need
* callback URL
* ngrok or public instance
* buy a URL for the project
* ssl certificate
* Return 200 ok when receiving a webhook
* I need a `Twitch EventSub Secret?`

## Flow as I understand it
---https://dev.twitch.tv/docs/eventsub/eventsub-subscription-types---

1. Stream Helper subscribes to topics at Twitch EventSub
  a. stream online
2. My service listens for twitch to call it
3. My service receives a POST
4. My service does something
5. ???
6. Profit

## Stuff to read/research
* TWITCH ACCESS TOKENS
* TWITCH EVENTSUB SECRETS

