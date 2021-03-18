<?php

$host = "localhost";
$dbname = "SFM";
$dbusername = "webclient";
$dbpassword = "wc_boss5";


try{
	$conn = new PDO("mysql:host=$host;dbname=$dbname", $dbusername, $dbpassword);
	echo "Connected to $dbname at $host successfully.";

	if ($_SERVER["REQUEST_METHOD"] == "POST"){

		//Sanitize POST Request Data
		$username = filter_var($_POST["username"],FILTER_SANITIZE_STRING);
		$password = filter_var($_POST["password"],FILTER_SANITIZE_STRING);
	
		//Create SQL Query to poll USFMSUser Table in SFMS database for username provided by webclient
		$sql = "SELECT * FROM SFMSUser WHERE username = :username";
		
		//Generate prepared statement
		$stmt = $conn->prepare($sql);

		//Bind sanitized form data to respective SQL INSERT clause placeholders
		$stmt->bindParam(':username', $username);
		
		//Check if username and password fields are empty
		if ($username == '' || $password == ''){

			echo "Login Failed - Empty Field(s) Present";
			$conn = null;
		}
		else{
			//Execute fully formed prepared statement
			$stmt->execute();

			//Fetch all results of SQL query
			$results = $stmt->fetch();
			$userType = $results[4];							//Save User Type returned by DB to variable
			$db_password = $results[8];							//Save Hashed password returned by DB to variable
			$hashed_password = hash("sha256", $password);		//Hash password recieved from webclient 

			//Compare hashed password from database to hashed password from webclient
			if ($db_password == $hashed_password && $username == $username){

				if ($userType == 'admin'){
					header("Location: admin.html");
					echo "Admin Login Successful";
					$conn = null;
					
				}
				else{
					header("Location: member.html");
					echo "Member Login Successful";
					$conn = null;
					
				}
			}
			else{
				echo "Login Failed - Incorrect Username or Password Supplied";
				$conn = null;
			}	
		}
	}
}
catch (PDOException $pe){
	die("Could not connect to the database $dbname :" . $pe->getMessage());
}

?>

