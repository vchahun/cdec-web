import nltk
import re
import subprocess as sp

FIASANA = '/home/vchahune/tools/fiasana/bin'

class FiasanaTokenizer:
    def __init__(self, lang):
        self.pnorm = sp.Popen(['perl', FIASANA+'/normalize-text-standalone.pl', '-'+lang],
                stdin=sp.PIPE, stdout=sp.PIPE)
        self.ptok = sp.Popen(['perl', FIASANA+'/tokenize-text.pl', '--'+lang], 
                stdin=self.pnorm.stdout, stdout=sp.PIPE)

    def tokenize(self, sentence):
        self.pnorm.stdin.write(sentence.encode('utf8')+'\n')
        return self.ptok.stdout.readline()[:-1].decode('utf8')

class Tokenizer:
    def __init__(self):
        self.subs = [(re.compile(f, re.I | re.U), t) for (f, t) in self.subs]

    def tokenize(self, s):
        for f, t in self.subs:
            s = f.sub(t, s)
        return s

class EnglishDetokenizer(Tokenizer):
    subs = [ # Punctuation < left
            (u" ([,\.:;!\?\%\*\)\]\/\u201d\u2026])", r"\1"),
            # Punctuation > right
            (u"([\(\[\/\u201c]) ", r"\1"),
            # Hyphen
            (" @-@ ", r"-"),
            # Elisions
            (" (n't|'s|'m|'d|'ll|'re|'ve)", r"\1") ]

def recase(sentence):
    return sentence[0].upper()+sentence[1:] if sentence else ''

tokenizers = {
    'en': FiasanaTokenizer('eng'),
    'mg': FiasanaTokenizer('mlg')
}

detokenizers = {
    'en': EnglishDetokenizer()
}

def sent_tokenize(text):
    for sentence in nltk.sent_tokenize(text):
        yield sentence.strip().replace('\n', ' ')

def preprocess(sentence):
    return tokenizers['mg'].tokenize(sentence).lower()

def postprocess(sentence):
    return recase(detokenizers['en'].tokenize(sentence))
