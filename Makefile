# This expects a few requirements
# one, that https://github.com/Jmainguy/docker_rpmbuild is cloned into ~/Github/docker_rpmbuild
# two, that docker is installed and running
# three, that ~/Github/docker_rpmbuild/dockerbuild/build.sh centos6 has been run
rpm:
	@tar -czvf ~/Github/docker_rpmbuild/rpmbuild/SOURCES/whatismyip.tar.gz ../whatismyip
	@cp whatismyip.spec ~/Github/docker_rpmbuild/rpmbuild/SPECS/whatismyip.spec
	@cd ~/Github/docker_rpmbuild/; ./run.sh centos6 whatismyip
	@ls -ltrh ~/Github/docker_rpmbuild/rpmbuild/RPMS/x86_64/whatismyip*
