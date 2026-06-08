# Death of File Systems: Article by Jakob Nielsen - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">5</span>

<div class="article-header">

<h1 class="article-h1">The Death of File Systems</h1>

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

March 1, 1996

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">1996-03-01</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: The Death of File Systems&amp;body=https://www.nngroup.com/articles/file-death/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/file-death/&amp;title=The Death of File Systems&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/file-death/&amp;text=The Death of File Systems&amp;via=nngroup" data-share-type="Twitter">

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

</span>The file system has been a trusted part of most computers for many years, and will likely continue as such in operating systems for many more. However, several emerging trends in user interfaces indicate that the basic file-system model is inadequate to fully satisfy the needs of new users, despite the flexibility of the underlying code and data structures.

</div>

<div class="article-body">

<p><em>Originally published as: Nielsen, J. (1996). The impending demise of file systems. IEEE Software 13, 2 (March). </em></p>

<p>Relax, oh Nerdy Reader: I am not going to take away your beloved file-system APIs. Here I am talking about what the user <em> experiences, </em> not how we provide that experience. The file system has been a trusted part of most computers for many years, and will likely continue as such in operating systems for many more. However, several emerging trends in user interfaces indicate that the basic file-system model is inadequate to fully satisfy the needs of new users, despite the flexibility of the underlying code and data structures.</p>

<p>There is <strong> no need for users to know how their information is stored </strong> inside the guts of the computer. Indeed, the notion of a continuous file is itself an abstraction: It masks the fact that the information is normally stored on noncontiguous sectors of the hard disk. From a user perspective, current <strong> file systems are based on three assumptions</strong>:</p>

<ul>

<li>Information is partitioned into coherent and <strong> disjunct units</strong>, each of which is treated as a separate object (file). Users typically manipulate information using a file and are restricted to be "in" one file at a time.</li>

<li>Information objects are <strong> classified according to a single hierarchy</strong>: the subdirectory structure.</li>

<li>Each information object is given a single, semiunique <strong> name</strong>, which is fixed. This file name is the main way users access information inside the object.</li>

</ul>

<p>Window systems have made these assumptions less intolerable, but they still exist. Modern computing, particularly the Internet, is further undermining these assumptions in several ways.</p>

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

<a class="ga-article-toc-item" href="#toc-single-units-1">Single Units</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-single-trees-2">Single Trees</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-file-names-3">File Names</a>

</li>

</ul>

</div>

</div><h2 id="toc-single-units-1">Single Units</h2>

<p>Before the Internet, printed output supported a canonical representation of most information objects; the goal of computers was to deliver a <strong> WYSIWYG identity mapping </strong> between content and presentation. In modern user interfaces, information objects often have <strong> multiple presentations </strong> and units are combined in multiple ways for different users and tasks. For example, nomadic users might want to retrieve e-mail on PDAs or even by voice synthesis over the telephone. To allow this, the presentation must be significantly briefer than that for a large workstation screen.</p>

<p>On the Internet, a typical Web page consists of a text file and one or more image files that are not combined until the page is displayed by the browser. Even the atomic component objects may not always map to individual files. For example, an image may exist as both a GIF and a JPEG file; the version the server ships to the browser is determined by content negotiation.</p>

<p>Some ways to improve the Web user experience will complicate the issue further: the GIF and JPEG image "files" may not exist as such in the file system, but might be generated on demand from an underlying image representation with parameters such as compression, lossyness, and color-map depth determined dynamically by available bandwidth and other considerations. For example, if you download a Web page in your office using a direct Internet link, the pictures may arrive as large, beautiful, 24-bit color images. Should you download the same page at home using a slow modem, the page will arrive with small, coarse, black-and-white images.</p>

<h3>Off-Line Issues</h3>

<p>Even on stand-alone PCs, the file model is falling apart. Consider, for example, the task of installing a new application. A simple, file-based user interface would have you drag the application icon from the place it is stored to the place where it will be needed. These days, however, an application is rarely satisfied with a single file: typically, installation litters the system with numerous subsidiary files, preference and configuration files, initialization files, and so on down the laundry list -- all stored in obscure directories of little relevance to the average user.</p>

