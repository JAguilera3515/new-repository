import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()
 
# Add a raw PC to the request.
node = request.RawPC("node")

# Install and execute a script that is contained in the repository.
ode.addService(pg.Execute(shell="/bin/sh", command="sudo apt install docker.io"))

node.addService(pg.Execute(shell="sh", command="sudo bash /local/repository/install_docker.sh"))

node.addService(pg.Execute(shell="/bin/sh", command="/local/repository/docker-compose.yml"))

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
