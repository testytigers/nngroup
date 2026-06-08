# Why Frames Suck (Most of the Time) - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">6</span>

<div class="article-header">

<h1 class="article-h1">Why Frames Suck (Most of the Time)</h1>

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

November 30, 1996

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">1996-11-30</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Why Frames Suck (Most of the Time)&amp;body=https://www.nngroup.com/articles/why-frames-suck-most-of-the-time/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/why-frames-suck-most-of-the-time/&amp;title=Why Frames Suck (Most of the Time)&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/why-frames-suck-most-of-the-time/&amp;text=Why Frames Suck (Most of the Time)&amp;via=nngroup" data-share-type="Twitter">

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

</span>Frames break the unified model of the web and introduce a new way of looking at data that has not been well integrated into the other aspects of the web.

</div>

<div class="article-body">

<p><img align="right" alt="Frame Free Logo" border="0" height="120" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/framefree.gif" width="79"/> Judging from the email I receive, the most controversial statement I have made in my Alertbox columns so far was to make "the use of frames" one of the mistakes in my first list of <a href="/articles/original-top-ten-mistakes-in-web-design/"> top 10 mistakes in web design</a>.</p>

<p>For new or inexperienced web designers, I stand by my original recommendation. <strong> Frames: Just Say No. </strong></p>

<p>With respect to the use of frames by highly skilled web designers, I have changed my opinion somewhat: people who <em> really </em> know what they are doing can sometimes use frames to good effect, though even experienced designers are advised to use frames as sparingly as possible.</p>

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

<a class="ga-article-toc-item" href="#toc-fundamental-problems-with-frames-1">Fundamental Problems with Frames</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-implementation-problems-with-frames-2">Implementation Problems with Frames</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-when-its-ok-to-use-frames-3">When It's OK to Use Frames</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-toward-a-richer-node-model-4">Toward a Richer Node Model</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-have-these-conclusions-changed-5">Have These Conclusions Changed?</a>

</li>

</ul>

</div>

</div><h2 id="toc-fundamental-problems-with-frames-1">Fundamental Problems with Frames</h2>

<p>Part of the genius of Tim Berners-Lee's original design of the web was a total unification of several concepts in a single idea, <strong> the page</strong>:</p>

<ul>

<li>the user's <strong>view</strong> of the information on the screen</li>

<li>the unit of <strong>navigation</strong> (what you get when you click a link or activate a navigation action like a bookmark)</li>

<li>a textual <strong>address</strong> used to retrieve information over the net (the URL)</li>

<li>the storage of the information on the server and the author's <strong>editing unit</strong> (except if using embedded objects like image files which do require the author to manage multiple files for a page)</li>

</ul>

<p>The fundamental design of the web is based on having the page as the atomic unit of information, and the notion of the page permeates all aspects of the web. The simplicity of the original web contributed to its ease of use and its rapid uptake.</p>

<p>Frames break the unified model of the web and introduce a new way of looking at data that has <a href="https://www.nngroup.com/articles/style-sheets-vs-frames-as-web-extensions/"> not been well integrated</a> into the other aspects of the web. With frames, the user's view of information on the screen is now determined by a <em> sequence </em> of navigation actions rather than a <em> single </em> navigation action.</p>

<p>Navigation does not work with frames since the unit of navigation is different from the unit of view. If users create a bookmark in their browser they may not get the same view back when they follow the bookmark at a later date since the bookmark doesn't include a representation of the state of the frames on the page.</p>

<p>Even worse, URLs stop working: the addressing information shown at the top of the browser no longer constitutes a complete specification of the information shown in the window. If an author copies the URL in order to include it as a hypertext anchor in one of his or her own pages then that anchor will not lead readers to the desired view but to the initial state of the frameset. Similarly, if a user decides to send an email message to a friend with the recommendation to check out a page, then copying the URL from the browser will not work if frames are used since the URL points to the frameset and not to the current view (with the information of interest to the friend). Given that <a href="https://www.nngroup.com/articles/social-proof-ux/">social filtering</a> is one of the most powerful mechanisms for information discovery on the internet, it is an utter disaster to disable the URL as an addressing mechanism.</p>

<h2 id="toc-implementation-problems-with-frames-2">Implementation Problems with Frames</h2>

<p>In addition to the fundamental problems discussed above, there are several minor problems with the current implementation of frames. These problems will go away over the next few years, but for designs done in 1997 (and maybe even 1998) they will remain a reason to minimize use of frames.</p>

<h3>Users with Frames-Challenged Browsers</h3>

<p>The November 1996 browser statistics from Interse show the following distribution of browser usage:</p>

<ul>

<li>Netscape 2: 13% of users</li>

<li>Netscape 3: 47% of users</li>

<li>Internet Explorer 3: 28% of users</li>

<li>Other browsers or earlier versions: 13% of users</li>

</ul>

<p>Percentages sum to 101% due to rounding. Thus, 13% of users would not even be able to <em> see </em> a site with frames. Sure, it is possible in principle to use the <code> &lt;NOFRAMES&gt; </code> feature to serve alternate content to these users, but most designers don't bother designing two versions of their pages and reserve <code> &lt;NOFRAMES&gt; </code> for a "helpful" link to the download site for a frames-supporting browser version.</p>

<p>13% of users are still using Netscape 2 which had one of the worst usability problems to be seen on the web so far: the BACK button in the browser simply didn't work with framed sites. The BACK feature is an absolutely essential safety net that gives users the confidence to navigate freely in the knowledge that they can always get back to firm ground. We have known from some of the earliest studies of user navigation behavior that BACK is the second-most used navigation feature in web browsers (after the simple "click on a link to follow it" action). Thus, breaking the BACK button is no less than a usability catastrophe.</p>

