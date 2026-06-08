# Reviving Advanced Hypertext - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">8</span>

<div class="article-header">

<h1 class="article-h1">Reviving Advanced Hypertext</h1>

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

January 2, 2005

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2005-01-02</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Reviving Advanced Hypertext&amp;body=https://www.nngroup.com/articles/reviving-advanced-hypertext/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/reviving-advanced-hypertext/&amp;title=Reviving Advanced Hypertext&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/reviving-advanced-hypertext/&amp;text=Reviving Advanced Hypertext&amp;via=nngroup" data-share-type="Twitter">

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

</span>To manage a huge, worldwide information space, users need proven features like fat links, typed links, integrated search and browsing, overview maps, big-screen designs, and physical hypertext.

</div>

<div class="article-body">

<p>Tim Berners-Lee's genius in inventing the Web in 1991 was to strip the hypertext concept to the bone and design a system with minimal features that worked across the Internet.</p>

<p>The Web really has only one feature: <strong> uni-directional plain links </strong> that replace the existing page with a new one. Yes, the feature has twists, such as the ability to go back or open the link in a new window (which I <a class="old" href="/articles/the-top-ten-web-design-mistakes-of-1999" title="Alertbox: top ten Web design mistakes of 1999"> recommend against </a> ), but fundamentally, the Web has no advanced hypertext capabilities.</p>

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

<a class="ga-article-toc-item" href="#toc-new-web-features-1">New Web Features</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-any-hope-2">Any Hope?</a>

</li>

</ul>

</div>

</div><h2 id="toc-new-web-features-1">New Web Features</h2>

<p>Since the first hypertext systems in the 1960s, many more features have been invented and several turned out to be useful. Maybe it's time to implement some of these features for the Web.</p>

<h3>Fat Links</h3>

<p>Fat links are links that point to more than one page. Now that browsers like Firefox and Safari support<strong> <a href="/articles/multi-tab-page-parking/">tabbed browsing</a></strong>, it's possible to have a link that opens up multiple tabs, and thus lets users access several destinations in one click.</p>

<p>Although many users like tabs, I'm personally less enamored of them, possibly because I use a fairly large screen (2048 x 1536 pixels). With a big screen, it's usually better to manage multiple pages in windows rather than in tabs. Taskbar usability improves because you can see more of the window title in the buttons on the bottom of the screen. Also, a big screen lets you display multiple Web pages simultaneously, which dramatically improves the usability of critical tasks like <a class="old" href="/articles/the-3cs-of-critical-web-use-collect-compare-choose" title="Alertbox: The 3Cs of Critical Web Use: Collect, Compare, Choose"> collect, compare, and choose</a>. Still, tabs do have their advantages, and in any case, they're only one possible implementation of fat links.</p>

<p>(Note: Bookmarks are a special kind of link; Firefox's ability to open all of a folder's bookmarks at once is thus a <strong> fat bookmark</strong>.)</p>

<h3>Typed Links</h3>

<p>If the user interface formally recognized different link types, it could <strong> display and manage them differently</strong>. The most obvious type distinction is between a website's internal links and links that point to other sites.</p>

<p>Browsers could implement this distinction today by simply looking at the domain name in the URL: if you're displaying a page from foobar.com, links to foobar.com pages are internal and all others are external. A slightly more advanced system might recognize the possibility of a given company owning multiple domains.</p>

<p>Many website designers have attempted to design icons that <strong> notify users about links to external sites</strong>, but these attempts usually fail because the designs are non-standard. <a href="https://www.nngroup.com/videos/jakobs-law-internet-ux/" title="Jakob's Law of Internet UX (2 min. video w. Jakob Nielsen)">Jakob's Law states that users spend most of their time on <em> other </em> sites</a> and form their expectations based on their aggregated user experience. Thus, unless all sites have the same icons (and use them consistently), it's a doomed endeavor to visualize link typing with icons, rather than to embed types at a deeper system level.</p>

<p>Of course, typed links could have many uses beyond the simple internal/external distinction. For example, browsers could treat destinations that require micropayment or registration differently than free links. Similarly, they could distinguish between links to arguments that support or refute a position.</p>

<h3>Explicit Structure</h3>

<p>Instead of treating atomic links and pages as the UI's only concepts, we could add an explicit representation of the information architecture. Opera already does this, giving users buttons to go to a site's home page, help system, category listings, and so on.</p>

