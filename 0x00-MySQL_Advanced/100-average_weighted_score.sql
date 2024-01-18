-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE w_avg_score FLOAT;
    SET w_avg_score = (SELECT SUM(score * weight) / SUM(weight) 
                        FROM users AS u
                        JOIN corrections as c ON u.id=C.user_id 
                        JOIN projects AS p ON c.project_id=p.id 
                        WHERE u.id=user_id);
    UPDATE users
    SET average_score = w_avg_score
    WHERE id=user_id;
END
$$
DELIMITER ;
