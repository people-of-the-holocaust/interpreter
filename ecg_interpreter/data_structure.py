#Imports
from supabase import create_client, Client
from dotenv import load_dotenv
import os

#Grab URL from local enviroment.
DATABASE_URL = os.getenv("DATABASE_URL")

#Encyclopedia class
class Encyclopedia:
    #List of Volumes, will always be Volumes class
    volumesList = None

    #Constructor for Encyclopedia
    def __init__(self):
        self.volumesList = []
    
    #Function to add a volume to the volumesList
    def addVolume(self, newVol):
        self.volumesList.append(newVol)
    
    #Outputs a list of actions
    def getActions(self):
        outputActions = []
        for volume in self.volumesList:
            outputActions.extend(volume.getActions())
        return outputActions
    
    def insertIntoDatabase(self):
        actions = self.getActions()
        for i in range(0,10):
            actNode = Action(i, i+10, "verb", "details", i+100)
            actions.append(actNode)

        supabase: Client = create_client(
        os.environ.get("SUPABASE_URL"), os.environ.get("SUPABASE_KEY")
        )
        supabase.auth.sign_in_with_password(
        {
        "email": os.environ.get("SUPABASE_USER"),
        "password": os.environ.get("SUPABASE_PASSWORD"),
        }
        )
        selection = supabase.table("Activity").select("*").execute()
        selectionData = selection.data

        for actionInd in actions:
            supabase.table("Activity").insert({"Activity ID": (actions.index(actionInd)+len(selectionData)),
                                            "Person Subj ID": actionInd.personSubjID, 
                                            "Person Obj ID": actionInd.personObjID, 
                                            "Action": actionInd.action, 
                                            "Details": actionInd.details,
                                            "Place ID": actionInd.placeID}).execute()
    
#Page class (Used in Encyclopedia)
class Volume:
    volumeNumber = None
    volumeURL = None
    #List of articles in the Volume. Always will be Articles class
    articlesList = None

    #Constructor for Volume
    def __init__(self, volNum, volURL):
        self.volumeNumber = volNum
        self.volumeURL = volURL
        self.articlesList = []

    #Function to add article to articlesList
    def addArticle(self, newArticle):
        self.articlesList.append(newArticle)

    #Function for returning list of People objects under a Page.
    def getActions (self):
        outputActions = []
        for article in self.articlesList:
            outputActions.extend(article.getActions())
        return outputActions
    
    def insertIntoDatabase(self):
        actions = self.getActions()
        supabase: Client = create_client(
        os.environ.get("SUPABASE_URL"), os.environ.get("SUPABASE_KEY")
        )
        supabase.auth.sign_in_with_password(
        {
        "email": os.environ.get("SUPABASE_USER"),
        "password": os.environ.get("SUPABASE_PASSWORD"),
        }
        )
        selection = supabase.table("Activity").select("*").execute()
        selectionData = selection.data

        for actionInd in actions:
            supabase.table("Activity").insert({"Activity ID": (actions.index(actionInd)+len(selectionData)),
                                            "Person Subj ID": actionInd.personSubjID, 
                                            "Person Obj ID": actionInd.personObjID, 
                                            "Action": actionInd.action, 
                                            "Details": actionInd.details,
                                            "Place ID": actionInd.placeID}).execute()

#Paragraph class (under Pages)
class Article:
    title = None
    text = None
    documentNumber = None
    #List of key sentences in the Article. Always will be Sentences Class
    sentsList = None

    #Constructor for Article
    def __init__(self, title, text, docNum):
        self.title = title
        self.text = text
        self.documentNumber = docNum
        self.sentsList = []

    #Function to add key sentence to sentsList
    def addSent(self, newSent):
        self.sentsList.append(newSent)
    
    #Function for returning list of People objects under a Page.
    #May need reworking due to returning multiple arrays of People.
    def getActions (self):
        outputActions = []
        for sentences in self.sentsList:
            outputActions.extend(sentences.getActions())
        return outputActions

#Sentences class (under Articles)
class Sentence:
    text = None
    #List of ID numbers for names that appear in the sentence. Always will be numbers.
    pids = None
    #List of persons in a sentence. Always will be filled with Persons Class.
    actionsList = None

    #Constructor for Sentence
    def __init__(self, text, pids):
        self.text = text
        self.pids = pids
        self.actionsList = []
    
    #Function to add action to actionsList
    def addAction(self, newAction):
        self.actionsList.append(newAction)

    #Function for returning list of People objects under a Page.
    #May need reworking due to returning multiple arrays of People.
    def getActions (self):
        return self.actionsList

#Action class (under Sentences)
class Action:
    personSubjID = None
    personObjID = None
    action = None
    details = None
    placeID = None

    #Constructor for Action
    def __init__(self, psid, poid, act, det, lid):
        self.personSubjID = psid
        self.personObjID = poid
        self.action = act
        self.details = det
        self.placeID = lid
