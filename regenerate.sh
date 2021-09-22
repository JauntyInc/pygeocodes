#!/bin/bash

openapi-generator-cli generate -i https://api.geo.codes/swagger/doc.json -g python -o . -c config.yaml
mv geocodes_README.md README.md
