Name:           xanfetch
Version:        1.0.0
Release:        1%{?dist}
Summary:        A command-line system information tool written in bash

License:        MIT
URL:            https://github.com/xanmoy/xanfetch.git
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:       bash >= 3.2

%description
xanfetch is a command-line system information tool that displays details about your OS, software, and hardware in a visually appealing way, supporting almost 150 operating systems.

%prep
%setup -q

%build
# No compilation needed for a bash script.

%install
rm -rf %{buildroot}
install -Dm755 xanfetch %{buildroot}/usr/bin/xanfetch

%files
%license LICENSE
/usr/bin/xanfetch

%changelog
* Thu Nov 07 2024 Tanmoy Ganguly - 1.0.0-1
- Initial package creation
