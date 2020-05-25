import numpy
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

#loading dataset
df = pd.read_csv('excelfile.csv')
df.columns = ['name','name group','lowlevel.spectral_centroid.mean','lowlevel.spectral_centroid.max',
              'lowlevel.spectral_centroid.min','lowlevel.spectral_centroid.stdev',
              'lowlevel.spectral_flux.max','lowlevel.spectral_flux.mean','lowlevel.spectral_flux.min',
              'lowlevel.spectral_flux.stdev','lowlevel.spectral_rms.max','lowlevel.spectral_rms.mean',
              'lowlevel.spectral_rms.min','lowlevel.spectral_rms.stdev','lowlevel.spectral_spread.max',
              'lowlevel.spectral_spread.mean','lowlevel.spectral_spread.min','lowlevel.spectral_spread.stdev',
              'lowlevel.zerocrossingrate.max','lowlevel.zerocrossingrate.mean','lowlevel.zerocrossingrate.min',
              'lowlevel.zerocrossingrate.stdev','lowlevel.barkbands_flatness_db.max',
              'lowlevel.barkbands_flatness_db.mean','lowlevel.barkbands_flatness_db.min',
              'lowlevel.barkbands_flatness_db.stdev','lowlevel.erbbands_flatness_db.max',
              'lowlevel.erbbands_flatness_db.mean','lowlevel.erbbands_flatness_db.min',
              'lowlevel.erbbands_flatness_db.stdev','lowlevel.melbands_flatness_db.max',
              'lowlevel.melbands_flatness_db.mean','lowlevel.melbands_flatness_db.stdev',
              'lowlevel.melbands_flatness_db.min','centroid','effectiveduration','logattacktime.logpoint1',
              'logattacktime.logpoint2','logattacktime.logpoint3','logattacktime.decimalpoint1',
              'logattacktime.decimalpoint2','logattacktime.decimalpoint3','']

values = df.values

X = values[:,3:-1]
Y = values[:,1]

# Feature extraction
model = LogisticRegression()
rfe = RFE(model, 2)
fit = rfe.fit(X, Y)
print("Num Features: %s" % (fit.n_features_))
print("Selected Features: %s" % (fit.support_))
print("Feature Ranking: %s" % (fit.ranking_))

idxs = numpy.where(fit.support_ == True)

X_name = df.columns[3+idxs[0][0]]
Y_name = df.columns[3+idxs[0][1]]
print(X_name)
print(Y_name)

def scatterplot(df, x_dim, y_dim):
  x = df[x_dim]
  y = df[y_dim]

  fig, ax = plt.subplots(figsize=(10, 5))

  #defining an array of colors
  colors = ['red' if l == 'percussive' else 'black' if l == 'wind' else 'green' if l == 'string' else 'purple' for l in df['name group']]
  ax.scatter(x, y, alpha=0.70, color=colors)

  #adds a title and axes labels
  ax.set_xlabel(x_dim)
  ax.set_ylabel(y_dim)

  #removing top and right borders
  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)

  #adds major gridlines
  ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

  plt.show()

scatterplot(df, X_name, Y_name)
