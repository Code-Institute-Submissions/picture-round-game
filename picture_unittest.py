import unittest
import json

USER_FILE_NAME = "user_data.json"
questions_answers_file = "questions_answers.json"

class Picture(unittest.TestCase):
    
    def test_question(self):
        self.assertEqual('treasure island'.lower(), 'treasure island')
        self.assertEqual('batman'.lower(), 'batman')
        self.assertEqual('charlottes web'.lower(), 'charlottes web')
        self.assertEqual('jungle book'.lower(), 'jungle book')
        self.assertEqual('arabian nights'.lower(), 'arabian nights')
        self.assertEqual('king solomons mines'.lower(), 'king solomons mines')
        
    def test_question_islower(self):
        self.assertTrue('treasure island'.islower())
        self.assertTrue('batman'.islower())
        self.assertTrue('charlottes web'.islower())
        self.assertTrue('jungle book'.islower())
        self.assertTrue('arabian nights'.islower())
        self.assertTrue('king solomons mines'.islower())
        self.assertFalse('TREASURE ISLAND'.islower())
        self.assertFalse('BATMAN'.islower())
        self.assertFalse('CHARLOTTES WEB'.islower())
        self.assertFalse('JUNGLE BOOK'.islower())
        self.assertFalse('ARABIAN NIGHTS'.islower())
        self.assertFalse('KING SOLOMONS MINE'.islower())
    
    def test_question_split(self):
        one = 'treasure island'
        two = 'charlottes web'
        three = 'jungle book'
        four = ' arabian nights'
        five = 'king solomons mines'
        self.assertEqual(one.split(), ['treasure', 'island'])
        self.assertEqual(two.split(), ['charlottes', 'web'])
        self.assertEqual(three.split(), ['jungle', 'book'])
        self.assertEqual(four.split(), ['arabian', 'nights'])
        self.assertEqual(five.split(), ['king', 'solomons', 'mines'])
        with self.assertRaises(TypeError):
            one.split(2)
            two.split(2)
            three.split(2)
            four.split(2)
            five.split(3)
    
    def test_user(self):
        self.assertEqual("bob".lower(), "bob")    
        self.assertEqual("bob".upper(), "BOB")
    
    def test_user_input(self):
        self.assertTrue("bob".islower())
        self.assertFalse("BOB".islower())
        # self.assertFalse("bob1".islower()) didn't pass
        # self.assertFalse("bob!".islower()) didn't pass
    
    def user(self, username):
        with open(USER_FILE_NAME, "r+") as user_data:
            all_user_dicts = json.load(user_data)
            print("all_user_dicts", all_user_dicts, )
            print("username", username)
            for dict in all_user_dicts:
                if dict["name"] == username:
                    return dict
        
            return ""
    
    
if __name__ == '__main__':
    unittest.main()
