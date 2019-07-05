from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import cross_val_score
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.manifold import LocallyLinearEmbedding
from sklearn.pipeline import Pipeline
import numpy as np
import os
import pandas as pd
from sklearn.base import TransformerMixin
from joblib import dump, load
from django.conf import settings





class custom_filter(TransformerMixin):
    def __init__(self, *featurizers):
        self.featurizers = featurizers
    
    def fit_transform(self,*aa): 
        X ,y= aa[0]
        self.X = X.copy()
        self.y = y.copy()
        self.X = pd.DataFrame(self.X)
        self.y = pd.DataFrame(self.y)
        upper_part = self.X.iloc[:,2] > 0
        bottom_part = self.X.iloc[:,2] < -0.3
        self.X = self.X[upper_part | bottom_part]
        self.y = self.y[upper_part | bottom_part]
        self.fitted = True
        
        return self.X.values,self.y.values
    
    def transform(self,*aa): 
        X ,y= aa[0]
        return X,y
        
class wrapper(TransformerMixin):
    def __init__(self,transformer):
        self.transformer = transformer
    def fit_transform(self, *aa): 
        X ,y= aa[0]
        self.transformer.fit(X)
        return self.transformer.transform(X),y
    def transform(self,*aa):  
        X ,y= aa[0]
        return self.transformer.transform(X),y
    

class wrapper_clf(TransformerMixin):
    def __init__(self,clf):
        self.clf = clf
    def decision_function(self, *aa):
        X,y= aa[0]
        return self.clf.decision_function(X)
    def fit(self, *aa):
        X,y= aa[0]
        return self.clf.fit(X,y)
    def get_params(self,deep=True):
        return self.clf.get_params(deep)
    def predict(self, *aa):
        X,y= aa[0]
        return self.clf.predict(X)
    def predict_proba(self, *aa):
        X,y= aa[0]
        return self.clf.predict_proba(X)
    def score(self,*aa):
        X,y= aa[0]
        return self.clf.score(X,y)


print(__name__,'------------------------------')
tennis_ssmg = load(settings.BASE_DIR+"\\sofascore\\ml-models\\tennis_ssmg.joblib")
    


