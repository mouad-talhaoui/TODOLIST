CREATE TABLE `students` (
  `id` int(11) NOT NULL,
  `description` varchar(255) NOT NULL,
  `state` varchar(255) NOT NULL
  ) ENGINE=MyISAM DEFAULT CHARSET=latin1;


INSERT INTO `tasks` (`id`, `description`, `state`) VALUES
(3, 'home work 1 ', 'done'),
(4, 'home work 2', 'done'),
(5, 'home work 3', 'done'),
(6, 'home work 4', 'done'),
(7, 'home work 5', 'done');

ALTER TABLE `tasks`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `tasks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;