from __future__ import division
from xml.etree.ElementTree import parse


def get_duration(duration_str):
    ''' Providing a time value, it returns the amount of seconds.

    If the argument was already in seconds "5s", a value of 5 will
    be returned

    If the argument is a division: "14260543/90000s", the result of
    the division will be returned.

    Note that the 's' character will be removed if it exists within
    the string.
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
        self.clip_count = None
        self.clips = []
        self.speeds = []

        self.read_file(filename)

    def read_file(self, filename):
        percentage = 100

        tree = parse(filename)
        root = tree.getroot()
        project = root.find('project')
        resources = project.find('resources')
        mformat = resources.find('format')
        sequence = project.find('sequence')
        spine = sequence.find('spine')
        clips = spine.findall('ref-clip') or spine.findall('clip') or spine.findall('video')

        # Get the framerate
        self.framerate = timevalue_to_seconds(mformat.get('frameDuration'))

        if clips:
            self.clip_count = len(clips)
            for current_clip in clips:
                clip_found = clip_wrapper()
                clip_found.name = current_clip.get('name')

                # Get clip percentages
                timeMaps = current_clip.findall('timeMap')
                if timeMaps:
                    for timeMap in timeMaps:
                        timepts = timeMap.findall('timept')
                        if timepts:
                            for timept in timepts:
                                time = get_duration(timept.get('time'))
                                if time != 0:
                                    chunk = (get_duration(timept.get('value')))
                                    percentage = (chunk*100)/time

                    clip_found.percentage = int(round(percentage))

                else:
                    clip_found.percentage = 100
                
                # Get clip start and end frame
                pass

                # Add current clip to the clip list
                self.clips.append(clip_found)


class clip_wrapper(object):
    def __init__(self):
        self.name = None
        self.percentage = None
        self.start_frame = None
        self.end_frame = None
