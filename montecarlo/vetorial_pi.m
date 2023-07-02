% Qualquer arquivo .m que começa com uma definição de função é um arquivo de função.
% Adicionar uma declaração sem sentido ao topo transforma em um script.
0;

function aprox_pi = pi_aprox_paralelo(n)
  acertos = 0;
  tic;

  vec_x = rand(1, n);
  vec_y = rand(1, n);

  z = (vec_x.*vec_x + vec_y.*vec_y < 1);

  acertos = sum(z);

  aprox_pi = 4 * acertos / n;

  toc;


  clf; % Limpa a figura atual

  % plot da 1/4 circunferencia
  t = linspace(0, pi/2, 100);
  x = cos(t);
  y = sin(t);
  plot(x, y, 'LineWidth', 2, 'Color', 'red');

  % plot do retângulo de lado 1
  h = rectangle ("Position", [0, 0, 1, 1]);
  set(h, 'LineWidth', 2, 'EdgeColor', 'green');
  axis equal;

  hold on; % Mantem o gráfico atual

  % Plotar os pontos dentro do retângulo
  scatter(vec_x, vec_y, 'filled');

endfunction


% Código de teste
disp("\n--Versão paralela--")
faixa = [20, 50, 100, 1000, 25000, 50000, 100000, 500000, 1000000];

for i= 1:length(faixa)
  n = faixa(i);

  disp(["## it ", num2str(i), ": ", "n=", num2str(n)])
  pi_aprox = pi_aprox_paralelo(n);
  erro = pi - pi_aprox;
  disp(["Aproximacao: ", num2str(pi_aprox)])
  disp(["Erro: ", num2str(erro)])
  disp(" ");
 end

