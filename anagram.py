def isAnagram(strng1: str, strng2: str) -> bool:
  print("Checking for Anagrams")

  if strng1.isalnum == False or strng2.isalnum == False:
    return False

  strng1.upper()
  s_list1 = strng1.split()
  s_list1 = sorted(s_list1)
  print("First word: ", s_list1)

  strng2.upper()
  s_list2 = strng2.split()
  s_list2.sort()
  print("Second word: ", s_list2)

  if s_list1 == s_list2:
    return True
  
  return False

