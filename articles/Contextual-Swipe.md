# Using Swipe to Trigger Contextual Actions - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">6</span>

<div class="article-header">

<h1 class="article-h1">Using Swipe to Trigger Contextual Actions</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Angie Li</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/IMG_2729_copy-square-close-800px.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list">

Angie Li

</span>

<p class="publication-date">

February 12, 2017

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2017-02-12</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Using Swipe to Trigger Contextual Actions&amp;body=https://www.nngroup.com/articles/contextual-swipe/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/contextual-swipe/&amp;title=Using Swipe to Trigger Contextual Actions&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/contextual-swipe/&amp;text=Using Swipe to Trigger Contextual Actions&amp;via=nngroup" data-share-type="Twitter">

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

</span>Implementations of swipe-to-delete or swipe to reveal contextual actions often suffer from usability problems.

</div>

<div class="article-body">

<p>While many touch gestures still get limited use in most mobile apps, one that has become fairly widely adopted is the swipe-to-delete, which simply involves dragging the finger across an item, in a gesture that resembles the physical action of crossing off a list item with a pen.</p>

<p>Initially introduced by Apple in the iOS Mail app, today many apps use it not only to remove an item from a list, but also to expose an entire set of contextual actions<a>.</a></p>

<p>While in the early iPhone years, this gesture was unfamiliar to the users, nowadays it’s so widely spread that many iOS and even Android users have learned it and use it frequently. Applications have embraced it as a convenient way to prioritize content and eliminate some <a href="/articles/browser-and-gui-chrome/">visible chrome</a> from the small mobile screen, and also to keep actions in line with the content that they affect. Yet, <strong>contextual swipe</strong> (the name we will use in this article for swipe-to-delete and its many relatives that trigger contextual actions) has questionable usability in many of its implementations.</p>

<figure class="caption"><img alt="" height="607" loading="lazy" src="https://media.nngroup.com/media/editor/2016/12/21/01-reminders.png" width="692"/>

<figcaption><em>In the iOS Reminders app, swiping towards the left on an item revealed the </em>More<em> and </em>Delete<em> buttons. Swiping right without choosing an action kept the item in the list.</em></figcaption>

</figure>

<p><strong>Disadvantages of Contextual Swipe</strong></p>

<p>Despite the growing number of applications that use this gesture, there are several reasons to take caution with contextual-swipe designs:</p>

<ol>

<li>

<p><strong>Lack of signifiers </strong>makes it unclear where the contextual swipe can be used. (This is a general problem for gesture-based interactions.) Although many users have become familiar with the gesture, some are still not used to it. And even those who have learned it may occasionally forget to perform it in the absence of any visible cues.<br/>

A complicating factor is that not all applications support this gesture, which <a href="/articles/power-law-learning/">slows down users’ learning</a>. When encountering new apps or revisiting infrequently used apps, users will have difficulty to predict if they can use contextual swipe.  For example, the Key Ring app for iPhone (an app for storing digitized loyalty cards) did nothing when an item was swiped, although widespread use of this technique may suggest otherwise.</p>

</li>

</ol>

<figure class="caption"><img alt="" height="623" loading="lazy" src="https://media.nngroup.com/media/editor/2016/12/21/02-keyring.PNG" width="350"/>

<figcaption><em>Swipe-to-delete was not available in the Key Ring app. In order to delete a card, the item had to be opened to reveal a detailed view.</em></figcaption>

</figure>

<ol>

<li value="2"><strong>Content is obscured</strong> when the user swipes to reveal actions. Although swiping is useful for keeping the actions close to the content they affect, swiping to reveal the menu often obscures the content beyond recognition. In the YouTube app, users had to swipe left to unsubscribe from a channel. However, swiping obscured the name of the channel and made it difficult to confirm that the right channel had been selected before taking action. Users wanting to avoid mistakes would need swipe right to reveal the full name of the channel before continuing.</li>

</ol>

<figure class="caption"><img alt="" height="623" loading="lazy" src="https://media.nngroup.com/media/editor/2016/12/21/03-youtube-unsubscribe.png" width="350"/>

<figcaption><em>In the iOS YouTube app swiping left on a channel revealed an </em>Unsubscribe<em> button, but also obscured the name of the channel that the user could unsubscribe from.</em></figcaption>

</figure>

<ol>

