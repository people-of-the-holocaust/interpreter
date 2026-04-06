import psycopg2

#Tests the connnection using psycopg2 to the database.

#Invalid user in connection, hashedPass is the hashed password, currently not used
#intended for testing valid users
def test_invalid_user(hashePass):
    try:
        connect = psycopg2.connect("dbname='People of the Holocaust' user='invalidUser' host='test' password = hashedPass")
    except:
        print("Test 1: Invalid user")

#Valid user, incorrect password
def test_invalid_pass():
    try:
        connect = psycopg2.connect("dbname='People of the Holocaust' user='viewDB' host='test' password = 'invalidpass'")
    except:
        print("Test 2: Invalid password")

#Valid connection with exact values
def test_valid_connection(hashPass):
    try:
        connect = psycopg2.connect("dbname='People of the Holocaust' user='viewB' host='test' password='hashedPass'")
    except:
        print("Test 3: Could not connect")

#Incorrect amount of informmtion provied
#Insertion into a test database test
def test_database_data(hashPass, activity):
    try:
        connect = psycopg2.connect("dbname='People of the Holocaust' user='userEdit' host='test' password='hashedPass'")
    except:
        print("Connection failed")
    cursor = connect.cursor()
    
    #Test values purely to not interact with the rest of the database
    cursor.execute("INSERT INTO Activity (Person Subj ID, Person Obj ID, Action, details) VALUES (%(int4)s, %(int4)s, %(varchar)s, %(varchar)s, %(int4)s", 
                   (activity[0], activity[1], activity[2], activity[3], activity[4]))
    cursor.execute("SELECT * from Activity;")
    
    print(cursor.fetchone())

    assert (cursor.fetchone() == (activity[0], activity[1], activity[2], activity[3], activity[4]))
    connect.rollback()
    connect.close()