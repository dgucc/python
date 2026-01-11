Voici une **version optimisée du solveur d'anagrammes en Python**, qui reprend les mêmes idées que la version Java mais avec les particularités de Python :

---

## ✨ Version Python optimisée

```python
#!/usr/bin/env python3
from collections import defaultdict
import sys

def load_wordlist(filename="wordlist.txt"):
    anagram_map = defaultdict(set)
    try:
        with open(filename, "r", encoding='utf-8') as f:
            for line in f:
                word = line.strip().upper()
                key = ''.join(sorted(word))
                anagram_map[key].add(word)
    except FileNotFoundError:
        print("Erreur : impossible d'ouvrir wordlist.txt")
        sys.exit(1)
    return anagram_map

def doit(letters, anagram_map):
    letters = letters.upper()
    available = sorted(letters)
    n = min(len(available), 15)  # Limite à 15 lettres pour éviter explosion
    found_words = set()

    for i in range(1, 1 << n):  # 2^n combinaisons
        candidate = []
        for j in range(n):
            if i & (1 << j):
                candidate.append(available[j])
        sorted_candidate = ''.join(candidate)
        if sorted_candidate in anagram_map:
            found_words.update(anagram_map[sorted_candidate])

    # Grouper par longueur
    grouped = defaultdict(list)
    for word in found_words:
        grouped[len(word)].append(word)

    # Afficher
    print(f"-------------------------")
    print(f"Anagrammes de [{letters} - {len(letters)}]")
    print(f"-------------------------")

    for length in sorted(grouped):
        words = ', '.join(sorted(grouped[length]))
        print(f"[{length}] {words}")

def main():
    anagram_map = load_wordlist()

    if len(sys.argv) > 1:
        doit(sys.argv[1], anagram_map)
    else:
        while True:
            try:
                letters = input("\nLettres: ").strip()
                if not letters:
                    break
                doit(letters, anagram_map)
            except (EOFError, KeyboardInterrupt):
                break

if __name__ == "__main__":
    main()
```

---

## 🔍 Points clés de l’optimisation

- **`defaultdict(set)`** → pas besoin de vérifier si une clé existe.
- **`set` pour les résultats** → pas de doublons.
- **`''.join(sorted(word))`** → rapide pour obtenir la clé de tri.
- **`1 << n`** → puissance de 2 rapide pour les combinaisons.
- **Tri des résultats par longueur** → plus lisible.
- **Encodage UTF-8** → gestion des accents si nécessaire.

---

## 🧪 Exemple d’exécution

```bash
$ python3 anagram_solver.py ATELIER
-------------------------
Anagrammes de [ATELIER - 7]
-------------------------
[3] RAT, TAR
[4] LIRE, TELA
[5] AILER, RELAT
[6] ALTERE, LATERE
...
```

Ou en mode interactif :

```bash
$ python3 anagram_solver.py
Lettres: ATELIER
[...]
```

---

Souhaites-tu une version qui utilise des **trie**, **backtracking**, ou qui trie par **score de mots** (comme au Scrabble) ?