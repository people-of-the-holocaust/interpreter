import pandas as pd
import spacy
nlp = spacy.load("en_core_web_sm")

def parse_action(name, s):
    print(s)
    # tokenize s using spacy
    token_s = nlp(s)
    # get root verb
    for token in token_s:
        if token.text == name:
            # print(token.text, token.dep_, token.head.text)
            subject = token
                
            # handle apposition cases (where name is appos, not nsubj)
            if token.dep_ == "appos":
                subject = token.head
            
            # subject case
            if subject.dep_ in ("nsubj", "nsubjpass"):
                verb = subject.head
                obj = None
                for child in verb.children:
                    if child.dep_ in ("dobj", "obj", "attr", "pobj"):
                        obj = child
                # print("SUBJECT:", name, "- VERB:", verb.text, "OBJECT:", obj.text if obj else None)
                action = {"subj": name, "verb": verb.text, "obj": obj.text if obj else None}
                return action
            # object case
            if token.dep_ in ("dobj", "obj", "pobj"):
                # print("OBJECT:", name, "- VERB:", token.head.text)
                action = {"subj": None, "verb": token.head.text, "obj": name}
                return action

# main function - get the action within the given sentence associated with the given pid
# returns the action node
def get_person_action(sent, pid, ppl_df):
    # format name, save lname and fname separately
    person = ppl_df.iloc[pid]
    fname = (person["First Name"] if pd.notna(person["First Name"]) else "")
    # name = fname + ((" (" + person["Alt First Name"] + ")") if pd.notna(person["Alt First Name"]) else "")
    # name += ((" " + person["Middle Name"] + " ") if pd.notna(person["Middle Name"]) else " ")
    lname = (person["Last Name"] if pd.notna(person["Last Name"]) else "")
    # name += lname + ((" (" + person["Alt Last Name"] + ") ") if pd.notna(person["Alt Last Name"]) else "")
    
    # get action for each sentence, related to this person
    # parse_action currently NOT RETURNING ANYTHING - need to actually create node
    if lname in sent:
        action = parse_action(lname, sent)
    else:
        action = parse_action(fname, sent)
    return action

