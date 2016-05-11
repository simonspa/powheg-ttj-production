#!/bin/bash

STARTJOB=1
NJOBS=500
let "MAXJOBS=$STARTJOB+$NJOBS"

if [ $1 ]
    then
    echo "Running step $1"
else
    echo "Specify step! [1 ISG/UBR, 3 Event Generation]"
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
    # produce new seeds:
    # $RANDOM returns a different random integer at each invocation.
    # Nominal range: 0 - 32767 (signed 16-bit integer).

    count=1
    echo
    echo "Generating $MAXJOBS random numbers as seeds for POWHEG."
    > pwgseeds.dat
    while [ "$count" -le $MAXJOBS ]
    do
	number=$RANDOM
	echo $number >> pwgseeds.dat
	let "count += 1"  # Increment count.
    done
    echo "Done."

    # compute in parallel importance sampling grid and upper bounding grid
    cat ../config/${powheginput} | sed -e 's/numevts.*/numevts 0/' -e "s/##TOPMASS##/$topmass/g" > powheg.input

    for (( i=$STARTJOB; i<=$MAXJOBS; i++ ))
    do
      sed -e "s/##JOBNUMBER##/$i/g" -e "s/##PATH##/\/nfs\/dust\/cms\/user\/spanns\/powhegbox\/POWHEG-BOX\/ttJ/g" < ../config/powhegNode.sh-tmpl > powhegNode${i}.sh
      #qsub powhegNode${i}.sh
    done

fi


if [ $1 == 3 ]
    then

    # Generate the events:
    cat ../config/${powheginput} | sed -e "s/##TOPMASS##/$topmass/g" > powheg.input
    for (( i=$STARTJOB; i<=$MAXJOBS; i++ ))
    do
      qsub powhegNode${i}.sh
    done

fi

