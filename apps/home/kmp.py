def highlight(text, indecies, length):
    for i in range(len(indecies) - 1, -1, -1):
        text = text[0:indecies[i]] + "<span class='highlight'>" + text[indecies[i]:indecies[i] + length] + "</span>" + text[indecies[i] + length:len(text)]
    return text

def longestPrefix(str):
    table = [None] * len(str)
    maxPrefix = 0
    table[0] = 0

    for i in range(1, len(str)):
        while maxPrefix > 0 and str[i] != str[maxPrefix]:
            maxPrefix = table[maxPrefix - 1]
        if str[maxPrefix] == str[i]:
            maxPrefix = maxPrefix + 1
        table[i] = maxPrefix
    return table


def kmp_algorithm(text, search):
    prefixes = longestPrefix(search)
    matches = []
  
    j = 0 # searchFor
    i = 0 # text
    while i < len(text):
        if text[i] == search[j]:
            i = i + 1
            j = j + 1

        if j == len(search):
            matches.append(i - j)
            j = prefixes[j - 1]
        elif i != len(text) and text[i] != search[j]:
            if j != 0:
                j = prefixes[j - 1]
            else:
                i = i + 1
    return matches