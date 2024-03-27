from datetime import datetime, timedelta


def addMaterials():
    global first_session, second_session, third_session, fourth_session, fifth_session
    first_session = {}
    second_session = {}
    third_session = {}
    fourth_session = {}
    fifth_session = {}

    material = input("What did you study today?").lower()
    while material:
        today = datetime.today()

        if material not in first_session:
            first_session[material] = today
            second_session[material] = today + timedelta(days=1)
        elif material not in third_session and material in second_session:
            third_session[material] = second_session[material] + timedelta(days=3)
        elif material not in fourth_session and material in third_session:
            fourth_session[material] = third_session[material] + timedelta(days=5)
        elif material not in fifth_session and material in fourth_session:
            fifth_session[material] = fourth_session[material] + timedelta(days=7)
        material = input("Anything else?")

    print(f"First sessions:\n {[(key, value.strftime('%d/%m/%y')) for key, value in first_session.items()]}\n")
    print(f"Second sessions:\n {[(key, value.strftime('%d/%m/%y')) for key, value in second_session.items()]}\n")
    print(f"Third sessions:\n {[(key, value.strftime('%d/%m/%y')) for key, value in third_session.items()]}\n")
    print(f"Fourth sessions:\n {[(key, value.strftime('%d/%m/%y')) for key, value in fourth_session.items()]}\n")
    print(f"Fifth sessions:\n {[(key, value.strftime('%d/%m/%y')) for key, value in fifth_session.items()]}\n")


def whatToReviewToday():
    today = datetime.today()
    studyList = []
    for key, value in second_session.items():
        if value == today and key not in studyList:
            studyList.append(key)
    for key, value in third_session.items():
        if value == today and key not in studyList:
            studyList.append(key)
    for key, value in fourth_session.items():
        if value == today and key not in studyList:
            studyList.append(key)
    for key, value in fifth_session.items():
        if value == today and key not in studyList:
            studyList.append(key)
    if studyList == []:
        return "Looks like there's nothing to study today. Take a break!"
    return f"Today you need to review: {[item for item in studyList]}."
