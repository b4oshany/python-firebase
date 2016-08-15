import datetime

from firebase.firebase import FirebaseApplication, FirebaseAuthentication


if __name__ == '__main__':
    SECRET = 'ITC50GuznzevQBgZnOd3GPWtos2YkU0WrzS7ta7Z'
    DSN = 'https://driquizo.firebaseio.com/'
    EMAIL = 'b4.oshany@gmail.com'
    # authentication = FirebaseAuthentication(SECRET,EMAIL, True, True)
    firebase = FirebaseApplication(DSN, None)

    snapshot = firebase.get('/quizzes', None,
                 params={'print': 'pretty'},
                 headers={'X_FANCY_HEADER': 'very fancy'})
    print snapshot

    # data = {'name': 'Ozgur Vatansever', 'age': 26,
    #         'created_at': datetime.datetime.now()}

    # snapshot = firebase.post('/quizzes', data)
    # print(snapshot)

    def callback_get(response):
        with open('/dev/null', 'w') as f:
            f.write(response)

    firebase.get_async('/quizzes', snapshot, callback=callback_get)

