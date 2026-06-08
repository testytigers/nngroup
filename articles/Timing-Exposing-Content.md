# Timing Guidelines for Exposing Hidden Content - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">6</span>

<div class="article-header">

<h1 class="article-h1">Timing Guidelines for Exposing Hidden Content</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Aurora Harley</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/Aurora-Harley-20190601SF.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list"><a class="ga-article-author" href="/articles/author/aurora-harley/">

Aurora Harley</a></span>

<p class="publication-date">

January 11, 2015

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2015-01-11</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Timing Guidelines for Exposing Hidden Content&amp;body=https://www.nngroup.com/articles/timing-exposing-content/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/timing-exposing-content/&amp;title=Timing Guidelines for Exposing Hidden Content&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/timing-exposing-content/&amp;text=Timing Guidelines for Exposing Hidden Content&amp;via=nngroup" data-share-type="Twitter">

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

</span>Events triggered via hover or click require distinct timing to avoid accidental activations and ensure that the user feels in control of the interface.

</div>

<div class="article-body">

<p>Hiding content and navigational elements on web pages is an increasing trend, fueled in part by the goal of displaying minimal content and the constraints of <a href="/articles/scaling-user-interfaces/">producing a single design for mobile and desktop</a>. While it is a good practice to <a href="/articles/defer-secondary-content-for-mobile/">defer secondary content</a> (at least on mobile) and <a href="/articles/minimize-cognitive-load/">limit visual clutter in order to minimize cognitive load</a>, it is just as important—if not more so—to ensure that any hidden content appears only once it is certain that the user <em>intends</em> to expose it.</p>

<p>In this article we won’t discuss whether it’s appropriate to hide something in the first place. Neither will we cover whether the design communicates clearly the affordance to unhide the hidden stuff. Here, we focus purely on the mechanics of how this unhiding happens.</p>

