class Environment:
    def __init__(self):
        self.QA = {
            "what is the name of your company" : "Rawdata",
            "what is the name of the CEO" : "Chacko Cherian",
            "who heads the operations" : "Vineeth Menon",
            "can you send a quote" : "Please reachout to vineeth@rawdatatech.com",
        }

class simpleChatbotAgent(Environment):
    def __init__(self, environment):
        self.continueFlag = 1
        while(self.continueFlag == 1):
            self.inputQuestion = input("\nWelcome to the rawdata chatbot!\nAsk me a question...\n")
        
            if self.inputQuestion.lower() in environment.QA.keys():
                print(environment.QA[self.inputQuestion.lower()])
                self.continueFlag = int(input("Do you want to continue? 1/0"))
            else:
                print("Sorry, I do not have an answer for that, let me have an executive contact you:")
                self.enqNumber = input("Could you please leave your phone number here so that I can reach you?: ")
                self.continueFlag = int(input("Do you want to continue? 1/0: "))

env = Environment()
simpleChatbotAgent(env)