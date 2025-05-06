-- 코드를 입력하세요
SELECT product_id, product_name, product_cd, category, price
FROM FOOD_PRODUCT
WHERE price = (SELECT MAX(PRICE) FROM FOOD_PRODUCT)