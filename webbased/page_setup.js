//DOCTYPE JavaScript.
// Code is ordered by subheadings to aid understanding and readability.

// MAP 
var map; // Define the Map object.
var myCentreLat = 56.974924; // Starting Latitude position. Majority of markers can be viewed with these specifications. 
var myCentreLng = -4.592285; // Starting Longitude position. 
var initialZoom = 7; // Initial Zoom factor. 
var infowindow; // Global variable.

google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function addMarker(myPos,myTitle,myInfo) { // Determines the marker icon design and location.
   var marker = new google.maps.Marker({ 
	   position: myPos, // Determines the Marker location on map.
	   map: map, 
	   title: myTitle,
	   icon: 'condominium.png' // Determines icon used for the marker.
});
   infowindow = new google.maps.InfoWindow(); // Enables an infowindow to appear. The text is location-specific.  
   google.maps.event.addListener (marker, 'click', function() { // The text is viewed once the marker is clicked.
   infowindow.setContent(myInfo);
   infowindow.open(map, this); // When a separate marker is clicked, the previous infowindow disappears.
})
}
 
function addPoly(polyPath,myInfo,line_colour,fillvalue) { // Polygon style choices.
	myPoly = new google.maps.Polygon({
		paths: polyPath,
		strokeColor: line_colour, 
		strokeOpacity: 0.8,
		strokeWeight: 3,
		fillColor: fillvalue,
		fillOpacity: 0.2
	});
	myPoly.setMap(map); // Polygon set to map. Polygon and marker data is located in 'map_data.js' due to the high quantity of data required for accurate coordinates.
}

			
function initialize() { // Loads local variables (e.g. latlng and myOptions). 
   var latlng = new google.maps.LatLng(myCentreLat,myCentreLng); // Map centres at previously specified latitude and longitudes when opened.
   var myOptions = {
      zoom: initialZoom,
      center: latlng,
      mapTypeId: google.maps.MapTypeId.HYBRID // Type of base map used (others include Terrain).
   };
   map = new google.maps.Map(
      document.getElementById("map_canvas"),myOptions);
	  
   for (id in os_markers) { // For loop enabling location-specific title and average house price by year in each marker infowindow.
        var info = "<div class=infowindow><h1><u>" +
         os_markers[id].title + "</h1></u><p><b>Average House Prices: </b></p><p>"
         + os_markers[id].prices + "</p></div>";

      var osPt = new OSRef( // Convert coordinates Easting-Northing to Latitude-Longitude, using OsRef from JScoord library (see '.jscoord-1.1.1.js' for coding).
         os_markers[id].easting,os_markers[id].northing);
      var llPt = osPt.toLatLng(osPt); // 'toLatLng' from JScoord library, converts points to Latitude and Longitude.
      llPt.OSGB36ToWGS84(); // Changing the Datum used (OS National Grid use a different one (OSGB36) to Google Maps). 
							// 11pt acts as the object where the coordinates and datum are being changed.
      addMarker(new google.maps.LatLng(llPt.lat,llPt.lng), os_markers[id].title,info); // Adds marker with Latitude and Longitude properties.
   }
      
   for (id in os_polydata) { // For loop creating the Polygon with specific data points.  
		var polyPath = []; // Empty array. Points are read through.
		
		var thisBoundary = os_polydata[id].boundary;
		
		for (pt in thisBoundary) { 
			var osPt = new OSRef(thisBoundary[pt].easting, // Convert coordinates Easting-Northing to Latitude-Longitude, using OsRef from JScoord library.
				thisBoundary[pt].northing);
			var llPt = osPt.toLatLng(osPt); // 'toLatLng' from JScoord library, converts points to Latitude and Longitude.
			llPt.OSGB36ToWGS84(); // Changing the Datum used (OS National Grid use a different one (OSGB36) to Google Maps). 
			var myLatLng = new google.maps.LatLng(llPt.lat,llPt.lng); // 11pt acts as the object where the coordinates and datum are being changed.
			polyPath.push(myLatLng); // Constructs the Polygon.
		} 
		var fillvalue = os_polydata[id].value // Colour of each polygon centre is defined in 'value' rows of overlays.js file.
		addPoly(polyPath, info,"#000000",fillvalue); // Adds Polygon with all coordinate points, and determines line colour and fill colour.
	}  
};

// PAGE
 
$(document).ready(function(){ // Sticky navigation bar.
window.onscroll = function() {myFunction()};

var topnav = document.getElementById("topnav");
var sticky = topnav.offsetTop;

function myFunction() {
  if (window.pageYOffset >= sticky) { // Ensures if sticky aspect does not work, navigation bar and associated hyperlinks remain fixed at top of web page.
    topnav.classList.add("sticky")
  } else {
    topnav.classList.remove("sticky");
  }
}
});

