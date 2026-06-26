import joblib 
model=joblib.load("model/model.pkl")
exprience=[[7]]
prediction=model.predict(exprience)

if prediction[0]==1:
    print("Promoted")
else:
    print("Not promoted")