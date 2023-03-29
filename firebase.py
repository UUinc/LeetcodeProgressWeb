def SetFirebaseData():
    doc_ref = db.collection(u'problems').document()
    doc_ref.set(my_data)

def GetFirebaseData(db):
    problems = []
    problems_ref = db.collection(u'problems')
    problemsList = problems_ref.stream()
    for problem in problemsList:
        problems.append(problem.to_dict())
    
    problems.sort(key= lambda item: item['date'], reverse=True)
    return problems