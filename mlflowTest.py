import inspect

import mlflow
import pprint
from mlflow import log_metric, log_param, log_artifacts

#find all variables
#print(globals())
#print(locals())

print("1", dir(mlflow))
print("2", dir(mlflow.tracking))
print("3", dir(mlflow.tracking.MlflowClient))
print("4", dir(mlflow.get_tracking_uri))
print("5", dir('ActiveRun'))

## Ansatz mit for-Schleifen Methoden abzubilden
import xml.etree.ElementTree as gfg

def GenerateXML(fileName):
    root = gfg.Element("Catalog")

    m1 = gfg.Element("mobile")
    root.append(m1)

    b1 = gfg.SubElement(m1, "brand")
    b1.text = "Redmi"
    b2 = gfg.SubElement(m1, "price")
    b2.text = "6999"

    m2 = gfg.Element("mobile")
    root.append(m2)

    c1 = gfg.SubElement(m2, "brand")
    c1.text = "Samsung"
    c2 = gfg.SubElement(m2, "price")
    c2.text = "9999"

    m3 = gfg.Element("mobile")
    root.append(m3)

    d1 = gfg.SubElement(m3, "brand")
    d1.text = "RealMe"
    d2 = gfg.SubElement(m3, "price")
    d2.text = "11999"

    tree = gfg.ElementTree(root)

    with open(fileName, "wb") as files:
        tree.write(files)



def GenerateXML1(fileName, framework):
    fwktree = [framework]
    root = gfg.Element(framework) #+ '___' + str(type(eval(framework)))[8:-2])

    levelone = dir(mlflow)
    levelone = [x for x in levelone if not x.startswith('_')]
    levelone = [x for x in levelone if x not in fwktree]   # to avoid duplicants and endless loops
    fwktree.extend(levelone)

    for eleone in levelone:
        e1 = gfg.Element(eleone) # + '___' + str(type(eval(framework + '.' + eleone)))[8:-2])
        root.append(e1)

        leveltwo = dir(eval('mlflow.' + eleone))  #eval gibt direkt den Pfad an, ansonsten wäre es ein String
        leveltwo = [x for x in leveltwo if not x.startswith('_')]
        leveltwo = [x for x in leveltwo if x not in fwktree]
        fwktree.extend(leveltwo)

        for eletwo in leveltwo:
            e2 = gfg.SubElement(e1, eletwo) # + '___' + str(type(eval(framework + '.' + eleone + '.' + eletwo)))[8:-2])

            levelthree = dir(eval(('mlflow.' + eleone + '.' + eletwo)))
            levelthree = [x for x in levelthree if not x.startswith('_')]
            levelthree = [x for x in levelthree if x not in fwktree]
            fwktree.extend(levelthree)

            for elethree in levelthree:
                e3 = gfg.SubElement(e2, elethree) # + '___' + str(type(eval(framework + '.' + eleone + '.' + eletwo + '.' + elethree)))[8:-2])

                levelfour = dir(eval(('mlflow.' + eleone + '.' + eletwo + '.' + elethree)))
                levelfour = [x for x in levelfour if not x.startswith('_')]
                levelfour = [x for x in levelfour if x not in fwktree]
                fwktree.extend(levelfour)

                for elefour in levelfour:
                    e4 = gfg.SubElement(e3, elefour) #+ '___' + str(type(eval(framework + '.' + eleone + '.' + eletwo + '.' + elethree + '.' + elefour)))[8:-2])

                    levelfive = dir(eval(('mlflow.' + eleone + '.' + eletwo + '.' + elethree + '.' + elefour)))
                    levelfive = [x for x in levelfive if not x.startswith('_')]
                    levelfive = [x for x in levelfive if x not in fwktree]
                    fwktree.extend(levelfive)

                    for elefive in levelfive:
                        e5 = gfg.SubElement(e4, elefive)

    tree = gfg.ElementTree(root)

    with open(fileName, "wb") as files:
        tree.write(files)

GenerateXML1('mlflow.xml', 'mlflow')

import xml.dom.minidom

dom = xml.dom.minidom.parse('mlflow.xml') # or xml.dom.minidom.parseString(xml_string)
pretty_xml_as_string = dom.toprettyxml()
print(pretty_xml_as_string)

object_methods = [method_name for method_name in dir(mlflow.h2o)
                  if callable(getattr(mlflow.h2o, method_name))]

object_methods = [x for x in object_methods if not x.startswith('_')]

object_methods = [method_name for method_name in dir(mlflow)
                  if callable(getattr(mlflow, method_name))]

""""
mlflow1 = dir(mlflow)
mlflow1 = [x for x in mlflow1 if not x.startswith('_')]
mlflow1 = ['mlflow.' + mlflowx for mlflowx in mlflow1]
print("6", mlflow1)
"""


"""
mlflow2 = []
for mlflowx in mlflow1:
    mlflowdir = dir(eval(mlflowx))
    mlflowdir = [x for x in mlflowdir if not x.startswith('_')]
    mlflowdir = [mlflowx + '.' + mlflowy for mlflowy in mlflowdir]
    mlflow2.append(mlflowdir)
    mlflow2.append('----------------------------------------------')
    print(mlflowdir)
"""
#print(mlflow2)

#for mlflow2 in mlflow1:
    #print(mlflow2, dir(eval(mlflow2))) #eval gibt direkt den Pfad an, ansonsten wäre es ein String
    #print(mlflow2, dir(mlflow.active_run))



"""

import os.path, pkgutil
pkgpath = os.path.dirname(mlflow.__file__)
mlflow_modules = ([name for _, name, _ in pkgutil.iter_modules([pkgpath])])
print(mlflow_modules)

from pkgutil import iter_modules

def list_submodules(module):
    for submodule in iter_modules(module.__path__):
        print(submodule.name)

#list_submodules(mlflow)

print("\n\n")

import importlib
import pkgutil

import sys
"""

"""""
import modules


def find_abs_modules(module):
    path_list = []
    spec_list = []
    for importer, modname, ispkg in pkgutil.walk_packages(module.__path__):
        import_path = f"{module.__name__}.{modname}"
        if ispkg:
            spec = pkgutil._get_spec(importer, modname)
            importlib._bootstrap._load(spec)
            spec_list.append(spec)
        else:
            path_list.append(import_path)
    for spec in spec_list:
        del sys.modules[spec.name]
    return path_list


if __name__ == "__main__":
    print(sys.modules)
    print(find_abs_modules(modules))
    print(sys.modules)

"""""



