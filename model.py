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

from pydantic import BaseModel
from typing import Dict, List

class NormalizedWord(BaseModel):
    word:str

class SynonymList(BaseModel):
    synonyms:List[str]

class SingleSentence(BaseModel):
    sentence:str

class FeatureVector(BaseModel):
    vector:List[float]

class TransversalState(BaseModel):
    userId: str
    roleId: int
    username: str
    csrfToken: str
