import joblib
def employee_promotion_prdication():
    model=joblib.load("model/model.pkl")
    prediction=model.predict([[8]])
    assert prediction[0]==1