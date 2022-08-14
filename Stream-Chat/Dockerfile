FROM python
COPY . /src
RUN python -m pip install --upgrade pip && pip install -r /src/requirements.txt
CMD [ "python", "/src/main.py"]
