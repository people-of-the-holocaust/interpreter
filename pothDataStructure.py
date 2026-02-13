#Encyclopedia class
class Encyclopedia:
    #List of Pages
    pages = []
    
#Page class (Used in Encyclopedia)
class Page:
    #List of paragraphs in the Page. Always will Para class
    pageText = None
    paras = []

#Paragraph class (under Pages)
class Para:
    #List of setences in the paragraph. Always will be Sentenes Class
    paragraphText = None
    sents = []

#Sentences class (under Paragraphs)
class Sentences:
    #List of persons in a sentence. Always will be filled with Persons Class.
    sentText = None
    persons = []

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
    
    
