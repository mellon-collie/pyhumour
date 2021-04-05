"""Implementation of the Noun Absurdity property."""

import numpy as np
import re
from scipy.spatial import distance

from _utilities.pos_tag_bigram_frequency_matrix import POSTagBigramFrequencyMatrix


class NounAbsurdity:
    """Calculates the 'Noun Absurdity' value of a given text."""

    def __init__(self, frequency_matrix):
        """
        :param POSTagBigramFrequencyMatrix frequency_matrix: The adjective-noun frequency matrix
        """
        if not isinstance(frequency_matrix, POSTagBigramFrequencyMatrix):
            raise TypeError('The given matrix is not an instance of POSTagBigramFrequencyMatrix')
        self.adj_noun_dict = frequency_matrix
        self.adj_noun_mapping = frequency_matrix.get_all_row_keys()

    def calculate(self, pos_tags: list) -> float:
        """Return the 'Humourous Noun Absurdity' value of a given text.

        :param list pos_tags: List of pos_tags for the given text.
        """
        embeddings_index = {}
        target_path = 'pyhumour/resources/numberbatch-en.txt'
        try:
            f = open(target_path, encoding='utf-8')
        except FileNotFoundError:
            import requests
            url = 'https://conceptnet.s3.amazonaws.com/downloads/2019/numberbatch/numberbatch-en-19.08.txt.gz'
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(target_path, 'wb') as f:
                    f.write(response.raw.read())
            f = open(target_path, encoding='utf-8')
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
                    for k in self.adj_noun_mapping[adj]:
                        tup = (adj, k)
                        try:
                            noun_absurdity_positive += self.adj_noun_dict[tup]*distance.cosine(
                                embeddings_index[noun], embeddings_index[k])
                            noun_absurdity_count += self.adj_noun_dict[tup]
                        except Exception:
                            noun_absurdity_positive += 0
                            noun_absurdity_count += 0
            noun_absurdity_average = noun_absurdity_positive / noun_absurdity_count
        except Exception:
            noun_absurdity_average = 0

        return noun_absurdity_average
