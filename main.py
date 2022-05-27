# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    str_1=list(word)
    str_1.sort()
    str_2=list(anagram)
    str_2.sort()
    if (str_1==str_2):
        return True
        
    else:
        return False
    
print(find_anagram("below", "elbow"))
print(find_anagram("hello", "check"))
