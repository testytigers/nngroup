# Sliders, Knobs, and Matrices: Balancing Exploration and Precision - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">9</span>

<div class="article-header">

<h1 class="article-h1">Input Controls for Parameters: Balancing Exploration and Precision with Sliders, Knobs, and Matrices</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Page Laubheimer</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/2022-portrait-page-3.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list">

Page Laubheimer

</span>

<p class="publication-date">

May 14, 2017

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2017-05-14</span>

</p>

</div>

</div>

</div>

<div class="article-share">

<a class="article-share-title ga-share" href="#">

<span class="article-share-icon"></span>

<p class="article-share-label body-medium">Share</p>

</a>

<div class="share-links tooltip">

<div class="tip-arrow"></div>

<ul>

<li class="body-medium">

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Input Controls for Parameters: Balancing Exploration and Precision with Sliders, Knobs, and Matrices&amp;body=https://www.nngroup.com/articles/sliders-knobs/" data-share-type="Email">

<svg

width="24"

viewbox="0 0 24 24"

fill="none"

xmlns="http://www.w3.org/2000/svg"

class="icon"

>

<rect x="2.375" y="5" width="19.25" height="14" rx="0.65625" stroke="currentColor" stroke-width="1.3125"/>

<path d="M21.625 6.75L12.4156 14.285C12.1738 14.4828 11.8262 14.4828 11.5844 14.285L2.375 6.75" stroke="currentColor" stroke-width="1.3125"/>

</svg>Email article

</a>

</li>

<li class="body-medium">

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/sliders-knobs/&amp;title=Input Controls for Parameters: Balancing Exploration and Precision with Sliders, Knobs, and Matrices&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/sliders-knobs/&amp;text=Input Controls for Parameters: Balancing Exploration and Precision with Sliders, Knobs, and Matrices&amp;via=nngroup" data-share-type="Twitter">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-x" />

</svg>

Share on Twitter

</a>

</li>

</ul>

</div>

</div>

</div>

<div class="article-container">

<div class="article-content">

<div class="article-summary article-heading-small-light">

<span class="article-summary-label">

Summary:&nbsp;

</span>Linked controls support coarse and fine parameter selection and ensure both ease of exploration and precision.

</div>

<div class="article-body">

<p>Numeric parameters are attributes of an object whose values are numbers. Examples include product price and quantity on ecommerce sites or object transparency in photo-editing applications.</p>

<p>Common interactive controls for numeric parameters range from text input fields, sliders, virtual knobs that rotate, 2D matrices with editable curves, and steppers that increment or decrement a given value. Each type of control is useful in different circumstances and communicates information about the data being modified. Wherever possible, there should be a <a href="https://www.nngroup.com/books/design-everyday-things-revised/">natural mapping</a> between the type of control and the data. For example, a rotating virtual knob naturally corresponds to an angle parameter. When the UI control communicates some information about the parameter it modifies, the design adheres to one of the <a href="https://www.nngroup.com/articles/ten-usability-heuristics/">10 usability heuristics</a> — match between system and the real world.</p>

<p>Many<a href="https://www.nngroup.com/courses/application-ux/"> applications</a> and websites, particularly those used for creative pursuits or data analysis, have long lists of parameters that allow for detailed adjustment of specific attributes. With complex continuous parameters, a balance must be set between:</p>

<ul>

<li><strong>Exploration: </strong>allowing users to easily explore the effect of the control for the whole range of the parameter,<strong> </strong><em>and</em></li>

<li><strong>Precision</strong>: enabling the user to precisely choose a specific value.</li>

</ul>

<div class="table-of-contents">

<div class="content">

<div class="header">

<div class="toc-header">

<h2 class="toc-title article-heading-small">

In This Article:

</h2>

<span class="expand-icon"></span>

</div>

<a class="current-element" href="#"></a>

</div>

