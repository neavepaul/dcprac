sudo apt install rpcbind

rpcinfo

rpcgen -a -C add.x

make -f Makefile.add

add the logic to the server and client files if not there alr

sudo ./add_server

sudo ./add_client localhost 10 20
