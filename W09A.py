import random
from typing import TextIO
from random import choice
from playsound import playsound
import time
import string

T = [0.0]
M = [0.0]
Me = [0.0]


def make_nthgram_dictionary(filename: str, nth: int) -> dict[str, list[str]]:
    t1 = time.time()
    no = ["/", "", "--", "|", "]", "[", "(", ")", "{", "}", ":", ";", "=", "_",
          "`", "\\", '#', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'â',
          "€", "©", "‰", ",", "'", '"', "*"]

    word_d = {}
    with open(filename) as f:
        words = f.read().strip().split()
    key = []
    key.append("")
    j = 0
    for i in range(0, len(words) - nth):
        while nth != len(key):
            word = words[i + j]
            for char in no:
                if char in word:
                    word = word.replace(char, "")
            if not word.istitle():
                word = word.lower()
            key.append(word)
            j += 1
        value = words[i + j]
        word_d.setdefault(tuple(key), []).append(value)
        key = key[1:]
        key.append(value)

    t2 = time.time()
    T[0] = (T[0] + t2 - t1)
    M[0] = (M[0] + t2 - t1)
    print("\t Time of Dic " + filename + ": " + str(t2 - t1))
    return word_d


def mimic_text_nthgram(word_dict: dict[tuple[str], list[str]], nth: int,
                       num_words: int, debugg=False) -> str:
    """
    Based on the word patterns in <word_dict>, return a string with
    <num_words> words that mimics the text.
    """
    t1 = time.time()
    # TODO
    marks = []
    Atricle = []
    Verb = []
    Prepostion = []
    Pronouns = []
    Conjection = []
    grammar(marks, Atricle, Verb, Prepostion, Pronouns, Conjection)
    # Article == 1
    # Noun == 2
    # Verb == 3
    # Preposition == 4
    # If Preposition, must loop, can't end on 4
    # Pronouns == 5

    acc = ""
    all_keys = list(word_dict.keys())
    if len(choice(all_keys)) < nth:
        return "Invalid nth entry"

    all_value = list(word_dict.values())
    counter = 0

    key = choice(all_keys)
    value = list(key)
    while not (key[0].isupper()):
        key = choice(all_keys)
        value = list(key)

    prev_word = ""
    i = 0
    p = True
    print(acc)
    while i < num_words:

        q = False

        while not q:
            q = True
            for ind in range(len(value)):
                if list(key)[ind] != value[ind]:
                    q = False
            if not q:
                key = choice(all_keys)

        # p = p and (counter != 0 or value[0].istitle())

        # if a < ((nth // 2) - 1) and i > 3:
        # print("acc:" + str(acc))
        # print("a:" + str(a))
        # print("Value:" + str(value))
        # print("Key:" + str(key))

        # i = 0
        # acc = ""
        # key = choice(all_keys)
        # value = list(key)

        a = nth
        # p = p and (
        #     sentence_structure(value[0], acc, num_words, counter, all_value,
        #                        Verb, i, Prepostion, Atricle, prev_word,
        #                        Pronouns, Conjection))

        if p:
            if debugg:
                print(value)
                print(key)

            # counter = check_part_of_spech(value, Verb, Prepostion,
            #                             Atricle, Pronouns, Conjection)

            prev_word = value[0]
            acc += " " + value[0]
            if not (i == num_words - 1) or acc[-1] in marks:
                i += 1

            if debugg:
                print("One word")
                print(acc)
                print(i)
                print("\n")

            if acc[-1] in marks:
                counter = 0
            else:
                counter = 1
            value = list(key[1:])
            key = choice(all_keys)

        elif len(acc) < 1:
            key = choice(all_keys)
            value = list(key)

    t2 = time.time()
    T[0] = (T[0] + t2 - t1)
    print("\t Time of Mimic: " + str(t2 - t1))
    print("\t Total Dic Time: " + str(M))
    print("\t Total Merge Time: " + str(Me))
    print("\t Total Time: " + str(T))
    T[0] = (T[0] - T[0])
    Me[0] = (Me[0] - Me[0])
    M[0] = (M[0] - M[0])

    return acc[1:]


