SELECT b.title, b.year_published, a.first || ' ' || a.last AS author_name
FROM books b
JOIN authors a ON b.author_id = a.author_id
ORDER BY b.year_published;

