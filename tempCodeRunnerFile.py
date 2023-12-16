if __name__ == "__main__":
	while True:
		# sentence = "do you use credit cards?"
		sentence = input("You: ")
		if sentence == "quit":
			break
		if sentence == "reset":
			Reset_data()
			continue
		list = Get_Input(sentence)
		print(Read_Input(list))