<p>(Note: because we're analyzing <a href="/articles/powers-of-10-time-scales-in-ux/">time-dependent user experience</a> phenomena, the illustrations are video clips. Depending on which browser you use, you may have to hover over the still images to expose the video player controls.)</p>

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

<a class="ga-article-toc-item" href="#toc-examples-of-hidden-content-1">Examples of Hidden Content</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-recognizing-intent-2">Recognizing Intent</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-timing-guidelines-3">Timing Guidelines</a>

</li>

</ul>

</div>

</div><h2 id="toc-examples-of-hidden-content-1">Examples of Hidden Content</h2>

<p>The most common example of hidden page content is the mega menu. The mega menu also best illustrates the common problem of hidden content: it often acts as if it had a mind of its own, and “decides” to appear or disappear inappropriately and unexpectedly. There is currently no web standard that dictates how a hidden submenu should be exposed. Thus, users are forced to experiment with hover versus click during their first experience with a site. If the menu is implemented well, this fleeting question does not pose a serious usability issue. Problems arise once the mega menu opens unintentionally (from the user’s perspective) upon hover, when the user merely glides the mouse across the triggering item, in the attempt to get to another area of page content.</p>

<figure>

<video controls="" poster="https://s3.amazonaws.com/media.nngroup.com/media/editor/2014/12/04/chairish_hoverMegaMenu_closed.png" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2014/12/04/Chairish_UnintentionalTrigger.mp4" style="border:1px solid #000;" width="100%">Your browser does not support the video tag.</video>

<figcaption><em>The drop-down mega menu on the Chairish website opens immediately upon hover, even when the mouse is merely passing over the main-menu item without stopping. The exposed menu is so large that it can cover the entire banner area on the homepage. This can cause strain on those users attempting to move the cursor from the header area of the site toward the hero banner (for instance, because they have just used the browser’s URL bar or buttons and now they want to move down to click the main call to action). These users must now work harder to collapse the menu and get to the content that they need.</em></figcaption>

</figure>

<p>Tooltips, expanding ads, and calls to action or information boxes that appear over list items (such as quick-view boxes on thumbnails from product-listing pages) are other examples of common elements with hover interactions that can prove annoying to users if triggered too sensitively.</p>

<h2 id="toc-recognizing-intent-2">Recognizing Intent</h2>

<p>How can designers know for sure that the user really wants to expose the hidden content?</p>

<p>The clearest indication of intent to expose hidden content (or really, to take any action) is a click or tap on an element. Elements relying on hover to trigger events, in contrast, require more consideration when determining user intent. <strong>Revealing hidden content <a href="/articles/too-fast-ux/">too quickly</a> on mouseover can result in accidental activations</strong> and creates a jarring user experience. On the other hand, when users do intend to expose hidden content, <strong>revealing content too slowly makes the system appear sluggish</strong>, and can make people lose patience and abandon the site. Additionally, due to the <a href="/articles/response-times-3-important-limits/">slow response time</a> and lack of immediate feedback, users may assume that the element does not actually trigger anything. Users are like Goldilocks: in hover interactions they expect the timing to be <em>just right</em>.</p>

<p>For hover interactions, the best cue for determining user intent is that the <strong>user’s mouse actually stops on the element</strong> that will trigger the event. The longer the stop, the stronger the indication of intent. If the mouse cursor is still in motion, intent to activate hidden content cannot be assumed because the mouseover could be part of the cursor’s path to another element, or merely a motion made while consuming content. If the hidden content displaces or covers other elements on the page, designers need to be extra careful and require a longer mouse stop over the triggering element before exposing the hidden content. In other words, the more disruptive the content displayed, the more certain designers need to be of user’s intent before triggering the animation. (Note: the visual feedback that an element is interactive should be displayed immediately, however, even if the user does not pause the mouse on that element. That type of feedback ensures target discoverability, but it should not be intrusive and should not require any <a href="/articles/interaction-cost-definition/">interaction cost</a> to dismiss it.)</p>

<p>Some of the mouse-stop time can actually be absorbed by the animation itself: a longer transition animation that starts once the user moves the mouse on top of the triggering element but progresses relatively slowly and resets when the mouse leaves the target area can reduce the user frustration and disorientation. A successful, familiar example is the display of an alternate product image on a product-listing page: it’s not disruptive, it is initiated soon after the mouse moves on top of the target, yet it can take some time, and it stops if the mouse moves away quickly.</p>

<figure>

<video controls="" poster="//s3.amazonaws.com/media.nngroup.com/media/editor/2014/12/04/herschel_hoveralternateimage.png" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2014/12/04/Herschel_hoverAlternateImage.mp4" style="border:1px solid #000;" width="100%">Your browser does not support the video tag.</video>

<figcaption><em>When users hover over product images on a browse page of the Herschel website, an alternate image of the product is displayed. This alternate image replaces the default via a fade animation, which begins after the cursor has remained within the target area for a short period. While the animation does not necessarily wait until the cursor has completely stopped, the timing is long enough to determine intent when combined with the slow transition animation and does not cause user annoyance.</em></figcaption>

</figure>

<p>Once the content is exposed, if the mouse cursor leaves the target area of a hover-activated element, there should be a slight delay before hiding the content to ensure that the mouseout was intentional and the user does not intend to return to the content. Ignoring this recommendation leads to the <a href="/articles/mega-menus-work-well/">diagonal problem in mega menus</a>, when the path to content in the dropdown menu causes the cursor to leave the hover target area. In such situations, the continuous motion of the mouse and reentry into the active target area within a reasonable amount of time communicates the user’s intent to remain within the exposed content. Users should not be forced to stay within the lines. (Another solution would be to check whether the mouse remains within the triangular area from the starting mouse position and the top and bottom points of the submenu. Tog first invented this solution for Apple menus back in 1986, and discusses it in his <a href="http://www.asktog.com/columns/022DesignedToGiveFitts.html">Fitts' Law interaction design quiz</a>, in question 6. A breakdown of <a href="http://bjk5.com/post/44698559168/breaking-down-amazons-mega-dropdown">Amazon's use of this triangle principle written by Ben Kamens</a> is another good example of this solution in practice. This solution, focusing on cursor position and determining whether the mouse could feasibly be moving toward a related target, allows for longer time delays before closing a menu to account for those users who do not possess lightning-speed mouse skills.)</p>

<figure>

<video controls="" poster="//s3.amazonaws.com/media.nngroup.com/media/editor/2014/12/04/latimes_drawermenu.png" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2014/12/04/LATimes_DiagonalEffect.mp4" style="border:1px solid #000;" width="100%">Your browser does not support the video tag.</video>

<figcaption><em>The left navigation with drawer-style submenu on the LA Times website is a perfect example of the diagonal problem that can occur with hover-activated menus. When attempting to move the mouse cursor from the </em>Entertainment<em> top-level menu item to a subitem in the </em>Sections<em> menu, the path of the cursor momentarily leaves the target area of </em>Entertainment<em> and passes over </em>Sports<em>, which triggers the submenu to change to display the </em>Sports<em> subitems instead.</em></figcaption>

</figure>

<h2 id="toc-timing-guidelines-3">Timing Guidelines</h2>

<p>When exposing hidden elements on a web page, the speed of the animation must be fine-tuned so users feel in control of the interface. Visual feedback that an element is interactive (via a change in background color, text color, or style) must appear within <a href="/articles/website-response-times/">0.1 seconds to maintain the feeling of instantaneous response</a> and communicate to the user that the element will trigger some sort of event upon continued hover or click. Then, the user’s intent to expose any corresponding hidden content can be assumed either immediately upon click or tap, or after the mouse cursor paused movement and remained in the target area for around 0.3–0.5 seconds, at which time the hidden content can safely be animated onto the page. Only if the user has clicked or tapped outside of the target area, or the mouse cursor has left the target area and exposed content for longer than 0.5 seconds, can the intent to collapse the exposed content be determined.</p>

<p>For <strong>click and tap</strong> <strong>interactions</strong>, these timing guidelines are quite simple:</p>

<ol>

<li>On click or tap, display visual feedback and begin exposing hidden content within 0.1 seconds.</li>

<li>Keep displaying the exposed content until the user clicks or taps outside of the exposed content area.</li>

</ol>

<p>For <strong>hover interactions</strong>, the timing guidelines for speed of visual feedback and exposing hidden elements must be broken down into more steps:</p>

<ol>

<li>Mouse cursor enters target area: display visual feedback within 0.1 seconds.</li>

<li>Wait 0.3–0.5 seconds.</li>

<li>If cursor remains stopped within target area, display corresponding hidden content within 0.1 seconds.</li>

<li>Keep displaying the exposed content element until the cursor has left the triggering target area or the exposed content for longer than 0.5 seconds.</li>

</ol>

<p>A few hundred milliseconds may seem insignificant, but they are critical unless you plan on creating the next Minesweeper. If, instead, you aim for smooth hover interactions, getting the timing right to the tenth of a second can save users effort (and frustration) and create a frictionless user experience.</p>

<script>

$('video').on('click', function() {

ga('send', 'event', 'video', 'click', 'article-video');

});

</script>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Web Page UX Design" href="/courses/web-page-design/?lm=timing-exposing-content&amp;pt=article">

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

<li>

<a class="tile ga-article-related-course" data-course-title="The Human Mind and Usability" href="/courses/human-mind/?lm=timing-exposing-content&amp;pt=article">

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

</ul>

</div>

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">animation,Human Computer Interaction,Interaction Design,ui elements,Web Usability,response time</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Human Computer Interaction</span>

<a class="ga-article-related-topic" href="/topic/human-computer-interaction/">Human Computer Interaction</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/interaction-design/">Interaction Design</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/web-usability/">Web Usability</a>

</li>

</ul>

</div>

</div>

</div>

</div>