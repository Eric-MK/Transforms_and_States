import cairo
import os


def draw_desk(context):
    # Draw a rectangle for the desk at (0, 0)
    context.rectangle(0, 0, 100, 60)  # Adjust width and height as needed
    context.fill()

# Create a surface and context
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 200, 200)
context = cairo.Context(surface)

# Call the draw_desk function
draw_desk(context)

# Save the result to a PNG file in the "output" folder
output_folder = "output_folder"

output_path = os.path.join(output_folder, "desk_default.png")
surface.write_to_png(output_path)

print(f"Saved the result to: {output_path}")