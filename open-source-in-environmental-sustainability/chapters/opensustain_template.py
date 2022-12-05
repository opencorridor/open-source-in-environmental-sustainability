import plotly.io as pio
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image

logo_img = Image.open("logo.png")  # image path
# default plotting options
# Palette https://coolors.co/palette/0e7c7b-17bebb-ffc857-e9724c-c5283d
marker_color = "#0E7C7B"
color_continuous_scale = px.colors.sequential.Aggrnyl[::-1]
color_discrete_sequence = ["#0E7C7B", "#17BEBB", "#FFC857", "#E9724C", "#C5283D"]
boarder_color = "#000000"

# OpenSustain.Tech colours
# marker_color = "#159485"
# boarder_color = "#000000"
# color_continuous_scale = px.colors.make_colorscale(["#26E5A9","#3E59FB"])
# color_divergent_scale = px.colors.make_colorscale(["#26E5A9", "#E5ECF6","#3E59FB"])
# color_discrete_sequence = ["#3e59fb","#007dff","#0097ff","#00acff","#00bef9","#00cdde","#00dac1","#26e5a9"]

# Register your theme as a named template
pio.templates["OpenSustain"] = go.layout.Template(
    layout=dict(
        margin=dict(b=0),  # bottom margin
        font=dict(
            family="Open Sans",
            color="#040404",
            size=15,
        ),
        title_font_family="Open Sans",
        title_font_color="#040404",
    ),
)

# Combine your theme with plotly's default
pio.templates.default = "plotly+OpenSustain"
