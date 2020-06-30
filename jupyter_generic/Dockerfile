FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu16.04

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 git tzdata pandoc && rm -rf /var/lib/apt/lists/*

RUN wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc

RUN pip --no-cache-dir install jupyterlab==1.0.5 ipykernel

# Kernel 1: pytorch=0.4.1 torchvision=0.2.1 cuda90
RUN conda create --name PyTorch_0.4.1_Cuda90_Vision_0.2.1 python=3.6
ENV PATH /opt/conda/envs/PyTorch_0.4.1_Cuda90_Vision_0.2.1/bin:$PATH
RUN . /opt/conda/etc/profile.d/conda.sh && conda activate PyTorch_0.4.1_Cuda90_Vision_0.2.1 && conda install pytorch=0.4.1 torchvision=0.2.1 cuda90 -c pytorch && \
     pip --no-cache-dir install \
          opencv-contrib-python==4.1.0.25 \
          mlflow==0.9.1 \
          youtube-dl \
          scikit-image==0.13.1 \
          matplotlib==3.1.0 \
          Pillow==5.3.0 \
          Cython==0.29.9 \
          wget==3.2 \
          future==0.17.1 \
          ipykernel && \
     python -m ipykernel install --name PyTorch_0.4.1_Cuda90_Vision_0.2.1


# Kernel 2: pytorch=1.1.0 torchvision=0.3.0 cuda10
RUN conda create --name PyTorch_1.1.0_Cuda10_Vision_0.3.0 python=3.6
ENV PATH /opt/conda/envs/PyTorch_1.1.0_Cuda10_Vision_0.3.0/bin:$PATH
RUN . /opt/conda/etc/profile.d/conda.sh && conda activate PyTorch_1.1.0_Cuda10_Vision_0.3.0 && conda install pytorch=1.1.0 torchvision=0.3.0 cudatoolkit=10.0 -c pytorch && \
     pip --no-cache-dir install \
          opencv-contrib-python==4.1.0.25 \
          mlflow==0.9.1 \
          youtube-dl \
          scikit-image==0.13.1 \
          matplotlib==3.1.0 \
          Pillow==5.3.0 \
          Cython==0.29.9 \
          wget==3.2 \
          future==0.17.1 \
          ipykernel && \
     python -m ipykernel install --name PyTorch_1.1.0_Cuda10_Vision_0.3.0


# Kernel 3: pytorch=1.2.0 torchvision=0.4.0 cuda10
RUN conda create --name PyTorch_1.2.0_Cuda10_Vision_0.4.0 python=3.6
ENV PATH /opt/conda/envs/PyTorch_1.2.0_Cuda10_Vision_0.4.0/bin:$PATH
RUN . /opt/conda/etc/profile.d/conda.sh && conda activate PyTorch_1.2.0_Cuda10_Vision_0.4.0 && conda install pytorch=1.2.0 torchvision=0.4.0 cudatoolkit=10.0 -c pytorch && \
     pip --no-cache-dir install \
          opencv-contrib-python==4.1.0.25 \
          mlflow==0.9.1 \
          youtube-dl \
          scikit-image==0.13.1 \
          matplotlib==3.1.0 \
          Pillow==5.3.0 \
          Cython==0.29.9 \
          wget==3.2 \
          future==0.17.1 \
          ipykernel && \
     python -m ipykernel install --name PyTorch_1.2.0_Cuda10_Vision_0.4.0



COPY jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py

ENV PASSWORD="Jupyter"

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# change timezone
RUN ln -sf /usr/share/zoneinfo/Turkey /etc/localtime

WORKDIR /workspace

RUN chmod -R a+w .

CMD [ "jupyter", "lab" ]
