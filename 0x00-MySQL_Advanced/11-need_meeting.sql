-- SQL script that creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month.
CREATE VIEW need_meeting AS
SELECT s.name
FROM students s
LEFT JOIN meetings m ON s.id = m.student_id
WHERE s.score < 80
      AND (m.last_meeting IS NULL OR m.last_meeting < NOW() - INTERVAL 1 MONTH);
