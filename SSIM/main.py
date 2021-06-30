# This is a sample Python script.

import tensorflow as tf
import glob
from os import remove


def process_dir(dir_to_process, acceptation_value_similitude):
    url = dir_to_process
    # we have the list of files ended in jpg
    list_files = sorted(glob.glob(url + "/*.jpg"))
    img_base = None
    deleted = 0
    iteration = 0

    for url_file in list_files:
        iteration = iteration + 1
        if img_base is None:
            image_contents = tf.io.read_file(url_file)
            img_base = tf.image.decode_jpeg(image_contents, channels=3)
        else:
            image_contents = tf.io.read_file(url_file)
            current_image = tf.image.decode_jpeg(image_contents, channels=3)
            ssim1 = tf.image.ssim(img_base, current_image, max_val=255, filter_size=11, filter_sigma=1.5, k1=0.01,
                                  k2=0.03)
            print(ssim1)
            if ssim1 > acceptation_value_similitude:
                remove(url_file)
                deleted = deleted + 1
            else:
                img_base = current_image
    print('the numbers of deleted images is %d', deleted)


if __name__ == '__main__':
    similitude_required = 0.55
    list_dirs = [

        '/home/adrian/Descargas/bags/RESULTS/ARSI_2017_10_16_CarrerFusina-result/yes',
        '/home/adrian/Descargas/bags/RESULTS/ARSI_2017_10_16_CarrerFusina-result/no',
        '/home/adrian/Descargas/bags/RESULTS/ARSI_2017_10_16_CarrerRibera-result/yes',
        '/home/adrian/Descargas/bags/RESULTS/ARSI_2017_10_16_CarrerRibera-result/no',
        '/home/adrian/Descargas/bags/RESULTS/ARSI_2017_10_16_PassatgeMercantil-result/yes',
        '/home/adrian/Descargas/bags/RESULTS/ARSI_2017_10_16_PassatgeMercantil-result/no',
        '/home/adrian/Descargas/bags/RESULTS/ARSI_2018_12_11_Avda.Pearson-result/yes',
        '/home/adrian/Descargas/bags/RESULTS/ARSI_2018_12_11_Avda.Pearson-result/no',

        '/home/adrian/Descargas/bags/RESULTS/siar_2017-09-21-12-17-39-result/yes',
        '/home/adrian/Descargas/bags/RESULTS/siar_2017-09-21-12-17-39-result/no',
        '/home/adrian/Descargas/bags/RESULTS/siar_2017-10-11-11-05-03-result/yes',
        '/home/adrian/Descargas/bags/RESULTS/ssiar_2017-10-11-11-05-03-result/no',
        '/home/adrian/Descargas/bags/RESULTS/siar_2017-10-17-10-12-16-result/yes',
        '/home/adrian/Descargas/bags/RESULTS/siar_2017-10-17-10-12-16-result/no',
        '/home/adrian/Descargas/bags/RESULTS/siar_2018-05-18-10-28-30-result/yes',
        '/home/adrian/Descargas/bags/RESULTS/siar_2018-05-18-10-28-30-result/no',
        '/home/adrian/Descargas/bags/RESULTS/siar_2018-06-12-10-23-30-result/yes',
        '/home/adrian/Descargas/bags/RESULTS/siar_2018-06-12-10-23-30-result/no',
        '/home/adrian/Descargas/bags/RESULTS/siar_2018-06-12-10-54-51-result/yes',
        '/home/adrian/Descargas/bags/RESULTS/siar_2018-06-12-10-54-51-result/no',
        '/home/adrian/Descargas/bags/RESULTS/siar_2018-06-27-10-31-55-result/yes',
        '/home/adrian/Descargas/bags/RESULTS/siar_2018-06-27-10-31-55-result/no',
        '/home/adrian/Descargas/bags/RESULTS/siar_2018-06-28-09-57-28-result/yes',
        '/home/adrian/Descargas/bags/RESULTS/siar_2018-06-28-09-57-28-result/no',
        '/home/adrian/Descargas/bags/RESULTS/siar_2018-07-04-09-38-22-result/yes',
        '/home/adrian/Descargas/bags/RESULTS/siar_2018-07-04-09-38-22-result/no',
        '/home/adrian/Descargas/bags/RESULTS/siar_2018-07-04-10-12-06-result/yes',
        '/home/adrian/Descargas/bags/RESULTS/siar_2018-07-04-10-12-06-result/no',
        '/home/adrian/Descargas/bags/RESULTS/siar_2018-07-04-10-39-41-result/yes',
        '/home/adrian/Descargas/bags/RESULTS/siar_2018-07-04-10-39-41-result/no',
        '/home/adrian/Descargas/bags/RESULTS/siar_2018-07-04-11-24-04-result/yes',
        '/home/adrian/Descargas/bags/RESULTS/siar_2018-07-04-11-24-04-result/no'
    ]
    for d in list_dirs:
        print(d)
        process_dir(d, similitude_required)