<li value="3"><strong>Some of the actions associated with contextual swipe are nonstandard. </strong>Because swipe was originally used to delete an item from a list, most users who have learned the gesture expect it to reveal some destructive actions. While many implementations do associate such actions with swipe (e.g., unsubscribe in the YouTube app), others reveal completely unexpected options. For instance, in the Spotify app, swiping left on a song that was not part of the user’s library revealed an option to save the song. (Pretty much the opposite action of deleting it.) This nonstandard behavior is problematic because users would not think to attempt swipe if they wanted to add a song to their library, since saving is not a destructive action.

<p>Some applications associate a plethora of actions with the swipe, delete included. Remember, most users won’t discover these actions (or they will discover them only accidentally when they attempt to delete the item).</p>

In the example below,  B&amp;H Photo app used swipe gestures to reveal multiple actions associated with the items in the shopping cart — not only <em>Remove </em>from cart, but also <em>Save for Later, Savings, </em>and <em>Accessories</em>.</li>

</ol>

<figure class="caption"><img alt="" height="623" loading="lazy" src="https://media.nngroup.com/media/editor/2016/12/21/04-bh-photo.png" width="350"/>

<figcaption><em>In the B&amp;H Photo app several actions were nested behind a swiping gesture. Keeping too many actions from view not only made it more difficult to see the affected content, but also made these features less discoverable.</em></figcaption>

</figure>

<p> </p>

<ol>

<li value="4"><strong>Contextual swipe is sometimes used inconsistently within the same app. </strong>Some apps expose different types of actions depending on either:</li>

</ol>

<ul style="margin-left: 40px;">

<li>the direction of the swipe (e.g., swipe left means something else than swipe right)</li>

<li>the state of the item being swiped</li>

</ul>

<p style="margin-left: 40px;">For example, in Spotify, swiping could have 3 meanings:</p>

<ul style="margin-left: 40px;">

<li>Swiping left on a song that was not part of the user’s library revealed a <em>Save</em> option (as discussed before).</li>

<li>Swiping left on a song in the user’s library revealed a <em>Remove </em>option.</li>

<li>Swiping right on a song revealed an option to add the song to a queue of music that was being played.</li>

</ul>

<p>When multiple actions are associated with the same gesture, it becomes harder for people to learn and remember them. (This is an instance of what psychologists call <em>the fan effect — </em>when a cue is associated with many items, it’s harder to retrieve any of those items.)</p>

<figure class="caption"><img alt="" height="607" loading="lazy" src="https://media.nngroup.com/media/editor/2016/12/21/05-spotify.png" width="692"/>

<figcaption><em>Spotify app for iPhone: the contextual swipe revealed multiple actions: swiping left on a song revealed a button to save the song to your personal music library. If the song was already in the library, then the identical gesture would cause a button for removing the song to be shown instead.</em></figcaption>

</figure>

<ol>

<li value="5"><strong>Poorly implemented swipe-to-delete can lead to loss of data</strong>. Swipe is a fairly easy-to-perform gesture, and every now and then people will accidentally <a href="/articles/slips/">remove an item unintendedly</a>.<br/>

To prevent such accidents, it’s important to always ask for confirmation or provide an easy way to undo the swipe.</li>

</ol>

<figure class="caption"><img alt="" height="623" loading="lazy" loop="infinite" src="https://media.nngroup.com/media/editor/2016/12/21/overcast-loop.gif" width="350"/>

<figcaption><em>Overcast app for iPhone: swiping alone would not delete a podcast. In order to remove a podcast, the </em>Delete<em> button needed to be selected, which prevented users from accidentally deleting items</em></figcaption>

</figure>

<ol>

<li value="6"><strong><a href="/articles/ios-7/">Swipe ambiguity</a> can affect how effective contextual swipe is. </strong>To make matters worse, some apps use horizontal swipe gestures not only for destructive actions, but also to navigate across different sections of the app. In many iOS apps, the horizontal swipe is used to go back to a previous page, and in Android it is sometimes used to reveal a hidden menu. Plus, on the iPad, horizontal swipe can be used to split the screen into multiple windows.

<p>All these gestures can affect the usability of contextual swipe. Imagine that you were trying to open up another application and accidentally deleted an important work email. Or, vice versa, imagine that you wanted to remove an item from a list and unintendedly triggered a split view.</p>

</li>

</ol>

<figure class="caption"><img alt="" height="519" loading="lazy" src="https://media.nngroup.com/media/editor/2016/12/21/07-ipad-pro-swipe.png" width="692"/>

