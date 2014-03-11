##
## update $PATH for use with molly-guard
##

# if we're superuser, put molly-guard binaries at the beginning of $PATH
if ( `id -u` == 0 ) then
    # TODO: avoid duplicates same as in *.sh
    set path = ( /usr/share/molly-guard/bin $path )
endif
