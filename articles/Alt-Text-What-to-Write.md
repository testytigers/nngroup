# Alt Text: What to Write

**Author:** Emma Cionca, Tanner KohlerEmma CioncaandTanner KohlerNovember 22, 20242024-11-22

**Topics:** Accessibility, Writing for the Web

**Source:** https://www.nngroup.com/articles/write-alt-text/

---

November 22, 20242024-11-22

Share

Alt text, or alternative text, is a brief description added to images on a website, enabling screen readers to convey visual content to individuals with visual impairments. Well-crafted alt text is essential for ensuring web accessibility and usability. The best alt text takes into consideration the context of the image along with its purpose.

If an image is essential for a task or for understanding page content, it needs alt text.The following recommendations apply to every instance of alt text — regardless of the type of image it describes.

Read the page copy surrounding the image to understand its purpose. Look for any references to the image or explanations of the image — especially if image captions are present. (Struggling to understand context is one reason AI does not write good alt text on its own.)

The context of an image and the author’s intention for including it determine what the alt text should say, which is why the best alt text is created with input from those who write the content and choose the images. Alt text for the same image changes from context to context because different things will be relevant about the same image in different places.

The following example shows how the alt text for the same image changes based on its context.

Write the basic idea(s) that the image conveys in the context of the surrounding page copy. Try answering the question “Why did the author include this image?”

Focus the alt text on the unique value that the image adds to the page. Reduce the alt text to state only that unique message toavoid redundancy with other page copy. (AI can be helpful for simplifying your writing at this stage.)

An image isdecorativeif users can complete all tasks and understand all information on the page without it.Decorative images create a specific look and feel for sighted users but don’t convey information relevant for any tasks. Because of this, they’re superfluous and don’t merit screen-reader users’ time or attention, so the alt-text attribute should be empty so that the screen reader skips right over them.

TheW3C statesthat:“whether to treat an image as informative or decorative is a judgment that authors make, based on the reason for including the image on the page.”

Decorative images often include:

Decorative images can also include page elements that use an image file, such as:

Functional images enable users to take actions within an interface. Alt text for functional images should not describe the image; instead, it shoulddescribe what will happenwhen the image is clicked or tapped.

However, if an image is accompanied by words or a label that enables the same action when clicked, the image is considered redundant and does not merit alt text.

Functional images include:

Informative images add task-related information beyond the contents of the surrounding page copy. If they visualize information that is already communicated elsewhere in writing, these images are considered redundant and will benefit froma deeper analysis into whether theyactuallyrequire alt text.

For example, a graph showing a full data set accompanying a written analysis of that data is informative. Informative images don't serve a functional purpose. Alt text for informative images should highlight the unique value they contribute to the page and avoid redundantly restating things already communicated elsewhere. Alt text for informative images tends to be the most difficult to write.

Informative images can be simple or complex, depending on how easy it is to textually describe the information conveyed by the image.

An informative image is consideredsimple when its main message can be summarized in one sentencethat fits within about 150 characters.

Simple informative images often include:

While some images, such as graphs and charts, seem complicated at first glance, their main point is often simple.

For example, a line graph might contain hundreds of data points, yet its main message might be the simple correlation between the two variables, which can be succinctly described in one sentence.

Simple informative images may include text.If the text is short enough to fit with about 150 characters and is an important part of the image's message, include the exact words in the alt text. Otherwise, including the exact text isn’t necessary.

An informative image iscomplexwhen:

This is often the case for intricate visuals that communicate more than one point.

Complex informative images often include:

Make complex informative images more accessibleby altering the page copy surrounding the image.Editing the page copy to communicate the image’s message often makes the visual itself redundant. In many cases, this could be as simple as including a list or table within the HTML of the page.

If the page’s body copy cannot be altered, consider adding a caption right above or below the image. Richer page copy can also benefit users with low vision, learning disabilities, or lack of subject-matter expertise, but must be balanced withbrevity.

For unalterable page content, provide expanded alt text in a long description.Long descriptions house more detailed information than is reasonable to stuff into traditional alt text. They can include longer paragraphs of text, lists, or tables.

A long description is text that is present in the HTML but invisible to people who do not use a screen reader. It can live on the same page as the image, ideally next to it, or on a separate page, linked to from an invisible link next to the image. If the description is located on a separate page, it can be made visible or invisible, depending on the HTML and the preferences of the designer.

Atlas V

Delta IV Heavy

Vulcan

Falcon 9

Falcon Heavy

Engine

1 x RD-180

3 x RS-68A

2 x BE-4

9 x Merlin 10

27 x Merlin 10

Cycle Type

OX Rich Closed Cycle

Open Cycle

OX Rich Closed Cycle

Open Cycle

Open Cycle

Propellant

KeroLOX

HydroLOX

MethaLOX

KeroLOX

KeroLOX

However, linking to long descriptions in other locations increases theinteraction costof accessing the alt text compared to presenting the analysis in the body text for all users.

At the time of writing, Artificial Intelligence (AI) tools still struggle to reliably write good alt text that communicates the intention behind images and accommodates their context.

Use AI to refine alt text rather than relying on AI to write itfrom scratch — particularly when usingLLM chatbots like ChatGPT. One critical step in writing useful alt text is toidentify the intentionbehind including the image.

AI cannot read the mind of the author; it can only describe what it “sees.” When given strict parameters and adequate context, it might generate something decent forredundantorsimple informativeimages. But it will struggle to produce accurate alt text forfunctionalimages because it may have difficulty interacting with interfaces and might not have a real understanding of what each interface element does.

When it comes to alt text forcomplex informativeimages, AI tends to write too much.

We hope that future accessibility software will leverage AI to efficiently aid in laborious accessibility work, but we are not there yet. Even AI-infusedaccessibility widgets are not yet up to the taskand can cause more harm than good.

Wrangling AI to write alt text is often more time-consuming than doing it yourself. However, if you are set on using an AI chatbot to help,the results should be reviewed by those who understand the intentions behind images. Your prompts should include the following parameters (which can also be used to evaluate the bot’s output):

We tested AI’s alt text writing ability by inputting a screenshot from an Everyday Astronaut webpage alongside a prompt.

We provided several popular LLM chatbots with the above information and the results were largely lackluster. Important details were often omitted for the sake of concision, and the chatbots misidentified key aspects of the image. While the AI-generated alt text was usable after some editing, it took more time and effort to hold its hand than to write it ourselves.

Always make sure the alt text in your HTML code functions properly by testing prior to publishing. There are many testing tools available online, like thisbrowser extensionfrom the Institute for Disability Research, Policy & Practice at Utah State University, which allows you to test for accessibility issues directly in your browser. Ideally,a person with low or no vision will test yoursiteprior to publishing, and report on the issues that they come up with.

As with anything, writing good alt text takes practice. Always evaluate your alt text before implementing it and remember that your main driver should be meeting the user’s goal. Don’t recreate visual experiences — help your users efficiently obtain necessary information.

There are many fantastic resources available to help create good alt text. Two of our favorites include:

W3C Web-Accessibility Initiative (WAI)

WebAIM: Web Accessibility In Mind

Use UX writing to shape your content to meet your readers' needs

Interaction

Foundational concepts that everyone should know

Interaction

Techniques and tools for implementing an actionable content strategy

Management