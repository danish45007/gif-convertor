import imageio
import os

clip = os.path.abspath('SampleVideo_1280x720_1mb.mp4')


def gitmaker(inputPath,targetFormat):

    outputPath = os.path.splitext(inputPath)[0]+targetFormat

    print(f'convertin{inputPath} \n to {outputPath}')

    reader = imageio.get_reader(inputPath)

    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(outputPath,fps=fps)

    for frames in reader:

        writer.append_data(frames)

        print(f'Frames{frames}')

    print("Done!!")

    writer.close()

gitmaker(clip,'.gif')
