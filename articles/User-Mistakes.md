# Preventing User Errors: Avoiding Conscious Mistakes - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">8</span>

<div class="article-header">

<h1 class="article-h1">Preventing User Errors: Avoiding Conscious Mistakes</h1>

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

September 7, 2015

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2015-09-07</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Preventing User Errors: Avoiding Conscious Mistakes&amp;body=https://www.nngroup.com/articles/user-mistakes/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/user-mistakes/&amp;title=Preventing User Errors: Avoiding Conscious Mistakes&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/user-mistakes/&amp;text=Preventing User Errors: Avoiding Conscious Mistakes&amp;via=nngroup" data-share-type="Twitter">

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

</span>Thoughtful design is transparent and easy to understand, provides a preview, and helps users to easily correct their errors.

</div>

<div class="article-body">

<p>To err is human, and errors happen when people engage with user interfaces. According to Don Norman, there are two categories of user errors: slips and mistakes. Slips occur when a user is on autopilot, and takes the wrong actions in service of a reasonable goal. We discuss slips and slip prevention in detail in the <a href="/articles/slips/">first article in this series</a>. In this article we focus on <strong>mistakes</strong>.</p>

<p><strong>Mistakes</strong> occur when a user has developed a <a href="/articles/mental-models/">mental model</a> of the interface that isn’t correct, and forms a goal that doesn’t suit the situation well. For example, many online children’s games start with a short video tutorial or with a video advertisement for another game; in our <a href="/articles/childrens-websites-usability-issues/">user testing with children</a>, we noticed that, when the video looks too much like a real game, kids are tempted to interact with it, thinking that they can already start playing. In this situation, the users form and execute an inappropriate goal, largely because they interpret incorrectly what they see on the website (namely, they think that the video is the real game). Good design should help prevent such mismatches between the user’s expectations and the interface.</p>

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

<a class="ga-article-toc-item" href="#toc-the-2-gulfs-1">The 2 Gulfs</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-gather-user-data-2">Gather User Data</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-follow-design-conventions-3">Follow Design Conventions</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-communicate-affordances-4">Communicate Affordances</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-preview-results-5">Preview Results</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-preventing-both-mistakes-and-slips-6">Preventing Both Mistakes and Slips</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-summary-7">Summary</a>

</li>

</ul>

</div>

</div><h2 id="toc-the-2-gulfs-1">The 2 Gulfs</h2>

<p>When working with a system like a website or app, users start with a goal of some kind and, based on their <a href="/articles/mental-models/">mental model of the system</a>, they form an action plan to accomplish that goal. Then they take action, and look to verify that their action produced the desired results. In his book <a href="/books/design-everyday-things-revised/"><em>The Design of Everyday Things</em></a><em>, </em>Don Norman refers to this process as bridging the <em>Gulf of Execution</em> (“How do I work with this tool to accomplish my goal?”) and the <em>Gulf of Evaluation</em> (“Did this work how I wanted it to?”).</p>

<p>A lot of user mistakes (but not slips) happen when users do not get enough help in bridging these two gulfs, and the designers’ mental model and interpretation of how the system should work does not match users’ mental models. In those situations, users either <a href="/articles/indicators-validations-notifications/">form an action plan that is incorrect or they do not understand well how the state of the system changed as a result of their actions</a>. While preventing slips is often a simple matter of validation and enforcing constraints, preventing mistakes involves understanding users’ mental models and their expectations and making your designers match them. Do not make the error of thinking that users are going to eventually learn your designers’ mental models; while that may be the case in rare situations where users are forced to use the system regularly, with most consumer-facing apps and websites users just navigate to a different site instead of bothering to learn a tricky one.</p>

<h2 id="toc-gather-user-data-2">Gather User Data</h2>

