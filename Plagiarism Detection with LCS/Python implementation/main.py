def longest_common_subsequence(base_doc, student_doc):
    m = len(base_doc)
    n = len(student_doc)

    table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if base_doc[i - 1] == student_doc[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    return table[m][n]


def main():

    with open('base_document.txt', 'r') as base_file:
        base_doc = base_file.read().lower().split()

    with open('student_document.txt', 'r') as student_file:
        student_doc = student_file.read().lower().split()

    lcs_length = longest_common_subsequence(base_doc, student_doc)

    base_doc_length = len(base_doc)
    student_doc_length = len(student_doc)
    average_length = (base_doc_length + student_doc_length) / 2

    similarity_percentage = (lcs_length / average_length) * 100

    print("LCS length: ", lcs_length)
    print(f"Similarity Percentage: {similarity_percentage:.2f}%")


if __name__ == "__main__":
    main()
