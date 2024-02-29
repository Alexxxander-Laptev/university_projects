function lab5graph ( phi, delta )
    figure(1); % открыть рис. 1
    subplot(2,1,1);
    set(gca,'FontSize',16);
    plot(phi(:,1),phi(:,2),'b');
    hold on;
    title('Переходные процессы при изменении курса')
    xlabel('Время, сек');
    ylabel('\phi, град');
    h = get(gca, 'Children')
    set(h(1),'LineWidth',1.5)
    legend('Нелинейная система')
    
    subplot(2,1,2);
    set(gca,'FontSize',16);
    plot(delta(:,1),delta(:,2),'b');
    hold on;
    xlabel('Время, сек');
    ylabel('\phi, град');
    h = get(gca, 'Children')
    set(h(1),'LineWidth',1.5)
    legend('Нелинейная система')
    
    print -dmeta
