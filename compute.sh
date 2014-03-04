#apt-get install nova-novncproxy novnc nova-api \
 # nova-ajax-console-proxy nova-cert nova-conductor \
 # nova-consoleauth nova-doc nova-scheduler \
  #python-novaclient
#keystone user-create --name=nova --pass=token --email=bhanoori@usc.edu
#keystone user-role-add --user=nova --tenant=service --role=admin
#keystone service-create --name=nova --type=compute \
 # --description="Nova Compute service"
#adminid=$(keystone tenant-list | awk '/ admin / {print $2}')
#serviceid=$(keystone tenant-list | awk '/ admin / {print $2}')
#naga="asas"
#public="http://controller:8774/v2/%\$adminid\$serviceid\"
 keystone endpoint-create \
  --service-id=$(keystone service-list | awk '/ compute / {print $2}') \
  --publicurl=http://controller:8774/v2/%\(tenant_id\)s \
  --internalurl=http://controller:8774/v2/%\(tenant_id\)s \
  --adminurl=http://controller:8774/v2/%\(tenant_id\)s