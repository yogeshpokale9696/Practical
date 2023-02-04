import pandas as pd
# import decision tree classifier
import pydotplus
from six import StringIO
from IPython.display import Image
from sklearn.tree import DecisionTreeClassifier, export_graphviz
# import train test fnction
from sklearn.model_selection import train_test_split
from sklearn import metrics, tree, __all__
from sklearn.datasets import make_classification
from sklearn import  preprocessing



data =pd.read_csv("golf_df.csv")
print(data.head())
df = pd.DataFrame(data)
print("dataframe is:",df)
feature_cols = list(df[[ 'Outlook' ,'Temperature', 'Humidity' , 'Windy']])

label1 = preprocessing.LabelEncoder()
df=df.apply(label1.fit_transform)
print(label1)
print("column headers :",feature_cols)

X = df.drop('Play', axis=1)
y = df['Play']
print(X)
print(y)

# X,y =make_classification(100,4,n_classes=2,shuffle=True, random_state=1)
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.8,test_size=0.2,shuffle=True,random_state=1)
clf  = DecisionTreeClassifier()

clf1 = clf.fit(X_train,y_train)
print("clf is:", clf1)
y_pred = clf.predict(X_test)
print(y_pred)

Accuracy = metrics.accuracy_score(y_test,y_pred)
print("Accuracy is : ", Accuracy*100)
print("confusion matrix",y_test,y_pred)

Q=input("\Select Outlook \n0.Overcast \n1.Rainy \n2.Sunny")
T=input("\Select Temperature \n0.cool \n1.hot \n2.mild")
H=input("\Select Temperature \n0.High \n1.Normal ")
W=input("\Select Temperature \n0.False \n1.True ")

if(clf.predict([[Q ,T ,H ,W]])):
    print("yes , we can play")
else:
    print("no, we can not play")

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True,feature_names = feature_cols,class_names=['Yes','No'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('image2.png')
Image(graph.create_png())