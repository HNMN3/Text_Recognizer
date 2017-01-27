#Keep Coding And change the world and do not forget anything... Not Again..
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
# Red Color 6
def color_diff(c1,c2):
    color1_rgb = sRGBColor(*c1);
    # Blue Color
    color2_rgb = sRGBColor(*c2);
    # Convert from RGB to Lab Color Space 12
    color1_lab = convert_color(color1_rgb, LabColor);
    # Convert from RGB to Lab Color Space
    color2_lab = convert_color(color2_rgb, LabColor)
    # Find the color difference
    delta_e = delta_e_cie2000(color1_lab, color2_lab);
    return delta_e
