
##
## debianize $PATH for use with molly-guard
##

# if we're superuser, reorder $PATH if it's wrong to get molly-guard working
if [ `/usr/bin/id -u` -eq 0 ]
then
	# switch sbin entries
	PATH=`echo ${PATH} | sed -re 's#(^|:)/sbin(:|.*)/usr/sbin(:|$)#\1/usr/sbin\2/sbin\3#'`
	# switch bin entries
	PATH=`echo ${PATH} | sed -re 's#(^|:)/bin(:|.*)/usr/bin(:|$)#\1/usr/bin\2/bin\3#'`
	export PATH
fi
