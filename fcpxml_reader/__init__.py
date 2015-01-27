from xml.etree.ElementTree import parse


def get_frames_from_time(seconds, fps):
    ''' Returns the numer of frames in the amount of
    seconds specified using the framerate specified.

    '''
    return int(seconds * fps)


def timevalue_to_seconds(duration_str):
    ''' Providing a time division ex: "14260543/90000s" or a time expression
    ex: "5s", returns the amount of seconds as an integer.

    '''

    if duration_str.endswith('s'):
        duration_str = duration_str[:-1]

    values = duration_str.split('/')
    if len(values) > 1:
        val01, val02 = values
        val01 = int(val01)
        val02 = int(val02)
        val = None

        if val01 > val02:
            val = val01/val02
        else:
            val = val02/val01
        return val

    return float(values[0])


class fcpxml_wrapper(object):
    def __init__(self, filename=None):
        self.framerate = 0
        self.clip_name = None
        self.cuts = []
        self.speeds = []

        self.read_file(filename)

    def read_file(self, filename):
        tree = parse(filename)
        root = tree.getroot()
        project = root.find('project')
        resources = project.find('resources')
        mformat = resources.find('format')

        # Get the framerate
        self.framerate = timevalue_to_seconds(mformat.get('frameDuration'))