def mimic_text_from_word(word_dict: dict[str, list[str]], nth: int,
                         num_words: int,
                         intitial_word: str, debugg=False) -> str:
    """
       Based on the word patterns in <word_dict>, return a string with
       <num_words> words that mimics the text.
       """
    """
    Based on the word patterns in <word_dict>, return a string with
    <num_words> words that mimics the text.
    """
    t1 = time.time()
    # TODO
    marks = []
    Atricle = []
    Verb = []
    Prepostion = []
    Pronouns = []
    Conjection = []
    grammar(marks, Atricle, Verb, Prepostion, Pronouns, Conjection)

    # Article == 1
    # Noun == 2
    # Verb == 3
    # Preposition == 4
    # If Preposition, must loop, can't end on 4
    # Pronouns == 5

    acc = ""

    intitial_word = str(intitial_word)

    all_keys = list(word_dict.keys())

    if len(all_keys[0]) < nth:
        return "Invalid nth entry"

    all_value = list(word_dict.values())
    in_Val = True

    for i in all_value:
        if intitial_word == i[0]:
            in_Val = False

    in_vale = True

    if in_Val:
        for i in all_value:
            if intitial_word.lower() == i[0]:
                in_vale = False

    if in_Val and in_vale:
        return 'invalid word'
    elif in_Val and not in_vale:
        intitial_word = intitial_word.lower()

    if debugg:
        print(intitial_word)

    counter = 0
    key = choice(all_keys)

    while str(key[0]) != str(intitial_word):
        key = choice(all_keys)
        if debugg:
            print(intitial_word)
            print(key[0])
            print("\n")

    value = list(key)
    prev_word = ""
    print("")
    i = 0
    p = True
    while i < num_words:
        q = False
        if debugg:
            trys = 0
        while not q:
            q = True
            for ind in range(len(value)):
                if list(key)[ind] != value[ind]:
                    q = False
                    if debugg:
                        print("Key: " + str(key))
                        print("Value: " + str(value))
                        print("\n")
            if not q:
                key = choice(all_keys)
                if debugg:
                    trys += 1
                    print(trys)

        # p = (counter != 0 or value[0].istitle()) or i == 0

        # p = p and (
        #     sentence_structure(value[0], acc, num_words, counter, all_value,
        #                        Verb, i, Prepostion, Atricle, prev_word,
        #                        Pronouns, Conjection))

        if p:

            if debugg:
                print("\n")
                print(value)
                print(key)

            counter = check_part_of_spech(value, Verb, Prepostion,
                                          Atricle, Pronouns, Conjection)

            acc += " " + value[0]
            if not (i == num_words - 1) or acc[-1] in marks:
                i += 1

            if debugg:
                print("\n")
                print("One word")
                print(acc)
                print(i)
                print("\n")
                print("\n")

            value = list(key[1:])
            prev_word = key[0]
            key = choice(all_keys)

    t2 = time.time()
    Mi = [t2 - t1]
    T[0] = (T[0] + t2 - t1)
    print("\t Time of Mimic: " + str(Mi))
    print("\t Total Dic Time: " + str(M))
    print("\t Total Merge Time: " + str(Me))
    print("\t Total Time: " + str(T))
    T[0] = (T[0] - T[0])
    Me[0] = (Me[0] - Me[0])
    M[0] = (M[0] - M[0])

    return acc[1:]