<p>The benefit of explicit structural commands is that they <strong> free users from slavery to individual site designs</strong>. Users need no longer suffer under bad sites. And, even on good sites, they can simply use a standard command that's always the same rather than spend time trying to comprehend each sites navigation. That's a primary reason for the <em> Back </em> button's popularity: it lets you avoid searching the page for a link that might accomplish the same thing.</p>

<h3>User-Constructed Structure</h3>

<p>A particularly interesting form of structural UI is any structure that's built by the user and added on top of existing hypertext. Annotations and guided tours are two examples.</p>

<ul>

<li><strong>Annotations </strong> superimpose user-generated content, such as text, doodles, or links to other sites. This structure has many uses, including simply letting you post reminders to yourself about your last experience with a site.</li>

<li><strong>Guided tours </strong> let you collect a series of pages and subsites and combine them with additional material into a new structure that you can communicate to others. This is great for e-learning applications, but also has more pragmatic uses. For example, you might research a business purchase and send your boss a guided tour with the pros and cons of different options.</li>

</ul>

<h3>Integrated Search and Browsing</h3>

<p>Search is one of the main ways people access the Web, and it has the huge benefit of letting them explicitly state what they want during each visit. Unfortunately, users leave all information about their current queries behind as soon as they start browsing from the SERP (search engine results page).</p>

<p>In 1990, Bell Communications Research's SuperBook project proved the benefits of integrating search results with navigation menus and other information space overviews. There are three basic approaches to this. The first is simply to <strong> annotate each navigation label with the number of search hits </strong> in the area it points to.</p>

<p>A second, more advanced approach would use an indication of <strong> aggregated search relevance</strong>. A site might, for example, emphasize an area containing one extremely relevant page over an area with ten less relevant pages. In any case, the key is to give users a prospective view of the extent to which different navigation options relate to the current query.</p>

<p>Also, once users arrive at a page, it's beneficial to <strong> highlight query terms</strong>. Doing so makes it easy for users to judge why the page was deemed relevant, and thus easier to decide whether to stay or leave. Highlighting query terms also helps users narrow their attention to the most relevant part of the page.</p>

<p>A third approach to integrating search and browsing is to <strong> display higher-value advertising</strong>. If the site knows the user's most recent query, it can display ads related to those keywords instead of more generic ads. Of course, ads on content pages will never be as successful as the same ads on a SERP, because the user's behavior has changed from seeking to reading. While on the search engine, users are looking for someplace else to go, and thus are very likely to click on any ad that promises to solve the problem inherent in the current query. On a content page, that same ad conflicts with the user's goal to process the information and possibly return to the search engine to select the next destination. Still, an ad that's relevant to the user's current problem (as indicated by recent query terms) should beat advertising chosen with less situational awareness.</p>

<p>Placing search ads on content pages should particularly benefit players — like Yahoo! and MSN — that combine search engines with networks of other services. Such sites can directly transfer their knowledge of user queries to the non-search parts of their network. Other sites might extract the user query terms from the referrer information that's usually received when visitors arrive from search engines. Or, search engines might stop passing along the current query string and start selling it as a separate data stream to destination sites.</p>

<p>(Once we start transferring keyword relevance to post-SERP behavior, it will be interesting to measure how fast the user's intent diverges and thus how fast the value of targeting the previous intent decays. I would not be surprised if the keywords' value evaporated within five minutes. Web users are fickle.)</p>

<h3>Overview Maps</h3>

<p>In several studies of pre-Web hypertexts, having an overview map of the information space improved users' performance between 12% and 41%. Knowing where you are, where you've been, and where you can go is a significant help in navigating online information.</p>

<p><strong>Navigation menus </strong> and <strong> site maps </strong> are two common approximations of overview maps, but neither provides the full set of features that users need. Due to space constraints, navigation menus show only a limited view of users' options. Site maps don't highlight current location, partly because users must leave their current location to access the site map as a separate pageview.</p>

<p>Certainly, it would help if designers followed the <a class="old" href="http://www.nngroup.com/reports/sitemaps/" title="Nielsen Norman Group report: Site Map Usability: 28 design guidelines based on usability studies with people using site maps"> twenty-eight design guidelines for site map usability</a>. But ultimately, designers must integrate overview diagrams with the browser to support three core features:</p>

