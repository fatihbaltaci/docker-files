#!/bin/bash

#changed_docker_files=( $(git diff-tree --no-commit-id --name-only -r $GITHUB_SHA | grep Dockerfile) )
changed_docker_files=( $(git diff-tree --no-commit-id --name-only -r 5d06329a59f8dce74732b73271b0db7dbde102ba) )

echo $changed_docker_files