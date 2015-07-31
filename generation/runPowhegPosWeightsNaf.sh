#!/bin/bash


if [ $1 ]
    then
    echo "Running step $1"
else
    echo "Specify step! [1 ISG, 2 UBR, 3 Event Generation]"
    exit
fi

if [ $2 == "" ]
then
    echo "Top mass parameter missing!"
    exit
fi

topmass=$2
powheginput="powheg.input-tmpl_m${topmass}_posweights"
echo "Generating samples for mass mt = $topmass, file $powheginput"

if [ $1 == 1 ]
then

# compute in parallel importance sampling grid and upper bounding grid
    cat ../config/${powheginput} | sed 's/numevts.*/numevts 0/' > powheg.input
    cp ../config/pwgseeds.dat pwgseeds.dat
    for i in {1..50} #NJOBS
    do
      sed "s/##JOBNUMBER##/$i/g" < ../config/powhegNode.sh-tmpl > powhegNode${i}-tmp.sh
      sed "s/##PATH##/\/nfs\/dust\/cms\/user\/spanns\/powhegbox\/POWHEG-BOX\/ttJ/g" < powhegNode${i}-tmp.sh > powhegNode${i}.sh
      rm powhegNode${i}-tmp.sh
      qsub powhegNode${i}.sh
    done

fi


if [ $1 == 3 ]
    then

# generate the events:
    cat ../config/${powheginput} > powheg.input
    for i in {1..50} #NJOBS
    do
      qsub powhegNode${i}.sh
    done

fi

