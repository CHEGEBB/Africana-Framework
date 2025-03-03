import sys
import time
import subprocess
from src.core.bcolors import *

torstring = ['# Created by africana-framework. Delete at your own risk!', '', 'VirtualAddrNetworkIPv4 10.192.0.0/10', 'AutomapHostsOnResolve 1',
              'TransPort 9040 IsolateClientAddr IsolateClientProtocol IsolateDestAddr IsolateDestPort', 'DNSPort 5353', 'CookieAuthentication 1']

privoxystring = ['# Created by africana-framework. Delete at your own risk!', '', 'confdir /etc/privoxy', 'logdir /var/log/privoxy', 'logfile logfile', 'debug   4096 ', 'debug   8192', 'user-manual /usr/share/doc/privoxy/user-manual',
              'actionsfile default.action', 'actionsfile user.action', 'filterfile default.filter', 'listen-address  127.0.0.1:8118', 'toggle  1', 'enable-remote-toggle 0',
              'enable-edit-actions 0', 'enable-remote-http-toggle 0', 'buffer-limit 4096', 'forward-socks5t   /               127.0.0.1:9050 .']

squidstring = ['# Created by africana-framework. Delete at your own risk!', '','acl manager proto cache_object', 'acl localhost src 127.0.0.1/32 ::1', 'acl to_localhost dst 127.0.0.0/8 0.0.0.0/32 ::1', 'acl ftp proto FTP', 'acl localnet src 10.0.0.0/8', 'acl localnet src 172.16.0.0/12',
              'acl localnet src 192.168.0.0/16', 'acl localnet src fc00::/7', 'acl localnet src fe80::/10', 'acl SSL_ports port 443', 'acl Safe_ports port 80 ', 'acl Safe_ports port 21',
              'acl Safe_ports port 443', 'acl Safe_ports port 70', 'acl Safe_ports port 210', 'acl Safe_ports port 1025-65535', 'acl Safe_ports port 280', 'acl Safe_ports port 488', 'acl Safe_ports port 591', 'acl Safe_ports port 777',
              'acl Safe_ports port 3128', 'acl CONNECT method CONNECT', 'http_access allow manager localhost', 'http_access deny manager', 'http_access deny !Safe_ports', 'http_access deny CONNECT !SSL_ports',
              'http_access allow localhost', 'http_access allow all', 'http_port 3128', 'hierarchy_stoplist cgi-bin ?', 'cache_peer 127.0.0.1 parent 8118 7 no-query no-digest', 'coredump_dir /var/spool/squid', 
              'refresh_pattern ^ftp:           1440    20%     10080','refresh_pattern ^gopher:        1440    0%      1440', 'refresh_pattern -i (/cgi-bin/|\?) 0     0%      0', 'refresh_pattern .               0       20%     4320',
              'httpd_suppress_version_string on', 'forwarded_for off', 'always_direct allow ftp', 'never_direct allow all']
dhclientstring = ['# Created by africana-framework. Delete at your own risk!', '', 'option rfc3442-classless-static-routes code 121 = array of unsigned integer 8;', 'send host-name = gethostname();', 'request subnet-mask, broadcast-address, time-offset, routers,', ' domain-name, domain-name-servers, domain-search, host-name,',
              '	dhcp6.name-servers, dhcp6.domain-search, dhcp6.fqdn, dhcp6.sntp-servers,', '    netbios-name-servers, netbios-scope, interface-mtu,', '	rfc3442-classless-static-routes, ntp-servers;', 'prepend domain-name-servers 127.0.0.1,1.1.1.1, 1.0.0.1, 8.8.8.8, 8.8.4.4;']

changemacstring = ['# Created by africana-framework. Delete at your own risk!', '', '[Unit]', 'Description=changes mac for %I', 'Wants=network.target', 'Before=network.target', 'BindsTo=sys-subsystem-net-devices-%i.device', 'After=sys-subsystem-net-devices-%i.device', '', '[Service]', 'Type=oneshot', 'ExecStart=/usr/bin/macchanger -r %I', 'RemainAfterExit=yes',
                   '', '[Install]', 'WantedBy=multi-user.target']

resolvstring = ['# Created by africana-framework. Delete at your own risk!', 'nameserver 1.1.1.1', 'nameserver 1.0.0.1', 'nameserver 8.8.8.8', 'nameserver 8.8.4.4']

