retry() {
    counter=1
    maxtries=$1; shift;
    delay=$1; shift;
    echo Retrying "$@" with maxtries:$maxtries and delay:$delay
    while [[ $counter -le $maxtries ]]; do
        $@
        if [[ "$?" = "0" ]]; then
            break
        else
            >&2 echo Failed attempt $counter/$maxtries
            ((counter++))
            sleep $delay
        fi
    done
    if [[ $counter -gt $maxtries ]]; then
        >&2 echo FAILED
        return 1
    fi
}
