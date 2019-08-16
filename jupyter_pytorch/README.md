### Run as a Service

```
$ JUPYTER_FILES=/home/cluster/jupyter_files
$ docker run -dit -p 8888:8888 -v $JUPYTER_FILES:/workspace --restart=always --name=jupyter_notebook fatihbaltaci/jupyter:pytorch_1.0
```

**Default Password:** Jupyter


### Dependencies

```
	opencv-contrib-python==4.1.0.25
	mlflow==0.9.1 
	youtube-dl 
	scikit-image==0.13.1 
	matplotlib==3.1.0 
	Pillow==5.3.0 
	Cython==0.29.9 
	wget==3.2 
	future==0.17.1 
	jupyterlab==1.0.5
```