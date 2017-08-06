from __future__ import division

import string

from plag import main_func
#from plag import *
import codecs
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.stem import PorterStemmer

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer



def pre_processing(text,flag=True):
    '''This function cleans out the unnecessary information from the text and does the required pre processing . 
    
    Pre processing steps:
	*Sentence segmentation (Seg)*
        Split text in the document into sentences and thereby allowing line-by-line processing in the subsequent tests.

	*Tokenisation (Tok)*
	Determine token (words, punctuation symbols, etc.) boundaries in sentences.

	*Lowercase (Low)*
	Substitute every uppercase letters with lowercase to generalise the matching.

	*Stop-word removal (Stop)*
	Remove functional words ( articles pronouns prepositions complementisers and determiners ) .

	*Punctuation removal (Pun)*
	Remove punctuation symbols.

	*Stemming (Stem)*
	Transform words into their stems in order to generalise the comparison analysis

	*Lemmatisation (Lem)*
	Transform words into their dictionary base forms in order to generalise the comparison analysis.

    
    :Argument1: text {string} -- text to be pre-processed
    :Argument2:	flag {bool} -- stop-word arg . (default: {True})
    
    :returns: string -- pre-processed string
    '''
    text=text.lower()
    #sent_tokenize_list = sent_tokenize(text)
    #print sent_tokenize_list
    #print len(sent_tokenize_list)
    #tokenise words
    a=stopwords.words('english')



    stop_words=set(a)

    #stop_words.append('u')
    words=word_tokenize(text)
    print words
    result = []
    #remove stop words
    if flag:
        for item in words:
            if item not in stop_words:
                result.append(item)
        #print "Filtered",result
        fil=str(result)
    else:
        result

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
    final= ' '.join(list1)
    finall=str(final)
    finallstr=''
    sanwrd = 'u'
    splitfinall = finall.split()
    for wrd in splitfinall:
        if wrd != sanwrd:
            finallstr += str(wrd)+str(' ')
    finallstr=str(finallstr)
    #print finallstr
    return finallstr






def main_method(file_list,inputFile):
    """
    This function takes a list of original files which is to be compared with input file and displays the similar text and similarity 
    score.
  
    :Argument1: file_list (list of files) -- A list of original files .
    :Argument2: inputFile (file) -- Input file which is suspected to have plagiarism
    """

    fileLastIndex=[]
    combinedFile=''
    inputText=''
    for file in file_list:
        with codecs.open(str(file), 'r', encoding='utf-8', errors='ignore') as rd:
            originalFile = rd.read()
            combinedFile= combinedFile+originalFile+'\n'
            fileLastIndex.append((len(combinedFile.split()),file))


    
    
    with codecs.open(str(inputFile), 'r', encoding='utf-8', errors='ignore') as rd:
        inputText = rd.read()

   
    main_func(inputText, combinedFile,fileLastIndex)
    



#main_method(['orig_taska.txt','g1pA_taska.txt','g2pE_taska.txt'],'g0pA_taska.txt')
