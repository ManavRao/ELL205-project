import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--mode', '-mode', help="Mode : encrypt or decrypt", type=str)
parser.add_argument('--method', '-method', help="encrypt image or audio", type=str)
parser.add_argument('--a', '-audio', help="audio file name", type=str)
parser.add_argument('--i', '-image', help="dataset folder path", type=str)

args = parser.parse_args()

try:
    if args.mode == "encrypt":
        try:
            if args.method == "audio":
                file = args.a
            elif args.method == "image":
                file = args.i
            else:
                print("enter method to be either image(for image to image encryption) or audio(for audio to image encryption)")
        except:
            print("error in getting method value")

    elif args.mode == "decrypt":
        try:
            if args.method == "audio":
                file = args.a
            elif args.method == "image":
                file = args.i
            else:
                print("enter method to be either image(for image to image encryption) or audio(for audio to image encryption)")
        except:
            print("error in getting method value")

    else:
        print("enter mode to be either encrypt or decrypt")

except:
    print("Usage python3 main.py -mode encrypt/decrypt -method image {-i imagename or -a audio_name}")
