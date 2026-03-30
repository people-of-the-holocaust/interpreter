import pandas as pd

# import modules to test
from ecg_interpreter import is_key
from ecg_interpreter import get_person_action

# CREATE DUMMY PPL_DF FOR TESTS
# load in people table from people_sort
dummy_ppl_df = pd.read_csv('./../tables/people_table.csv')
dummy_ppl_df = dummy_ppl_df.drop('Unnamed: 0', axis=1)
dummy_ppl_df.index.name = "ID"

# Is a sentence that includes 1+ person's name (that is in the people_table) categorized as KEY?
def test_is_key_correct_name1():
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    # assert result == pid

def test_is_key_correct_name2():
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    # assert result == pid

def test_is_key_correct_name3():
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    # assert result == pid

def test_is_key_multiple_names1():
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    # assert result == list of pids

def test_is_key_multiple_names2():
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    # assert result == list of pids

def test_is_key_multiple_names3():
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    # assert result == list of pids

# Is a sentence that includes a person's name (that is NOT in the people_table) NOT categorized as KEY?
def test_is_not_key_incorrect_name1():
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    assert not result, "The pid list should be empty"

def test_is_not_key_incorrect_name2():
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    assert not result, "The pid list should be empty"

def test_is_not_key_incorrect_name3():
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    assert not result, "The pid list should be empty"

# Is a sentence that does not include a person's name NOT categorized as KEY?
def test_is_not_key_no_name1():
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    assert not result, "The pid list should be empty"

def test_is_not_key_no_name2():
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    assert not result, "The pid list should be empty"

def test_is_not_key_no_name3():
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    assert not result, "The pid list should be empty"

# Is a KEY sentence where the name is the subject accurately broken up into action parts (subject = name, verb = root verb associated with the clause that includes the name, obj = obj of sentence or NONE, details = rest of sentence)?
def test_action_subj1():
    pid = 1
    sentence = ""
    result = get_person_action(sentence, pid, dummy_ppl_df)
    # assert action node accuracy

def test_action_subj2():
    pid = 1
    sentence = ""
    result = get_person_action(sentence, pid, dummy_ppl_df)
    # assert action node accuracy

def test_action_subj3():
    pid = 1
    sentence = ""
    result = get_person_action(sentence, pid, dummy_ppl_df)
    # assert action node accuracy

# Is a KEY sentence where the name is the object accurately broken up into action parts (subject = NONE, verb = root verb associated with the clause that includes the name, obj = name, details = rest of sentence)?

def test_action_obj1():
    pid = 1
    sentence = ""
    result = get_person_action(sentence, pid, dummy_ppl_df)
    # assert action node accuracy

def test_action_obj2():
    pid = 1
    sentence = ""
    result = get_person_action(sentence, pid, dummy_ppl_df)
    # assert action node accuracy

def test_action_obj3():
    pid = 1
    sentence = ""
    result = get_person_action(sentence, pid, dummy_ppl_df)
    # assert action node accuracy
