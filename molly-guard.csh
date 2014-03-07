##
## set up molly-guard aliases
##

# if we're superuser, point reboot/shutdown commands at molly-guard
if ( `id -u` == 0 ) then
    alias halt /usr/sbin/halt
    alias poweroff /usr/sbin/poweroff
    alias reboot /usr/sbin/reboot
    alias shutdown /usr/sbin/shutdown
endif
