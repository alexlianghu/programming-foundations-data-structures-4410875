user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}


def update_preferences(user_pref):
    tmpDict = user_pref.copy()
    for key, value in user_pref.items():
        if value is None:
            del (tmpDict[key])
    return tmpDict

def update_preferences2(user_pref):
    tmpDict = {}
    for key, value in user_pref.items():
        if value is not None:
            tmpDict[key] = value
    return tmpDict


def update_preferences3(user_pref):
    tmpDict = {key: value for key, value in user_pref.items() if value is not None}
    return tmpDict

print(f'option 1 : {user_preferences}  --> {update_preferences(user_preferences)}')
print(f'option 2 : {user_preferences}  --> {update_preferences2(user_preferences)}')
print(f'option 3 : {user_preferences}  --> {update_preferences3(user_preferences)}')