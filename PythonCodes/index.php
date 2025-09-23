<?php

DEFINE("IMAGEROOT", "/images/");  #CHANGE /images/ TO THE PATH OF THE ASSOCIATED IMAGES

$textcolor = "#006699";           #TEXT COLOUR
$bgcolor = "#FFFFFF";             #PAGE BACKGROUND COLOUR

$normalcolor = "#FFFFFF";         #TABLE ROW BACKGROUND COLOUR
$highlightcolor = "#FFFFFF";      #TABLE ROW BACKGROUND COLOUR WHEN HIGHLIGHTED
$headercolor = "#FFFFFF";         #TABLE HEADER BACKGROUND COLOUR
$bordercolor = "#FFFFFF";         #TABLE BORDER COLOUR

?>
<html>
<head>
<title>Directory Listings of <? echo $_SERVER["REQUEST_URI"]; ?> </title>
<style type='text/css'>
<!--
body {     color: <? echo $textcolor; ?>; font: tahoma, small verdana,arial,helvetica,sans-serif; background-color: <? echo $bgcolor; ?>; }
table { font-family: tahoma, Verdana, Geneva, sans-serif; font-size: 10pt; border: 1px; border-style: solid; border-color: <? echo $bordercolor; ?>; }
.row { background-color: <? echo $normalcolor; ?>; border: 0px;}
a:link { color: <? echo $textcolor; ?>;  text-decoration: none; } 
a:visited { color: <? echo $textcolor; ?>;  text-decoration: none; } 
a:hover, a:active { color: <? echo $textcolor; ?>;  text-decoration: underline; } 
img {border: 0;}
#bottomborder {border: <? echo $bordercolor;?>;border-style: solid;border-top-width: 0px;border-right-width: 0px;border-bottom-width: 1px;border-left-width: 0px}
.copy { text-align: center; color: <? echo $textcolor; ?>; font-family: tahoma, Verdana, Geneva, sans-serif;  font-size: 10pt; text-decoration: underline; }
//-->
</style>
</head>
<body>
<?php
clearstatcache();
if ($handle = opendir('.')) {
  while (false !== ($file = readdir($handle))) { 
    if ($file != "." && $file != ".." && $file != substr($PHP_SELF, -(strlen($PHP_SELF) - strrpos($PHP_SELF, "/") - 1))) { 
      
	  if (filetype($file) == "dir") {
		  //SET THE KEY ENABLING US TO SORT
		  $n++;
		  if($_REQUEST['sort']=="date") {
			$key = filemtime($file) . ".$n";
		  }
		  else {
			$key = $n;
		  }
          $dirs[$key] = $file . "/";
      }
      else {
		  //SET THE KEY ENABLING US TO SORT
		  $n++;
		  if($_REQUEST['sort']=="date") {
			$key = filemtime($file) . ".$n";
		  }
		  elseif($_REQUEST['sort']=="size") {
			$key = filesize($file) . ".$n";
		  }
		  else {
			$key = $n;
		  }
          $files[$key] = $file;
      }
    }
  }
closedir($handle); 
}

#USE THE CORRECT ALGORITHM AND SORT OUR ARRAY
if($_REQUEST['sort']=="date") {
	@ksort($dirs, SORT_NUMERIC);
	@ksort($files, SORT_NUMERIC);
}
elseif($_REQUEST['sort']=="size") {
	@natcasesort($dirs); 
	@ksort($files, SORT_NUMERIC);
}
else {
	@natcasesort($dirs); 
	@natcasesort($files);
}

#ORDER ACCORDING TO ASCENDING OR DESCENDING AS REQUESTED
if($_REQUEST['order']=="desc" && $_REQUEST['sort']!="size") {$dirs = array_reverse($dirs);}
if($_REQUEST['order']=="desc") {$files = array_reverse($files);}
$dirs = @array_values($dirs); $files = @array_values($files);

echo "<table width=\"450\" border=\"0\" cellspacing=\"0\" align=\"center\"><tr bgcolor=\"$headercolor\"><td colspan=\"2\" id=\"bottomborder\">";
if($_REQUEST['sort']!="name") {
  echo "<a href=\"".$_SERVER['PHP_SELF']."?sort=name&order=asc\">";
}
else {
  if($_REQUEST['order']=="desc") {#
    echo "<a href=\"".$_SERVER['PHP_SELF']."?sort=name&order=asc\">";
  }
  else {
    echo "<a href=\"".$_SERVER['PHP_SELF']."?sort=name&order=desc\">";
  }
}
echo "File</td><td id=\"bottomborder\" width=\"50\"></a>";
if($_REQUEST['sort']!="size") {
  echo "<a href=\"".$_SERVER['PHP_SELF']."?sort=size&order=asc\">";
}
else {
  if($_REQUEST['order']=="desc") {#
    echo "<a href=\"".$_SERVER['PHP_SELF']."?sort=size&order=asc\">";
  }
  else {
    echo "<a href=\"".$_SERVER['PHP_SELF']."?sort=size&order=desc\">";
  }
}
echo "Size</td><td id=\"bottomborder\" width=\"120\" nowrap></a>";
if($_REQUEST['sort']!="date") {
  echo "<a href=\"".$_SERVER['PHP_SELF']."?sort=date&order=asc\">";
}
else {
  if($_REQUEST['order']=="desc") {#
    echo "<a href=\"".$_SERVER['PHP_SELF']."?sort=date&order=asc\">";
  }
  else {
    echo "<a href=\"".$_SERVER['PHP_SELF']."?sort=date&order=desc\">";
  }
}
echo "Date Modified</a></td></tr>";

$arsize = sizeof($dirs);
for($i=0;$i<$arsize;$i++) {
  echo "\t<tr class=\"row\" onMouseOver=\"this.style.backgroundColor='$highlightcolor'; this.style.cursor='hand';\" onMouseOut=\"this.style.backgroundColor='$normalcolor';\" onClick=\"window.location.href='" . $dirs[$i] . "';\">";
  echo "\t\t<td width=\"16\"><img src=\"" . IMAGEROOT . "folder.gif\" width=\"16\" height=\"16\" alt=\"Directory\"></td>";
  echo "\t\t<td><a href=\"" . $dirs[$i] . "\">" . $dirs[$i] . "</a></td>";
  echo "\t\t<td width=\"50\" align=\"left\">-</td>";
  echo "\t\t<td width=\"120\" align=\"left\" nowrap>" . date ("M d Y h:i:s A", filemtime($dirs[$i])) . "</td>";
  echo "\t</tr>";
}

$arsize = sizeof($files);
for($i=0;$i<$arsize;$i++) {
  
  echo "\t<tr class=\"row\" onMouseOver=\"this.style.backgroundColor='$highlightcolor'; this.style.cursor='hand';\" onMouseOut=\"this.style.backgroundColor='$normalcolor';\" onClick=\"window.location.href='" . $files[$i] . "';\">\r\n";
  echo "\t\t<td width=\"16\"></td>\r\n";
  echo "\t\t<td><a href=\"" . $files[$i] . "\">" . $files[$i] . "</a></td>\r\n";
  echo "\t\t<td width=\"50\" align=\"left\">" . round(filesize($files[$i])/1024) . "KB</td>\r\n";
  echo "\t\t<td width=\"120\" align=\"left\" nowrap>" . date ("M d Y h:i:s A", filemtime($files[$i])) . "</td>\r\n";
  echo "\t</tr>\r\n";
}
?>
</body>
</html>