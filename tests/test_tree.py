# ADD TO OTHER DATA STRUCTURE TESTS WHEN BRANCH IS MERGED IN

from ecg_interpreter.data_structure import Encyclopedia, Volume, Article, Sentence, Action
from ecg_interpreter import print_ecg

def test_empty_tree():
    ecg = Encyclopedia()
    expected = "ENCYCLOPEDIA OBJECT DOES NOT HAVE ANY VOLUMES"
    result = print_ecg(ecg)
    assert result == expected

def test_1ofEach_tree():
    ecg = Encyclopedia()
    v1 = Volume(1, "url1")
    a1 = Article("Test Article 1", "article 1 text test", 10)
    s1 = Sentence("sentence 1 text test", [0])
    act0 = Action(0, None, "did", "subject test", 200)

    s1.addAction(act0)
    a1.addSent(s1)
    v1.addArticle(a1)
    ecg.addVolume(v1)

    expected = "\n\n\nVOLUME " + str(v1.volumeNumber) + " : " + str(v1.volumeURL)
    expected += ("\n\nARTICLE: " + str(a1.title) + " : " + str(a1.documentNumber))
    expected += "\nSENTENCE:"
    expected += str(act0.personSubjID) + " " + str(act0.action) + " " + str(act0.details) + " in " + str(act0.placeID)

    result = print_ecg(ecg)
    assert result == expected

def test_2vols_tree():
    ecg = Encyclopedia()
    v1 = Volume(1, "url1")
    v2 = Volume(2, "url2")
    a1 = Article("Test Article 1", "article 1 text test", 10)
    a2 = Article("Test Article 2", "article 2 text test", 20)
    s1 = Sentence("sentence 1 text test", [0])
    s2 = Sentence("sentence 2 text test", [1])
    act0 = Action(0, None, "did", "subject test", 200)
    act1 = Action(None, 1, "did", "object test", 200)

    s1.addAction(act0)
    a1.addSent(s1)
    v1.addArticle(a1)
    ecg.addVolume(v1)

    s2.addAction(act1)
    a2.addSent(s2)
    v2.addArticle(a2)
    ecg.addVolume(v2)

    expected = "\n\n\nVOLUME " + str(v1.volumeNumber) + " : " + str(v1.volumeURL)
    expected += ("\n\nARTICLE: " + str(a1.title) + " : " + str(a1.documentNumber))
    expected += "\nSENTENCE:"
    expected += str(act0.personSubjID) + " " + str(act0.action) + " " + str(act0.details) + " in " + str(act0.placeID)
    expected += "\n\n\nVOLUME " + str(v2.volumeNumber) + " : " + str(v2.volumeURL)
    expected += ("\n\nARTICLE: " + str(a2.title) + " : " + str(a2.documentNumber))
    expected += "\nSENTENCE:"
    expected += (str(act1.details) + " " + str(act1.action) + " " + str(act1.personObjID) + " in " + str(act1.placeID))

    result = print_ecg(ecg)
    assert result == expected

