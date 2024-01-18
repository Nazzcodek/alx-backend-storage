-- SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score DECIMAL(10, 2);

    -- Calculate the average score for the user
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = user_id;

    -- Create a temporary users table
    CREATE TEMPORARY TABLE temp_users AS
        SELECT id, name, average_score
        FROM users
        WHERE id = user_id;

    -- Update or insert the average score for the user
    INSERT INTO users (id, name, average_score)
    SELECT id, name, avg_score
    FROM temp_users
    ON DUPLICATE KEY UPDATE average_score = avg_score;

    -- Drop the temporary table
    DROP TEMPORARY TABLE IF EXISTS temp_users;

END;

$$

DELIMITER ;
