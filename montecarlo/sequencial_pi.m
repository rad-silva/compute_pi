% Qualquer arquivo .m que começa com uma definição de função é um arquivo de função.
% Adicionar uma declaração sem sentido ao topo transforma em um script.
0;

function pi_aprox = pi_aprox_sequencial(n)
  acertos = 0;
  vector_x = [];
  vector_y = [];

  tic;

  for i = 1:n
    x = rand();
    y = rand();

    % Armazena os pontos gerados para plotar posteriormente
    vector_x(i) = x;
    vector_y(i) = y;

    if (x*x + y*y < 1)
      acertos = acertos + 1;
    end
  end

  pi_aprox = 4 * acertos / n;

  toc;


  %clf; % Limpa a figura atual

  % plot da 1/4 circunferencia
  %t = linspace(0, pi/2, 100);
  %x = cos(t);
  %y = sin(t);
  %plot(x,y);

  % plot do retângulo de lado 1
  %h = rectangle ("Position", [0, 0, 1, 1]);
  %axis equal;

  %hold on; % Mantem o gráfico atual

  % Plotar os pontos dentro do retângulo
  %scatter(vector_x, vector_y, 'filled');

end


% Código de teste
disp("\n--Versão iterativa--")
faixa = [20, 50, 100, 1000, 25000, 50000, 100000, 500000, 1000000];

for i = 1:length(faixa)
  n = faixa(i);

  disp(["## it ", num2str(i), ": ", "n=", num2str(n)])
  pi_aprox = pi_aprox_sequencial(n);
  erro = pi - pi_aprox;
  disp(["Aproximacao: ", num2str(pi_aprox)])
  disp(["Erro: ", num2str(erro)])
  disp(" ");
 end

