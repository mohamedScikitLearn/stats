from flask import Flask,render_template,url_for,request
import pandas as pd 
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
import re
from nltk import FreqDist
import os
from nltk.corpus import stopwords
nltk.download('stopwords')

stopwordss=stopwords.words('english')
stopFr=stopwords.words('french')
stop_words = []
for i in stopFr:
  stop_words.append(i)

for i in stopwordss:
  stop_words.append(i)

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])

def predict():
     if request.method == 'POST':
         
        filepath  = request.files['file']
     
      
         
        data = read_file(filepath)
       
        print(data)
        avg=  average_number(filepath)
        words = data.split()
        number_words= len(words)
        ##########
        
        filtered_sentence = [w for w in words if not w.lower() in stop_words]

        fdist = FreqDist(filtered_sentence)
        freqs= fdist.most_common(10)# GET TOP 10 first TOKENS

      ########## 
       


       
       # # avg= average_Number(filepath)
       #  freq= get_frequent_tokens_without_stops(filepath)
        
       #  print('number_words = ', number_words , "avg =" , number_words)
        return render_template('result.html',count=number_words, frequent = freqs,avg= avg)

    
def read_file(filepath):

    data = filepath.read()
    data= data.decode()
    return data
    
def numberwords(filepath): # replace this with data
  data= read_file(filepath)
  words = data.split()
  nmbr_words= len(words)
  print(nmbr_words)
  return nmbr_words



def average_number(filepath):
  data = read_file(filepath)
  doc = data.split('.')
  averages=[]
 
  for sentence in  doc: 
    try:  

        words = sentence.split()
    
        average = sum(len(word) for word in words) / len(words)
    
        print(average)
        averages.append(average)
        print(averages)
        avg= sum(averages)/len(averages)
    except ZeroDivisionError:
        avg=10

    return avg


def get_frequent_tokens_without_stops(filepath):

  data = filepath.read()
  words = data.split()
  filtered_sentence = [w for w in words if not w.lower() in stop_words]

  fdist = FreqDist(filtered_sentence)
  freqs= fdist.most_common(10)# GET TOP 10 first TOKENS
  return freqs





if __name__ == '__main__':
	app.run(debug=True)
