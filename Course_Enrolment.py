import random as ran
class Environment(object):
    def __init__(self):
        # Randomly assign grades for the student from 0 to 10
        self.grade_course1 = ran.randint(0,10)
        self.grade_course2 = ran.randint(0,10)
        self.grade_course3 = ran.randint(0,10)
        self.grade_course4 = ran.randint(0,10)
        print("Your Grades for Course 1: ",self.grade_course1,"\n",
              "Your Grades for Course 2: ",self.grade_course2,"\n",
              "Your Grades for Course 3: ",self.grade_course3,"\n",
              "Your Grades for Course 4: ",self.grade_course4,"\n",
              )

class courseEnrolmentAgent(Environment):
    def __init__(self,environment):
        if(environment.grade_course1 >5 and
        environment.grade_course2 >5 and
        environment.grade_course3 >5 and
        environment.grade_course4 >5) :
            print("You may enrol for Course 5 and 6")
        else:
            print("You need to pass courses 1 to 4 to enrolment to course 5 and course 6.")

env = Environment()
courseAgent = courseEnrolmentAgent(env)

