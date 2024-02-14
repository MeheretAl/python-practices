def longSubstring(word: str) -> int:
    i = 0
    j = 0
    holder = set()
    maxmiumLength = 0
    while i < len(word):
        while(word[i] in holder):
            holder.remove(word[j])
            j+=1
        holder.add(word[i])
        maxmiumLength = max(maxmiumLength,i-j+1)
        i+=1


    return maxmiumLength

            


word = "PWWKEW" 
print(longSubstring(word))


