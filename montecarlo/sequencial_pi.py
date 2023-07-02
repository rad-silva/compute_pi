import random
import time
import math
import matplotlib.pyplot as plt

if __name__ == '__main__':
  faixa = [100000, 1000000, 10000000, 100000000]
  times = []
  
  for i in range(len(faixa)):
    start = time.time()

    n = faixa[i]
    acertos = 0

    for _ in range(n):
      x = random.random()
      y = random.random()

      if (x*x + y*y < 1):
        acertos+=1

    aprox_pi = 4 * acertos / n
    erro = math.pi - aprox_pi

    end = time.time()

    times.append(end - start)   

    print('-it %d:  n=%d' % (i, n))
    print("Aproximacao: ", aprox_pi)
    print("Tempo de execucao: ", end - start, "\n")

  plt.plot(faixa, times)
  plt.xlabel('n')
  plt.ylabel('Tempo de execução (s)')
  plt.title('Tempo de execução em função do número de pontos')
  plt.show()
