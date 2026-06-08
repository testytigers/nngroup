# Scaling User Interfaces: An Information-Processing Approach  - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">9</span>

<div class="article-header">

<h1 class="article-h1">Scaling User Interfaces: An Information-Processing Approach to Multi-Device Design</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Raluca Budiu</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/2023-04-portraits-raluca.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list"><a class="ga-article-author" href="/articles/author/raluca-budiu/">

Raluca Budiu</a></span>

<p class="publication-date">

April 13, 2014

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2014-04-13</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Scaling User Interfaces: An Information-Processing Approach to Multi-Device Design&amp;body=https://www.nngroup.com/articles/scaling-user-interfaces/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/scaling-user-interfaces/&amp;title=Scaling User Interfaces: An Information-Processing Approach to Multi-Device Design&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/scaling-user-interfaces/&amp;text=Scaling User Interfaces: An Information-Processing Approach to Multi-Device Design&amp;via=nngroup" data-share-type="Twitter">

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

</span>Designing for all screen sizes must consider the capacity of the human–device communication channel, which depends on users’ memory, device portability, and screen size.

</div>

<div class="article-body">

<p>Back in the middle of the 20th century, when Claude Shannon introduced his <strong>information theory</strong>, not only did he revolutionize the science of signal processing, but he also deeply influenced a cohort of other disciplines, starting from computer science and artificial intelligence, and ending with cognitive psychology. One of the ideas coming from information theory was that communication systems are made of <strong>modules</strong> connected through limited-capacity communication <strong>channels</strong>.</p>

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

<a class="ga-article-toc-item" href="#toc-humandevice-communication-channel-1">Human–Device Communication Channel</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-users-working-memory-limits-the-capacity-of-the-communication-channel-2">Users’ Working Memory Limits the Capacity of the Communication Channel</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-screen-size-limits-the-capacity-of-the-communication-channel-3">Screen Size Limits the Capacity of the Communication Channel</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-attention-limits-the-capacity-of-the-communication-channel-4">Attention Limits the Capacity of the Communication Channel</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-mobile-design-and-the-limited-capacity-of-the-communication-channel-5">Mobile Design and the Limited Capacity of the Communication Channel</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-the-simplicity-continuum-6">The Simplicity Continuum</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-where-are-we-headed-7">Where Are We Headed?</a>

</li>

</ul>

</div>

</div><h2 id="toc-humandevice-communication-channel-1">Human–Device Communication Channel</h2>

<p>The basic concept in information theory is the<strong> communication system</strong>. A communication system comprises:</p>

<ol>

<li>Two <strong>modules</strong>: an information source and a destination.</li>

<li>A <strong>communication channel</strong> that transmits information from the source to the destination.</li>

</ol>

<p>The communication channel has a certain <strong>capacity </strong>that limits the amount of information that can be transmitted from source to destination. For instance, a network that connects 2 computers can be thought of as a communication system; the network bandwidth (which normally refers to the amount of data that can be transmitted between the 2 computers) is equivalent to the channel capacity. For example, if you have a 50 Mbps Internet connection, your computer can receive 50 million bits per second across the network (assuming everything is working at full speed) — that is the channel capacity.</p>

<p>While the clinical-sounding terminology describing these concepts may make them seem dated, nothing could be further from the truth. The idea of modules and channels is a powerful one and can and should be applied to the new art of mobile design.</p>

<p>When users interact with technology (a computer or a mobile device), they form a communication system with two modules (the user and the device) and a communication channel between them. The capacity of this channel is governed by the combined characteristics of the device and of the humans interacting with it. These characteristics include:</p>

<ul>

<li>The user’s working memory</li>

<li>The amount of attention that the user is able to devote to the communication</li>

<li>The size of the device screen</li>

</ul>

<p>We will discuss each of these characteristics separately and we will see how each of them influences mobile design.</p>

