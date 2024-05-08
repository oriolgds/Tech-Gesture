def hex_to_rgb(hex_color):
    """Convert hexadecimal color to RGB."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def hex_to_bgr(hex_color):
    """Convert hexadecimal color to BGR."""
    rgb = hex_to_rgb(hex_color)
    return (rgb[2], rgb[1], rgb[0])  # OpenCV uses BGR instead of RGB