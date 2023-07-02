% Qualquer arquivo .m que começa com uma definição de função é um arquivo de função.
% Adicionar uma declaração sem sentido ao topo transforma em um script.
0;

function [aprox_pi, duration] = pi_aprox_paralelo(n)
  start = tic;

  vet = 0:n;

  soma = sum((-1).^vet ./ (2.*vet + 1));
  aprox_pi = 4 * soma;

  duration = toc(start);
endfunction


%
% Código de teste
disp("\n--Versão paralela--")
faixa = [20, 50, 100, 1000, 25000, 50000, 100000, 500000, 1000000, 10000000];
times = zeros(size(faixa));

for i= 1:length(faixa)
  n = faixa(i);
  [pi_aprox, time_duration] = pi_aprox_paralelo(n);
  times(i) = time_duration;

  disp(["## it ", num2str(i), ": ", "n=", num2str(n)])
  disp(["Aproximacao: ", num2str(pi_aprox)])
  disp(["Tempo de execucao: ", num2str(time_duration)])
  disp(" ");
end

plot(faixa, times);
xlabel('n');
ylabel('Tempo (s)');
title('Tempos de execução em relação a n');

