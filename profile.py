import geni.portal as portal
import geni.rspec.pg as pg

pc = portal.Context()
request = pc.makeRequestRSpec()

lan = request.LAN("lan")

for index in range(2):
    node = request.RawPC(f"node{index}")
    node.hardware_type = "d7525"
    node.disk_image = (
        "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU24-64-STD"
    )

    interface = node.addInterface(f"if{index}")
    interface.addAddress(
        pg.IPv4Address(
            f"10.10.1.{index + 1}",
            "255.255.255.0"
        )
    )
    lan.addInterface(interface)

    storage = node.Blockstore("docker-storage", "/mydata")
    storage.size = "100GB"
    storage.placement = "nonsysvol"

pc.printRequestRSpec(request)