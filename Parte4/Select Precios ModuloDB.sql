SELECT
	MIN(p.precio_und) precio_minimo,
	MAX(p.precio_und) precio_maximo,
	AVG(p.precio_und) precio_promedio
FROM
	productos p;