<p>Discovering the specific gaps between users’ mental models and designers’ mental models is critical for avoiding mistakes, and requires gathering user data. There is a <a href="http://www.nngroup.com/articles/which-ux-research-methods/">wealth of user research methods</a> that can suit a variety of circumstances, so it is important to select a methodology that provides you with the context for <em>why</em> users make mistakes and what their expectations are. Methods such as contextual inquiry, field studies, and ethnographic studies are well suited for figuring out users’ mental models and expectations at an early stage, when you’re starting a new design. Once you do have a system (or at least a <a href="http://www.nngroup.com/articles/paper-prototyping/">prototype</a>) you can use qualitative usability testing to detect gaps between designers’ mental models and users’ expectations.</p>

<h2 id="toc-follow-design-conventions-3">Follow Design Conventions</h2>

<p>Using <strong>standard design conventions</strong> helps users bridge both the Gulf of Evaluation and the Gulf of Execution, and understand what actions they can take. This is reinforced by <a href="https://www.nngroup.com/videos/jakobs-law-internet-ux/">Jakob’s Law</a><strong>, </strong>which states that “users spend most of their time on <em>other </em>websites.” Each and every user that interacts with your website or application has been trained by thousands of other designers to expect common interactive elements to look and work a certain way, and error-prone conditions can arise when your website deviates from those conventions.</p>

<figure class="caption"><img alt="Southwest Airlines mobile site calendar interface" border="0" height="569" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/08/02/southwestmobile.png" width="320"/>

<figcaption><em>Southwest’s mobile site uses the convention of greying out dates in the past, letting you know you can’t select them when booking a flight. Unfortunately, it also uses the same design for the next month’s dates, implying unavailability.</em></figcaption>

</figure>

<h2 id="toc-communicate-affordances-4">Communicate Affordances</h2>

<p>Besides using conventions that users are able to recognize from previous experiences, another method of making controls understandable (and thus helping users bridge the Gulf of Execution) is having the design communicate how it can be used. For example, users are accustomed to <a href="/articles/clickable-elements/">clickable buttons</a> looking like they have a subtle amount of shadow on the outside. This effect makes a button look like it is rising up out of the page, and you can push it. Conversely, form fields are also rectangular, but have a small amount of shadow on the inside of the shape, to indicate that they’re empty and can be filled.</p>

<p>This attribute of the design that indicated how it can be used is often referred to as the object’s <strong>signifier</strong>. The <strong>affordance</strong> itself is the <em>way</em> in which the object can be interacted with (buttons can be pushed, form fields can have typed input added), and the visual cues that communicate this to the user are known as the signifier of the affordance. If there isn’t a clear signifier that communicates the affordance, users may not understand how to use a control, and make mistakes.</p>

<figure class="caption"><img alt="Polarr iOS photo editor interface" border="0" height="405" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/08/02/polarr.png" width="720"/>

<figcaption><em>Polarr is a popular photo editor on iOS. The right-hand editing controls (</em>Temp<em>, </em>Tint<em>, etc.) require that you tap on the box, and then swipe left or right to change the numeric value of that parameter. However, the controls don’t indicate how users should interact with them, so novices are likely to accidentally set those controls to the wrong values several times before learning how to interact with them properly. An additional interaction difficulty is present: since the controls are on the far right side of the display, you can easily decrease the parameters by swiping left, but you quickly run out of horizontal space to swipe right and increase the value.</em></figcaption>

</figure>

<h2 id="toc-preview-results-5">Preview Results</h2>

<p>Sometimes, users don’t realize they’re about to trigger an action that results in changes that are wide in scope and difficult to verify. Users may well wish to revise their goals once they have had a chance to compare the effect of the action with their goal; <em>Preview</em> features provide an opportunity to bridge the Gulf of Evaluation without making a mistake.</p>

<p>A good example is rendering special effects in a video-editing software where the editing the system does in the background may take 5 or 10 minutes, and the computer will be mostly unresponsive while it’s working. In this case, even if users haven’t permanently lost any work, if the result isn’t what they’re looking for, they have lost quite a bit of time, and possibly also patience. Wherever possible, offer a preview state that users can examine to make sure that they will get what they want. This assists in avoiding time-consuming mistakes before they can be made.</p>

