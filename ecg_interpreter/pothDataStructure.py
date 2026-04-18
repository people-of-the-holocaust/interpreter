import psycopg2
#Maybe use scypt instead of bcrypt here
# import bycrypt

#TODO Add Getters and Setters to data structure.

hashedPass = "$2a$12$4pwVb9bxNCsByFDbwpXXQOBwMvjq.gNFArdovKlno8yHq91AvmcQS"

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
            outputActions.extend(volume.getActions)
        return outputActions
    
    def insert_into_database(self, inputpass):
        try:
            bcrypt.checkpw(inputpass, hashedPass)
            encActions = self.getActions
            #Fix this where password to be a hashed bcrypt password AND update password away from this test password.
            connect = psycopg2.connect("dbname='postgres', user='postgres', host='db.elkjpkawrounaqjwzbjo.supabase.co', password='inputpass'")

            with connect.cursor as curs:
                for actions in encActions:
                #Add to execute for ids, description, and so on. May need to rework an 
                    curs.execute("INSERT INTO Activity (Person Subj ID, Person Obj ID, Action, details, Place ID) VALUES (%s, %s, %s, %s, %s)",
                             (actions.personSubjID, actions.personObjID, actions.action, actions.details, actions.placeId))
            connect.commit()
            curs.close()
            connect.close()
        except:
            print("Error, passwords do not match")
    
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
    #May need reworking due to returning multiple arrays of People.

    def getActions (self):
        outputActions = []
        for article in self.articlesList:
            outputActions.extend(article.getActions())
        return outputActions

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
        for sentences in self.sents:
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
