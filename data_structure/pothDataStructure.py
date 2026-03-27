#Error, psycopg2 could not be resolved from source (reportMissingModuleSource)
import psycopg2
#Maybe use scypt instead of bcrypt here
import bycrypt

#Encyclopedia class
class Encyclopedia:
    #List of Volumes, will always be Volumes class
    volumesList = []

    #Outputs a list of actions
    def getActionInfo(self):
        outputList = []
        for volume in self.volumesList:
            outputList.append(volume.getActionInfo)
        return outputList
    
#Page class (Used in Encyclopedia)
class Volume:
    #List of articles in the Volume. Always will Articles class
    articlesList = []

    #Function for returning list of People objects under a Page.
    #May need reworking due to returning multiple arrays of People.
    def getActionInfo (self):
        for articles in self.articlesList:
            return articles.getPeople()

#Paragraph class (under Pages)
class Article:
    #List of setences in the Article. Always will be Sentences Class
    paragraphText = None
    sentsList = []

    #Function for returning list of People objects under a Page.
    #May need reworking due to returning multiple arrays of People.
    def getActionInfo (self):
        for sentences in self.sents:
            return sentences.getActionsList()

#Sentences class (under Articles)
class Sentences:
    #Sentence Text as a String.
    sentText = None
    #List of persons in a sentence. Always will be filled with Persons Class.
    actionsList = []

    #Function for returning list of People objects under a Page.
    #May need reworking due to returning multiple arrays of People.
    def getActonsList (self):
        return self.actionsList

#Action class (under Sentences)
class Action:
    personSubjID = None
    personObjID = None
    action = None
    details = None
    placeID = None


#Getters and Setters are not required, as access is by (object name).(field)
    
#TODO Write Python to add the tuples (Page:People []) that uses PostgreSQL commands
#to add to our current databaase.

#Will need to create and use an encyclopedia
encylopediaData = []
for encyclo in encycloList:
   encylopediaData.append(encyclo.getInfo)


#REMEMBER encrypt so that others cannot get access to the database without authorization.
dbConnect = psycopg2.connect("dbname='tempName' user='dBeaver' host='testHost' password='notUsedYet'")
dbEditor = dbConnect.cursor()

#People: fName, afName, mName, lName, alName, title, dates, status, organizations, gender
#Places: Name, Type, Subtype, Current Country, Latitude, Longitude, Location Accuracy
#Activity: description, date
for data in encylopediaData:
    dbEditor.execute("INSERT INTO people ()")