<p>But before doing so, we need to stress that, unlike for computers connected by a physical network, when we talk about communication capacity in this article, we're not talking about the number of bits per second a person receives, because we're not interested in raw data. Rather, we want to know how much <em>information</em> the person has internalized from dealing with the <em>data</em> on the screen.</p>

<h2 id="toc-users-working-memory-limits-the-capacity-of-the-communication-channel-2">Users’ Working Memory Limits the Capacity of the Communication Channel</h2>

<p>If a person is listening to someone giving a lecture, he has to rely mostly on his memory to remember what the speaker refers to and to connect new information to either his background knowledge or to other ideas that the speaker may have introduced before. The<strong> working memory</strong> of the listener is heavily taxed (at least if he is paying attention): he has to remember part of the information presented before to make sense of the new concepts introduced later on. The working memory is a highly individual variable; different people may have different working-memory sizes. How much we can keep around in our working memory dictates the quality of comprehension. Good speakers know their audience and pace their speech to cater to both small and large working-memory capacities.</p>

<p>When browsing the web, users keep information about their current goal in their working memory. For instance, they will carry information such as “I am trying to plan a vacation in France for my family during the month of July”. They also use their working memory to store contextual information about the site, about the current page, and about the site’s interface. (The concept of working memory is closely related to that of <a href="http://www.nngroup.com/articles/minimize-cognitive-load/">cognitive load</a>.) Thus, the capacity of the human–device communication channel is naturally limited by the user’s working memory. If the site or an application asks the user to learn too much new information (for instance, because the content presented is too complex or because the interaction is unique or unusual), often the user will reach an impasse where his working memory will not have that information anymore and he will need to go search for it. Sometimes the search may be very easy — for instance if what the user needs is right there, on the same page, in front of his eyes. In other situations, the user may need to navigate away from the current page (and thus incur a higher <a href="http://www.nngroup.com/articles/interaction-cost-definition/">interaction cost</a>) to find the content necessary to solve his impasse.</p>

<p>(For much more on the impact of human-memory characteristics and limitations on UX design, see our full-day course on <a href="http://www.nngroup.com/courses/human-mind/">The Human Mind and Usability</a>.)</p>

<h2 id="toc-screen-size-limits-the-capacity-of-the-communication-channel-3">Screen Size Limits the Capacity of the Communication Channel</h2>

<p>Each time a user does not understand content presented on a website, she can look around at the other information displayed in front of her. Obviously, the size of the screen limits how much information can be seen at once, before scrolling down or up or before navigating to a different page. Thus, in the human–device information system, the capacity of the communication channel is determined by the screen size. (As we will see later, the attention span and other individual variables may also influence the channel capacity.) The bigger the screen size, the larger the capacity of the communication channel between the human and the device. Once people have to take action and navigate to a different view (either by scrolling down the page or by switching pages altogether), users will incur (1) an interaction cost; and possibly (2) an extra memory load (either because they must remember what was on this page or because they must remember where else they may go to find the information that they need).</p>

<p>The smaller screen size is the main reason that <a href="http://www.nngroup.com/articles/mobile-content-is-twice-as-difficult/">mobile content is twice as difficult than desktop content</a>: because the mobile screen is so much smaller, users must rely on their working memory to keep around information that exists on the page but is not visible in front of their eyes.</p>

<h2 id="toc-attention-limits-the-capacity-of-the-communication-channel-4">Attention Limits the Capacity of the Communication Channel</h2>

<p>Beside screen size, the other variable that influences the capacity of the communication channel is the amount of attention that users can devote to a device. The more portable a device, the more likely people are to use it pretty much everywhere, and also the more likely they are to be interrupted while using that device. The attention capacity with a portable device is very different than with a desktop computer. In fact, a paper published in Mobile HCI back in 2011 showed that the <strong>average session duration on mobile was 72 seconds</strong>. While it may be a few seconds more or less now, a mobile site or app basically has slightly more than a minute to help users get to where they need. (In contrast, the average <strong>session size on the desktop is about twice as long</strong> — 2.5 minutes.)</p>

