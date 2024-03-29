def maximumOddBinaryNumber(s: str) -> str:
    answer = ['0'] * len(s)
    j = 0

    for i in range(len(s)):
        if s[i] == '1':
            answer[j] = '1'
            j += 1

    answer[j - 1], answer[-1] = answer[-1], '1'

    return ''.join(answer)
