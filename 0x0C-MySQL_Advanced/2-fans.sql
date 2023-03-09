--creates table users
SELECT DISTINCT `origin`, SUM(`fans`) as `nb_fans` from metal_bands
GROUP BY `origin`
ORDER BY `nb_fans` DESC;