function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Year', 'Scotland', 'United Kingdom'],
		  ['2010',	131902,		170365],
		  ['2011',	129489,		167888],
		  ['2012',  125249,		168556],
		  ['2013',	125755,		172890],
		  ['2014',	131664,		186770],
		  ['2015', 	136887,		197890],
		  ['2016', 	138749,		211725],
		  ['2017',  142836,		221403],
		  ['2018',  149104,		228354],
		  ['2019',	152055,		230839],
		  ['2020',	151779,		231049]
        ]);
		
        var options = {
          title: 'Scotland and UK Average House Prices 2010 to 2020 (£)',
          curveType: 'function',
          legend: { position: 'bottom' }
        };

        var chart = new google.visualization.LineChart(document.getElementById('graph'));

        chart.draw(data, options);
      }
	
// Buttons

function LiveIn() { // If 'LiveIn' button clicked, text appears below the buttons and a value of 1 is added to the counter within the text.
	  if (typeof(Storage) !== "undefined") {
		if (localStorage.LiveIn) {
		  localStorage.LiveIn = Number(localStorage.LiveIn)+1; // 1 added to 'Live In:' underneath the buttons.
		} else {
		  localStorage.LiveIn = 1; // Remains at 1 if the button does not work.
		}
		document.getElementById("longterm").innerHTML = "Live In: " + localStorage.LiveIn;
		} else {
		document.getElementById("longterm").innerHTML = "Sorry, your browser does not support web storage..."; // Error message if web storage does not work.
	  }
	};
	
		function Rent() { // If 'Rent' button clicked, text appears below the buttons and a value of 1 is added to the counter within the text.
	  if (typeof(Storage) !== "undefined") {
		if (localStorage.Rent) {
		  localStorage.Rent = Number(localStorage.Rent)+1; // 1 added to 'Rent:' underneath the buttons.
		} else {
		  localStorage.Rent = 1; // Remains at 1 if the button does not work.
		}
		document.getElementById("shortterm").innerHTML = "Rent: " + localStorage.Rent;
		} else {
		document.getElementById("shortterm").innerHTML = "Sorry, your browser does not support web storage..."; // Error message if web storage does not work.
	  }
	};

			function Resell() { // If 'Resell' button clicked, text appears below the buttons and a value of 1 is added to the counter within the text.
	  if (typeof(Storage) !== "undefined") {
		if (localStorage.Resell) {
		  localStorage.Resell = Number(localStorage.Resell)+1; // 1 added to 'Resell for Profit:' underneath the buttons.
		} else {
		  localStorage.Resell = 1; // Remains at 1 if the button does not work.
		}
		document.getElementById("nonresident").innerHTML = "Resell for Profit: " + localStorage.Resell;
		} else {
		document.getElementById("nonresident").innerHTML = "Sorry, your browser does not support web storage..."; // Error message if web storage does not work.
	  }
	};

	
		function Other() { // If 'Other' button clicked, text appears below the buttons and a value of 1 is added to the counter within the text.
	  if (typeof(Storage) !== "undefined") {
		if (localStorage.Other) {
		  localStorage.Other = Number(localStorage.Other)+1; // 1 added to 'Other:' underneath the buttons.
		} else {
		  localStorage.Other = 1; // Remains at 1 if the button does not work.
		}
		document.getElementById("unknown").innerHTML = "Other: " + localStorage.Other;
		} else {
		document.getElementById("unknown").innerHTML = "Sorry, your browser does not support web storage..."; // Error message if web storage does not work.
	  }
	};

// FOOTER
// Email submission box in Footer.
var isEmpty    = function(x) { return x === ""; } // Function to check if field is empty.

var invalid    = function(x) { x.style.backgroundColor = '#ff7e7e'; error = true; }// If field is invalid it is passed here and box turns pink.

var valid      = function(x) { x.style.backgroundColor = "White"; }// If field is valid, passed here, changes field back to white in case of form resubmit.

function validate()	{ // Ensures whether email is inputted successful or unsuccessfully the user is made aware and alerted.

	error 	 	 = false; 
	var emailbox = document.getElementsByClassName('boxes');
	var emailaddress = document.getElementById('email'); 

	for (var i=0;i<emailbox.length;i++) { // Clear pink highlighting in case form is resubmitted 
		valid(emailbox[i]); 
	}
	
	for (var i=0;i<emailbox.length;i++) { // For loop through all fields to check if Email submission box is empty. 
		if	(isEmpty(emailbox[i].value))	{
			invalid(emailbox[i]); 
		}
	} 
		
	if (error) { // If error, return false and alerts user. User has to select 'ok' on alert to ensure reads alert.
	alert("Please check email address for Errors and Resubmit. Thanks!");
		return false; 
	} 
	
	else 	{ // Submit form if there are no errors. Page refreshes.
		alert("Thanks for signing up to the mailing list!");
		return true; 
		 ;
	} 
}

