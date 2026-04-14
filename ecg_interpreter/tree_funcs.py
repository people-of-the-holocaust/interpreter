# given an Encyclopedia object, traverse through the tree and print out the data in a readable format
def print_ecg(ecg_node):
    if ecg_node:
        if len(ecg_node.volumesList) > 0:
            for vol in ecg_node.volumesList:
                print_vol(vol)
        else:
            print("ENCYCLOPEDIA OBJECT DOES NOT HAVE ANY VOLUMES")

    else:
        print("ENCYCLOPEDIA OBJECT DOES NOT EXIST")

def print_vol(vol_node):
    if vol_node:
        print("VOLUME", vol_node.volumeNumber, ":", vol_node.volumeURL)
        if len(vol_node.articlesList) > 0:
            for article in vol_node.articlesList:
                print_article(article)
        else:
            print("VOLUME OBJECT DOES NOT HAVE ANY ARTICLES")
    else:
        print("VOLUME OBJECT DOES NOT EXIST")

def print_article(article_node):
    if article_node:
        print("ARTICLE:", article_node.title, ":", article_node.documentNumber)
        if article_node.text is None:
            print("Article does not have any text.")
        if len(article_node.sentsList) > 0:
            for sent in article_node.sentsList:
                print_sent(sent)
        else:
            print("ARTICLE OBJECT DOES NOT HAVE ANY SENTENCES")
    else:
        print("ARTICLE OBJECT DOES NOT EXIST")


def print_sent(sent_node):
    if sent_node:
        print("SENTENCE:")
        if sent_node.text is None:
            print("Sentence does not have any text.")
        if len(sent_node.pids) == 0:
            print("Sentence does not have any pids.")
        if len(sent_node.actionsList) > 0:
            for action in sent_node.actionsList:
                print_action(action)
        else:
            print("SENTENCE OBJECT DOES NOT HAVE ANY SENTENCES")
    else:
        print("SENTENCE OBJECT DOES NOT EXIST")

def print_action(action_node):
    if action_node:
        if all(field is None for field in [action_node.personSubjID, action_node.personObjID, action_node.action, action_node.details, action_node.placeID]):
            print("ACTION HAS NO FIELDS")
            return
        # action could not be parsed
        if action_node.action is None:
            print(action_node.details)
            print("Action in above sentence could not be parsed during processing.")
        # object case
        elif action_node.personSubjID is None:
            print(action_node.details, action_node.action, action_node.personObjID, "in", action_node.placeID)
        # subject case
        elif action_node.personObjID is None:
            print(action_node.personSubjID, action_node.action, action_node.details, "in", action_node.placeID)
    else:
        print("ACTION OBJECT DOES NOT EXIST")
    