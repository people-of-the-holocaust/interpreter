import pandas as pd
from nltk.tokenize import word_tokenize


# helper function - if first name found, determine if next words are middle or last name
# checks for fmal, afmal, fal, or afal
def is_full_name_altlname(filtered_df, words_lst, fname_i, sent):
    next_w = words_lst[fname_i + 1]
    # check if next word is a corresponding middle name - trying to find fmal or afmal
    found_mnames = filtered_df[filtered_df['Middle Name'] == next_w]
    if len(found_mnames) != 0:
        # check if word after mname is a corresponding last name - trying to find fmal or afmal
        next2_w = words_lst[fname_i + 2]
        found_lnames = found_mnames[found_mnames['Alt Last Name'] == next2_w]
    # check if next word is a corresponding last name - trying to find fal or afal
    else:
        found_lnames = filtered_df[filtered_df['Alt Last Name'] == next_w]
        
    # found one row with valid fml or fl name
    if len(found_lnames) == 1:
        found_id = found_lnames.index[0]
        print("FINAL ID", found_id)
        return found_id
    # did not find valid name, classify as NOT PERSON NAME (-1)
    elif len(found_lnames) == 0:
        print("NOT PERSON NAME")
        return -1
    # found multiple options, parse further (LEFT FOR NEXT ITERATION)
    print("TOO MANY PEOPLE")
    return -2
    
    
# helper function - if first name found, determine if next words are middle or last name
# checks for fml, afml, fl, or afl
def is_full_name(filtered_df, words_lst, fname_i, sent):
    next_w = words_lst[fname_i + 1]
    # check if next word is a corresponding middle name - trying to find fml or afml
    found_mnames = filtered_df[filtered_df['Middle Name'] == next_w]
    if len(found_mnames) != 0:
        # check if word after mname is a corresponding last name - trying to find fml or afml
        next2_w = words_lst[fname_i + 2]
        found_lnames = found_mnames[found_mnames['Last Name'] == next2_w]
    # check if next word is a corresponding last name - trying to find fl or afl
    else:
        found_lnames = filtered_df[filtered_df['Last Name'] == next_w]
        
    # found one row with valid fml or fl name
    if len(found_lnames) == 1:
        found_id = found_lnames.index[0]
        print("FINAL ID", found_id)
        return found_id
    # did not find valid name with reg lname, check alt lname
    elif len(found_lnames) == 0:
        print("CHECK ALT LAST NAME")
        return is_full_name_altlname(filtered_df, words_lst, fname_i, sent)
    # found multiple options, parse further (LEFT FOR NEXT ITERATION)
    print("TOO MANY PEOPLE")
    return -2


# main function - determine if a given sentence contains a person name
# sent might be KEY for multiple people
# returns a list of pids for whom this sentence is KEY
def is_key(sent, ppl_df):
    pids = []
    # result: -1 = no pid found, -2 = multiple people found, else = found pid
    result = -1
    words = word_tokenize(sent)
    for i, w in enumerate(words):
        found_fnames = ppl_df[ppl_df['First Name'] == w]
        if len(found_fnames) != 0:
            result = is_full_name(found_fnames, words, i, sent)
            print("REG RESULT:", result)
        # didn't find the correct person from fname, check afname
        if result == -1:
            found_afnames = ppl_df[ppl_df['Alt First Name'] == w]
            if len(found_afnames) != 0:
                result = is_full_name(found_afnames, words, i, sent)
                print("ALT RESULT:", result)
        # didn't find correct person from fname or afname, check if lname
        if result == -1:
            found_lnames = ppl_df[ppl_df['Last Name'] == w]
            # found multiple options, parse further (LEFT FOR NEXT ITERATION)
            if len(found_lnames) != 0:
                result = -2
        if result != -1 and result != -2:
            if result not in pids:
                pids.append(result)
    return pids

