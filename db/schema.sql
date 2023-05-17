CREATE DATABASE nba_stats_app;
\c nba_stats_app

CREATE TABLE players(
    id SERIAL PRIMARY KEY, 
    image_url TEXT,
    name TEXT,
    ppg TEXT,
    rpg TEXT,
    apg TEXT,
    championship TEXT
);
INSERT INTO players(image_url, name, ppg, rpg, apg, championship)
VALUES
('https://a2.espncdn.com/combiner/i?img=%2Fphoto%2F2020%2F0509%2Fr696991_2559x3841cc.jpg&w=1140&cquality=40&format=jpg', 'Michael Jordan', '30.1', '6.2', '5.3', '6'),
('https://a3.espncdn.com/combiner/i?img=%2Fphoto%2F2020%2F0509%2Fr696990_2136x2541cc.jpg&w=1140&cquality=40&format=jpg', 'LeBron James', '27.1', '7.4', '7.4', '4'),
('https://a1.espncdn.com/combiner/i?img=%2Fphoto%2F2020%2F0509%2Fr696981_854x1386cc.jpg&w=1140&cquality=40&format=jpg', 'Kobe Bryant','25.0', '5.2', '4.7', '5'),
('https://a1.espncdn.com/combiner/i?img=%2Fphoto%2F2022%2F0611%2Fr1023731_1296x729_16%2D9.jpg&w=920&h=518&scale=crop&cquality=80&location=origin&format=jpg', 'Stephen Curry', '24.6', '4.7', '6.5', '4'),
('https://a4.espncdn.com/combiner/i?img=%2Fphoto%2F2020%2F0508%2Fr696686_2205x2931cc.jpg&w=1140&cquality=40&format=jpg', 'Shaquille ONeal', '23.7', '10.9', '2.5','4');

CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  email TEXT,
  password_digest TEXT
);

CREATE TABLE comment(
  id SERIAL PRIMARY KEY,
  user_id INTEGER,
  player_id INTEGER,
  comment TEXT
);



