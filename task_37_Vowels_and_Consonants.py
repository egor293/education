def Vowels_and_consonants(letter):
    if letter=='y':return 'Vowel or consonant'
    if letter=='a' or letter=='o' or letter=='u' or letter=='i' or letter=='u':return 'Vowel'
    return 'Consonant'

assert Vowels_and_consonants('a')=='Vowel',Vowels_and_consonants('a')
assert Vowels_and_consonants('y')=='Vowel or consonant',Vowels_and_consonants('y')
assert Vowels_and_consonants('s')=='Consonant',Vowels_and_consonants('s')