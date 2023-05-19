#!/bin/bash

#name=null
code="hello"
#pos=true
argument=$1
read -r name
echo "---------"
#echo $code
#echo $name

if [ "$name" = "$code" ]; then
   echo "123"
else
   echo "$argument"

fi


#echo "$argument"
#echo "$name"
