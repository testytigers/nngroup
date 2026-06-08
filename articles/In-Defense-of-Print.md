# In Defense of Print - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">2</span>

<div class="article-header">

<h1 class="article-h1">In Defense of Print</h1>

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

January 31, 1996

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">1996-01-31</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: In Defense of Print&amp;body=https://www.nngroup.com/articles/in-defense-of-print/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/in-defense-of-print/&amp;title=In Defense of Print&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/in-defense-of-print/&amp;text=In Defense of Print&amp;via=nngroup" data-share-type="Twitter">

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

</span>Paper remains the optimal medium for some forms of writing, especially for long works like a book. It is an unfortunate fact that current computer screens lead to a reading speed that is approximately 25% slower than reading from paper. We have invented better screens and it is just a matter of time before reading from computers is as good as reading from paper, but for the time being we have to design our information for the actual screens in use around the world.

</div>

<div class="article-body">

<p>As an online publishing enthusiast, I sometimes get ridiculed for having written a traditional <a href="/books/multimedia-and-hypertext/"> printed book</a> about hypertext and the Internet. I don't feel apologetic about publishing something in print because paper remains the optimal medium for some forms of writing, especially for long works like a book.</p>

<p>It is an unfortunate fact that current computer screens lead to a reading speed that is approximately 25% slower than reading from paper. We <em> have </em> invented better screens and it is just a matter of time before reading from computers is as good as reading from paper, but for the time being we have to design our information for the actual screens in use around the world.</p>

<p>The reduced reading speed on computers can be compensated by good hypertext design that allows the user to read less information and to find it faster. A typical example is online help and documentation: because the information is right there on the computer, there is no need to spend time finding the hardcopy manual, and because of good search tools and hypertext links between related information, users can go directly to the one or two sections that contain the answer to their problem. After all, Nielsen's first law of computer documentation is that <strong> users don't read it</strong>. The second law is that if they read it anyway, it's because they are in deep trouble and need the answer to a specific problem. Thus, somebody reading a manual won't really <em> read </em> it cover-to-cover, so online presentation makes perfect sense.</p>

<p>Other types of information do require the user to read large amounts of text. A typical example would be the instructional materials to teach a programmer a new programming language. Users typically want to spend an extended period of time reading long texts and they prefer not having to sit at their screen while doing so. Thus, even when the reading speed problem gets solved, we may still find that people decide to print out long texts rather than read them on the screen.</p>

<p>In any case, our surveys have shown over and over again that users do like the ability to get long documents in hardcopy, which is why even online publishing systems need a print feature. The implication for web design is to provide printable versions of any long documents. Web browsers are slowly gaining decent print functionality, but one cannot rely on browser companies to produce well-crafted printouts since their main interest is online information. For example, Netscape and Internet Explorer both use the same typeface and font size for online viewing and printing, even though it is known to all typography specialists that the two media require different type.</p>

<p>My recommendation is to generate <strong>two version of long web documents</strong>: one that is optimized for <strong>online viewing </strong>(is chunked appropriately into many files and has plenty of hypertext links) and one that is optimized for <strong>printing </strong>(has good layout and is in one piece). The print file should probably be in formats like PostScript or PDF. It is extremely important to denote any such files as being for printouts only and always supplement them with links to the same content in HTML for online viewing by users who want to browse or search a small part of the document.</p>

<p>PostScript and <a href="http://www.nytimes.com/library/cyber/under/062597under-wayner.html"> Acrobat</a> files should <a href="/articles/pdf-unfit-for-human-consumption/"><strong> never </strong> be read online</a>. PostScript viewers are fine for checking out the structure of a document in order to determine whether to print it, but users should not be tricked into the painful experience of actually spending an extended period of time with online PostScript. We learned this lesson the hard way in one of my projects: The current release of Sun's AnswerBook documentation viewer displays PostScript windows of the same pages that are used in our printed manuals. The next version of the product will use an SGML-based content structure that allows for much nicer information presentation and searching.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Content Strategy and Governance" href="/courses/content-strategy/?lm=in-defense-of-print&amp;pt=article">

<h4 class="title heading-small">Content Strategy and Governance</h4>

<p id="content-strategy-and-governance" class="description body-small">

Techniques and tools for implementing an actionable content strategy

</p>

<div class="ux-specialties">

<div class="ux-specialty-item">

<svg width="16" height="16" viewBox="0 0 21 21" aria-hidden="true">

<use href="#icon-management" />

</svg>

<p class="ux-specialty ux-management">Management</p>

</div>

</div>

</a>

</li>

<li>

<a class="tile ga-article-related-course" data-course-title="Writing Compelling Digital Copy" href="/courses/writing/?lm=in-defense-of-print&amp;pt=article">

<h4 class="title heading-small">Writing Compelling Digital Copy</h4>

<p id="writing-compelling-digital-copy" class="description body-small">

Use UX writing to shape your content to meet your readers&#x27; needs

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

<a class="tile ga-article-related-course" data-course-title="Omnichannel Journeys and Customer Experience" href="/courses/cross-channel-user-experience/?lm=in-defense-of-print&amp;pt=article">

<h4 class="title heading-small">Omnichannel Journeys and Customer Experience</h4>

<p id="omnichannel-journeys-and-customer-experience" class="description body-small">

Create a seamless, cohesive cross-channel experience

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Content Strategy,Writing for the Web</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Content Strategy</span>

<a class="ga-article-related-topic" href="/topic/content-strategy/">Content Strategy</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/writing-web/">Writing for the Web</a>

</li>

</ul>

</div>

</div>

</div>

</div>