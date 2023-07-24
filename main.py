import pandas as pd
import nltk
from preprocessing import preprocessing
import os

final_cases = pd.read_csv('final_cases.csv')
dignity_cases = pd.read_csv('dignity_cases.csv')
all_processed_facts = []


# TEXT PREPROCESSING (Legal Stop words)
legal_sw = ['adjourned', 'affidavit', 'allegation', 'appeal', 'appellant', 'application', 'applicant', "applicant's",
            'arbitration','case', 'cause', 'claim', 'clerk', 'complaint', 'consent', 'contempt', 'contravention',
            'conviction','costs', 'court', 'cross-examination', 'defence', 'defendant', 'deposition', 'discovery',
            'dispute','evidence', 'examination', 'fact', 'hearing', 'judge', 'judgment', 'jurisdiction', 'justice','law',
            'lawsuit', 'legal', 'litigant', 'litigation', 'moot', 'motion', 'objection', 'order', 'parties', 'pleading',
            'proceedings', 'ruling', 'sentence', 'settlement', 'solicitor', 'statute', 'subpoena', 'testimony', 'trial',
            'verdict', 'witness', 'cases', 'courts', "litigant's", "defendant's","judge's", 'council', 'government',
            'mr', 'lawyer', 'supreme', 'judicial', 'ha', 'wa', 'european','union','person','right','freedom','expression',
            'see','paragraph','read','follows','article','human','section','criminal','police','abdullah','öcalan','turkish',
            'turkey','istanbul','public','prosecutor','russian federation','public','event','administrative','offence',
            'moscow','proceeding','decision']

month_sw = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november'
            , 'december']

files_to_consider = []
counter_dignity = 0


for filename in dignity_cases['Case']:
    trial = preprocessing(filename)
    cleaned = trial.clean()
    #print("CLEANED: " + cleaned)
    facts = trial.get_facts(cleaned)
    #print("FACTS: " + facts)
    processed = trial.preprocess_text(facts, legal_sw, month_sw, s_w=True, lemma=True)
    # print("PROCESSED: " + processed)

    # Save all processed facts in a list
    all_processed_facts.append(processed)

    #if 'dignity' in processed:
    #    files_to_consider.append([filename, processed])
    #    counter_dignity = counter_dignity + 1
    #    #Save all processed facts in a list
    #    all_processed_facts.append(processed)

'''
print(counter_dignity)
dignity_cases = pd.DataFrame(columns=['Case', 'fact'])
for file in files_to_consider:
    new_row = {'Case': file[0], 'fact': file[1]}
    dignity_cases = pd.concat([dignity_cases, pd.DataFrame([new_row])], ignore_index=True)
final_cases.to_csv('dignity_cases.csv', index=False)

'''


def prepare(all_text):
    facts_df = pd.DataFrame(columns=['Facts', 'Cluster', 'x0', 'x1'])
    facts_df['Facts'] = all_text

    return facts_df

# CSVs for experiments

facts = prepare(all_text=all_processed_facts)
facts.to_csv('facts_processed.csv')
#facts.to_csv('facts_lemma.csv')
#facts.to_csv('facts_sw.csv')
#facts.to_csv('facts_none.csv')



# This piece of code was to filter the documents (downloaded from scraping) that actually contained text and were not empty
'''
final_cases = pd.DataFrame(columns=['Case'])
for file in files_to_consider:
    new_row = {'Case': file}
    final_cases = pd.concat([final_cases, pd.DataFrame([new_row])], ignore_index=True)
final_cases.to_csv('final_cases.csv', index=False)
'''

