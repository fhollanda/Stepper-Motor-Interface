load('C:\Users\lucas\Desktop\4eb8290c-66b5-49cc-b9dd-a6747ec87dcf.mat')
a = acquired_data

%------------------%

x = zeros(1, 2500)
x(:) = a(1,1,1,:) % a(número da captura, dimensão (tempo), quantidade de pontos) %

%------------------%

y = zeros(1, 2500)
y(:) = a(1,1,2,:) % a(número da captura, dimensão (amplitude), quantidade de pontos) %

%------------------%

plot(x,y) % remontagem de apenas uma captura %