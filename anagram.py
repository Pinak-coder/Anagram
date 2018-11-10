
def anagram(string_a,string_b):
  dict_a = {}
  dict_b = {}
  int_i = 0
  int_j = 0
  while int_i < len(string_a):
    if string_a[int_i] in dict_a:
      dict_a[string_a[int_i]] += 1
    else:
      dict_a[string_a[int_i]] = 1
    int_i +=1
  print(dict_a)

  while int_j < len(string_b):
    if string_b[int_j] in dict_b:
      dict_b[string_b[int_j]] += 1
    else:
      dict_b[string_b[int_j]] = 1
    int_j +=1
  print(dict_b)  

  int_k = 0
  while int_k < len(string_a):
    if string_a[int_k] in dict_b and dict_a[string_a[int_k]] == dict_b[string_a[int_k]]:
      int_k +=1
    else:
      return "it isnt"
  return "its an anagram lol"

print(anagram("hello","helol"))
    
