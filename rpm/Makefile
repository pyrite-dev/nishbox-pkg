all:
	rpmdev-setuptree
	git clone https://github.com/pyrite-dev/nishbox.git --recursive nishbox-0.0.0
	tar --create --file nishbox-0.0.0.tar.gz nishbox-0.0.0
	mv nishbox-0.0.0.tar.gz ~/rpmbuild/SOURCES
	cp ./nishbox.spec ~/rpmbuild/SPECS
	rpmbuild -ba ~/rpmbuild/SPECS/nishbox.spec
