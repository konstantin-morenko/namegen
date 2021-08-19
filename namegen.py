
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
sonants = ['a', 'e', 'i', 'o', 'u', 'y']

import random

def make_syllables(consonants, sonants):
    syllables = []
    for c in consonants:
        for s in sonants:
            syllables.append(c + s)
    return syllables

def gen_word(ln = 3, start_with_sonant = False, end_with_consonant = False):
    sy = make_syllables(consonants, sonants)
    word = ""
    if start_with_sonant:
        word += random.choice(sonants)
    for i in range(0, ln):
        word += random.choice(sy)
    if end_with_consonant:
        word += random.choice(consonants)
    return word

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Generate random names')
    parser.add_argument('--syllables',
                        help='number of syllables',
                        type=int,
                        action='store',
                        default=3)
    parser.add_argument('--start-with-sonant',
                        action='store_true')
    parser.add_argument('--end-with-consonant',
                        action='store_true')
    parser.add_argument('--number-of-names',
                        type=int,
                        action='store',
                        default=1)
    parser.add_argument('--seed',
                        type=int,
                        action='store')
    args = parser.parse_args()

    if(args.seed):
        random.seed(args.seed)

    for i in range(0, args.number_of_names):
        print(str(i) + ": " + gen_word(args.syllables, args.start_with_sonant, args.end_with_consonant))
