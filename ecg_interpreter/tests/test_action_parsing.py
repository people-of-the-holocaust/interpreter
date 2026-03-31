import pandas as pd

# import modules to test
from ecg_interpreter import get_person_action

# CREATE DUMMY PPL_DF FOR TESTS
# currently loading in people table from people_sort
dummy_ppl_df = pd.read_csv('dummy_people_table.csv')
dummy_ppl_df = dummy_ppl_df.drop('Unnamed: 0', axis=1)
dummy_ppl_df.index.name = "ID"

# Is a KEY sentence where the name is the subject accurately broken up into action parts (subject = name, verb = root verb associated with the clause that includes the name, obj = obj of sentence or NONE, details = rest of sentence)?
def test_action_subj1():
    # article
    pid = 1
    sentence = ""
    result = get_person_action(sentence, pid, dummy_ppl_df)
    # assert action node accuracy

def test_action_subj2():
    # article
    pid = 1
    sentence = ""
    result = get_person_action(sentence, pid, dummy_ppl_df)
    # assert action node accuracy

def test_action_subj3():
    # article
    pid = 1
    sentence = ""
    result = get_person_action(sentence, pid, dummy_ppl_df)
    # assert action node accuracy

# Is a KEY sentence where the name is the object accurately broken up into action parts (subject = NONE, verb = root verb associated with the clause that includes the name, obj = name, details = rest of sentence)?

def test_action_obj1():
    # article
    pid = 1
    sentence = ""
    result = get_person_action(sentence, pid, dummy_ppl_df)
    # assert action node accuracy

def test_action_obj2():
    # article
    pid = 1
    sentence = ""
    result = get_person_action(sentence, pid, dummy_ppl_df)
    # assert action node accuracy

def test_action_obj3():
    # article
    pid = 1
    sentence = ""
    result = get_person_action(sentence, pid, dummy_ppl_df)
    # assert action node accuracy
