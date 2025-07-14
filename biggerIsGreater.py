def biggerIsGreater(w):
    l1 = list(w)
    for char in range(len(l1)-1,-1,-1):
        for i in range(char-1,-1,-1):
            if l1[i]<l1[char]:
                for j in range(char,len(l1)+1):
                    l1[j],l1[i] = l1[i],l1[j]
                    return ''.join(l1)
                


word = "dkhc"
print(biggerIsGreater(word))


'''
    Summarization of the idea proposed:
        the fishermen community of a particular village are facing a issue while going for fishing with their GPS trackers. The issue is that GPS trackers(preferably their own mobile devices) are not waterproof & hence gets damaged very often. We are asked to come up with an effective solution to solve this issue of GPS trackers...

    Solution discussed so far:
        1. In the beginning we discussed about buying a cost effective GPS tracker which of course is the easier way
        2. Then after going through some of the research papers i came up with the idea of linking GPS trackers along with the signal frequencies to track the availability of fishes in that particular area so that they can increase the probability of dropping their net & catching more fishes
        3. The final conclusion that we came to was to delve more deeper into the above mentioned & solution & check out on its practical application, also a point to be noten is that, if i also come to know what kind of fish is available in this particular area it will increase my probability of earning more money in the market as each fish has its own value in the market
'''