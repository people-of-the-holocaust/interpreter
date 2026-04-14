#Error, psycopg2 could not be resolved from source (reportMissingModuleSource)
import psycopg2
#Maybe use scypt instead of bcrypt here
import bycrypt

#TODO Add Getters and Setters to data structure.

#Encyclopedia class
class Encyclopedia:
    #List of Volumes, will always be Volumes class
    volumesList = []

    #Function to add a volume to the volumesList
    def addVolume(self, newVol):
        self.volumesList.append(newVol)
    
    #Outputs a list of actions
    def getActions(self):
        output = []
        for volume in self.volumesList:
            output.append(volume.getActions)
        return output
    
#Page class (Used in Encyclopedia)
class Volume:
    volumeNumber = None
    volumeURL = None
    #List of articles in the Volume. Always will be Articles class
    articlesList = []

    #Constructor for Volume
    def __init__(self, volNum, volURL):
        self.volumeNumber = volNum
        self.volumeURL = volURL

    #Function to add article to articlesList
    def addArticle(self, newArticle):
        self.articlesList.append(newArticle)

    #Function for returning list of People objects under a Page.
    #May need reworking due to returning multiple arrays of People.
    def getActions (self):
        output = []
        for article in self.articlesList:
            output.append(article.getActions())
        return output

#Paragraph class (under Pages)
class Article:
    title = None
    text = None
    documentNumber = None
    #List of key sentences in the Article. Always will be Sentences Class
    sentsList = []

    #Constructor for Article
    def __init__(self, title, text, docNum):
        self.title = title
        self.text = text
        self.documentNumber = docNum

    #Function to add key sentence to sentsList
    def addSent(self, newSent):
        self.sentsList.append(newSent)
    
    #Function for returning list of People objects under a Page.
    #May need reworking due to returning multiple arrays of People.
    def getActions (self):
        output = []
        for sentences in self.sents:
            output.append(sentences.getActions())
        return output

#Sentences class (under Articles)
class Sentence:
    text = None
    #List of ID numbers for names that appear in the sentence. Always will be numbers.
    pids = []
    #List of persons in a sentence. Always will be filled with Persons Class.
    actionsList = []

    #Constructor for Sentence
    def __init__(self, text, pids):
        self.text = text
        self.pids = pids
    
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


#TODO test this tree data structure.


#TODO here attach using psycopg2 with Postgresql
#REMEMBER encrypt so that others cannot get access to the database without authorization.
#dbConnect = psycopg2.connect("dbname='tempName' user='dBeaver' host='testHost' password='notUsedYet'")
#dbEditor = dbConnect.cursor()

#People: fName, afName, mName, lName, alName, title, dates, status, organizations, gender
#Places: Name, Type, Subtype, Current Country, Latitude, Longitude, Location Accuracy
#Activity: description, date
#for data in encylopediaData:
#    dbEditor.execute("INSERT INTO people ()")
