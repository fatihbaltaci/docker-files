# Ubuntu 18.10

### Packages: 
* wget
* vim
* unzip
* zip
* curl

### Build Ubuntu 18.10 Dockerfile

`$ cd ubuntu_18.10`

`$ docker build -t ubuntu:18.10-full .`

# Python 3.6

### Packages: 
* urwid

### Build Python 3.6 Dockerfile

`$ cd python_3.6`

`$ docker build -t python:3.6.10-full . `


# Jupyter Notebook

`$ cd jupyter_pytorch`

`$ docker build -t jupyter:pytorch_1.0 .`


### Run as a Service

```
$ JUPYTER_FILES=/home/cluster/jupyter_files
$ docker run -dit -p 8888:8888 -v $JUPYTER_FILES:/workspace --restart=always --name=jupyter_notebook fatihbaltaci/jupyter:pytorch_1.0
```

**Default Passwork:** Jupyter
