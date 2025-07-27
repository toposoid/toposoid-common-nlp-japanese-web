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

from chikkarpy import Chikkar
from chikkarpy.dictionarylib import Dictionary

#This module provides utilities for the Japanese version of Synonym
class ChikkarUtils():
    chikkar = Chikkar()
    system_dic = Dictionary()
    chikkar.add_dictionary(system_dic)
    #chikkar.enable_verb()

    #Extract synonyms of parameter words using Sudachi
    def getSynonyms(self, normalizedWord):
        return set(self.chikkar.find(normalizedWord))
