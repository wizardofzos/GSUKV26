#!/bin/bash

HOST="192.168.1.141"
USER="IBMUSER"
REMOTE_DIR="'IBMUSER"
LOCAL_FILE="PDS.XMIT"

# Prompt for password securely
read -s -p "Password for $USER: " PASS
echo ""

ftp -inv $HOST <<EOF
user $USER $PASS

cd $REMOTE_DIR

binary

put $LOCAL_FILE

bye
EOF
