#!/usr/bin/bash
d=$(date)
QUERY_STRING="$1 $2 $3 $4 $5 $6 $7 $8 $9"
echo '<html><body bgcolor="blue">'
./cgi-bin/$QUERY_STRING
echo '</body></html>'



