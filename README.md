# Python-Final: Jewelry-Image-Caption-Generator
This project has taken shape as a Caption Generator for Jewelry - An AI Model that captions uploaded jewelry images to help users easily identify pieces, stones and materials.

## The Function:

A jewelry image is uploaded as input and the model analyzes it and describes what it sees, writing a description as an output. 
Say, a gold ring with emerald for example, or a vintage necklace with intricate details. 

## Why BLIP:

I chose BLIP because it's not just a classifier that will identify images as a "ring" or "necklace." It actually describes things. It considers the whole image and explains what it sees in words.
This is a good tool to use for jewelry of significance for consumers or for research and analysis for professionals and designers. 
Somebody interested in Jewelry doesn't just want to be told the image infront of them is a ring -- this is something they can easily identitfy by themselves.
It is much more useful to know what differentiates the piece and makes it special, be that the details, the materials, or the design. BLIP makes this possible!
BLIP also loads fast. I originally wanted to use Stable Diffusion for image generation, which proved to be quite problematic in Colab.
It took many attempts, and the cells would either not finish loading or the URLS remain impossible to open on the broswer to test, which prompted me to experiment and helped me land on BLIP.

## The Data:

People upload their own jewelry images, bringing in their own their own data/datasets. 
BLIP was trained on millions of images so it generalizes to whatever people upload, whether old, new, or i.e. art deco, modern or entirely unique.
The limitations to the model are that it may at times, misss jewelry-specific details. 
It may not recognize exactly what gemstone something is, and the quality of analyses will remain dependent on the resolution and colors of the uploaded images.
However, it is a useful tool that is proficient at understanding an overall design and describing it.

## The Building:

I started trying to make an image generator app for jewelry designers.
I spent many hours trying to figure out how to make it work, before realizing that this project may have been too ambitious for my skillset as I struggled to navigate hiccups and complications,
and accepting it was way too slow and incompatible with Colab and my knowledge of it.
I then considered what I could build that was more approachable, while still being a valuable tool and aligned with my interest, 
I then felt inspired by the course content on building image identifying models that I particularily enjoyed, and landed on the jewelry caption generator tool.
When I started working on that and had the same struggled with Colab and Stable Diffusion, I began to research furhter and switched to BLIP, and then built it in Streamlit. 
My main personal lesson here was that the most ambitious project isn't always the right one. 
Practical, and functional is can be much stronger that aiming to impress with a foundation that is unstable. 

## The Challenges:

Besides the decision fatigue and analysis paralysis that came with choosing what to focus on with this final projects, 
getting Streamlit to load in Colab without timing out was one of the biggest hiccups, I attempted to integrate various models and different configurations, without much resolve. 
I eventually understood the problem wasn't my code, but that I was unknowingly trying to force a heavy Model into a light environment in Colab. 
I am glad to eventually have landed on a more appropriate model and having been able to learn and experiment with different ones while getting there.

## The Learnings:

Big models aren't always better -- Sometimes, smaller is smarter! That is one of the key lessons I am taking with me from this project. 
Seeking support and advice, building resilience and making projects work for yourself and your interests are other important takeways. 
Another key point as mentioned earlier is that a project that works is much better than something that looks cool but doesn't load. 
I learned that when something isn't working, and I keep hitting walls,
I need to begin becoming comfortable detaching from my preconcieved notions of success, and sometimes even changing my approach entirely, 
and grounding my ideas in the reality of circumstance and skill to create viable, feasible projects of actionable value and impact. 
