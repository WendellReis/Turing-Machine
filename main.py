import sys
import json
import os.path

class TM:
    def __init__(self, args):
        with open(args) as arc:
            data = json.load(arc)
        self.Q = data['estados']
        self.E = data['alfabeto']
        self.T = data['simbolos']
        self.TR = data['transicoes']
        self.q0 = data['estado_inicial']
        self.QACC = data['estados_aceitacao']
        self.QREJ = data['estados_rejeicao']
        self.words = data['palavras']

    def inicialize(self):
        self.tape = ['$']
        self.index = 0
    
    def showTM(self):
        print(f"Q = {self.Q}")
        print(f"E = {self.E}")
        print(f"T = {self.T}")

        print("TR = [")
        for k in self.TR:
            print(f"\t{k}: [")
            for t in self.TR[k]:
                print(f"\t\t{t},")
            print("\t]")
        print("]")

        print(f"q0 = {self.q0}")
        print(f"QACC = {self.QACC}")
        print(f"QREJ = {self.QREJ}")


    def process(self,w,s = None):
        if s == None:
            s = self.q0
        
        

    def eval(self):
        for w in self.words:
            self.inicialize()
            print(f"{w}: {"YES" if self.process(w) else "NO"}")
        
def main(args):
    assert os.path.exists(args), "Arquivo especificado nao existe."
    m = TM(args)
    m.showTM()
    

if __name__ == "__main__":
    assert len(sys.argv) != 1, "Arquivo de entrada nao especificado."
    main(sys.argv[1])