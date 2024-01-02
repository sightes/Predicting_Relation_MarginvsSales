% Fuentes del Ruido en los Datos: Simulación en MATLAB

% Parámetros de simulación
N = 1000;  % Número de muestras
t = linspace(0, 10, N);  % Tiempo

% Datos sin ruido
datos_puros = sin(2 * pi * 0.5 * t);

% Ruido Interno
% Error de medición
ruido_medicion = 0.05 * randn(size(t));

% Error de procesamiento (aproximación)
ruido_procesamiento = 0.05 * sin(2 * pi * 0.5 * t + 0.5);

% Error de cuantificación
datos_cuantificados = round(datos_puros * 10) / 10;

% Ruido Externo
% Interferencias
ruido_interferencia = 0.1 * cos(2 * pi * 10 * t);

% Perturbaciones ambientales
ruido_ambiental = 0.1 * rand(size(t));

% Ruido humano (simulado como un error aleatorio en algunos puntos)
indices_error = randi([1 N], 1, 10);
ruido_humano = zeros(size(t));
ruido_humano(indices_error) = 0.5 * (rand(size(indices_error)) - 0.5);

% Combinando los datos puros con los diferentes tipos de ruido
datos_ruidosos = datos_puros + ruido_medicion + ruido_procesamiento + ...
                 datos_cuantificados + ruido_interferencia + ...
                 ruido_ambiental + ruido_humano;

% Visualización
figure;
subplot(2, 1, 1);
plot(t, datos_puros, 'b', 'LineWidth', 1.5);
title('Datos Sin Ruido');
xlabel('Tiempo');
ylabel('Amplitud');

subplot(2, 1, 2);
plot(t, datos_ruidosos, 'r', 'LineWidth', 1.5);
title('Datos con Ruido (Interno y Externo)');
xlabel('Tiempo');
ylabel('Amplitud');
