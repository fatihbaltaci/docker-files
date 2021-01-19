# Run Container

```bash
mkdir -p .ssh && mkdir -p .config/redial && docker run -it --rm --workdir="/home/$USER" -u $(id -u ${USER}):$(id -g ${USER}) -v "/etc/group:/etc/group:ro" -v "/etc/passwd:/etc/passwd:ro" -v $HOME/.config/redial:$HOME/.config/redial -v $HOME/.ssh:$HOME/.ssh fatihbaltaci/redial
```
