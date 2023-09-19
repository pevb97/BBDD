select c.nombre Nombre_Categoria, AVG(p.precio_und) Precio_Promedio
from productos p
right join categorias c
on p.categoria_id  = c.id
group by c.id 
order by Precio_Promedio desc;

select c.nombre Nombre_Categoria, sum(s.cantidad) Cantidad_De_Productos_En_Stock
from categorias c
left join  productos p
on c.id  = p.categoria_id
right join stocks s
on p.id = s.producto_id
group by c.id
order by Cantidad_De_Productos_En_Stock desc;

select s.nombre Nombre_Sucursal, sum(o.total) Total_Ventas
from sucursales s
left join ordenes o
on s.id = o.sucursal_id
group by s.id
order by Total_Ventas desc;

select c.nombre Nombre_Cliente, sum(o.total) Total_Comprado_En_Ordenes
from clientes c
left join ordenes o
on c.id = o.cliente_id
group by c.id
order by Total_Comprado_En_Ordenes desc
limit 1;