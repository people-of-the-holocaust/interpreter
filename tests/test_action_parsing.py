# import modules to test
from ecg_interpreter import get_person_action
from ecg_interpreter.data_structure import Action

# expected output from get_person_action:
# {"personSubjID", "personObjID", "action", "details", "placeID"}

# ALL TESTS WILL FAIL RIGHT NOW BECAUSE get_person_action DOES NOT RETURN THIS FORMAT

# Is a KEY sentence where the name is the subject accurately broken up into action parts (subject = name, verb = root verb associated with the clause that includes the name, obj = obj of sentence or NONE, details = rest of sentence)?
def test_action_subj1(dummy_ppl_df):
    # article KOPRIVNICA - lid 2533
    # Martin Nemec - pid 10335
    pid = 10335
    lid = 2533
    sentence = "After the end of World War II, the first commandant, Martin Nemec, was condemned to death and hanged in Danica."
    expected = Action(pid, None, "condemned", "to death and hanged in Danica.", lid)
    # expected = {"personSubjID": pid, "personObjID": None, "action": "condemned", "details": "to death and hanged in Danica.", "placeID": lid}
    result = get_person_action(sentence, pid, dummy_ppl_df, lid)
    assert vars(result) == vars(expected)

def test_action_subj2(dummy_ppl_df):
    # article KORCZYNA - lid 1479
    # Aron Neubarth - pid 10350
    pid = 10350
    lid = 1479
    sentence = "Survivor Aron Neubarth, who moved to the ghetto when rural Jews were brought in (in June 1942), testified that Korczyna‚Äôs Jews were allowed to leave the ghetto only for organized labor assignments."
    expected = Action(pid, None, "testified", "that Korczyna‚Äôs Jews were allowed to leave the ghetto only for organized labor assignments.", lid)
    # expected = {"personSubjID": pid, "personObjID": None, "action": "testified", "details": "that Korczyna‚Äôs Jews were allowed to leave the ghetto only for organized labor assignments.", "placeID": lid}
    result = get_person_action(sentence, pid, dummy_ppl_df, lid)
    assert vars(result) == vars(expected)

def test_action_subj3(dummy_ppl_df):
    # article PAKRUOJIS - lid 1741
    # Moshe Plocki - pid 11224
    pid = 11224
    lid = 1741
    sentence = "Some of those arrested, including Moshe Plocki and Chaja Edelman, were murdered, and about 30 others were transferred, in early July, to the prison in ≈†iauliai."
    expected = Action(pid, None, "murdered", ", and about 30 others were transferred, in early July, to the prison in ≈†iauliai.", lid)
    # expected = {"personSubjID": 11224, "personObjID": None, "action": "murdered", "details": ", and about 30 others were transferred, in early July, to the prison in ≈†iauliai.", "placeID": lid}
    result = get_person_action(sentence, pid, dummy_ppl_df, lid)
    assert vars(result) == vars(expected)

# Is a KEY sentence where the name is the object accurately broken up into action parts (subject = NONE, verb = root verb associated with the clause that includes the name, obj = name, details = rest of sentence)?

def test_action_obj1(dummy_ppl_df):
    # article ZSCHORLAU - lid 811
    # Erich Pilz - pid 11145
    pid = 11145
    lid = 811
    sentence = "Zschorlau’s harsh conditions and rough interrogations caused the deaths of Otto Hempel, Paul Höhl, Albert Höhnel, Erich Pilz, and Alfred Schädlich."
    expected = Action(None, pid, "caused", "Zschorlau’s harsh conditions and rough interrogations", lid)
    # expected = {"personSubjID": None, "personObjID": pid, "action": "caused", "details": "Zschorlau’s harsh conditions and rough interrogations", "placeID": lid}
    result = get_person_action(sentence, pid, dummy_ppl_df, lid)
    assert vars(result) == vars(expected)

def test_action_obj2(dummy_ppl_df):
    # article GRÜNBERG I - lid 254
    # Anna Viebig - pid 15363
    pid = 15363
    lid = 254
    sentence = "The staff mentioned by former prisoners included Anna Viebig, Waltrand Schirmre, Hildegard Kuehn, Helga Siebert, and Anna Hempel."
    expected = Action(None, pid, "included", "The staff mentioned by former prisoners", lid)
    # expected = {"personSubjID": None, "personObjID": pid, "action": "included", "details": "The staff mentioned by former prisoners", "placeID": lid}
    result = get_person_action(sentence, pid, dummy_ppl_df, lid)
    assert vars(result) == vars(expected)

def test_action_obj3(dummy_ppl_df):
    # article HERMANOWICZE - lid 1335
    # Boris Sosnovik - pid 13949
    pid = 13949
    lid = 1335
    sentence = "On November 17, 1942, a punitive unit from Szarkowszczyzna shot Boris Sosnovik while trying to escape, but Iosif Sosnovik was able to flee; he was subsequently sheltered by the Arliukevich family in Podorszczyna."
    expected = Action(None, pid, "shot", "On November 17, 1942, a punitive unit from Szarkowszczyzna", lid)
    # expected = {"personSubjID": None, "personObjID": pid, "action": "shot", "details": "On November 17, 1942, a punitive unit from Szarkowszczyzna", "placeID": lid}
    result = get_person_action(sentence, pid, dummy_ppl_df, lid)
    assert vars(result) == vars(expected)
