import unittest
import fcpxml_reader
import os

print __file__


class test_get_frames_from_seconds(unittest.TestCase):
    def test_4sec_to_frames_30fps(self):
        frames = fcpxml_reader.get_frames_from_time(4, 30)
        self.assertEqual(frames, 120)

    def test_4sec_to_frames_25fps(self):
        frames = fcpxml_reader.get_frames_from_time(4, 25)
        self.assertEqual(frames, 100)


class test_framerates(unittest.TestCase):
    def setUp(self):
        self.data_folder = os.getcwd() + r'\data'

    # Testing the files that are supposed to be 25 fps
    def test_25_cut_3_clip_100_50_50(self):
        fname = self.data_folder + r'\25fps\cut\3_clip_100_50_50.fcpxml'
        wrapper = fcpxml_reader.fcpxml_wrapper(fname)
        self.assertEqual(wrapper.framerate, 25)

    def test_25_nocut_1_clip_25(self):
        fname = self.data_folder + r'\25fps\no cut\1_clip_25.fcpxml'
        wrapper = fcpxml_reader.fcpxml_wrapper(fname)
        self.assertEqual(wrapper.framerate, 25)

    def test_25_nocut_1_clip_50(self):
        fname = self.data_folder + r'\25fps\no cut\1_clip_50.fcpxml'
        wrapper = fcpxml_reader.fcpxml_wrapper(fname)
        self.assertEqual(wrapper.framerate, 25)

    def test_25_nocut_1_clip_100(self):
        fname = self.data_folder + r'\25fps\no cut\1_clip_100.fcpxml'
        wrapper = fcpxml_reader.fcpxml_wrapper(fname)
        self.assertEqual(wrapper.framerate, 25)

    def test_25_nocut_1_clip_150(self):
        fname = self.data_folder + r'\25fps\no cut\1_clip_150.fcpxml'
        wrapper = fcpxml_reader.fcpxml_wrapper(fname)
        self.assertEqual(wrapper.framerate, 25)

    def test_25_nocut_1_clip_200(self):
        fname = self.data_folder + r'\25fps\no cut\1_clip_200.fcpxml'
        wrapper = fcpxml_reader.fcpxml_wrapper(fname)
        self.assertEqual(wrapper.framerate, 25)

    # Testing the files that are supposed to be 25 fps
    def test_30_cut_3_clip_100_50_50(self):
        fname = self.data_folder + r'\30fps\cut\3_clip_100_50_50.fcpxml'
        wrapper = fcpxml_reader.fcpxml_wrapper(fname)
        self.assertEqual(wrapper.framerate, 30)

    def test_30_cut_3_clip_100_200_200(self):
        fname = self.data_folder + r'\30fps\cut\3_clip_100_200_200.fcpxml'
        wrapper = fcpxml_reader.fcpxml_wrapper(fname)
        self.assertEqual(wrapper.framerate, 30)

    def test_30_nocut_1_clip_25(self):
        fname = self.data_folder + r'\30fps\no cut\1_clip_25.fcpxml'
        wrapper = fcpxml_reader.fcpxml_wrapper(fname)
        self.assertEqual(wrapper.framerate, 30)

    def test_30_nocut_1_clip_50(self):
        fname = self.data_folder + r'\30fps\no cut\1_clip_50.fcpxml'
        wrapper = fcpxml_reader.fcpxml_wrapper(fname)
        self.assertEqual(wrapper.framerate, 30)

    def test_30_nocut_1_clip_100(self):
        fname = self.data_folder + r'\30fps\no cut\1_clip_100.fcpxml'
        wrapper = fcpxml_reader.fcpxml_wrapper(fname)
        self.assertEqual(wrapper.framerate, 30)

    def test_30_nocut_1_clip_150(self):
        fname = self.data_folder + r'\30fps\no cut\1_clip_150.fcpxml'
        wrapper = fcpxml_reader.fcpxml_wrapper(fname)
        self.assertEqual(wrapper.framerate, 30)

    def test_30_nocut_1_clip_200(self):
        fname = self.data_folder + r'\30fps\no cut\1_clip_200.fcpxml'
        wrapper = fcpxml_reader.fcpxml_wrapper(fname)
        self.assertEqual(wrapper.framerate, 30)


if __name__ == '__main__':
    unittest.main()
