import pandas as pd
import spacy
nlp = spacy.load("en_core_web_sm")
from ecg_interpreter import Action

def parse_action(name, s):
    doc = nlp(s)

    for token in doc:
        if token.text == name:
            node = token

            # handle coordination (X and Y)
            if node.dep_ == "conj":
                node = node.head

            # climb dependency tree
            while node.dep_ not in ("nsubj", "nsubjpass", "dobj", "obj", "ROOT"):
                if node.head == node:
                    break
                node = node.head

            # SUBJECT CASE
            if node.dep_ in ("nsubj", "nsubjpass"):
                verb = node.head
                return {
                    "subj": name,
                    "verb": verb.text,
                    "obj": None
                }
            # OBJECT CASE
            if node.dep_ in ("dobj", "obj"):
                return {
                    "subj": None,
                    "verb": node.head.text,
                    "obj": name
                }
            # fallback if ROOT reached
            if node.dep_ == "ROOT":
                return {
                    "subj": name,
                    "verb": node.text,
                    "obj": None
                }
    return None

# main function - get the action within the given sentence associated with the given pid
# returns the action node
# CURRENTLY ASSUMES ARTICLE LOCATION IS THE LID - FUTURE ITERATIONS SHOULD CHECK SENT FOR MENTION OF ANOTHER PLACE
def get_person_action(sent, pid, ppl_df, lid):
    # format name, save lname and fname separately
    person = ppl_df.loc[pid]
    fname = (person["First Name"] if pd.notna(person["First Name"]) else "")
    afname = (person["Alt First Name"] if pd.notna(person["Alt First Name"]) else "")
    mname = (person["Middle Name"] if pd.notna(person["Middle Name"]) else "")
    lname = (person["Last Name"] if pd.notna(person["Last Name"]) else "")
    alname = (person["Alt Last Name"] if pd.notna(person["Alt Last Name"]) else "")
    
    # get action for each sentence, related to this person
    if lname in sent:
        result = parse_action(lname, sent)
    elif alname in sent:
        result = parse_action(alname, sent)
    elif fname in sent:
        result = parse_action(fname, sent)
    elif afname in sent:
        result = parse_action(afname, sent)
    else:
        result = parse_action(mname, sent)

    
    # format action dict (SWITCH TO NODE LATER)
    # error handling: cannot parse action - return action node with just sent, pid, and lid
    if result == None:
        action = Action()
        action.action = None
        action.details = sent
        action.personObjID = None
        action.personSubjID = pid
        action.placeID = lid
        # action = {"personSubjID": pid, "personObjID": None, "action": None, "details": sent, "placeID": lid}
    # OBJECT CASE
    elif result["subj"] == None:
        details_index = sent.find(result["verb"]) - 1
        action = Action()
        action.action = result["verb"]
        action.details = sent[:details_index].strip()
        action.personObjID = pid
        action.personSubjID = None
        action.placeID = lid
        # action = {"personSubjID": None, "personObjID": pid, "action": result["verb"], "details": sent[:details_index].strip(), "placeID": lid}
    # SUBJECT CASE
    else:
        details_index = sent.find(result["verb"]) + len(result["verb"])
        action = Action()
        action.action = result["verb"]
        action.details = sent[details_index:].strip()
        action.personObjID = None
        action.personSubjID = pid
        action.placeID = lid
        # action = {"personSubjID": pid, "personObjID": None, "action": result["verb"], "details": sent[details_index:].strip(), "placeID": lid}
    return action

