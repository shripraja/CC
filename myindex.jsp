myindex.jsp
<%@page contentType="text/html" pageEncoding="UTF-8"%> 
<!DOCTYPE html> 
<html> 
<head> 
    <title>Google Map Location</title> 
 
    <style> 
        #map { 
            height: 400px; 
            width: 100%; 
        } 
    </style> 
 
    <script async defer 
        
src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=
initMap"> 
    </script> 
</head> 
 
<body> 
 
<% 
    double lati = 40.7128; 
    double longi = -74.0060; 
 
    try { 
        String latParam = request.getParameter("t1"); 
        String longParam = request.getParameter("t2"); 
 
        if (latParam != null && !latParam.isEmpty()) 
            lati = Double.parseDouble(latParam); 
 
        if (longParam != null && !longParam.isEmpty()) 
            longi = Double.parseDouble(longParam); 
    } catch (Exception e) { 
        // default location 
    } 
%> 
 
<h3>Google Maps Location</h3>
<div id="map"></div> 
 
<script> 
function initMap() { 
    var location = { lat: <%=lati%>, lng: <%=longi%> }; 
 
    var map = new google.maps.Map(document.getElementById("map"), { 
        zoom: 12, 
        center: location 
    }); 
 
    new google.maps.Marker({ 
        position: location, 
        map: map 
    }); 
} 
</script>
myinput.jsp
<%@page contentType="text/html" pageEncoding="UTF-8"%> 
<!DOCTYPE html> 
<html> 
<head> 
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"> 
    <title>Enter Latitude and Longitude</title> 
</head> 
 
<body> 
 
<!-- Form to accept input values for latitude and longitude --> 
<form action="myindex.jsp" method="get"> 
    <pre> 
Enter Latitude  : <input type="number" step="any" name="t1"/> 
Enter Longitude : <input type="number" step="any" name="t2"/> 
 
<input type="submit" value="Show Map"/> 
    </pre> 
</form> 
