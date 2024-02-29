sysdata;
Kaw = 8.1280;
T = 1;
Cpd = tf(Kc*[Ts+1 1], [1 1]);
Dpd = c2d ( Cpd, T, 'tustin' );
[nD,dD] = tfdata ( Dpd );

close all;
figure(1);
subplot(2,1,1);
set(gca,'FontSize',16);
subplot(2,1,2);
set(gca,'FontSize',16);

aT = [2 3 5];
col = 'bgr';
for i=1:length(aT)
  T = aT(i);
  Dpd = c2d ( Cpd, T, 'tustin' );
  [nD,dD] = tfdata ( Dpd, 'v' );
  sim('lab7')
  subplot(2,1,1);
  plot(phi(:,1),phi(:,3),col(i));
  hold on;
  subplot(2,1,2);
  plot(delta(:,1),delta(:,3),col(i));
  hold on; 
end

subplot(2,1,1);
plot(phi(:,1),phi(:,2),'k--');
title('Поворот на 90 градусов')
legend('T=2', 'T=3', 'T=5', 'Непрерывная система');
xlabel('Время, сек');
ylabel('\phi, град');
h = get(gca, 'Children');
for i=1:4
  set(h(i),'LineWidth',1.5);
end

subplot(2,1,2);
plot(delta(:,1),delta(:,2),'k--');
legend('T=2', 'T=3', 'T=5', 'Непрерывная система');
xlabel('Время, сек');
ylabel('\delta, град');
h = get(gca, 'Children');
for i=1:4
  set(h(i),'LineWidth',1.5);
end

print -dmeta