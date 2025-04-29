# Solutions to group anagrams
def group_anagrams(words):
    anagram_map = {}
    
    for word in words:
        
        sorted_word = ''.join(sorted(word))
        
        if sorted_word in anagram_map:
            anagram_map[sorted_word].append(word)
        else:
            anagram_map[sorted_word] = [word]
            
    return list(anagram_map.values())

# Example usage
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(words)
print(result)
