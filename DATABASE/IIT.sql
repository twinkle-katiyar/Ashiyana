-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: localhost    Database: IIT
-- ------------------------------------------------------
-- Server version	5.7.26-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `atable`
--

DROP TABLE IF EXISTS `atable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `atable` (
  `Sn` int(5) DEFAULT NULL,
  `UserId` text,
  `PropertyId` text,
  `Appointment_date` text,
  `Appointment_time` text,
  `Status` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `atable`
--

LOCK TABLES `atable` WRITE;
/*!40000 ALTER TABLE `atable` DISABLE KEYS */;
INSERT INTO `atable` VALUES (1,'Sachin Verma_1','HH122','22-07-19','12:00pm','Pending'),(2,'Sanskar Katiyar_2','HH142','23-07-19','12:00pm','Pending'),(3,'Twinkle Katiyar_3','HH130','19-02-19','12:00pm','Done'),(4,'Varkha Yadav_4','HH147','21-03-19','12:00pm','Schedule New'),(5,'Alia Rai_5','HH136','24-08-19','1:00pm','Pending');
/*!40000 ALTER TABLE `atable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `property`
--

DROP TABLE IF EXISTS `property`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `property` (
  `Price` int(20) DEFAULT NULL,
  `BHK` int(5) DEFAULT NULL,
  `Sqft` int(10) DEFAULT NULL,
  `Property_Type` text,
  `Exterior_Wall` text,
  `Location` text,
  `Property_id` text,
  `Status` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `property`
--

LOCK TABLES `property` WRITE;
/*!40000 ALTER TABLE `property` DISABLE KEYS */;
INSERT INTO `property` VALUES (295850,1,584,'Apartment','Wood Siding','Kanpur','HH101','ON'),(908790,5,612,'Bungalow','Brick','Kanpur','HH102','ON'),(678900,3,615,'Villa','Wood Siding','Kanpur','HH103','ON'),(379900,2,618,'Apartment','Wood Siding','Kanpur','HH104','ON'),(340000,2,634,'Apartment','Brick','Kanpur','HH105','ON'),(265000,1,641,'Apartment','Brick','Kanpur','HH106','OFF'),(240000,0,642,'Plot','Land','Kanpur','HH107','ON'),(388100,0,650,'Plot','Land','Kanpur','HH108','ON'),(240000,0,660,'Plot','Land','Kanpur','HH109','ON'),(250000,0,664,'Plot','Land','Kanpur','HH110','ON'),(335000,0,669,'Plot','Land','Kanpur','HH111','ON'),(376750,0,673,'Plot','Land','Kanpur','HH112','OFF'),(210000,0,680,'Plot','Land','Kanpur','HH113','OFF'),(289900,1,685,'Office Space','Brick','Kanpur','HH114','ON'),(535000,3,687,'Apartment','Wood Siding','Kanpur','HH115','ON'),(218000,1,689,'Apartment','Brick','Kanpur','HH116','ON'),(400000,3,689,'Apartment','Wood Siding','Kanpur','HH117','OFF'),(226000,1,690,'Office Space','Brick','Kanpur','HH118','ON'),(363700,1,692,'Apartment','Brick','Kanpur','HH119','ON'),(215000,0,698,'Plot','Land','Delhi','HH120','ON'),(327000,1,698,'Apartment','Concrete Block','Delhi','HH121','ON'),(331100,2,700,'Office Space','Concrete Block','Delhi','HH122','OFF'),(240000,1,703,'Apartment','Wood','Delhi','HH123','ON'),(320000,2,704,'Apartment','Brick','Delhi','HH124','ON'),(290800,1,704,'Apartment','Brick','Delhi','HH125','ON'),(375000,2,705,'Apartment','Brick','Delhi','HH126','ON'),(377000,2,709,'Apartment','Wood Siding','Delhi','HH127','ON'),(262500,1,711,'Office Space','Brick','Delhi','HH128','ON'),(216250,1,712,'Apartment','Brick','Delhi','HH129','ON'),(270000,1,722,'Apartment','Brick','Delhi','HH130','OFF'),(235000,1,723,'Apartment','Stucco','Delhi','HH131','ON'),(225000,0,724,'Plot','Land','Delhi','HH132','ON'),(370000,1,725,'Apartment','Wood Siding','Delhi','HH133','OFF'),(232000,1,736,'Apartment','Brick','Delhi','HH134','ON'),(281900,1,737,'Office Space','Brick','Delhi','HH135','ON'),(355000,2,740,'Apartment','Brick','Delhi','HH136','OFF'),(890000,5,741,'Bungalow','Wood Siding','Delhi','HH137','ON'),(231900,1,750,'Apartment','Brick','Delhi','HH138','ON'),(284000,1,755,'Office Space','Brick','Delhi','HH139','ON'),(255000,0,759,'Plot','Land','Lucknow','HH140','ON'),(285850,1,759,'Apartment','Brick','Lucknow','HH141','ON'),(249298,1,759,'Apartment','Brick','Lucknow','HH142','OFF'),(380000,2,760,'Office Space','Brick','Lucknow','HH143','ON'),(244800,1,767,'Apartment','Brick','Lucknow','HH144','ON'),(397400,0,771,'Plot','Land','Lucknow','HH145','ON'),(345000,2,781,'Apartment','Wood Siding','Lucknow','HH146','ON'),(220000,1,792,'Apartment','Brick','Lucknow','HH147','OFF'),(279000,1,796,'Office Space','Concrete','Lucknow','HH148','ON'),(286900,1,797,'Apartment','Brick','Lucknow','HH149','ON'),(220000,1,800,'Apartment','Brick','Lucknow','HH150','ON'),(305000,1,805,'Apartment','Brick','Lucknow','HH151','ON'),(409575,3,805,'Bungalow','Concrete Block','Lucknow','HH152','OFF'),(300367,1,805,'Apartment','Block','Lucknow','HH153','ON'),(230000,1,809,'Apartment','Brick','Lucknow','HH154','ON'),(270000,1,810,'Office Space','Brick','Lucknow','HH155','ON'),(210000,0,811,'Plot','Land','Lucknow','HH156','ON'),(366700,1,817,'Office Space','Brick','Patna','HH157','ON'),(238600,2,834,'Apartment','Brick','Patna','HH158','ON'),(284900,1,838,'Apartment','Block','Patna','HH159','ON'),(253000,1,850,'Apartment','Brick','Patna','HH160','ON'),(305000,1,850,'Apartment','Brick','Patna','HH161','OFF'),(280000,1,850,'Office Space','Brick','Patna','HH162','ON'),(411000,3,855,'Apartment','Wood Siding','Patna','HH163','ON'),(270900,1,856,'Apartment','Wood Siding','Patna','HH164','ON'),(406250,3,859,'Apartment','Brick','Patna','HH165','OFF'),(365000,1,866,'Apartment','Brick','Patna','HH166','ON'),(440000,0,879,'Plot','Land','Patna','HH167','ON'),(250000,1,880,'Office Space','Brick','Patna','HH168','ON'),(350100,2,900,'Single-Family','Stucco','Patna','HH169','ON'),(250000,1,900,'Apartment','Brick','Patna','HH170','ON'),(305000,2,902,'Office Space','Concrete','Patna','HH171','ON'),(200000,1,914,'Apartment','Brick','Mathura','HH172','OFF'),(371500,1,917,'Apartment','Block','Mathura','HH173','ON'),(270000,1,920,'Apartment','Brick','Mathura','HH174','ON'),(318000,1,926,'Office Space','Brick','Mathura','HH175','ON'),(408400,3,933,'Apartment','Stucco','Mathura','HH176','ON'),(325000,1,934,'Apartment','Stucco','Mathura','HH177','ON'),(239000,1,945,'Office Space','Brick','Mathura','HH178','ON'),(367500,1,950,'Apartment','Brick','Mumbai','HH179','ON'),(378000,1,961,'Apartment','Wood Siding','Mumbai','HH180','ON'),(269000,1,966,'Apartment','Wood','Mumbai','HH181','ON'),(245000,1,999,'Office Space','Brick','Mumbai','HH182','ON'),(225000,1,1005,'Apartment','Brick','Mumbai','HH183','ON'),(302000,1,1014,'Apartment','Brick','Mumbai','HH184','ON'),(387900,1,1050,'Apartment','Stucco','Mumbai','HH185','ON'),(560000,4,1092,'Apartment','Brick','Mumbai','HH186','OFF'),(750000,5,1322,'Office Space','Wood Siding','Mumbai','HH187','ON'),(299700,1,814,'Apartment','Wood Siding','Mumbai','HH188','ON'),(779900,1,1207,'Apartment','Brick','Mumbai','HH189','OFF'),(379000,1,1489,'Office Space','Brick','Mumbai','HH190','ON'),(225000,1,768,'Apartment','Brick','Mumbai','HH191','ON'),(230000,2,793,'Office Space','Brick','Kolkata','HH192','ON'),(328000,2,800,'Apartment','Brick','Kolkata','HH193','ON'),(407800,3,803,'Apartment','Wood Siding','Kolkata','HH194','OFF'),(470630,2,814,'Apartment','Concrete Block','Kolkata','HH195','ON'),(270000,2,816,'Office Space','Brick','Kolkata','HH196','ON'),(670000,4,835,'Bungalow','Brick','Kolkata','HH197','ON'),(355000,2,836,'Apartment','Brick','Kolkata','HH198','ON'),(283000,2,845,'Apartment','Brick','Kolkata','HH199','ON'),(378000,2,864,'Apartment','Brick','Kolkata','HH200','ON'),(255000,0,870,'Plot','Land','Kolkata','HH201','ON'),(306000,2,875,'Apartment','Brick','Kolkata','HH202','ON'),(292999,1,875,'Office Space','Brick','Kolkata','HH203','OFF'),(369900,2,891,'Apartment','Brick','Kolkata','HH204','ON'),(326000,2,893,'Apartment','Brick','Kolkata','HH205','ON'),(350000,2,900,'Apartment','Brick','Chennai','HH206','ON'),(350000,1,900,'Office Space','Brick','Chennai','HH207','ON'),(396875,2,912,'Apartment','Brick','Chennai','HH208','ON'),(374900,2,912,'Apartment','Brick','Chennai','HH209','ON'),(232150,2,920,'Apartment','Brick','Chennai','HH210','ON'),(327000,2,924,'Office Space','Brick','Chennai','HH211','ON'),(890000,4,928,'Bungalow','Wood Siding','Chennai','HH212','ON'),(290000,2,930,'Apartment','Wood Siding','Chennai','HH213','ON'),(301000,2,930,'Apartment','Wood Siding','Chennai','HH214','ON'),(275000,2,930,'Office Space','Metal','Chennai','HH215','ON'),(531000,0,931,'Plot','Land','Chennai','HH216','ON'),(405000,2,945,'Apartment','Brick','Chennai','HH217','ON'),(336000,2,950,'Plot','Land','Chennai','HH218','OFF'),(214000,2,952,'Office Space','Brick','Aligarh','HH219','ON'),(327500,2,958,'Apartment','Brick','Aligarh','HH220','ON'),(251489,0,959,'Plot','Land','Aligarh','HH221','ON'),(238900,2,960,'Apartment','Brick','Aligarh','HH222','ON'),(297000,1,960,'Apartment','Brick','Aligarh','HH223','OFF'),(235000,2,960,'Office Space','Brick','Aligarh','HH224','ON'),(210000,2,960,'Apartment','Metal','Aligarh','HH225','ON'),(215000,1,966,'Apartment','Brick','Aligarh','HH226','ON'),(285000,2,966,'Apartment','Wood','Indore','HH227','OFF'),(239900,2,976,'Apartment','Brick','Indore','HH228','ON'),(375500,1,983,'Apartment','Brick','Indore','HH229','ON'),(415000,2,993,'Office Space','Brick','Indore','HH230','ON'),(230581,2,996,'Apartment','Brick','Indore','HH231','ON'),(400000,3,1008,'Apartment','Brick','Indore','HH232','OFF'),(420000,3,1010,'Office Space','Brick','Indore','HH233','ON'),(292000,2,1011,'Apartment','Brick','Indore','HH234','ON'),(200000,0,1015,'Plot','Land','Indore','HH235','ON'),(226000,1,1021,'Apartment','Brick','Indore','HH236','ON'),(220000,0,1024,'Plot','Land','Amritsar','HH237','ON'),(280000,2,1032,'Office Space','Brick','Amritsar','HH238','ON'),(299900,2,1032,'Apartment','Brick','Amritsar','HH239','OFF'),(204000,2,1044,'Office Space','Brick','Amritsar','HH240','ON'),(350000,0,1062,'Plot','Land','Amritsar','HH241','ON'),(228000,2,1070,'Apartment','Brick','Amritsar','HH242','ON'),(300000,2,1073,'Apartment','Brick','Amritsar','HH243','ON'),(280000,2,1083,'Office Space','Brick','Amritsar','HH244','ON'),(305500,3,1100,'Apartment','Brick','Varanasi','HH245','ON'),(348500,1,1103,'Office Space','Brick','Varanasi','HH246','OFF'),(210000,0,1177,'Plot','Land','Varanasi','HH247','ON'),(250000,2,1179,'Apartment','Brick','Varanasi','HH248','ON'),(890000,4,1185,'Bungalow','Brick','Varanasi','HH249','ON');
/*!40000 ALTER TABLE `property` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `psold`
--

DROP TABLE IF EXISTS `psold`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `psold` (
  `sn` int(5) DEFAULT NULL,
  `UserId` text,
  `PropertyId` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `psold`
--

LOCK TABLES `psold` WRITE;
/*!40000 ALTER TABLE `psold` DISABLE KEYS */;
INSERT INTO `psold` VALUES (1,'Mohini Katyal_100','HH106'),(2,'Sumit Kaur_101','HH112'),(3,'Faiz Khan_102','HH117'),(4,'Rohini_103','HH113'),(5,'Roushan Singh_104','HH133');
/*!40000 ALTER TABLE `psold` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rtable`
--

DROP TABLE IF EXISTS `rtable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rtable` (
  `Sn` int(5) DEFAULT NULL,
  `UserId` text,
  `Reviews` text,
  `STARS` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rtable`
--

LOCK TABLES `rtable` WRITE;
/*!40000 ALTER TABLE `rtable` DISABLE KEYS */;
INSERT INTO `rtable` VALUES (1,'Afrah Riaz_6','Very reliable place for a person to buy property according their needs !! Felt Gr8 !!','5 '),(2,'Ria Singh_2002','Amazing Locality !!! The place and Property is exactly same as promised !!1 A gr8 experience ! ALL THANKS TO \"ASHIANA\"','4'),(3,'Garima Arora_390',' \"ASHIANA\" really gave me my dream ASHIANA . I luved the place and locality . ','4'),(4,'Gaurav kumar_420',' The process of House booking took more time than promised, All i could say is dont rely completely on them ','2'),(5,'Mahima Saxena_4233',' Ashiana!!! thanks for this gr8 property !!  !!!  ','4'),(6,'Rishabh Rai_3090','  -  ','4'),(7,'Kapil Raj_90','  -  ','5'),(8,'Kajal Raman_91','Peaceful Location !! All happy and gay atmosphere  ','3'),(9,'Jyoti Sotta_909','The best Ahiana from Ashiana !! ','5'),(10,'Ruchi_1001',' -  ','4'),(11,'Alia Rai_5 ','ASHIYANA is the best place to buy your Dream Ashiyana !!! One get huge varieties to choose the best match. Dont wait just grab it.','5');
/*!40000 ALTER TABLE `rtable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stu`
--

DROP TABLE IF EXISTS `stu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stu` (
  `sn` int(5) DEFAULT NULL,
  `uid` varchar(30) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `age` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stu`
--

LOCK TABLES `stu` WRITE;
/*!40000 ALTER TABLE `stu` DISABLE KEYS */;
INSERT INTO `stu` VALUES (1,'Twinkle_1','Twinkle',21),(2,'Varkha_2','Varkha',20);
/*!40000 ALTER TABLE `stu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `Sn` int(200) DEFAULT NULL,
  `Name` text,
  `UserId` text,
  `Password` text,
  `Age` text,
  `MobNo` text,
  `AdharNo` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Sachin Verma','Sachin Verma_1','abcd','89','8907654321','908978675645'),(2,'Sanskar Katiyar','Sanskar Katiyar_2','abcd','20','1234567890','112233445566'),(3,'Twinkle Katiyar','Twinkle Katiyar_3','abcd','20','7890678900','998877889098'),(4,'Varkha Yadav','Varkha yadav_4','abcd','21','1234556678','334455456789'),(5,'Alia Rai','Alia Rai_5','abcd','22','2345678909','223344567890'),(6,'Afrah Riaz','Afrah Riaz_6','sdfg','45','2345657890','123444556677'),(7,'Raima Raj','Raima Raj_7','abcdfg','20','2233456789','090989876787'),(8,'Ragini Sharma','Ragini Sharma_8','abcd','24','8907890909','908989787690'),(9,'Reena Jha','Reena Jha_9','abcd','54','2345678909','123454657688'),(10,'Sakshi Bansal','Sakshi Bansal_10','abfg','34','9878906789','879065456787'),(11,'Rhythm Chauhan','Rhythm Chauhan_11','sdfg','23','2345432343','123321234565');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vtable`
--

DROP TABLE IF EXISTS `vtable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vtable` (
  `sn` int(5) DEFAULT NULL,
  `UserId` text,
  `PropertyId` text,
  `Price` text,
  `BHK` text,
  `Sqft` text,
  `Property_Type` text,
  `Exterior_Wall` text,
  `Location` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vtable`
--

LOCK TABLES `vtable` WRITE;
/*!40000 ALTER TABLE `vtable` DISABLE KEYS */;
INSERT INTO `vtable` VALUES (1,'Firoz Khan_156','HH152','223470','0','590','Plot','Land','Delhi'),(2,'Kamakhya Yadav_166','HH246','323470','2','690','Apartment','Brick','Delhi'),(3,'Ria Kaushik_169','HH239','322270','2','678','Apartment','Brick','Agra'),(4,'Riama Agarwal_1456','HH232','222270','3','360','Apartment','Brick','Agra'),(5,'Vibu Mittal_1756','HH227','435670','4','560','Apartment','Brick','Agra'),(6,'Twinkle Katiyar_3','HH606','789090','5','900','Villa','Modular','Banaras');
/*!40000 ALTER TABLE `vtable` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-08 10:27:30
