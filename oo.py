# Create your classes here

class Student:
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question:
    def __init__(self, question, correct_answer): 
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluete(self):        
        
        print(self.question)
        user_answer = input("Answer:")

        if user_answer == self.correct_answer:
            return True
        else:
            return False   

class Exam:
    def __init__(self, exam_name):        
        self.questions_list = []  
        self.exam_name = exam_name

    def add_question(self, question):
        self.questions_list.append(question)

    def administer(self):
        score = 0

        for object_question in self.questions_list: 
            question_call = object_question.ask_and_evaluete()

            if question_call == True:
                score +=1

        total_questions = len(self.questions_list)

        return score/total_questions       


# new_student = Student("Suelen", "Matos", "4865 edge")
# print(new_student.first_name, new_student.last_name, new_student.address)

question1 = Question('What is the method for adding an element to a set?', '.add()')
question2 = Question('What does pwd stand for?','print working directory')
# print(question1.question, question1.correct_answer)
# print(question2.question, question2.correct_answer)

# question1.ask_and_evaluete()

process_exam = Exam("Math")
process_exam.add_question(question1)
process_exam.add_question(question2)
result = process_exam.administer()
print(f" Your result is : {result}")
