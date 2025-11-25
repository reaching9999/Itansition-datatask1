DROP TABLE IF EXISTS summary;

CREATE TABLE summary AS
SELECT
    publication_year,
    COUNT(id) AS book_count,

    
    ROUND(AVG(
        CASE
            WHEN price_text LIKE '€%' THEN CAST(TRIM(price_text, '€ ') AS REAL) * 1.2
            
            ELSE CAST(TRIM(price_text, '$ ') AS REAL)
        END
    ), 2) AS average_price_usd
FROM
    books
WHERE
    publication_year IS NOT NULL
    AND price_text IS NOT NULL
GROUP BY
    publication_year
ORDER BY
    publication_year;