def mimic_text_from_phrase(word_dict: dict[str, list[str]], nth: int,
                           num_words: int,
                           intitial_word: str, debugg=False) -> str:
    """
       Based on the word patterns in <word_dict>, return a string with
       <num_words> words that mimics the text.
       """
    """
    Based on the word patterns in <word_dict>, return a string with
    <num_words> words that mimics the text.
    """
    t1 = time.time()
    # TODO
    marks = []
    Atricle = []
    Verb = []
    Prepostion = []
    Pronouns = []
    Conjection = []
    grammar(marks, Atricle, Verb, Prepostion, Pronouns, Conjection)

    # Article == 1
    # Noun == 2
    # Verb == 3
    # Preposition == 4
    # If Preposition, must loop, can't end on 4
    # Pronouns == 5

    acc = ""

    intitial_word = str(intitial_word)
    intitial_word = intitial_word.strip().split()

    all_keys = list(word_dict.keys())
    all_value = list(word_dict.values())

    if len(all_keys[0]) < nth:
        return "Invalid nth entry"

    if len(all_value[0]) < len(intitial_word):
        length = len(all_value[0])
    else:
        length = len(intitial_word)

    nums = 0
    in_Val = True

    if len(intitial_word) > len(all_keys[0]):
        for i in all_keys:
            if intitial_word[:len(i)] == list(i):
                in_Val = False
    elif len(intitial_word) < len(all_keys[0]):
        for i in all_keys:
            if intitial_word == list(i)[:len(intitial_word)]:
                in_Val = False
    else:
        for i in all_keys:
            m = list(i)
            if intitial_word == m:
                in_Val = False

    if in_Val:
        return 'invalid word'

    if debugg:
        print(intitial_word)

    counter = 0
    key = choice(all_keys)

    if len(key) < len(intitial_word):
        length = len(key)
    else:
        length = len(intitial_word)

    while list(key)[:len(intitial_word)] != intitial_word:
        key = choice(all_keys)
        if debugg:
            print(intitial_word)
            print(key[:len(intitial_word)])
            print("\n")

    value = list(key)
    prev_word = ""
    print("")
    i = 0
    p = True
    while i < num_words:
        q = False
        if debugg:
            trys = 0
        while not q:
            q = True
            for ind in range(len(value)):
                if list(key)[ind] != value[ind]:
                    q = False
                    if debugg:
                        print("Key: " + str(key))
                        print("Value: " + str(value))
                        print("\n")
            if not q:
                key = choice(all_keys)
                if debugg:
                    trys += 1
                    print(trys)

        # p = (counter != 0 or value[0].istitle()) or i == 0

        # p = p and (
        #     sentence_structure(value[0], acc, num_words, counter, all_value,
        #                        Verb, i, Prepostion, Atricle, prev_word,
        #                        Pronouns, Conjection))

        if p:

            if debugg:
                print("\n")
                print(value)
                print(key)

            counter = check_part_of_spech(value, Verb, Prepostion,
                                          Atricle, Pronouns, Conjection)

            acc += " " + value[0]
            if not (i == num_words - 1) or acc[-1] in marks:
                i += 1

            if debugg:
                print("\n")
                print("One word")
                print(acc)
                print(i)
                print("\n")
                print("\n")

            value = list(key[1:])
            prev_word = key[0]
            key = choice(all_keys)

    t2 = time.time()
    Mi = [t2 - t1]
    T[0] = (T[0] + t2 - t1)
    print("\t Time of Mimic: " + str(Mi))
    print("\t Total Dic Time: " + str(M))
    print("\t Total Merge Time: " + str(Me))
    print("\t Total Time: " + str(T))
    T[0] = (T[0] - T[0])
    Me[0] = (Me[0] - Me[0])
    M[0] = (M[0] - M[0])

    return acc[1:]


def make_dictionary(filename: str) -> dict[str, list[str]]:
    t1 = time.time()
    no = ["/", "", "--", "|", "]", "[", "(", ")", "{", "}", ":", ";", "=", "_",
          "`", "\\", '#', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'â',
          "€", "©", "‰", ",", "'", '"', " ", "*"]
    word_d = {}
    with open(filename) as f:
        words = f.read().split()
    prev_word = ''
    for word in words:
        p = True
        n = 0
        while n < len(no):
            if no[n] in word:
                word = word.replace(no[n], "")
            n += 1
        if not word.istitle():
            word = word.lower()

        word_d.setdefault(prev_word, []).append(word.lower())
        prev_word = word.lower()

    t2 = time.time()
    T[0] = (T[0] + t2 - t1)
    M[0] = (M[0] + t2 - t1)
    print("\t Time of Dic " + filename + ": " + str(t2 - t1))
    return word_d


