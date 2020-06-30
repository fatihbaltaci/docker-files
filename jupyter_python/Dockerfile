FROM python:3.7

LABEL maintainer="baltacifatih14@gmail.com"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y wget vim unzip zip curl tzdata pandoc && rm -rf /var/lib/apt/lists/*

RUN pip3 --no-cache-dir install \ 
        opencv-contrib-python==4.2.0.34 \ 
        mlflow==1.7.2 \ 
        youtube_dl==2020.3.24 \ 
        scikit-image==0.16.2 \ 
        matplotlib==3.2.1 \ 
        Pillow==7.1.1 \ 
        Cython==0.29.16 \ 
        wget==3.2 \ 
        future==0.18.2 \ 
        jupyterlab==2.1.0 \ 
        ipywidgets==7.5.1 \ 
        tqdm==4.45.0 \ 
        pandas==1.0.3 \ 
        numpy==1.18.2 \ 
        scipy==1.4.1 \ 
        seaborn==0.10.0 \ 
        scikit-learn==0.22.2.post1 \ 
        plotly==4.6.0

COPY jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py

ENV PASSWORD="Jupyter"
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# change timezone
RUN ln -sf /usr/share/zoneinfo/Turkey /etc/localtime

WORKDIR /workspace

CMD [ "jupyter", "lab" ]
