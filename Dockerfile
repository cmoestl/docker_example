FROM python:3.7

ADD requirements.txt /home/cmoestl/pycode/docker_example/


ADD app.py /home/cmoestl/pycode/docker_example/

WORKDIR /home/cmoestl/pycode/docker_example/

RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]