from collections import defaultdict


def group_anagrams(strs):
    # anagrams = defaultdict(list)
    # for word in strs:
    #     sorted_word = ''.join(sorted(word))
    #     anagrams[sorted_word].append(word)
    # return anagrams.values()
    dict_ = {}
    for data in strs:
        word_data = "".join(sorted(data))

        if word_data not in dict_:
            dict_[word_data] = [data]
        else:
            dict_[word_data].append(data)
    result = []

    for data in dict_.values():
        result.append(data)
    return result


print("Reversed word:", group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
