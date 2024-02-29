function [sigma,Tpp] = overshoot ( t, y )
    yInf = y(end);
    diff = (y - yInf) / abs (yInf);
    sigma = max(diff) * 100;
    i = find(abs(diff) > 0.02, 1, 'last');
    Tpp = t(i+1);
