#!/bin/bash

openapi-generator-cli generate \
    --input-spec http://localhost:8000/openapi.json \
    --generator-name python-legacy \
    --config config.json \
    --library asyncio

