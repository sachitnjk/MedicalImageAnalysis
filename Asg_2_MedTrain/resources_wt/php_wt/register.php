<?php
$email = $_POST['email'];
$usn = $_POST['usn'];
$pwd = $_POST['pwd'];

if (!empty($email) || !empty($usn) || !empty($pwd)){
	$host = "localhost";
	$dbusername = "root";
	$dbpassword = "";
	$dbname = "utrain";

	// creating connection
	$conn = new mysqli($host, $dbusername, $dbpassword, $dbname);
	if(mysqli_connect_error()){
		die('Connect Error('.mysql_errno().')'.mysqli_connect_error());
	} else {
		$SELECT = "SELECT email from register where email = ? Limit 1";
		$INSERT = "INSERT Into register (email, usn, pwd) values(?, ?, ?)";

		//Prepare Statement
		$stmt = $conn->prepare($SELECT);
		$stmt->bind_param("s", $email);
		$stmt->execute();
		$stmt->bind_result($email);
        $stmt->store_result();
        $rnum = $stmt->num_rows;


        if ($rnum==0){
        	$stmt->close();

        	$stmt = $conn->prepare($INSERT);
        	$stmt->bind_param("sss", $email, $usn, $pwd);
        	$stmt->execute();
        	echo "New record inserted sucessfully";
        } else {
        	echo "Someone already registered using this email";
        } 

        $stmt ->close();
        $conn ->close();
	}
else {
    echo "All fields are required"
        die();	
	}
}	
?>

