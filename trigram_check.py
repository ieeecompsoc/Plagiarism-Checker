from __future__ import division
import nltk
import string
import sys
import glob
import os
import shutil
import errno
import codecs
from nltk.stem import PorterStemmer

from nltk.util import ngrams
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from nltk.stem import WordNetLemmatizer
path= 'C:/Python27/corp/*.txt'
files = glob.glob(path)
i=len(files)


while i!=0:
    x=i
    def inputfile(path):
        
        for names in files:
            try:
                f=open("C:/Python27/corp/{0}.txt".format(x),"r")
                text =f.read()
                
            except UnicodeDecodeError:
                    reload(sys)
                    sys.setdefaultencoding('utf-8')
            
            return text
            
    
    text1=open("al.txt","r").read()
    text1=text1.lower()
    text2=inputfile(path)
    text2=text2.lower()
       
    def pre_processing(text):
        sent_tokenize_list = sent_tokenize(text)
        #print sent_tokenize_list
        #print len(sent_tokenize_list)
        #tokenise words
        #print stop_words
        words=word_tokenize(text)
        stop_words = str(stopwords.words('english'))
        alpha=stop_words.replace("u'", "")
    #print words
        result = []
    #print alpha
    #remove stop words
        for item in words:
            if item not in alpha:
                result.append(item)
    #print "Filtered",result
        fil=str(result)
    #remove punctuation
        repstr=" " * 32
        table=string.maketrans(string.punctuation,repstr)
        s=fil.translate(table)
    #return s


    #lemmatizing
        lemmatizer=WordNetLemmatizer()
        h=lemmatizer.lemmatize(s)
    #print "Lemma",lemmatizer.lemmatize(s)
    #stemming
        wordss=word_tokenize(h)
        ps=PorterStemmer()
        list1=[]
        for i in wordss:
            k=(ps.stem(i))
            list1.append(k)
    #print list1
        final= '  '.join(list1)
        finall=str(final)
        return finall

    def plagcheck(text1,text2):
        tex1=pre_processing(text1)
        tex2=pre_processing(text2)
        n=3
        trigrams1 = list(ngrams(tex1.split(), n))
        trigrams2 = list(ngrams(tex2.split(), n))
    #print trigrams1
    #print trigrams2
        def compare(trigrams1, trigrams2):
            common=[]
            for gram in trigrams1:
                if gram in trigrams2:
                    common.append(gram)
            return common
        a=compare(trigrams1,trigrams2)
        print "SIMILARITY",a
        print "intersection",len(a)
        print "ref file",len(trigrams1)
        print "Ratio",len(a)/len(trigrams1)
    
    plagcheck(text1,text2)
    i=i-1
