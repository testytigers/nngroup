# The Difference Between Web Design and GUI Design - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">3</span>

<div class="article-header">

<h1 class="article-h1">The Difference Between Web Design and GUI Design</h1>

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

April 30, 1997

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">1997-04-30</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: The Difference Between Web Design and GUI Design&amp;body=https://www.nngroup.com/articles/the-difference-between-web-design-and-gui-design/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/the-difference-between-web-design-and-gui-design/&amp;title=The Difference Between Web Design and GUI Design&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/the-difference-between-web-design-and-gui-design/&amp;text=The Difference Between Web Design and GUI Design&amp;via=nngroup" data-share-type="Twitter">

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

<p>Designing for the Web is different from designing traditional software user interfaces. Mainly, the designer has to <strong> give up full control </strong> and share responsibility for the UI with users and their client hardware/software.</p>

<p>Of course there are also <a href="/articles/why-web-design-similar-gui-design/"> similarities </a>  between designing for the Web and traditional UI design: at the most basic level, both are interactive systems, and both are software designs as opposed to the design of physical objects.</p>

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

<a class="ga-article-toc-item" href="#toc-device-diversity-1">Device Diversity</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-the-user-controls-navigation-2">The User Controls Navigation</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-part-of-a-whole-3">Part of a Whole</a>

</li>

</ul>

</div>

</div><h2 id="toc-device-diversity-1">Device Diversity</h2>

<p>In traditional GUI design, you control every pixel on the screen: as you lay out a dialog box, you can rest assured that it will look <em> exactly </em> the same on the user's screen. You know what system you are designing for, you know what fonts it has installed, you know how large the screen typically will be, and you have the system vendor's styleguide to tell you the rules for combining the interaction widgets.</p>

<p>On the Web, all these assumptions fall apart. Users may be accessing the Web through traditional computers, but could easily be using a <a href="/articles/webtv-usability-review/"> WebTV </a> , a pen-based hand-held device, a Nokia cellphone, or even their car as an Internet device. In traditional design, the difference in screen area between a laptop and a high-end workstation is a factor of six. On the Web, we currently need to accommodate a factor of 100 in screen area between handhelds and workstations and a factor of 1,000 in bandwidth between modems and T-3 connections.</p>

<p>Any given Web design will look very different on this variety of devices: clearly, WYSIWYG is dead. Indeed, <strong> looking different is a feature, not a bug </strong> , since an optimal user experience requires adjustments to the characteristics of each device. The more specialized or low-end the device, the stricter the requirements for Web content to morph into something suited for the platform. The only way to make this happen is for designers to give up full control and let the presentation of their pages be determined by an interplay of page specifications and the preference settings and other characteristics of the client device.</p>

<p>Designing an abstract UI specification that is instantiated differently for each platform is much harder than it sounds. The basic principles of HTML can take the designer a long way toward the ideal, but not all the way there. It is recommended to separate meaning and presentation and to use <a href="/articles/effective-use-of-style-sheets/"> style sheets </a>  to specify presentation, but doing so works better for informational content than for interactions.</p>

<h2 id="toc-the-user-controls-navigation-2">The User Controls Navigation</h2>

<p>In traditional GUI design, the designer can control where the user can go when. You can gray out menu options that are not applicable in the current state, and you can throw up a modal dialog box that takes over the computer until the user has answered the question.</p>

<p>On the Web, the user fundamentally controls his or her navigation through the pages. Users can take paths that were never intended by the designer: for example, they can jump straight into the guts of a site from a search engine without ever going through the home page. Users also control their own bookmark menu and can use it to create a customized interface to a site.</p>

<p>Web designers need to accommodate and support user-controlled navigation. Sometimes you can force users through set paths and prevent people from linking to certain pages, but sites that do so feel harsh and dominating. It is better to design for freedom of movement and, for example, put a logo (linked to the home page) on every page to provide context and navigation for users who have gone straight to that page.</p>

<h2 id="toc-part-of-a-whole-3">Part of a Whole</h2>

<p>A traditional application is an enclosed user interface experience: even though window systems allow application-switching and make multiple applications visible simultaneously, the user is fundamentally "in" a single application at any given time and only that application's commands and interaction conventions are active. Users spend relatively long periods of time in each application and become familiar with its features and design.</p>

<p>On the Web, users move between sites at a very rapid pace and the borders between different designs (i.e., sites) are very fluid. It is rare for users to spend more than a few minutes at a time at any given site, and users' navigation frequently takes them from site to site to site as they follow the hyperlinks. Because of this rapid movement, users feel that they are <strong> using the Web as a whole </strong> rather than any specific site: users don't want to read any manuals or help information for individual sites but demand the ability to use a site on the basis of the Web conventions they have picked up as an aggregate of their experience using other sites. In usability studies, users complain bitterly whenever they are exposed to sites with too diverging ways of doing things. In other words, <strong> the Web as a whole has become a genre </strong> and each site is interpreted relative to the rules of the genre.</p>

<p>Traditional GUIs are also part of a whole, of course, and it is advisable to follow the vendor's design styleguide. The point is that the balance between individual design and the whole tilts in favor of the whole for Web designs. At the same time, we don't have any established Web design styleguide that can dictate how designers should use their interface vocabulary to build sites that fit this whole. I am a strong proponent of getting an official set of Web design conventions; as long as we don't have one, my advice to Web designers is to design to fit in and to acknowledge that your site is not the center of the users' universe: they <em> are </em> going to move between sites, and we <em> have </em> to make it easy for them to use each new site as they go.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Application Design for Web and Desktop" href="/courses/application-ux/?lm=the-difference-between-web-design-and-gui-design&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Application Design</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Application Design</span>

<a class="ga-article-related-topic" href="/topic/applications/">Application Design</a>

</li>

</ul>

</div>

</div>

</div>

</div>