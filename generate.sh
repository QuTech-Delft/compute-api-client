#!/bin/bash

set -e

check=$1

export OPENAPI_GENERATOR_VERSION=6.4.0

openapi-generator-cli generate \
    --input-spec http://localhost:8000/openapi.json \
    --generator-name python-legacy \
    --config config.json \
    --library asyncio \
    --type-mappings enum=Enum

    mv compute_api_client_README.md README.md

if [ "$check" = "check" ]; then
    git diff --quiet HEAD
else
    curl -o ../../../docs/design/code/apps/compute_job_manager_openapi.json http://localhost:8000/openapi.json

    rm -rf ../../../docs/design/code/libs/compute_api_client
    mkdir ../../../docs/design/code/libs/compute_api_client
    cp README.md ../../../docs/design/code/libs/compute_api_client/index.md
    cp compute_api_client/docs/* ../../../docs/design/code/libs/compute_api_client/

    sed -i -e 's|compute_api_client/docs/||g' ../../../docs/design/code/libs/compute_api_client/index.md
    find ../../../docs/design/code/libs/compute_api_client -name "*.md" -exec sed -i -e 's|../README|index|g' {} \;

    # Update the version of the poetry project
    git_tag=$(git describe --tags --abbrev=0)
    poetry_tag=$(cat pyproject.toml | grep "^version =" | cut -d'"' -f2)

    echo "Last Git tag:           ${git_tag}"
    echo "Current Poetry version: ${poetry_tag}"

    echo "Please input the new version for this repo"
    read version

    sed -i -e "s/^version =.*/version = \"${version}\"/" pyproject.toml

    cd ../dispatcher/
    poetry lock --no-update

    echo "Success!"
fi
