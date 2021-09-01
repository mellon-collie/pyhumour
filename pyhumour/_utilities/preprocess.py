import re
import json
from nltk import (
    tokenize,
    pos_tag
)
import os
import sys
from concurrent import futures
import itertools


def preprocess_text(text, contraction_map):
    if not isinstance(text, str):
        return text

    text = text.lower()
    change_characters = {'‚': ',', '\ufeff': ' ', '„': '"', "—": '-', '™': ' ', '″': '"', 'ƒ': 'f', '�': ' ',
                         '′': "'", '‘': "'",
                         '…': '...', '’': "'", '‑': '-', '\u2028': ' ', 'π': 'π', 'Ł': ' ', '⚪': ' ', '–': '-',
                         '\u200b': ' ', '”': '"',
                         'Н': 'H', '€': '€'}
    is_change_characters = set(text).intersection(change_characters.keys())
    if is_change_characters:
        for i in is_change_characters:
            text = re.sub(i, change_characters[i], text)
    # contraction_map removal
    words = set(text.split())  # taking all the unique words in a sentence
    is_change_words = words.intersection(contraction_map.keys())
    if is_change_words:
        for i in is_change_words:
            text = re.sub(i, contraction_map[i], text)
    if '<' in set(text):
        text = re.sub("<.*>", "", text)
    text = " ".join(text.split())
    text = " ".join(tokenize.sent_tokenize(text))
    text = " ".join(tokenize.word_tokenize(text))

    return text


def preprocess_texts_in_chunks(text_list: list, contraction_map) -> list:

    number_worker_processes = len(text_list) // 50000 + 1
    number_worker_processes = number_worker_processes if number_worker_processes < 4 else 4
    if number_worker_processes > 1:
        futures_list = []
        text_chunks = [text_list[x: x + 50000] for x in range(0, len(text_list), 50000)]
        with futures.ProcessPoolExecutor(max_workers=number_worker_processes) as executor:
            for chunk in text_chunks:
                futures_list.append(executor.submit(preprocess_text, chunk, contraction_map))

        chunks_result = [future.result() for future in futures_list]
        preprocess_texts_list = list(itertools.chain(*chunks_result))
        return preprocess_texts_list

    else:
        return preprocess_texts(text_list, contraction_map)


def preprocess_texts(text_list: list, contraction_map) -> list:
    preprocess_texts_list = []

    for text in text_list:
        preprocess_texts_list.append(preprocess_text(text, contraction_map))

    return preprocess_texts_list


def pos_tag_texts(text_list: list) -> list:
    pos_tag_text_list = []
    for text in text_list:
        pos_tag_text_list.append(pos_tag(tokenize.word_tokenize(text)))

    return pos_tag_text_list
