import unittest
import fcpxml_reader
import os


class clip_name_logic(unittest.TestCase):
    def test_clip_name_logic(self):
        self.data_fldr = os.getcwd() + r'\data'
        data = []

        for current_fps in ['25fps', '30fps']:
            for clip_type in ['cut', 'no cut']:
                if clip_type == 'cut':
                    pass
                    '''
                    filename = '3_clip_100_50_50.fcpxml'
                    clip_path = os.path.join(self.data_fldr, current_fps,
                                             clip_type, filename)
                    '''
                else:
                    for current_speed in ['25', '50', '100', '150', '200']:
                        filename = '1_clip_{0}.fcpxml'.format(current_speed)
                        clip_path = os.path.join(self.data_fldr,
                                                 current_fps,
                                                 clip_type, filename)

            base_filename = filename.rpartition('.')[0]
            data.append([clip_path, 'name-'+base_filename])

        for current in data:
            wrapper = fcpxml_reader.fcpxml_wrapper(current[0])
            self.assertEqual(wrapper.clips[0].name, current[1])


class seconds_to_frames_logic(unittest.TestCase):
    def test_seconds_to_frames_logic(self):
        # Seconds to frames at 30 fps
        frames = fcpxml_reader.get_frames_from_time(4, 30)
        self.assertEqual(frames, 120)

        # Seconds to frames at 25 fps
        frames = fcpxml_reader.get_frames_from_time(4, 25)
        self.assertEqual(frames, 100)


class clip_percentage_logic(unittest.TestCase):
    def test_clip_percentage_logic(self):
        self.data_fldr = os.getcwd() + r'\data'

        data = []

        for current_fps in ['25fps', '30fps']:
            for clip_type in ['cut', 'no cut']:
                if clip_type == 'cut':
                    pass
                    '''
                    filename = '3_clip_100_50_50.fcpxml'
                    clip_path = os.path.join(self.data_fldr, current_fps,
                                             clip_type, filename)
                    '''
                else:
                    for current_speed in [25, 50, 100, 150, 200]:
                        filename = '1_clip_{0}.fcpxml'.format(current_speed)
                        clip_path = os.path.join(self.data_fldr, current_fps,
                                                 clip_type, filename)

                        data.append([clip_path, current_speed])

        for current in data:
            wrapper = fcpxml_reader.fcpxml_wrapper(current[0])
            self.assertEqual(wrapper.clips[0].percentage, current[1])


class clip_number_logic(unittest.TestCase):
    def test_clip_number_logic(self):
        self.data_fldr = os.getcwd() + r'\data'

        data = []
        clip_count = None

        for current_fps in ['25fps', '30fps']:
            for clip_type in ['cut', 'no cut']:
                if clip_type == 'cut':
                    filename = '3_clip_100_50_50.fcpxml'
                    clip_path = os.path.join(self.data_fldr, current_fps,
                                             clip_type, filename)
                    clip_count = 3

                else:
                    for current_speed in ['25', '50', '100', '150', '200']:
                        filename = '1_clip_{0}.fcpxml'.format(current_speed)
                        clip_path = os.path.join(self.data_fldr, current_fps,
                                                 clip_type, filename)
                    clip_count = 1

                data.append([clip_path, clip_count])

        for current in data:
            wrapper = fcpxml_reader.fcpxml_wrapper(current[0])
            self.assertEqual(wrapper.clip_count, current[1])


class framerate_logic(unittest.TestCase):
    def test_framerate_logic(self):
        self.data_fldr = os.getcwd() + r'\data'

        data = [[self.data_fldr + r'\25fps\cut\3_clip_100_50_50.fcpxml', 25],
                [self.data_fldr + r'\25fps\no cut\1_clip_25.fcpxml', 25],
                [self.data_fldr + r'\25fps\no cut\1_clip_50.fcpxml', 25],
                [self.data_fldr + r'\25fps\no cut\1_clip_100.fcpxml', 25],
                [self.data_fldr + r'\25fps\no cut\1_clip_150.fcpxml', 25],
                [self.data_fldr + r'\25fps\no cut\1_clip_200.fcpxml', 25],

                [self.data_fldr + r'\30fps\cut\3_clip_100_50_50.fcpxml', 30],
                [self.data_fldr + r'\30fps\no cut\1_clip_25.fcpxml', 30],
                [self.data_fldr + r'\30fps\no cut\1_clip_50.fcpxml', 30],
                [self.data_fldr + r'\30fps\no cut\1_clip_100.fcpxml', 30],
                [self.data_fldr + r'\30fps\no cut\1_clip_150.fcpxml', 30],
                [self.data_fldr + r'\30fps\no cut\1_clip_200.fcpxml', 30]]

        for current in data:
            wrapper = fcpxml_reader.fcpxml_wrapper(current[0])
            self.assertEqual(wrapper.framerate, current[1])


if __name__ == '__main__':
    unittest.main()
