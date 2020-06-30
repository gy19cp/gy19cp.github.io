<!DOCTYPE html>
<!--Ensures email data inputted into website is transferred safely and securely to PGAdmin database. 
Queries parameterized, coding sanitized and alerts to inform user, all in place to reduce risk of hacking and data loss.-->
<head>
	<title>Project</title>
	
	<link rel="stylesheet" type="text/css" href="map_style.css">
	<script type="text/javascript" src="page_setup.js"></script> <!--Links all functions for page style (header, footer), map (markers), buttons and more.-->
	
</head>

<body>

	<div class = "title">
		<h1>Scotland House Prices</a></h1>
	</div>

	<?php 
	
		array_filter($_POST, 'trim_value'); 
		
		$pattern = "/[^A-Za-z0-9\s\.\:\-\+\!\@\,\'\"]/"; // Special characters filter encodes certain characters, protecting from HTML injection attacks.
		$email		= sanitize('email',FILTER_SANITIZE_SPECIAL_CHARS,$pattern); 
		 
		$pgsqlOptions = "host='localhost' dbname='geog5871' user= $user password= $password"; // Connects to PGAdmin Databse. No sensitive passwords are left in.
		$dbconn = pg_connect($pgsqlOptions) or die ('connection failure'); //Or die statements allow user to see when errors occur.
		
		$inputemail = pg_query($dbconn, "SELECT email FROM clientemails") or die ('Query 1 failed: '.pg_last_error()); // Returns all email data collected.
		$email = pg_fetch_result($inputemail, 0, 0);
		
		$email++; // Increment email by one to create new email row.
		
		$dbconn = pg_connect($pgsqlOptions);
		$insertQuery = pg_prepare($dbconn, "my_query", "INSERT INTO clientemail(email) VALUES($1)"); // Parameterized query, does not allow data to run as a command.
		$result = pg_execute($dbconn, "my_query", array($email))  or die ('Insert Query failed: '.pg_last_error()); 

		
		if (is_null($result))	{
			echo 'Data insert failed, please try again';
		}
		
		else {
			echo 'Data insert successful';
		}
		
		//Close db connection
		pg_close($dbconn);
		
		
		function trim_value(&$value){ // Trim data to remove white spaces from data inputted.
		   $value = trim($value);
		   $pattern = "/[\(\)\[\]\{\}]/";
		   $value = preg_replace($pattern," - ",$value); // Regex replaces brackets with hyphens and removes everything except characters shown.
		}

		function sanitize($str,$filter,$pattern) {
		   $sanStr = preg_replace($pattern,"",$sanStr);
		   $sanStr = filter_var($_POST[$str], $filter);
		   if (strlen($sanStr) > 255) $sanStr = substr($sanStr,0,255); // Truncates array elements that are too long, reduces risk of successful attack.
		   return $sanStr;
		} 
	?>

</body>