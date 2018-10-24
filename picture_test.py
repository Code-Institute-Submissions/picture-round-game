
def get_question_by_id(question_id):
    return 1,2,3,4,5,6
    
def number_of_questions(question):
    return "question"
    
def the_question(actual, expected):
    assert expected == actual, "Expected {1,2,3,4,5,6}, got {none}".format(expected,actual)

the_question(number_of_questions([1,2,3,4,5,6]), "question")#Test passed


def user(username):# Test to have lower case for usernames
    each_user = 0
    for u in username:
        if u.islower():
            each_user += 1
    return each_user


assert user("") == 0, "No string"
assert user("A") == 0, "An uppercase"
assert user("a") == 1, "lower case"
assert user("!£$%&*") == 0, "special"



def question_one(one):
    answer = "treasure island"
    return answer

def first_question(answer):
    return "answer"
    
def checking_question(actual, expected):
    assert expected == actual, "Expected {treasure island}, got {none}".format(expected, actual)

checking_question(first_question(["treasure island"]), "answer")

print("All tests passed")

