# ChatGPT examples
Some prompts and ChatGPT responses that I found interesting.

## Development
### Pong in Python
Prompt: `Write pong in Python`

Result: 2 player pong game written using turtle library 

Output: [pong.py](development/pong.py)

It had a small error but it might be due to the fact that I had to write continue multiple times and ChatGPT returned code formatted as code along with code formatted as regular text. Github Copilot fixed the error so in the end I got a working version while writing 0 lines of code.

![](media/pong.png)

### Video face replace 
Prompt: `Write program that finds faces in a video and replaces them and replaces them with a given picture`

Result: Python script that uses `cv2` and `dlib`.

Output: [face_image_replace.py](development/face_image_replace.py)

This worked out of the box but it produced output file that is many times larger than the input file. 
I don't use these libraries so I'm not sure if this is normal behavior.
![](media/face_image_replace.gif)

### Blur faces in video
`write python code that recognizes and blurs faces in a video file`

Result: This is very similar to the example above so the code is basically the same [blur_face_video.py](development/blur_face_video.py)

## Text (articles) manipulation
It's a text model so logically it does really good on this.

### Analyze text
Prompt: `Calculate price per minute of these 2 plans ...'

Output: [Midjourney plans pricing](text/text_analysis.png)

### Text editing

Prompt: `Write similar article but for iPhone` 

This produced [basically the same article](text/similar_for_iphone.png) but it realized that iPhone means switching from Google to Apple. It still kept some Google stuff.

So I adjusted the prompt to: `Write it for iPhone but introduce a different feature and don't mention google lens`

And now we get a [different article](text/iphone_different_feature.png) completely adjusted for iPhone.

### Summarizing text
Prompt: `Summarize this text...`

Output: [Summary of article](text/text_summary.png)

### Explaining scientific articles
This is for newer articles so it definitely didn't train on them.
 
Prompt: `...Explain in simpler terms`

Not sure about [this physics article](scientific_article1.png). It looks simplified but it also reads like a summary.


## Issues
It seems like it can easily get confused about facts and change its answer if questioned - [minecraft release year](issues/minecraft_year_release.jpg)

It often [fails simple math ](issues/chatgpt_math.png) but it [corrects itself](issues/chatgpt_math_correction.png) if I ask to do it step by step.
