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
