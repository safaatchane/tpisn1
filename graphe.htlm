<html>
<head>
<title>Graphe</title>
<meta charset="utf-8"/>
<script type="text/javascript">

function main() {
	var xmin=-10;
	var xmax=10;
	var xgrad= 10;
	var ymin = -10;
	var ymax = 10;
	var ygrad = 1;
	var plot = document.getElementById("curve");
	var pen = plot.getContext("2d");
	var y0 = plot.height*(0-ymax)/(ymin-ymax); 
	var x0= plot.width*(0-xmin)/(xmax-xmin);
	pen.beginPath();
	pen.moveTo(0,y0);
	pen.lineTo(plot.width,y0);
	pen.moveTo(x0,0);
	pen.lineTo(x0,plot.height);
	
	pen.stroke();
	
} 
	

</script>
</head>
<body onload="main()">

<canvas id="curve" width="800" height="450" style= "background: yellow"/>
</body>
</html>
