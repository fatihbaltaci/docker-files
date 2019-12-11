# Python 3.7

import subprocess
from pathlib import Path


def prepare_docker_build(file_path, hub_username):
    print(file_path)
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
            command, shell=True, capture_output=True, check=True)
        return process.stdout.decode("utf-8")
    except subprocess.CalledProcessError as error:
        print("Exception Occured: " + str(error))


if __name__ == "__main__":

    COMMAND_CHANGED_DOCKERFILES = "git diff-tree --no-commit-id --name-only -r f553255007e46af1d7a4ba1833b2dbc30e2c7563"
    DOCKERHUB_USERNAME = "fatihbaltaci"

    process_git = run_command(COMMAND_CHANGED_DOCKERFILES)
    output = process_git.splitlines()

    for file_path in output:
        if not "Dockerfile" in file_path:
            continue
        print("Changed Dockerfile: " + file_path)

        file_path = "python_3.6/Dockerfile"

        dockerfile_dir, image_tag = prepare_docker_build(file_path=file_path, hub_username=DOCKERHUB_USERNAME)

        COMMAND_BUILD_DOCKER_FILE = "cd " + dockerfile_dir + " && docker build . --tag " + \
            image_tag
        print(COMMAND_BUILD_DOCKER_FILE)
        output = run_command(COMMAND_BUILD_DOCKER_FILE)
        print(output)
