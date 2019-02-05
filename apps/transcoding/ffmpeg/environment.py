from golem.docker.environment import DockerEnvironment
from golem.docker.image import DockerImage


class ffmpegEnvironment(DockerEnvironment):
    DOCKER_IMAGE = 'golemfactory/ffmpeg'
    DOCKER_TAG = '1.0'
    ENV_ID = 'FFMPEG'
    SHORT_DESCRIPTION = ''

    def __init__(self, binds=None):
        super().__init__(additional_images=[DockerImage(
            repository=self.DOCKER_IMAGE,
            tag=self.DOCKER_TAG
            )])
        self.binds = binds or []

    def get_container_config(self):
        d = super(ffmpegEnvironment, self).get_container_config()
        d['binds'] = self.binds
        return d