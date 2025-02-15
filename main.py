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

    def inicialize(self,w):
        self.tape = ['$']
        for c in w:
            self.tape.append(c)
        self.tape.append('?')
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


    def showTape(self):
        for e in self.tape:
            if e != '?':
                print(e,end='')

    def process(self,idx = 0,s = None):
        if s == None:
            s = self.q0
        
        if s in self.QREJ:
            return False
        elif s in self.QACC:
            return True
        
        if idx == len(self.tape):
            self.tape.append('?')
        
        c = self.tape[idx]
        t = self.TR[s]
        aux = False
        for k in t:
            if k[0] == c:
                aux = True
                self.tape[idx] = k[1]
                idx = idx + (1 if k[2] == 'R' else -1)
                s = k[3]
                break
        
        if not aux:
            return False
        return self.process(idx,s)
            
        
    def eval(self):
        for w in self.words:
            self.inicialize(w)
            print(f"{w}: {"YES" if self.process() else "NO"} | ",end='')
            self.showTape()
            print()
        
def main(args):
    assert os.path.exists(args), "Arquivo especificado nao existe."
    m = TM(args)
    m.showTM()
    m.eval()
    

if __name__ == "__main__":
    assert len(sys.argv) != 1, "Arquivo de entrada nao especificado."
    main(sys.argv[1])