def mimic_text(word_dict: dict[str, list[str]], num_words: int) -> str:
    """
    Based on the word patterns in <word_dict>, return a string with
    <num_words> words that mimics the text.
    """
    t1 = time.time()
    # TODO
    marks = ["!", "?", ".", '"']
    Atricle = ["the", "some", "a", "an", "one"]
    Verb = []
    with open("en-verbs.txt", "r+") as file:
        lines = file.readlines()
        for i in lines:
            word = i.strip()
            word = word.replace(",,,,,,,,,,,,", " ")
            word = word.replace(",,,,,", " ")
            word = word.replace(",,,", " ")
            word = word.replace(",,", " ")
            words = word.split()
            for j in words:
                if "," in j:
                    Verb.append(j[:j.find(",")].lower())
                elif len(j) > 0:
                    Verb.append(j.lower())

    Prepostion = []
    with open("prepositions.txt", "r") as file:
        p = file.readlines()
    for i in range(len(p)):
        Prepostion.append(p[i].strip().lower())
    print(str(Prepostion))

    Pronouns = []
    with open("pronouns.txt", "r+") as file:
        lines = file.readlines()
        for i in lines:
            word = i.strip()
            word = word.replace("'", "")
            word = word.replace(',', "")
            Pronouns.append(word.lower())
    Conjection = []
    with open("conjection.txt", "r+") as file:
        lines = file.readlines()
        for i in lines:
            word = i.strip().lower()
            Conjection.append(word)
    # Article == 1
    # Noun == 2
    # Verb == 3
    # Preposition == 4
    # If Preposition, must loop, can't end on 4
    # Pronouns == 5

    prev_word = ""
    i = 0
    at = 0
    acc = " "
    all_keys = list(word_dict.keys())
    all_value = list(word_dict.values())
    key = choice(all_keys)
    counter = 0
    value = choice(word_dict[key])
    q = 0
    while i < num_words:
        if key in all_keys and value != key:
            value = choice(word_dict[key])
            if len(acc) > 1 and not value.istitle():
                key = choice(all_keys)
            at += 1
            if (sentence_structure(value, acc, num_words, counter, all_value,
                                   Verb, i, Prepostion, Atricle, prev_word,
                                   Pronouns, Conjection)):
                key = value
                at = 0
                acc += " " + value
                prev_word = value
                if acc[-1] in marks:
                    counter = 0
                elif value.lower() in Verb:
                    counter = 3
                elif value.lower() in Prepostion:
                    counter = 4
                elif value.lower() in Atricle:
                    counter = 1
                elif value == "I" or value.lower() in Pronouns:
                    counter = 5
                elif value.lower() in Conjection:
                    counter = 6
                else:
                    counter = 2
                i += 1
            elif at >= len(word_dict[key]):
                at = 0
                q += 1
                print(q)
                key = choice(all_keys)
                if q > 100:
                    print(acc)
                    print(value)
        else:
            key = choice(all_keys)

    t2 = time.time()
    T[0] = (T[0] + t2 - t1)
    print("\t Time of Mimic: " + str(t2 - t1))
    print("\t Total Dic Time: " + str(M))
    print("\t Total Merge Time: " + str(Me))
    print("\t Total Time: " + str(T))
    T[0] = (T[0] - T[0])
    Me[0] = (Me[0] - Me[0])
    M[0] = (M[0] - M[0])
    return acc


def merge_dictionary(dict1: dict, dict2: dict) -> dict:
    t1 = time.time()
    big_d = dict1.copy()
    small_d = dict2.copy()

    if len(dict1) > len(dict2):
        big_d = dict2.copy()
        small_d = dict1.copy()

    for i in small_d:
        for j in small_d[i]:
            big_d.setdefault(i, []).append(j)

    t2 = time.time()
    T[0] = (T[0] + t2 - t1)
    Me[0] = (Me[0] + t2 - t1)
    print("\t Time of Merge: " + str(t2 - t1))
    return big_d


