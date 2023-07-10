import re
import pandas as pd

abusive = pd.read_csv('D:/Binar_Data Science/data/abusive.csv', encoding='utf-8')
new_kamusalay = pd.read_csv('D:/Binar_Data Science/data/new_kamusalay.csv', encoding='latin1')
new_kamus_alay = {}
for k,v in new_kamusalay.values:
    new_kamus_alay[k] = v


def processing_word(input_text):
    new_text = [] 
    new_new_text = [] 
    text = input_text.split(" ") 
    for word in text: 
        if word in abusive['ABUSIVE'].tolist(): 
            continue # jika ada, skip
        else:
            new_text.append(word) 
   
    for word in new_text:
        new_word = new_kamus_alay.get(word, word) 
        new_new_text.append(new_word)
    
    text = " ".join(new_new_text)
    return text

def processing_text(input_text):
    text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', 'EMAIL', input_text) 
    text = text.lower() 
    text = re.sub(r'[^\w\s]', '', text) 
    text = text.replace(" 62"," 0")
    text = re.sub(r"\b\d{4}\s?\d{4}\s?\d{4}\b", "NOMOR_TELEPON", text) 
    text = text.replace("USER","")
    text = text.strip()
    
    text = processing_word(text)
    return text