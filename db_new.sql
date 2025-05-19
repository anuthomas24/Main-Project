/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - antique_integrity
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`antique_integrity` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `antique_integrity`;

/*Table structure for table `auction` */

DROP TABLE IF EXISTS `auction`;

CREATE TABLE `auction` (
  `auction_id` int(10) NOT NULL AUTO_INCREMENT,
  `seller_id` int(10) DEFAULT NULL,
  `product_name` varchar(500) DEFAULT NULL,
  `product_image` varchar(5000) DEFAULT NULL,
  `details` varchar(500) DEFAULT NULL,
  `base_amount` varchar(500) DEFAULT NULL,
  `added_date` varchar(500) DEFAULT NULL,
  `auction_end_date` varchar(500) DEFAULT NULL,
  `winner_id` varchar(500) DEFAULT NULL,
  `status` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`auction_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `auction` */

insert  into `auction`(`auction_id`,`seller_id`,`product_name`,`product_image`,`details`,`base_amount`,`added_date`,`auction_end_date`,`winner_id`,`status`) values 
(1,2,'Wheel cup','static/product_images/7cbd467c-bcf0-4dda-9e13-ff4f188f78e5soldier-army-man-line-icon-vector-illustration-2GN2BHN.jpg','Nil','500','2024-12-10','2024-12-16','4','Finished');

/*Table structure for table `auction_result` */

DROP TABLE IF EXISTS `auction_result`;

CREATE TABLE `auction_result` (
  `result_id` int(10) NOT NULL AUTO_INCREMENT,
  `winner_id` int(10) DEFAULT NULL,
  `auction_id` int(10) DEFAULT NULL,
  `bid_amount` varchar(500) DEFAULT NULL,
  `date` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`result_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `auction_result` */

insert  into `auction_result`(`result_id`,`winner_id`,`auction_id`,`bid_amount`,`date`) values 
(1,4,1,'605','2024-12-16');

/*Table structure for table `bid` */

DROP TABLE IF EXISTS `bid`;

CREATE TABLE `bid` (
  `bid_id` int(10) NOT NULL AUTO_INCREMENT,
  `auction_id` int(10) DEFAULT NULL,
  `user_id` int(10) DEFAULT NULL,
  `amount` varchar(500) DEFAULT NULL,
  `date_time` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`bid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `bid` */

insert  into `bid`(`bid_id`,`auction_id`,`user_id`,`amount`,`date_time`) values 
(1,1,2,'505','2024-12-15 09:06:26'),
(2,1,4,'605','2024-12-15 09:07:39');

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `category_id` int(10) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`category_id`,`category_name`) values 
(1,'Maiores quibusdam mo'),
(2,'ghjkl');

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(10) NOT NULL AUTO_INCREMENT,
  `sender_id` int(10) DEFAULT NULL,
  `sender_type` varchar(50) DEFAULT NULL,
  `receiver_id` int(10) DEFAULT NULL,
  `receiver_type` varchar(500) DEFAULT NULL,
  `message` varchar(500) DEFAULT NULL,
  `date` varchar(500) DEFAULT NULL,
  `time` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`chat_id`,`sender_id`,`sender_type`,`receiver_id`,`receiver_type`,`message`,`date`,`time`) values 
(1,2,'user',1,'seller','hello','2024-12-13','10:08:32'),
(2,2,'user',4,'seller','hello','2024-12-13','10:08:42'),
(3,2,'user',5,'seller','hii','2024-12-13','10:08:49'),
(4,4,'seller',3,'user','hello','2024-12-13','10:53:00'),
(5,4,'seller',3,'user','heyy','2024-12-13','10:53:04'),
(11,4,'seller',2,'user','heyy','2024-12-13','10:54:10'),
(10,4,'seller',3,'user','hoo','2024-12-13','10:53:59'),
(12,4,'seller',2,'user','hoo','2024-12-13','10:54:27'),
(13,2,'user',4,'seller','hii','2024-12-13','10:54:50'),
(14,4,'seller',2,'user','hiiidjic','2024-12-13','11:07:05'),
(15,2,'user',4,'seller','cjnm','2024-12-13','11:10:45'),
(16,6,'user',1,'seller','hiii','2024-12-16','09:07:12');

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaints_id` int(10) NOT NULL AUTO_INCREMENT,
  `sender_id` int(10) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `reply` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`complaints_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

insert  into `complaints`(`complaints_id`,`sender_id`,`title`,`description`,`reply`,`date`) values 
(1,1,'new','complaiintsnb','oky','19/11/2024'),
(2,2,'Aut eum commodi non ','Error laborum Delen','pending','2024-11-20'),
(3,2,'Omnis in fugit dign','Do odio voluptatem o','pending','2024-11-20'),
(4,2,'Et quis laudantium ','Possimus et eu in a','pending','2024-11-20'),
(5,2,'Dolor ea laborum Om','Dolor est dolore nat','pending','2024-11-27'),
(6,6,'Beatae culpa omnis ','Mollitia in quo nihi','pending','2024-12-12');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(10) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`user_name`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(2,'amal','123','user'),
(5,'new','123','seller'),
(4,'seller','seller','seller'),
(6,'newuser','1234','user');

/*Table structure for table `orders` */

DROP TABLE IF EXISTS `orders`;

CREATE TABLE `orders` (
  `order_id` int(10) NOT NULL AUTO_INCREMENT,
  `user_id` int(10) DEFAULT NULL,
  `product_id` int(10) DEFAULT NULL,
  `date` varchar(500) DEFAULT NULL,
  `status` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `orders` */

insert  into `orders`(`order_id`,`user_id`,`product_id`,`date`,`status`) values 
(1,1,1,'20/11/2024','pending'),
(2,2,1,'2024-11-20','paid'),
(3,2,5,'2024-11-20','pending'),
(4,2,2,'2024-11-27','pending'),
(5,2,2,'2024-11-27','pending'),
(6,2,0,'2024-11-27','pending'),
(7,4,0,'2024-12-12','pending'),
(8,4,2,'2024-12-12','pending');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(10) NOT NULL AUTO_INCREMENT,
  `order_id` int(10) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`order_id`,`amount`,`date`,`status`) values 
(1,1,'500','20/11/205','pending'),
(2,2,'500','2024-11-20','paid'),
(3,2,'500','2024-11-27','paid');

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `product_id` int(10) NOT NULL AUTO_INCREMENT,
  `category_id` int(10) DEFAULT NULL,
  `seller_id` int(10) DEFAULT NULL,
  `product_name` varchar(50) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `image` varchar(50000) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`product_id`,`category_id`,`seller_id`,`product_name`,`amount`,`description`,`image`) values 
(1,1,2,'Blake Rhodes','500','Eaque fugiat except','static/product_images/8169b6c1-f5d0-4f4b-8a8b-741b0e6f1556chat_9691105.png'),
(5,1,2,'Cameran Neal','190','Lorem qui eum reicie','static/product_images/4a1cad8e-f8ef-41dd-ae4a-85f0200b54e4Untitled design (7).png'),
(6,1,2,'Maggy Dixon','260','Quod doloribus repre','static/product_images/e223717c-fe03-4405-a180-5c7ba42d4adarobot_3279301.png'),
(7,2,2,'Allen Wiley','82','Ut quia unde consequ','static/product_images/99a3a644-0912-4045-a1b4-0c8c5e066760Untitled design (7).png'),
(8,1,2,'Cameron Bell','23','Ipsam non commodi ac','static/product_images/fff65001-62bc-412a-bad4-0110b7872d632003976-200.png');

/*Table structure for table `product_images` */

DROP TABLE IF EXISTS `product_images`;

CREATE TABLE `product_images` (
  `products_images_id` int(10) NOT NULL AUTO_INCREMENT,
  `product_id` int(10) DEFAULT NULL,
  `images` varchar(5000) DEFAULT NULL,
  PRIMARY KEY (`products_images_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `product_images` */

insert  into `product_images`(`products_images_id`,`product_id`,`images`) values 
(1,1,'static/product_images/137067ee-d8b7-4ae4-aa82-627cf45e0890robot_3279301.png'),
(2,5,'static/product_images/0c8e4872-a9b6-4d23-a5dc-9653b1c03432Untitled design (11).png'),
(3,1,'static/product_images/e4452c2e-3104-457d-9b04-a344f75c206fmedicinal-plant-indian-country-borage-or-coleus-amboinicus-india-kerala-BBTCYW.jpg'),
(4,2,'static/product_images/bf4ff459-1077-4e7d-a1de-7c659a726f322003976-200.png');

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `rating_id` int(10) NOT NULL AUTO_INCREMENT,
  `user_id` int(10) DEFAULT NULL,
  `product_id` int(10) DEFAULT NULL,
  `rating` varchar(500) DEFAULT NULL,
  `review` varchar(500) DEFAULT NULL,
  `date` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`rating_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

insert  into `rating`(`rating_id`,`user_id`,`product_id`,`rating`,`review`,`date`) values 
(1,1,1,'3.5','good','20/11/2024'),
(2,2,2,'4.5','jjnkm','254'),
(3,2,1,'2.5','Ut cillum sit nostru','2024-11-20'),
(4,2,1,'2.3','Molestias elit in l','2024-11-27');

/*Table structure for table `seller` */

DROP TABLE IF EXISTS `seller`;

CREATE TABLE `seller` (
  `seller_id` int(10) NOT NULL AUTO_INCREMENT,
  `login_id` int(10) DEFAULT NULL,
  `seller_name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `licence_number` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`seller_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `seller` */

insert  into `seller`(`seller_id`,`login_id`,`seller_name`,`place`,`phone`,`email`,`licence_number`) values 
(1,1,'amal','thrissur','7894561230','amal@gmail.com','785205852025'),
(2,4,'Joelle Sanders','Deleniti at dolore m','+1 (411) 679-7456','lifyc@mailinator.com','Vanna Ward'),
(3,5,'Martina Richard','Fugiat aute modi ill','+1 (277) 479-6829','xeqomohak@mailinator.com','Zachery Robbins');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(10) NOT NULL AUTO_INCREMENT,
  `login_id` int(10) DEFAULT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`) values 
(1,3,'anu','amal','thrissur','789456132','amal@gmail.com'),
(2,2,'Buffy Hernandez','Joan Macdonald','Cillum alias ut ipsu','+1 (967) 245-4298','zutyhecuwy@mailinator.com'),
(4,6,'Buffy','Tyler','Est iste irure et do','+1 (864) 829-7456','feqoxe@mailinator.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
