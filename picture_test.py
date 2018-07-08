def round_one(questions_and_answers):
    questions_and_answers ={
        "picture one": "treasure island",
        "picture two": "batman",
    }
    for answer in questions_and_answers.keys():
        questions_and_answers[answer]
    if answer == "treasure island":
        print("Correct")
    else:
        return("incorrect")
    return questions_and_answers   
    
assert round_one("treasure island") == 1, "Correct"
assert round_one("batman") == 0, "incorrect" 

print("All the tests passed") 

#def round_one(picture):
#    return("False")
#assert round_one([]) == False, "No picture" 
#print("All tests passed")