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

