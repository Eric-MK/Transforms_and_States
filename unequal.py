import cairo
import os

#set up surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 600)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8,0.8,0.8)
ctx.paint()

width = 100
height = 100

# Red rectangle
ctx.set_source_rgb(1,0,0)
ctx.rectangle(150,200, width, height)
ctx.fill()

# Blue Rectangle 
ctx.scale(2/3, 1/3)
ctx.set_source_rgb(0,0,1)
ctx.rectangle(300,150,width,height)
ctx.fill()

# Save the result to a PNG file in the "output" folder
output_folder = "output_folder"

output_path = os.path.join(output_folder, "unequalscaling.png")
surface.write_to_png(output_path)

print(f"Saved the result to: {output_path}")