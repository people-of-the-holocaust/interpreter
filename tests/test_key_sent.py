# import modules to test
from ecg_interpreter import is_key

# Is a sentence that includes one person's name (that is in the people_table) categorized as KEY?
def test_is_key_fl1(dummy_ppl_df):
    # article 2376
    # Samek Szatan - pid 14470
    pids = [14470]
    sentence = "The Judenrat, with Dr. Bromberger as chairman and Samek Szatan as vice-chairman, and the Jewish police force were formed in mid-December 1939."
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids
def test_is_key_fl2(dummy_ppl_df):
    # article 4394
    # Ernst Meley - pid 9606
    pids = [9606]
    sentence = "From April 1941 to March 1944, the camp commandant was Oberstleutnant Ernst Meley."
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids

def test_is_key_fml1(dummy_ppl_df):
    # Johanna Edith Anders - pid 253
    pids = [253]
    sentence = "Johanna Edith Anders is a person in the ECG."
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids
def test_is_key_fml2(dummy_ppl_df):
    # D. S. Blen - pid 1205
    pids = [1205]
    sentence = "This is a sentence about D. S. Blen."
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids

def test_is_key_fmal(dummy_ppl_df):
    # Kurt von Österreich (Oesterreich) - pid 16761
    pids = [16761]
    sentence = "This is a sentence about Kurt von Oesterreich"
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids

def test_is_key_fal1(dummy_ppl_df):
    # Maria Hradec (Kraus) - pid 6006
    pids = [6006]
    sentence = "This is a test sentence about Maria Kraus who has an alt last name."
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids
def test_is_key_fal2(dummy_ppl_df):
    # Madeleine	Steinberg (White) - pid 14147
    pids = [14147]
    sentence = "Madeleine White has another last name."
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids

# def test_is_key_afmal():
#     # test person - not part of actual dataset 
#     # name - pid 
#     pids = []
#     sentence = ""
#     result = is_key(sentence, dummy_ppl_df)
#     assert result == pids

# def test_is_key_afal():
#     # test person - not part of actual dataset 
#     # name - pid 
#     pids = []
#     sentence = ""
#     result = is_key(sentence, dummy_ppl_df)
#     assert result == pids

def test_is_key_afml(dummy_ppl_df):
    # article 
    # Kurt (Schmidt) Friedrich Plötner - pid 11243
    pids = [11243]
    sentence = "Schmidt Friedrich Plötner is a person in the ECG."
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids

def test_is_key_afl1(dummy_ppl_df):
    # Maurice (Moritz) Feiner - pid 3463 
    pids = [3463]
    sentence = "This is a test sentence for Moritz Feiner who has an alt first name."
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids
def test_is_key_afl2(dummy_ppl_df):
    # Otto (Tull) Harder - pid 5422
    pids = [5422]
    sentence = "Tull Harder is a person with an alt first name."
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids

# Is a sentence that includes more than one person's name (that is in the people_table) categorized as KEY with all of the pids returned correctly?
# def test_is_key_multiple_names1():
#     sentence = ""
#     result = is_key(sentence, dummy_ppl_df)
#     # assert result == list of pids

# def test_is_key_multiple_names2():
#     sentence = ""
#     result = is_key(sentence, dummy_ppl_df)
#     # assert result == list of pids

# def test_is_key_multiple_names3():
#     sentence = ""
#     result = is_key(sentence, dummy_ppl_df)
#     # assert result == list of pids

# Is a sentence that includes a person's name (that is NOT in the people_table) NOT categorized as KEY?
# def test_is_not_key_incorrect_name1():
#     sentence = ""
#     result = is_key(sentence, dummy_ppl_df)
#     assert not result, "The pid list should be empty"

# def test_is_not_key_incorrect_name2():
#     sentence = ""
#     result = is_key(sentence, dummy_ppl_df)
#     assert not result, "The pid list should be empty"

# def test_is_not_key_incorrect_name3():
#     sentence = ""
#     result = is_key(sentence, dummy_ppl_df)
#     assert not result, "The pid list should be empty"

# Is a sentence that does not include a person's name NOT categorized as KEY?
# def test_is_not_key_no_name1():
#     # article 4278
#     sentence = "The camp's German military personnel included about 20 people."
#     result = is_key(sentence, dummy_ppl_df)
#     assert not result, "The pid list should be empty"

# def test_is_not_key_no_name2():
#     # article
#     sentence = ""
#     result = is_key(sentence, dummy_ppl_df)
#     assert not result, "The pid list should be empty"

# def test_is_not_key_no_name3():
#     # article
#     sentence = ""
#     result = is_key(sentence, dummy_ppl_df)
#     assert not result, "The pid list should be empty"
