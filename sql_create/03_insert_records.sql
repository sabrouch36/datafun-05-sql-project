INSERT INTO authors (author_id, first, last) VALUES
('a1', 'George', 'Orwell'),
('a2', 'J.K.', 'Rowling'),
('a3', 'Jane', 'Austen'),
('a4', 'Mark', 'Twain'),
('a5', 'Leo', 'Tolstoy'),
('a6', 'Agatha', 'Christie'),
('a7', 'Ernest', 'Hemingway'),
('a8', 'Fyodor', 'Dostoevsky'),
('a9', 'Charles', 'Dickens'),
('a10', 'H.G.', 'Wells');

INSERT INTO books (book_id, title, year_published, author_id) VALUES
('b1', '1984', 1949, 'a1'),
('b2', 'Animal Farm', 1945, 'a1'),
('b3', 'Harry Potter', 1997, 'a2'),
('b4', 'Pride and Prejudice', 1813, 'a3'),
('b5', 'Adventures of Huckleberry Finn', 1884, 'a4'),
('b6', 'War and Peace', 1869, 'a5'),
('b7', 'Murder on the Orient Express', 1934, 'a6'),
('b8', 'The Old Man and the Sea', 1952, 'a7'),
('b9', 'Crime and Punishment', 1866, 'a8'),
('b10', 'Oliver Twist', 1839, 'a9');
