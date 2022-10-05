'''
  Copyright 2021 Linked Ideal LLC.[https://linked-ideal.com/]
 
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at
 
      http://www.apache.org/licenses/LICENSE-2.0
 
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
 '''
from fastapi.testclient import TestClient
from api import app
from model import NormalizedWord, SynonymList
import pytest

#This is a unit test module
client = TestClient(app)
def test_EmptyWord():    
    response = client.post("/getSynonyms",
                        headers={"Content-Type": "application/json"},
                        json={"word": ""})    
    assert response.status_code == 200
    synonymList = SynonymList.parse_obj(response.json())
    assert synonymList.synonyms == []

def test_SimpleVerb():    
    response = client.post("/getSynonyms",
                        headers={"Content-Type": "application/json"},
                        json={"word": "論ずる"})    
    assert response.status_code == 200
    synonymList = SynonymList.parse_obj(response.json())
    print(synonymList.synonyms.sort())
    assert synonymList.synonyms.sort() == ['論じる', '論述', '話し合う'].sort()

def test_SimpleNoun():    
    response = client.post("/getSynonyms",
                        headers={"Content-Type": "application/json"},
                        json={"word": "映画"})    
    assert response.status_code == 200
    synonymList = SynonymList.parse_obj(response.json())
    assert synonymList.synonyms.sort() == ['フィルム'].sort()

def test_VocabularyNotFoundInWordNet():    
    response = client.post("/getSynonyms",
                        headers={"Content-Type": "application/json"},
                        json={"word": "確約"})    
    assert response.status_code == 200
    synonymList = SynonymList.parse_obj(response.json())
    assert synonymList.synonyms.sort() == ['了承', '承諾', '約束'].sort()

def test_VocabularyNotFoundInWord2Vec():    
    response = client.post("/getSynonyms",
                        headers={"Content-Type": "application/json"},
                        json={"word": "秀逸だ"})    
    assert response.status_code == 200
    synonymList = SynonymList.parse_obj(response.json())
    assert synonymList.synonyms == []

def test_ChiveModel():    
    response = client.post("/getSynonyms",
                        headers={"Content-Type": "application/json"},
                        json={"word": "SEO"})    
    assert response.status_code == 200
    synonymList = SynonymList.parse_obj(response.json())
    assert synonymList.synonyms.sort() == ['セスアップ', 'リスティング', '検索エンジン'].sort()


def test_ChikkarSynonym():
    response = client.post("/getSynonyms",
                        headers={"Content-Type": "application/json"},
                        json={"word": "ケータイ"})    
    assert response.status_code == 200
    synonymList = SynonymList.parse_obj(response.json())    
    assert synonymList.synonyms.sort() == ['mobile', '携帯', '携帯電話', 'モバイル'].sort()
    
