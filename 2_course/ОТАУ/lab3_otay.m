figure(1);
subplot(2, 1, 1);
plot(phi(:,1),phi(:,2));
title('Курс');
xlabel('Время, сек');
ylabel('\phi, градусы');
subplot(2, 1, 2);
plot(delta(:,1),delta(:,2));
title('Угол поворота руля');
xlabel('Время, сек');
ylabel('\delta, градусы');
print -dmeta
phi0 = phi;
delta0 = delta;

subplot(2, 1, 1);
plot(phi0(:,1), phi0(:,2),...       
     phi (:,1), phi(:,2));
title('Курс');
xlabel('Время, сек');
ylabel('\phi, градусы');
legend('ПД-регулятор', ...
       'ПИД-регулятор');
subplot(2, 1, 2);
plot(delta0(:,1), delta0(:,2),...       
     delta (:,1), delta(:,2));
title('Угол перекладки руля');
xlabel('Время, сек');
ylabel('\delta, градусы');
legend('ПД-регулятор', ...
       'ПИД-регулятор');
[gm,phim] = margin(W)
gm = 20*log10(gm)
