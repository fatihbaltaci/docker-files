FROM pytorch/pytorch:1.4-cuda10.1-cudnn7-runtime

LABEL maintainer="baltacifatih14@gmail.com"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y wget vim unzip libgtk2.0-dev swig tzdata && rm -rf /var/lib/apt/lists/*

RUN pip --no-cache-dir install \
        opencv-contrib-python==4.1.0.25 \
        mlflow==0.9.1 \
        youtube-dl \
        scikit-image==0.16.2 \
        matplotlib==3.1.0 \
        Pillow==5.3.0 \
        Cython==0.29.9 \
        wget==3.2 \
        future==0.17.1 \
        jupyterlab==1.2.4 \
        ipywidgets \
        tqdm


COPY jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py

ENV PASSWORD="Jupyter"

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# change timezone
RUN ln -sf /usr/share/zoneinfo/Turkey /etc/localtime

WORKDIR /workspace

CMD [ "jupyter", "lab" ]