<p>Combining these two statistics leads to the conclusion that more than a quarter of the users either can't see frames at all or can only do so while suffering severe usability problems. Even though many of these users will upgrade over the next year, there will probably still be about 10% left by the end of 1997. Remember that many people don't view web browsing as a central part of their lives and therefore don't invest much effort in keeping up with the changing tools.</p>

<p>Thus, even if frames improve a design, they only do so for 3/4 of the users, meaning that the improvement will have to be substantial to be worth the additional effort and the risk of aggravating the frames-poor quarter of the users.</p>

<h3>Print Problems</h3>

<p>Many browsers cannot print framed pages appropriately. Of course, most browsers don't print <em> anything </em> really well, but at least regular pages normally print in full. With frames, it is common to have the print command result in the printing of a single frame. Printing the full page is difficult with scrolling frames: should only the visible part of the frame be printed or should the content be allowed to expand and take up more room than it does on the screen?</p>

<h3>Authoring Problems</h3>

<p>The original release of HTML was simple enough that many people learned it without any problems. Frames are another matter, though. Newsgroups like <code> comp.infosystems.www.authoring.html </code> are filled with questions from web authors who desperately need to know why their frames don't work as intended. Frames are currently so hard to learn that many page authors write buggy code.</p>

<h3>Search Problems</h3>

<p><a class="out" href="http://www.eric-a-hall.com/articles/19980209.html" title="Case study: how search engines index and describe a site with and without frames - Eric Hall's net.Opinion for Feb. 1998">Search engines have trouble with frames</a> since they don't know what composites of frames to include as navigation units in their index.</p>

<h3>User Preferences</h3>

<p>Many websites that offer users a choice between regular and framed versions have found that most users prefer frame-free designs.</p>

<h2 id="toc-when-its-ok-to-use-frames-3">When It's OK to Use Frames</h2>

<p>The main issue in using frames is to ensure that URLs keep working. To do so, all hypertext links must have a <code> TARGET="_top" </code> attribute in their anchor tag (e.g., <code> &lt;A HREF=foo.html TARGET="_top"&gt; </code> ). Adding the <code> _top </code> makes the browser clear out all the frames and replace the entire window with a new frameset. The destination frameset may well have many frames that are identical to the ones in the departure frameset and will be cached in the browser, but by forcing a complete reload in principle, the browser gets a new URL for the destination. This means that navigation actions (e.g., bookmarking) work again and that the URL is available for other people to link to.</p>

<p>The only exception from the need to use a <code> TARGET="_top" </code> attribute is when frames are used as a shortcut for scrolling within a single page. For example, a very long directory or other alphabetical listing could have a frame on top listing the letters of the alphabet. Clicking one of these letters would cause the listing to scroll within another frame while keeping the user on the same page and thus not destroying navigation.</p>

<p>Frames are also useful for "meta-pages" that comment on other pages. For example, a web design styleguide may need to mix discussions of design principles with live examples of entire pages that follow (or break) the rules. In these cases, the embedded page should be treated as an embedded image (even though it is implemented as an independent page) and the "main" information that users will want to bookmark should be the content of the commenting frame.</p>

<p>Finally, it seems that the <a href="https://www.w3.org/TR/WD-frames-970331"> inline frames</a> introduced in HTML 4.0 will be mostly harmless. A frame that is inlined will be subordinate to the main page, and the user can still bookmark the main page and navigate as usual. Since mainstream browsers still do not implement HTML 4.0, we don't know whether inline frames will have their own implementation problems: in particular, it is doubtful whether good ways will be found to print pages that have scrolling inline frames. (My current best guess is that it will be best to print the currently visible part of a scrolling inline frame in order to maintain the layout of the main page, but some users may want to have the entire contents printed, so messy option settings may be necessary.)</p>

<h2 id="toc-toward-a-richer-node-model-4">Toward a Richer Node Model</h2>

<p>In the long term, we will need a richer model for hypertext nodes on the web than can be supported by frames. For example, composite nodes, typed nodes, hierarchical nesting of nodes, nodes with different views, and nodes with actions that influence other nodes are all ideas that have been explored in <a href="http://www.nngroup.com/books/multimedia-and-hypertext/"> hypertext research</a>. It will be important to retain the positive attributes of the web as we move toward these richer information structures.</p>

<h2 id="toc-have-these-conclusions-changed-5">Have These Conclusions Changed?</h2>

<p>Learn the latest usability guidelines in our course on <a class="new" href="http://www.nngroup.com/events/tutorials/usability.html" title="Nielsen Norman Group: conference tutorial outline">Web Page UX Design</a> at the <a class="new" href="https://www.nngroup.com/training/" title="Conference program and list of usability training tutorials"> UX Conference</a>.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Emerging Patterns in Interface Design" href="/courses/emerging-patterns-interface-design/?lm=why-frames-suck-most-of-the-time&amp;pt=article">

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

<li>

<a class="tile ga-article-related-course" data-course-title="The Human Mind and Usability" href="/courses/human-mind/?lm=why-frames-suck-most-of-the-time&amp;pt=article">

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

<a class="tile ga-article-related-course" data-course-title="Web Page UX Design" href="/courses/web-page-design/?lm=why-frames-suck-most-of-the-time&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Web Usability,web trends,ui elements,design mistakes,computer history</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Web Usability</span>

<a class="ga-article-related-topic" href="/topic/web-usability/">Web Usability</a>

</li>

</ul>

</div>

</div>

</div>

</div>