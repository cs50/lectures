# flask
export FLASK_APP=application.py
export FLASK_DEBUG=1
function flask()
{
    if [[ "$1" == "run" ]]; then
        command flask run --host=0.0.0.0 --port=8080 --with-threads "${@:2}"
    else
        command flask "$@"
    fi
}
