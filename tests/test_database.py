from ecg_interpreter import Action
from supabase import create_client, Client
from dotenv import load_dotenv
import os

#Load dotenv
load_dotenv()

#Tests the connnection using psycopg2 to the database.

#Invalid user in connection, hashedPass is the hashed password, currently not used
#intended for testing valid users

#Incorrect amount of informmtion provied
#Insertion into a test database test
def test_database_data():
    #Test Data
    activity_expected = [55,155, 255, "aTest0", "dTest0", 555]
    #Create Supabase Client
    supabase: Client = create_client(
        os.environ.get("SUPABASE_URL"), os.environ.get("SUPABASE_KEY")
    )
    #Authorization to sign into database
    supabase.auth.sign_in_with_password(
    {
        "email": os.environ.get("SUPABASE_USER"),
        "password": os.environ.get("SUPABASE_PASS"),
    }
    )  

    #Insert into database with test function
    supabase.table("Activity").insert({"Activity ID": activity_expected[0],
                                        "Person Subj ID": activity_expected[1], 
                                        "Person Obj ID": activity_expected[2], 
                                        "Action": activity_expected[3], 
                                        "Details": activity_expected[4],
                                        "Place ID": activity_expected[5]}).execute()
    
    #Select data from table, from Action column aTest0.
    selection = supabase.table("Activity").select("*").eq("Action", "aTest0").execute()
    selectionData = selection.data

    #Turn the data into a viewable list.
    outputData = list(selectionData[0].values())
    try:
        assert (outputData == activity_expected)
        print("test_database_data() succeeded, assertion is valid")
    except:
        print("Assertation failed, data does not match")
    #Removes test data, just so it doesn't affect the rest of the database. 
    supabase.table("Activity").delete().eq("Action", "aTest0").execute()
    print("Deleted test data from database")

#Test insert multiple lines
def test_database_insert_multiple():
    #Create Supabase Client with .env file
    supabase: Client = create_client(os.environ.get("SUPABASE_URL"), os.environ.get("SUPABASE_KEY"))
    #Authorization to sign into database
    supabase.auth.sign_in_with_password(
        {"email": os.environ.get("SUPABASE_USER"),
         "password": os.environ.get("SUPABASE_PASS"),
        }
    )
    #Creation of activity expected values, insert into Activity table.
    for i in range(0, 5):
        activity_expected = [i, i+1, i+2, "TestAction" + str(i+25), "TestDetails" + str(i+50), i+100]
        supabase.table("Activity").insert({"Activity ID": activity_expected[0],
                                        "Person Subj ID": activity_expected[1], 
                                        "Person Obj ID": activity_expected[2], 
                                        "Action": activity_expected[3], 
                                        "Details": activity_expected[4],
                                        "Place ID": activity_expected[5]}).execute()
    selection = supabase.table("Activity").select("*").execute()
    selectionData = selection.data
    #print(selectionData)

    for i in range(0, len(selectionData)):
        activity_expected = [i, i+1, i+2, "TestAction" + str(i+25), "TestDetails" + str(i+50), i+100]
        outputData = list(selectionData[i].values())
        #print(outputData)
        #print(activity_expected)
        try:
            assert (outputData == activity_expected)
            print("test_database_insert_multiple() succeeded, Assertion is valid")
        except:
            print("Assertion failed, output and expected are not equal.")
        #Delete test data from table.
        supabase.table("Activity").delete().eq("Action", "TestAction" + str(i+25)).execute()

#Test function for function insertIntoDatabase in data_structure.py
def test_insertIntoDatabase():
    #Creation of fake actions list, and append Action objects
    actions = []
    for i in range(0,10):
        actNode = Action(i, i+10, "verb", "details", i+100)
        actions.append(actNode)

    #Connect to Supabase Client
    supabase: Client = create_client(
    os.environ.get("SUPABASE_URL"), os.environ.get("SUPABASE_KEY")
    )
    #Sign in with local .env file.
    supabase.auth.sign_in_with_password(
    {
    "email": os.environ.get("SUPABASE_USER"),
    "password": os.environ.get("SUPABASE_PASS"),
    }
    )
    #Selection of all rows from table.
    selection = supabase.table("Activity").select("*").execute()
    #Getter for data, translates into list[dict{key:value}, dict{key:value}, ... dict{key:value}]
    selectionData = selection.data
    #Loop for inserting Actions into database
    #supabase.table -> go to table "TableName", .insert() -> inserts by "Column Name": value, .execute() -> execute command
    for actionInd in actions:
        #Print statements for indexes
        #print(actions.index(actionInd)+len(selectionData))
        #print(actionInd.personSubjID, actionInd.personObjID, actionInd.action, actionInd.details, actionInd.placeID)
        supabase.table("Activity").insert({"Activity ID": (actions.index(actionInd)+len(selectionData)),
                                            "Person Subj ID": actionInd.personSubjID, 
                                            "Person Obj ID": actionInd.personObjID, 
                                            "Action": actionInd.action, 
                                            "Details": actionInd.details,
                                            "Place ID": actionInd.placeID}).execute()
    print("test_insertIntoDatabase success, added test files to DB")