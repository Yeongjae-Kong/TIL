SELECT pt_name, pt_no, gend_cd, age,
case
WHEN tlno IS NULL THEN "NONE"
else tlno
end
as TLNO
FROM patient
WHERE gend_cd = "W" and AGE <= 12
ORDER BY age DESC, pt_name ASC;
