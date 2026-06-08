# Accessible Design for Users With Disabilities - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">6</span>

<div class="article-header">

<h1 class="article-h1">Accessible Design for Users With Disabilities</h1>

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

September 30, 1996

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">1996-09-30</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Accessible Design for Users With Disabilities&amp;body=https://www.nngroup.com/articles/accessible-design-for-users-with-disabilities/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/accessible-design-for-users-with-disabilities/&amp;title=Accessible Design for Users With Disabilities&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/accessible-design-for-users-with-disabilities/&amp;text=Accessible Design for Users With Disabilities&amp;via=nngroup" data-share-type="Twitter">

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

</span>How to design websites for universal access, including users with visual, auditory, motor, and cognitive disabilities. Using good ALT-text only gets you so far.

</div>

<div class="article-body">

<p><em><strong><em>Note:</em></strong><em> This article was written in 1996, and our understanding of accessibility has evolved significantly since then. We preserve this article as a reflection of our journey and growth in this field, so please read it within its historical context. </em><em>For updated guidance, visit <a href="https://www.nngroup.com/articles/accessibility-inclusivity-study-guide/">our study guide on accessibility and inclusivity.</a></em></em></p>

<p> </p>

<p>Making the Web more accessible for users with various disabilities is to a great extent a matter of using HTML the way it was intended: to encode <em> meaning </em> rather than <em> appearance</em>. As long as a page is coded for meaning, it is possible for alternative browsers to present that meaning in ways that are optimized for the abilities of individual users and thus facilitate the use of the Web by disabled users.</p>

<p>Before discussing the difficulties disabled users may have in accessing Web information, we should note that online information provides many benefits compared with printed information: it is easy for people with poor eyesight to increase the font size, and text-to-speech conversion for blind users works much better for online text than for print. Indeed, many disabled users are empowered by computers to perform tasks that would have been difficult for them with traditional technology. For an example, see a <a href="http://www.nytimes.com/library/cyber/week/0528blind.html"> <cite> New York Times </cite> article about one of their blind subscribers</a> who now reads the newspaper by going to the Website in Lynx. You can even hear how the article sounds through a screen reader - note how reading is done at <em> very </em> high speed (access to the <cite> Times </cite> site requires registration).</p>

<p>The Web Accessibility Initiative has published <a href="https://www.w3.org/WAI/tips/">guidelines for accessible Web design</a>. I refer you to these guidelines for more detail and will focus on broader issues in this column.</p>

<p><img alt="Web Access Symbol (for people with disabilities)" height="131" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/access2.0.gif" width="141"/><br/>

<em>The Web Access Symbol (for people with disabilities)<br/>

from the National Center for Accessible Media</em><br/>

This symbol can be used to signify sites or pages for which an effort has been made to enhance access for disabled users.</p>

<h2>Visual Disabilities</h2>

<p>The most serious accessibility problems given the current state of the Web probably relate to blind users and users with other visual disabilities since most Web pages are highly visual. For example, it is quite common to see combinations of background and foreground colors that make pages virtually unreadable for colorblind users.</p>

<p>Textual pages are reasonably easy to access for blind users since the text can be fed to a screen reader. Long pages are problematic since it is harder for a blind user to scan for interesting parts than it is for a sighted user. In order to facilitate scanning it is recommended to emphasize the structure of the page by proper HTML markup: use &lt;H1&gt; for the highest level heading, &lt;H2&gt; for the main parts of the information within the &lt;H1&gt;s, and &lt;H3&gt; and lower levels for even finer divisions of the information. By doing so, the blind user can get an overview of the structure of a page by having the &lt;H1&gt;s and &lt;H2&gt;s read aloud and can quickly skip an uninteresting section by instructing the screen reader to jump to the next lower-level heading.</p>

<p>Most people already know about the use of <strong> ALT attributes </strong> to provide alternative text for images, though there are still many Web pages without ALTs. Some accessibility specialists advocate so-called described images, where text is provided to verbalize what a seeing user would see. For example, the Web Access Symbol shown above might be described as "a glowing globe with a keyhole." In my opinion, such literal descriptions are fairly useless for Web pages unless the user is an art critic. I much prefer <strong> utility descriptions </strong> that verbalize the <em> meaning </em> or <em> role </em> of the image in the dialogue: what is the image intended to communicate and what will happen if it is clicked?</p>

