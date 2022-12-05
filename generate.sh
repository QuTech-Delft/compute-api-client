#!/bin/bash

openapi-generator-cli generate \
    --input-spec http://localhost:8000/openapi.json \
    --generator-name python-legacy \
    --config config.json \
    --library asyncio \
    --type-mappings enum=Enum

mv compute_api_client_README.md README.md

rm -rf ../../../docs/design/code/components/compute_api_client
mkdir ../../../docs/design/code/components/compute_api_client
cp README.md ../../../docs/design/code/components/compute_api_client/index.md
cp compute_api_client/docs/* ../../../docs/design/code/components/compute_api_client/

sed -i '' -e 's|compute_api_client/docs/||g' ../../../docs/design/code/components/compute_api_client/index.md
find ../../../docs/design/code/components/compute_api_client -name "*.md" -exec sed -i '' -e 's|../README|index|g' {} \;
