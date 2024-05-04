PREFIX = /usr
MANDIR = $(PREFIX)/share/man

all:
	@echo Run \'make install\' to install xanfetch.

install:
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@mkdir -p $(DESTDIR)$(MANDIR)/man1
	@cp -p xanfetch $(DESTDIR)$(PREFIX)/bin/xanfetch
	@cp -p xanfetch.1 $(DESTDIR)$(MANDIR)/man1
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/xanfetch

uninstall:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/xanfetch
	@rm -rf $(DESTDIR)$(MANDIR)/man1/xanfetch.1*
