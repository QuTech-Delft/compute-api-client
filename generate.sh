#!/bin/bash

# Script for generating the API client library and accompanying docs for the Compute Job Manager API.
#
# Usage:
# Requires the openapi-generator-cli, which will be installed in the dev-container by dev-install.
# Make sure the Compute Job Manager is running (OpenAPI specs should be available on port 8000) and run the script.
# The script will prompt you to choose a new version number for the library.
#
# Examples
# Generate client and docs:
# $ ./generate.sh
# Check for changes in client and docs:
# $ ./generate.sh check


set -e

check=$1

export OPENAPI_GENERATOR_VERSION=7.14.0

openapi-generator-cli generate \
    --input-spec http://localhost:8000/openapi.json \
    --generator-name python \
    --config config.json \
    --library asyncio

    mv compute_api_client_README.md README.md

if [ "$check" = "check" ]; then
    # Allows CI to verify the client is up to date
    git diff HEAD
else
    # Update documentation
    curl -o ../../../../docs/design/code/apps/compute_job_manager_openapi.json http://localhost:8000/openapi.json

    rm -rf ../../../../docs/design/code/libs/compute_api_client
    mkdir ../../../../docs/design/code/libs/compute_api_client
    cp README.md ../../../../docs/design/code/libs/compute_api_client/index.md
    cp compute_api_client/docs/* ../../../../docs/design/code/libs/compute_api_client/

    sed -i -e 's|compute_api_client/docs/||g' ../../../../docs/design/code/libs/compute_api_client/index.md
    find ../../../../docs/design/code/libs/compute_api_client -name "*.md" -exec sed -i -e 's|../README|index|g' {} \;

    # Update the version of the uv project
    git_tag=$(git describe --tags --abbrev=0)
    uv_tag=$(cat pyproject.toml | grep "^version =" | cut -d'"' -f2)

    echo "Last Git tag:           ${git_tag}"
    echo "Current uv version:     ${uv_tag}"

    echo "Please input the new version for this repo"
    read version

    sed -i -e "s/^version =.*/version = \"${version}\"/" pyproject.toml

    echo "Updating dispatcher dependencies"
    cd ../../dispatcher/
    uv lock

    echo "Updating integration test dependencies"
    cd ../../../tests/integration/
    uv lock

    echo "Updating e2e test dependencies"
    cd ../e2e/
    uv lock

    echo "Success!"
fi
