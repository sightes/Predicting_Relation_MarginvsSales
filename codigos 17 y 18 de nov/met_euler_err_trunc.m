% Definición de parámetros y condiciones iniciales
t0 = 0;       % Tiempo inicial
tf = 1;       % Tiempo final
y0 = 1;       % Condición inicial
h = 0.1;      % Paso de tiempo

% Función de la ecuación diferencial y' = y
f = @(y) y;

% Inicialización de variables
t = t0:h:tf;
y_euler = zeros(size(t));
y_exact = zeros(size(t));
y_euler(1) = y0;
y_exact(1) = y0;

% Método de Euler
for i = 1:length(t)-1
    y_euler(i+1) = y_euler(i) + h * f(y_euler(i));
    y_exact(i+1) = exp(t(i+1));
end

% Cálculo del error de truncamiento
truncation_error = abs(y_exact - y_euler);

% Visualización
plot(t, y_euler, 'b-o', t, y_exact, 'r-*');
legend('Solución Euler', 'Solución Exacta');
xlabel('Tiempo (t)');
ylabel('y');
title('Comparación entre Método de Euler y Solución Exacta');
grid on;

% Visualización del error de truncamiento
figure;
plot(t, truncation_error, 'k-x');
xlabel('Tiempo (t)');
ylabel('Error de Truncamiento');
title('Error de Truncamiento en el Método de Euler');
grid on;