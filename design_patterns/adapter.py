

class Synthesizer(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "The {} synthesizer".format(self.name)

    def play(self):
        return "is playing an electronic song"


class Human(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "{} the human".format(self.name)

    def speak(self):
        return "says hello"


class Computer(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "The {} computer".format(self.name)

    def execute(self):
        return "Execute a program"


"""
- The execute() method is the main action that the computer can perform.
This method is called by the client code. 
- The client only knows how to call the execute() method, and it has no
idea about play() or speak(). ====> Adapter to the rescue.
"""


class Adapter(object):

    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


if __name__ == "__main__":
    objects = [Computer('Dell')]

    synth = Synthesizer('moog')
    synth_adapter = Adapter(synth, dict(execute=synth.play))
    objects.append(synth_adapter)

    human = Human('Hung')
    human_adapter = Adapter(human, dict(execute=human.speak))
    objects.append(human_adapter)

    for obj in objects:
        print("{} {}".format(str(obj), obj.execute()))
