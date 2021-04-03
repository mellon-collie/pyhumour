"""Implementation of the Noun Absurdity property."""

import numpy as np
import re
from scipy.spatial import distance


class NounAbsurdity:
    """Calculates the 'Noun Absurdity' value of a given text."""

    def __init__(self, humorous_adj_noun_mapping, humorous_adj_noun_dict):
        self.humorous_adj_noun_mapping = humorous_adj_noun_mapping
        self.humorous_adj_noun_dict = humorous_adj_noun_dict

    def calculate(self, pos_tags: list) -> float:
        """Return the 'Humourous Noun Absurdity' value of a given text.

        :param list pos_tags: List of pos_tags for the given text.
        """
        embeddings_index = {}
        f = open('numberbatch-en.txt', encoding='utf-8')
        for line in f:
            values = line.split()
            word = values[0]
            coefs = np.asarray(values[1:], dtype='float32')
            embeddings_index[word] = coefs
        f.close()
        acceptable_types = ('JJ', 'JJR', 'JJS')
        second_type = ('NN', 'NNS', 'NNP', 'NNPS')
        noun_absurdity_positive = 0
        noun_absurdity_count = 0
        try:
            for j in range(len(pos_tags)-1):
                if pos_tags[j][1] in acceptable_types and pos_tags[j+1][1] in second_type:
                    adj = re.sub('[^A-Za-z]*', '', pos_tags[j][0])
                    adj = adj.lower()
                    noun = re.sub('[^A-Za-z]*', '', pos_tags[j+1][0])
                    noun = noun.lower()
                    for k in self.humorous_adj_noun_mapping[adj]:
                        tup = (adj, k)
                        try:
                            noun_absurdity_positive += self.humorous_adj_noun_dict[tup]*distance.cosine(
                                embeddings_index[noun], embeddings_index[k])
                            noun_absurdity_count += self.humorous_adj_noun_dict[tup]
                        except Exception:
                            noun_absurdity_positive += 0
                            noun_absurdity_count += 0

            noun_absurdity_average = noun_absurdity_positive / noun_absurdity_count
        except Exception:
            noun_absurdity_average = 0
        noun_absurdity_humorous_average = noun_absurdity_average
        return noun_absurdity_humorous_average
