Summary: A web interface for running Linux shell commands. 
Name: OliveTin
Group: Applications/System
URL: http://olivetin.app
Source0: OliveTin-%{version}-linux-amd64.tar.gz
License: AGPL-3.0
Version: %{version}
Release: 1
  
Requires: golang
  
%description
OliveTin is a web interface for running Linux shell commands. 
  
Use cases
- Give controlled access to run shell commands to less technical folks who cannot be trusted with SSH. I use this so my family can podman restart plex without asking me, and without giving them shell access!
- Great for home automation tablets stuck on walls around your house - I use this to turn Hue lights on and off for example.
- Sometimes SSH access isn’t possible to a server, or you are feeling too lazy to type a long command you run regularly! I use this to send Wake on Lan commands to servers around my house.

%prep
%setup -q -n OliveTin-%{version}-linux-amd64
  
%build
mkdir -p %{buildroot}/etc/OliveTin/
cp config.yaml %{buildroot}/etc/OliveTin/

mkdir -p %{buildroot}/usr/local/sbin/
cp OliveTin %{buildroot}/usr/local/sbin/

mkdir -p %{buildroot}/etc/systemd/system/
cp OliveTin.service %{buildroot}/etc/systemd/system/

mkdir -p %{buildroot}/usr/share/OliveTin/webui/
cp -r webui/{js,index.html,style.css,*.png,*.js} %{buildroot}/usr/share/OliveTin/webui/
  
%files
/usr/local/sbin/OliveTin
/etc/systemd/system/OliveTin.service
/usr/share/OliveTin/webui/*
%config(noreplace) /etc/OliveTin/config.yaml
  
%changelog
* Thu Mar 05 2015 James Read <contact@jwread.com> 1.0.0
	See changelog
