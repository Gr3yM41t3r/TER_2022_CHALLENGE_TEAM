import csv
import spacy
nlp = spacy.load("en_core_web_sm")


"""claims = []
claims.append("Hillary Clinton says she helped usher Iran to the negotiating table")
claims.append("In his first TV interview as president, Obama said we ''should talk to Iran")
claims.append("Paul Begala says Mitt Romney said he would pay no taxes under Paul Ryan's tax plan")"""


# fonction de nettoyage avec spacy
def nettoyage(sentences):
    # selection de la racine de chaque phrase
    document = list(nlp(sentences).sents)
    sentence_root = []
    for sentence in document:
        if sentence.root is not None:
            sentence_root.append(sentence.root)

    # selection des elements a supprimer
    for roo in sentence_root:
        elmt_to_rmv = [roo]
        for child in roo.children:
            if child.dep_ == 'nsubj':
                elmt_to_rmv.append(child)
        for c in elmt_to_rmv:
            if c != roo and [elem for elem in c.children] is not []:
                c2 = [c for c in c.children]
                if len(c2) == 1:
                    elmt_to_rmv.append(c2[0])

        # supression
        newsentences = ''
        for token in nlp(sentences):
            if token.idx not in [e.idx for e in elmt_to_rmv]:
                if len(newsentences) < 1:
                    newsentences = str(token)
                else:
                    newsentences += ' ' + str(token)
        return newsentences


'''
#displacy.serve(nlp(claims[0]), style="dep")
for cl in claims:
    print(cl,"...",nettoyage(cl))
'''