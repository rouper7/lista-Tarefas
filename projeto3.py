class Tarefa:
    def __init__(self,nome,concluida=False) :
        self._nome=nome
        self._concluida=concluida

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,valor):
        if isinstance(valor,str):
            self._nome=valor
        else:
            raise ValueError("so aceito strings")
    
    @property
    def concluida(self):
        return self._concluida
    
    @concluida.setter
    def concluida(self,valor):
        if isinstance(valor,bool):
            self._concluida=valor
        else: 
            raise ValueError("somente aceitamos booleano")
    
    def marcar_como_concluida(self):
        self.concluida=True
    
class ListaDeTarefas:
    def __init__(self,tarefas=None) :
        if tarefas is None:
            self._tarefas=[]
        else:
            self._tarefas=tarefas

    @property
    def tarefas(self):
        return self._tarefas
    
    def add_tarefa(self,*nova_tarefa):
        try:
            for tarefa in nova_tarefa:
                if isinstance(tarefa,Tarefa):            
                    self.tarefas.append(tarefa)
                else:
                    print("crie uma tarefa para adicionar na ListaDeTarefas")        
        except Exception as e:
            print(f"ocorreu um erro {e}")

    def listar_tarefas(self):
        for tarefa in self._tarefas:
            if tarefa.concluida==True:                
                print(f"tarefa:{tarefa.nome} -concluida")
            else:
                print(f"tarefa:{tarefa.nome} -nao concluida")
    
    def remover_tarefa(self,nome_tarefa_excluir):
        for tarefa in self.tarefas:
            if tarefa.nome==nome_tarefa_excluir or tarefa==nome_tarefa_excluir:
                print(f"****tarefa \"{tarefa.nome}\" foi excluida****")
                self.tarefas.remove(tarefa)
                break
        else:
            print("nao existe esse nome")
                

def main():
    try:
        t1=Tarefa("lavar louca")
        t1.nome="varrer chao"
        t1.marcar_como_concluida()
        t2=Tarefa("desenhar")
        t3=Tarefa("praticar ingles")
        
        l1=ListaDeTarefas()
        
        l1.add_tarefa(t1,t2,t3)
        
               
        l1.listar_tarefas()
    
        print(f"\n\n\n")
        l1.listar_tarefas()
    except NameError as name:
        print(f"Erro:digite o nome correto pois o  {name}")
        
    except Exception as e:
        print(f"ocorreu um erro: {e}")
        

if __name__=="__main__":
    main()