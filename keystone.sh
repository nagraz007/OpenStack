#keystone tenant-create --name=admin --description="Admin Tenant"
#keystone tenant-create --name=service --description="Service Tenant"
#keystone user-create --name=admin --pass=token \
#   --email=bhanoori@usc.edu
#keystone role-create --name=admin
#keystone user-role-add --user=admin --tenant=admin --role=admin
#keystone user-role-add --user=admin --tenant=admin --role=_member_
keystone service-create --name=keystone --type=identity \
  --description="Keystone Identity Service"
keystone endpoint-create \
  --service-id=the_service_id_above \
  --publicurl=http://controller:5000/v2.0 \
  --internalurl=http://controller:5000/v2.0 \
  --adminurl=http://controller:35357/v2.0