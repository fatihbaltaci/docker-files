### Run as a Service

```
$ JUPYTER_FILES=/home/cluster/jupyter_files
$ docker run -dit -p 8888:8888 -v $JUPYTER_FILES:/workspace --restart=always --name=jupyter_lab fatihbaltaci/jupyter
```

**Default Password:** Jupyter


### Dependencies

```
        torch==1.4.0
	torchvision==0.5.0
	opencv-contrib-python==4.1.0.25 
        mlflow==0.9.1 
        youtube-dl 
        scikit-image==0.16.2 
        matplotlib==3.1.0
        Pillow==5.3.0 
        Cython==0.29.9 
        wget==3.2 
        future==0.17.1 
        jupyterlab==1.2.4
```
