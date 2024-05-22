docker build -f ./Dockerfile-arch -t python_arch .
docker build -f ./Dockerfile-debian -t python_debian .
docker build -f ./Dockerfile-ubuntu -t python_ubuntu .
docker build -f ./Dockerfile-fedora -t python_fedora .
# docker build -f ./Dockerfile-custom -t custom_python .
docker pull python:3.12