<p>Using the file system as a user interface to install and copy applications has caused users many painful hours. In response, vendors have provided special installer and uninstaller utilities with their software. This led to a profusion of installers and uninstallers -- and to inconsistency and extra work for the user trying to keep track of all the additional utilities.</p>

<h3>Unit To Units</h3>

<p>Not only does a single information unit often map to multiple files; it can also contain <strong> multiple information units that should be treated differently </strong> in the user interface. The e-mail inbox, for example, should definitely be treated as a multiplicity of message objects. On a Web page, it is sometimes useful for the HTML file to contain both the visible information shown to the user and other information that is used for other purposes. Our server, for example, has more than 20,000 Web pages, so we decided to add metainformation to each file -- the e-mail address of the person responsible for the file. For performance reasons, this information is stored as a comment field in the file itself, even though it is a separate information object. If I changed my email address because I moved to a different domain within the company, the user interface should allow me to update the e-mail address associated with all my Web pages with a single operation.</p>

<h2 id="toc-single-trees-2">Single Trees</h2>

<p>File systems are structured as <strong> strict hierarchies of directories </strong> and subdirectories. For users, however, the same information unit often has <strong> multiple classifications</strong>. A corporate logo might appear on several Web pages, and thus would belong to several page objects across the server hierarchy. I often produce presentations (implemented as a small set of files per presentation) with slides that include screen shots, Web pages, or other designs I work on. A specific image might thus be classified as part of the "AnswerBook" development project as well as the "Singapore keynote" presentation project. In either case, if I change one object, I want all occurrences of the object to change. This should be true even if I changed the look -- expanding a slide to 400 percent in one case, reducing it in another: it's still the same information even if presented with a different look. Remember, WYSIWYG is tired; enriched representation is wired.</p>

<p>Hypertext links are the classic case of breaking up file hierarchies. Indeed, the very name comes from the fact that they form an n-dimensional hyperspace. Users are notoriously incapable of understanding large hierarchies, which is why cross-references and other hypertext links are so useful on the Web. Anybody who has tried to find something in the Yellow Pages knows how difficult it is to navigate somebody else's classification structure. If you want to buy a steak, do you look under B for butchers? No. How about S for steaks? Not quite. Try M for meat, retail. Butcher's supplies, however, <em> are </em> under B! (Your Yellow Pages directory may use a different classification. Indeed, that there is no single classification scheme in the real world is a further example of the problem.)</p>

<h2 id="toc-file-names-3">File Names</h2>

<p>Currently, files are represented in the user interface by their name and a few additional attributes (mainly data types illustrated by icons). File names are problematic user-interface primitives for several reasons. First, <strong> users rarely generate good file names</strong>, even in systems that allow long ones. In general, users don't like to type, have limited creativity in thinking up good names, and are hit by what I call the "premature classification problem": the name normally has to be generated long before the content is created, and thus users may not fully understand what they're naming. Second, users often have <strong> difficulty recognizing a name and remembering </strong> what it stands for, especially when many similar names are in use. Finally, when numerous information objects are in use, users sometimes have to type a name rather than simply recognizing it from a list. Not only is name-typing error prone, but users often don't remember the exact name and directory path they need to retrieve a certain information object.</p>

<p>In addition to these practical problems, <strong> named references are fundamentally unsuitable </strong> for accessing information in a system laden with it. Users often don't know exactly what they are looking for. They have no way of peeking inside a file without opening it up and paying the ensuing penalty in terms of performance and screen space. Hypertext links are fundamentally content-driven and context-sensitive: if well designed, they provide a preview of the content and get users to it without revealing where or how it is stored. URLs, on the other hand, are poorly designed file names.</p>

<p>The technology needed to create more flexible information interfaces will certainly include object-storage mechanisms and compound-document architectures, although exactly how they will be structured is not yet clear. What is clear is that we should stop presenting computer and network information storage as one icon per file and start visualizing the logical structure of the information.</p>

<p><em>See also later thoughts about similar UX issues: <a href="https://www.nngroup.com/articles/anti-mac-interface/">The Anti-Mac Interface</a> and <a href="https://www.nngroup.com/articles/alphabetical-sorting-must-mostly-die/">Alphabetical Sorting Must (Mostly) Die</a>.</em><br/>

</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Emerging Patterns in Interface Design" href="/courses/emerging-patterns-interface-design/?lm=file-death&amp;pt=article">

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