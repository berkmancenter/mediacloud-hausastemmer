from hausastemmer.HausaStemmer import HausaStemmer

# noinspection PyRedundantParentheses
__all__ = ('stem')

__stemmer = HausaStemmer()


def stem(term, lookup=True):
    # type: (str, bool) -> str
    """Stem Hausa language term (word).
    :param term: term (word) to stem
    :param lookup: whether to use lookup dictionary for stemming
    :return: stemmed term, or original term if the term can't be stemmed
    :rtype: str
    """

    # FIXME maybe trim the stem?
    # FIXME remove len()
    # FIXME implement lookup()
    term_stem = __stemmer.stem(p=term, i=0, j=len(term) - 1, lookup=lookup)

    return term_stem