<ul class="toc-items">

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-discrete-vs-continuous-controls-1">Discrete vs. Continuous Controls</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-ui-controls-that-support-exploration-2">UI Controls that Support Exploration</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-link-controls-for-coarse-fine-parameter-adjustment-3">Link Controls for Coarse + Fine Parameter Adjustment</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-default-values-for-parameter-controls-4">Default Values for Parameter Controls</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-5">Conclusion</a>

</li>

</ul>

</div>

</div><h2 id="toc-discrete-vs-continuous-controls-1">Discrete vs. Continuous Controls</h2>

<p>There are two major types of input controls:</p>

<ul>

<li><strong>Discrete controls</strong> offer a limited number of steps or options available. Examples include on/off switches or <a href="https://www.nngroup.com/articles/checkboxes-vs-radio-buttons/">checkboxes and radio buttons</a> with a few, preselected options.</li>

<li><strong>Continuous controls</strong> allow for a range of inputs, typically between a minimum and maximum value. Sliders or knobs are continuous controls. (Note that, in theory, a continuous parameter can take any possible value within the range.)</li>

</ul>

<p style="margin-left:.25in;">(Strictly speaking, a slider that ranges from 0–100 in steps of whole integers is technically a discrete control, since the set of integers is not continuous. In practical terms, a slider that features a large range of values instead of just a few fixed options can be thought of as a continuous control because that’s how it feels in the user experience.)</p>

<figure class="caption"><img alt="Kindle for Mac sliders" height="313" loading="lazy" src="https://media.nngroup.com/media/editor/2017/05/08/kindle-for-mac.png" width="700"/>

<figcaption><em>Kindle for Mac features both discrete and continuous controls: 1) the </em>Font Size<em> slider is a discrete control because the only font-size choice is one of the 12 prespecified values corresponding to the barely visible hash marks below the slider. If the user attempts to move the slider in-between the discrete options available, the interface will snap it to the nearest available value. 2) The radio buttons for </em>Color Mode<em> are also discrete, because there are only 3 options to choose from. 3) </em>Words per Line<em> and </em>Brightness<em> sliders are continuous controls — users can select any value along the range.</em></figcaption>

</figure>

<h2 id="toc-ui-controls-that-support-exploration-2">UI Controls that Support Exploration</h2>

<p><strong>Linear sliders</strong></p>

<p>A<a href="https://www.nngroup.com/articles/gui-slider-controls/"> linear slider</a> is a useful default control when the corresponding parameter has a defined range (with clear maximum and minimum values), but the precise value is less likely to be important to users. Acquiring a precise value on a slider is difficult, due to the<a href="https://www.nngroup.com/articles/gui-slider-controls/"> Accot-Zhai Steering Law</a> (a corollary of the well-known <a href="http://www.asktog.com/columns/022DesignedToGiveFitts.html">Fitts’ Law</a>), which is an HCI principle that says that the time it takes a user to steer a pointing device through a 2D tunnel (such as a slider) depends on the length and the width of the tunnel. Most sliders have a narrow width, so users often have a hard time to hit a specific spot accurately.</p>

<p>Sliders are effective when users can scrub through the range of the control and see the effects in real time; they are not a good choice when there is significant response delay between the user action and its effect on the screen. (According to <a href="https://www.nngroup.com/articles/response-times-3-important-limits/">standard response-time guidelines</a>, this delay should be at most 0.1 seconds.) Examples where sliders are a poor choice include complex computations such as video effects that might not render in real time or filter controls (e.g., price ranges) for large datasets, if it will take time to load the results of the change.</p>

<figure class="caption"><img alt="iOS brightness slider" height="622" loading="lazy" src="https://media.nngroup.com/media/editor/2017/05/08/ios-brightness.png" width="350"/>

