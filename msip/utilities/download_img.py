import os.path
from PIL import Image
from urllib.request import urlopen

def run():
    if os.path.isdir('./data/'):
        fnames = [ 'lena', 'baboon', 'goldhill', 'barbara' ]
        for idx in range(len(fnames)):
            fname = fnames[idx] + '.png'
            if not os.path.isfile('./data/{0}'.format(fname)):
                url = 'http://homepages.cae.wisc.edu/~ece533/images/{0}'.format(fname)
                img = Image.open(urlopen(url))
                img.save('./data/{0}'.format(fname))
                print('Downloaded and saved {0} in ./data'.format(fname))
            else:
                print('{0} already exists in ./data'.format(fname))
    else:
        print('./data folder does not exist')


if __name__ == '__main__':
    run()
