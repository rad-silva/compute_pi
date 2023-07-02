# Para executar o programa você pode executar o seguindo comando no linux ou usando o WSL no windows
# mpiexec -n 4 python3 script.py
#
# Pode ser útil salvar o resultado em um arquivo de texto, para isso utilize
# mpiexec -n 4 python3 script.py > caminho/arquivo.txt
#
# *Atualize o caminho em que o gráfico do tempo de execução em função de n será salvo

from mpi4py import MPI
import numpy as np
import time
import matplotlib.pyplot as plt

path_graph = '/mnt/c/Users/radsi/Graduacao/EnC/Perfil7/Arquitetura/pi_aprox/montecarlo/arquivo.png'

comm = MPI.COMM_WORLD  # 
rank = comm.Get_rank() # 
size = comm.Get_size() # nro de processadores

n_por_rank = [25000, 250000, 2500000, 25000000]
timers = []

for i in range(len(n_por_rank)):
  n = size * n_por_rank[i]
  tot_inside_circle = 0    

  # Cria vetores com valores <=1 aleatórios para x e y
  if rank == 0:
    data_x = np.random.rand(1, n)
    data_y = np.random.rand(1, n)
  else:
    data_x = None
    data_y = None

  # Cria vetores locais que irão receber parte dos vetores de dados
  local_data_x = np.empty(n_por_rank[i])
  local_data_y = np.empty(n_por_rank[i])

  # Distribui partes do vetor para cada nó
  comm.Scatter(data_x, local_data_x, root=0)
  comm.Scatter(data_y, local_data_y, root=0)


  start = time.time()

  # Atribui o valor 1 caso o ponto esteja dentro do circulo
  point_inside_circle = (local_data_x ** 2 + local_data_y ** 2) < 1
  count_points_inside_circle = np.sum(point_inside_circle)

  # Reduz a soma dos pontos dentro do círculo para o nó raiz
  tot_inside_circle = comm.reduce(count_points_inside_circle, MPI.SUM, root=0)

  end = time.time()
  time_execution = end - start


  # Coleta os tempos de processamento de todos os nós no nó raiz
  times_execution_rank = comm.gather(time_execution, root=0)

  if rank == 0:
    # calcula o maior tempo de execução dentre todos os nós
    max_time = max(times_execution_rank)
    timers.append(max_time)

    pi = 4 * tot_inside_circle / n

    print("-it %d:  n=%d" % (i, n))
    print("Numero de nos", size)
    print("Aproximacao obtida: ", pi)
    print("Tempo de execucao: %.8f" % max_time)
    print()
  
if rank == 0:
  plt.plot(n_por_rank, timers)
  plt.xlabel('n')
  plt.ylabel('Tempo de execução (s)')
  plt.title('Tempo de execução em função do número de pontos')
  plt.savefig(path_graph)


 