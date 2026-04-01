# import modules to test
from ecg_interpreter import get_person_action

# expected output from get_person_action:
# {"personSubjID", "personObjID", "action", "details", "placeID"}

# Is a KEY sentence where the name is the subject accurately broken up into action parts (subject = name, verb = root verb associated with the clause that includes the name, obj = obj of sentence or NONE, details = rest of sentence)?
def test_action_subj1(dummy_ppl_df):
    # article KOPRIVNICA
    # Martin Nemec - pid 10335
    pid = 10335
    sentence = "After the end of World War II, the first commandant, Martin Nemec, was condemned to death and hanged in Danica."
    expected = {"personSubjID": 10335, "personObjID": None, "action": "condemned", "details": "", "placeID": 1}
    result = get_person_action(sentence, pid, dummy_ppl_df)
    assert result == expected

def test_action_subj2(dummy_ppl_df):
    # article KORCZYNA
    # Aron Neubarth - pid 10350
    pid = 10350
    sentence = "Survivor Aron Neubarth, who moved to the ghetto when rural Jews were brought in (in June 1942), testified that Korczyna‚Äôs Jews were allowed to leave the ghetto only for organized labor assignments."
    expected = {"personSubjID": 10350, "personObjID": None, "action": "testified", "details": "", "placeID": 1}
    result = get_person_action(sentence, pid, dummy_ppl_df)
    assert result == expected

def test_action_subj3(dummy_ppl_df):
    # article PAKRUOJIS
    # Moshe Plocki - pid 11224
    pid = 11224
    sentence = "Some of those arrested, including Moshe Plocki and Chaja Edelman, were murdered, and about 30 others were transferred, in early July, to the prison in ≈†iauliai."
    expected = {"personSubjID": 11224, "personObjID": None, "action": "murdered", "details": "", "placeID": 1}
    result = get_person_action(sentence, pid, dummy_ppl_df)
    assert result == expected

# Is a KEY sentence where the name is the object accurately broken up into action parts (subject = NONE, verb = root verb associated with the clause that includes the name, obj = name, details = rest of sentence)?

def test_action_obj1(dummy_ppl_df):
    # article ZSCHORLAU
    # Erich Pilz - pid 11145
    pid = 11145
    sentence = "Zschorlau’s harsh conditions and rough interrogations caused the deaths of Otto Hempel, Paul Höhl, Albert Höhnel, Erich Pilz, and Alfred Schädlich."
    expected = {"personSubjID": None, "personObjID": 11145, "action": "caused", "details": "", "placeID": 1}
    result = get_person_action(sentence, pid, dummy_ppl_df)
    assert result == expected

def test_action_obj2(dummy_ppl_df):
    # article GRÜNBERG I
    # Anna Viebig - pid 15363
    pid = 15363
    sentence = "The staff mentioned by former prisoners included Anna Viebig, Waltrand Schirmre, Hildegard Kuehn, Helga Siebert, and Anna Hempel."
    expected = {"personSubjID": None, "personObjID": 15363, "action": "mentioned", "details": "", "placeID": 1}
    result = get_person_action(sentence, pid, dummy_ppl_df)
    assert result == expected

def test_action_obj3(dummy_ppl_df):
    # article HERMANOWICZE
    # Boris Sosnovik - pid 13949
    pid = 13949
    sentence = "On November 17, 1942, a punitive unit from Szarkowszczyzna shot Boris Sosnovik while trying to escape, but Iosif Sosnovik was able to flee; he was subsequently sheltered by the Arliukevich family in Podorszczyna."
    expected = {"personSubjID": None, "personObjID": 13949, "action": "shot", "details": "", "placeID": 1}
    result = get_person_action(sentence, pid, dummy_ppl_df)
    assert result == expected
