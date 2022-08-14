FROM python
COPY . /src
WORKDIR "/src"
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
CMD [ "python", "main.py"]
