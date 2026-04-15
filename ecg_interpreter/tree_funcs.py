# given an Encyclopedia object, traverse the tree and return a formatted string containing the tree data
def print_ecg(ecg_node):
    formatted_tree = ""
    if ecg_node:
        if len(ecg_node.volumesList) > 0:
            for vol in ecg_node.volumesList:
                formatted_tree += str(print_vol(vol))
            return formatted_tree
        else:
            return "ENCYCLOPEDIA OBJECT DOES NOT HAVE ANY VOLUMES"

    else:
        return "ENCYCLOPEDIA OBJECT DOES NOT EXIST"

def print_vol(vol_node):
    formatted_vol = ""
    if vol_node:
        formatted_vol += ("\n\n\nVOLUME " + str(vol_node.volumeNumber) + " : " + str(vol_node.volumeURL))
        if len(vol_node.articlesList) > 0:
            for article in vol_node.articlesList:
                formatted_vol += str(print_article(article))
            return formatted_vol
        else:
            return "VOLUME OBJECT DOES NOT HAVE ANY ARTICLES"
    else:
        return "VOLUME OBJECT DOES NOT EXIST"

def print_article(article_node):
    formatted_article = ""
    if article_node:
        formatted_article += ("\n\nARTICLE: " + str(article_node.title) + " : " + str(article_node.documentNumber))
        if article_node.text is None:
            formatted_article += "Article does not have any text saved.\n"
        if len(article_node.sentsList) > 0:
            for sent in article_node.sentsList:
                formatted_article += str(print_sent(sent))
            return formatted_article
        else:
            return "ARTICLE OBJECT DOES NOT HAVE ANY SENTENCES"
    else:
        return "ARTICLE OBJECT DOES NOT EXIST"


def print_sent(sent_node):
    formatted_sent = ""
    if sent_node:
        formatted_sent += "\nSENTENCE:"
        if sent_node.text is None:
            formatted_sent += "Sentence does not have any text.\n"
        if len(sent_node.pids) == 0:
            formatted_sent += "Sentence does not have any pids.\n"
        if len(sent_node.actionsList) > 0:
            for action in sent_node.actionsList:
                formatted_sent += str(print_action(action))
            return formatted_sent
        else:
            formatted_sent += "SENTENCE OBJECT DOES NOT HAVE ANY ACTIONS"
            return formatted_sent
    else:
        return "SENTENCE OBJECT DOES NOT EXIST"

def print_action(action_node):
    if action_node:
        if all(field is None for field in [action_node.personSubjID, action_node.personObjID, action_node.action, action_node.details, action_node.placeID]):
            return "\nACTION HAS NO FIELDS"
        # action could not be parsed
        if action_node.action is None:
            return (str(action_node.details) + "\nAction in above sentence could not be parsed during processing.")
        # object case
        elif action_node.personSubjID is None:
            return (str(action_node.details) + " " + str(action_node.action) + " " + str(action_node.personObjID) + " in " + str(action_node.placeID))
        # subject case
        elif action_node.personObjID is None:
            return (str(action_node.personSubjID) + " " + str(action_node.action) + " " + str(action_node.details) + " in " + str(action_node.placeID))
    else:
        return "ACTION OBJECT DOES NOT EXIST"
    