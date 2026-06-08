# Effective Use of Style Sheets - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">5</span>

<div class="article-header">

<h1 class="article-h1">Effective Use of Style Sheets</h1>

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

June 30, 1997

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">1997-06-30</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Effective Use of Style Sheets&amp;body=https://www.nngroup.com/articles/effective-use-of-style-sheets/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/effective-use-of-style-sheets/&amp;title=Effective Use of Style Sheets&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/effective-use-of-style-sheets/&amp;text=Effective Use of Style Sheets&amp;via=nngroup" data-share-type="Twitter">

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

<p>Cascading style sheets (<a href="http://htmlhelp.com/reference/css/">CSS</a>) are an <a href="/articles/style-sheets-vs-frames-as-web-extensions/"> elegantly designed extension</a> to the Web and one of the greatest hopes for recapturing the Web's ideal of <strong> separation of presentation and content</strong>. The Web is the ultimate cross-platform system, and your content will be presented on such a huge variety of devices that pages should specify the meaning of the information and leave presentation details to a merger (or "cascade") of site-specified style sheets and the user's preferences. If the introduction of <a href="http://www.nngroup.com/articles/webtv-usability-review/"> WebTV</a> broke your pages, you will appreciate the ability to introduce new page designs by creating a single style sheet file rather than by modifying thousands of content pages.</p>

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

<a class="ga-article-toc-item" href="#toc-centralized-style-1">Centralized Style</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-implementation-advice-2">Implementation Advice</a>

</li>

</ul>

</div>

</div><h2 id="toc-centralized-style-1">Centralized Style</h2>

<p>Use a <strong> single style sheet for all of the pages on your site </strong> (or possibly a few coordinated ones if you have pages with very different needs: for example technical documentation versus marketing pages). One of the main benefits of style sheets is to ensure visual continuity as the user navigates your site. Legacy publications have long known the value of basing print products on a single typeface: no matter where you turn in a magazine or a newspaper, the text and basic layout will look the same. Websites will gain the same brand cohesiveness if all the pages on a site link to the same style sheet.</p>

<p>Always use <strong> linked style sheets </strong> rather than embedded styles. Only by referencing an external file will you get the maintenance benefits of being able to update the look of your entire site with a single change. Also, by pulling style definitions out of your pages, you make them smaller and faster to download. If you use a single style sheet for your entire site, that file will be a single download once and for all.</p>

<p>For each site, all the style sheets should be designed by a single, central design group. Two reasons: First, <strong> centralized design </strong> is the only way to ensure a consistent style and reap one of the main benefits of style sheets. Second, the majority of Web content creators are not capable of designing and writing good style sheets. Experience with word processors that support style sheets indicates that <strong> most authors mangle their style sheets terribly</strong>. Understanding the effect of style is relatively easy in traditional desktop publishing because it is a WYSIWYG environment with a single, canonical output form. The <a href="http://www.nngroup.com/articles/the-difference-between-web-design-and-gui-design/"> Web is not WYSIWYG</a> because of the variability in supported platforms. Furthermore, Web stylesheets are cascading, meaning that the site's style sheet is merged with the user's style sheet to create the ultimate presentation. These differences make it important that Web style sheets are designed by a specialist who understands the many ways in which the result may look different than what is on his or her own screen.</p>

<p>Fund an <strong> active evangelism program </strong> to teach your content creators how to use the centrally defined style sheet. Do not assume that people understand the concept of style and how to apply it, simply because they know a word processor with style sheets. Research shows that <a href="http://www.ifi.uio.no/%7Epaalso/artikler/styles/new-version/pap.html"> most users make horrible mistakes in using word processing style sheets</a>: partly because the main word processors have particularly bad style sheet usability and partly because style is hard. Your style sheet should come with a small manual that explains the different styles and when and how to use them. Include <strong> plenty of examples</strong>, including both raw HTML code (cutting-and-pasting examples is the main way people use documentation) and screenshots of the appearance of correctly coded pages in several mainstream browsers on several different platforms. The screenshots should be made into clickable imagemaps, allowing users to click on an effect they want to achieve and get to the documentation for the appropriate styles. In particular, if multiple styles have similar appearance, many errors can be avoided by explaining the differences and when to use which style.</p>

