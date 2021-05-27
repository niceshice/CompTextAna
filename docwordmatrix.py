import os
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from plotly import express
from glob import glob

repo = "./Korpus/"

glob_pattern = os.path.join('Korpus_texte', '*')
files = sorted(glob(glob_pattern), key=os.path.getctime)

vec = CountVectorizer(input="filename")
X = vec.fit_transform(files)
X = TfidfTransformer(use_idf=True).fit_transform(X)
print(X.shape)

pca = PCA(n_components=2)
x2d = pca.fit_transform(X.toarray())

x_axis = x2d[:,0]
y_axis = x2d[:,1]

plot = express.scatter(x=x_axis, y=y_axis)
plot.show()
