# The Two UX Gulfs: Evaluation and Execution - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">6</span>

<div class="article-header">

<h1 class="article-h1">The Two UX Gulfs: Evaluation and Execution</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Kathryn Whitenton</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/Kathryn_1.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list"><a class="ga-article-author" href="/articles/author/kathryn-whitenton/">

Kathryn Whitenton</a></span>

<p class="publication-date">

March 11, 2018

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2018-03-11</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: The Two UX Gulfs: Evaluation and Execution&amp;body=https://www.nngroup.com/articles/two-ux-gulfs-evaluation-execution/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/two-ux-gulfs-evaluation-execution/&amp;title=The Two UX Gulfs: Evaluation and Execution&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/two-ux-gulfs-evaluation-execution/&amp;text=The Two UX Gulfs: Evaluation and Execution&amp;via=nngroup" data-share-type="Twitter">

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

</span>With every interaction, users must overcome the twin challenges of understanding the current state of a system and figuring out how to change it. Designers can support them by being aware of these gulfs and bridging them with a transparent conceptual model.

</div>

<div class="article-body">

<p>Last week, I bought a great new Bluetooth headset — then, sadly, proceeded to spend over an hour on a frustrating quest to connect it to my computer. Despite the promises made by both the headset manual and the computer-support site, the headset did not automatically connect to the computer. After re-reading the instructions, checking to make sure both devices were on, scouring the headset reviews to confirm it was compatible with my computer, and even testing the headset by syncing it to a different computer, I was just about ready to give up and return the darn thing when I found a random help page (from a completely different hardware manufacturer), which changed everything.</p>

<p>This new help page showed an actual screenshot of what the Windows 10 Bluetooth settings switch looks like when it is turned on. Looking at this screenshot, I instantly realized my mistake: the Bluetooth settings screen I’d been staring at for the past hour was actually showing me that Bluetooth was off on my computer.</p>

<figure class="caption"><img alt="Screencapture of a Bluetooth switch in both the off and on positions" height="330" loading="lazy" src="https://media.nngroup.com/media/editor/2018/02/25/bluetooth-switch-both-off-and-on.png" width="720"/>

<figcaption><em>This Bluetooth-connectivity switch has a circle that can be shifted from side to side to change the state to </em>Off<em> (left) or </em>On<em> (right). The label reflects the current state of the control, not what will happen when the switch will be moved to the right. (Unlike the label for the plus icon, which explains what will happen when clicking it.)</em></figcaption>

</figure>

<p>I felt pretty dumb when I realized my mistake. But my failure to understand the current state of the device is actually an extremely common usability problem — so common that visibility of system status is the very first in Jakob Nielsen’s famous <a href="https://www.nngroup.com/articles/ten-usability-heuristics/">10 Usability Heuristics</a>.</p>

<p>Looking at this design, it’s clear that the creators knew it was important to make the <a href="https://www.nngroup.com/articles/indicators-validations-notifications/">status visible</a>: they even included an explicit status label, <em>Off</em>, next to the control switch.</p>

<p>So what went wrong? To understand, we need to dig deeper.</p>

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

<a class="ga-article-toc-item" href="#toc-the-gulf-of-evaluation-and-the-gulf-of-execution-1">The Gulf of Evaluation and the Gulf of Execution</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-execution-and-evaluation-are-interdependent-2">Execution and Evaluation Are Interdependent</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-bridging-the-gulfs-with-mental-models-3">Bridging the Gulfs with Mental Models</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-why-the-gulfs-are-important-4">Why the Gulfs Are Important</a>

</li>

</ul>

</div>

</div><h2 id="toc-the-gulf-of-evaluation-and-the-gulf-of-execution-1">The Gulf of Evaluation and the Gulf of Execution</h2>

<p>Two of the many challenges people must overcome to successfully interact with technology are:</p>

<ul>

<li>Evaluation: Understanding the state of the system</li>

<li>Execution: Taking action to accomplish a specific goal</li>

</ul>

<p>These challenges are described as the “gulf of evaluation” and the “gulf of execution” because, without effective design elements to support users, they can become insurmountable barriers between users and their goals.</p>

<p>The terms <em>gulf of evaluation</em> and <em>gulf of execution</em> were invented in 1986 by Ed Hutchins, Jim Hollan, and Don Norman, when they wrote about the virtues of <a href="https://www.nngroup.com/articles/direct-manipulation/">direct manipulation</a> in helping users bridge these gulfs. (Their work was published in the book “<a href="https://www.nngroup.com/books/user-centered-system-design/">User Centered System Design</a>,” edited by Norman and Draper, which was the first use of the term ‘user-centered design’, long before Don joined Jakob Nielsen to establish the Nielsen Norman Group). Don’s book, “The Design of Everyday Things,” tells the story of the gulfs and details their importance in the design process. Thirty years later, the two gulfs are still essential concepts in our field.</p>

