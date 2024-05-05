sudo apt install rpcbind

rpcinfo

rpcgen -a -C add.x

make -f Makefile.add

sudo ./add_server

sudo ./add_client localhost 10 20