<figure class="caption"><img alt="iOS 8 Display Zoom accessibility option" border="0" height="569" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/08/02/displayzoom.png" width="320"/>

<figcaption><em>In iOS 8, there is an accessibility option that allows users with low vision to zoom the display so that icons and text are larger. Applying zoom requires restarting the phone, which is a <strong>heavyweight</strong> action that will take a while, so iOS shows a preview of what things will look like before you commit to applying this change. This helpful preview allows you to evaluate whether or not your goal really is to zoom the display.</em></figcaption>

</figure>

<h2 id="toc-preventing-both-mistakes-and-slips-6">Preventing Both Mistakes and Slips</h2>

<p>Some error-prevention strategies work with both slips and mistakes. The following are good general guidelines for reducing the likelihood (and the severity) of all types of errors.</p>

<h3>Remove Memory Burdens</h3>

<p>Whenever users need to keep a lot of information in their <a href="http://www.nngroup.com/articles/short-term-memory-and-web-usability/">short-term memory</a> while working on a task, they are vulnerable to slips where they can repeat steps, or fail to complete the task. Memory-lapses can also result in mistakes where users forget earlier decisions they’ve already made, and repeat the process with different outcomes. A good strategy for preventing both of these types of errors is to remove burdens on users’ memory.</p>

<p>Whenever possible, remove conditions that require users to keep information in their own memory while they move from one step to another in complex, multistep procedures. Instead, strive to display the contextual information that users need to complete a task. Remember, users are often distracted, multitasking, or otherwise not fully focused on the website or app that they’re using. A good approach is to imagine that your users could be interrupted by a phone call after every step in a multistep process. You want to show all of the information users need to readily resume their tasks after having been interrupted for several minutes.</p>

<figure class="caption"><img alt="Hipmunk.com's interface for choosing a flight midway through the process" border="0" height="317" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/08/02/hipmunk.png" width="720"/>

<figcaption><em>Hipmunk provides a quick glance at the contextual information needed to resume the process of choosing a flight, even after an interruption. At this second step in the booking process, it clearly shows the dates of travel, the airports in question, the fact that the lowest-priced fare for departure was chosen, and that the user is required to pick a return flight. Even users who had been distracted for quite some time could easily resume this process without accidentally deviating from their original requirements and plan for this flight, or attempting to repeat the steps already completed.</em></figcaption>

</figure>

<h3>Confirm Before Destructive Actions</h3>

<p>Designers typically focus on user tasks related to creation. But deleting also has to be straightforward. Remember, when users delete an item, they destroy something that had taken work to create. Before you finish removing the object of that hard work, make absolutely sure that the user really meant to <em>Delete </em>by showing users a <a href="https://www.nngroup.com/articles/confirmation-dialog/">confirmation dialog</a>.</p>

<p>This can be an effective, simple, and familiar way to give the user a final chance to stop, and double-check if they really want to delete all those vacation photos, for example.</p>

<figure class="caption"><img alt="OS X Yosemite Photos app confirmation dialog " border="0" height="563" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/08/02/photosdialog.png" width="720"/>

<figcaption><em>Apple’s new Photos app uses a conventional dialog box to make sure that the user really intended to delete these photos of a recent hiking trip, and indicates that the scope of the action is the highlighted 24 photos. Even better, the button to confirm the delete action is clearly labeled </em>Delete<em>, rather than the generic </em>Confirm<em>.</em></figcaption>

</figure>

