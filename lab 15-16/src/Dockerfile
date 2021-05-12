FROM python:3.9

RUN mkdir -p /usr/src/app/

WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN pip install -r library.txt
#CMD ["python", "pars.py"]
ENTRYPOINT ["python", "/usr/src/app/pars.py"]
