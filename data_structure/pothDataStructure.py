#Error, psycopg2 could not be resolved from source (reportMissingModuleSource)
import psycopg2
#Maybe use scypt instead of bcrypt here
import bycrypt

#TODO Add Getters and Setters to data structure.

#Encyclopedia class
class Encyclopedia:
    #List of Volumes, will always be Volumes class
    volumesList = []

    #Outputs a list of actions
    def getActions(self):
        output = []
        for volume in self.volumesList:
            output.append(volume.getActions)
        return output
    
#Page class (Used in Encyclopedia)
class Volume:
    #List of articles in the Volume. Always will Articles class
    articlesList = []

    #Function for returning list of People objects under a Page.
    #May need reworking due to returning multiple arrays of People.
    def getActions (self):
        output = []
        for article in self.articlesList:
            output.append(article.getActions())
        return output

#Paragraph class (under Pages)
class Article:
    #List of setences in the Article. Always will be Sentences Class
    paragraphText = None
    sentsList = []

    #Function for returning list of People objects under a Page.
    #May need reworking due to returning multiple arrays of People.
    def getActions (self):
        output = []
        for sentences in self.sents:
            output.append(sentences.getActions())
        return output

#Sentences class (under Articles)
class Sentences:
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