<figcaption><em>The iOS screen-brightness slider is not used to select a precise luminance value, but to acquire a relative, approximate brightness value: most often, users attempt to make the screen brighter (or dimmer) than it is currently. Critical to the usability of this control is that the system responds immediately with feedback, changing the screen brightness as the user moves the control; if there was a significant delay between the user’s action and its effect on screen brightness, the user would not be able to accurately select an appropriate value on the slider.</em></figcaption>

</figure>

<p>A variation of sliders features two controls that select a minimum and, respectively, maximum acceptable value. This variation is often used for implementing filters on websites, allowing users to set a minimum and maximum price, beginning and end times for flights, and so forth. As with other types of sliders, selecting a precise value is difficult, so this pattern is of limited utility in most situations. However, when combined with a graph such as a histogram (that shows how many options are available across the range of the slider), a dual-control slider can ensure that users select a range that has available matching content or options and thus prevent zero search results.</p>

<figure class="caption"><img alt="Kayak double slider" border="0" height="418" loading="lazy" src="https://media.nngroup.com/media/editor/2017/05/08/kayak-dual-slider.png" width="467"/>

<figcaption><em>Kayak.com features range sliders for selecting an acceptable take-off time interval for a flight. Although a precise departure value such as 12:15pm will be hard to select with this slider, the accompanying chart, graphing flight cost over departure time, enables users to optimize their choice over both time and price. The orange vertical line helps users map their choice onto the price chart.</em></figcaption>

</figure>

<p><strong>Virtual Knobs</strong></p>

<p>Virtual knobs or other controls which the user must 'rotate' can naturally represent parameters such as <em>panning – </em>where an audio engineer moves a sound to play from either the left or right speaker (or anywhere in-between) when mixing audio. However, virtual knobs are physically challenging to manipulate with common input devices such as mice and trackpads, which don’t have a natural <a href="https://www.nngroup.com/articles/user-mistakes/">affordance </a>for rotation. Because linear-input devices like mice have difficulty executing rotation, some designs add a <strong>hidden</strong> linear-dragging functionality to the knob, allowing users to click and drag up or down, vertically, in order to increase or decrease the parameter value. However, this behavior is not expected, and usually has no <a href="https://www.nngroup.com/articles/user-mistakes/">signifier</a>, so users may never discover it. (Plus, if implemented poorly, it can wrest control away from those attempting to move their mouse in a circle to mimic the rotation of the knob.)</p>

<div class="captioned">

<video controls="" poster="https://s3.amazonaws.com/media.nngroup.com/media/editor/2017/05/08/Garageband+poster+frame.png" src="https://s3.amazonaws.com/media.nngroup.com/media/editor/2017/05/08/Garageband.mp4" style="border:1px solid #000;" width="75%">Your browser does not support the video tag. Video of Garageband knob behavior during click and drag</video>

<div class="caption"><em>(Click to play video.) GarageBand has multiple knob controls that can be clicked and dragged vertically to control rotation. This design supports devices (such as mice) that don’t handle rotation well, but it’s not easily discoverable, and it can interfere with users’ attempt to move the mouse around the circular path of the knob in order to ‘rotate’ it. The choice of knobs in this case is an allusion to the physical controls used by audio engineers of the past, and represents a poor use of skeuomorphism — a horizontal slider would have been a more appropriate control for the </em>Compression <em>parameter, since its values do not map onto a circle.</em></div>

</div>

<figure class="caption"><img alt="Adobe lightroom sliders and knobs" border="0" height="275" loading="lazy" src="https://media.nngroup.com/media/editor/2017/05/08/lightroom-controls.png" width="491"/>

<figcaption><em>Adobe Lightroom uses multiple types of input controls for numeric parameters, including sliders and virtual knobs. Although they all represent continuous numeric data, each type of input control reflects some important, additional information about the data being modified: the </em>Angle<em> control uses a knob to naturally represent the angle of the shadow around an object, and the sliders (such as </em>Opacity<em>, which runs from 0%–100%) represent numeric data with a natural maximum and minimum.</em></figcaption>

</figure>

