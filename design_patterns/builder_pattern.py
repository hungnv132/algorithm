
class Computer(object):

    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None
        self.hdd = None
        self.gpu = None

    def __str__(self):
        info = "Memory: {}GB; Hard disk: {}GB;  Graphics Card: {}".format(
            self.memory, self.hdd, self.gpu)
        return info


class ComputerBuilder(object):

    def __init__(self):
        self.computer = Computer('HNV12345678')

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, amount):
        self.computer.gpu = amount


class HardwareEngineer(object):

    def __init__(self):
        self.builder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        [step for step in (self.builder.configure_memory(memory),
                           self.builder.configure_hdd(hdd),
                           self.builder.configure_gpu(gpu))]

    @property
    def computer(self):
        return self.builder.computer


if __name__ == '__main__':
    engineer = HardwareEngineer()
    engineer.construct_computer(memory=8, hdd=500, gpu='Core i8')
    computer = engineer.computer
    print(computer)