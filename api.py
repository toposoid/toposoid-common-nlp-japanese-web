'''
  Copyright (C) 2025  Linked Ideal LLC.[https://linked-ideal.com/]
 
  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU Affero General Public License as
  published by the Free Software Foundation, version 3.
 
  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU Affero General Public License for more details.
 
  You should have received a copy of the GNU Affero General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from fastapi import FastAPI, Header
from model import NormalizedWord, SynonymList, SingleSentence, FeatureVector, TransversalState
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from WordNetUtils import WordNetUtils
from Word2VecUtils import Word2VecUtils
from ChikkarUtils import ChikkarUtils
from SentenceBertUtils import SentenceBertUtils
from typing import Optional
from ToposoidCommon.model import StatusInfo
#from utils import formatMessageForLogger
#import yaml

import os
#rom logging import config
#config.dictConfig(yaml.load(open("logging.yml", encoding="utf-8").read(), Loader=yaml.SafeLoader))
#import logging
#LOG = logging.getLogger(__name__)
import traceback
#from typing import List

import ToposoidCommon as tc
from typing import Optional
LOG = tc.LogUtils(__name__)

app = FastAPI(
    title="toopsoid-common-nlp-japanese-web",
    version="0.6-SNAPSHOT"
)

wordNetUtils = WordNetUtils()
word2VecUtils = Word2VecUtils()
chikkarUtils = ChikkarUtils()
sentenceBertUtils = SentenceBertUtils()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# This API is for getting synonyms
@app.post("/getSynonyms")
def getSynonyms(normalizedWord:NormalizedWord, X_TOPOSOID_TRANSVERSAL_STATE: Optional[str] = Header(None, convert_underscores=False)):
    transversalState = TransversalState.parse_raw(X_TOPOSOID_TRANSVERSAL_STATE.replace("'", "\""))
    try:
        synonyms = []
        thresholdNoun = float(os.environ["TOPOSOID_SYNONYM_NOUN_SIMILARITY_THRESHHOLD_JP"])
        thresholdVerb = float(os.environ["TOPOSOID_SYNONYM_VERB_SIMILARITY_THRESHHOLD_JP"])
        if not normalizedWord.word.strip() == "":
            nounSynonums, verbSynonyms = wordNetUtils.getSynonyms(normalizedWord.word)
            nounSynonums = nounSynonums | chikkarUtils.getSynonyms(normalizedWord.word) #Chikkar is nominal only            

            if len(nounSynonums) == 0 and len(verbSynonyms) == 0:
                synonyms = word2VecUtils.getSimilarWords(normalizedWord.word)
            else:
                for synonym in nounSynonums:
                    if word2VecUtils.calcSimilarityByWord2Vec(normalizedWord.word, synonym) > thresholdNoun:
                        synonyms.append(synonym) 
                for synonym in verbSynonyms:
                    if word2VecUtils.calcSimilarityByWord2Vec(normalizedWord.word, synonym) > thresholdVerb:
                        synonyms.append(synonym)    
        response = JSONResponse(content=jsonable_encoder(SynonymList(synonyms=synonyms)))
        LOG.info("Getting synonym completed.", transversalState)
        return response
    except Exception as e:
        LOG.error(traceback.format_exc(), transversalState)
        return JSONResponse({"status": "ERROR", "message": traceback.format_exc()})


@app.post("/getFeatureVector")
def getFeatureVector(input:SingleSentence, X_TOPOSOID_TRANSVERSAL_STATE: Optional[str] = Header(None, convert_underscores=False)):
    transversalState = TransversalState.parse_raw(X_TOPOSOID_TRANSVERSAL_STATE.replace("'", "\""))
    try:        
        vector = sentenceBertUtils.getFeatureVector(input.sentence)
        response = JSONResponse(content=jsonable_encoder(FeatureVector(vector=list(vector))))
        LOG.info("Getting feature vector completed.", transversalState)
        return response
    except Exception as e:
        LOG.error(traceback.format_exc(), transversalState)
        return JSONResponse({"status": "ERROR", "message": traceback.format_exc()})
