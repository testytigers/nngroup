# Using the Title Attribute to Help Users Predict Where They Are Going - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">3</span>

<div class="article-header">

<h1 class="article-h1">Using the Title Attribute to Help Users Predict Where They Are Going</h1>

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

June 19, 2016

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2016-06-19</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Using the Title Attribute to Help Users Predict Where They Are Going&amp;body=https://www.nngroup.com/articles/title-attribute/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/title-attribute/&amp;title=Using the Title Attribute to Help Users Predict Where They Are Going&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/title-attribute/&amp;text=Using the Title Attribute to Help Users Predict Where They Are Going&amp;via=nngroup" data-share-type="Twitter">

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

</span>The link title attribute can be used to provide additional details for mouse users, but should not be relied on as the main source of information scent.

</div>

<div class="article-body">

<p>One of the greatest problems on the web is that <strong>users don't know where they are going</strong> when they follow links. Web browsers have the ability to pop up a short explanation of a link <em>before </em>the user selects it. Such explanations can give users a <strong>preview of where the link will lead </strong>and improve their navigation:</p>

<ul>

<li><strong>bad links are less likely to be followed</strong>; users will waste less time going down the garden path</li>

<li>increasing users' understanding of good links helps them interpret the destination page upon arrival and <strong>reduce</strong> <strong>disorientation</strong></li>

</ul>

<p>The link explanation is called a link title and most browsers display it in a <strong>tooltip</strong>. It is very easy to encode — for example, the HTML code for adding a title to the link in the following paragraph is <code><a>&lt;a href="https://www.nngroup.com/articles/information-scent/" title="Alertbox: Information Foraging — Why Google Makes People Leave Your Site Faster"&gt;</a></code>. If you rest your cursor on the “information scent” link below, the title will pop up after about a second. Having an informative tooltip appear when the mouse hovers on a link gives users an indication of the type of information they can expect to get from following the link. Although it’s not a good practice to rely <em>only </em>on the title attribute to convey <a href="https://www.nngroup.com/articles/information-scent/" title="Alertbox: Information Foraging – Why Google Makes People Leave Your Site Faster">information scent</a>, you can take advantage of it to provide additional detail about that link. The title attribute can be applied to other HTML elements (such as images and form fields) beside links.</p>

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

<a class="ga-article-toc-item" href="#toc-guidelines-for-link-titles-1">Guidelines for Link Titles</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-touchscreen-devices-and-the-title-attribute-2">Touchscreen Devices and the Title Attribute</a>

</li>

</ul>

</div>

</div><h2 id="toc-guidelines-for-link-titles-1">Guidelines for Link Titles</h2>

<ul>

<li>The goal of the link title is to <strong>help users predict</strong> what will happen if they follow a link.</li>

<li>Appropriate information to include in a link title can be:

<ul>

<li><strong>name of the site</strong> the link will lead to (if different from the current site)</li>

<li><strong>name of the subsite</strong> the link will lead to (if staying within the current site but moving to a different part of the site)</li>

<li>added details about the <strong>kind of information to be found on the destination page</strong> and how it relates to the link name and to the context of the current page</li>

<li>warnings about possible problems at the other end of the link (for example, "Subscription required" when linking to <em>The Wall St. Journal</em>)</li>

</ul>

</li>

<li>Link titles should be less than 80 characters, and should only <strong>rarely go above 60 characters</strong>. Shorter link titles are better; however super-tooltips are useful for displaying more text in the context of a large overview screen.</li>

<li><strong>Do not add link titles to all links</strong>: if it is <em>obvious</em> from the link name and its surrounding context where the link will lead, then a tooltip will increase clutter and ultimately reduce usability. (Even if users may not actually purposefully hover on the link, the tooltip may be displayed while the user moves the mouse.) A link title is superfluous if it simply repeats the same text that is already shown in the link label displayed on the page.</li>

<li>Do not assume that the link title will look the same for all users. Indeed, screen readers will not display the text, but may read the text aloud. Different browsers will <strong>display link titles in different ways</strong>, as shown in the figure. And most touchscreen browsers will not display the link title at all.</li>

</ul>

<figure class="caption"><img alt="" border="0" height="227" loading="lazy" src="https://media.nngroup.com/media/editor/2016/06/15/microsoft-tooltip-example.png" width="720"/>

<figcaption><em>Example of a Tooltip on Edge on Microsoft Windows 10</em></figcaption>

</figure>

<figure class="caption"><img alt="" border="0" height="227" loading="lazy" src="https://media.nngroup.com/media/editor/2016/06/15/safari-tooltip.png" width="720"/>

<figcaption><em>Example of a Tooltip on Safari on Mac OS X</em></figcaption>

</figure>

<p>Finally and most important, link titles do not eliminate the need for good information scent: <strong>the link label and its surrounding text should be understandable</strong> even if the link title is not displayed. Users should not have to point to a link to understand what it means: the tooltip should be reserved for <em>supplementary</em> information. Moreover, the link text should be properly <em>formatted</em> to ensure good scannability.</p>

<h2 id="toc-touchscreen-devices-and-the-title-attribute-2">Touchscreen Devices and the Title Attribute</h2>

<p>Some <a href="http://www.w3.org/TR/html/dom.html#the-title-attribute" title="World Wide Web Consortium: comments on the title attribute">people recommend against link titles</a> because hovering is not supported by touchscreen browsers and by keyboard-only browsers. Although a special gesture such as the <a href="https://www.nngroup.com/articles/3d-touch/" title="Article: 3D Touch on iPhone 6S: Embrace the Force">3D Touch</a> could be used to display the tooltip, most touchscreen browsers do not support this feature. However, this is no reason to deny the usability benefits of link titles to those users who do use a mouse. As long as the link title is treated as an <a href="https://www.nngroup.com/articles/enhancement/" title="Article: The Role of Enhancement in Web Design">enhancement</a> for mouse users and is not required for using the site, you can help some users without hurting others. Since a browser that does not display link titles will simply ignore them and will not change in any way the layout of the page, we recommend that you use this feature as a way to fully take advantage of the desktop capabilities and to optimize for this device.</p>

<p><em>(An earlier version of this article was originally published January 11, 1998. The article was last updated and revised on June 19, 2016.)</em></p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Navigation</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Navigation</span>

<a class="ga-article-related-topic" href="/topic/navigation/">Navigation</a>

</li>

</ul>

</div>

</div>

</div>

</div>