<h2 id="toc-mobile-design-and-the-limited-capacity-of-the-communication-channel-5">Mobile Design and the Limited Capacity of the Communication Channel</h2>

<p>Designing for different screen sizes needs to take into account the capacity of the communication channel. Designing for mobile is pretty much like passing a camel through the eye of a needle: it’s hard to do it through such a tiny channel. Different approaches to mobile design attempt to solve the problem in different ways, but they all need to be aware of the limited channel capacity.</p>

<p>Responsive design (in the most “purist” sense of the term, that insists that the identically same functionality and content will be available on all devices) solves the capacity problem by chopping up the site into cells on a fluid grid and rearranging those cells on the smaller screen in a way that takes into account the relative priorities of the cells. Basically, it delivers the same content piece by piece through a narrower communication channel. As a result, all the content is available on smaller screens. Remember, however, that the user inherently will have to work harder and keep more items in memory to get to a random piece of information on the site.</p>

<p>Some users may be willing to spend the time and effort, others will simply give up (or be forced to give up because of an interruption) if they don’t find what they need after a reasonable amount of time. Because responsive design <strong>linearizes the content </strong>(by reducing the dimensionality of the content grid, from n columns by m rows to n×m rows by 1 column, in the extreme case of designing for a smartphone), it requires users to go through the content sequentially before they reach any particular piece of information. Therefore, techniques that <strong>facilitate direct access</strong> are very important with responsive design: making sure that the navigation is easily accessible and contains pointers to all chunks of information that may be potentially relevant to a user.</p>

<figure class="caption"><img alt="" height="394" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2014/04/10/grid.png" width="250"/>

<figcaption><em>A responsive webpage laid out on a 2×3 grid on the desktop may be transformed into a 1×6 grid on a smartphone. If a mobile user is interested in the content in chunk number 4 she will need to sequentially scroll down through chunks 1–3 to get to see it. In contrast, on the desktop (or a larger screen) the content in chunk 4 will usually be immediately visible (with no need of scrolling).</em></figcaption>

</figure>

<p>(As an aside, the communication problem inherent in linearizing a web page is one of the main reasons for which <a href="http://www.nngroup.com/articles/beyond-accessibility-treating-users-with-disabilities-as-people/">users who are blind are slower than sighted users at using websites</a>: hearing the information read out loud in a linear fashion by the screen reader is inherently less efficient than visual scanning of that same information on a screen. For users who are blind, the auditory channel is all they have, and designers can employ tricks like <a href="http://www.nngroup.com/articles/keyboard-accessibility/"><em>Skip navigation</em> links</a> to expedite use despite the limitations of sound. For sighted users, it behooves us to expedite their use even more by exploiting the strengths of vision.)</p>

<p>Websites that are specifically designed for mobile start from a different assumption. They do take into account the limited channel capacity and make assumptions about what the users may be interested in. They deliver to the channel: they presume that, since content that’s buried too deeply into a site or app will be hard to find anyway and unlikely to be used, they’d better not pay the price of information overload or long load times; hence they leave out functionality and information that is deemed mobile unworthy.</p>

<p>Mobile sites bet on knowing what’s important to the mobile user and trim the content and functionality to fit the narrow mobile channel. The challenge is: how well can designers guess what the user needs will be on mobile? Is it better to have information out there, even if buried in a long page, under the assumption that those who need that information will be motivated enough to find it despite the higher interaction cost? This is a call that must be made from case to case.</p>

<p>How about apps? Apps usually give up on passing the camel through the eye of the needle; they assume that in the fast mobile world users will not be bothered with a camel anyhow. Mobile apps (at least those <a href="http://www.nngroup.com/articles/mobile-native-apps/">who don’t simply enclose a mobile site in a native app</a>) invent a new creature altogether, better suited to the demands of the device. They usually are built around a few tasks that they often support creatively and fully.</p>

