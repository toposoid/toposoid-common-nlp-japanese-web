ARG BASE_IMAGE_LABEL
FROM toposoid/python-nlp-japanese:${BASE_IMAGE_LABEL}

ARG TARGET_BRANCH
ARG SENTENCE_TRANSFORMER_MODEL
ARG VECTOR_MODEL

WORKDIR /app
ENV DEPLOYMENT=local

#SHELL ["/bin/bash", "-c"]

RUN apt-get update \
&& apt-get -y install git unzip \
#&& curl -LsSf https://astral.sh/uv/install.sh | sh \
#&& source ${HOME}/.local/bin/env \
&& git clone https://github.com/toposoid/toposoid-common-nlp-japanese-web.git \
&& cd toposoid-common-nlp-japanese-web \
&& git fetch origin ${TARGET_BRANCH} \
&& git checkout ${TARGET_BRANCH} \
&& mv -f /tmp/entity_vector.model.bin ./ \
&& mv -f /tmp/wnjpn.db ./ \
&& mv -f /tmp/chive-1.2-mc${VECTOR_MODEL}.kv ./ \
&& mv -f /tmp/chive-1.2-mc${VECTOR_MODEL}.kv.vectors.npy ./ \
&& mkdir -p models \
&& mkdir -p models/sentence-transformers_${SENTENCE_TRANSFORMER_MODEL} \
&& mv -f /tmp/${SENTENCE_TRANSFORMER_MODEL}/* ./models/sentence-transformers_${SENTENCE_TRANSFORMER_MODEL}/ \
&& rm -Rf /tmp/* \
&& sed -i s/__##GIT_BRANCH##__/${TARGET_BRANCH}/g requirements.txt 
&& pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

COPY ./docker-entrypoint.sh /app/
ENTRYPOINT ["/app/docker-entrypoint.sh"]

#uvを使用するとchikkarpyがインストールできない。　　