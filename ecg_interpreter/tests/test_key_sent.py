import pandas as pd

# import modules to test
from ecg_interpreter import is_key

# CREATE DUMMY PPL_DF FOR TESTS
# currently loading in people table from people_sort
dummy_ppl_df = pd.read_csv('dummy_people_table.csv')
dummy_ppl_df = dummy_ppl_df.drop('Unnamed: 0', axis=1)
dummy_ppl_df.index.name = "ID"

# Is a sentence that includes one person's name (that is in the people_table) categorized as KEY?
def test_is_key_fl1():
    # article 2376
    # Samek Szatan - pid 14470
    pids = [14470]
    sentence = "The Judenrat, with Dr. Bromberger as chairman and Samek Szatan as vice-chairman, and the Jewish police force were formed in mid-December 1939."
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids
def test_is_key_fl2():
    # article 4394
    # Ernst Meley - pid 9606
    pids = [9606]
    sentence = "From April 1941 to March 1944, the camp commandant was Oberstleutnant Ernst Meley."
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids

def test_is_key_fml1():
    # name - pid  
    pids = []
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids
def test_is_key_fml2():
    # article 
    # name - pid 
    pids = []
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids

def test_is_key_fmal1():
    # article 
    # name - pid 
    pids = []
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids
def test_is_key_fmal2():
    # article 
    # name - pid 
    pids = []
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids

def test_is_key_fal1():
    # article 
    # name - pid 
    pids = []
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids
def test_is_key_fal2():
    # article 
    # name - pid 
    pids = []
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids

def test_is_key_afmal1():
    # article 
    # name - pid 
    pids = []
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids
def test_is_key_afmal2():
    # article 
    # name - pid 
    pids = []
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids

def test_is_key_afal1():
    # article 
    # name - pid 
    pids = []
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids
def test_is_key_afal2():
    # article 
    # name - pid 
    pids = []
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids

def test_is_key_afml1():
    # article 
    # name - pid 
    pids = []
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids
def test_is_key_afml2():
    # article 
    # name - pid 
    pids = []
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids

def test_is_key_afl1():
    # Maurice (Moritz) Feiner - pid 3463 
    pids = [3463]
    sentence = "This is a test sentence for Moritz Feiner who has an alt first name."
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids
def test_is_key_afl2():
    # article 
    # name - pid 
    pids = []
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids

# Is a sentence that includes more than one person's name (that is in the people_table) categorized as KEY with all of the pids returned correctly?
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
    # article 4278
    sentence = "The camp's German military personnel included about 20 people."
    result = is_key(sentence, dummy_ppl_df)
    assert not result, "The pid list should be empty"

def test_is_not_key_no_name2():
    # article
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    assert not result, "The pid list should be empty"

def test_is_not_key_no_name3():
    # article
    sentence = ""
    result = is_key(sentence, dummy_ppl_df)
    assert not result, "The pid list should be empty"
