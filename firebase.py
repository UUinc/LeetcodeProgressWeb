import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def SetFirebaseData(new_problem):
    doc_ref = db.collection(u'problems').document()
    doc_ref.set(new_problem)

def GetFirebaseData():
    problems = []
    problems_ref = db.collection(u'problems')
    problemsList = problems_ref.stream()
    for problem in problemsList:
        problems.append(problem.to_dict())
    
    problems.sort(key= lambda item: item['date'], reverse=True)
    return problems