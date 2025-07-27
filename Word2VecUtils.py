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

from gensim.models import KeyedVectors
import os


#This module provides utilities for the Japanese version of Word2Vec

class Word2VecUtils():
    model = None
    chiveModel = None
    def __init__(self) :
        modelDir = './entity_vector.model.bin'
        self.model = KeyedVectors.load_word2vec_format(modelDir, binary=True)    
        self.chiveModel = KeyedVectors.load("./" + os.environ["TOPOSOID_CHIVE_MODEL_VERSION"])
    
    #This function calculates the similarity between two words given by a parameter in Word2Vec
    def calcSimilarityByWord2Vec(self, word, synonym):
        if word in self.model.key_to_index and synonym in self.model.key_to_index:
            return self.model.similarity(word, synonym)
        elif word in self.chiveModel.key_to_index and synonym in self.chiveModel.key_to_index:
            return self.chiveModel.similarity(word, synonym)
        else:
            return 0.0
    #This function gets synonyms with high similarity from Word2Vec.
    def getSimilarWords(self, word):
        thresholdW2V = float(os.environ["TOPOSOID_WORD2VEC_SIMILARITY_THRESHHOLD_JP"])
        similarWords = set()
        if word in self.model.index_to_key:
            for row in self.model.most_similar(positive=[word]):
                if row[1] > thresholdW2V and not row[0] == word:
                    similarWords.add(row[0])
        
        if len(similarWords) == 0 and word in self.chiveModel.index_to_key:
            for row in self.chiveModel.most_similar(positive=[word]):
                if row[1] > thresholdW2V and not row[0] == word:
                    similarWords.add(row[0])
        return list(similarWords)

