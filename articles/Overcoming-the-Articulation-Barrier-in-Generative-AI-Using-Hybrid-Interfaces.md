# Overcoming the Articulation Barrier in Generative AI Using Hybrid Interfaces

**Author:** Tarun MugunthanTarun MugunthanAugust 13, 20232023-08-13

**Topics:** Artificial Intelligence, Interaction Design

**Source:** https://www.nngroup.com/articles/ai-articulation-barrier/

---

August 13, 20232023-08-13

Share

Most tools used for AI image generation haveprompt-based user input:Users write a text prompt, and the AI model responds by creating images that match the prompt.

An interface that accepts only text input can bechallenging for usersfor 2 reasons:

This article reports observations on the challenges that Midjourney users have with creating prompts and presents a design solution that addresses them.

The findings in this article are based on data from Midjourney, one of the most popular AI-based image-generation tools. Because Midjourney offers services through a Discord server, any member can see other users’ prompts and the images created by the AI in response to them. Thus, Midjourney represents a unique research opportunity.

To understand the challenges that users face in interacting with AI-based image generators, I analyzed over 100 prompts and the resultant images and traced the iterations users went through to generate their final images. This data captures real-world usage and has high ecological validity.

I also looked at eight prompt-writing guides for AI image-generation tools compiled by expert users. These helped me understand the gap between how beginners and experts approached writing prompts.

Articulating your needs in writing is challenging. Thisarticulation barrieris even higher for image generators than for text generators like ChatGPT. Image-generator prompts are far more complex and must capture not only a detailed description of the subject of the image, but also abstract concepts related to the desired visual aesthetics. Based on prompts written by users on Midjourney as well as prompt-writing guides,the key to generating good images is prompt specificity. Specificity applies to:

Prompt-writing guides encourage prompters to use many adjectives and rich scene descriptions to create adequate images. For example, the prompta pretty vaseis too broad;a photograph of an antique vase with floral patterns on top of a wooden tableis a lot more likely to produce the intended result.

Creating a prompt that is descriptive enough is cognitively taxing. Good prompts specifyall the image elements relevant to the final goal.Users may not even know or be able to recall the right words for many of these elements.This effort compounds quickly when the articulation process has to be repeated many times. Rarely did I observe a user in Midjourney stop after generating one image. Most users attempted to generate an image multiple times by iterating on the prompt. They changed, added or removed words, or rephrased the entire prompt. They repeated the process until they reached images they were happy with (or gave up).

Adding to this complexity is the fact thatusers may desire certain stylistic properties for their images.To that effect, style attributes are often chained at the end of a Midjourney prompt to produce a detailed or vividly colored result.  For example, the prompt “futuristic city” will generate a very different image than “futuristic city, cyberpunk”.

Among the data I analyzed,many prompts included style termslikesynth-wave,steampunk,octane render,dystopian,unreal engine,psychedelic,art nouveau, and so on. These terms arerooted in specific cultural and creative trendsknown only to a few. Thus, users who are unfamiliar with these trends lack the associated vocabulary and will have a hard time recreating that aesthetic.

Another common technique for specifying style attributes wasincluding the name of a visual artist(e.g.,Hokusai,Diego Rivera,Monet, andMiyazaki) in the prompt. This technique helps recreate specific visual properties much more quickly than trying to define the brushwork, style, or color palette of generated artwork.Swirling brushstrokes with bright, solid colors, and abstract, post-impressionist imageryis much harder for a user to articulate thanVan Gogh’s style(assuming the user knows who Van Gogh is). While this technique somewhat reduces the articulation barrier, it requires comprehensive knowledge of different artists and what their styles look like.

Users’ prompts often chained together several style terms and artist names to create images with the exact visual properties they were looking for (see the image and prompt below).

However, this technique demands a level of cultural exposure that not everyone possesses. Manyusers may be able to visualize images in their minds but lack the vocabulary to write the required prompt.

This articulation barrier is also encountered in search: there, too, users may not know the correct term describing something they’re looking for. However, in that situation, they can engage inkeyword foraging. With AI-prompt generation, foraging is not posssible (yet): there’s no way to find the right keywords just by using the image-generation tool.

The articulation barrier is a usability challenge for AI image-generation tools. Given that specific prompts with detailed descriptions and style specifications will likely result in superior outputs,how might wehelp users produce such prompts? In other words:

A solution to the articulation problem combines the best of two different interaction styles:text-based interactionandGUI-based interaction.

Text inputgives the userflexibilityto create the images that they envision. Retaining this flexibility is essential to preserving the value of generative AI. On the other hand, aGUIcould lessen the users’ memory load by favoringrecognition over recall. It could allow users to select options without having to recall fancy terminology.

Prompt Suggestions

A good interface must help users write descriptive prompts and use adjectives to specify visual details.

Writing and rewriting good descriptive prompts require users to come up with words that vividly describe the image. Writing assistants, common now in email composers, suggest words and phrases based on what a user has already typed. Suggestions like these could be very helpful at an early stage of prompt writing, when users are thinking about how to phrase their input.

I designed an AI tool that suggests details that can be added to a prompt to enrich it. This tool preserves the flexibility of writing but makes adding descriptors easier by surfacing alternative words, phrases, or sentence structures that could improve the prompt.

Midjourney users ofteninclude multiple synonymous descriptors in the promptto increase the chance they will get the desired result. This kind of redundancy is easily achieved with prompt suggestions.

Presenting Visual Properties as Options to Select from

Since cultural and aesthetic references used in prompts are outside many users’ knowledge, I also explored the idea of allowing users to select from different visual properties for their image, by showing thumbnail images with the visual effect that each term would have on the generated image. Users could choose and apply that effect without needing to know the name of the term and make their decision based on the visual clue provided in the thumbnail.

For instance, to create an aesthetic based on paint splashes and bright colors, users could pick the Jackson Pollock thumbnail, rather than needing to know about Jackson Pollock’s style and use it as a verbal reference.

This concept does not do away with prompts but instead helps users improve their prompts more easily. Users can write prompts to the best of their knowledge and add different visual properties to them by selecting from the given options. Over time, as users see and select more and more options, they will learn the names and aesthetics they were previously unaware of and expand their vocabulary. Thus, this tool improves the discoverability of visual properties by surfacing them as options.

Hybrid interfaces can address important usability issues in AI image-generation tools, but their utility does not stop there. Problems of discoverability and recall are shared by the many other generative-AI tools with prompt-based interfaces, including text generators like ChatGPT and code generators like Github Copilot. These powerful tools can do a lot for us, but not all users know the full extent of these possibilities.

Gaps in knowledge and awareness can be filled by surfacing possible commands and actions such that users may discover new ways of using the tool. By improving their vocabulary over time, they can gradually become more proficient. Forcing people to recall everything can also be avoided by showing them options to select from in the form of GUI elements that sit alongside text prompts as input. Further exploration and evaluation will show more conclusive results on the improved usability of hybrid interfaces, but they are a step in the right direction for many generative AI tools, given the issues present in their purely prompt-based counterparts.