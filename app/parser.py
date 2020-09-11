class Sentence():

    def __init__(self, subject, verb, obj):
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]
        self.string = f'{self.subject} {self.verb} {self.object}'
    
    def __repr__(self):
        return f'{self.subject} {self.verb} {self.object}'
    
def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    
    else:
        return None

def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)
        if word[0] == expecting:
            return word
        
        else:
            return None
    
    else:
        return None

def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)

def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    
    else:
        return (None, None) 

def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)
    
    if next_word == 'noun':
        return match(word_list, 'noun')
    
    elif next_word == 'direction':
        return match(word_list, 'direction')
    
    else:
        return (None, None)

def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'number':
        return match(word_list, 'number')
    
    elif next_word == 'noun':
        return match(word_list, 'noun')
    
    elif next_word == 'verb':
        return ('noun', 'i')
    
    else:
        return (None, None)

def parse_numbers(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'number':
        return match(word_list, 'number')
    
    else:
        return None

def parse_sentence(word_list):
    subj = parse_subject(word_list)

    if isinstance(subj[1], int):
        return subj[1]

    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)

def scan(words):

    directions = [
        'down', 'downstairs', 'upstairs','up', 'north', 
        'west', 'back', 'south', 'east'
    ]
    verbs = ['go', 'open', 'look', 'pull', 'take']
    stop_words = ['the', 'in', 'through', 'at', 'it', 'to', 'big', 'main']
    nouns = ['door', 'trapdoor', 'lever', 'note', 'i', 'hall']
    numbers = [f'{i}' for i in range(0, 10)]

    words_list = words.split()
    type_word = []

    for i in words_list:
        x = i.lower()
        
        if x in directions:
            type_word.append(('direction', x))
    
        elif x in verbs:
            type_word.append(('verb', x))

        elif x in stop_words:
            type_word.append(('stop', x))
        
        elif x in nouns:
            type_word.append(('noun', x))
        
        elif list(i)[0] in numbers:
            type_word.append(('number', int(i)))
        
        else:
            type_word.append(('error', i))
    
    return type_word






    
     
    



