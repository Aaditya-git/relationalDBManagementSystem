WORKSPACE=$1
DESTINATION="/var/opt/rdbms/relationalDBManagementSystem/"
sudo rm -rf $DESTINATION
sudo mkdir -p $DESTINATION

sudo cp -rvf $WORKSPACE/* $DESTINATION
sudo chown -R $USER:$USER /usr/local/lib/python3.7/site-packages
echo "/var/opt/rdbms/relationalDBManagementSystem" > /usr/local/lib/python3.7/site-packages/addProjectPath.pth
ls -lrt /usr/local/lib/python3.7/site-packages/
echo "Starting Server..."
cd $DESTINATION/rdbms/
pwd
# python3 manage.py runserver 0.0.0.0:8000
