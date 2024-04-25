import string
#map version
def checkIfPangram(sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        freq = {}
        let = list(string.ascii_lowercase)
        for char in let:
            freq[char] = 0

        for char in sentence:
            freq[char] += 1

        for char in let:
            if freq[char] == 0:
                return False

        return True

#set Version
def checkPanagram(sentence:str) ->bool:
    check = set()
    for char in sentence:
        if char in check:
            continue
        else:
            check.add(char)
    
    return len(check) == 26
check = "jwtucoucmdfwxxqnxzkaxoglszmfrcvjoiunqqausaxxaaijyqdqgvdnqcaihwilqkpivenpnekioyqujrdrovqrlxovcucjqzjsxmllfgndfprctxvxwlzjtciqxgsxfwhmuzqvlksyuztoetyjugmswfjtawwaqmwyxmvo"

checkIfPangram(check)