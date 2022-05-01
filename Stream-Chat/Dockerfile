FROM python
COPY . /src
ENV TWITCH_OAUTH_TOKEN "$TWITCH_OAUTH_TOKEN"
ENV OPENWEATHERMAP_API "$OPENWEATHERMAP_API"
CMD pip install --upgrade pip
CMD pip install numpy pandas socket json urllib requests collections
CMD [ "python", "/src/main.py"]
