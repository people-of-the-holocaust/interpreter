import psycopg2, os
from dotenv import load_dotenv

load_dotenv()

#.env local file with Database URL
DATABASE_URL = os.getenv("DATABASE_URL")

#Encyclopedia class
class Encyclopedia:
    #List of Volumes, will always be Volumes class
    volumesList = []

    #Outputs a list of actions
    def getActions(self):
        outputActions = []
        for volume in self.volumesList:
            outputActions.extend(volume.getActions)
        return outputActions
    
    def insert_into_database(self):
        encActions = self.getActions
        DATABASE_URL = os.getenv("DATABASE_URL")
        #Fix this where password to be a hashed bcrypt password AND update password away from this test password.
        connect = psycopg2.connect(DATABASE_URL)

        with connect.cursor as curs:
            for actions in encActions:
            #Add to execute for ids, description, and so on. May need to rework an 
                curs.execute("INSERT INTO Activity (Person Subj ID, Person Obj ID, Action, details, Place ID) VALUES (%s, %s, %s, %s, %s)",
                            (actions.personSubjID, actions.personObjID, actions.action, actions.details, actions.placeId))
        connect.commit()
        curs.close()
        connect.close()
    
#Page class (Used in Encyclopedia)
class Volume:
    #List of articles in the Volume. Always will Articles class
    articlesList = []

    #Function for returning list of People objects under a Page.
    #May need reworking due to returning multiple arrays of People.

    def getActions (self):
        outputActions = []
        for article in self.articlesList:
            outputActions.extend(article.getActions())
        return outputActions

#Paragraph class (under Pages)
class Article:
    #List of setences in the Article. Always will be Sentences Class
    paragraphText = None
    sentsList = []

    #Function for returning list of People objects under a Page.
    #May need reworking due to returning multiple arrays of People.
    def getActions (self):
        outputActions = []
        for sentences in self.sents:
            outputActions.extend(sentences.getActions())
        return outputActions

#Sentences class (under Articles)
class Sentence:
    #List of persons in a sentence. Always will be filled with Persons Class.
    actionsList = []

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