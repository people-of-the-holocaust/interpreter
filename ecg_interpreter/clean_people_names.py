import pandas as pd

# hard coded list of titles and deliminators
titles = ["oberleutnant", "bank", "oberstleutnant", "oberst", "countess", 
          "major", "prince", "doctor", "leutnant", "lieutenant", "hauptmann", "ss",
          "general", "colonel", "oberstleutnant dr.", "rittmeister", "général des corps d’armée",
          "officer", "prisoner", "king", "prussian crown prince", "hauptmann dr.", "captain",
          "jewish council member", "oberstleutnant z.v.", "oberleutnant d.r.", "adjutant-chef",
          "hauptmann d.r.", "kriegsverwaltungsinspektor", "Czarny", "kriminalrat", "oberst dr.", "sergeant",
          "oberarzt d.r.", "camp administrator", "police chief", "major der polizei", "camp director", 
          "camp commander", "leutnant d.r.", "oberleutnant dr.", "oberarzt dr.", "stabsarzt dr.", 
          "représentant général", "brigadier-chief adjutant", "kapitän zur see", "unterarzt dr.", 
          "oberstabsarzt dr.", "sd officer", "camp chief", "ss-hauptsturmführer dr.", "oberfeldarzt dr.",
          "senior lieutnant", "leutnant der landwehr", "hauptmann z.v.", "ss officer", 
          "kgf.-bezirkskommandant oberst", "lieutenant colonel", "camp commandant", "major d.r.",
          "stabsarzt d.r. dr.", "major der landwehr", "hauptmann der landwehr z.v.",
          "generalleutnant der polizei", "feldgendarmerie oberleutnant", "chief counselor of justice",
          "major z.f.", "staff sergeant", "oberkriegsgerichtsrat dr.", "lieutenant general"
         ]
alt_delims = ["or", "née", "neé", "aka", "formerly", "later", "born", "possibly"]
loc_delims = ["in", "at", "from"]
org_delims = ["with"]

# handle indicators for an alternate name
def handle_alt_del(delim, text):
    delimiter = "(" + delim + " "
    delim_i = text.index(delimiter)
    name = text[:(delim_i-1)]
    alt_name = text[(delim_i + len(delimiter)):-1]
    return (name, alt_name)

# handle indicators for a location
def handle_loc(delim, text):
    delimiter = "(" + delim + " "
    delim_i = text.index(delimiter)        
    name = text[:(delim_i-1)]
    place = text[(delim_i + len(delimiter)):-1]
    return (name, place)

# handle indicators for an organization
def handle_org(delim, text):
    delimiter = "(" + delim + " "
    delim_i = text.index(delimiter)        
    name = text[:(delim_i-1)]
    org = text[(delim_i + len(delimiter)):-1]
    return (name, org)

# handle first name
def split_first(first):
    fname = first
    alt_fname = ""
    mname = ""
    title = ""
    place = ""
    if 'Prince of Belgium' in fname:
        title = fname
        fname = ""
        place = "Belgium"
    if ' and ' in fname:
        # need to figure out how to split these into two rows of people
#         print(first)
        space = first.index(' ')
        fname = first[:space]
        person2 = first[space:]
    if '“' in fname:
        start = first.index('“') + 1
        end = first.index('”')
        alt_fname = first[start:end].strip(",")
        space = first.index(' ')
        fname = first[:space]
    if '(' in fname:
        # get text within paranthesis
        start = first.index('(') + 1
        end = first.index(')')
        in_para = first[start:end]
        # check if in_para first word is a delimiter, handle accordingly
        pot_delim = in_para[:in_para.index(" ")]
        if pot_delim in alt_delims:
            fname, alt_fname = handle_alt_del(pot_delim, first)
        elif pot_delim in loc_delims:
            fname, place = handle_loc(pot_delim, first)
        # classify in_para as title or alt name, set fname with text around paranthesis
        else:
            if in_para.lower() in titles:
                title = in_para
            else:
                alt_fname = in_para
            fname = first[:start] + first[end:]
            fname = fname.replace(" ()", "")
    if fname[-3:] == "von":
        mname = fname[-3:]
        fname = fname[:-3].strip()
    if ' ' in fname:
        parts = fname.split(" ")
        if len(parts) == 2:
            fname = parts[0]
            mname = parts[1]
        # catch all else --> fname = first
    return [fname, alt_fname, mname, title, place]

