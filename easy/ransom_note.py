def canConstruct(ransomNote, magazine):
    dict_ = {}
    for i in magazine:
        dict_[f"{i}"] = magazine.count(i)

    for i in ransomNote:
        dict_[i] -= 1

        if dict_[i] < 0:
            return False

    return True


ransomNote = "aa"
magazine = "aaab"
print(canConstruct(ransomNote, magazine))
