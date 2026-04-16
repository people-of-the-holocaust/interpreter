import psycopg2
#Maybe use scypt instead of bcrypt here
import bycrypt

#TODO Add Getters and Setters to data structure.

#Encyclopedia class
class Encyclopedia:
    #List of Volumes, will always be Volumes class
    volumesList = []

    #TODO add functionality to get Sentences Objects
    def getSentences(self):
        outputSentences = []
        for volume in self.volumesList:
            outputSentences.extend(volume.getSetnences)
        return outputSentences
    
    #Outputs a list of actions
    def getActions(self):
        outputActions = []
        for volume in self.volumesList:
            outputActions.extend(volume.getActions)
        return outputActions
    
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


#REMEMBER encrypt so that others cannot get access to the database without authorization.
#Must be an Encyclopedia value
def insert_into_database(root):
    encActions = root.getActions
    #Fix this where password is the password for account
    connect = psycopg2.connect("dbname='postgres', user='01a76196-f218-4028-888e-c7b310493720', host='db.elkjpkawrounaqjwzbjo.supabase.co', password='dummyPass")

    with connect.cursor as curs:
        for actions in encActions:
            #Add to execute for ids, description, and so on.
            curs.execute("INSERT INTO Activity (Person Subj ID, Person Obj ID, Action, details, Place ID) VALUES (%s, %s, %s, %s, %s)",
                         (actions.personSubjID, actions.personObjID, actions.action, actions.details, actions.placeId))


#People: fName, afName, mName, lName, alName, title, dates, status, organizations, gender
#Places: Name, Type, Subtype, Current Country, Latitude, Longitude, Location Accuracy
#Activity: description, date
#for data in encylopediaData:
#    dbEditor.execute("INSERT INTO people ()")
