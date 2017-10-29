CREATE DATABASE IF NOT EXISTS `BostonHacks` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `BostonHacks`;

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
  `cat_id` int(11) NOT NULL  AUTO_INCREMENT,
  `cat_name` text NOT NULL,
  `cat_parent` text NOT NULL,
  Primary Key(cat_id)
);

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `virtual_assistant`;
CREATE TABLE `virtual_assistant` (
  `va_id` varchar(14) NOT NULL,
  `va_name` text NOT NULL,
  `va_address` text NOT NULL,
  Primary key(va_id)
) ;

-- --------------------------------------------------------
--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `u_id` varchar(14) NOT NULL,
  `name` text NOT NULL,
  PRIMARY KEY (u_id)
);

--
-- Table structure for table `problems`
--

DROP TABLE IF EXISTS `problems`;
CREATE TABLE `problems` (
  `p_id` int(11) NOT NULL  AUTO_INCREMENT,
  `u_id` varchar(14) NOT NULL,
  `cat_id` int(11) NOT NULL,
  `details` text NOT NULL,
  `va_id` varchar(14) NOT NULL,
  `va_input` text NOT NULL,
  Primary key(p_id),
  Foreign key(u_id) REFERENCES User(u_id),
  Foreign key(va_id) REFERENCES virtual_assistant(va_id),
  Foreign key(cat_id) REFERENCES category(cat_id)
);

-- --------------------------------------------------------

--
-- Table structure for table `specialization`
--

DROP TABLE IF EXISTS `specialization`;
CREATE TABLE `specialization` (
  `va_id` varchar(14) NOT NULL,
  `cat_id` int(11) NOT NULL,
  Primary key(va_id,cat_id),
  Foreign key(va_id) REFERENCES virtual_assistant(va_id),
    Foreign key(cat_id) REFERENCES category(cat_id)
) ;

-- --------------------------------------------------------
--
-- Table structure for table 'schedule'
--
DROP TABLE IF EXISTS `schedule`;
CREATE TABLE `schedule` (
  `va_id` varchar(14) NOT NULL,
  `va_day` varchar(4) NOT NULL,
  `start_hr` int(2) NOT NULL,
  `start_min` int(2) NOT NULL,
  `end_hr` int(2) NOT NULL,
  `end_min` int(2) NOT NULL,
  PRIMARY KEY(va_id,va_day),
  Foreign key(va_id) REFERENCES virtual_assistant(va_id)
);
Insert into virtual_assistant Values('+16179552483','John Einstein','1167 Boylston Street,Boston, MA 02215');
Insert into virtual_assistant Values('+18572058079','Ruturaj Nene','1171 Boylston Street,Boston, MA 02215');
Insert into virtual_assistant Values('+919987874666','Pranav Raikundalia','Malad, Mumbai 400064');

Insert into category(cat_name,cat_parent) Values('Orthopedic','doctor');
Insert into category(cat_name,cat_parent) Values('General','doctor');
Insert into category(cat_name,cat_parent) Values('Cardiologist','doctor');
Insert into category(cat_name,cat_parent) Values('Pediatrician','doctor');
Insert into category(cat_name,cat_parent) Values('Maternity Care','doctor');
Insert into category(cat_name,cat_parent) Values('Psychiatrist','doctor');
Insert into category(cat_name,cat_parent) Values('Chemistry','tutor');
Insert into category(cat_name,cat_parent) Values('Biology','tutor');
Insert into category(cat_name,cat_parent) Values('Physics','tutor');
Insert into category(cat_name,cat_parent) Values('Maths','tutor');
Insert into category(cat_name,cat_parent) Values('Computer Science','tutor');
Insert into category(cat_name,cat_parent) Values('History','tutor');
Insert into category(cat_name,cat_parent) Values('Economics','tutor');
Insert into category(cat_name,cat_parent) Values('Java','coder');
Insert into category(cat_name,cat_parent) Values('C/C++','coder');
Insert into category(cat_name,cat_parent) Values('Python','coder');
Insert into category(cat_name,cat_parent) Values('R','coder');
Insert into category(cat_name,cat_parent) Values('Rackets/Scheme','coder');
Insert into category(cat_name,cat_parent) Values('MySQL','coder');
Insert into category(cat_name,cat_parent) Values('PHP','coder');
Insert into category(cat_name,cat_parent) Values('Shell','coder');



Insert into specialization Values('+16179552483','1');
Insert into specialization Values('+16179552483','2');
Insert into specialization Values('+16179552483','3');
Insert into specialization Values('+16179552483','4');
Insert into specialization Values('+16179552483','5');
Insert into specialization Values('+16179552483','6');
Insert into specialization Values('+18572058079','7');
Insert into specialization Values('+18572058079','8');
Insert into specialization Values('+18572058079','9');
Insert into specialization Values('+18572058079','10');
Insert into specialization Values('+18572058079','11');
Insert into specialization Values('+18572058079','12');
Insert into specialization Values('+18572058079','13');
Insert into specialization Values('+919987874666','14');
Insert into specialization Values('+919987874666','15');
Insert into specialization Values('+919987874666','16');
Insert into specialization Values('+919987874666','17');
Insert into specialization Values('+919987874666','18');
Insert into specialization Values('+919987874666','19');
Insert into specialization Values('+919987874666','20');
Insert into specialization Values('+919987874666','21');

Insert into schedule Values('+16179552483','Sun','00','00','05','00');
Insert into schedule Values('+18572058079','Sun','10','00','17','00');
Insert into schedule Values('+919987874666','Sun','10','00','17','00');

Insert into virtual_assistant Values('+16178299091','Hardik Shah','1187 Boylston Street,Boston, MA 02215');
Insert into schedule Values('+16178299091','Sun','10','00','17','00');
Insert into specialization Values('+16178299091','1');
Insert into specialization Values('+16178299091','2');
Insert into specialization Values('+16178299091','3');
Insert into specialization Values('+16178299091','4');
Insert into specialization Values('+16178299091','5');
Insert into specialization Values('+16178299091','6');