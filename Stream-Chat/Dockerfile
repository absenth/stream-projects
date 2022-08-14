FROM python
COPY . /src
CMD python -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD [ "python", "/src/main.py"]
