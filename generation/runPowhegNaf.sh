#!/bin/bash


if [ $1 ]
    then
    echo "Running step $1"
else
    echo "Specify step! [1 ISG, 2 UBR, 3 Event Generation]"
    exit
fi

if [ $2 ]
then
    topmass="${2/p/.}d0"
    echo "Top Mass: $topmass"
else
    echo "Top mass parameter missing!"
    exit
fi

powheginput="powheg.input-tmpl"
echo "Generating samples for mass mt = $topmass, file $powheginput"

if [ $1 == 1 ]
then

# compute in parallel importance sampling grid and upper bounding grid
    cat ../config/${powheginput} | sed -e 's/numevts.*/numevts 0/' -e "s/##TOPMASS##/$topmass/g" > powheg.input
    cp ../config/pwgseeds.dat pwgseeds.dat
    for i in {1..250} #NJOBS
    do
      sed -e "s/##JOBNUMBER##/$i/g" -e "s/##PATH##/\/nfs\/dust\/cms\/user\/spanns\/powhegbox\/POWHEG-BOX\/ttJ/g" < ../config/powhegNode.sh-tmpl > powhegNode${i}.sh
      qsub powhegNode${i}.sh
    done

fi


if [ $1 == 3 ]
    then

# generate the events:
    cat ../config/${powheginput} | sed -e "s/##TOPMASS##/$topmass/g" > powheg.input
    for i in {1..250} #NJOBS
    do
      qsub powhegNode${i}.sh
    done

fi

