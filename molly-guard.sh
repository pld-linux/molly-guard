##
## update $PATH for use with molly-guard
##

# if we're superuser, put molly-guard binaries at the beginning of $PATH
if [ $(id -u) = 0 ]; then
    case $PATH in
        */usr/share/molly-guard/bin*)
            # avoid duplicates
            ;;
        *)
            PATH="/usr/share/molly-guard/bin:$PATH"
            ;;
    esac
fi
