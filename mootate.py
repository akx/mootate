import argparse
import random
import string
import time

dict_words = [w.strip() for w in open("/usr/share/dict/words")]


def mootate(phrase):
    words = []
    for word in phrase.split(None):
        if random.random() < 0.01:
            word = "".join(
                (
                    random.choice(
                        string.ascii_lowercase
                        if c.islower()
                        else string.ascii_uppercase
                    )
                    if random.random() < 0.07
                    else c
                )
                for c in word
            )
        if random.random() < 0.002:
            if random.random() < 0.3:
                cand_words = [
                    w
                    for w in dict_words
                    if (w.startswith(word[0]) or w.endswith(word[-1]))
                    and abs(len(w) - len(word)) <= 1
                ]
            else:
                word_let = set(word)
                cand_words = [
                    w
                    for w in dict_words
                    if abs(len(w) - len(word)) <= 1 and len(set(w) ^ word_let) < 2
                ]
            if cand_words:
                word = random.choice(cand_words)
        words.append(word)
    return " ".join(words)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("phrase")
    args = ap.parse_args()
    phrase = args.phrase
    last_phrase = None
    while True:
        phrase = mootate(phrase)
        if phrase != last_phrase:
            print(phrase)
            last_phrase = phrase
        time.sleep(0.05)


if __name__ == "__main__":
    main()
