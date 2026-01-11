
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class AnagramSolver {

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