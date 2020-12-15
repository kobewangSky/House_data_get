FROM nvidia/cuda:10.2-runtime-ubuntu18.04

RUN apt-get update\
&& apt-get install -y openssh-server\
&& apt-get install -y net-tools\
&& apt-get install -y vim\
&& apt-get install -y zip

RUN mkdir /var/run/sshd\
&& echo 'root:password' | chpasswd\
&& sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config\
&& sed -i 's/\/usr\/lib\/openssh\/sftp-server/internal-sftp/' /etc/ssh/sshd_config\
&& sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd\
&& echo "export VISIBLE=now" >> /etc/profile

RUN apt-get install -y python3-pip\
&& apt-get install -y git\
&& pip3 install torch torchvision

RUN pip3 install Cython\
&& pip3 install matplotlib\
&& pip3 install wandb\
&&pip3 install pandas\
&&pip3 install jupyter\
&&pip3 install tqdm

RUN export PATH=$PATH:/usr/local/cuda/bin