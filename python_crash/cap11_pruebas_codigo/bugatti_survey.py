from survey import AnonymousSurvey

# Define una pregunta y hace una encuesta.
question = "What color is your Bugatti?"
my_survey = AnonymousSurvey(question)

# Muestra la pregunta y guarda las respuuestas a la pregunta.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Color: ")
    if response == 'q':
        break
    my_survey.store_response(response)


# Muestra los resultdos de la encuesta.
print("\nThank you to every G for participating in the Bugatti survey!")
my_survey.show_results()