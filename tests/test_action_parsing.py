# import modules to test
from ecg_interpreter import get_person_action

# expected output from get_person_action:
# {"personSubjID", "personObjID", "action", "details", "placeID"}

# Is a KEY sentence where the name is the subject accurately broken up into action parts (subject = name, verb = root verb associated with the clause that includes the name, obj = obj of sentence or NONE, details = rest of sentence)?
def test_action_subj1(dummy_ppl_df):
    # article KOPRIVNICA
    # Martin Nemec - pid 
    pid = 1
    sentence = "After the end of World War II, the first commandant, Martin Nemec, was condemned to death and hanged in Danica."
    expected = {"personSubjID": 1, "personObjID": 1, "action": "", "details": "", "placeID": 1}
    result = get_person_action(sentence, pid, dummy_ppl_df)
    assert result == expected

def test_action_subj2(dummy_ppl_df):
    # article KORCZYNA
    # Aron Neubarth - pid 
    pid = 1
    sentence = "Survivor Aron Neubarth, who moved to the ghetto when rural Jews were brought in (in June 1942), testified that Korczyna‚Äôs Jews were allowed to leave the ghetto only for organized labor assignments."
    expected = {"personSubjID": 1, "personObjID": 1, "action": "", "details": "", "placeID": 1}
    result = get_person_action(sentence, pid, dummy_ppl_df)
    assert result == expected

def test_action_subj3(dummy_ppl_df):
    # article PAKRUOJIS
    # Moshe Plocki - pid 
    pid = 1
    sentence = "Some of those arrested, including Moshe Plocki and Chaja Edelman, were murdered, and about 30 others were transferred, in early July, to the prison in ≈†iauliai."
    expected = {"personSubjID": 1, "personObjID": 1, "action": "", "details": "", "placeID": 1}
    result = get_person_action(sentence, pid, dummy_ppl_df)
    assert result == expected

# Is a KEY sentence where the name is the object accurately broken up into action parts (subject = NONE, verb = root verb associated with the clause that includes the name, obj = name, details = rest of sentence)?

def test_action_obj1(dummy_ppl_df):
    # article ZSCHORLAU
    # Erich Pilz - pid 
    pid = 1
    sentence = "Zschorlau’s harsh conditions and rough interrogations caused the deaths of Otto Hempel, Paul Höhl, Albert Höhnel, Erich Pilz, and Alfred Schädlich."
    expected = {"personSubjID": 1, "personObjID": 1, "action": "", "details": "", "placeID": 1}
    result = get_person_action(sentence, pid, dummy_ppl_df)
    assert result == expected

def test_action_obj2(dummy_ppl_df):
    # article
    # Anna Viebig - pid 
    pid = 1
    sentence = "The staff mentioned by former prisoners included Anna Viebig, Waltrand Schirmre, Hildegard Kuehn, Helga Siebert, and Anna Hempel."
    expected = {"personSubjID": 1, "personObjID": 1, "action": "", "details": "", "placeID": 1}
    result = get_person_action(sentence, pid, dummy_ppl_df)
    assert result == expected

def test_action_obj3(dummy_ppl_df):
    # article
    # Boris Sosnovik - pid
    pid = 1
    sentence = "On November 17, 1942, a punitive unit from Szarkowszczyzna shot Boris Sosnovik while trying to escape, but Iosif Sosnovik was able to flee; he was subsequently sheltered by the Arliukevich family in Podorszczyna."
    expected = {"personSubjID": 1, "personObjID": 1, "action": "", "details": "", "placeID": 1}
    result = get_person_action(sentence, pid, dummy_ppl_df)
    assert result == expected
