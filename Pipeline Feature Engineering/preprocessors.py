import numpy as np
import pandas as pd

# Din sklearn.base se importa doua clase de baza:
# 1. BaseEstimator - ce contine metodele get_params() pentru citirea parametrilor si set_params(**params) pentr usetarea unor parametri
# 2. TransformerMixin - ce contine metoda fit_transform(X,y,**params) pentru determinarea parametrilor si aplicarea transformarii asupra datelor
from sklearn.base import BaseEstimator, TransformerMixin


# Convertorul ce transforma valorile caracteristicilor cu valori ale timpului(ani) specificate ca parametru de intrare
# in valori ale duratei de timp ce reprezinta diferenta dintre valoarea caracteristicii de referinta specificata al doilea parametru de intrare
# si valoarea curenta
class TemporalVariableTransformer(BaseEstimator, TransformerMixin):

    def __init__(self, variables, reference_variable):
        
        if not isinstance(variables, list):
            raise ValueError('variables trebuie sa fie o lista de denumiri a caracterristicilor ce au drept valori ani')
        
        self.variables = variables # o lista de caracteristici cea au valori ale timpului
        self.reference_variable = reference_variable # o caracteristica ce are valore a timpului

    def fit(self, X, y=None):
        # aceasta metodea este necesara pentru a determina parametrii in pipeline
        return self

    def transform(self, X):

    	# se realizeaza o copie a setului de date
        X = X.copy()

        # in setul de date X se substitie valorile caracteristicilor din lista cu diferenta dintre timpul de referinta si valoarea curenta
        for feature in self.variables:
            X[feature] = X[self.reference_variable] - X[feature]

        return X


# Un transformator ce substiuie toate valorile caracteriticilor categoriale ordinale specificate ca parametru de intrare
# cu valorile numerice corespunzatoare din dictionarul specificat ca al doilea parametru
class Mapper(BaseEstimator, TransformerMixin):

    def __init__(self, variables, mappings):

        if not isinstance(variables, list):
            raise ValueError('variables trebuie sa fie o lista de denumiri a caracteristicilor')

        self.variables = variables
        self.mappings = mappings

    def fit(self, X, y=None):
        # aceasta metodea este necesara pentru a determina parametrii in pipeline
        return self

    def transform(self, X):
        # se realizeaza o copie a setului de date
        X = X.copy()

        # in setul de date X se substitie valorile caracteristicilor cu valorile dictionarului corespunzatoare cheii respective
        for feature in self.variables:
            X[feature] = X[feature].map(self.mappings)

        return X