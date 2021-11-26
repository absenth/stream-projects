FROM python
COPY . /src
ENV TWITCH_OAUTH_TOKEN "TWITCH_OAUTH_TOKEN"
CMD pip install numpy pandas socket json urllib requests collections
CMD["python", "/src/main.py"]
