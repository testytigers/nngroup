# Dark Mode: How Users Think About It and Issues to Avoid

**Author:** Tanner Kohler, Amy ZhangTanner KohlerandAmy ZhangAugust 27, 20232023-08-27

**Topics:** Visual Design, Mobile & Tablet, Accessibility

**Source:** https://www.nngroup.com/articles/dark-mode-users-issues/

---

August 27, 20232023-08-27

Share

Dark mode is more popular than ever. You might even think it’s essential — at least if you were to read many of the web-design articles devoted to the topic. However, it takes valuable time and resources to fully support dark mode and “wear it well” because most designs are built in light mode first. To understand how much dark mode impacts users, we recently conducted a survey and somemobile usability-testingsessions in dark mode on mobile.

In a recent survey of 115 mobile users asking what mode they generally have their mobile device in,roughly 1/3 said dark mode, 1/3 said light mode, and 1/3 said a combination of both.The argument that dark mode improves the user experience (and accessibility in some cases) always seems to circle back to the same few reasons, mentioned by users, designers, and developers alike:

Let’s take a closer look at the commonly cited reasons for supporting and using dark mode.

Reducing eye strain is the most common reason users with normal vision mention for using dark mode. As one research participant put it, “My eyes have always been very sensitive to bright lights. So ideally, I use dark mode on everything I can. [...] I don't think I can go back to normal. [I have] a lot less eye strain. I don't think I'm getting headaches as much […]”

While dark mode is not guaranteed to reduce headaches,this belief is widespread and motivates many users to permanently set their devices to dark mode.

Dark modedoesslightly reduce the amount of light being taken in by the retina andmightfeel easier on the eyes during a single session — particularly in dark environments. However,some researchhas failed to find a significant difference in reported measures of eye strain and headaches when participants complete tasks in both light mode and dark mode.

One study compared participants’ levels of eye fatigue while reading passages in both dark and light modes within an immersivevirtual reality(VR) headset. This setup allowed the researchers to control all lighting conditions and isolate the effects of the dark and light modes better than simply having participants look at screens in a brightly lit room. The researchers found that dark modewasbest at reducing eye fatigue when the entire virtual environment was dimly lit, yetdark mode's advantage over a dimly lit light mode was still very small. It seems that the brightness level of the screen and surrounding environment make as much of an impact on eye fatigue as the color of the design.

Another widespread notion is that enabling dark mode in the smartphone’s operating-system settings will automatically save battery across the board (similar toLow-power modeorBattery-saver mode).

When asked why they use dark mode, some survey respondents commented,“[dark mode] uses less battery than light mode”or“to save battery power.”Most users are likely to switch dark mode on in the operating-system settings, assuming they are enjoying the maximum battery-saving benefitsdark mode has to offer across the device (whether individual designs support dark mode or not), and do not think about it again. This is because most users do not fully understand how the process works.

