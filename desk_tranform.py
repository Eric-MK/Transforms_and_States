import cairo
import math
import os



def draw_desk(context, x, y, rotation, scale_x, scale_y):
    # Apply transforms
    context.translate(x, y)
    context.rotate(rotation)
    context.scale(scale_x, scale_y)

    # Draw a rectangle for the desk at the transformed location
    context.rectangle(0, 0, 100, 60)  # Adjust width and height as needed
    context.fill()

# Create a surface and context
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 400, 400)
context = cairo.Context(surface)

# Call the draw_desk function with different parameters
draw_desk(context, 100, 100, math.pi/4, 1, 1)  # Draw at (100, 100), rotated by 45 degrees
draw_desk(context, 200, 200, 0, 1.5, 0.5)       # Draw at (200, 200), scaled by 1.5 in x and 0.5 in y


# Save the result to a PNG file in the "output" folder
output_folder = "output_folder"

output_path = os.path.join(output_folder, "desk_transformed.png")
surface.write_to_png(output_path)

print(f"Saved the result to: {output_path}")