<figcaption><em>iPad Pro: The Mail and Photos apps appeared in split-view mode on the screen at the same time. Swiping right on an email message in could mark the message as read or could close the panel containing the Mail app, depending on how close to the edge of this panel the swipe was executed.</em></figcaption>

</figure>

<p>Even if users can easily recover from such incidents, the overall user experience degrades as the user feels less in control over the interface.</p>

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

<a class="ga-article-toc-item" href="#toc-recommendations-for-using-contextual-swipe-1">Recommendations for Using Contextual Swipe</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-2">Conclusion</a>

</li>

</ul>

</div>

</div><h2 id="toc-recommendations-for-using-contextual-swipe-1"><strong>Recommendations for Using Contextual Swipe</strong></h2>

<ul>

<li><strong>Maximize content visibility </strong>and make sure that users know the item that they are deleting or acting upon. Contextual actions should be in view of the content it affects. Keep content in view anytime the contextual swipe is used in order to minimize uncertainty.</li>

</ul>

<figure class="caption"><img alt="" height="607" loading="lazy" src="https://media.nngroup.com/media/editor/2016/12/21/08.png" width="692"/>

<figcaption><em>Notability for iPhone (left): a contextual swipe kept the name of each ‘note’ aligned with the app border, allowing users to see what they were deleting. Wunderlist (right): The list title shifted off screen when users performed a contextual swipe, preventing them from checking the name of the list before acting on it.</em></figcaption>

</figure>

<ul>

<li><strong>Ask for confirmation </strong>before completing a destructive action.<br/>

Using contextual swipe to remove an item without confirmation can be problematic. Prevent mistakes and avoid errors by asking for confirmation with something as simple as a delete button.</li>

<li>Alternatively, if the action is highly repetitive and asking for confirmations would be tedious, <strong>support easy undo.</strong> Make sure that the undo option is highly salient on the screen, so people won’t have to look for it.<br/>

<br/>

In the YouTube app, after unsubscribing from a channel, users were provided the chance to undo or re-subscribe right away.</li>

</ul>

<figure class="caption"><img alt="" height="623" loading="lazy" src="https://media.nngroup.com/media/editor/2016/12/21/09-youtube.png" width="350"/>

<figcaption><em>After unsubscribing from a channel in the YouTube app there were multiple options to undo the action and re-subscribe.</em></figcaption>

</figure>

<ul>

<li><strong>Limit contextual swipe to destructive actions. </strong>Burying key actions behind a contextual swipe prevents users from discovering them. Most users expect to use contextual swipe to find destructive actions, such as <em>Delete</em> and <em>Remove</em>: not only was this the original use of the gesture (and thus the best known), there’s also a bit of a metaphorical relation between the gesture to swipe something off the screen and the command to delete that object.</li>

<li><strong>Keep the behavior of contextual swipe consistent</strong> within an application. People have difficulty learning multiple meanings for the same gesture and they will not expect swipe to do different things on different pages of your app. Avoid using actions that are dependent on the state of an item or of the location within the app; instead, keep the meaning of contextual swipe consistent because <a href="/articles/overloaded-vs-generic-commands/">overloaded commands</a> tend to be confusing.</li>

<li><strong>Do not overuse swipe gestures in your app. </strong>If your app uses contextual swipe, make sure it won’t interfere with other uses of swipe in your app (such as swipe to navigate from one page to another).</li>

</ul>

<h2 id="toc-conclusion-2"><strong>Conclusion</strong></h2>

<p>Contextual swipe is popular in app development, but when used incorrectly it can cause confusion. Take caution when using it as a primary method of providing actions for content. Although more and more users have learned to associate swipe with delete, some apps still do not use it, while others use inconsistently or in nonstandard ways. Moreover, the swipe gesture can obscure the item, and thus either increase <a href="/articles/user-mistakes/">user mistakes</a>, or force people to work harder to reassure themselves that they selected the right item.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Mobile User Experience" href="/courses/usability-mobile-websites-apps/?lm=contextual-swipe&amp;pt=article">

<h4 class="title heading-small">Mobile User Experience</h4>

<p id="mobile-user-experience" class="description body-small">

Essential UX design principles for small-screen websites and apps

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">contextual menu,mobile navigation,Interaction Design,Mobile &amp; Tablet</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Interaction Design</span>

<a class="ga-article-related-topic" href="/topic/interaction-design/">Interaction Design</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/mobile-and-tablet-design/">Mobile &amp; Tablet</a>

</li>

</ul>

</div>

</div>

</div>

</div>