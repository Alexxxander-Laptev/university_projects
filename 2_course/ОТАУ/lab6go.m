sysdata
Kaw = 8.1280;
sim ('lab6')
figure(1); % открыть рис. 1
subplot(2,1,1);
set(gca,'FontSize',16);
plot(phi(:,1),phi(:,2),'b');
hold on;
plot(phi(:,1),phi(:,3),'g');
hold on;
plot(phi(:,1),phi(:,4),'r');
hold off;
title('Поворот на 30 градусов')
xlabel('Время, сек');
ylabel('\phi, град');
h = get(gca, 'Children')
set(h(1),'LineWidth',1.5)
set(h(2),'LineWidth',1.5)
set(h(3),'LineWidth',1.5)
legend('Линейная система', ...      
       'Нелинейная система', ...
       'Система с компенсацией')

subplot(2,1,2);
set(gca,'FontSize',16);
plot(delta(:,1),delta(:,2),'b');
hold on;
plot(delta(:,1),delta(:,3),'g');
hold on;
plot(delta(:,1),delta(:,4),'r');
hold off;
xlabel('Время, сек');
ylabel('\delta, град');
h = get(gca, 'Children')
set(h(1),'LineWidth',1.5)
set(h(2),'LineWidth',1.5)
set(h(3),'LineWidth',1.5)
legend('Линейная система', ...      
       'Нелинейная система', ...
       'Система с компенсацией')

print -dmeta
[si,Tpp] = overshoot(phi(:,1),...
                     phi(:,4));
