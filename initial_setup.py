import os

if os.getuid():
    print "I cannot run as a normal process.. Make me root dude!!!"

print "Switching off Network manager and switching on network service"
os.system("service NetworkManager stop")
os.system("service network start")
os.system("chkconfig NetworkManager off")
os.system("chkconfig network on")

print "Switching off firewalld and starting iptables, making that act as the firewall"
os.system("service firewalld stop")
os.system("service iptables on")
os.system("chkconfig firewalld off")
os.system("chkconfig iptables on")

controller_ip = raw_input("Enter the IP of this node")
compute_ip = raw_input("Enter the ip of the compute node")
controller_hostname = raw_input("Enter the hostname of this node")
compute_hostname = raw_input("Enter the hostname of the compute node")


print "Editing the /etc/hosts file to add the ip and hostnames"

os.system("echo #controller >> /etc/hosts")
cmd = "echo "+ controller_ip " " + controller_hostname
os.system(cmd)

