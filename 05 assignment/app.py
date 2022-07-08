from flask import Flask
import ghhops_server as hs

app = Flask(__name__)
hops = hs.Hops(app)

"""
    How to create inputs and outputs for hops.
    
    Hops Inputs should match the number of Hops inputs
    Hops Outputs should match the number of items that the functions returns 
"""


@hops.component(
    "/mycomponent",
    name = "MyComponent",
    inputs=[
        hs.HopsString("Name", "N", "Provide your name"),
        hs.HopsString("City", "C", "Provide your city"),
        hs.HopsString("Country", "Cy", "Provide your country")
    ],
    outputs=[
       hs.HopsString("Text","T","Print presentation")
    ]
)
def printPresentation(name, city, country):
    text= "My name is {} and I am  from {}, {}".format(name, city, country)
    return text



if __name__== "__main__":
    app.run(debug=True)