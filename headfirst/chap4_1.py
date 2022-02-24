def search4vowels(word):
    """Display any vowels found in an asked-for word."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)


search4vowels('hitch-hiker')