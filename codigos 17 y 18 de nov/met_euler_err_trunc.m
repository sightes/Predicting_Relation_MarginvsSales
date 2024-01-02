% Definici�n de par�metros y condiciones iniciales
t0 = 0;       % Tiempo inicial
tf = 1;       % Tiempo final
y0 = 1;       % Condici�n inicial
h = 0.1;      % Paso de tiempo

% Funci�n de la ecuaci�n diferencial y' = y
f = @(y) y;

% Inicializaci�n de variables
t = t0:h:tf;
y_euler = zeros(size(t));
y_exact = zeros(size(t));
y_euler(1) = y0;
y_exact(1) = y0;

% M�todo de Euler
for i = 1:length(t)-1
    y_euler(i+1) = y_euler(i) + h * f(y_euler(i));
    y_exact(i+1) = exp(t(i+1));
end

% C�lculo del error de truncamiento
truncation_error = abs(y_exact - y_euler);

% Visualizaci�n
plot(t, y_euler, 'b-o', t, y_exact, 'r-*');
legend('Soluci�n Euler', 'Soluci�n Exacta');
xlabel('Tiempo (t)');
ylabel('y');
title('Comparaci�n entre M�todo de Euler y Soluci�n Exacta');
grid on;

% Visualizaci�n del error de truncamiento
figure;
plot(t, truncation_error, 'k-x');
xlabel('Tiempo (t)');
ylabel('Error de Truncamiento');
title('Error de Truncamiento en el M�todo de Euler');
grid on;