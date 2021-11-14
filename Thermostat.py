import random

class Environment(object):
    def __init__(self):
        # Define the states of the Thermostat off as 0 and heating as 1
        thermostat_states = [0, 1]
        self.Tstate = random.choice(thermostat_states)

        # Define states of the environment - 0 = cold, 1 = comfortable, 2 = hot
        environment_states = [0, 1, 2]
        self.Envstate = random.choice(environment_states)
        if (self.Envstate == 0):
            print("The room is cold", self.Envstate)
        elif (self.Envstate == 1):
            print("The room is comfortable", self.Envstate)
        elif (self.Envstate == 2):
            print("The room is hot", self.Envstate)

        if (self.Tstate == 0):
            print("The heater is now Off",self.Tstate)
        else:
            print("The heater is now Heating", self.Tstate)


class Thermostat(Environment):
    def __init__(self, environment):
        # environment - 0 = cold, 1 = comfortable, 2 = hot
        # Thermostat off as 0 and heating as 1
        if environment.Envstate == 0 and environment.Tstate == 0:
            print("Turning on the Heater : Heating...")
        if environment.Envstate == 0 and environment.Tstate == 1:
            print("Continuing to Heat...")
        if environment.Envstate == 2 and environment.Tstate == 0:
            print("No Change...")
        if environment.Envstate == 2 and environment.Tstate == 1:
            print("Switching off")
        if environment.Envstate == 1 and (environment.Tstate == 0 or 1):
            print("Since you are comfortable, No Change")


        # Changing States:
        if environment.Envstate == 0 and environment.Tstate == 0:
            environment.Tstate = 1
        if environment.Envstate == 2 and environment.Tstate == 1:
            environment.Tstate = 0

Environ = Environment()
heatingExperiment = Thermostat(Environ)
