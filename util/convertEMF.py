import matplotlib.pyplot as plt
import subprocess
import os

inkscapePath = r"E:\ProgramFiles\Inkscape\bin\inkscape.exe"
savePath = r"path\to\images\folder"


def exportEmf(savePath, plotName, fig=None, keepSVG=True):
    """Save a figure as an emf file

    Parameters
    ----------
    savePath : str, the path to the directory you want the image saved in
    plotName : str, the name of the image
    fig : matplotlib figure, (optional, default uses gca)
    keepSVG : bool, whether to keep the interim svg file
    """

    figFolder = savePath + r"\{}.{}"
    svgFile = figFolder.format(plotName, "svg")
    emfFile = figFolder.format(plotName, "emf")
    if fig:
        use = fig
    else:
        use = plt
    use.savefig(svgFile)
    subprocess.run([inkscapePath, svgFile, '--export-filename', emfFile])

    if not keepSVG:
        os.system('del "{}"'.format(svgFile))