def large():
    m1 = merge_dictionary(make_dictionary("Main/big.txt"),
                          make_dictionary("Main/big2.txt"))
    m2 = merge_dictionary(m1, make_dictionary("Main/big3.txt"))
    m3 = merge_dictionary(m2, make_dictionary("Main/big 4.txt"))
    m4 = merge_dictionary(m3, make_dictionary("Main/The holy book.txt"))
    m5 = merge_dictionary(m4, make_dictionary("Main/The holy book2.txt"))
    m6 = merge_dictionary(m5, make_dictionary("Main/The holy book3.txt"))
    m7 = merge_dictionary(m6, make_dictionary("Main/The holy book4.txt.txt"))
    m8 = merge_dictionary(m7, make_dictionary("Main/Hamlet.txt"))
    m9 = merge_dictionary(m8, make_dictionary("Main/big5.txt"))
    m10 = merge_dictionary(m9, make_dictionary("Main/big6.txt"))
    m11 = merge_dictionary(m10, make_dictionary("Main/big7.txt"))
    m12 = merge_dictionary(m11, make_dictionary("Main/big8.txt"))
    print(M)

    return m12


def large_nthgram(nth):
    m1 = merge_dictionary(make_nthgram_dictionary("Main/big.txt", nth),
                          make_nthgram_dictionary("Main/big2.txt", nth))
    m2 = merge_dictionary(m1, make_nthgram_dictionary("Main/big3.txt", nth))
    m3 = merge_dictionary(m2, make_nthgram_dictionary("Main/big 4.txt", nth))
    m4 = merge_dictionary(m3, make_nthgram_dictionary("Main/The holy book.txt", nth))
    m5 = merge_dictionary(m4,
                          make_nthgram_dictionary("Main/The holy book2.txt", nth))
    m6 = merge_dictionary(m5,
                          make_nthgram_dictionary("Main/The holy book3.txt", nth))
    m7 = merge_dictionary(m6, make_nthgram_dictionary("Main/The holy book4.txt.txt",
                                                      nth))
    m8 = merge_dictionary(m7, make_nthgram_dictionary("Main/Hamlet.txt", nth))
    m9 = merge_dictionary(m8, make_nthgram_dictionary("Main/big5.txt", nth))
    m10 = merge_dictionary(m9, make_nthgram_dictionary("Main/big6.txt", nth))
    m11 = merge_dictionary(m10, make_nthgram_dictionary("Main/big7.txt", nth))
    m12 = merge_dictionary(m11, make_nthgram_dictionary("Main/big8.txt", nth))
    m13 = merge_dictionary(m12,
                           make_nthgram_dictionary("Main/All_Shakespeare.txt", nth))

    return m13


def seuss(nth):
    m1 = make_nthgram_dictionary("Main/seuss1.txt", nth)

    for i in range(2, 7):
        m1 = merge_dictionary(m1, make_nthgram_dictionary(
            ("Main/seuss" + str(i) + '.txt'), nth))

    return m1


def grammar(marks, atricle, verb, prepostion, pronouns, conjection):
    # Article == 1
    # Noun == 2
    # Verb == 3
    # Preposition == 4
    # If Preposition, must loop, can't end on 4
    # Pronouns == 5
    Marks = ["!", "?", ".", "..."]
    for i in Marks:
        marks.append(i)
    Atricle = ["the", "some", "a", "an", "one"]
    for i in Atricle:
        atricle.append(i)
    with open("Main/en-verbs.txt", "r+") as file:
        lines = file.readlines()
        for i in lines:
            word = i.strip()
            word = word.replace(",,,,,,,,,,,,", " ")
            word = word.replace(",,,,,", " ")
            word = word.replace(",,,", " ")
            word = word.replace(",,", " ")
            words = word.split()
            for j in words:
                if "," in j:
                    verb.append(j[:j.find(",")].lower())
                elif len(j) > 0:
                    verb.append(j.lower())

    with open("Main/prepositions.txt", "r") as file:
        p = file.readlines()
    for i in range(len(p)):
        prepostion.append(p[i].strip().lower())

    with open("Main/pronouns.txt", "r+") as file:
        lines = file.readlines()
        for i in lines:
            word = i.strip()
            word = word.replace("'", "")
            word = word.replace(',', "")
            pronouns.append(word.lower())
    with open("Main/conjection.txt", "r+") as file:
        lines = file.readlines()
        for i in lines:
            word = i.strip().lower()
            conjection.append(word)


