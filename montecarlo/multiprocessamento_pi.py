from multiprocessing import Pool
from multiprocessing import cpu_count
import random
import time
import math


def inside_circle(coordinate):
  x, y = coordinate
  return x**2 + y**2 < 1

if __name__ == '__main__':
  faixa = [20, 50, 100, 1000, 25000, 50000, 100000, 500000, 1000000]
  times = []

  for k in range(len(faixa)):
    start = time.time()
    
    n = faixa[k]
    acertos = 0

    x = [random.random() for i in range(n)]
    y = [random.random() for i in range(n)]

    num_processadores = cpu_count()

    # cria um objeto Pool do módulo multiprocessing e define o número
    # de processos paralelos que serão utilizados para executar as tarefas
    with Pool(num_processadores) as p:
      z = p.map(inside_circle, zip(x, y)) # aplica a função a cada elemento

    acertos = sum(z)
    aprox_pi = 4 * acertos / n
    erro = math.pi - aprox_pi

    end = time.time()

    times.append(end - start)

    print('-it:', k)
    print('n =', n)
    print("Numero de processadores disponiveis:", num_processadores)
    print("Aproximacao: ", aprox_pi)
    print("Erro: ", erro)
    print("Tempo de execucao: ", end - start, "\n")