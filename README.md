# toposoid-common-nlp-japanese-web
This is a WEB API that works as a microservice within the Toposoid project.
Toposoid is a knowledge base construction platform.(see [Toposoid Root Project](https://github.com/toposoid/toposoid.git))
This Microservice provides an NLP function that handles Japanese and outputs the result in JSON.

[![Test And Build](https://github.com/toposoid/toposoid-common-nlp-japanese-web/actions/workflows/action.yml/badge.svg)](https://github.com/toposoid/toposoid-common-nlp-japanese-web/actions/workflows/action.yml)

<img width="1164"  src="https://github.com/toposoid/toposoid-common-nlp-japanese-web/assets/82787843/0c50650d-cc0d-40ac-a347-92ed337d2d4c">
<img width="1071"  src="https://github.com/toposoid/toposoid-common-nlp-japanese-web/assets/82787843/549462aa-1fad-42de-af03-ae5a3afd1c2f">

## Requirements
* Docker version 20.10.x, or later
* docker-compose version 1.22.x

### Recommended Environment For Standalone
* Required: at least 4GB of RAM
* Required: at least 12.2GB of HDD(Docker Image Size)

## Setup For Standalone
```bssh
docker-compose up -d
```
The first startup takes a long time until docker pull finishes.

## Usage
```bash
#getSynonyms
curl -X POST -H "Content-Type: application/json" -d '{
    "word": "SEO"
}' http://localhost:9006/getSynonyms
#getFeatureVector
curl -X POST -H "Content-Type: application/json" -d '{
    "sentence": "これはテストです。"
}' http://localhost:9006/getFeatureVector
```
* ref. http://localhost:9006/docs

# Note
* This microservice uses 9006 as the default port.
* The Bert models used in this repository is below.　
https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
https://huggingface.co/sentence-transformers/paraphrase-multilingual-mpnet-base-v2
* You can change the SentenceBERT model by changing the environment variable TOPOSOID_SENTENCEBERT_MODEL_JP.

## License
toposoid/scala-common-nlp-japanese-web is Open Source software released under the [Apache 2.0 license](https://www.apache.org/licenses/LICENSE-2.0.html).

## Author
* Makoto Kubodera([Linked Ideal LLC.](https://linked-ideal.com/))

Thank you!
