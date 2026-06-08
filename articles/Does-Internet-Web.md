# Does Internet = Web ? - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">4</span>

<div class="article-header">

<h1 class="article-h1">Does Internet = Web ?</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Jakob Nielsen</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/Jakob-Nielsen-tie-800x800.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list"><a class="ga-article-author" href="/articles/author/jakob-nielsen/">

Jakob Nielsen</a></span>

<p class="publication-date">

September 19, 1998

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">1998-09-19</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Does Internet = Web ?&amp;body=https://www.nngroup.com/articles/does-internet-web/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/does-internet-web/&amp;title=Does Internet = Web ?&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/does-internet-web/&amp;text=Does Internet = Web ?&amp;via=nngroup" data-share-type="Twitter">

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

</span>Advanced functionality requires Internet-enabled client-server software with optimized user interfaces that cannot be delivered in a Web browser. Reserve the Web for hypertext and

content features.

</div>

<div class="article-body">

<p>

The Internet is much more than the Web, and usability will suffer if people try to make the Web do things it is not suited for and make it the only user interface to the Internet.</p>

<p>

My simple definitions are that</p>

<ul>

<li>

The <strong> Internet </strong> allows any computer in the world to exchange data with any other computer in the world. As a result, a <strong> client program on one computer can access a server on another computer</strong>.</li>

<li>

The <strong> Web </strong> is a <strong> hypertext system </strong> that runs over the Internet as one of its services. As a result, users can sit at any computer and <strong> browse documents that live anywhere in the world</strong>; furthermore, these documents can link to documents from any other place in the world.</li>

</ul>

<p>

Viewing the Web as a hypertext means that it needs <a class="old" href="http://www.nngroup.com/articles/browser-navigation/" title="Alertbox Nov. 1997: Lack of navigation support in v.4 browsers"> navigation support</a> features and that users will come to rely on consistent use of these navigation features to move around in hyperspace. In other words, there is a specific user interface that is optimal for the hypertext problem of navigating a huge information space to find and read information. Not that we are anywhere close to an optimal hypertext interface in today's Web browsers, but they do have some features like <code> Back </code> and <code> bookmarks </code> that users quickly learn to rely on.</p>

<p>

It is <strong> unlikely that the user interface that is optimal for browsing hypertext will also be optimal for every other thing </strong> people want to do with computers. Thus, if the Web becomes a single, universal interface to all Internet services, we will either end up with a sub-optimal hypertext interface for the browsing tasks or get a sub-optimal user interface for all the non-browsing tasks.</p>

<p>

Email is a good example: it was the first killer app for the Internet and requires a rather different user interface than Web browsing. There <em> are </em> services to access email through a Web browser, but they have a distinctly second-class feel relative to the use of a smoothly designed email interface like Eudora or Outlook.</p>

<p>

The same is true for other popular Internet services like home banking and airline reservations: optimized <strong> stand-alone applications deliver a superior user experience </strong> to that derived from shoehorning the same features into a Web browser.</p>

<p>

Obviously, these stand-alone applications need to be Internet-enabled and they must have ways of dealing with firewalls, encryption, and other practical issues in Internet access. Quite likely, the long-term solution is for operating systems to include a much richer layer of Internet services than the current simple IP transport.</p>

<p>

Stand-alone applications have some downsides:</p>

<ul>

<li>

They must be <strong> downloaded </strong> before they can be used. Once downloaded, they can provide much faster response times than a Web browser, since they only need to exchange minimal data with the server (whereas Web interfaces must download page layouts and behavior specifications along with every set of data). Thus, stand-alone applications only make sense for tasks that must be done repeatedly. For a once-only task, it is better to start immediately and then suffer a more awkward user interface and slower response times for each step.</li>

<li>

They must be <strong> reimplemented for any new computer platform </strong> that becomes sufficiently popular. This need not be a huge hardship, since some newer programming and scripting languages are cross-platform. Even so, each new platform has its own requirements, and it is obviously not possible to port an application from a desktop computer to a palm-sized computer without having to redesign its user interface. Even if the code is portable, the design is not, so some reimplementation is inevitable. For an application that is used extensively, the optimal user experience derived from this redesign will be well worth the effort, but for a rarely used application the cost may be prohibitive, meaning that it will either only be available on the most widely used platforms or that it will be restricted to an awkward Web-like interface.</li>

<li>

<strong>Administration and upgrades </strong> are often mentioned as downsides to specialized applications, but it should be possible to have component software that could upgrade itself as needed (without requiring a full download every time 10% of the code change) and that could be administered remotely (if the user grants that privilege).</li>

</ul>

<p>

Some interactions are sufficiently document-like in nature that they should not be considered applications. If the user's main interaction consists of browsing information, then a hypertext-like user interface may be fine. CarPoint's pricing calculator is a good example of using an integrated OCX control to achieve some functionality on a Web page while keeping it within the hypertext paradigm. Who cares that it's running code as long as it doesn't <em> feel </em> like it.</p>

<p align="center">

<img alt="Screenshot from

Microsoft's CarPoint service" height="469" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/carpoint.gif" width="658"/><br/>

<em>By clicking options on and off, a CarPoint user can determine the price of different car configurations. </em></p>

<p>

Clicking checkboxes in the CarPoint Auto-Pricer has no effect outside the Web page: the user is not buying the car, but simply browsing the options. Yet it is clearly a good idea to recalculate the price to reflect the currently chosen options. The price calculator is a <a class="old" href="http://www.nngroup.com/articles/when-to-open-web-based-applications-in-a-new-window/" title="Alertbox Oct. 1997:

When to step outside the page"> content feature and not a functionality feature</a>: this is why it works to embed it on a Web page. My preferred design for a car price interface would have been even more firmly based on hypertext: include links from each of the options to secondary pages with an explanation and a review of each option.</p>

<p>

The problems start once we need functionality features that include state transitions and multiple views. One of the most common usability problems on the Web these days is when the <code> Back </code> button breaks because the previous page is no longer a valid view of the data on the server. Some sites put big warnings on their pages: DO NOT TOUCH THE BACK BUTTON. This doesn't work. The <code> Back </code> button is so ingrained in users' habits that they reach for it all the time, no matter what you say. Remember that any individual website is an insignificant speck of dust in the universe of the Web: you cannot override habits formed while browsing hundreds of other sites.</p>

<p>

I think it is time to <strong> recognize that the Web cannot be all things </strong> and still retain a good user interface. Let's reserve the Web for what it's good for: browsing hypertext (including dynamic content that does not have complex functionality). And let's start building Internet-enabled client-server applications that provide optimized user interfaces on the client. The <strong> Web may still have limited roles in support </strong> of these advanced applications:</p>

<ul>

<li>

navigating to the service and finding it in the first place</li>

<li>

help and supplementary information</li>

<li>

a secondary interface with limited or awkward features for short-term use at a computer that does not have the specialized client software installed</li>

</ul>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Emerging Patterns in Interface Design" href="/courses/emerging-patterns-interface-design/?lm=does-internet-web&amp;pt=article">

<h4 class="title heading-small">Emerging Patterns in Interface Design</h4>

<p id="emerging-patterns-in-interface-design" class="description body-small">

Trending UX patterns and their impact on the total user experience

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Human Computer Interaction,new technologies</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Human Computer Interaction</span>

<a class="ga-article-related-topic" href="/topic/human-computer-interaction/">Human Computer Interaction</a>

</li>

</ul>

</div>

</div>

</div>

</div>