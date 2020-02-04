# Python 3.7

import os
import subprocess
from pathlib import Path


def prepare_docker_build(file_path, hub_username):
    file_dir = file_path.split("/Dockerfile")[0]
    splitted_dir = file_dir.split("/")
    name = splitted_dir[0]  # libtorch
    tag = hub_username + "/" + name 
    if len(splitted_dir[1:]) > 0:
        tag += ":" + "_".join(splitted_dir[1:])  # 1.3.1_cpu
    return file_dir, tag


def run_command(command):
    try:
        process = subprocess.run(
            command, shell=True, capture_output=True, check=True, universal_newlines=True)
        return process.stdout
    except subprocess.CalledProcessError as error:
        return f"Exception Occured: {str(error)}"

def docker_build(command):
    return_code = os.system(command)
    if return_code != 0:
        print("There is a problem !!!")


if __name__ == "__main__":

    COMMAND_CHANGED_DOCKERFILES = "git diff-tree --no-commit-id --name-only -r 5b1705b68444794feb7cf41d531c85b5a6c5e027"
    DOCKERHUB_USERNAME = "fatihbaltaci"

    process_git = run_command(COMMAND_CHANGED_DOCKERFILES)
    output = process_git.splitlines()

    for file_path in output:
        if not "Dockerfile" in file_path:
            continue
        print("Changed Dockerfile: " + file_path)

        dockerfile_dir, image_tag = prepare_docker_build(file_path=file_path, hub_username=DOCKERHUB_USERNAME)

        docker_file_path = Path(dockerfile_dir) / "Dockerfile"

        COMMAND_BUILD_DOCKER_FILE = f"docker build --tag {image_tag} -f {docker_file_path} . "
        
        print(COMMAND_BUILD_DOCKER_FILE)
        docker_build(COMMAND_BUILD_DOCKER_FILE)
