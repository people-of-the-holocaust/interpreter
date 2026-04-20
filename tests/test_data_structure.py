from ecg_interpreter import Encyclopedia, Volume, Article, Sentence, Action

#Testing data structure

#One of each node, Encyclopedia->Volume->Article->Sentence->Action, all empty
def test_one_of_each_node():
    actNode = Action(0, None, "verb", "details", 1)
    sentNode = Sentence("text", [0])
    artiNode = Article("title", "text", 5)
    volNode = Volume(1, "url")
    encycNode = Encyclopedia()

    encycNode.addVolume(volNode)
    volNode.addArticle(artiNode)
    artiNode.addSent(sentNode)
    sentNode.addAction(actNode)

    #Assertions that check if made properly.
    assert len(encycNode.volumesList) == 1
    assert len(encycNode.volumesList[0].articlesList) == 1
    assert len(encycNode.volumesList[0].articlesList[0].sentsList) == 1
    assert len(encycNode.volumesList[0].articlesList[0].sentsList[0].actionsList) == 1

#Testing four Volumes with one of Article, Sentence, and Action.
def test_three_nodes_in_encyclopedia():
    encyNode = Encyclopedia()
    for i in range(4):
        volumeNode = Volume(i, "url")
        encyNode.addVolume(volumeNode)

        artiNode = Article("title", "text", 5)
        encyNode.volumesList[i].addArticle(artiNode)

        sentNode = Sentence("text", [0])
        encyNode.volumesList[i].articlesList[0].addSent(sentNode)

        actNode = Action(0, None, "verb", "details", 1)
        encyNode.volumesList[i].articlesList[0].sentsList[0].addAction(actNode)

    #Assertation
    assert len(encyNode.volumesList) == 4
    for i in range(len(encyNode.volumesList)):
        assert len(encyNode.volumesList[i].articlesList) == 1
        assert len(encyNode.volumesList[i].articlesList[0].sentsList) == 1
        assert len(encyNode.volumesList[i].articlesList[0].sentsList[0].actionsList) == 1

#Test Encyclopedia gathering a combined list of three lesser Actions within the above.
def test_accessing_actions():
    encyNode = Encyclopedia()
    for i in range(4):
        volumeNode = Volume(i, "url")
        encyNode.addVolume(volumeNode)

        artiNode = Article("title", "text", 5)
        encyNode.volumesList[i].addArticle(artiNode)

        sentNode = Sentence("text", [0])
        encyNode.volumesList[i].articlesList[0].addSent(sentNode)
        for j in range(3):
            actNode = Action(0, None, "verb", "details", 1)
            encyNode.volumesList[i].articlesList[0].sentsList[0].addAction(actNode)
    
    actions = encyNode.getActions()
    #Expected to be of size of 12 with varying actions.
    assert len(actions) != 0
    assert len(actions) == 12
 
#Test for when there's no actions possible.
def test_no_actions():
    encyNode = Encyclopedia()
    for i in range(4):
        volumeNode = Volume(i, "url")
        encyNode.addVolume(volumeNode)

        artiNode = Article("title", "text", 5)
        encyNode.volumesList[i].addArticle(artiNode)

        sentNode = Sentence("text", [0])
        encyNode.volumesList[i].articlesList[0].addSent(sentNode)
    
    assert len(encyNode.getActions()) == 0

#Tests for sentences.
def test_grab_sentences():
    encyNode = Encyclopedia()
    for i in range(4):
        volumeNode = Volume(i, "url")
        encyNode.addVolume(volumeNode)

        artiNode = Article("title", "text", 5)
        encyNode.volumesList[i].addArticle(artiNode)

        sentNode = Sentence("text", [0])
        encyNode.volumesList[i].articlesList[0].addSent(sentNode)

        actNode = Action(0, None, "verb", "details", 1)
        encyNode.volumesList[i].articlesList[0].sentsList[0].addAction(actNode)

    #Assertation
    assert len(encyNode.volumesList) == 4
    for i in range(len(encyNode.volumesList)):
        assert len(encyNode.volumesList[i].articlesList) == 1
        assert len(encyNode.volumesList[i].articlesList[0].sentsList) == 1
        assert len(encyNode.volumesList[i].articlesList[0].sentsList[0].actionsList) == 1

#Test Encyclopedia gathering a combined list of three lesser Actions within the above.
# GET SENTENCES DOES NOT EXIST RIGHT NOW??? - saving test for future if needed
# def test_accessing_actions():
#     encyNode = Encyclopedia()
#     for i in range(4):
#         volumeNode = Volume(i, "url")
#         encyNode.addVolume(volumeNode)

#         artiNode = Article("title", "text", 5)
#         encyNode.volumesList[i].addArticle(artiNode)

#         sentNode = Sentence("text", [0])
#         encyNode.volumesList[i].articlesList[0].addSent(sentNode)
#         for j in range(3):
#             actNode = Action(0, None, "verb", "details", 1)
#             encyNode.volumesList[i].articlesList[0].sentsList[0].addAction(actNode)

#     assert len(encyNode.getSentences()) == 4


#Tests for when zero sentences.
# GET SENTENCES DOES NOT EXIST RIGHT NOW??? - saving test for future if needed
# def test_zero_sentences():
#     artiNode = Article("title", "text", 5)
#     volNode = Volume(1, "url")
#     encycNode = Encyclopedia()

#     encycNode.addVolume(volNode)
#     volNode.addArticle(artiNode)
    
#     assert len(encycNode.getSentences()) == 0

# test_one_of_each_node()
# test_three_nodes_in_encyclopedia()
# test_accessing_actions()
# test_zero_sentences()