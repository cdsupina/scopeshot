import visa


def take_screenshot():

    resname = None
    rm = visa.ResourceManager("@py")
    for r in rm.list_resources():
        if r.startswith('USB0::2391::6056:'):
            resname = r
            break
        if r.startswith('USB0::10893::6008:'):
            resname = r
            break

    if resname is None:
        return None

    inst = rm.open_resource(resname)
    inst.read_termination = "\n"
    inst.write_termination = "\n"
    inst.timeout = None

    print(inst.query("*IDN?"))

    inst.write("*CLS")

    inst.write(":HARDcopy:INKSaver OFF")
    inst.query(":DISPlay:DATA? PNG, COLor")

    image_data = inst.read_raw()

    return image_data[10:]





