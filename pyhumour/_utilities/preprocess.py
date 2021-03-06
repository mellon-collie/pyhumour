import re
from nltk import (
    tokenize,
    pos_tag
)
from concurrent import futures
import itertools
import asyncio


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


async def preprocess_texts_in_chunks(loop, executor, text_list: list, contraction_map) -> tuple:
    number_worker_processes = len(text_list) // 50000 + 1
    preprocess_texts_list = []
    if number_worker_processes > 1:
        futures_list = []
        text_chunks = [text_list[x: x + 50000] for x in range(0, len(text_list), 50000)]
        for chunk in text_chunks:
            futures_list.append(loop.run_in_executor(executor, preprocess_texts, chunk, contraction_map))
        chunks_result = await asyncio.gather(*futures_list)
        preprocess_texts_list = list(itertools.chain(*chunks_result))
    else:
        preprocess_texts_list = preprocess_texts(text_list, contraction_map)

    pure_preprocessed_texts = []
    pos_tagged_texts = []

    for index, item in enumerate(preprocess_texts_list):
        pure_preprocessed_texts.append(item[0])
        pos_tagged_texts.append(item[1])

    return pure_preprocessed_texts, pos_tagged_texts


def preprocess_texts(text_list: list, contraction_map) -> list:
    preprocess_texts_list = []
    for text in text_list:
        preprocessed_text = ""
        pos_tagged_text = []
        try:
            preprocessed_text = preprocess_text(text, contraction_map)
        except Exception as e:
            preprocessed_text = text
        try:
            pos_tagged_text = pos_tag(tokenize.word_tokenize(preprocessed_text))
        except Exception as e:
            pos_tagged_text = []
        preprocess_texts_list.append((preprocessed_text, pos_tagged_text))
    return preprocess_texts_list


def pos_tag_texts(text_list: list) -> list:
    pos_tag_text_list = []
    for text in text_list:
        pos_tag_text_list.append(pos_tag(tokenize.word_tokenize(text)))
    return pos_tag_text_list
