from collections import Counter 
def is_anagram(str1, str2): 
     return Counter(str1) == Counter(str2) 
  
# or without having to import anything  
def is_anagram(str1, str2):  
    return sorted(str1) == sorted(str2)  
s1=input('Enter first String: ')
s2=input('Enter 2nd String: ')
if (is_anagram(s1,s2)):
    print('They are Anagrams')
else:
    print('They are not Anagrams')
