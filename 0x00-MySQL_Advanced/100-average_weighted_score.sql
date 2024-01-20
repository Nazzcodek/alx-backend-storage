-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
-- Create Procedure
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
DECLARE score_weight FLOAT;
SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight) INTO score_weight
FROM corrections
JOIN projects ON projects.id = corrections.project_id
WHERE corrections.user_id = user_id;

UPDATE users
SET average_score = score_weight
WHERE id = user_id;
END $$

DELIMITER ;
