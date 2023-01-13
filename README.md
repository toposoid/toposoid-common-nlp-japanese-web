# toposoid-common-nlp-japanese-web
This is a WEB API that works as a microservice within the Toposoid project.
Toposoid is a knowledge base construction platform.(see [Toposoid Root Project](https://github.com/toposoid/toposoid.git))
This Microservice provides an NLP function that handles Japanese and outputs the result in JSON.

[![Test And Build](https://github.com/toposoid/toposoid-common-nlp-japanese-web/actions/workflows/action.yml/badge.svg)](https://github.com/toposoid/toposoid-common-nlp-japanese-web/actions/workflows/action.yml)

<img width="1202" src="https://user-images.githubusercontent.com/82787843/148643043-b06a0fa8-5d65-496f-9bee-a08efc8c3a57.png">

<img width="948" src="https://user-images.githubusercontent.com/82787843/212320227-766b6524-5043-4c99-ac0f-106acae34821.png">

## Requirements
* Docker version 20.10.x, or later
* docker-compose version 1.22.x

### Memory requirements
* Required: at least 6GB of RAM
* Required: 10G or higher of HDD

## Setup
```bssh
docker-compose up -d
```
It takes more than 20 minutes to pull the Docker image for the first time.

## Usage
```bash
#getSynonyms
curl -X POST -H "Content-Type: application/json" -d '{
    "word": "SEO"
}
' http://localhost:9006/getSynonyms
#getFeatureVector
curl -X POST -H "Content-Type: application/json" -d '{
    "sentence": "これはテストです。"
}
' http://localhost:9006/getFeatureVector
```

# Note
* This microservice uses 9006 as the default port.
* Currently, only the function to get synonyms is open to the public in this API.
* The vector dimension of getFeatureVector's response defaults to 768.

## License
toposoid/scala-common-nlp-japanese-web is Open Source software released under the [Apache 2.0 license](https://www.apache.org/licenses/LICENSE-2.0.html).

## Author
* Makoto Kubodera([Linked Ideal LLC.](https://linked-ideal.com/))

Thank you!