<figure class="caption"><img alt="Diagram of the gulfs of evaluation and execution as they mediate between users and systems in the world" height="426" loading="lazy" src="https://media.nngroup.com/media/editor/2018/02/25/two-gulfs.png" width="720"/>

<figcaption><em>The gulf of evaluation and the gulf of execution describe two major challenges that users must overcome to successfully interact with any device. As indicated by the figure, users are stuck in an (almost) endless cycle, alternating these two issues: after you execute, you must evaluate the outcome, plan to execute your next step, evaluate that outcome, and so on, until you reach your desired end-goal and quit.</em></figcaption>

</figure>

<p>Furthermore, both of these challenges are composed of subtasks which users must accomplish. For example, successful evaluation requires not just <strong>perceiving</strong> the system-status indicator, but also <strong>interpreting</strong> what it means. Similarly, execution requires both <strong>planning</strong> an action based on an understanding how the controls work, and actually <strong>manipulating</strong> the controls. This type of granular, specific analysis of the interaction is important because success at one subtask doesn’t necessarily mean success at the others.</p>

<p>Determining whether something is on or off is a classic example of the <strong>gulf of evaluation</strong>; for this Bluetooth switch, it was easy to see both the switch and the label, but the visibility of these items did not necessarily mean they could be correctly interpreted.</p>

<h2 id="toc-execution-and-evaluation-are-interdependent-2">Execution and Evaluation Are Interdependent</h2>

<p>Successful execution usually depends on correct evaluation. In this Bluetooth example, as soon as I corrected my evaluation of the current state, I instantly knew how to enable Bluetooth by clicking the switch. It was easy to formulate an action plan to use the system, but any plan based on faulty evaluation is doomed to failure.</p>

<p>This interdependence affects many real-world interactions; for example, <a href="https://www.nngroup.com/articles/flat-design/">in many flat designs users have problems navigating</a>. It’s not because they don’t know how to click a link, but because they fail to understand that a link is presented to them.</p>

<h2 id="toc-bridging-the-gulfs-with-mental-models-3">Bridging the Gulfs with Mental Models</h2>

<p>Interpretation requires effort, and most people try to minimize this effort by relying on a mental model to understand a system. A <strong>mental model </strong>is a theory of how a system works, what its signals mean, and what the outcomes of different user actions will be. To save time, most people <a href="https://www.nngroup.com/articles/mental-models/">rely on their past experiences to quickly build mental models for new systems</a>.</p>

<p>Designers can leverage this natural tendency by deliberately including design elements that help users build effective mental models. This requires:</p>

<ol>

<li>Identifying a relevant design which users are already familiar with</li>

<li>Creating <strong>visual similarities</strong> between the new design and the familiar design</li>

<li>Creating <strong>functional similarities</strong> between the new design and the familiar design</li>

</ol>

<p>Both physical and digital experiences can work as the basis for the mental model for a system; the important thing is that the visual signals suggest a model which actually matches the system functionality, at least well enough to let the user correctly interpret the system’s state indicators and predict outcomes.</p>

<p>Coming back to the initial Bluetooth example, there are several different possible models for how an on/off switch can work. Some switches use no labels at all, and use positions or different background colors to distinguish different states. Others have labels outside the switch, and work by pushing the switch towards the label that describes the desired state. For example, the switch on the speaker shown below is currently <em>OFF</em>; to turn it on, you push the switch towards the word <em>ON</em>.</p>

<figure class="caption"><img alt="Examples of different on-off switches with different models " height="240" loading="lazy" src="https://media.nngroup.com/media/editor/2018/02/25/on-off-switch-mental-models.png" width="720"/>

<figcaption>Left:<em> Some switches do not include labels and use only color to distinguish between different states. </em>Right:<em> This speaker users a physical sliding on/off switch; to turn it on, you slide it towards the word ‘ON’, and to turn it off you slide it towards the word ‘OFF’. </em></figcaption>

</figure>

<p>The Bluetooth switch shown at the beginning of this article incorporates a label which visually resembles the labeled slider switch; but does not work the same way. On the Bluetooth switch, pushing the switch towards the label <em>Off</em> changes the switch status to <em>On</em>, which is the opposite of how the physical, labeled slider switch works.</p>