def check_part_of_spech(value, verb, prepostion, atricle, pronouns, conjection):

    # Article == 1
    # Noun == 2
    # Verb == 3
    # Preposition == 4
    # If Preposition, must loop, can't end on 4
    # Pronouns == 5

    counter = 0

    if len(value[0]) > 0:
        marks = [".", "!", "?", "..."]
        if value[0][-1] in marks:
            counter = 0
        elif value[0].lower() in verb:
            counter = 3
        elif value[0].lower() in prepostion:
            counter = 4
        elif value[0].lower() in atricle:
            counter = 1
        elif value[0] == "I" or value[0].lower() in pronouns:
            counter = 5
        elif value[0].lower() in conjection:
            counter = 6
        else:
            counter = 2
    return counter


def sentence_structure(value, acc, num_words, counter, all_value, verb, i, prep,
                       atricle, prev_word, pronouns, conjuntion):
    marks = ["!", "?", "."]
    if len(prev_word) < 1 or len(value) < 1:
        return True
    to_begin = not (len(acc) == 1 or prev_word[-1] in marks)
    to_begin = to_begin or value.istitle()
    to_begin = True

    capital = not (value.istitle()) or len(acc) == 1 or prev_word[-1] in marks
    capital = capital
    capital = True

    not_end_prepo = value[-1] not in marks or counter != 4
    not_end_prepo = True  ##

    ending = (i < (num_words - 1)) or (value[-1] in marks)

    not_double_verb = value not in verb
    not_double_verb = not_double_verb or counter != 3
    not_double_verb = True

    use_of_art = counter != 1 or value.lower() not in prep
    use_of_art = use_of_art or value.lower() not in verb
    use_of_art = True

    use_of_prep = value.lower() not in prep
    use_of_prep = use_of_prep or counter == 2
    use_of_prep = True

    after_prep = counter != 4 or value.lower() not in verb or value.lower() == "she"
    after_prep = after_prep or value.lower() == "he" or value.lower() == "they"
    after_prep = True

    use_of_pronouns = counter != 5 or (prev_word == "she" or prev_word == "his")
    use_of_pronouns = use_of_pronouns or prev_word == "them" or value in verb
    use_of_pronouns = use_of_pronouns or i >= num_words - 2
    use_of_pronouns = True

    dont_end_with = i != num_words - 1 or value not in pronouns
    after_verb = counter != 3 or value.lower() in pronouns
    after_verb = after_verb or value.lower() in prep or value.lower() in atricle
    after_verb = True

    pronouns_verbs = prev_word == "she" or prev_word == "his"
    pronouns_verbs = not (pronouns_verbs or prev_word == "them")
    pronouns_verbs = pronouns_verbs or not (value in verb)
    pronouns_verbs = True

    dont_repeat = value != prev_word

    dont_conjuct = counter != 1 or value not in conjuntion
    dont_conjuct = dont_conjuct or counter != 6
    dont_conjuct = True
    pronouns_article = counter != 1 or value not in pronouns

    state = ending and to_begin and capital and not_end_prepo
    state = state and not_double_verb and use_of_prep and use_of_art
    state = state and dont_repeat and use_of_pronouns and after_verb
    state = state and dont_conjuct and after_prep and dont_end_with
    state = state and pronouns_verbs

    # print("")
    # print(i)
    # print(acc)
    # print(value)
    # print("")
    return state


def shakespeare(nth):
    return make_nthgram_dictionary("Main/All_Shakespeare.txt", nth)


