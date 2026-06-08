# When to Open Web-Based Applications in a New Window - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">3</span>

<div class="article-header">

<h1 class="article-h1">When to Open Web-Based Applications in a New Window</h1>

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

October 14, 1997

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">1997-10-14</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: When to Open Web-Based Applications in a New Window&amp;body=https://www.nngroup.com/articles/when-to-open-web-based-applications-in-a-new-window/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/when-to-open-web-based-applications-in-a-new-window/&amp;title=When to Open Web-Based Applications in a New Window&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/when-to-open-web-based-applications-in-a-new-window/&amp;text=When to Open Web-Based Applications in a New Window&amp;via=nngroup" data-share-type="Twitter">

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

Web-based applications can be divided into two rough categories:

</p>

<dl>

<dt>

<strong>

Functionality Apps

</strong>

</dt>

<dd>

Independent mini-applications in their own right with state transitions and multiple views (e.g., a tabbed dialog). Functionality applets often manipulate "real-world" data that exists separately from the webpage (e.g., allowing customers to manage their checking accounts, inventory control, server administration).

</dd>

<dt>

<strong>

Content Apps

</strong>

</dt>

<dd>

Tightly integrated with the content of a Web page. Examples include site navigation controls (e.g., an active sitemap, outline flippers to expand and contract a hierarchical listing), active content (e.g., a model of an engine that can be rotated, animated, and otherwise manipulated in place), and minor functions (e.g., a currency converter). Typically, running a content applet has no results other than changing the appearance of the current webpage.

</dd>

</dl>

<p>

Content applets should be displayed in a browser together with the Web page they belong to;

<strong>

functionality applets should display in a new, non-browser window

</strong>

without any Web navigation controls.

</p>

<p>

If functionality applets are displayed in a browser window, then users will invariably confuse applet interactions with browser interactions. Most seriously, users will frequently

<strong>

click the browser's

<code>

back

</code>

button when they want to undo an action in the applet or return to a prior state or view

</strong>

. Of course, going

<code>

back

</code>

in the browser takes the user to the previous

<em>

Web

</em>

page and kills the applet.

</p>

<p>

The problem is that the hypertext navigation metaphor is too strong as long as the user is within a browser window. Users simply cannot abstract away from using the browser's commands to navigate, even when they are "supposed" to navigate within the applet. The only solution is to open the applet in its own window without any browser controls. Once the applet appears in another window, users stop thinking "Web" and start interacting with the applet on its own terms.

</p>

<p>

In the long term, the solution to this problem is to eliminate browsers and move to a completely integrated navigation system that unifies navigation between system states and information objects and maintains a single navigation interface for all user actions, no matter whether they are on or off the Web. After all, users should not have to care whether they are dealing with HTML or another data type or whether they connect to the Internet, to an intranet, or to local content on their own harddisk.

</p>

<p>

Functionality applets may include hypertext

<strong>

links back to the Web

</strong>

. Typical examples include help pages and an airline reservation system that allows users to read more about different types of aircraft. Such hypertext links should take the user out of the functionality applet and back to the Web browser (while the functionality applet remains visible in its separate window).

</p>

<p>

Erika Kindlund from JavaSoft provides more detail about the design of a particular functionality applet: the administration interface for the Java Web Server. Her

<a class="old" href="/articles/navigating-the-applet-browser-divide/" title="Navigating the AppletBrowser Divide">

test data clearly shows the need to open functionality applications in a new window

</a>

. Server administration is clearly a "large" applet with its own navigation, and serious usability problems were found in an early design that kept the applet on the browser page.

</p>

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

<a class="ga-article-toc-item" href="#toc-other-applet-usability-issues-1">

Other Applet Usability Issues

</a>

</li>

</ul>

</div>

</div><h2 id="toc-other-applet-usability-issues-1">

Other Applet Usability Issues

</h2>

<p>

Most issues in applet usability are no different from

<a href="/articles/ten-usability-heuristics/">

traditional rules

</a>

for user interface design. A functionality applet that spawns its own window(s) should follow application design guidelines, and a content applet that stays on the page should follow Web design guidelines and principles for good information design.

</p>

<h3>

Progress Indicator Needed When Connecting Back to Server

</h3>

<p>

Applets that communicate back to the server should show a progress indicator while doing so. Progress indicators (often shown as

<strong>

percent-done bars

</strong>

) are necessary in any user interface for any operation that has slow

<a href="/articles/response-times-3-important-limits/">

response times

</a>

(more than 10 seconds). Applets that connect back to the server will often experience highly variable delays due to the weakness of the Internet. It is thus doubly important for the progress indicator to show the actual progress of the operation and its expected duration. For example, the progress indicator could show the proportion of a database that has been searched or the steps in a sequence that have been completed (while avoiding system-oriented terminology). Such progress indications may require a trickle of info from the server to the applet as it is servicing the request.

</p>

<p>

Applets should have a

<strong>

cancel button

</strong>

to allow the user to interrupt any slow operations. Interruptability is particularly needed for any server connections.

</p>

<h3>

Double-Click

</h3>

<p>

In principle, applets should follow current user interface standards, so there may unfortunately be cases where double-clicks need to be supported at this time. In the future, however,

<strong>

double-click must die

</strong>

since it causes novice users great difficulties and since it conflicts with the single-click interaction style of the Web. The main reason for double-click is to allow two operations to be overloaded onto a single-button mouse. Designers of more recent multi-button GUIs have faithfully duplicated a weaknesses that was made necessary by limitations of an early single-button GUI: let's do better in the future. Content applets should be particularly wary of double-click since people will think of them as single-click Web content. (Former Apple human evangelist Bruce Tognazzini provides further details about how newer window systems copied acknowledged weaknesses of the Mac: see his book

<a href="http://www.amazon.com/exec/obidos/ISBN=0201489171/useitcomusablein/">

Tog on Software Design

</a>

.)

</p>

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

<a class="tile ga-article-related-course" data-course-title="Application Design for Web and Desktop" href="/courses/application-ux/?lm=when-to-open-web-based-applications-in-a-new-window&amp;pt=article">

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