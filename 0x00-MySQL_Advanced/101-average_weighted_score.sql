-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users AS u, 
        (SELECT u.id, SUM(score * weight) / SUM(weight) AS w_avg 
        FROM users AS u
        JOIN corrections as c ON u.id=C.user_id 
        JOIN projects AS p ON c.project_id=p.id 
        GROUP BY u.id)
    AS wa
    SET u.average_score = wa.w_avg 
    WHERE u.id=wa.id;
END
$$
DELIMITER ;
