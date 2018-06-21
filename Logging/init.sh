apt-get update 
apt-get install apache2 -y
apt-get install bc -y
apt-get install wget -y
apt-get install screen -y
a2enmod cgi
service apache2 restart

cd /usr/lib/cgi-bin
echo "0" > num.txt
chmod 777 num.txt
touch test.sh
chmod a+x test.sh 