<p>All <strong> imagemaps </strong> should be client-side and should use ALT attributes for each of the link options so that a user who cannot see the image can have descriptions of the destination read as he or she moves the cursor around. There are still some browsers that only support server-side imagemaps, but client-side imagemaps are clearly the way to go in the future. Sighted users would also benefit from having ALT attributes displayed in the appropriate parts of the picture rectangle if they didn't want to wait for the image file to download, and it is rather obvious that an ALT attribute can describe the meaning of the hyperlink destination in much more user-friendly terms than a weird URL. In general, it is often the case that design rules that may have been intended to help users with disabilities end up being of benefit to all users.</p>

<p>In addition to completely blind users, there are many users who can see but have reduced eyesight. These users typically need large fonts which is a standard feature of most Web browsers. To support these users, <strong> never encode information with absolute font sizes </strong> but use relative sizes instead. For example, when using Style Sheets, do not set the <code> font-size </code> attribute to a number of points or pixels but set it to a percentage of the default font size. By doing so, your text will grow or shrink as the user issues "text larger" or "text smaller" commands and the initial appearance of the page will match the user's preferences.</p>

<p>Full support of users with reduced eyesight would require pages to look equally well at all font sizes. Doing so is often not practical, and it might be acceptable to make pages look slightly worse at huge font sizes as long as the basic page layout will still work. It is recommended to test pages with the default font set to 10, 12, and 14 point to ensure that the design is optimal for these common font sizes and then to make additional checks with default fonts of 18 and 24 points to make sure that the design still works at these accessibility-enhancing sizes.</p>

<h2>Auditory Disabilities</h2>

<p>People who are deaf or have other auditory disabilities rarely have problems on the Web since sound effects are usually totally gratuitous. The usability of a site almost always stays the same when the sound is turned off. With the trend toward more multimedia this is not going to remain the case, though. In particular, transcripts should be made available of spoken audioclips and videos should be made available in versions with subtitles (which will also benefit users who are not native speakers of the language used in the video).</p>

<h2>Motor Disabilities</h2>

<p>Many users have difficulty with detailed mouse movements and may also have problems holding down multiple keyboard keys simultaneously. Most of these issues should be taken care of by improved browser design and should not concern content designers except for the advice not to design imagemaps that require extremely precise mouse positioning. Client-side imagemaps will work even for users who cannot use a mouse at all: the browser should be able to move through the links under keyboard control.</p>

<h2>Cognitive Disabilities</h2>

<p>By cognitive disabilities, I do not refer to below-average intelligence, though many sites will have to support such users as broader segments of the population go online. Currently, the Internet is so difficult to use that users need to be fairly intelligent to figure it out, but even these smart users sometimes have cognitive disabilities. Unfortunately, cognitive disabilities have not been the focus of as much user interface research as physical disabilities, so I only have a few examples.</p>

<p>People vary in their spatial reasoning skills and in their short-term memory capacity. Programmers and graphic designers tend to get uncommonly high scores on tests of spatial reasoning skills and are therefore good at visualizing the structure of a Web site. Similarly, young people (i.e., most Web designers) certainly have better memories for obscure codes (e.g., a URL) than older people. It is safe to assume that most users will have significantly greater difficulty navigating a Web site than its designers have. Simplified navigation helps <em> all </em> users, but is a required enabler for users at the opposite extreme of the scales. People who have difficulty visualizing the structure of an information can be helped if the site designers have produced such a visualization for them in the form of a sitemap; they would be further aided if the browser updated the display of the sitemap with the path of the navigation and the location of the current page.</p>

<p>Users with dyslexia may have problems reading long pages and will be helped if the design facilitates scanability by proper use of headings as noted above. Selecting words with high information content as hypertext anchors will help these users, as well as blind users, scan for interesting links (no "click here", please).</p>

<p>Most <strong> search </strong> user interfaces require the user to type in keywords as search terms. Users with spelling disabilities (and foreign-language users) will obviously often fail to find what they need as long as perfect spellings are required. A first suggestion is to for search engines to include a spelling checker; other ideas from advanced information retrieval like query-by-example and similarity search can also help these users (and benefit everybody else at the same time).</p>

<p>A final note: I realize that my own pages do not follow every last guideline. I have a very pragmatic approach to usability and may cut a corner in order to meet deadlines or satisfy other design trade-offs. There is a great difference between less-than-perfect design and completely reckless design, though.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Accessibility</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Accessibility</span>

<a class="ga-article-related-topic" href="/topic/accessibility/">Accessibility</a>

</li>

</ul>

</div>

</div>

</div>

</div>