-- 코드를 입력하세요
SELECT member_id, member_name, gender, DATE_FORMAT(date_of_birth, "%Y-%m-%d") as DATE_OF_BIRTH
FROM member_profile
WHERE TLNO IS NOT NULL AND SUBSTR(date_of_birth, 6, 2) = '03' AND gender = 'W'
ORDER BY member_id ASC