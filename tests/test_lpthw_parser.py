from sentence_parser.lpthw_parser import *
import pytest

def test_word_list():
    assert peek([
        ('subject', 'player'),
        ('verb', 'run'), 
        ('direction', 'north')
    ]) == 'subject'
    assert peek([]) == None

def test_match():
    test =[
        ('subject', 'player'),
        ('verb', 'run'), 
        ('direction', 'north')
    ]
    assert match(test, 'subject') ==  ('subject', 'player')
    assert match(test, 'object') == None
    assert match([], 'verb') == None

def test_skip():
    test = [
        ('verb', 'run'),
        ('verb', 'kill'),
        ('noun', 'bear')
    ]
    skip(test, 'verb')
    assert test == [('noun', 'bear')]

def test_parse_verb():
    test = [
        ('verb', 'run'),
        ('verb', 'kill'),
        ('stop', 'the'),
        ('noun', 'bear')
    ]
    assert parse_verb(test) == ('verb', 'run') 
    assert parse_verb(test) == ('verb', 'kill')
    with pytest.raises(Exception):
        parse_verb(test)
    assert test == [('noun', 'bear')]

def test_parse_object():
    test = [
        ('stop', 'the'),
        ('noun', 'bear')
    ]
    assert parse_object(test) == ('noun', 'bear')
    assert test == []

def test_parse_subject():
    test = [
        ('verb', 'kill'),
        ('stop', 'the'),
        ('noun', 'bear')
    ]
    assert parse_subject(test) == ('noun', 'player')
    test.pop(0)
    assert parse_subject(test) == ('noun', 'bear')
    assert test == []

def test_parse_numbers():
    test = [
        ('stop', 'the'),
        ('number', 2),
        ('noun', 'bear')
    ]
    assert parse_numbers(test) == ('number', 2)
    with pytest.raises(Exception):
        parse_numbers(test)

def test_parse_sentence():
    assert sentence.subject == 'bear'
    assert sentence.verb == 'run'
    assert sentence.object == 'south'
    assert sentence.string == 'bear run south'

    
    
    


    


    
    




    

