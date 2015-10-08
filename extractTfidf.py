import os.path
import nltk.stem
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import csv

DIR='Data/'
posts=[open(os.path.join(DIR,f)).read() for f in os.listdir(DIR)]

#vectorizer=CountVectorizer(min_df=1,stop_words='english')

english_stemmer=nltk.stem.SnowballStemmer('english')
class StemmedCountVectorizer(CountVectorizer):
    def build_analyzer(self):
        analyzer=super(StemmedCountVectorizer,self).build_analyzer()
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))
vectorizer=StemmedCountVectorizer(min_df=1,stop_words='english')

x_train=vectorizer.fit_transform(posts)
num_samples,num_features=x_train.shape
#print("#samples:%d, #features:%d" % (num_samples,num_features)) 

#print (vectorizer.get_feature_names())



class StemmedTfidfVectorizer(TfidfVectorizer):
    def build_analyzer(self):
        analyzer=super(StemmedTfidfVectorizer,self).build_analyzer()
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc)) 
        
vectorizer2=StemmedTfidfVectorizer(min_df=1,stop_words='english',decode_error='ignore')
x_train=vectorizer2.fit_transform(posts)
num_samples,num_features=x_train.shape
#print("#samples:%d, #features:%d" % (num_samples,num_features)) 
#print (vectorizer2.get_feature_names())

feature_names=vectorizer2.get_feature_names()
dense =x_train.todense()


files=['goodrtl-parkin-1','m2s_som_ha','MYA_VOL2_v1']
def writeScore2csv(filename,index,dense,feature_names):
    episode = dense[index].tolist()[0]
    phrase_scores = [pair for pair in zip(range(0, len(episode)), episode) if pair[1] > 0]
    sorted_phrase_scores = sorted(phrase_scores, key=lambda t: t[1] * -1)
    with open('Data/{0}.csv'.format(filename),'wb') as csvfile:
        writekeywords=csv.writer(csvfile)
        for phrase, score in [(feature_names[word_id], score) for (word_id, score) in sorted_phrase_scores][:100]:
            print('{0: <100} {1}'.format(phrase, score))
            writekeywords.writerow([phrase,score])

for filename in files:
    writeScore2csv(filename,files.index(filename),dense,feature_names)       