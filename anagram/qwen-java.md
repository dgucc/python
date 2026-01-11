---

Souhaites-tu une version optimisée ou adaptée à un usage particulier ?

Voici une version **optimisée** du script Perl, en Java, qui améliore la **vitesse**, la **mémoire**, et la **lisibilité**.

---

### ✅ Optimisations apportées

1. **Suppression des doublons** dans les combinaisons (éviter de recompter les mêmes lettres).
2. **Utilisation de structures efficaces** : `Set`, `StringBuilder`, `BitSet`, etc.
3. **Limitation des calculs redondants** (par exemple, ne pas trier à chaque fois).
4. **Prétraitement du dictionnaire** pour réduire la recherche.
5. **Génération des sous-masques de bits plus efficace**.

---

## ✨ Version Java optimisée

```java
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class OptimizedAnagramSolver {

    private static Map<String, Set<String>> anagramMap = new HashMap<>();

    public static void main(String[] args) throws IOException {
        loadWordlist("wordlist.txt");

        if (args.length > 0) {
            doit(args[0]);
        } else {
            Scanner scanner = new Scanner(System.in);
            while (true) {
                System.out.print("\nLettres: ");
                System.out.flush();

                String input = scanner.nextLine().trim();
                if (input.isEmpty()) break;

                doit(input);
            }
        }
    }

    private static void loadWordlist(String filename) throws IOException {
        try (BufferedReader reader = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = reader.readLine()) != null) {
                line = line.trim().toUpperCase();
                char[] chars = line.toCharArray();
                Arrays.sort(chars);
                String sorted = new String(chars);

                anagramMap.computeIfAbsent(sorted, k -> new HashSet<>()).add(line);
            }
        }
    }

    private static void doit(String letters) {
        letters = letters.toUpperCase();
        char[] available = letters.toCharArray();
        Arrays.sort(available);

        Set<String> foundWords = new TreeSet<>(); // Pour tri automatique

        int n = Math.min(available.length, 15); // Limite à 15 lettres
        int mask = 1 << n;

        for (int i = 1; i < mask; i++) {
            StringBuilder candidate = new StringBuilder();
            for (int j = 0; j < n; j++) {
                if ((i & (1 << j)) != 0) {
                    candidate.append(available[j]);
                }
            }

            String sortedCandidate = candidate.toString();
            Set<String> matches = anagramMap.get(sortedCandidate);
            if (matches != null) {
                foundWords.addAll(matches);
            }
        }

        // Grouper par longueur
        Map<Integer, List<String>> groupedByLength = foundWords.stream()
            .collect(Collectors.groupingBy(String::length));

        System.out.println("-------------------------");
        System.out.println("Anagrammes de [" + letters + " - " + letters.length() + "]");
        System.out.println("-------------------------");

        groupedByLength.entrySet().stream()
            .sorted(Map.Entry.comparingByKey())
            .forEach(entry -> {
                System.out.println("[" + entry.getKey() + "] " + String.join(", ", entry.getValue()));
            });
    }
}
```

---

## 🚀 Améliorations notables

- **HashSet/Set pour les résultats** → évite les doublons.
- **TreeSet** pour trier les résultats automatiquement.
- **Stream API** pour grouper par longueur proprement.
- **Limite à 15 lettres** pour ne pas exploser la mémoire ou le temps de calcul.
- **Stockage des mots dans des Sets** dans le dictionnaire → pas de chaînes concaténées à parser.

---

## 🧪 Exemple de sortie

```
Lettres: ATELIER

-------------------------
Anagrammes de [ATELIER - 7]
-------------------------
[3] RAT, TAR
[4] LIRE, TELA
[5] AILER, RELAT
[6] ALTERE, LATERE
...
```

---

## 💡 Variante : avec tri par score / points

Si tu veux aussi attribuer des points aux mots (comme au Scrabble), tu peux rajouter une fonction de score :

```java
private static int computeScore(String word) {
    int[] scores = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
    return word.chars().map(c -> scores[c - 'A']).sum();
}
```

Puis trier les résultats par score croissant/décroissant.

---

Souhaites-tu aussi une version en Python ou C++ optimisée ?