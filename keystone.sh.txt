keystone tenant-create --name=admin --description="Admin Tenant"
keystone tenant-create --name=service --description="Service Tenant"
keystone user-create --name=admin --pass=token \
   --email=bhanoori@usc.edu
keystone role-create --name=admin
keystone user-role-add --user=admin --tenant=admin --role=admin
keystone user-role-add --user=admin --tenant=admin --role=_member_