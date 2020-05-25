Good evening, 

I am using Essentia to analyze the sounds and I use the [Extractor](https://essentia.upf.edu/reference/std_Extractor.html) class to export the low level features.

Some of the parameters of this class are:

> - lowLevelFrameSize (*integer ∈ (0, ∞), default = 2048*) :
>
>   the frame size for computing low level features
>
> - lowLevelHopSize (*integer ∈ (0, ∞), default = 1024*) :
>
>   the hop size for computing low level features

```python
import essentia.standard as es
features = es.Extractor(lowLevel =True,
                        highLevel=False,
                        midLevel =False,
                        lowLevelFrameSize=1024,
                        lowLevelHopSize=128)(MonoAudio)
```

The image below was generated with the default FrameSize (=2048) and HopSize (=1024)

![FrameSize = 2048 / HopSize = 1024](https://scontent.fath5-1.fna.fbcdn.net/v/t1.15752-9/96745357_2846280758824054_4148341605050351616_n.png?_nc_cat=111&_nc_sid=b96e70&_nc_eui2=AeHBBkAFjlELDYneRxk-RrDBb5uTov7ovF9vm5Oi_ui8X6wnbksp7qY4E2mVWUy-A9Ou3elhltsPrly7zXkqYssh&_nc_ohc=mHqLlkrOo6gAX_uLu7Q&_nc_ht=scontent.fath5-1.fna&oh=90900e14235cfe59c7fd8fd18016b632&oe=5EDDDAF5)

While the next image was generated with FrameSize=1024 and HopSize=256

![FrameSize = 1024 / HopSize = 256](https://scontent.fath5-1.fna.fbcdn.net/v/t1.15752-9/96142851_889272028164144_4113485501606920192_n.png?_nc_cat=102&_nc_sid=b96e70&_nc_eui2=AeHJ7jCXeU5DAw_gwvKsu9LoIdjrg5BENQUh2OuDkEQ1Bd0IDE7TGS1PfHT8v2WLaUm71WNwweTpA4rrvoswr9hy&_nc_ohc=RHBhBwpM-68AX8o--42&_nc_ht=scontent.fath5-1.fna&oh=d18bfc4fcb0395f1df63c2b49229c576&oe=5EDE0557)

The similarities and the differences are obvious, but I don’t understand what the purpose of FrameSize and HopeSize and why it does affect the result. 

Also I can’t understand why the x-axis changes values. 

Can you explain to me the above?

Thanks in advance.