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
def test_is_key_multiple_names1(dummy_ppl_df):
    # Marie Berthier - pid 1008
    # Otto Bleymehl - pid 1207
    pids = [1008, 1207]
    sentence = "This is a sentence about two people, Marie Berthier and Otto Bleymehl."
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids

def test_is_key_multiple_names2(dummy_ppl_df):
    # Eugen Witt - pid 16134
    # Antanas Paškauskas - pid 10909
    # Yitzhak Aaron - pid 1
    pids = [16134, 10909, 1]
    sentence = "Eugen Witt, Antanas Paškauskas, and Yitzhak Aaron are in this sentence."
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids

def test_is_key_multiple_names3(dummy_ppl_df):
    # Alfred Braun - pid 1571
    # Friedrich Übelhör - pid 16763
    # Gerard Libot - pid 8693
    pids = [1571, 16763, 8693]
    sentence = "Person number 1 is Alfred Braun, person number 2 is Friedrich Übelhör, and person number 3 is Gerard Libot."
    result = is_key(sentence, dummy_ppl_df)
    assert result == pids

# Is a sentence that includes a person's name (that is NOT in the people_table) NOT categorized as KEY?
def test_is_not_key_incorrect_name(dummy_ppl_df):
    sentence = "This is a sentence about a fake person, Billy Bob Jean."
    result = is_key(sentence, dummy_ppl_df)
    assert not result, "The pid list should be empty"

# Is a sentence that does not include a person's name NOT categorized as KEY?
def test_is_not_key_no_name1(dummy_ppl_df):
    # article 4278
    sentence = "The camp's German military personnel included about 20 people."
    result = is_key(sentence, dummy_ppl_df)
    assert not result, "The pid list should be empty"

def test_is_not_key_no_name2(dummy_ppl_df):
    # article 3655
    sentence = "Between 1940 and 1946, 450 Roma were imprisoned at Les Alliers, the number not exceeding 350 at any time."
    result = is_key(sentence, dummy_ppl_df)
    assert not result, "The pid list should be empty"

def test_is_not_key_no_name3(dummy_ppl_df):
    # article 1511
    sentence = "From the age and social structure of the women, one can conclude that those brought to this camp were the “last reserves” of female prisoners who could work: there were many older women and women with a long history in camps."
    result = is_key(sentence, dummy_ppl_df)
    assert not result, "The pid list should be empty"
