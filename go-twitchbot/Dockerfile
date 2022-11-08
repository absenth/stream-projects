FROM golang:bullseye
WORKDIR /app
COPY . /app
RUN go mod download
RUN go build -o /twitch-bot
CMD [ "/twitch-bot" ]
