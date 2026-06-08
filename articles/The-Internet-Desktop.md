# The Internet Desktop - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">2</span>

<div class="article-header">

<h1 class="article-h1">The Internet Desktop</h1>

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

February 29, 1996

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">1996-02-29</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: The Internet Desktop&amp;body=https://www.nngroup.com/articles/the-internet-desktop/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/the-internet-desktop/&amp;title=The Internet Desktop&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/the-internet-desktop/&amp;text=The Internet Desktop&amp;via=nngroup" data-share-type="Twitter">

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

<div class="article-body">

<p align="center">

<strong>Warning: </strong> Abstractions ahead this month</p>

<p>

We sometimes say that the network is the computer, but how will users interact with such a beast? Currently, the user experience of a highly networked computer is still very similar to that of using a personal computer, but in a few years we will see the emergence of new user interfaces that are optimized for connectivity. We call this the <em> Internet Desktop </em> .</p>

<p>

A key element of the Internet Desktop will be to <strong> get rid of Web browsers </strong> as a separate application category. There are two reasons you will want to eliminate the web browser from your system in a few years:</p>

<ol>

<li>

Fundamentally, it is pretty silly to have a special browser for certain information objects simply because they happen to come from a specific storage location. There is no reason to treat information differently because it comes from the Internet instead of coming from your harddisk. Just imagine if we treated information differently depending on whether it was stored on a floppy disk (the transport protocol for "Sneakernet") or on your harddisk. You try to read a file but get an error message: <em> Sorry, this file is stored on a floppy disk so you need to start your floppy browser before you can read it! </em></li>

<li>

Web browsers confuse two feature sets that can be delivered more cleanly if they are separated: web browsers handle both the <strong> presentation </strong> of information objects <em> and </em> the <strong> navigation </strong> between information objects. Actually, as discussed in a prior column, current web browsers do a <a href="/articles/features-for-the-next-generation-of-web-browsers"> lousy job of navigation support </a> , but they do try.</li>

</ol>

<p>

The Internet Desktop will unify the treatment of all information objects, no matter where they live: local harddisk, local area network, corporate intranet, and the Internet will all have the same user interface and users will move seamlessly between various storage locations. The Internet Desktop will provide a framework for presentation applets that are optimized for each of the various data types accessed by the user. HTML will obviously be one such data type, and an HTML viewer will definitely be available. The Internet Desktop will provide navigation as a universal support mechanism that cuts across the presentation applets. For example, the Desktop's history mechanism will allow users to return to previously seen information objects no matter what presentation applet was used to display them: the history list, bookmark list, etc. will include Internet objects, email messages, and corporate documents intermixed according to the individual user's information access behavior (each person has a single consciousness leading to a linear user experience that can structure the history of information use). There will also be some kind of universal search feature to allow users to find objects by content, though it currently not clear how to extend the search from local data to Internet data (most likely, the search will be scoped with billion-object searches reserved for exceptional cases).</p>

<p>

</p>

<p>

I am deliberately using terms like <em> presentation applet displaying an information object </em> instead of traditional terms like <em> opening a file in an application. </em> I believe that the traditional concept of "the file" is poised to be removed from the user experience since it is much too inflexible (for more information, please see my essay on <a href="/papers/filedeath.html"> The Death of File Systems </a> ). As a simple example, the delivery of an information object to the presentation applet will not be an exact duplicate of the stored version of the information object. First, of course, all information of any importance will be encrypted during storage and transport and will be decrypted by the Internet Desktop before being handed to the presentation applet. Second, the presentation version of the object will be modified to suit the specific circumstances of each display operation: if, for example, an image object is being sent to a PDA user with a monochrome screen then it will be converted from 24-bit color into black-and-white <em> before </em> leaving the server (and it may be compressed with severe lossiness if the user is on an expensive wireless connection). There will be no single, canonical representation of information objects - goodbye WYSIWYG; hello adaptable data.</p>

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

<a class="ga-article-toc-item" href="#toc-update-1">

Update</a>

</li>

</ul>

</div>

</div><h2 id="toc-update-1">

Update</h2>

<p>

Revisiting these concepts in 2000: <a class="new" href="/articles/the-network-is-the-user-experience-microsofts-net-announcement/" title="Alertbox June 2000"> The Network is the User Experience </a> .</p>

<p>

</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Emerging Patterns in Interface Design" href="/courses/emerging-patterns-interface-design/?lm=the-internet-desktop&amp;pt=article">

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