# The Need for Speed - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">4</span>

<div class="article-header">

<h1 class="article-h1">The Need for Speed</h1>

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

February 28, 1997

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">1997-02-28</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: The Need for Speed&amp;body=https://www.nngroup.com/articles/the-need-for-speed-1997/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/the-need-for-speed-1997/&amp;title=The Need for Speed&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/the-need-for-speed-1997/&amp;text=The Need for Speed&amp;via=nngroup" data-share-type="Twitter">

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

</span>All usability studies show that fast response times are essential for Web usability: let&#x27;s believe the data for once! Advice for speeding up sites despite the fact that bandwidth is going down, not up.

</div>

<div class="article-body">

<p>Every Web usability study I have conducted since 1994 has shown the same thing: users beg us to speed up page downloads. In the beginning, my reaction was along the lines of "let's just give them better design and they will be <em> happy </em> to wait for it". I have since become a reformed sinner since even my skull is not thick enough to withstand consistent user pleas year after year.</p>

<p>Research on a wide variety of <a href="http://www.nngroup.com/books/multimedia-and-hypertext/"> hypertext</a> systems has shown that users need response times of less than one second when moving from one page to another if they are to navigate freely through an information space. Traditional human factors research into <a href="/articles/response-times-3-important-limits/">response times</a> also shows the need for response times faster than a second. For example, studies done at IBM in the 1970s and 1980s found that mainframe users were more productive when the time between hitting a function key and getting the requested screen was less than a second.</p>

<p><img align="right" alt="Distribution of the bandwidth of users' connections to the Internet over the last three years" height="259" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/connection_speeds.gif" width="380"/></p>

<p>Unfortunately we are not getting subsecond response times on the Web any time soon, so we know that users are going to be hurt by slow downloads. Currently, the minimum goal for response times should therefore be to get pages to users in no more than ten seconds, since that's the limit of people's ability to keep their attention focused while waiting.</p>

<p>The figure shows the distribution of the speeds with which users have connected to the Internet according to the last six <a href="http://www.cc.gatech.edu/gvu/user_surveys/"> Georgia Tech Web user surveys</a>. Two things are clear from the figure: users are replacing slow modems (14.4) with fast modems (28.8 or 33.6), but the proportion of users who connect at modem-speeds stays about the same. Even worse, the proportion of users connecting at <strong> high bandwidths (T-1 or better) is going down</strong>, even though the Web requires at least <a href="/articles/needing-personal-t1-line/">T-1 speed</a> to work well. Mid-band (ISDN, leased lines, etc.) is increasing somewhat, but the truth is that mid-band speeds are insufficient for decent Web response times.</p>

<p>The problem is that the user's experienced response time is a determined by the weakest link in the chain from server to browser:</p>

<ul>

<li>the <strong> throughput of the server</strong>: ought not to be a problem since the cost of hardware is the smallest part of developing a website, but popular sites often get surprised by rapidly increasing traffic and do not upgrade their machines fast enough.</li>

<li>the <strong> server's connection </strong> to the Internet: many sites try to save on their connection and put off upgrading from, say, a T-1 to a T-3 even when their current connection is saturated</li>

<li>the <strong> Internet itself</strong>: even though the net keeps getting upgraded, it still has bottlenecks, especially for cross-continent connections and for use at peak hours</li>

<li>the <strong> user's connection </strong> to the Internet: as discussed above, connection speeds are very low for the majority of users and will stay that way for several years</li>

<li>the rendering <strong> speed of the user's browser </strong> and computer: rarely a big problem, though complex tables can take significant time to lay out on low-end machines</li>

</ul>

<p>Each of these many steps introduces its own delay in getting a webpage from the server to the user. Unfortunately, the delays are <strong> cumulative</strong>, meaning that we are not going to get snappy response times simply by improving a single link in the chain: when you upgrade from a modem to an ISDN line, you typically get twice as good Web performance and not the five times improvement implied by the bitrates.</p>

<p>Considering these fundamental facts in both human factors and computer networking, there is only one conclusion: webpages have to be designed with speed in mind. In fact, <strong> speed must be the overriding design criterion</strong>. To keep <a href="/articles/size-limits-for-web-pages/"> page sizes small</a>, graphics should be kept to a minimum and <a href="/articles/guidelines-for-multimedia-on-the-web/">multimedia</a> effects should only be used when they truly add to the user's understanding of the information.</p>

<p>Conservative use of graphics does not imply boring pages. Much can be done by colored table cells and creative (but restrained) use of different fonts. In particular, <a href="/articles/effective-use-of-style-sheets/"> style sheets</a> can be used to improve page design without incurring a download penalty. If you are using style sheets (and everybody should be doing so by the end of 1997), I do recommend making them linked rather than embedded: a linked style sheet only needs to be downloaded once (assuming that you have a consistent style for your site), whereas embedded styles add to the size of every single page.</p>

<p>The most important issue in response time is when the user gets to see a screenful of useful information. It matters less if it takes longer to load the full page and all its illustrations if the user can start acting on <em> some </em> information fast. Guidelines for fast initial loading are:</p>

<ul>

<li>the top of the page should be meaningful even when no images have been downloaded (i.e., more text, less images)</li>

<li>use ALT attributes for images so that the user can understand what they are about before they are rendered</li>

<li>the browser must draw the top of the page fast: it can only do so if it has all the information it will need for layout, so include WIDTH and HEIGHT attributes on all images and table columns</li>

<li>complex tables often take a long time to render, so cut down on the complexity of your tables by splitting the information into several tables. In particular, the top table should be simple and fast to render.</li>

</ul>

<p>A practical tip: links to a directory should include the final slash in the URL when embedded in webpages. The slash should be left out when writing the URL for human consumption. For example, the link to the list of Alertbox columns should be written as <code>http://www.useit.com/alertbox</code> in a (printed) magazine article but coded as <code>http://www.useit.com/alertbox/</code> for the hypertext anchor in the online version of the article. The reason to include the slash in online links is to avoid a redirect when the server would have told the browser that the link refers to a directory and not a file. Adding trailing slashes to HREFs when appropriate reduces latency by a small but noticeable amount, so you may as well do it.</p>

<p>A final recommendation is to use a server that supports HTTP keep-alive: saving the overhead of establishing a new TCP/IP connection for every "hit" cuts latency dramatically. The experienced response time to load a page often <a href="http://www.w3.org/Protocols/HTTP/Performance/Pipeline.html">drops to about half</a> by using keep-alive.</p>

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

<a class="ga-article-toc-item" href="#toc-more-on-responsiveness-1">More on Responsiveness</a>

</li>

</ul>

</div>

</div><h2 id="toc-more-on-responsiveness-1">More on Responsiveness</h2>

<p><a class="new" href="/articles/website-response-times/" title="Alertbox: Website Response Times">2010 update to this article</a> (including eyetracking example of the devastating effect of slow response times).</p>

<p><a href="https://www.nngroup.com/articles/the-need-for-speed/">2020 update</a>: median page download times are 6 seconds on desktop and 20 seconds on mobile.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Application Design for Web and Desktop" href="/courses/application-ux/?lm=the-need-for-speed-1997&amp;pt=article">

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

<li>

<a class="tile ga-article-related-course" data-course-title="Emerging Patterns in Interface Design" href="/courses/emerging-patterns-interface-design/?lm=the-need-for-speed-1997&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">response time,Application Design,Human Computer Interaction,new technologies</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Application Design</span>

<a class="ga-article-related-topic" href="/topic/applications/">Application Design</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/human-computer-interaction/">Human Computer Interaction</a>

</li>

</ul>

</div>

</div>

</div>

</div>