The truth is that dark mode can save battery only on devices with OLED (Organic Light-Emitting Diode) displays. As of 2023, roughly half of smartphones being produced use an OLED display. For reference, the first iPhone to use an OLED display was the iPhone X, which was released in 2017. OLED displays control each pixel individually and send only as much power to each one as needed at any given time. This means that, when portions of a design use dark colors, those pixels can use less power than those displaying brighter colors. Pixels displaying pure black (#000000) can be turned off completely and save the most power.

A study at Purdue University found an average of 67% reduction in power consumption by using dark mode when the screen brightness was at 100%. However, at only 30% screen brightness, the average power savings from using dark mode dropped to only 14%. In other words,screenbrightness is as important as the display mode when it comes to battery consumption.

Designs using manyimages,videos,graphics, or other content that are the same in dark and light modes have the least capacity to save battery life.

Many people simply like the way dark mode looks. Some survey respondents made comments such as,"it’s more visually appealing to me,”“I like the look of the dark screen,”and“dark mode is way cooler.”

Some designs are even built in dark mode and do not allow users to transition to light mode. In most of these cases,building in dark mode first is an aesthetic choice; it does not improve usability.For example, Spotify opted for permanent dark mode after users seemed to prefer it over a light-mode aesthetic. Those overseeing this design choice at Spotifycompared the app’s experienceto a movie theater. They emphasized that the less important UI elements can fade into the dark background to prioritize the colorful imagery and album art — just as a dark theater does not detract from the movie on the screen. Similar logic seems to guide the designs of many video-streaming applications such as Netflix, Hulu, Disney+, Peacock, Kanopy, Max, and Amazon Prime Video — none of which can be switched into light mode.

Theaesthetic-usability effectpredicts that, when designs are seen as attractive, people will assume that they are easier to use. One participant commented,“I also like the aesthetic of the dark mode. It makes everything seem more modern and easier to use.”However, such comments are not reason enough to build all designs in dark mode first.Aesthetically pleasing visual design cannot make up for poor usability.Thefundamentalsof usability have very little to do with light mode and dark mode. If you are skeptical, try conducting a few usability testing sessions using the same tasks in light mode and dark mode on your own or a competitor’s application. It’s unlikely that the color scheme will be the source of the biggest usability problems.

Over time, various research studies have shown that dark mode can benefit individuals with cloudy-ocular-media conditions, such as cataracts. In such disorders, the various transparent media in the eye (e.g., lens) reflect light in a fuzzier manner and, when there is a lot of light, it is harder for the eye to focus.

The bottom line is:for people with visual impairments, it’s best not to enforce either display modeand, instead, respect their system-wide choice.

It’s debatable how much a design team who is trying to prioritize time and stretch a budget should worry about arguably reduced eye strain or minimal battery savings for users.

However, it isnotdebatable that many users like the dark mode aesthetic, which might be reason enough to support it. (Just not at the expense of fixing real usability issues!) Additionally, the benefits for those with visual impairments are also important and should be discussed as part of largeraccessibility considerationswithin the organization.Aesthetic appeal and improved accessibility are the strongest arguments for supporting dark mode.

Users think about dark mode at the operating-system level, not at the individual application level.Once they’ve set their device to dark mode in the system settings, they generally assume that all applications and websites will automatically display in dark mode — that is, they basically expect to see a lot more black than white. They do not expect to have to enable dark mode within individual applications.

In users’ minds, dark mode seems to be a bit like screen brightness: dimming the phone’s screen brightness affects all applications and websites in the same way. Many users don’t realize that the system does not automatically override application-level settings and force dark mode everywhere.

Dark-mode fans in our study barely seemed to notice when designs did not support dark mode.They did not generally comment about the fact that some designs were bright white while their phone was in dark mode and certainly didn’t show signs of abandoning these websites or applications. Also, interestingly, at the end of our study sessions, participants struggled to recall whether they had encountered any designs which did not support dark mode.

For example, one usability-testing participant spent a few minutes looking for Christmas stockings on Etsy in full dark mode (see image below). Once he found a stocking he liked, he visited a separate website — which did not support dark mode — to estimate the cost of having the stockings embroidered. When he opened the embroidery website, he did not comment about the fact that the website was not in dark mode, nor did he hesitate in any way before using it. Roughly 10 minutes later, when asked whether any of the websites or applications he had used during the session had not supported dark mode, he responded, “I don’t think any of them [didn’t], I think all of them were dark mode.”When we reminded him of the embroidery website, he commented,“I feel as though there are certain things that I would put more urgency of having dark mode on … I feel as though [this] random, offhanded website, I really don’t care about.”

Unfortunately, we weren't able to observe participants in their natural environments using designs for long periods, such as reading at night in a dark room. We also acknowledge that a user-testing environment sometimes leads people todeviate from their normal behaviors and priorities. However,we would be very surprised to see users avoid or abandon a design because it does not support dark mode.

It can be fairly simple to render a design in dark mode — for example, by using a plugin in your favorite design tool. However, while a tool might do most of the heavy lifting, it will never be as thorough as a real designer.You must check for common issues.The following examples highlight small ways in which dark mode can be problematic or simply tacky when done carelessly.

Graphics need to look equally good in dark mode and light mode. It’s problematic if portions of the graphic become invisible against a dark background, or if nontransparent backgrounds are revealed. It’s better to use an SVG, WEBP, or a PNG than a JPG to support transparency.

The most common method for creating the illusion that one UI element is layered over another is to use shadows that signal depth. This includes the darkened, translucent scrims (or “grayed-out” sections) used to signal the difference between amodaland a nonmodaloverlay.

A white page element on a white background can be okay in light mode because the use of darker shadows can create the necessary depth to understand the interface. However, placing a black element on a black background can be problematic because a lighter “shadow” does not create the same layered effect — it makes the top element look like it’s glowing.

The best way to create depth with layered dark elements is to use the darkest colors for the page elements on the bottom, and the lightest colors for the elements on top (or “closest” to the user). For example, placing a gray page element on a black background is visually interpreted the same way a drop shadow is with white on white.

Three main issues make it difficult to read in dark mode:

Thin fontscan be easily “swallowed up” by a dark background — particularly for individuals with poor eyesight. This is true even of pure white fonts on pure black backgrounds.

Thick(or bolded)fontscan seem to “bleed” into the background as the user tries to read. Generally, light fonts on dark backgrounds tend to appear bolder than dark fonts with the same font weight on light backgrounds.

Fonts without sufficient color contrastwith the background are obviously difficult to see and read in both dark and light modes.

To maintain the legibility of text in logos, consider adding strokes, glows, shadows, or gradients that will be visible in dark mode but invisible in light mode. This strategy can be especially helpful in email communications, because email clients may display your messages in both light and dark modes. Even though you may be able to request that the email client use two different logo versions for dark and light mode, there is no guarantee that all email clients will comply.

When choosing the color of fonts in dark mode,use one color with different levels of opacity.This allows you to accommodate different background colors throughout the interface. Using one color consistently at 100% opacity (such as a light gray) will look good on some backgrounds, and poor on others.

Highly saturated colors on dark backgrounds have poor visibility and do not comply with accessibility guidelines, such as the WCAG 2 requirement of a minimum contrast ratio of 4.5:1 for normal text and 3:1 for large text.

It is common for native mobile applications to provide links to web pages. These pages are sometimes displayed in in-app browsers or in the phone’s browser application. In many cases, the native application supports dark mode, yet the website is shown in light mode. It is ironic when product teams go to great lengths to support dark mode throughout the application, only to shove users “into the light.”

Dividers or visual section markers, such ascards, should be seen equally well in dark and light modes. Thin, gray dividers are easily swallowed up on very dark backgrounds. Missing dividers and invisible cards undermine the Gestalt principle ofcommon regions, making it more difficult to understand how a page is organized.

While outlining elements on the page to visually separate them is often sufficient in light mode, in dark mode, it can be helpful to use slight color differentiation to distinguish a card from the background.

When a page element is meant to stand out from the background and “float,” it should be equally distinctive in light mode and dark mode.

Not all scanning devices are as sophisticated as phone cameras, and many cannot process scannable codes (such as QR codes or barcodes) when they are inverted in dark mode. Many scanning devices expect a dark foreground on a light background. It's best topresent scannable codes in formats that will not render differently in light mode and dark mode(such as a PNG).

Dark mode is a nice-to-have, not necessarily a need-to-have in most cases. There will always be users who are grateful when dark mode is supported — particularly when they use a design frequently, for long periods, and in dark conditions. However,dark mode should not take priority over ensuring basic usability just because it is popular and preferred by many users and designers.

Investing in dark mode is most important in the following circumstances:

If you decide to support dark mode, here are a few recommendations:

Dash, P., & Hu, Y. C. (2021, June). How much battery does dark mode save? An accurate OLED display power profiler for modern smartphones. InProceedings of the 19th Annual International Conference on Mobile Systems, Applications, and Services(pp. 323-335).

Eisfeld, H., & Kristallovich, F. (2020). The rise of dark mode: A qualitative study of an emerging user interface design trend.

Erickson, A., Kim, K., Bruder, G., & Welch, G. F. (2020, March). Effects of dark mode graphics on visual acuity and fatigue with virtual reality head-mounted displays. In2020 IEEE Conference on virtual reality and 3D user interfaces (VR)(pp. 434-442). IEEE.

Essential UX design principles for small-screen websites and apps

Interaction

Create user interfaces using essential principles, techniques, and methods of visual design

Interaction

Create and evaluate applications for advanced decision making, complicated workflows, and complex domains

Interaction