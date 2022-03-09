import sapien.core as sapien
from sapien.utils import Viewer
import numpy as np

engine = sapien.Engine()
renderer = sapien.VulkanRenderer()
engine.set_renderer(renderer)

scene = engine.create_scene()
scene.set_timestep(1/100.)



scene.add_ground(altitude=0)  # Add a ground
actor_builder = scene.create_actor_builder()
actor_builder.add_box_collision(half_size=[0.5, 0.5, 0.5])
actor_builder.add_box_visual(half_size=[0.5, 0.5, 0.5], color=[1., 0., 0.])
box = actor_builder.build(name='box')  # Add a box
box.set_pose(sapien.Pose(p=[0, 0, 0.5]))



# Add some lights so that you can observe the scene
rscene = scene.get_renderer_scene()
rscene.set_ambient_light([0.5, 0.5, 0.5])
rscene.add_directional_light([0, 1, -1], [0.5, 0.5, 0.5])

viewer = Viewer(renderer)  # Create a viewer (window)
viewer.set_scene(scene)  # Bind the viewer and the scene

# The coordinate frame in Sapien is: x(forward), y(left), z(upward)
# The principle axis of the camera is the x-axis
viewer.set_camera_xyz(x=-4, y=0, z=2)
# The rotation of the free camera is represented as [roll(x), pitch(-y), yaw(-z)]
# The camera now looks at the origin
viewer.set_camera_rpy(r=0, p=-np.arctan2(2, 4), y=0)
viewer.window.set_camera_parameters(near=0.05, far=100, fovy=1)




while not viewer.closed:  # Press key q to quit
    scene.step()  # Simulate the world
    scene.update_render()  # Update the world to the renderer
    viewer.render()