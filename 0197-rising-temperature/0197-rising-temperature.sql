SELECT w.id AS Id
FROM Weather AS w
JOIN Weather as t
on w.recordDate = ADDDATE(t.recordDate, INTERVAL 1 DAY)
WHERE w.temperature > t.temperature;