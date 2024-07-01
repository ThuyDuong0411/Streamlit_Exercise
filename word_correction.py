import streamlit as st


def levenshtein_distance(source, target):
    n = len(source) + 1
    m = len(target) + 1
    distances = [[0] * m for i in range(n)]
    for i in range(n):
        distances[i][0] = i
    for j in range(m):
        distances[0][j] = j
    a = 0
    b = 0
    c = 0
    for i in range(1, n):
        for j in range(1, m):
            if (source[i-1] == target[j-1]):
                distances[i][j] = distances[i-1][j-1]
            else:
                a = distances[i][j-1]
                b = distances[i-1][j]
                c = distances[i-1][j-1]
                if (a <= b and a <= c):
                    distances[i][j] = a + 1
                elif (b <= a and b <= c):
                    distances[i][j] = b + 1
                else:
                    distances[i][j] = c + 1
    return distances[n-1][m-1]


def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words


def main():
    vocabs = load_vocab(file_path='./vocab.txt')
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input("Your word")
    if st.button("Compute"):
        distances = dict()
        for vocab in vocabs:
            distance = levenshtein_distance(word, vocab)
            distances[vocab] = distance
        sorted_distances = dict(
            sorted(distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distances.keys())[0]
        st.write("Correct:", correct_word)

        col1, col2 = st.columns(2)
        col1.write(vocabs)
        col2.write(sorted_distances)


if __name__ == "__main__":
    main()
