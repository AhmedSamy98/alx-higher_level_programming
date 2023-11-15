-- Grants for user_0d_1@localhost
SELECT
    CONCAT('GRANT ', GROUP_CONCAT(privilege_type), ' ON *.* TO `user_0d_1`@`localhost`') AS grants
FROM
    information_schema.user_privileges
WHERE
    grantee = 'user_0d_1@localhost'
GROUP BY
    grantee;

