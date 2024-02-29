sysdata;
Ts0 = Ts;
aTs = linspace(0.8, 1.2, 100) * Ts0;
aSi = [];
aTpp = [];
for Ts=aTs
    sim ( 'lab5' )
    [si,Tpp] = overshoot ( phi(:,1), phi(:,2) );
    aSi = [aSi si];
    aTpp = [aTpp Tpp];
end

aSi = [aTs; aSi];
aTpp = [aTs; aTpp];

figure(1); % открыть рис. 1
subplot(2,1,1);
set(gca,'FontSize',16);
plot(aSi(1,:),aSi(2,:),'b');
hold on;
title('Влияние изменения постоянной времени судна')
xlabel('Ts, сек');
ylabel('\sigma, %');
h = get(gca, 'Children');
set(h(1),'LineWidth',1.5)

subplot(2,1,2);
set(gca,'FontSize',16);
plot(aTpp(1,:),aTpp(2,:),'b');
hold on;
xlabel('Ts, сек');
ylabel('Tpp, сек');
h = get(gca, 'Children');
set(h(1),'LineWidth',1.5)

print -dmeta
