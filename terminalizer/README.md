
```bash
docker run -it --rm --privileged -v $HOME/gifs:/home/node/gifs -v config:/home/node/.terminalizer fatihbaltaci/terminalizer bash
```

```bash
terminalizer record hello
xvfb-run -s "-screen 0 1920x1080x16" terminalizer render hello -o hello.gif
```