<p>Despite my preference for linked style sheets and central design, individual <strong> page authors should be allowed to create additional embedded styles for their own pages </strong> when necessary. Authors should be encouraged to only do so when absolutely necessary, but there will always be cases where a certain style is needed that is not supplied in the central style sheet. If many pages need the same effect, it should be added to the site's global style sheet, but it would be bad to inflate the one linked style sheet with styles that are only needed once. Single-page styles should be embedded rather than linked: the page should continue to link in the global style sheet and then override it with local, embedded styles as necessary. Doing so has the benefit of allowing future changes to the central style sheet to propagate to the modified page to the greatest extent possible.</p>

<h2 id="toc-implementation-advice-2">Implementation Advice</h2>

<ul>

<li>Pages must <strong> continue to work when style sheets are disabled</strong>: for example, do not use tricks where the same words are repeated multiple times with small offsets to create shadow effects (without the intended style, the text turns into gibberish). Retaining a decent presentation without the style sheet is mandatory to support users with older browsers, <a href="http://www.nngroup.com/articles/accessible-design-for-users-with-disabilities/"> blind users</a>, and users who need to disable the style feature in their browser (either because of bugs or because your style conflicts too much with their preferences). Luckily, it is very easy to check conformance with this rule: simply disable style sheets in your browser and reload the page.</li>

<li><strong>Do not use more than two fonts </strong> (plus possibly a third for special text like <code> computer code </code> ). Remember the lesson from the early days of desktop publishing: using a lot of fonts simply because you <em> can </em> will result in a ransom-note look. Typically, you can use one typeface for body text and another, bolder, face for headings. Note that it is fine (indeed, recommended) to use a long list of alternate fonts in the style sheet specification for a given class of text: the user's browser will pick the first available font in the list and use it throughout your pages, meaning that the user will see a single font, making the site feel typographically unified. It is important that lists of font names have the fonts listed in the same order, since the browser picks the first one it has available.</li>

<li><strong>Do not use absolute font sizes</strong>; instead specify all text relative to the base font size defined by the user's preference setting. For example, large text could be defined as "200%", meaning that it would be set as 24 point if the user preferred 12 point for body text and 20 point if the user preferred 10 point for body text. Whether people prefer large or small fonts depends on a variety of questions, including the size and resolution of their monitors and the user's eyesight. It is somewhat annoying to visit a website where the text is too small for comfortable reading under my circumstances, but it is <em> very </em> annoying to click on the "make text bigger" button and have nothing happen because the font sizes were defined as an absolute number of points.</li>

<li><strong>Do not use the <code> !important </code> attribute </strong> to override the user's settings. It is hard to imagine cases where you are justified in ignoring the user's preferences if the user felt strongly enough to use his or her own <code> !important </code> rating, so <code> !important </code> should be reserved for user style sheets.</li>

<li>If you have multiple style sheets, then make sure to <strong> use the same CLASS names for the same concept in all of the style sheets</strong>. Content creators using two or more style sheets will be confused if different CLASSes are used for the same thing or if one style sheet has a CLASS that is missing in the other style sheet even though the concept applied in both cases. If, for example, you have a CLASS for the name of the author of a document, then all of your style sheets should have this CLASS, even though it may be defined to render differently, as appropriate for the different kinds of documents.</li>

</ul>

<p><a href="http://www.w3.org/Style/CSS/Buttons/"><img align="left" alt="CSS logo" border="0" height="31" loading="lazy" src="http://www.w3.org/Style/CSS/Buttons/mwcos" width="88"/> </a> Even though the CSS logo button is nice, I recommend that you restrain yourself and do not plaster it all over your site. In particular, do not put it on the home page. Users do not care how you implement your site (except if they follow a link to "about this site" - it would be great to put a CSS button on the "About" page). A firm rule for home page design is <strong> more is less </strong> : the <em> more </em> buttons and options you put on the home page, the <em> less </em> users are capable of quickly finding the information they need. (Because of this rule I am puzzled by the many home pages that feature download buttons for various browser vendors: why anybody would reduce the usability of their own site in order to give another company free advertising is beyond me.)</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="The Human Mind and Usability" href="/courses/human-mind/?lm=effective-use-of-style-sheets&amp;pt=article">

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

<a class="tile ga-article-related-course" data-course-title="Emerging Patterns in Interface Design" href="/courses/emerging-patterns-interface-design/?lm=effective-use-of-style-sheets&amp;pt=article">

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

<a class="tile ga-article-related-course" data-course-title="Web Page UX Design" href="/courses/web-page-design/?lm=effective-use-of-style-sheets&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">new technologies,Web Usability</span>

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