import random

def gene_cb():
    """Gera um gene válido para o problema das caixas binárias
    
    Return:
      Um valor zero ou um.
    """
    lista = [0, 1]
    gene = random.choice(lista)
    return gene


def individuo_cb(n):
    """Gera um individuo para o problema das caixas binárias.
    
    Args:
      n: número de genes do indivíduo.
    
    Return:
       Uma lista com n genes. Cada gene é um valor zero ou um.
    """
    individuo = []
    for i in range(n):
        gene = gene_cb()
        individuo.append(gene)
    return individuo


def funcao_objetivo_cb(individuo):
    """Computa a função objetivo no problema das caixas binárias.
    
    Args:
      individiuo: lista contendo os genes das caixas binárias
    
    Return:
      Um valor representando a soma dos genes do individuo.
    """
    return sum(individuo)

def populacao_cb(tamanho, n):
    """Cria uma população no problema das caixas binárias.
    
    Args:
        tamanho: tamanho da população
        n: número de genes de um indivíduo
    
    Returns:
        Uma lista onde cada item é um indivíduo. Um indivíduo é uma lista com n genes.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cb(n))
    return populacao

def selecao_roleta_max(populacao, fitness):
    """Seleciona indivíduos de uma população usando o método da roleta
    
    Nota: apenas funciona para problemas de maximização
    
    Args:
        população: lista com todos os indivíduos da população.
        fitness: lista com o valor da funcao objetivo dos indivíduos da população.
        
    Returns:
    População dos indivíduos selecionados.   
    """
    populacao_selecionada = random.choices(populacao, weights=fitness, k=len(populacao))
    return populacao_selecionada
    
def funcao_objetivo_pop_cb(populacao):
    """Calcula a função objetivo para todos os membros de uma população
    
    Args:
        população: lista com todos os indivíduos da população.
    
    Return: Lista de valores representando a fitness de cada indivíduo de uma população
    """
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_cb(individuo)
        fitness.append(fobj)
    return fitness

def cruzamento_ponto_simples(pai, mae):
    """Operador de cruzamento de ponto simples.
    
    Args:
        pai: uma lista representando um individuo
        mae: uma lista representando um individuo
        
    Returns:
        Duas listas, sendo que cada uma representa um filho dos pais que foram os argumentos.
    """
    ponto_de_corte = random.randint(1, len(pai) - 1)
    
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    
    return filho1, filho2

def mutacao_cb(individuo):
    """Realiza a mutação de um gene no problema das caixas binárias.
    
    Args:
        individuo: lista contendo os genes das caixas binárias.
        
    Return:
        Um valor representando a soma dos genes do individuo.
    """
    gene_a_ser_mutado = random.randint(0, len(individuo)-1)
    individuo[gene_a_ser_mutado] = gene_cb()
    return (individuo)