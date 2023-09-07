import os

import pandas as pd
import re
from preprocessing import preprocessing

dignity_cases = pd.read_csv('dignity_cases.csv')
processed = pd.read_csv('facts_processed.csv')
violations_df = pd.DataFrame(columns=['File', 'Name', 'Two', 'Three', 'Eight', 'Facts'])


def use_regular(clean):
    # removes all non-alphanumeric characters and spaces
    characters = re.sub(r'[^\w\s]', '', clean)
    # removes all digits
    #digits = re.sub(r'\d+', '', characters)
    # makes sure there is a space between uppercase and lowercase text
    final = re.sub(r'(?<=[a-z0-9])(?=[A-Z])', ' ', characters)

    return final


def check_name(file):
    return True


def check_violation(reg):
    cut = reg.split()

    #start_phrase = {"FOR, THESE, REASONS, THE, COURT"}
    start_phrase = {"REASONS"}
    start_index = None
    end_index = len(cut) - 1
    #print("End Index ")
    #print(end_index)
    for single in cut:
        if any(phrase in single for phrase in start_phrase):
            # find the start index
            start_index = cut.index(single) + len(single)
            #print(start_index)
    if start_index is not None:
        ending = ' '.join(cut[start_index:end_index])
        #print(ending)

        art_two_phrase = "Holds that there has been a violation of Article 2"
        art_three_phrase = "Holds that there has been a violation of Article 3"
        art_eight_phrase = "Holds that there has been a violation of Article 8"

        if art_two_phrase in ending:
            flag_two = True
        else:
            flag_two = False

        if art_three_phrase in ending:
            flag_three = True
        else:
            flag_three = False

        if art_eight_phrase in ending:
            flag_eight = True
        else:
            flag_eight = False

        return flag_two, flag_three, flag_eight
    else:
        # Cannot find the last paragraph
        return False, False, False


def add_to_df(df, f, n, flag_two, flag_three, flag_eight, fact):
    new_row = {
        'File': f,
        'Name': n,
        'Two': flag_two,
        'Three': flag_three,
        'Eight': flag_eight,
        'Facts': fact
    }

    # Append the new row to the DataFrame
    df.loc[len(df)] = new_row
    #df = df.append(new_row, ignore_index=True)

    return df

print(processed['Facts'][0])

keeping_count = []
count = 0
for filename in dignity_cases['Case']:
    for file in os.listdir('text_files'):
        if file == filename:
            process = preprocessing(file)
            clean = process.clean()
            regular = use_regular(clean)
            keeping_count.append(filename)
            flag2, flag3, flag8 = check_violation(regular)
            #print(flag2, flag3, flag8)
            if (flag2 is not False) or (flag3 is not False) or (flag8 is not False):
                name = "TODO"
                facts = processed['Facts'][count]
                violations_df = add_to_df(violations_df, filename, name, flag2, flag3, flag8, facts)
    count = count + 1
print(len(keeping_count))
print(count)
violations_df.to_csv('violations_data.csv')
