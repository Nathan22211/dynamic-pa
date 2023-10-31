import sys

gcode = ''
output = []
with open(sys.argv[1], 'r') as gcode:
    for line in gcode:
        if line == ";TYPE:External perimeter":
            output.append(line)
            output.append("_USE_PA F=ex_p")
        elif line == ";TYPE:Overhang perimeter":
            output.append(line)
            output.append("_USE_PA F=ov_p")
        elif line == ";TYPE:Internal perimeter":
            output.append(line)
            output.append("_USE_PA F=in_p")
        elif line == ";TYPE:Top solid infill":
            output.append(line)
            output.append("_USE_PA F=topsol_in")
        elif line == ";TYPE:Solid infill":
            output.append(line)
            output.append("_USE_PA F=sol_p")
        elif line == ";TYPE:Internal infill":
            output.append(line)
            output.append("_USE_PA F=in_p")
        elif line == ";TYPE:Bridge infill":
            output.append(line)
            output.append("_USE_PA F=bri_p")
        elif line == ";TYPE:Internal bridge infill":
            output.append(line)
            output.append("_USE_PA F=inbriin_p")
        elif line == ";TYPE:Thin wall":
            output.append(line)
            output.append("_USE_PA F=thinwall_p")
        elif line == ";TYPE:Gap fill":
            output.append(line)
            output.append("_USE_PA F=gfill_p")
        elif line == ";TYPE:Skirt":
            output.append(line)
            output.append("_USE_PA F=skirt_p")
        elif line == ";TYPE:Support material":
            output.append(line)
            output.append("_USE_PA F=sup_p")
        elif line == ";TYPE:Support material interface":
            output.append(line)
            output.append("_USE_PA F=supint_p")
        else:
            output.append(line)
    output.append("finished with dynamic PA")

curr_output_line = 0
with open(sys.argv[1], 'w') as f:
    for line in output:
        f.write(line)
        
