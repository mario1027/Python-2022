from apps.routes import blueprint
from flask import render_template, request,redirect

@blueprint.route("/")
def index():
    return render_template("index.html")



@blueprint.route("/<template>")
def route_template(template):
    if not template.endswith(".html"):
        template+".html"
    variable="Hola mundo"
    segment=get_segment(request)
    return render_template(template, variable1=variable)



def get_segment(request):
    try:
        segment=request.path.split("/")[-1]
        if segment=="":
            segment="index"
        return segment
    except:
        return None