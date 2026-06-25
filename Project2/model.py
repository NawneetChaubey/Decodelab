from sklearn.datasets import load_iris
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,f1_score

iris = load_iris()

x = iris.data
y =iris.target

x_train , x_test , y_train , y_test = train_test_split(
    x,y,test_size=0.2,random_state=42
)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test =  scaler.fit_transform(x_test)


model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train,y_train)
model_pred = model.predict(x_test)
accuracy = accuracy_score(y_test,model_pred)

f1 = f1_score(y_test,model_pred,average="weighted")

cm = confusion_matrix(
    y_test,
    model_pred
)

def predict_species(features):
    scaled_data = scaler.transform([features])
    prediction = model.predict(scaled_data)
    return iris.target_names[prediction[0]]