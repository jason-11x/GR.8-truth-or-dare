import os
import random
import array
import json
import time
def changeQuestions(which_question,new_data,filename):
	with open(filename,'r+') as f:
		data = json.load(f)


		data[which_question] = new_data
	with open(filename,'w') as f:
		json.dump(data,f,indent=4)
	return

def getData(whichOne,filename):
	with open(filename,'r+') as f:
		data = json.load(f)
		return data[whichOne]

changeQuestions("random",True,"questions.json")
truth = ["mom or dad","your worst friend is: ","can you help code me?"]
dare = ["Un-subscribe to a Youtuber","say hello in 10 languages. no google","You got no dare YAY"]
	#the truth or dare
print("Booting code.")
time.sleep(1)
print("Grabbing data.")
time.sleep(1)
print("Done. Have fun :D")
time.sleep(1)
print("This is Truth or Dare! v8.1.0")
print("Now you can ask a DARE and TRUTH question to next player")
print("If you want to copy this code and say you code it, sure? I don't know why you want to do this.\n")
time.sleep(2)
while True:

	print("This is Truth or Dare! v8.1.0")
	print("Now you can ask a DARE and TRUTH question to next player")
	print("If you want to copy this code and say you code it, sure? I don't know why you want to do this.\n")
	time.sleep(1)
	truthOrDare=input("Truth or Dare ")
	noAnswer = getData("random", "questions.json")
	print("\nGetting question. Please wait")
	time.sleep(1)
	if truthOrDare.lower().startswith("t"):

		truthQuestionStored = getData("truth","questions.json")
		if noAnswer:
			print("Here is your TRUTH question: "+random.choice(truth))
		elif not noAnswer:
			print("Here is the TRUTH question from the last player: "+truthQuestionStored)
		input("Press ENTER if you answered the TRUTH")

	elif truthOrDare.lower().startswith("d"):
		dareQuestionStored = getData("dare","questions.json")
		if noAnswer:
			print("Here is your DARE question: "+random.choice(dare))
		elif not noAnswer:
			print("Here is the DARE question from the last player: "+dareQuestionStored)
		input("Press ENTER if you answered the DARE")

	#next question
	changeQuestions("random",False,"questions.json")
	nextQuestionAnswer = input("Do you want to give the truth or dare question for the next player?(y/n) ")
	if nextQuestionAnswer.lower() == "y":
		dareQuestion = input("What is your DARE for the next player? ")
		changeQuestions("dare",dareQuestion,"questions.json")
		truthQuestion = input("What is your TRUTH for the next player? ")
		changeQuestions("truth", truthQuestion, "questions.json")

	else:
		changeQuestions("random",True,"questions.json")
	print("Thank you for playing Truth Or Dare v8.1.0")
	time.sleep(1)
	print("I hope you enjoy this game! Bye <3")
	time.sleep(3)
	os.system('clear')
