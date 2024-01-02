% Definición de parámetros y condiciones iniciales
m = 1;        % Masa
t0 = 0;       % Tiempo inicial
tf = 10;      % Tiempo final
x0 = 0;       % Condición inicial para x
v0 = 1;       % Condición inicial para v (x')
h = 0.01;     % Paso de tiempo

% Definición de la función F(t, x, v)
F = @(t, x, v) -9.81 * m;  % Por ejemplo, una fuerza gravitacional

% Inicialización de variables
t = t0:h:tf;
x = zeros(size(t));
v = zeros(size(t));
x(1) = x0;
v(1) = v0;

% Método de Euler para resolver el sistema de ecuaciones
for i = 1:(length(t)-1)
    v(i+1) = v(i) + h * F(t(i), x(i), v(i)) / m;
    x(i+1) = x(i) + h * v(i);
end

% Visualización
plot(t, x);
xlabel('Tiempo (t)');
ylabel('Posición (x)');
title('Solución de la Segunda Ley de Newton usando el Método de Euler');
grid on;