<p>It’s important to use confirmation dialogs carefully, however, since they interrupt users’ workflow, and inherently slow them down. If a confirmation dialog asks “do you really want to do that?” after every decision, many users won’t spend the time to double-check whether they made an error before instinctively clicking the highlighted <em>Confirm</em> button. Counter-intuitively, a design intended to prevent errors can actually <em>increase</em> them, as the user starts rushing to counteract the inefficiency of constantly confirming. Like in Aesop’s famous fable, “The Boy Who Cried Wolf”, a UI can become “The Computer That Cried Confirm” a few times too many. In both cases, people will have stopped paying attention to the false alarms by the time there’s something important to cry about. Don’t use confirmation dialogs as the sole error prevention method, apply them carefully with the other techniques discussed in this article to maximize their usefulness and limit their inefficiency.</p>

<h3>Support Undo</h3>

<p>Another primary principle of preventing users from making errors is to acknowledge that they <em>will</em> make mistakes and slips from time to time, and provide a safety net that makes these errors less costly. Nearly everyone has experienced the utterly horrifying moment of realizing that you just accidentally deleted an entire folder or directory of important documents, when you really only meant to delete only one file.</p>

<p>Providing the ability to undo the most recent action can help users to feel more secure and more confident to experiment with unfamiliar features, since they are aware that a mistake is low cost and can be easily fixed.</p>

<figure class="caption"><img alt="Gmail Undo feature " border="0" height="192" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/08/02/gmailundo.png" width="720"/>

<figcaption><em>Gmail offers a nice, contextual </em>Undo<em> feature for destructive actions, like accidentally deleting 92 emails. This feature proved so useful that Gmail has now also made it available when sending emails, allowing one to </em>Undo<em> an email from being delivered up to 30 seconds after hitting </em>Send<em>.</em></figcaption>

</figure>

<h3>Warn Before Errors Are Made</h3>

<p>Presenting subtle, contextual error warnings while a user is actively making an error can help them to quickly correct it. For example, when users are typing a review into an input box on an ecommerce store, don’t wait until after they have hit <em>Submit</em> to show an error message that the review is 35 characters too long, let them know while they’re typing those extra 35 characters (or better yet, warn them as they get <em>close</em> to the limit).</p>

<figure class="caption"><img alt="Twitter warning feature before reaching the character limit" border="0" height="268" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/08/02/twitterwarning.png" width="720"/>

<figcaption><em>Twitter famously has a strict character limit for </em>Tweets<em>, and warns users before they exceed that limit with a remaining character count.</em></figcaption>

</figure>

<figure class="caption"><img alt="Twitter's error message once the character limit has been reached" border="0" height="268" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/08/02/twitteroverage.png" width="720"/>

<figcaption><em>Once a </em>Tweet<em> is longer than the limit, it shows a negative counter, highlights the excess characters, and deactivates the </em>Tweet<em> button, which lets users know exactly what they need to do to fix their mistake.</em></figcaption>

</figure>

<h2 id="toc-summary-7">Summary</h2>

<p>Even though users will always make some mistakes when using software, it’s possible to reduce overall errors by designing with the user’s experience in mind. Prevent mistakes by helping the user to build a good mental model of your interface. Use design patterns that communicate how they work to users, encourage users to double-check their work (especially before deleting), and warn before mistakes are made. These simple guidelines can help enable lower rates of user errors, and ultimately improve usability.</p>

<h3>Reference</h3>

<p>Don Norman. <a href="/books/design-everyday-things-revised/"><em>The Design of Everyday Things</em></a>, Basic Books 2013.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="UX Basic Training" href="/courses/ux-basic-training/?lm=user-mistakes&amp;pt=article">

<h4 class="title heading-small">UX Basic Training</h4>

<p id="ux-basic-training" class="description body-small">

Foundational concepts that everyone should know

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">errors,Heuristic Evaluation,Interaction Design</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Heuristic Evaluation</span>

<a class="ga-article-related-topic" href="/topic/heuristic-evaluation/">Heuristic Evaluation</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/interaction-design/">Interaction Design</a>

</li>

</ul>

</div>

</div>

</div>

</div>