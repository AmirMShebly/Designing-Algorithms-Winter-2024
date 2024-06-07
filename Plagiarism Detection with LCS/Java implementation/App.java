package com.tabrizu;


import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;



public class App 
{
    public static List<String> readDocument(String filepath) throws IOException {
        List<String> words = new ArrayList<>();
        BufferedReader reader = new BufferedReader(new FileReader(filepath));

        String line;
        while((line = reader.readLine()) != null) {
            String[] tokens = line.toLowerCase().split("\\s+");
            for (String token: tokens) {
                if (!token.isEmpty()) {
                    words.add(token);
                }
            }
        }
        reader.close();
        return words;
    }

    public static int longestCommonSubsequence(List<String> baseDoc, List<String> studentDoc) {
        int m = baseDoc.size();
        int n = studentDoc.size();

        int[][] table = new int[m+1][n+1];

        for(int i = 1; i<=m; i++) {
            for (int j = 1; j <= n; j++) {
                if(i == 0 || j==0) {
                    table[i][j] = 0;
                }
                if (baseDoc.get(i-1).equals(studentDoc.get(j-1))) {
                    table[i][j] = table[i-1][j-1] + 1;
                }
                else {
                    table[i][j] = Math.max(table[i-1][j], table[i][j-1]);
                }
            }
        }
        return table[m][n];
    }



    
    public static void main( String[] args ) {
        try {
            List<String> baseDoc = readDocument("C:\\Users\\Lenovo\\Desktop\\DSA\\Java\\plagiarism-lcs\\src\\main\\java\\com\\tabrizu\\base_document.txt");
            List<String> studentDoc = readDocument("C:\\Users\\Lenovo\\Desktop\\DSA\\Java\\plagiarism-lcs\\src\\main\\java\\com\\tabrizu\\student_document.txt");

            int lcsLength = longestCommonSubsequence(baseDoc, studentDoc);

            double averageLength = (baseDoc.size() + studentDoc.size()) / 2.0;

            double similarityPercent = (lcsLength / averageLength) * 100.0;

            System.out.println("LCS length: " + lcsLength);
            System.out.println("Similarity Percentage: " + similarityPercent);

        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
}
