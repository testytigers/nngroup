# Slider Design: Rules of Thumb - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">3</span>

<div class="article-header">

<h1 class="article-h1">Slider Design: Rules of Thumb</h1>

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

September 13, 2015

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2015-09-13</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Slider Design: Rules of Thumb&amp;body=https://www.nngroup.com/articles/gui-slider-controls/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/gui-slider-controls/&amp;title=Slider Design: Rules of Thumb&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/gui-slider-controls/&amp;text=Slider Design: Rules of Thumb&amp;via=nngroup" data-share-type="Twitter">

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

</span>Selecting a precise value using a slider is a difficult task requiring good motor skills, even if the slider is well designed. If picking an exact value is important to the goal of the interface, choose an alternate UI element.

</div>

<div class="article-body">

<p>Sliders are often the UI control of choice for letting users select a value or range from a fixed set of options. However, in practice, <strong>sliders are difficult to manipulate</strong>. Especially on touch interfaces, the level of control needed to meticulously operate a slider to an exact value is simply not realistic.</p>

<blockquote>

<p><strong>Slider:</strong> A control element that uses a knob or lever moved horizontally to control a variable, such as volume on a radio or brightness on a screen.</p>

</blockquote>

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

<a class="ga-article-toc-item" href="#toc-imprecise-interactions-1">Imprecise Interactions</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-is-an-exact-value-necessary-2">Is an Exact Value Necessary?</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-think-about-the-thumb-3">Think About the Thumb</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-4">Conclusion</a>

</li>

</ul>

</div>

</div><h2 id="toc-imprecise-interactions-1">Imprecise Interactions</h2>

<p>When designing a usable UI we must consider the context in which the interface will be used. For mobile design in particular, users often hold their device in one hand while doing other activities—watching television, walking, or even driving. In such circumstances it can be daunting to tap and drag a control precisely to a particular spot. Sliders are subjected to the <strong>steering law</strong>, which describes the time needed to navigate through a tunnel—as you might guess, the longer and narrower the tunnel, the more time it takes to steer through it. (The steering law also applies to drop-down menus and <a href="/articles/horizontal-scrolling/">horizontal scrollbars</a>.) With mobile devices being, well, mobile, it is not surprising that we see many users accidentally nudge the slider off the value they were attempting to select <em>just </em>as they lift their finger off the screen.</p>

<figure class="caption"><img alt="Screenshot of Kayak iOS app filters" border="0" height="444" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/08/05/multiplesliders.png" width="250"/>

<figcaption><em>The Kayak app uses multiple sliders for filtering based on the time of flights. The </em>Depart<em> and </em>Arrive<em> sliders only allow whole hour values, but the </em>Duration<em> sliders force users to select a value down to the precise minute.</em></figcaption>

</figure>

<p>Another major consideration when designing a touch interface is the <a href="/topic/accessibility/">accessibility</a> of various UI elements. Think about how challenging it would be to interact with a slider control for users with motor difficulties. Would they be able to select a value even close to what they wanted? How much effort and how many tries would it take them? Many <a href="/articles/usability-for-senior-citizens/">older users have less steady hands</a> than younger users and would have similar difficulties performing precise gestures to manipulate small UI elements. Unless you want to render these users helpless, a slider control may not be the best choice.</p>

<h2 id="toc-is-an-exact-value-necessary-2">Is an Exact Value Necessary?</h2>

<p>Allowing the selection of a very specific value is often not necessary, nor very helpful, to the user.</p>

<p>Sliders work <strong>best when the specific value does not matter</strong> to the user, but an approximate value is good enough. Thus, Kayak may get away with using sliders for duration and arrival and departure hours, as most users will be fine with a departure time that is, say, midday, and won’t care to specify the exact moment of the departure. But whenever the exact value matters, sliders are not okay. For instance, if you had to enter quantities such as age or current weight or height within a form, a slider would not be appropriate.</p>

