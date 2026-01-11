Ce script Perl est un **solveur d'anagrammes** qui permet de trouver tous les mots possibles à partir d'une série de lettres données. Voici une explication détaillée :

---

### 🔧 **Fonctionnalité principale**
Trouver toutes les anagrammes possibles (mots valides) à partir d'un ensemble de lettres, en utilisant une liste de mots prédéfinie (`wordlist.txt`).

---

## 📦 Structure du Script

---

### 1. **Initialisation et chargement du dictionnaire**

```perl
$WORDLIST = "<wordlist.txt";
open WORDLIST or die "can't open $WORDLIST\n";
```
- Tente d'ouvrir le fichier `wordlist.txt`, qui contient la liste des mots valides.
- Si le fichier n'existe pas, le programme s'arrête avec une erreur.

```perl
%ANAGRAM = ();
while (my $line = <WORDLIST>){
    chomp $line;
    $line =~ s/\r//g; # Supprime les retours chariot Windows
    $sorted = join("", sort split("", $line)); # Trie les lettres
    $ANAGRAM{$sorted} = "$line,$ANAGRAM{$sorted}";
}
```
- Pour chaque mot dans le fichier :
  - On supprime les caractères de fin de ligne (`chomp`).
  - On trie les lettres du mot par ordre alphabétique pour former une clé unique.
  - On stocke le mot original dans une table de hachage `%ANAGRAM`, avec comme **clé la version triée des lettres**.
  - Cela permet de regrouper les anagrammes (ex : "listen" → "enlist").

---

### 2. **Mode d'utilisation**

```perl
if ($ARGV[0]){ 
    doit($ARGV[0]); 
}
```
- Si un argument est passé au script (ex. `perl script.pl abcdef`), il traite directement ce mot.

Sinon, il entre en mode interactif :

```perl
for (;;){
    print "\nLettres: "; 
    if ($line = <STDIN>){
        chomp $line; 
        doit($line); 
    } else {
        exit(0); 
    }
}
```
- Boucle infinie demandant à l'utilisateur d'entrer des lettres.
- Appelle la fonction `doit()` sur ces lettres.

---

### 3. **Traitement des lettres : Fonction `doit()`**

```perl
my @GIVEN = sort split("", uc($x));
```
- Convertit les lettres en majuscules et les trie.

```perl
for ($i = 0; $i < 32768; $i++){
    my $candidat = "";
    for ($bit = 0; $bit < 15; $bit++){
        if ($i & (1 << $bit)){
            $candidat = "$candidat"."$GIVEN[$bit]";
        }
    }
```
- **Boucle géniale** : Utilise une boucle de 0 à 32767 (soit 2^15) pour simuler **toutes les combinaisons possibles de lettres**.
  - Chaque bit de `$i` correspond à une lettre de `@GIVEN`.
  - Si le bit est à 1, la lettre est incluse dans le mot candidat.
  - Cela permet d'explorer **toutes les sous-séquences de lettres** (de 0 à 15 lettres).

```perl
my $soluce = "";
if ($soluce = $ANAGRAM{$candidat}){
    print "$ANAGRAM{$candidat}\n";
    $SOLUTION{$soluce} = length $soluce;
}
```
- Regarde si le mot candidat (lettres triées) existe dans la table `%ANAGRAM`.
- Si oui, ajoute la solution trouvée dans `%SOLUTION`.

---

### 4. **Affichage des résultats**

```perl
foreach $key (sort bylength keys %SOLUTION){
    my @C = split ',',$key;
    print "[" . length( $C[0]) . "] $key\n";
}
```
- Trie les résultats par **longueur des mots**, grâce à la fonction `bylength`.
- Affiche les mots trouvés avec leur longueur entre crochets.

---

## 🎯 Exemple d'utilisation

Si tu donnes `"ATELIER"` au script :

- Il va générer toutes les combinaisons de lettres (E, A, T, L, I, R, etc.)
- Chercher si celles-ci correspondent à des mots connus.
- Afficher quelque chose comme :
  ```
  [3] RAT,
  [4] LIRE, TELA,
  [5] AILER, RELAT,
  ...
  ```

---

## 🧠 Points techniques importants

- **Performance** : Le script explore 2^15 = 32768 combinaisons possibles, donc limité à 15 lettres.
- **Indexation par anagramme** : La clé est le mot trié, donc `"listen"` et `"silent"` ont la même clé (`eilnst`).
- **Mode interactif vs direct** : Peut fonctionner en boucle interactive ou en mode commande directe.

---

## 🧩 Inspiré du jeu "Le Mot le Plus Long"

Ce genre de script est typiquement utilisé pour résoudre des énigmes de type **"Des chiffres et des lettres"**, notamment l'épreuve du **Mot le Plus Long**.