def main():
    print("Would you like to mimic from:")
    print('1. A random beginning')
    print("2. Or start from a phrase")
    mode = input("")
    print("\n")
    while not mode.isnumeric() or int(mode) not in range(1, 3):
        print("Invalid Entery")
        print("Would you like to mimic from:")
        print('1. A random beginning')
        print("2. Or start from a phrase")
        mode = input("")
        print("\n")

    mode = int(mode)
    print(mode)

    print("\n")
    print("1. Works of Dr.Suess")
    print("2. Works of Shakespeare")
    print("3. Stephen King")
    print("4. Very Big text file")
    selcetion = input("")
    print("\n")
    while not selcetion.isnumeric():
        print("Invalid Entery")
        print("1. Works of Dr.Suess")
        print("2. Works of Shakespeare")
        print("3. Stephen King")
        print("4. Very Big text file")
        selcetion = input("")
        print("\n")

    selcetion = int(selcetion)
    while not (selcetion in range(1, 5)):
        print("Invalid Entery")
        print("Invalid Entery")
        print("1. Works of Dr.Suess")
        print("2. Works of Shakespeare")
        print("3. Stephen King")
        print("4. Very Big text file")
        selcetion = input("")
        print("\n")
        while not selcetion.isnumeric():
            print("Invalid Entery")
            print("1. Works of Dr.Suess")
            print("2. Works of Shakespeare")
            print("3. Stephen King")
            print("4. Very Big text file")
            selcetion = input("")
            print("\n")
        selcetion = int(selcetion)

    nth = input("How long is your depth (A numeric value, ideally 2 or 3):")

    while not nth.isnumeric():
        print("\n")
        print("Invalid Entery")
        print("\n")
        nth = input("How long is your depth: ")

    nth = int(nth)

    while nth < 1:
        print("Invalid Entery")
        nth = input("How long is your depth: ")
        print("\n")
        while not nth.isnumeric():
            print("Invalid Entery")
            print("\n")
            nth = input("How long is your depth: ")
        nth = int(nth)

    if selcetion == 1:
        dic = seuss(nth)
    elif selcetion == 2:
        dic = shakespeare(nth)
    elif selcetion == 3:
        dic = stephen_king(nth)
    elif selcetion == 4:
        dic = large_nthgram(nth)
    else:
        dic = large_nthgram(nth)

    length = input("How many words would you like to mimic? ")

    while not length.isnumeric():
        print("Invalid Entery")
        print("\n")
        length = input("How many words would you like to mimic? ")

    length = int(length)

    while length < 1:
        print("Invalid Entery")
        length = input("How many words would you like to mimic? ")
        print("\n")
        while not length.isnumeric():
            print("Invalid Entery")
            print("\n")
            length = input("How many words would you like to mimic? ")
        length = int(length)

    all_keys = list(dic.keys())
    in_Val = True
    print("\n")
    if mode == 2:
        while in_Val:

            intitial_word = input("What would you like your text to start with?: ")
            intin = intitial_word
            intitial_word = intitial_word.split()

            if len(intitial_word) > len(all_keys[0]):
                for i in all_keys:
                    m = list(i)
                    if intitial_word[:len(m)] == m:
                        in_Val = False
            elif len(intitial_word) < len(all_keys[0]):
                for i in all_keys:
                    m = list(i)
                    if intitial_word == m[:len(intitial_word)]:
                        in_Val = False
            else:
                for i in all_keys:
                    m = list(i)
                    if intitial_word == m:
                        in_Val = False
            if in_Val:
                print("Invalid Phrase. Try something shorter.")
                print("\n")
        print("Please Wait...")
        text = mimic_text_from_phrase(dic, nth, length, intin, False)
        print(text)
        return None
    else:
        print("Please Wait...")
        text = mimic_text_nthgram(dic, nth, length, False)
        print(text)
        return None


def stephen_king(nth):
    return make_nthgram_dictionary("Main/Stphen King.txt", nth)


main()