<p><strong>The wider or the denser the range selectable through a slider, the harder it is to select a precise value</strong>. The <em>Delectable</em> app asks users to rate wine on a 6-10 scale, accurate to a tenth of a point. Not only is the abnormal scale is confusing, but selecting the precise value (9.5 vs. 9.3, for instance) is quite a motor feat. One could perhaps argue that the user won’t mind rating the wine a 9.3 instead of a 9.5, since the values are in the same ballpark. But then, why bother with the tenths of a rating and not use a simpler 5-point scale instead?</p>

<figure class="caption"><img alt="Screenshots of product rating elements on Delectable iOS app and Amazon iOS app" border="0" height="446" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/08/05/ratingslidervsstars.png" width="510"/>

<figcaption><em>Left: The Delectable app uses a slider for assigning a very specific rating to a bottle of wine. Right: Amazon app uses the more common, and easier to select, tappable stars to assign a rating for a product.</em></figcaption>

</figure>

<figure class="caption"><img alt="Screenshot of Weightbot iOS app slider" border="0" height="434" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/08/05/toopreciseslider.png" width="300"/>

<figcaption><em>Weightbot, a weight-tracking app, commits a double error: (1) it uses a slider (that is an imprecise control) for something that needs to be indicated with precision (weight) and (1) the slider moves in very small increments (.1 lb). Plus, the value it starts with is random: if you weigh 120 or 210 lbs, good luck adjusting the slider!</em></figcaption>

</figure>

<h2 id="toc-think-about-the-thumb-3">Think About the Thumb</h2>

<p>In cases where the use of a slider may be appropriate, ensure that the visual design of the element does not hinder its usability. For touchscreens, consider where the user’s finger will be placed on the screen—and what areas of the screen will thus be covered—while manipulating the slider. While labels placed directly below the slider may work on desktop designs used with a mouse cursor, the same label placement does not work well for mobile devices and other touchscreen designs because the labels may be obscured by the users’ finger while they are interacting with the control.</p>

<figure class="caption"><img alt="Screenshots of filters on BrilliantEarth.com and AirBnB.com" border="0" height="446" loading="lazy" src="//s3.amazonaws.com/media.nngroup.com/media/editor/2015/08/05/sliderthumbs.png" width="510"/>

<figcaption><em>Left: The sliders on BrilliantEarth.com place the labels describing the slider increments below the slider track, where they will be obscured by the user’s thumb during the interaction. Right: AirBnB.com correctly displays the slider values above the UI element, so they would remain visible throughout use.</em></figcaption>

</figure>

<p>In order to remain visible during use, any labels describing the slider or its currently selected value must appear beside or above both thumbs involved: the thumb of the user, and the thumb of the slider (also known as the knob or elevator).</p>

<h2 id="toc-conclusion-4">Conclusion</h2>

<p>Use a slider only when the precise value won’t matter to the user, but rather only the approximate range. Make sure that the users can select that range correctly without having to struggle too much to hit a precise value. In addition, any slider labels must be displayed above or beside the slider, rather than below it, in order to remain visible while the user is selecting a value. Alternatively, consider a different UI element that allows users to tap or even type to specify their choice rather than relying on press-and-drag gestures.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Application Design for Web and Desktop" href="/courses/application-ux/?lm=gui-slider-controls&amp;pt=article">

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

<li>

<a class="tile ga-article-related-course" data-course-title="Designing Complex Apps for Specialized Domains" href="/courses/complex-apps-specialized-domains/?lm=gui-slider-controls&amp;pt=article">

<h4 class="title heading-small">Designing Complex Apps for Specialized Domains</h4>

<p id="designing-complex-apps-for-specialized-domains" class="description body-small">

Create and evaluate applications for advanced decision making, complicated workflows, and complex domains

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">direct manipulation,touch targets,Application Design,Mobile &amp; Tablet,Design Patterns,forms,ui elements,graphical user interfaces</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Application Design</span>

<a class="ga-article-related-topic" href="/topic/applications/">Application Design</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/mobile-and-tablet-design/">Mobile &amp; Tablet</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/design-patterns/">Design Patterns</a>

</li>

</ul>

</div>

</div>

</div>

</div>