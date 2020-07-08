#!/bin/bash

lucky(){
  count=$1

  read tmp
  declare -a data=($tmp)
  declare -a sub

  echo $tmp
  flag=0
  while ((flag==0))
  do
    unset sub
    declare -a sub
    for i in "${data[@]}"
    do
      ((RANDOM%6+1 > 3)) && sub+=($i)
    done

    if [ ${#sub[@]} == $count ]; then
       echo "${sub[@]}"
       flag=1
       break
    elif [ ${#sub[@]} -lt $count ]; then
       echo "${sub[@]}"
    else
       data=(${sub[@]})
    fi
  done
}