<ul>

<li><a href="/articles/navigation-you-are-here/"><strong>You-are-here </strong> markers</a>.</li>

<li><strong>Footprints </strong> showing where the user has been. Sites that <a class="old" href="/articles/change-the-color-of-visited-links" title="Alertbox: Change the Color of Visited Links"> change the color of visited links</a> partly offer this feature, assuming their site maps use textual links. But even these sites don't provide two essential elements of footprints:

<ul>

<li>Marking areas that the user has visited (even if the user hasn't been on the area's main page and thus hasn't seen the link's specific URL).</li>

<li>Using differential markings that indicate the extent of the user's visit to an area (did you see all the pages in a subsite or only a few of them?).</li>

</ul>

</li>

<li><strong>Search hit density </strong> markers, as discussed under "Integrating Search and Browsing."</li>

</ul>

<h3>Big-Screen Design</h3>

<p>In principle, the Web is independent of screen size. But in practice, the Web is designed for a small-screen user experience, in which users view one page at a time at a narrow width (typically 800 or 1024 pixels). Scrolling is the main way users access information that can't be displayed on a small screen.</p>

<p>Once we get screens the size and resolution of a broadsheet newspaper, the user interface will change. It will become possible to rely more on spatial hypertext and less on linear scrolling. In fact, the very concept of a page may vanish and be replaced by higher-level aggregate units that combine multiple data feeds.</p>

<p>The prevalence of <a class="old" href="http://www.nngroup.com/reports/intranet/portals/" title="Nielsen Norman Group report: Usability of Intranet Portals, Report from the Trenches"> portlets on intranet portals </a> is a weak precursor to the potential for integrating multiple information units that can be independently activated and updated.</p>

<h3>Physical Hypertext</h3>

<p>Rather than click underlined words on a screen, it's possible for users to retrieve a destination page through some real-world action. Physical objects can be the anchor points for a hypertext link.</p>

<p>Several doomed projects have tried to implement physical hypertext on the Web. The most prominent and clueless was CueCat: a barcode scanner that let users scan magazine ads to display more information about advertised products.</p>

<p>CueCat failed for two reasons:</p>

<ul>

<li><strong>It benefited advertisers, not users</strong>, so people had little incentive for keeping a CueCat around for those rare occasions when they wanted follow-up info on an ad. Typing in a URL is easier than digging out a special hardware device.</li>

<li><strong>It was tied to the PC</strong>, so it didn't help people when they were shopping or otherwise might want information but didn't have PC-based Web access.</li>

</ul>

<p>Future projects for physical hypertext must overcome these two downsides. It will be easy to embed barcode scanners and RFID readers in mobile phones and other PDAs with Internet capability. Such devices will let users link off physical objects they encounter when they're out and about. Where should the links lead? Not just to ads, but also to other useful information, such as review sites or comparison-shopping sites that tell users whether they're getting a good deal.</p>

<h3>Collaboration</h3>

<p>Browsing is a solitary experience. Life isn't.</p>

<p>I mention collaboration as my last feature, because it's the one for which old research provides the least guidance. There's some work on shared hypertexts, where people build up a collaborative knowledge base and/or solve other problems together. Wikis offer a primitive example of the power of multi-user hypertext. But mainly, collaboration remains a field with immense promise and little progress.</p>

<h2 id="toc-any-hope-2">Any Hope?</h2>

<p><a class="old" href="http://www.useit.com/alertbox/newfeatures.html" title="Alertbox sidebar: Features Missing in Current Web Browsers (as of 1995)">In 1995, I listed fifteen hypertext features </a> that were missing from Web browsers. None of these ideas have been implemented in the ten years since, except for Firefox's search box and Internet Explorer's search sidebar.</p>

<p>Is there any hope that the next decade will bring more progress? I think so. For one, most of the ideas mentioned here are rich sources of user interface patents, which offer a sustainable competitive advantage. (I invented at least five potential patents while writing this article, but didn't bother filing because I'm not in the business of suing infringers; a big company could rack up the patents if so inclined.)</p>

<p>The last ten years were a black hole: much attention was focused on doomed attempts at making the Web more like television. Hopefully, the next decade will focus instead on empowering users and giving us the features we need to master a worldwide information space.</p>

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