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
    print(command)
    process = subprocess.run(
            command, shell=True, capture_output=True, check=True, universal_newlines=True)
    return process.stdout

def docker_run_command(command):
    print(command)
    return_code = os.system(command)
    if return_code != 0:
        raise Exception("There is a problem !!!")

if __name__ == "__main__":
    DOCKERHUB_USERNAME = "fatihbaltaci"

    COMMAND_LAST_COMMIT_ID = "git rev-parse HEAD"
    LAST_COMMIT_ID = run_command(COMMAND_LAST_COMMIT_ID)
    COMMAND_CHANGED_FILES = f"git diff-tree --no-commit-id --name-only -r {LAST_COMMIT_ID}"
    CHANGED_FILES = run_command(COMMAND_CHANGED_FILES).splitlines()

    for file_path in CHANGED_FILES:
        if not "Dockerfile" in file_path:
            continue
        print("Changed Dockerfile: " + file_path)

        dockerfile_dir, image_tag = prepare_docker_build(file_path=file_path, hub_username=DOCKERHUB_USERNAME)

        docker_file_path = Path(dockerfile_dir) / "Dockerfile"

        COMMAND_BUILD_DOCKER_FILE = f"cd {dockerfile_dir} && docker build --tag {image_tag} ."
        docker_run_command(COMMAND_BUILD_DOCKER_FILE)
        COMMAND_PUSH_DOCKER = f"docker push {image_tag}"
        docker_run_command(COMMAND_PUSH_DOCKER)