class configure(object):
    def __init__(self):
        pass
    while True:
        try:
            if os.path.exists('/etc/tor/torrc.bak_africana'):
                print(f"{bcolors.BLUE}      [  {bcolors.CYAN}    Your system is already configured to be anonymous    {bcolors.GREEN} [ x ] {bcolors.BLUE} ]{bcolors.ENDC}")
            else:
                return config.onfigure_all()
                sys.exit(0) 
        except:
            break
    def configure_all(self):
        if os.system("which tor > /dev/null") == 0:
            if not os.path.exists('/etc/tor/torrc'):
                print(f"{bcolors.BLUE}      [             {bcolors.YELLOW}Torrc file is configured               {bcolors.BLUE} ] {bcolors.ENDC}")
                try:
                    f = open('/etc/tor/torrc', 'w+')
                    for elements in torstring:
                        f.write("%s\n" % elements)
                    f.close()
                    print(f"{bcolors.BLUE}      [                                           {bcolors.CYAN}{bcolors.GREEN}[ ✔ ] {bcolors.BLUE} ]{bcolors.ENDC}")
                except Exception as e:
                    print(f"{bcolors.BLUE}      [             {bcolors.RED}Failed to write the torrc file          {bcolors.BLUE} ] {bcolors.ENDC} \n {e} ")
                    pass
            else:
                print(f"\n{bcolors.BLUE}      [              {bcolors.YELLOW}Configuring Torrc                   {bcolors.BLUE}]{bcolors.ENDC}")
                time.sleep(0.4)
                subprocess.Popen(["cp", "/etc/tor/torrc", "/etc/tor/torrc.bak_africana"], stdout=subprocess.PIPE).communicate()
                torrc = open('/etc/tor/torrc', 'w')
                for elements in torstring:
                    torrc.write("%s\n" % elements)
                torrc.close()
                print(f"\n{bcolors.BLUE}      [  {bcolors.CYAN}                                        {bcolors.GREEN}[ ✔ ] {bcolors.BLUE} ]{bcolors.ENDC}")

        else:
            print(f"\n{bcolors.BLUE}      [         {bcolors.RED}No! Tor try 'apt install tor'           {bcolors.BLUE} ] {bcolors.ENDC}")
            print(f"{bcolors.BLUE}      [  {bcolors.CYAN}                                        {bcolors.GREEN} [ x ] {bcolors.BLUE} ]{bcolors.ENDC}")
            pass

        infile = "/lib/systemd/system/tor@default.service"
        outfile = "/lib/systemd/system/tor@default.service"
        delete_list = ['# Created by africana-framework. Delete at your own risk!\n', '[Install]\n', 'WantedBy=multi-user.target']
        fin = open(infile)
        os.remove("/lib/systemd/system/tor@default.service")
        fout = open(outfile, "w+")
        for line in fin:
            for word in delete_list:
                line = line.replace(word, '')
            fout.write(line)
        fin.close()
        fout.close()

        os.system('echo -n "\n# Created by africana-framework. Delete at your own risk!\n" >> "/lib/systemd/system/tor@default.service"')
        infile = "/lib/systemd/system/tor@default.service"
        outfile = "/lib/systemd/system/tor@default.service"
        delete_list = ['# Created by africana-framework. Delete at your own risk!\n']
        fin = open(infile)
        os.remove("/lib/systemd/system/tor@default.service")
        fout = open(outfile, "w+")
        for line in fin:
            for word in delete_list:
                line = line.replace(word, '# Created by africana-framework. Delete at your own risk!\n[Install]\nWantedBy=multi-user.target')
            fout.write(line)
        fin.close()
        fout.close()

        if os.system("which privoxy > /dev/null") == 0:
            if not os.path.exists('/etc/privoxy/config'):
                print(f"{bcolors.BLUE}      [           {bcolors.YELLOW}No privoxy/config file is configured        {bcolors.BLUE} ] {bcolors.ENDC}")
                try:
                    f = open('/etc/privoxy/config', 'w+')
                    for elements in privoxytring:
                        f.write("%s\n" % elements)
                    f.close()
                    print(f"{bcolors.BLUE}      [  {bcolors.CYAN}                                        {bcolors.GREEN} [ ✔ ] {bcolors.BLUE} ]{bcolors.ENDC}")
                except Exception as e:
                    print(f"{bcolors.BLUE}      [        {bcolors.YELLOW}  Failed to write the privoxy/config file.    {bcolors.BLUE} ] {bcolors.ENDC}\n {e}")
                    print(f"{color(bcolors.RED)}{bcolors.ENDC} ")
                    pass
            else:
                print(f"{bcolors.BLUE}      [         {bcolors.YELLOW}Configuring privoxy/config.             {bcolors.BLUE} ] {bcolors.ENDC}")
                time.sleep(0.4)
                subprocess.Popen(["cp", "/etc/privoxy/config", "/etc/privoxy/config.bak_africana"], stdout=subprocess.PIPE).communicate()
                privoxy = open('/etc/privoxy/config', 'w')
                for elements in privoxystring:
                    privoxy.write("%s\n" % elements)
                privoxy.close()
                print(f"{bcolors.BLUE}      [  {bcolors.CYAN}                                        {bcolors.GREEN} [ ✔ ] {bcolors.BLUE} ]{bcolors.ENDC}")

        else:
            print(f"{bcolors.BLUE}      [     {bcolors.RED}No! privoxy try 'apt install privoxy'      {bcolors.BLUE}  ] {bcolors.ENDC}")
            print(f"{bcolors.BLUE}      [  {bcolors.CYAN}                                        {bcolors.GREEN} [ x ] {bcolors.BLUE} ]{bcolors.ENDC}")
            pass

        if os.system("which squid > /dev/null") == 0:
            if not os.path.exists('/etc/squid/squid.conf'):
                print(f"{bcolors.BLUE}      [        {bcolors.RED} No squid/config file is configured.  {bcolors.BLUE} ] {bcolors.ENDC}")
                try:
                    f = open('/etc/squid/squid.conf', 'w+')
                    for elements in squidstring:
                        f.write("%s\n" % elements)
                    f.close()
                    print(f"{bcolors.BLUE}      [  {bcolors.CYAN}                                        {bcolors.GREEN} [ ✔ ] {bcolors.BLUE} ]{bcolors.ENDC}")
                except Exception as e:
                    print(f"{bcolors.BLUE}      [        {bcolors.RED} Failed to write the squid/config file  {bcolors.BLUE} ] {bcolors.ENDC} \n {e}")
                    pass
            else:
                print(f"{bcolors.BLUE}      [        {bcolors.YELLOW} Configuring Squid/config  {bcolors.BLUE}                   ] {bcolors.ENDC}")
                time.sleep(0.4)
                subprocess.Popen(["cp", "/etc/squid/squid.conf", "/etc/squid/config.bak_africana"], stdout=subprocess.PIPE).communicate()
                squid = open('/etc/squid/squid.conf', 'w')
                for elements in squidstring:
                    squid.write("%s\n" % elements)
                squid.close()
                print(f"{bcolors.BLUE}      [  {bcolors.CYAN}                                        {bcolors.GREEN} [ ✔ ] {bcolors.BLUE} ]{bcolors.ENDC}")

        else:
            print(f"{bcolors.BLUE}      [      {bcolors.RED}No! Squid try 'apt install squid'           {bcolors.BLUE}] {bcolors.ENDC}")
            print(f"{bcolors.BLUE}      [  {bcolors.CYAN}                                        {bcolors.GREEN} [ x ] {bcolors.BLUE} ]{bcolors.ENDC}")
            pass

        if os.system("which dhclient > /dev/null") == 0:
            if not os.path.exists('/etc/dhcp/dhclient.conf'):
                print(f"{bcolors.BLUE}      [{bcolors.YELLOW} No dhclient.conf file is configured.   {bcolors.BLUE}] {bcolors.ENDC}")
                try:
                    f = open('/etc/dhcp/dhclient.conf', 'w+')
                    for elements in dhclientstring:
                        f.write("%s\n" % elements)
                    f.close()
                    print(f"{bcolors.BLUE}      [  {bcolors.CYAN}                                        {bcolors.GREEN} [ ✔ ] {bcolors.BLUE} ]{bcolors.ENDC}")
                except Exception as e:
                    print(f"{bcolors.BLUE}      [        {bcolors.RED} Failed to write the dhclient.conf file {bcolors.BLUE}                   ] {bcolors.ENDC}\n {e}")
                    pass
            else:
                print(f"{bcolors.BLUE}      [      {bcolors.YELLOW} Configuring dhclient.conf file {bcolors.BLUE}            ]{bcolors.ENDC}")
                time.sleep(0.4)
                subprocess.Popen(["cp", "/etc/dhcp/dhclient.conf", "/etc/dhcp/dhclient.bak_africana"], stdout=subprocess.PIPE).communicate()
                dhclient = open('/etc/dhcp/dhclient.conf', 'w')
                for elements in dhclientstring:
                    dhclient.write("%s\n" % elements)
                dhclient.close()
                print(f"{bcolors.BLUE}      [  {bcolors.CYAN}                                        {bcolors.GREEN} [ ✔ ] {bcolors.BLUE} ]{bcolors.ENDC}")

        else:
            print(f"{bcolors.BLUE}      [  {bcolors.RED}No! dhcp try 'apt install isc-dhcp-client'      {bcolors.BLUE}]{bcolors.ENDC}")
            print(f"{bcolors.BLUE}      [  {bcolors.CYAN}                                        {bcolors.GREEN} [ x ] {bcolors.BLUE} ]{bcolors.ENDC}")
            pass

        if os.system("which macchanger > /dev/null") == 0:
            if not os.path.exists('/etc/systemd/system/changemac@.service'):
                print(f"{bcolors.BLUE}      [        {bcolors.RED} No changemac@.service file is configured. Configuring:) {bcolors.BLUE}            ] {bcolors.ENDC}")
                try:
                    f = open('/etc/systemd/system/changemac@.service', 'w+')
                    for elements in changemacstring:
                        f.write("%s\n" % elements)
                    f.close()
                    print(f"{bcolors.BLUE}      [  {bcolors.CYAN}                                        {bcolors.GREEN} [ ✔ ] {bcolors.BLUE} ]{bcolors.ENDC}")
                except Exception as e:
                    print(f"{bcolors.BLUE}      [        {bcolors.RED} Failed to write the changemac@.service file {bcolors.BLUE}            ] {bcolors.ENDC}\n {e}")
                    pass
            else:
                print(f"{bcolors.BLUE}      [       {bcolors.YELLOW}Configuring changemac@.service {bcolors.BLUE}            ] {bcolors.ENDC}")
                time.sleep(0.4)
                subprocess.Popen(["cp", "/etc/systemd/system/changemac@.service", "/etc/systemd/system/changemac@.service.bak_africana"], stdout=subprocess.PIPE).communicate()
                changemac = open('/etc/systemd/system/changemac@.service', 'w')
                for elements in changemacstring:
                    changemac.write("%s\n" % elements)
                changemac.close()
                print(f"{bcolors.BLUE}      [  {bcolors.CYAN}                                           {bcolors.GREEN}[ ✔ ]{bcolors.BLUE}]{bcolors.ENDC}")

        else:
            print(f"{bcolors.BLUE}      [    {bcolors.RED}No! macch try 'apt install macchanger'        {bcolors.BLUE}]{bcolors.ENDC}")
            print(f"{bcolors.BLUE}      [  {bcolors.CYAN}                                        {bcolors.GREEN} [ x ] {bcolors.BLUE} ]{bcolors.ENDC}")
            pass

        if os.system("which dnsmasq > /dev/null") == 0:
            if not os.path.exists('/etc/dnsmasq.conf'):
                print(f"{bcolors.BLUE}      [     {bcolors.RED}No dnsmasq.conf file is configured           {bcolors.BLUE}] {bcolors.ENDC}")
                print(f"{bcolors.BLUE}      [  {bcolors.CYAN}                                        {bcolors.GREEN} [ x ] {bcolors.BLUE} ]{bcolors.ENDC}")
                try:
                    infile = "/etc/dnsmasq.conf"
                    outfile = "/etc/dnsmasq.conf"
                    delete_list = ['#port=5353']
                    fin = open(infile)
                    os.remove("/etc/dnsmasq.conf")
                    fout = open(outfile, "w+")
                    for line in fin:
                        for word in delete_list:
                            line = line.replace(word, 'port=5353')
                        fout.write(line)
                    fin.close()
                    fout.close()
                    print(f"{bcolors.BLUE}      [                                          {bcolors.CYAN}{bcolors.GREEN} [ ✔ ] {bcolors.BLUE} ]{bcolors.ENDC}")
                except Exception as e:
                    print(f"{bcolors.BLUE}      [   {bcolors.RED}Failed to write the dnsmasq.conf file          {bcolors.BLUE}] {bcolors.ENDC}")
                    print(f"{bcolors.BLUE}      [  {bcolors.CYAN}                                        {bcolors.GREEN} [ x ] {bcolors.BLUE} ]{bcolors.ENDC}\n")
                    pass
            else:
                print(f"{bcolors.BLUE}      [          {bcolors.YELLOW} Configuring dnsmasq.conf{bcolors.BLUE}               ] {bcolors.ENDC}")
                time.sleep(0.4)
                try:
                    infile = "/etc/dnsmasq.conf"
                    outfile = "/etc/dnsmasq.conf"
                    delete_list = ['#port=5353']
                    fin = open(infile)
                    os.remove("/etc/dnsmasq.conf")
                    fout = open(outfile, "w+")
                    for line in fin:
                        for word in delete_list:
                            line = line.replace(word, 'port=5353')
                        fout.write(line)
                    fin.close()
                    fout.close()
                    print(f"{bcolors.BLUE}      [  {bcolors.CYAN}                                        {bcolors.GREEN} [ ✔ ] {bcolors.BLUE} ]{bcolors.ENDC}\n")
                except Exception as e:
                    print(f"\n{bcolors.BLUE}      [        {bcolors.RED} Failed to write the dnsmasq.conf file {bcolors.BLUE}      ] {bcolors.ENDC} \n {e}")
                    pass
        else:
            print(f"{bcolors.BLUE}      [        {bcolors.RED}Dnsmasq isn't installed, install it with 'sudo apt install dnsmasq{bcolors.BLUE}      ] {bcolors.ENDC} \n {e}")
            pass

config = configure()
if ' __name__' == '__main__':
        sys.exit(config())
