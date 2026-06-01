-- ==========================================
-- ЗАДАНИЕ 1
-- Вывожу список логинов курьеров с количеством 
-- их заказов в статусе «В доставке»
-- ==========================================

SELECT 
    c."login", 
    COUNT(o."track") AS "orders_count"
FROM 
    "Couriers" c
JOIN 
    "Orders" o ON c."id" = o."courierId"
WHERE 
    o."inDelivery" = true
GROUP BY 
    c."login";


-- ==========================================
-- ЗАДАНИЕ 2
-- Вывожу все трекеры заказов и их расчетные 
-- статусы
-- ==========================================

SELECT 
    "track",
    CASE 
        WHEN "finished" = true THEN 2
        WHEN "cancelled" = true THEN -1
        WHEN "inDelivery" = true THEN 1
        ELSE 0
    END AS "status"
FROM 
    "Orders";