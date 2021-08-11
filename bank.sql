CREATE TABLE `bank` (
  `account` INT(8) NOT NULL,
  `username` VARCHAR(20) NOT NULL,
  `password` INT(6) NOT NULL,
  `country` VARCHAR(20) NOT NULL,
  `province` VARCHAR(30) NOT NULL,
  `street` VARCHAR(20) NOT NULL,
  `door` VARCHAR(255) NOT NULL,
  `money` DOUBLE(15,2) NOT NULL,
  `bankname` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`account`)
) 