VERSION=1.0
PRJDIR=/home/shnavid/projects/baubau
TAROUT=$(PRJDIR)/redhat/SOURCES/baubau-$(VERSION).tar.bz2

package:
	cd $(PRJDIR)
	ln -f -s $(PRJDIR) baubau-$(VERSION)
	tar cfj $(TAROUT) baubau-$(VERSION)/baubau baubau-$(VERSION)/baubau.1 baubau-$(VERSION)/etc-baubau/exclude_files \
	baubau-$(VERSION)/etc-baubau/include_files baubau-$(VERSION)/Makefile
	rm baubau-$(VERSION)

rpm:
	cd $(PRJDIR)
	mkdir -p ./redhat/BUILD ./redhat/SPECS ./redhat/RPMS ./redhat/SOURCES ./redhat/SRPMS
	ln -f -s $(PRJDIR)/baubau.spec ./redhat/SPECS/
	make package
	cd $(PRJDIR)/redhat/SPECS
	rpmbuild -ba --define "_topdir /$(PRJDIR)/redhat" baubau.spec

clean:
	rm -rf $(PRJDIR)/redhat
