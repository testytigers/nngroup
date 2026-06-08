# Marginalia of Web Design - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">3</span>

<div class="article-header">

<h1 class="article-h1">Marginalia of Web Design</h1>

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

October 31, 1996

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">1996-10-31</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Marginalia of Web Design&amp;body=https://www.nngroup.com/articles/marginalia-of-web-design/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/marginalia-of-web-design/&amp;title=Marginalia of Web Design&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/marginalia-of-web-design/&amp;text=Marginalia of Web Design&amp;via=nngroup" data-share-type="Twitter">

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

<p>

This column has been touching on some pretty Big Issues lately, including <a href="/articles/accessible-design-for-users-with-disabilities/"> disabled access</a>, <a href="/articles/international-web-usability/"> international usability</a>, and <a href="/articles/the-rise-of-the-subsite/"> site structure</a>. This month, let's look at some details that may not be as profound but still matter for Web usability.</p>

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

<a class="ga-article-toc-item" href="#toc-page-titles-1">

Page Titles</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-text-size-and-color-2">

Text Size and  Color </a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-relevance-enhanced-image-reduction-better-thumbnails-3">

Relevance-Enhanced Image Reduction: Better Thumbnails</a>

</li>

</ul>

</div>

</div><h2 id="toc-page-titles-1">

Page Titles</h2>

<p>

As part of the HTML standard, every Web page should have a <code> &lt;TITLE&gt; </code> defined in its header. Page titles are important for navigation support since they are normally the default way to refer to pages in various navigation support mechanisms such as bookmark lists, history lists, overview diagrams, etc. Titles are also often used as the best way of listing retrieved pages in search engines.</p>

<p>

Many of these important uses of the page <code> &lt;TITLE&gt; </code> are taken out of context, and it is therefore important that the title has enough words to stand on its own and be meaningful when read in a menu or a search listing. On the other hand, overly long titles slow down users, so as a guideline aim at titles between four and ten words.</p>

<p>

Different pages need different titles. It is very unpleasant to visit, say, seven pages with the same title and then try to go back to a specific page from the history list. Also, of course, bookmarking more than one page from such a site is a guaranteed usability problem, since the bookmark/favorites menu will contain several identical entries with different results.</p>

<p>

A final point is to optimize titles for quick scanning. This implies moving information carrying terms toward the beginning of the title and preferably starting with a word that will match the user's needs when scanning down a menu or listing of titles. A classic mistake is to use a title like <code> <strong> Welcome to MyCompany</strong></code>. It would be much better to call the page <code> <strong> MyCompany - Home Page</strong></code>. Similarly, eliminate articles like The, A, and An from the beginning of the title. Doing so is particularly important because some title listings are alphabetized.</p>

<p>

<img align="right" alt="Page miniature of this webpage" height="123" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/pageminiature.gif" width="94"/> In addition to titles, other ways of referring to Web pages include verbal and visual summaries. Normally, such summaries are very difficult to produce algorithmically. The main exception is the <strong> miniature </strong> as shown by the illustration to the right. The figure shows a miniature of this page, generated by scaling it to 15 percent of full size. In general, page miniatures are only good as representations for highly graphic pages or pages with very characteristic layout.</p>

<p>

Two of the better uses of miniatures are for building a site map and for the history list when navigating sites that focus on visual arts.</p>

<h2 id="toc-text-size-and-color-2">

Text Size and <font color="blue" style="color: blue"> Color </font></h2>

<p>

Tell me, did you feel like clicking on the word "Color" in the above heading? Most likely, the word appeared in blue type, and if so you probably thought it was a hypertext link.</p>

<p>

On the Web, blue text equals clickable text, so <strong> never </strong> make text blue if it is not clickable. It is also bad, though not quite as bad, to make text red or purple, since these two colors are often used to denote hypertext links that have already been visited.</p>

<p>

<big>Another commonly seen mistake in text design is the use of large or small font sizes as the body text of a page. Page designers sometimes think that the default text in their browser is wrong for the effect they want to achieve, and it is certainly acceptable to make a small percentage of the text on a given page large or small, as appropriate. It is <strong> not </strong> recommended to change the font size of <em> all </em> the text on a page since the user must be assumed to have set the default font size in his or her browser to exactly the size that is most comfortable for that user on his or her monitor. Any other font size is thus by definition suboptimal for reading body text. </big></p>

<h2 id="toc-relevance-enhanced-image-reduction-better-thumbnails-3">

Relevance-Enhanced Image Reduction: Better Thumbnails</h2>

<p>

It is quite common to use thumbnail versions to represent images that are too large to be downloaded without a specific user request. Thumbnails are smaller, meaning that more can fit on a page and that download times are minimized. Unfortunately, the two most common ways of reducing images, scaling and cropping, both result in thumbnails that can be hard to interpret, as shown in the figure.</p>

<center>

<br/>

<img alt="A photo and three different thumbnails of same" height="238" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/relevance.jpg" width="580"/><br/>

<em>Three different ways of making thumbnails. </em></center>

<p>

</p>

<p>

Scaling reduces the image so much that pictures with extensive detail wash out and become too crowded to be meaningful. Cropping preserves those details that are within the new viewport, but at the cost of losing the context of the image as a whole. My recommendation is to use a combination of cropping and scaling, resulting in a technique I call <em> relevance-enhanced image reduction </em> . For example, to get a thumbnail that is 10 percent of the original image, first crop the image to 32 percent of the original size and then scale the result to 32 percent. The final image will be 0.32 x 0.32 = 0.1 of the original.</p>

<p>

As shown in the figure, relevance-enhanced image reduction results in a pleasant balance between presenting discernible detail and conserving context.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="The Human Mind and Usability" href="/courses/human-mind/?lm=marginalia-of-web-design&amp;pt=article">

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

<a class="tile ga-article-related-course" data-course-title="Web Page UX Design" href="/courses/web-page-design/?lm=marginalia-of-web-design&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Web Usability</span>

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