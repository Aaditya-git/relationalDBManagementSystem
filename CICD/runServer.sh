WORKSPACE=$1
DESTINATION="/var/opt/rdbms/relationalDBManagementSystem/"
SITE_PACKAGES_PATH="/lib/python3.7/site-packages"
sudo rm -rf $DESTINATION
sudo mkdir -p $DESTINATION

sudo cp -rvf $WORKSPACE/* $DESTINATION
sudo chown -R $USER:$USER $SITE_PACKAGES_PATH
echo $DESTINATION > $SITE_PACKAGES_PATH/addProjectPath.pth
# ls -lrt /usr/local/lib/python3.7/site-packages/
ls -lrt $SITE_PACKAGES_PATH

echo "Starting Server..."
cd $DESTINATION/rdbms/
pwd
# python3 manage.py runserver 0.0.0.0:8000