<p>This Windows 10 switch design is much easier to understand when you can see multiple switches in different states; the background color makes it obvious which switches are <em>Off</em> vs. <em>On</em>, and since both of these labels appear to the right of the switch, it’s clear that they describe the current selected state rather than just one end of the switch.</p>

<figure class="caption"><img alt="Example of multiple switches side by side" height="500" loading="lazy" src="https://media.nngroup.com/media/editor/2018/02/26/multiple-sliders-high-res.png" width="483"/>

<figcaption><em>When multiple switches are visible together and some are off, some are on, it’s easy to understand that the labels refer to the current selected state rather than to one specific position of the switch. (Additionally, in this screen, the fact that the Hide notifications switch is </em>Off<em> causes an additional interpretation difficulty due to the implicit double negation. Better to word all the features in a consistent — and positive — manner, so that </em>On<em> means that something is happening.)</em></figcaption>

</figure>

<p>But, across a complex menu of settings, it would be difficult to guarantee that an <em>Off</em>switch is always accompanied by another switch in the <em>On </em>position just to make sure people understand it. An alternative, better design would use a checkbox, which also relies on a mental model drawn from the physical world. Checkboxes originated on paper forms: a box with a mark would indicate that an option was selected, while no mark meant it was not. This was the model used for enabling Bluetooth in Windows 7; and, without the complications of label position and reliance on color, it posed a much lower evaluation burden on the user than its Windows 10 counterpart.</p>

<figure class="caption"><img alt="Example of checkbox settings in Windows 7 and Windows 10" height="423" loading="lazy" src="https://media.nngroup.com/media/editor/2018/02/25/checkbox-controls-in-windows-7-and-windows-10.png" width="720"/>

<figcaption>Left:<em> Windows 7 provided a checkbox to enable Bluetooth. The current status of a checkbox was easier to interpret, because it depended only on the presence of a mark in the box — not on the color, label, or label position. </em>Right:<em> Checkboxes still appear within the deeper settings in Windows 10; though updated to a more modern appearance, they retain the clear characteristics that make evaluating the current state easier.</em></figcaption>

</figure>

<h2 id="toc-why-the-gulfs-are-important-4">Why the Gulfs Are Important</h2>

<p>Don Norman first described his model of interaction decades ago, but difficulties with evaluation and execution still plague today’s interfaces. Understanding these gulfs and incorporating them into UX design is important for two reasons.</p>

<p>First, the challenges of evaluation and execution <strong>transcend interaction styles and device types</strong>. Regardless of whether you’re designing for a laptop, a watch, a smart speaker, or a refrigerator, people will still have to deal with these gulfs, and this framework is flexible enough to be applied effectively to novel design contexts.</p>

<p>Second, when it comes to solving design problems, the granularity of breaking down evaluation and execution into specific subtasks <strong>sheds light on the detailed reasons why designs fail</strong>, because it adopts a user-centered perspective. Heuristics like ‘make the system status visible’ tell you what a good design should do, but they don’t necessarily explain how to do it. Pinpointing whether a problem lies with visibility or interpretation gives you a better starting point for brainstorming solutions.</p>

<p>Users <em>must </em>bridge the gulfs of evaluation and execution to successfully interact with a design, but the challenge becomes much easier when the system’s creators are aware of these gulfs, and build in cues to send users down the right path.</p>

<p>Learn more in our full-day course, <a href="https://www.nngroup.com/courses/hci/">User Interface Principles Every Designer Must Know</a>. </p>

<p><strong>References</strong></p>

<p>Hutchins, E., J., Hollan, J., &amp; Norman, D. A. (1986). Direct Manipulation Interfaces. In A. N. Donald &amp; S. W. Draper (Eds.), <em>User Centered System Design; New Perspectives on Human-Computer Interaction</em> (pp. 339-352). Mahwah, NJ: Lawrence Erlbaum Associates.</p>

<p>Norman, D. (2013). <em>The Design of Everyday Things: Revised and Expanded Edition</em>. New York, NY: Basic Books.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="UX Basic Training" href="/courses/ux-basic-training/?lm=two-ux-gulfs-evaluation-execution&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">mental models,user-centered design,Human Computer Interaction,Interaction Design,interfaces,ui elements,signifiers</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Human Computer Interaction</span>

<a class="ga-article-related-topic" href="/topic/human-computer-interaction/">Human Computer Interaction</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/interaction-design/">Interaction Design</a>

</li>

</ul>

</div>

</div>

</div>

</div>