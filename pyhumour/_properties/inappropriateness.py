"""Implementation of the Inappropriateness property."""

from nltk.tokenize import word_tokenize
import pandas as pd
from wordfreq import word_frequency


class Inappropriateness:
    """Calculates the 'Inappropriateness' value of a given text."""

    @staticmethod
    def calculate(text: str) -> float:
        """
        Return the 'Inappropriateness' value of a given text.

        :param str text: Text for which Inappropriateness is calculated
        """
        df_erotica = pd.read_table('pyhumour/resources/ero-1gram-nostop-regexed.txt',
                                   delim_whitespace=True,
                                   names=('word', 'count'))
        total_count_erotica = df_erotica['count'].sum()
        tokens = word_tokenize(text)
        inappropriate_positive = 0.0
        for j in tokens:
            try:
                inappropriate_positive += (
                    (int(df_erotica.loc[df_erotica['word'] == j]['count']) /
                     total_count_erotica) /
                    word_frequency(j, 'en', wordlist='large'))
            except Exception:
                pass
        inappropriate_average = inappropriate_positive / len(tokens)

        return inappropriate_average