# handle last name
def split_last(last):
    lname = last
    alt_lname = ""
    desig = ""
    title = ""
    place = ""
    org = ""
    if 'family' in lname:
        desig = "Family"
        lname = lname.replace(" family", "")
    elif 'brothers' in lname:
        desig = "Brothers"
        lname = lname.replace(" brothers", "")
    else:
        desig = "Individual"
    if '“' in lname:
        start = last.index('“') + 1
        end = last.index('”')
        alt_lname = last[start:end].strip(",")
        space = last.index(' ')
        lname = last[:space]
    if '(' in lname:
        # get text within paranthesis
        start = last.index('(') + 1
        end = last.index(')')
        in_para = last[start:end]
        # check if in_para first word is a delimiter, handle accordingly
        pot_delim = in_para[:in_para.index(" ")]
        if pot_delim in alt_delims:
            lname, alt_lname = handle_alt_del(pot_delim, last)
        elif pot_delim in loc_delims:
            lname, place = handle_loc(pot_delim, last)
        elif pot_delim in org_delims:
            lname, org = handle_org(pot_delim, last)
        # classify in_para as title or alt name, set lname with text around paranthesis
        else:
            if in_para.lower() in titles:
                title = in_para
            elif "prisoner" in in_para.lower():
                ending = len("prisoner") * -1
                place = in_para[:ending].strip()
                title = "Prisoner"
            else:
                alt_lname = in_para
            lname = last[:start] + last[end:]
            lname = lname.replace(" ()", "")
    # catch all else --> lname = last
    return [lname, alt_lname, desig, title, place, org]

# given a raw name, split using above helper functions and add data to pdict
def populate_df(n1, n2, pdict):
    last, first = n1.split(", ") if "," in n1 else (n1, "")

    # if there is an n2, handle that as an alt name (LEFT FOR NEXT ITERATION)
    # last2, first2 = n2.split(", ") if "," in n2 else (n2, "")

    middle = ""
    title = ""
    place = ""
    org = ""
    
    first, alt_first, middle, t1, p1 = split_first(first)
    last, alt_last, desig, t2, p2, org = split_last(last)
    title = t1 if t2 == "" else t2
    place = p1 if p2 == "" else p2

    pdict["Designation"].append(desig)
    pdict["First Name"].append(first)
    pdict["Alt First Name"].append(alt_first)
    pdict["Middle Name"].append(middle)
    pdict["Last Name"].append(last)
    pdict["Alt Last Name"].append(alt_last)
    pdict["Title"].append(title)
    pdict["Place"].append(place)
    pdict["Organization"].append(org)

    return pdict

# main function - given list of all raw names, sort information people_table
# exports people_table to a csv file in tables, returns the ppl_df
def create_ppl_table(all_names):
    pdict = {
        "Designation": [], "First Name": [], "Alt First Name": [], "Middle Name": [], 
        "Last Name": [], "Alt Last Name": [], "Title": [], "Place": [], "Organization": []
    }

    for n in all_names:
        try:
            if ". See:" in n:
                n1, n2 = n.split(". See: ")
                pdict = populate_df(n1, n2, pdict)
            elif " See:" in n:
                n1, n2 = n.split(" See: ")
                pdict = populate_df(n1, n2, pdict)
            else:
                pdict = populate_df(n, ", ", pdict)
        except ValueError:
            pass

    ppl_df = pd.DataFrame(pdict)
    ppl_df.to_csv('./tables/people_table.csv')
    return ppl_df