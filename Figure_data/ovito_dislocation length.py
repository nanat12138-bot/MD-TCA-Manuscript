from ovito.io import import_file, export_file
from ovito.modifiers import DislocationAnalysisModifier
from ovito.vis import Viewport, DislocationVis,TachyonRenderer
import os

if os.path.exists(r'D:/output.txt'):##
    os.remove(r'D:/output.txt')##
    print('delet over')
else:
    print('not exist!')
'''
other=[]perfect=[]#1/2<110>shockley=[]#1/6<112>stair_rod=[]#1/6<110>
hirth=[]#1/3<100>frank=[]#1/3<111>'''

pipeline = import_file(r"D:/input/*.dump")##
dxa = DislocationAnalysisModifier()
dxa.input_crystal_structure = DislocationAnalysisModifier.Lattice.FCC#
pipeline.modifiers.append(dxa)
data=pipeline.compute()

DXA_data=r'D:/output.txt'#
export_file(
    pipeline,
    DXA_data,
    'txt/attr',
    columns=[
        'Timestep',
        'DislocationAnalysis.cell_volume',
        'DislocationAnalysis.total_line_length',
        'DislocationAnalysis.length.other',
        'DislocationAnalysis.length.1/2<110>',
        'DislocationAnalysis.length.1/6<112>',
        'DislocationAnalysis.length.1/6<110>',
        'DislocationAnalysis.length.1/3<100>',
        'DislocationAnalysis.length.1/3<111>'
    ],
    multiple_frames=True
)

data.particles.vis.enabled=False
dxa.defect_vis.enabled=False
pipeline.add_to_scene()
vp = Viewport()
vp.type = Viewport.Type.Front#Perspective,#vp.camera_dir = (1, 2, -1)
vp.zoom_all()

Frames=[0,5,10]##
for i,f in enumerate(Frames):
    vp.render_image(
        filename=f'D:/information_{f}.png',##
        size=(1024,768),
        frame=f,
        renderer=TachyonRenderer(ambient_occlusion=False,direct_light=True,shadows=False)
    )
print("done")

