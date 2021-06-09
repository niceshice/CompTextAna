import os
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from plotly import express
from glob import glob
import seaborn as sns

repo = "./Korpus/"

glob_pattern = os.path.join('Korpus_texte', '*')
files = sorted(glob(glob_pattern), key=os.path.getctime)

vec = CountVectorizer(input="filename")
X = vec.fit_transform(files)
print("X before trans", X)
X = TfidfTransformer(use_idf=True).fit_transform(X)
print("X.shape", X.shape)
print("X", X)

pca = PCA(n_components=3)
x2d = pca.fit_transform(X.toarray())
print("x2d", x2d)

x_axis = x2d[:,0]
print("x_axis", x_axis)
y_axis = x2d[:,1]
print("y_axis", y_axis)
z_axis = x2d[:,2]
print("z_axis", z_axis)

sns.scatterplot(x=x_axis, y=y_axis)

#plot = express.scatter_3d(x=x_axis,y=y_axis,z=z_axis)
#plot.show()
