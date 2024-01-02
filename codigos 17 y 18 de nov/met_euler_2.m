% Definici�n de par�metros y condiciones iniciales
m = 1;        % Masa
t0 = 0;       % Tiempo inicial
tf = 10;      % Tiempo final
x0 = 0;       % Condici�n inicial para x
v0 = 1;       % Condici�n inicial para v (x')
h = 0.01;     % Paso de tiempo

% Definici�n de la funci�n F(t, x, v)
F = @(t, x, v) -9.81 * m;  % Por ejemplo, una fuerza gravitacional

% Inicializaci�n de variables
t = t0:h:tf;
x = zeros(size(t));
v = zeros(size(t));
x(1) = x0;
v(1) = v0;

% M�todo de Euler para resolver el sistema de ecuaciones
for i = 1:(length(t)-1)
    v(i+1) = v(i) + h * F(t(i), x(i), v(i)) / m;
    x(i+1) = x(i) + h * v(i);
end

% Visualizaci�n
plot(t, x);
xlabel('Tiempo (t)');
ylabel('Posici�n (x)');
title('Soluci�n de la Segunda Ley de Newton usando el M�todo de Euler');
grid on;