<h2 id="toc-the-simplicity-continuum-6">The Simplicity Continuum</h2>

<p>When designing for mobile we often recommend simplicity. Simplicity means taking into account the capacity of the communication channel. A simple app or website is tailored to the channel capacity and does not make users work more than necessary to attain their goal. It takes into account:</p>

<ul>

<li>the user limitations (working-memory size and attention while using the device), and</li>

<li>the device limitations (the screen size)</li>

</ul>

<p>Designers sometimes misunderstand the concept of simplicity — they perceive it as static and independent on the device. We see tablet apps that are pretty much blown-up phone apps and we see systems such as <a href="http://www.nngroup.com/articles/windows-8-disappointing-usability/">Windows 8</a>;trying to fit one design on both tablets and desktop.What’s <strong>simple and appropriate</strong> on a phone can be <strong>simply dumb</strong> on a tablet or on a desktop.</p>

<figure class="caption"><img alt="" height="568" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2014/04/10/usatoday.PNG" width="700"/>

<figcaption><em>When Windows 8 first came out, the huge pictures with a little bit of text on the side in apps such as USA Today were ignoring the vast capacity of the desktop–human channel and were wasting it with too little information.(Newer versions of Windows 8 have been redesigned since to take better advantage of the large channel capacity.)</em></figcaption>

</figure>

<p>Not taking advantage of the channel size is bad because it makes users work unnecessarily (that is, interact more) to get to content that could have fit a single screen span. To continue our accessibility analogy, it's as if we forced everybody to have low vision and only see very little at a time.</p>

<p>Smartwatches are at the other end of the simplicity continuum. It would be simply ridiculous to show a desktop site on a 1.5 in ×1.5 in screen: nobody will be able to scroll through all the content available.</p>

<h2 id="toc-where-are-we-headed-7">Where Are We Headed?</h2>

<p>It’s clear that we’re moving towards an interconnected world populated by a plethora of devices — from smart thermostats, smartwatches and smart glasses, smart phones, phablets, tablets, laptops, desktops, smart TVs, and smart tabletops. We need a unified theory for designing for the continuum of screen sizes. This theory cannot reduce all these systems to a single denominator; designing for smartwatches is not the same as designing for tablets, and designing for mobile is not the same as designing for the desktop. Although many of the principles may be the same, they get applied differently on different devices. We need more nuance. The information-processing approach takes into account the capacity of the communication channel between the user and the device and can provide a start point for scaling user interfaces.</p>

<p>More about the differences and similarities in designing for different devices is discussed in our class on <a href="http://www.nngroup.com/courses/scaling-responsive-design/">Scaling User Interfaces</a>.</p>

<h3>Reference</h3>

<p>M. Bohmer, B. Hecht, J. Schoning, A. Kruger, G. Bauer. Falling asleep with Angry Birds, Facebook and Kindle — A large scale study on mobile application usage. <em>Mobile HCI 2011</em>.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="The Human Mind and Usability" href="/courses/human-mind/?lm=scaling-user-interfaces&amp;pt=article">

<h4 class="title heading-small">The Human Mind and Usability</h4>

<p id="the-human-mind-and-usability" class="description body-small">

Use psychology to predict and explain how your customers think and act

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

<li>

<a class="tile ga-article-related-course" data-course-title="Web Page UX Design" href="/courses/web-page-design/?lm=scaling-user-interfaces&amp;pt=article">

<h4 class="title heading-small">Web Page UX Design</h4>

<p id="web-page-ux-design" class="description body-small">

Strategically combine content, visuals, and interactive components to design successful web pages

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Human Computer Interaction,Mobile &amp; Tablet,Web Usability,information density</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Human Computer Interaction</span>

<a class="ga-article-related-topic" href="/topic/human-computer-interaction/">Human Computer Interaction</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/mobile-and-tablet-design/">Mobile &amp; Tablet</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/web-usability/">Web Usability</a>

</li>

</ul>

</div>

</div>

</div>

</div>