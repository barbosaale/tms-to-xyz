# tms-to-xyz
<h3> A python script for converting tiles from TMS to XYZ. </h3>

Original idea from: https://gist.github.com/tmcw/4954720

After creating tiles from a geotiff using gdal2tiles they are created in OSGeo's TMS standard, which may not be supported by some frameworks like Mapbox for example. The difference between XYZ and TMS standards is in inverted Y coordinate.

The script tms-to-xyz.py converts a set of tiles located in the folder informed in the input parameter.

<h4> Instructions for use: </h4>



