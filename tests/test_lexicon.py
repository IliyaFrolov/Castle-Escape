from sentence_parser import lexicon as lex

def test_directions():
    assert lex.scan("north south east down up") == [
        ('direction', 'north'), 
        ('direction', 'south'), 
        ('direction', 'east'),
        ('direction', 'down'),
        ('direction', 'up')
        ]

def test_verbs():
    assert lex.scan("go kill eat") == [
        ('verb', 'go'),
        ('verb', 'kill'),
        ('verb', 'eat')
    ]

def test_stops():
    assert lex.scan("the in of") == [
        ('stop', 'the'),
        ('stop', 'in'),
        ('stop', 'of')
    ]

def test_nouns():
    assert lex.scan("bear princess") == [
        ('noun', 'bear'),
        ('noun', 'princess')
    ]

def test_numbers():
    assert lex.scan("3 91234") == [
        ('number', 3),
        ('number', 91234)
    ]

def test_errors():
    assert lex.scan("bear IAS princess 3890md") == [
        ('noun', 'bear'),
        ('error', 'IAS'),
        ('noun', 'princess'),
        ('error', '3890md')
    ]

def test_capitalization():
    assert lex.scan(('29456 BEar DowN KiLL')) == [
        ('number', 29456),
        ('noun', 'bear'),
        ('direction', 'down'),
        ('verb', 'kill')
    ]