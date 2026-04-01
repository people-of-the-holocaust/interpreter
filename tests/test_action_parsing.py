import pandas as pd

# import modules to test
from ecg_interpreter import get_person_action

# Is a KEY sentence where the name is the subject accurately broken up into action parts (subject = name, verb = root verb associated with the clause that includes the name, obj = obj of sentence or NONE, details = rest of sentence)?
def test_action_subj1(dummy_ppl_df):
    # article
    pid = 1
    sentence = ""
    result = get_person_action(sentence, pid, dummy_ppl_df)
    # assert action node accuracy

def test_action_subj2(dummy_ppl_df):
    # article
    pid = 1
    sentence = ""
    result = get_person_action(sentence, pid, dummy_ppl_df)
    # assert action node accuracy

def test_action_subj3(dummy_ppl_df):
    # article
    pid = 1
    sentence = ""
    result = get_person_action(sentence, pid, dummy_ppl_df)
    # assert action node accuracy

# Is a KEY sentence where the name is the object accurately broken up into action parts (subject = NONE, verb = root verb associated with the clause that includes the name, obj = name, details = rest of sentence)?

def test_action_obj1(dummy_ppl_df):
    # article
    pid = 1
    sentence = ""
    result = get_person_action(sentence, pid, dummy_ppl_df)
    # assert action node accuracy

def test_action_obj2(dummy_ppl_df):
    # article
    pid = 1
    sentence = ""
    result = get_person_action(sentence, pid, dummy_ppl_df)
    # assert action node accuracy

def test_action_obj3(dummy_ppl_df):
    # article
    pid = 1
    sentence = ""
    result = get_person_action(sentence, pid, dummy_ppl_df)
    # assert action node accuracy
