# Ch. 4 - Working with Docker Images

# Clone example Docker image
# --config option ensures line endings are not accidentally altered from the Linux standard
git clone https://github.com/spkane/docker-node-hello.git --config core.autocrlf=input

# Examine directory
cd docker-node-hello
tree -a -I .git

# Build the image
docker image build -t example/docker-node-hello:latest .

# Running the image
docker container run --rm -d -p 8080:8080 example/docker-node-hello:latest

# Verify container status
docker container ls
docker context list

# See the container in action
curl localhost:8080


# Build Arguments

# Check out the build's maintainer label:
docker image inspect example/docker-node-hello:latest | grep maintainer

# Change the maintainer label:
docker image build --build-arg email=me@example.com -t example/docker-node-hello:latest .

# Check again with previous command
docker image inspect example/docker-node-hello:latest | grep maintainer


