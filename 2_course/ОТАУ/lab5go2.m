sysdata;
aPhi = linspace(1, 110, 110);
Ts0 = Ts;
aSi = [];
aTpp = [];
for Ts=aPhi
    sim ( 'lab5' )
    [si,Tpp] = overshoot ( phi(:,1), phi(:,2) );
    aSi = [aSi si];
    aTpp = [aTpp Tpp];
end

aSi = [aPhi; aSi];
aTpp = [aPhi; aTpp];

figure(1); % открыть рис. 1
subplot(2,1,1);
set(gca,'FontSize',16);
plot(aSi(1,:),aSi(2,:),'b');
hold on;
title('Влияние заданного курса')
xlabel('\phi_з_а_д, градусов');
ylabel('\sigma, %');
h = get(gca, 'Children');
set(h(1),'LineWidth',1.5)

subplot(2,1,2);
set(gca,'FontSize',16);
plot(aTpp(1,:),aTpp(2,:),'b');
hold on;
xlabel('\phi_з_а_д, градусов');
ylabel('Tpp, сек');
h = get(gca, 'Children');
set(h(1),'LineWidth',1.5)

print -dmeta
