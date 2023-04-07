#!/bin/bash

export OPENAPI_GENERATOR_VERSION=6.4.0

openapi-generator-cli generate \
    --input-spec http://localhost:8000/openapi.json \
    --generator-name python-legacy \
    --config config.json \
    --library asyncio \
    --type-mappings enum=Enum

mkdir -p ../../../docs/design/code/interfaces/compute_job_manager
curl -o ../../../docs/design/code/interfaces/compute_job_manager/openapi.json http://localhost:8000/openapi.json

mv compute_api_client_README.md README.md

rm -rf ../../../docs/design/code/components/compute_api_client
mkdir ../../../docs/design/code/components/compute_api_client
cp README.md ../../../docs/design/code/components/compute_api_client/index.md
cp compute_api_client/docs/* ../../../docs/design/code/components/compute_api_client/

sed -i -e 's|compute_api_client/docs/||g' ../../../docs/design/code/components/compute_api_client/index.md
find ../../../docs/design/code/components/compute_api_client -name "*.md" -exec sed -i -e 's|../README|index|g' {} \;

# Update the version of the poetry project
git_tag=$(git describe --tags --abbrev=0)
poetry_tag=$(cat pyproject.toml | grep "^version =" | cut -d'"' -f2)

echo "Last Git tag:           ${git_tag}"
echo "Current Poetry version: ${poetry_tag}"

echo "Please input the new version for this repo"
read version

sed -i -e "s/^version =.*/version = \"${version}\"/" pyproject.toml

echo "Success!"