def test_full_tree_addingAtEnd():
    ecg = Encyclopedia()
    v1 = Volume(1, "url1")
    v2 = Volume(2, "url2")
    a1 = Article("Test Article 1", "article 1 text test", 10)
    a2 = Article("Test Article 2", "article 2 text test", 20)
    a3 = Article("Test Article 3", "article 3 text test", 30)
    a4 = Article("Test Article 4", "article 4 text test", 40)
    a5 = Article("Test Article 5", "article 5 text test", 50)
    s1 = Sentence("sentence 1 text test", [0])
    s2 = Sentence("sentence 2 text test", [1, 2])
    s3 = Sentence("sentence 3 text test", [3])
    s4 = Sentence("sentence 4 text test", [4])
    s5 = Sentence("sentence 5 text test", [5])
    s6 = Sentence("sentence 6 text test", [6])
    s7 = Sentence("sentence 7 text test", [7, 8])
    s8 = Sentence("sentence 8 text test", [9])
    s9 = Sentence("sentence 9 text test", [3])
    s10 = Sentence("sentence 10 text test", [4, 6, 9])
    act0 = Action(0, None, "did", "subject test", 200)
    act1 = Action(None, 1, "did", "object test", 200)
    act2 = Action(2, None, None, "2 could not be parsed tests", 200)
    act3 = Action(3, None, "did", "subject test", 200)
    act4 = Action(None, 4, "did", "object test", 200)
    act5 = Action(5, None, None, "5 could not be parsed tests", 200)
    act6 = Action(6, None, "did", "subject test", 200)
    act7 = Action(None, 7, "did", "object test", 200)
    act8 = Action(8, None, None, "8 could not be parsed tests", 200)
    act9 = Action(9, None, None, "9 could not be parsed tests", 200)


    s1.addAction(act0)
    a1.addSent(s1)
    s2.addAction(act1)
    s2.addAction(act2)
    a1.addSent(s2)
    v1.addArticle(a1)
    s3.addAction(act3)
    a2.addSent(s3)
    s4.addAction(act4)
    a2.addSent(s4)
    v1.addArticle(a2)
    s5.addAction(act5)
    a3.addSent(s5)
    s6.addAction(act6)
    a3.addSent(s6)
    v1.addArticle(a3)
    ecg.addVolume(v1)

    s7.addAction(act7)
    s7.addAction(act8)
    a4.addSent(s7)
    s8.addAction(act9)
    a4.addSent(s8)
    v2.addArticle(a4)
    s9.addAction(act3)
    a5.addSent(s9)
    s10.addAction(act4)
    s10.addAction(act6)
    s10.addAction(act9)
    a5.addSent(s10)
    v2.addArticle(a5)
    ecg.addVolume(v2)

    expected = "\n\n\nVOLUME " + str(v1.volumeNumber) + " : " + str(v1.volumeURL)

    expected += ("\n\nARTICLE: " + str(a1.title) + " : " + str(a1.documentNumber))
    expected += "\nSENTENCE:"
    expected += str(act0.personSubjID) + " " + str(act0.action) + " " + str(act0.details) + " in " + str(act0.placeID)
    expected += "\nSENTENCE:"
    expected += (str(act1.details) + " " + str(act1.action) + " " + str(act1.personObjID) + " in " + str(act1.placeID))
    expected += (str(act2.details) + "\nAction in above sentence could not be parsed during processing.")

    expected += ("\n\nARTICLE: " + str(a2.title) + " : " + str(a2.documentNumber))
    expected += "\nSENTENCE:"
    expected += str(act3.personSubjID) + " " + str(act3.action) + " " + str(act3.details) + " in " + str(act3.placeID)
    expected += "\nSENTENCE:"
    expected += (str(act4.details) + " " + str(act4.action) + " " + str(act4.personObjID) + " in " + str(act4.placeID))

    expected += ("\n\nARTICLE: " + str(a3.title) + " : " + str(a3.documentNumber))
    expected += "\nSENTENCE:"
    expected += (str(act5.details) + "\nAction in above sentence could not be parsed during processing.")
    expected += "\nSENTENCE:"
    expected += str(act6.personSubjID) + " " + str(act6.action) + " " + str(act6.details) + " in " + str(act6.placeID)

    expected += "\n\n\nVOLUME " + str(v2.volumeNumber) + " : " + str(v2.volumeURL)

    expected += ("\n\nARTICLE: " + str(a4.title) + " : " + str(a4.documentNumber))
    expected += "\nSENTENCE:"
    expected += (str(act7.details) + " " + str(act7.action) + " " + str(act7.personObjID) + " in " + str(act7.placeID))
    expected += (str(act8.details) + "\nAction in above sentence could not be parsed during processing.")
    expected += "\nSENTENCE:"
    expected += (str(act9.details) + "\nAction in above sentence could not be parsed during processing.")

    expected += ("\n\nARTICLE: " + str(a5.title) + " : " + str(a5.documentNumber))
    expected += "\nSENTENCE:"
    expected += str(act3.personSubjID) + " " + str(act3.action) + " " + str(act3.details) + " in " + str(act3.placeID)
    expected += "\nSENTENCE:"
    expected += (str(act4.details) + " " + str(act4.action) + " " + str(act4.personObjID) + " in " + str(act4.placeID))
    expected += str(act6.personSubjID) + " " + str(act6.action) + " " + str(act6.details) + " in " + str(act6.placeID)
    expected += (str(act9.details) + "\nAction in above sentence could not be parsed during processing.")


    result = print_ecg(ecg)
    assert result == expected

