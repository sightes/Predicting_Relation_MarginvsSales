% Parámetros del Modelo Logístico
r = 0.1;   % Tasa de crecimiento
K = 500;   % Capacidad de carga
P0 = 50;   % Población inicial

% Parámetros de la simulación
T = 50;    % Tiempo total de simulación
dt = 0.5;  % Paso de tiempo (h)
n = T / dt; % Número de pasos

% Inicialización
P = zeros(n, 1); % Vector para almacenar la población en cada paso
t = 0:dt:T-dt;   % Vector de tiempo
P(1) = P0;       % Condición inicial

% Método de Euler
for i = 1:n-1
    dP = r * P(i) * (1 - P(i) / K); % Modelo logístico
    P(i+1) = P(i) + dP * dt;        % Método de Euler
end

% Visualización
plot(t, P);
xlabel('Tiempo');
ylabel('Población');
title('Modelo Logístico de Crecimiento de Población');
grid on;
