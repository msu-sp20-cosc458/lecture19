import unittest
import functions

class ChatBotResponseTest(unittest.TestCase):
    def test_not_command(self):
        response = functions.get_chatbot_response("Purple")
        self.assertEqual(response, "")
        
    def test_add_command(self):
        response = functions.get_chatbot_response("!! Hey nabin")
        self.assertEqual(response, "What's up!!")
        
    def test_add_command1(self):
        response = functions.get_chatbot_response("!! add 2 4")
        self.assertEqual(response, 6)
        
    def test_add_command2(self):
        response = functions.get_chatbot_response("!! divide 4 2")
        self.assertEqual(response, 2)
        
    def test_add_command3(self):
        response = functions.get_chatbot_response("!! say hello")
        self.assertEqual(response, "hello")
        
    def test_add_command4(self):
        response = functions.get_chatbot_response("!! blah blah")
        self.assertEqual(response, "Oops! I didn't recognize your command :(")

if __name__ == '__main__':
    unittest.main()
