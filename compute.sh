#apt-get install nova-novncproxy novnc nova-api \
  nova-ajax-console-proxy nova-cert nova-conductor \
  nova-consoleauth nova-doc nova-scheduler \
  python-novaclient
#keystone user-create --name=nova --pass=token --email=bhanoori@usc.edu
#keystone user-role-add --user=nova --tenant=service --role=admin
keystone service-create --name=nova --type=compute \
  --description="Nova Compute service"
keystone endpoint-create \
  --service-id=$(keystone service-list | awk '/ compute / {print $2}') \
  --publicurl=http://controller:5000/v2.0 \
  --internalurl=http://controller:5000/v2.0 \
  --adminurl=http://controller:35357/v2.0