<p><strong>2D Matrices</strong></p>

<p>A 2D matrix is a specialized input control used to simultaneously modify multiple related parameters by drawing a complex curve. Interaction with this control typically occurs by clicking to add <strong>breakpoints</strong> to an existing line or curve; once a new breakpoint has been added, dragging that breakpoint to a new location tells the system to interpolate between the breakpoints and draw a curve. This type of control is useful when you have two related parameters that depend on each other or will typically be modified together (such as luminance or RGB curves in photo- and video-editing applications), or when you need to represent the location or pathway of an object through a 2D space (such as surround sound for films).</p>

<div class="captioned">

<video controls="" poster="https://s3.amazonaws.com/media.nngroup.com/media/editor/2017/05/08/GIMP+posterframe.png" src="https://s3.amazonaws.com/media.nngroup.com/media/editor/2017/05/08/GIMP-curves.mp4" style="border:1px solid #000;" width="50%">Your browser does not support the video tag. Video of GIMP 2d matrix controls</video>

<div class="caption"><em>(Click to play video.) GIMP (GNU Image Manipulation Program) uses a 2D matrix to control simultaneously several parameters that would otherwise require multiple sliders. In this case, each axis displays a different parameter: the x-axis is </em>Input Tones<em> (from </em>Shadows<em> to </em>Highlights<em>), and the y-axis is </em>Output Tones<em>. The more horizontal the curve is made, the more limited the overall tonal range of the image will be. Representing this data with sliders or other numeric controls would require using multiple pairs of controls (one for each particular </em>Tone<em> value that the user wants to manipulate). With a 2D grid, the user simply clicks to add a breakpoint anywhere on the line, and can drag that breakpoint to a new set of coordinates. This design allows users to create complex curves by making many small adjustments.</em></div>

</div>

<h2 id="toc-link-controls-for-coarse-fine-parameter-adjustment-3">Link Controls for Coarse + Fine Parameter Adjustment</h2>

<p>The simplest way to solve the problem of acquiring precise values is to use an input-text box where users can type an exact value for that parameter. However, while this solution offers precision, it does not allow users to efficiently explore the range of values offered by that parameter. If you know the value beforehand, typing it is easy, but if you have no idea what the number should be, typing random values to figure out a color that looks right is, at best, tedious, even with additional input stepper buttons that increment or decrement the value. Even more, a text box doesn’t reveal the range of possible values. (For example, for RGB color, a range of 0–255 for each of the red, green, and blue parameters is not at all intuitive to a new user.)</p>

<figure class="caption"><img alt="Input steppers" border="0" height="78" loading="lazy" src="https://media.nngroup.com/media/editor/2017/05/08/input-steppers.png" width="500"/>

<figcaption><em>Microsoft Office uses numeric input steppers in the form of arrow buttons next to the text field as a way to quickly increment or decrement parameter values.</em></figcaption>

</figure>

<p>A typical solution to this problem is the use of separate, linked controls for <em>coarse</em> and <em>fine</em> adjustment of the same parameter. <strong>Linked controls</strong> are two (or more controls) that adjust the same parameter. Typically, a continuous control such as a slider is used for <em>coarse</em> input — to easily explore effects for a range of values, and find a rough approximation of the desired value. Then, a text box is added to allow for <em>fine</em> control — selecting a specific value. The fine control also helps power users that already know the specific value they’d like to use. This design not only allows detailed adjustment of the parameter, but also shows the numeric value of the parameter in its current state, which can teach users the numeric values associated with desired outputs.</p>

<p>It is critical that these two controls are continuously linked, so that both display the same value and adjusting one immediately changes the other accordingly. (Here, again, “immediately” means ≤0.1 sec.)</p>

<h3>Keyboard Focus on Linked Controls</h3>

