### Run as a Service

- Specify working directory (JUPYTER_FILES) for jupyter lab. 
```
$ JUPYTER_FILES=/home/cluster/jupyter_files
$ docker run -dit -p 8888:8888 -v $JUPYTER_FILES:/workspace --restart=always --name=jupyter_lab fatihbaltaci/jupyter_generic:latest
```

**Default Password:** Jupyter

### Kernels

- Kernel 1: pytorch=0.4.1 torchvision=0.2.1 cuda90
- Kernel 2: pytorch=1.1.0 torchvision=0.3.0 cuda10
- Kernel 3: pytorch=1.2.0 torchvision=0.4.0 cuda10


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


