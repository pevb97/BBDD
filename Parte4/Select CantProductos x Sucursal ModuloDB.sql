SELECT
	s2.nombre ,
	SUM(cantidad) cantidad_producto
FROM
	sucursales s2
LEFT JOIN stocks s
ON
	s.sucursal_id = s2.id
GROUP BY
	s2.nombre ;

SELECT
	s.sucursal_id ,
	SUM(cantidad) cantidad_producto
FROM
	stocks s
GROUP BY
	s.sucursal_id ;