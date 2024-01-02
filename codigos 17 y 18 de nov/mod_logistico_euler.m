% Par�metros del Modelo Log�stico
r = 0.1;   % Tasa de crecimiento
K = 500;   % Capacidad de carga
P0 = 50;   % Poblaci�n inicial

% Par�metros de la simulaci�n
T = 50;    % Tiempo total de simulaci�n
dt = 0.5;  % Paso de tiempo (h)
n = T / dt; % N�mero de pasos

% Inicializaci�n
P = zeros(n, 1); % Vector para almacenar la poblaci�n en cada paso
t = 0:dt:T-dt;   % Vector de tiempo
P(1) = P0;       % Condici�n inicial

% M�todo de Euler
for i = 1:n-1
    dP = r * P(i) * (1 - P(i) / K); % Modelo log�stico
    P(i+1) = P(i) + dP * dt;        % M�todo de Euler
end

% Visualizaci�n
plot(t, P);
xlabel('Tiempo');
ylabel('Poblaci�n');
title('Modelo Log�stico de Crecimiento de Poblaci�n');
grid on;
