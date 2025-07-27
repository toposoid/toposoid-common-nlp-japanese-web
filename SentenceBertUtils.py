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

import os 
import numpy as np
from sentence_transformers import SentenceTransformer

class SentenceBertUtils():
    model = None
    def __init__(self) :        
        self.model = SentenceTransformer(os.environ["TOPOSOID_SENTENCEBERT_MODEL_JP"])        

    def getFeatureVector(self, sentence):
        return self.model.encode(sentence)


