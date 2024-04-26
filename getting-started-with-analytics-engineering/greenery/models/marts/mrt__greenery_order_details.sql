select 
 o.order_id,
 p.name as product_name,
 p.price as unit_price,
 o.quantity
 
from {{ source('greenery', 'products') }} as p
right join {{ source('greenery', 'order_items') }} as o

on p.product_id = o.product_id