% Definici�n de la funci�n f(t, y)
f = @(t, y) -2 * t * y^2;

% Condiciones iniciales
t0 = 0;
y0 = 1;
tf = 2; % Tiempo final
h = 0.1; % Paso de tiempo

% M�todo de Euler
t = t0:h:tf;
y = zeros(size(t));
y(1) = y0;

for i = 1:(length(t) - 1)
    y(i+1) = y(i) + h * f(t(i), y(i));
end

% Visualizaci�n
plot(t, y);
xlabel('t');
ylabel('y');
title('Soluci�n de EDO usando M�todo de Euler');
grid on;