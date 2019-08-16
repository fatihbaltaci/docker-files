FROM pytorch/pytorch:1.0-cuda10.0-cudnn7-runtime

MAINTAINER Fatih Baltacı "baltacifatih14@gmail.com"

RUN apt-get update && apt-get install -y wget vim unzip libgtk2.0-dev swig

RUN pip --no-cache-dir install \
	opencv-contrib-python==4.1.0.25 \
	mlflow==0.9.1 \
	youtube-dl \
	scikit-image==0.13.1 \
	matplotlib==3.1.0 \
	Pillow==5.3.0 \
	Cython==0.29.9 \
	wget==3.2 \
	future==0.17.1 \
	jupyterlab==1.0.5

COPY jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py

ENV PASSWORD="Jupyter"

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# change timezone
RUN ln -sf /usr/share/zoneinfo/Turkey /etc/localtime

WORKDIR /workspace

CMD [ "jupyter", "notebook" ]