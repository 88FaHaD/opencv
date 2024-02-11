import roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="hSeeRZz6h7XtYkNNIvd8")
project = rf.workspace("clgprojects").project("clgproject")
dataset = project.version(1).download("yolov8")
