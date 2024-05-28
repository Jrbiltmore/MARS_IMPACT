# 3D_Modeling_Project/scripts/render_animation.py

import bpy
import logging
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
file_handler = logging.FileHandler('render_animation.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

def set_render_settings(output_path, fps=24, resolution=(1920, 1080)):
    """Set the render settings for the animation."""
    bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
    bpy.context.scene.render.ffmpeg.format = 'MPEG4'
    bpy.context.scene.render.ffmpeg.codec = 'H264'
    bpy.context.scene.render.ffmpeg.audio_codec = 'AAC'
    bpy.context.scene.render.filepath = output_path
    bpy.context.scene.render.fps = fps
    bpy.context.scene.render.resolution_x, bpy.context.scene.render.resolution_y = resolution
    logger.info(f"Render settings set: output_path={output_path}, fps={fps}, resolution={resolution}")

def render_animation():
    """Render the animation."""
    try:
        bpy.ops.render.render(animation=True)
        logger.info("Animation rendering completed successfully.")
    except Exception as e:
        logger.error(f"Animation rendering failed: {e}")
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Render the comet impact simulation animation.")
    parser.add_argument('--output', type=str, required=True, help="Path to save the rendered animation.")
    parser.add_argument('--fps', type=int, default=24, help="Frames per second for the animation.")
    parser.add_argument('--resolution', type=int, nargs=2, default=[1920, 1080], help="Resolution for the animation.")

    args = parser.parse_args()

    try:
        set_render_settings(args.output, args.fps, tuple(args.resolution))
        render_animation()
    except Exception as e:
        logger.error(f"Failed to render animation: {e}")