<p>To make use of linked controls even easier, move keyboard focus to the text box when a user adjusts the coarse slider, thereby allowing the user to both use the coarse control to set a rough value and then type in a more precise value easily, without having to click on the fine input field before typing. This design helps reduce the inefficiency associated with <em>homing</em> (i.e. moving one’s hand from mouse to keyboard and vice versa). However, ensure that keyboard shortcuts can still be used while focus is presented to the fine input control.</p>

<figure class="caption"><img alt="Photoshop input field focus" border="0" height="274" loading="lazy" src="https://media.nngroup.com/media/editor/2017/05/08/photoshop-input-field.png" width="400"/>

<figcaption><em>In a recent usability study, a user working with Adobe Photoshop on a PC ran into difficulties when using the </em>Transparency<em> slider in combination with the keyboard command to zoom in (ALT+Scroll wheel): since the keyboard focus moved to the fine-input control, an error beep was played each time he tried to use his keyboard shortcut (because the input field expected only numbers as a valid input). [As an aside, beeps violate all <a href="https://www.nngroup.com/articles/error-message-guidelines/">error-message guidelines</a>; we don’t recommend them.]</em></figcaption>

</figure>

<h2 id="toc-default-values-for-parameter-controls-4">Default Values for Parameter Controls</h2>

<p><a href="https://www.nngroup.com/articles/the-power-of-defaults/">Good parameter defaults</a> are important: not only can they save time and user effort, but they can provide guidance to novices. A typical approach to defaults is to use a neutral value, which will vary depending on the specific parameter: for a zoom slider, 100% (placed in the middle of the slider) makes a sensible default, for other controls, 0 or the maximum value might provide a neutral point. Provide an easy means to jump to the default value, such as a <em>Reset</em> button. This button is especially helpful if the neutral value is contained somewhere in the middle of the range (like in the zoom example before), or is not obvious (e.g., if the range is not from 0–100, or if the default value is not likely to be known by a novice user). It is also helpful to have some sort of visual indicator for default value, such as a small tick or hash mark above the slider, showing the location of the default value.</p>

<figure class="caption"><img alt="Apple Photos adjustment sliders" border="0" height="239" loading="lazy" src="https://media.nngroup.com/media/editor/2017/05/08/photos-app-adjustments.png" width="300"/>

<figcaption><em>Apple’s Photos app has multiple sliders to control parameters and an option that resets them to default values. (Unfortunately, the </em>Reset<em> function is hidden within a contextual menu.)</em></figcaption>

</figure>

<h2 id="toc-conclusion-5">Conclusion</h2>

<p>Detailed parameters need the right controls — that is, controls that convey some information not only about how they should be used, but also about the range of values appropriate for the parameter they represent. The control should provide easy means to explore the range of possible values and to specify a precise value. Provide users with separate but linked controls for coarse and fine values, use good defaults (and allow simple means to reset the value to those defaults), and provide keyboard focus to the fine control when the user manipulates the coarse control.</p>

<p>Learn more about UI controls in our <a href="https://www.nngroup.com/courses/application-ux/">day-long application-design course</a>.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Application Design for Web and Desktop" href="/courses/application-ux/?lm=sliders-knobs&amp;pt=article">

<h4 class="title heading-small">Application Design for Web and Desktop</h4>

<p id="application-design-for-web-and-desktop" class="description body-small">

Components, design patterns, workflows, and ways of interacting with complex data

</p>

<div class="ux-specialties">

<div class="ux-specialty-item">

<svg width="16" height="16" viewBox="0 0 21 21" aria-hidden="true">

<use href="#icon-interaction" />

</svg>

<p class="ux-specialty interaction-design">Interaction</p>

</div>

</div>

</a>

</li>

</ul>

</div>

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">controls,Application Design,Interaction Design,graphical user interfaces,interfaces,direct manipulation</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Application Design</span>

<a class="ga-article-related-topic" href="/topic/applications/">Application Design</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/interaction-design/">Interaction Design</a>

</li>

</ul>

</div>

</div>

</div>

</div>