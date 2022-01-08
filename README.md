# toposoid-common-nlp-japanese-web
This is a WEB API that works as a microservice within the Toposoid project.
Toposoid is a knowledge base construction platform.(see [Toposoid Root Project](https://github.com/toposoid/toposoid.git))
This Microservice provides an NLP function that handles Japanese and outputs the result in JSON.

[![Test And Build](https://github.com/toposoid/scala-common-nlp-english-web/actions/workflows/action.yml/badge.svg)](https://github.com/toposoid/scala-common-nlp-english-web/actions/workflows/action.yml)

<img width="1105" src="https://user-images.githubusercontent.com/82787843/146533705-b1a09ad0-5faa-42db-8e02-fd3babf1c9e6.png">

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
curl -X POST -H "Content-Type: application/json" -d '{
    "word": "execute"
}
' http://localhost:9008/getSynonyms
```

# Note
* This microservice uses 9008 as the default port.
* Currently, only the function to get synonyms is open to the public in this API.

## License
toposoid/scala-common-nlp-english-web is Open Source software released under the [Apache 2.0 license](https://www.apache.org/licenses/LICENSE-2.0.html).

## Author
* Makoto Kubodera([Linked Ideal LLC.](https://linked-ideal.com/))

Thank you!
