from tqdm import tqdm

class idLooper:

    def __init__(self, operator, nextLooper=None):
        self.operator = operator
        self.nextLooper = nextLooper

    def execute(self, generator):
        return (self.operator.get_generator(i.idNo) for sub_generator in generator for i in sub_generator)
    
    def handle_request(self, generator):
        if self.nextLooper :
            result = self.nextLooper.handle_request(self.execute(generator))
            return result
        else :
            result = self.execute(generator)
            return result

class id_ptpNo_Looper:

    def __init__(self, operator, nextLooper=None):
        self.operator = operator
        self.nextLooper = nextLooper

    def execute(self, generator):
        return (self.operator.get_generator(i.idNo, i.ptpNo) for sub_generator in generator for i in sub_generator)
    
    def handle_request(self, generator):
        if self.nextLooper :
            result = self.nextLooper.handle_request(self.execute(generator))
            return result
        else :
            result = self.execute(generator)
            return result

class SavingLooper:

    def __init__(self, operator, nextLooper=None):
        self.operator = operator
        self.nextLooper = nextLooper

    def execute(self, generator):
        for sub_generator in generator :
            for i in sub_generator :
                self.operator.save_sql(i)
    
    def handle_request(self, generator):
        self.execute(generator)

