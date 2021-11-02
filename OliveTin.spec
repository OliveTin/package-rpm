Summary: A web interface for running Linux shell commands. 
Name: OliveTin
Group: Applications/System
URL: http://olivetin.app
License: AGPL-3.0
  
Requires: golang
  
%description
OliveTin is a web interface for running Linux shell commands. 
  
Use cases
- Give controlled access to run shell commands to less technical folks who cannot be trusted with SSH. I use this so my family can podman restart plex without asking me, and without giving them shell access!
- Great for home automation tablets stuck on walls around your house - I use this to turn Hue lights on and off for example.
- Sometimes SSH access isn’t possible to a server, or you are feeling too lazy to type a long command you run regularly! I use this to send Wake on Lan commands to servers around my house.

%setup -q -n OliveTin-%{version}
  
%build
mkdir %{buildroot}/etc/OliveTin/
cp config.yaml %{buildroot}/etc/OliveTin/
  
%files
%config(noreplace) /etc/OliveTin/config.yaml
  
%changelog
* Thu Mar 05 2015 James Read <contact@jwread.com> 1.0.0
	See changelog
