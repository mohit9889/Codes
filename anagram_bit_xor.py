def isAnagram(s1, s2):
    if len(s1) != len(s2):
        print("length different")
    else:
        value = 0
        for i in range(0, len(s1)):
            value = value ^ ord(s1[i])
            print(s1[i],":",value)
            value = value ^ ord(s2[i])
            print(s2[i],":",value)
        if value == 0:
            print("Anagram")
        else:
            print("Not Anagram")

s1 = "aabbcd"
s2 = "abbadc"
isAnagram(s1, s2)
