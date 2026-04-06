from ecg_interpreter import Encyclopedia, Volume, Article, Sentence, Action

#Testing data structure

#One of each node, Encyclopedia->Volume->Article->Sentence->Action, all empty
def one_of_each_node_test():
    actNode = Action()
    sentNode = Sentence()
    artiNode = Article()
    volNode = Volume()
    encycNode = Encyclopedia()

    encycNode.volumesList.append(volNode)
    volNode.articlesList.append(artiNode)
    artiNode.sentsList.append(sentNode)
    sentNode.actionsList.append(actNode)

    #Assertions that check if made properly.
    assert len(encycNode.volumesList) == 1
    assert len(encycNode.volumesList[0].articlesList) == 1
    assert len(encycNode.volumesList[0].articlesList[0].sentsList) == 1
    assert len(encycNode.volumesList[0].articlesList[0].sentsList[0].actionsList) == 1

#Testing four Volumes with one of Article, Sentence, and Action.
def three_nodes_in_encyclopedia():
    encyNode = Encyclopedia()
    for i in range(4):
        volumeNode = Volume()
        encyNode.volumesList.append(volumeNode)

        artiNode = Article()
        encyNode.volumesList[i].articlesList.append(artiNode)

        sentNode = Sentence()
        encyNode.volumesList[i].articlesList[i].sentsList.append(sentNode)

        actNode = Action()
        encyNode.volumesList[i].acticlesList[i].setsList[i].actionsList.append(actNode)

    #Assertation
    for i in range(4):
        assert len(encyNode.volumesList) == 1
        assert len(encyNode.volumesList[i].articlesList) == 1
        assert len(encyNode.volumesList[i].articlesList[i].sentsList) == 1
        assert len(encyNode.volumesList[i].articlesList[i].sentsList[i].actionsList) == 1

#Test Encyclopedia gathering a combined list of three lesser Actions within the above.
def test_accessing_actions():
    encyNode = Encyclopedia()
    for i in range(4):
        volumeNode = Volume()
        encyNode.volumesList.append(volumeNode)

        artiNode = Article()
        encyNode.volumesList[i].articlesList.append(artiNode)

        sentNode = Sentence()
        encyNode.volumesList[i].articlesList[i].sentsList.append(sentNode)
        for j in range(3):
            actNode = Action()
            actNode.action = "Action in Sentence: " + str(i)
            actNode.detail = "Action Detail: " + str(j)
            actNode.placeID = j
            encyNode.volumesList[i].acticlesList[i].setsList[i].actionsList.append(actNode)
    actions = encyNode.getActions()

    #Expected to be of size of 12 with varying actions.
    assert len(actions) != 0
    assert len(actions) == 12

#Test for when there's no actions possible.
def test_no_actions():
    encyNode = Encyclopedia
    for i in range(4):
        volumeNode = Volume()
        encyNode.volumesList.append(volumeNode)

        artiNode = Article()
        encyNode.volumesList[i].articlesList.append(artiNode)

        sentNode = Sentence()
        encyNode.volumesList[i].articlesList[i].sentsList.append(sentNode)
    
    assert len(encyNode.getActions()) == 0

#Tests for sentences.
def test_grab_sentences():
    encyNode = Encyclopedia()
    for i in range(4):
        volumeNode = Volume()
        encyNode.volumesList.append(volumeNode)

        artiNode = Article()
        encyNode.volumesList[i].articlesList.append(artiNode)

        sentNode = Sentence()
        encyNode.volumesList[i].articlesList[i].sentsList.append(sentNode)

        actNode = Action()
        encyNode.volumesList[i].acticlesList[i].setsList[i].actionsList.append(actNode)

    #Assertation
    for i in range(4):
        assert len(encyNode.volumesList) == 1
        assert len(encyNode.volumesList[i].articlesList) == 1
        assert len(encyNode.volumesList[i].articlesList[i].sentsList) == 1
        assert len(encyNode.volumesList[i].articlesList[i].sentsList[i].actionsList) == 1

#Test Encyclopedia gathering a combined list of three lesser Actions within the above.
def test_accessing_actions():
    encyNode = Encyclopedia()
    for i in range(4):
        volumeNode = Volume()
        encyNode.volumesList.append(volumeNode)

        artiNode = Article()
        encyNode.volumesList[i].articlesList.append(artiNode)

        sentNode = Sentence()
        encyNode.volumesList[i].articlesList[i].sentsList.append(sentNode)
        for j in range(3):
            actNode = Action()
            actNode.action = "Action in Sentence: " + str(i)
            actNode.detail = "Action Detail: " + str(j)
            actNode.placeID = j
            encyNode.volumesList[i].acticlesList[i].setsList[i].actionsList.append(actNode)

    assert len(encyNode.getSentences()) == 4

#Tests for when zero sentences.
def test_zero_sentences():
    artiNode = Article()
    volNode = Volume()
    encycNode = Encyclopedia()

    encycNode.volumesList.append(volNode)
    volNode.articlesList.append(artiNode)
    
    assert len(encycNode.getSentences()) == 0