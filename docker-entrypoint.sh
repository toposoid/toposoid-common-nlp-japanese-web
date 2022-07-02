#!/bin/bash

cd /app/toposoid-common-nlp-japanese-web
uvicorn api:app --reload --host 0.0.0.0 --port 9006
