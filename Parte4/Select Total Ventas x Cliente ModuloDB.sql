SELECT
	c.nombre ,
	SUM(o.total) Total_Ventas
FROM
	clientes c
LEFT JOIN ordenes o
ON
	o.cliente_id = c.id
GROUP BY
	c.nombre ;

SELECT
	o.cliente_id ,
	SUM(o.total) Total_Ventas
FROM
	ordenes o
GROUP BY
	o.cliente_id ;