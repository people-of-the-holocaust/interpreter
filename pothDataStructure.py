#Error, psycopg2 could not be resolved from source (reportMissingModuleSource)
import psycopg2
#Maybe use scypt instead of bcrypt here
import bycrypt

#REMEMBER encrypt so that others cannot get access to the database without authorization.
databaseConnect = psycopg2.connect("dbname='tempName' user='dBeaver' host='serverHost' password='notUsedYet'")
dataBaseEditor = databaseConnect.cursor()

#Encyclopedia class
class Encyclopedia:
    #List of Pages, will always be Pages class
    pages = []

    #Outputs a tuple list that attaches People class to the Pages class
    def getInfo(self):
        outputList = []
        for page in self.pages:
            newTuple = (page, page.getPeople)
            outputList.append(newTuple)
        return outputList
    
#Page class (Used in Encyclopedia)
class Page:
    #List of Paragraphs in the Page. Always will Para class
    paras = []
    #Page desc contains the Page header that contains the location
    desc = None
    #Page date contains the date that is used in the database
    date = None

    #Function for returning list of People objects under a Page.
    #May need reworking due to returning multiple arrays of People.
    def getPeople (self):
        paragrphs = self.pars
        for paras in self.paragraphs:
            return paras.getPeople()

#Paragraph class (under Pages)
class Para:
    #List of setences in the paragraph. Always will be Sentenes Class
    paragraphText = None
    sents = []

    #Function for returning list of People objects under a Page.
    #May need reworking due to returning multiple arrays of People.
    def getPeople (self):
        for sentences in self.sents:
            return sentences.getPeople()

#Sentences class (under Paragraphs)
class Sentences:
    #Sentence Text as a String.
    sentText = None
    #List of persons in a sentence. Always will be filled with Persons Class.
    persons = []

    #Function for returning list of People objects under a Page.
    #May need reworking due to returning multiple arrays of People.
    def getPeople (self):
        return self.persons

#Persons class (under Sentences)
class Persons:
    #Fields for a specific person. None of these require getters or setters.
    fName = None
    aFName = None
    mName = None
    lName = None
    aLName = None
    title = None
    dates = None
    status = None
    orgs = None
    gender = None
    location = None

#Getters and Setters are not required, as access is by (object name).(field)
    
#TODO Write Python to add the tuples (Page:People []) that uses PostgreSQL commands
#to add to our current databaase.