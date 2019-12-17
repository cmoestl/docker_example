import numpy as np
import matplotlib.pyplot as plt
import os
import input

print()
print()
print(os.getcwd())
print(os.listdir())

print(input.a)

print('hello ',np.arange(10))

print('asdasdas222222')

plt.plot(np.arange(10))

plt.savefig('test2.png')

os.system('chmod 777 test2.png')

print(os.listdir())


print()
print()


#use
#sudo docker build -t app .

#sudo docker run -v /home/cmoestl/pycode/docker_example/://home/cmoestl/pycode/docker_example/ app


#sudo docker run app

#sudo docker rmi -f  f953db841197 
#sudo sh docker_shell.sh

#docker save -o ph.tar python-hello
#docker load -i ph.tar 

#docker without sudo
#https://github.com/sindresorhus/guides/blob/master/docker-without-sudo.md
#https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user
# sudo groupadd docker
#newgrp docker
#sudo usermod -aG docker $USER



#sudo docker volume create app-volume


'''
FROM python:3.7

COPY . appdir

ADD app.py /

RUN pip install -r requirements.txt

CMD [ "python", "./app.py" ]
'''