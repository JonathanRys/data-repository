import os
import json
import urllib3
 
eng_trie = {}

def add_to_trie(trie: dict, word: str, lower: bool=False) -> dict:
    if lower:
        word = word.lower()
    letter = word[:1]

    if len(word) == 1:
        # This is the last letter, add a terminator
        trie[word] = {**trie.get(word, {}), "EOW": True}
    else:
        if not trie.get(letter):
            trie[letter] = {}
        trie[letter] = add_to_trie(trie[letter], word[1:])
    return trie

if __name__ == "__main__":
    output_file = "./data/words.json"
    url = "https://github.com/JonathanRys/data-repository/blob/master/data/words.txt?raw=true"
    response = urllib3.request("GET", url)
    if response.status:
        for word in [word.strip() for word in response.data.decode().split('\n')]:
            if word:
                try:
                    add_to_trie(eng_trie, word, lower=True)
                except Exception as e:
                    print(f'ERROR for word "{word}": {e}')
    
    with open(output_file, 'w') as f:
        print(json.dumps(eng_trie), file=f)
