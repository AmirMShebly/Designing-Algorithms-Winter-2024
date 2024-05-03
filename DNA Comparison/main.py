def longest_common_subsequence(sequence1, sequence2):
    m = len(sequence1)
    n = len(sequence2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if sequence1[i - 1] == sequence2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_length = dp[m][n]
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if sequence1[i - 1] == sequence2[j - 1]:
            lcs.append(sequence1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs.reverse()
    return lcs_length, ''.join(lcs)


def main():
    sequence1 = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
    sequence2 = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"
    length, lcs = longest_common_subsequence(sequence1, sequence2)
    print("Length of LCS:", length)
    print("LCS:", lcs)


if __name__ == "__main__":
    main()