#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Andvance Intent and  Word Vector and ML Classification
Created on Mon May 21 12:22:30 2018

@author: hvyd
"""
import spacy
from sklearn.svm import SVC

# Define included entities
include_entities = ['DATE', 'ORG', 'PERSON']

# extract_entities(
def extract_entities(message):
    # dict to hold the entities
    ents = dict.fromkeys(include_entities)
    # Cspacy document
    doc = nlp(message)
    for ent in doc.ents:
        if ent.label_ in include_entities:
            # Save interesting entities
            ents[ent.label_] = ent.text
    return ents


doc = nlp("let's see that jacket in red and some blue jeans")

# Iterate over parents in parse tree
def find_parent_item(word):
    # Iterate over the word's ancestors
    for parent in word.ancestors:
        # Check for an "item" entity
        if entity_type(parent) == "item":
            return parent.text
    return None

# finds parent color entity
def assign_colors(doc):
    # Iterate over the document
    for word in doc:
        # Check for "color" entities
        if entity_type(word) == "color":
            # Find the parent
            item =  find_parent_item(word)
            print("item: {0} has color : {1}".format(item, word))






nlp = spacy.load('en')
n_sentences = len(sentences)
embedding_dim = nlp.vocab.vectors_length
X = np.zeros((n_sentences, embedding_dim))
for idx, sentence in enumerate(sentences):
    doc = nlp(sentence)
    X[idx, :] = doc.vector


#Classifier SVC
clf = SVC()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
n_correct = 0
for i in range(len(y_test)):
    if y_pred[i] == y_test[i]:
        n_correct += 1

print("Predicted {0} correctly out of {1} test examples".format(n_correct, len(y_test)))

#TEST
#print(extract_entities('friends called Mary who have worked at Google since 2010'))
#print(extract_entities('people who graduated from MIT in 1999'))


#assign_colors(doc)




