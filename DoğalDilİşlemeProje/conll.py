import nltk
from conllu import TokenList, Token
nltk.download('punkt')


def translate_conll(turkish_text):
    sentences = nltk.sent_tokenize(turkish_text, language='turkish')
    tokenized_sentences = [nltk.word_tokenize(sentence, language='turkish') for sentence in sentences]
    conll_output = ""
    for sentence in tokenized_sentences:
        token_list = TokenList()
        for i, word in enumerate(sentence):
            token = Token(index=i+1, form=word, lemma=word.lower(), upos='_', xpos='_', feats='_', head='_', deprel='_', deps='_', misc='_')
            token_list.append(token)
        conll_output += token_list.serialize() + "\n"

    with open('output.conll', 'a', encoding='utf-8') as f:
        f.write(conll_output)


