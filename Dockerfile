FROM toposoid/python-nlp-japanese:0.5-SNAPSHOT

WORKDIR /app
ARG TARGET_BRANCH
ENV DEPLOYMENT=local

RUN apt-get update \
&& apt-get -y install git \
&& git clone https://github.com/toposoid/toposoid-common-nlp-japanese-web.git \
&& cd toposoid-common-nlp-japanese-web \
&& git fetch origin ${TARGET_BRANCH} \
&& git checkout ${TARGET_BRANCH} \
&& pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt \
&& mv -f /tmp/entity_vector.model.bin ./ \
&& mv -f /tmp/wnjpn.db ./ \
&& mv -f /tmp/chive-1.2-mc15.kv ./ \
&& mv -f /tmp/chive-1.2-mc15.kv.vectors.npy ./ \
&& mkdir -p models \
&& mkdir -p models/sentence-transformers_paraphrase-multilingual-mpnet-base-v2 \
&& mv -f /tmp/paraphrase-multilingual-mpnet-base-v2/* ./models/paraphrase-multilingual-mpnet-base-v2/

COPY ./docker-entrypoint.sh /app/
ENTRYPOINT ["/app/docker-entrypoint.sh"]