def test_full_tree_addingInOrder():
    ecg = Encyclopedia()
    v1 = Volume(1, "url1")
    ecg.addVolume(v1)
    v2 = Volume(2, "url2")
    ecg.addVolume(v2)
    a1 = Article("Test Article 1", "article 1 text test", 10)
    a2 = Article("Test Article 2", "article 2 text test", 20)
    a3 = Article("Test Article 3", "article 3 text test", 30)
    v1.addArticle(a1)
    v1.addArticle(a2)
    v1.addArticle(a3)
    a4 = Article("Test Article 4", "article 4 text test", 40)
    a5 = Article("Test Article 5", "article 5 text test", 50)
    v2.addArticle(a4)
    v2.addArticle(a5)
    s1 = Sentence("sentence 1 text test", [0])
    s2 = Sentence("sentence 2 text test", [1, 2])
    a1.addSent(s1)
    a1.addSent(s2)
    s3 = Sentence("sentence 3 text test", [3])
    s4 = Sentence("sentence 4 text test", [4])
    a2.addSent(s3)
    a2.addSent(s4)
    s5 = Sentence("sentence 5 text test", [5])
    s6 = Sentence("sentence 6 text test", [6])
    a3.addSent(s5)
    a3.addSent(s6)
    s7 = Sentence("sentence 7 text test", [7, 8])
    s8 = Sentence("sentence 8 text test", [9])
    a4.addSent(s7)
    a4.addSent(s8)
    s9 = Sentence("sentence 9 text test", [3])
    s10 = Sentence("sentence 10 text test", [4, 6, 9])
    a5.addSent(s9)
    a5.addSent(s10)
    act0 = Action(0, None, "did", "subject test", 200)
    act1 = Action(None, 1, "did", "object test", 200)
    act2 = Action(2, None, None, "2 could not be parsed tests", 200)
    act3 = Action(3, None, "did", "subject test", 200)
    act4 = Action(None, 4, "did", "object test", 200)
    act5 = Action(5, None, None, "5 could not be parsed tests", 200)
    act6 = Action(6, None, "did", "subject test", 200)
    act7 = Action(None, 7, "did", "object test", 200)
    act8 = Action(8, None, None, "8 could not be parsed tests", 200)
    act9 = Action(9, None, None, "9 could not be parsed tests", 200)

    s1.addAction(act0)
    s2.addAction(act1)
    s2.addAction(act2)
    s3.addAction(act3)
    s4.addAction(act4)
    s5.addAction(act5)
    s6.addAction(act6)

    s7.addAction(act7)
    s7.addAction(act8)
    s8.addAction(act9)
    s9.addAction(act3)
    s10.addAction(act4)
    s10.addAction(act6)
    s10.addAction(act9)

    expected = "\n\n\nVOLUME " + str(v1.volumeNumber) + " : " + str(v1.volumeURL)

    expected += ("\n\nARTICLE: " + str(a1.title) + " : " + str(a1.documentNumber))
    expected += "\nSENTENCE:"
    expected += str(act0.personSubjID) + " " + str(act0.action) + " " + str(act0.details) + " in " + str(act0.placeID)
    expected += "\nSENTENCE:"
    expected += (str(act1.details) + " " + str(act1.action) + " " + str(act1.personObjID) + " in " + str(act1.placeID))
    expected += (str(act2.details) + "\nAction in above sentence could not be parsed during processing.")

    expected += ("\n\nARTICLE: " + str(a2.title) + " : " + str(a2.documentNumber))
    expected += "\nSENTENCE:"
    expected += str(act3.personSubjID) + " " + str(act3.action) + " " + str(act3.details) + " in " + str(act3.placeID)
    expected += "\nSENTENCE:"
    expected += (str(act4.details) + " " + str(act4.action) + " " + str(act4.personObjID) + " in " + str(act4.placeID))

    expected += ("\n\nARTICLE: " + str(a3.title) + " : " + str(a3.documentNumber))
    expected += "\nSENTENCE:"
    expected += (str(act5.details) + "\nAction in above sentence could not be parsed during processing.")
    expected += "\nSENTENCE:"
    expected += str(act6.personSubjID) + " " + str(act6.action) + " " + str(act6.details) + " in " + str(act6.placeID)

    expected += "\n\n\nVOLUME " + str(v2.volumeNumber) + " : " + str(v2.volumeURL)

    expected += ("\n\nARTICLE: " + str(a4.title) + " : " + str(a4.documentNumber))
    expected += "\nSENTENCE:"
    expected += (str(act7.details) + " " + str(act7.action) + " " + str(act7.personObjID) + " in " + str(act7.placeID))
    expected += (str(act8.details) + "\nAction in above sentence could not be parsed during processing.")
    expected += "\nSENTENCE:"
    expected += (str(act9.details) + "\nAction in above sentence could not be parsed during processing.")

    expected += ("\n\nARTICLE: " + str(a5.title) + " : " + str(a5.documentNumber))
    expected += "\nSENTENCE:"
    expected += str(act3.personSubjID) + " " + str(act3.action) + " " + str(act3.details) + " in " + str(act3.placeID)
    expected += "\nSENTENCE:"
    expected += (str(act4.details) + " " + str(act4.action) + " " + str(act4.personObjID) + " in " + str(act4.placeID))
    expected += str(act6.personSubjID) + " " + str(act6.action) + " " + str(act6.details) + " in " + str(act6.placeID)
    expected += (str(act9.details) + "\nAction in above sentence could not be parsed during processing.")


    result = print_ecg(ecg)
    assert result == expected