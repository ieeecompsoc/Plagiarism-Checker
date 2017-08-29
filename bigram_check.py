from __future__ import division
import nltk
import string
import glob
import os
import sys

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
        """returns text from file {0}.txt

        :param path: C:/Python27/corp/*.txt
        :type path: str
        :returns: *.txt.read()
        :rtype: str


        """
        for names in files:
            try:
                f=open("C:/Python27/corp/{0}.txt".format(x),"r")
                text =f.read()
                
            except UnicodeDecodeError:
                    reload(sys)
                    sys.setdefaultencoding('utf-8')
            
            return text
            
    
    text1=open("A.txt","r").read()
    text1=text1.lower()
    text2=inputfile(path)
    text2=text2.lower()
       
    def pre_processing(text):
        """ returns pre-processed text in text{0}

        :param text: text1
        :type text: str
        :returns: finall
        :rtype: str


"""
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

    def plagcheck(textt1,textt2):
        """returns Similarity between reference document al.txt and test document {0}.txt(Bigrams)
        returns Intersection of Bigrams between documents and the ratio of Plagiarism by Bigram-matching
        :param textt1: text1
        :param textt2: text2
        :type textt1: str
        :type textt2: str
        :returns: a --output of compare(bigramss1,bigramss2)
        :rtype: list




"""
        tex1=pre_processing(textt1)
        tex2=pre_processing(textt2)
        n=2
        bigrams1 = list(ngrams(tex1.split(), n))
        bigrams2 = list(ngrams(tex2.split(), n))
    #print bigrams1
    #print bigrams2
        def compare(bigramss1, bigramss2):
            
            """returns bigrams of text using ngram(text.split(),2)
            :param bigrams1: bigrams1
            :param bigrams2: bigrams2
            :type bigrams1: list
            :type bigrams2: list
            :returns: common
            :rtype: list
            """
            
            common=[]
            for gram in bigramss1:
                if gram in bigramss2:
                    common.append(gram)
            return common
        a=compare(bigrams1,bigrams2)
        print "SIMILARITY",a
        print "intersection",len(a)
        print "ref file",len(bigrams1)
        print "Ratio",len(a)/len(bigrams1)
    
    plagcheck(text1,text2)
    i=i-1
