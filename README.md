# tms-to-xyz
<h3> A python script for converting tiles from TMS to XYZ. </h3>

Original idea from: https://gist.github.com/tmcw/4954720

After creating tiles from a geotiff using gdal2tiles they are created in OSGeo's TMS standard, which may not be supported by some frameworks like Mapbox for example. The difference between XYZ and TMS standards is in inverted Y coordinate.

The script tms-to-xyz.py converts a set of tiles located in the folder informed in the input parameter. Note that the result will only be a change in .PNG file names. After conversion the tiles can be visualized in a layer in Mapbox for example.

<h4> Instructions for use: </h4>

Just run the script with python on terminal passing as parameter the folder containing the tiles

<b>Example:</b>  $ python tms-to-xyz.py C:\tiles 

<i> Back up your tiles before running! </i>

