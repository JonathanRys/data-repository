import json

json_trie = './data/words.json'

def get_data(file: str) -> dict:
    with open(file) as f:
        trie = json.loads(f.read())
    return trie

def check(word: str, trie: dict=get_data(json_trie)) -> bool:
    if not word:
        return True
    if trie:
        return check(word[1:], trie.get(word[:1]))
    return False

def is_english(word: str) -> bool:
    if not word:
        return False
    return check(word)

if __name__ == "__main__":
    words = ['albatros', 'winner', 'success', 'erwrtwaf']
    for word in words:
        if is_english(word):
            print(f'English: {word}')
        else:
            print(f'Not English: {word}')
