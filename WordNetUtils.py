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

import sqlite3
import threading



#This module provides utilities for the Jaoanese version of WordNet

class WordNetUtils(): 

    conn = None
    def __init__(self):        
        self.conn = sqlite3.connect("wnjpn.db", check_same_thread=False)
        
    #Extract synonyms of parameter words using WordNet
    def getSynonyms(self, normalizedWord):
        synonymsNoun = set()
        synonymsVerb = set()        
        cur = self.conn.execute("select * from word where lemma=?", (normalizedWord,))
        wordList = [row for row in cur]        
        for word in wordList:
            cur = self.conn.execute("select * from sense where wordid=?", (word[0],))
            synnetList = [row for row in cur]
            for synnet in synnetList:
                cur = self.conn.execute("select word.lemma, word.pos from sense, word where synset = ? and word.lang = 'jpn' and sense.wordid = word.wordid and word.pos in ('n', 'v');", (synnet[0],))
                for row in cur:
                    if row[0] == normalizedWord: 
                        continue
                    if row[1] == 'n':
                        synonymsNoun.add(row[0])
                    elif row[1] == 'v':
                        synonymsVerb.add(row[0])                                
        return (synonymsNoun, synonymsVerb)

