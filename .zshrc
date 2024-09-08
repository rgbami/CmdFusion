export PATH="$HOME/bin:$PATH"

# removes laptop name
PS1="%n@ %1~ %# "

function q () {
    ~/bin/cmdshortener.py "$@"
}

