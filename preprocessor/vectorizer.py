import numpy as np
from scipy.sparse import lil_matrix


def get_bigramms(word):
    """
    Функция, составляющая по слову множество биграмм его букв.
    """
    n_gramms = set()
    n_gramms.add(" " + word[0])
    n_gramms.add(word[-1] + " ")
    for i in range(0, len(word) - 2):
        n_gramms.add(word[i:i + 2])
    return n_gramms


class CountVectorizer:
    """
    Класс, реализующий преобразование строк в векторы с помощью подхода Bag of Words.
    :param analyzer: 'word' - мешок слов, 'char_bigrams' - мешок буквенных биграмм
    """
    def __init__(self, analyzer='word'):
        """
        """
        self.columns = []
        self.n_dimensions = 0
        self.analyzer = analyzer
    
    def fit(self, texts):
        """
        Функция, находящая все уникальные слова или буквенные n-граммы в данных текстах.
        """
        col = set()
        for text in texts:
            for word in text.split():
                if self.analyzer == 'word':
                    if word not in col:
                        col.add(word)
                elif self.analyzer == 'char_bigrams':
                    bigramms = get_bigramms(word)
                    col = col | bigramms
        self.n_dimensions = len(col)
        self.columns = list(col)


    def fit_transform(self, texts):
        self.fit(texts)
        return self.transform(texts)

    def transform(self, texts):
        """
        Функция, преобразующая список строк в массив numpy.array
        """
        shape = (len(texts), self.n_dimensions)
        matrix = lil_matrix(shape)
        for row_index, text in enumerate(texts):
            enterings = {k: 0 for k in self.columns}

            for key in enterings:
                if self.analyzer == 'word':
                    enterings[key] = text.count(key)
                elif self.analyzer == 'char_bigrams':
                    bigramms = []
                    for word in text.split():
                        bigramms.extend(get_bigramms(word))
                    enterings[key] = bigramms.count(key)

            for column_index, col in enumerate(self.columns):
                matrix[row_index, column_index] = enterings[col]
        return matrix

    def __setstate__(self, d):
        self.columns = d['columns']
        self.n_dimensions = d['n_dim']
        self.analyzer = d['analyzer']

    def __getstate__(self):
        return {'columns': self.columns, 'n_dim': self.n_dimensions, 'analyzer': self.analyzer}


