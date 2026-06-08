# Adding an Item to a Shopping Cart: Provide Clear, Persistent Feedback - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">6</span>

<div class="article-header">

<h1 class="article-h1">Adding an Item to a Shopping Cart: Provide Clear, Persistent Feedback</h1>

<div class="article-authors">

<span id="gaDataAuthors" class="ga-data-layer" aria-hidden="true">Page Laubheimer</span>

<div class="author-tile multiple body-small">

<div class="author-photos">

<img height="64" width="64" class="author-photo fluid" src="https://media.nngroup.com/media/people/photos/2022-portrait-page-3.jpg.256x256_q75_autocrop_crop-smart_upscale.jpg" alt="">

</div>

<div class="author-meta">

<span class="authors-list">

Page Laubheimer

</span>

<p class="publication-date">

June 17, 2018

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2018-06-17</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Adding an Item to a Shopping Cart: Provide Clear, Persistent Feedback&amp;body=https://www.nngroup.com/articles/cart-feedback/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/cart-feedback/&amp;title=Adding an Item to a Shopping Cart: Provide Clear, Persistent Feedback&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/cart-feedback/&amp;text=Adding an Item to a Shopping Cart: Provide Clear, Persistent Feedback&amp;via=nngroup" data-share-type="Twitter">

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

</span>To confirm that an item has been added to cart, show a number badge and a confirmation popover or page, and change the label of the Add to Cart button, while preserving the ability to add multiples of that item.

</div>

<div class="article-body">

<p>On ecommerce sites, the first step of purchasing a product is adding it to the shopping cart. Clear <a href="https://www.nngroup.com/articles/indicators-validations-notifications/">feedback</a> that this step was completed successfully gives users a sense of control and allows them to confidently continue shopping or proceed with their checkout. (It also complies with two of the <a href="https://www.nngroup.com/articles/ten-usability-heuristics/">10 usability heuristics</a> — <a href="https://www.nngroup.com/articles/visibility-system-status/">visibility of system status</a> and error prevention, as it reassures people that they have not <a href="https://www.nngroup.com/articles/slips/">slipped</a> and added the wrong item.)</p>

<p>However, our usability testing of ecommerce sites shows that many sites do a poor job of confirming when a product has been added to a cart. Specifically, these two issues often arise:</p>

<ul>

<li>It is not clear whether the site processed the add-to-cart action.</li>

<li>If the action was processed, there is no indication of whether the <em>correct</em> product (including specific options such as size, color, or quantity) was added to the cart.</li>

</ul>

<p>When these problems are encountered, users often feel compelled to double check and make sure that the add-to-cart action was completed successfully.  This behavior suggests that they have had poor prior experiences with adding products to carts.</p>

<p>This is a relatively old usability problem for ecommerce websites — we reported on it in in a previous round of ecommerce user research, and we warned publicly about this design flaw as one of the top-3 <a href="https://www.nngroup.com/articles/e-commerce-usability/">bad new ecommerce design trends in 2014</a>. I guess we warned in vain, because the same problem has become <em>worse</em> now, as proven by the new round of ecommerce testing that we have just completed.</p>

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

<a class="ga-article-toc-item" href="#toc-badges-on-the-cart-icon-1">Badges on the Cart Icon</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-confirmation-for-adding-an-item-to-cart-2">Confirmation for Adding an Item to Cart</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-changes-to-the-add-to-cart-button-3">Changes to the Add to Cart Button</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-4">Conclusion</a>

</li>

</ul>

</div>

</div><h2 id="toc-badges-on-the-cart-icon-1">Badges on the Cart Icon</h2>

<p>A noticeable badge superimposed on the cart icon clearly indicates the number of items in the cart and can indirectly assure users that a product has been successfully added to cart.  The badge will stand out clearly if its color contrasts with the cart icon.</p>

<p>If possible, include the cart subtotal near the icon as well. The subtotal helps in several ways:</p>

<ul>

<li>Users can infer to some degree if a major mistake (such as adding more than one of an item) was made.</li>

<li>A change in the subtotal can attract the eye (especially if accompanied by motion or animation).</li>

<li>The size of the cart is increased and represents a larger target for mouse or <a href="https://www.nngroup.com/reports/mobile-website-and-application-usability/">fingers</a>, leveraging <a href="http://www.asktog.com/columns/022DesignedToGiveFitts.html">Fitts’ Law</a>.</li>

</ul>

<figure class="caption"><img alt="Buddiboxes's mobile site shows the running subtotal in the cart icon" border="0" height="591" loading="lazy" src="https://media.nngroup.com/media/editor/2018/02/16/buddhiboxes.png" width="350"/>

<figcaption><em>The mobile site of Buddhiboxes.com showed a cart icon, the number of items in the cart, and the running subtotal, proving that displaying all these details is possible even on a small screen. Users were provided with useful, easily recognizable information; the larger shopping-cart target area was easy to tap without accidentally hitting other UI elements.</em></figcaption>

</figure>

<h2 id="toc-confirmation-for-adding-an-item-to-cart-2">Confirmation for Adding an Item to Cart</h2>

<p>However, just changing the cart icon to reflect the number of items in the cart isn’t enough. In addition to this numeric badge on the cart icon, use a secondary, more noticeable indicator to confirm that a product has been added to cart. Typical examples include a <a href="https://www.nngroup.com/articles/animation-usability/"><strong>subtly</strong> animated</a> popover or a separate page showing which product has been added to the cart. Include an image of the product and a list of corresponding options in these confirmations. However, don’t overuse animation: small amounts of movement can draw attention, but lots of movement are both distracting and annoying.</p>

<p>Stay away from disappearing <a href="https://www.nngroup.com/articles/overuse-of-overlays/">overlays</a> that quickly fade from view. The transient nature of these popovers prevents users from easily reviewing <em>what specifically</em> ended up in the cart — were the size and the color right? Viewing the feedback popover becomes a race against time and can create stress, as well as uncertainty about how to access this information again.</p>

<p>In our new round of usability testing, a participant shopping on Burberry.com added a coat to her cart, noticed the overlay showing that the product had been added to her cart, and began moving her mouse over to the overlay to doublecheck that the item was the size she wanted. However, before she could read the overlay, it disappeared. “Where did my bag go? I guess it’s really sensitive to the movement of my mouse.”</p>

<figure class="caption"><img alt="Burberry transient overlay for add to cart" border="0" height="366" loading="lazy" src="https://media.nngroup.com/media/editor/2018/02/16/burberrypopover.png" width="750"/>

<figcaption><em>The overlay on Burberry.com showed that an item has been added to the shopping bag, but disappeared quickly. Participants in our study attempted to review the feedback to make sure they had added the right item to their bag, but could not do so because of the transient overlay.</em></figcaption>

</figure>

<p>Here are the <strong>recommended</strong> ways to show feedback in the cart:</p>

<ul>

<li>An overlay or popover that <strong>doesn’t obstruct</strong> key information on the product page, and does not disappear on its own, or</li>

<li>A banner that appears on the product page at the top of the page, or</li>

<li>An new interstitial page that shows a <em>Product X has been added to the cart</em> message, with <em>View cart,</em> <em>Checkout,</em> and <em>Continue</em> <em>shopping</em> buttons</li>

</ul>

<figure class="caption"><img alt="Saks Fifth Avenue non modal overlay showing feedback that an item was added to cart" border="0" height="548" loading="lazy" src="https://media.nngroup.com/media/editor/2018/02/16/sakspersistentpopover.png" width="750"/>

<figcaption><em>Saks Fifth Avenue showed a <a href="http://www.nngroup.com/articles/modal-nonmodal-dialog/">nonmodal</a> overlay that didn’t disappear on its own after the user added a product to the cart. While the overlay obscured some of the page content (which we don’t recommend), it still kept the main product information visible. In addition, the nonmodal nature of the overlay allows users to select links outside the overlay without dismissing it. Finally, the overlay  didn’t look like the type of newsletter-signup popups that users in our study would often <a href="http://www.nngroup.com/articles/making-web-advertisements-work/">dismiss without reading</a>.</em></figcaption>

</figure>

<p> </p>

<figure class="caption"><img alt="Boden shows a banner indicating items have been added to cart, but also includes cross-sell promotions" border="0" height="787" loading="lazy" src="https://media.nngroup.com/media/editor/2018/02/16/bodenbanner.png" width="750"/>

<figcaption><em>BodenUSA displayed a banner above the product to indicate that it had been added to the cart. This banner appropriately showed a product image, the options selected, and a clear link to the checkout process. However, it also included upsell promotions (</em>We saw these and thought of you<em>), which can have two downsides: (1) users could assume that the promotions are items in their cart and wonder why they were different from the actual products that they had added to cart , and (2) they could also cause <a href="http://www.nngroup.com/articles/banner-blindness-old-and-new-findings/">banner blindness</a> and get ignored.</em></figcaption>

</figure>

<p> </p>

<figure class="caption"><img alt="Macy's iOS app shows a new interstitial page to confirm an item has been added to cart" border="0" height="402" loading="lazy" src="https://media.nngroup.com/media/editor/2018/02/16/macysinterstitial.png" width="350"/>

<figcaption><em>The Macy’s iOS app took users to a new interstitial page to show that an item had been added to the cart. This pattern is useful when users are likely to order only a few items during a session; otherwise, it can be disruptive for the users’ flow.</em></figcaption>

</figure>

<p>Which of these variations is appropriate for your design depends on the shopping behaviors of your users. In most cases, an overlay or a banner showing that something has been successfully added to one’s cart is most useful, especially on sites where users tend to purchase or compare several items. However, on sites with a limited number of options (such as a custom-furniture store), or with users who purchase only 1–2 items in a session (for example, repeat users such as Amazon Prime shoppers who do not bother to consolidate multiple items in a single order), an interstitial page can <a href="https://www.nngroup.com/articles/shopping-cart/">keep users focused on the checkout process</a>, and thus expedite it.</p>

<p>Whichever pattern you choose for your site, show:</p>

<ul>

<li>A nicely sized <a href="https://www.nngroup.com/articles/shopping-cart/">product image</a> that correctly reflects the color or other options selected by the user</li>

<li>The name of the product</li>

<li>The price of the item</li>

<li>The quantity added</li>

<li>Additional text listing any options selected (size, color, etc.)</li>

</ul>

<h2 id="toc-changes-to-the-add-to-cart-button-3">Changes to the <em>Add</em> <em>to</em> <em>Cart</em> Button</h2>

<p>In our usability studies, many participants accidentally added the same item to their cart multiple times, and, then were surprised during checkout when they noticed the replication.  There are  many reasons why people may add an item to the cart several times:</p>

<ul>

<li>They may forget that they have already put the product into their cart, either because of a distraction or because their purchase was split across a longer period of time (e.g., several hours or even days).</li>

<li>When engaging in comparison shopping across different similar items, people may save candidate products in their shopping cart (a form of external memory).</li>

<li>As they reach the same item in multiple ways (e.g., from a <a href="https://www.nngroup.com/reports/ecommerce-ux-search-including-faceted-search/">search-results page</a> and from a <em>Related</em> <em>Products </em>list on a product page), they may add it to their cart each time, without realizing that they have saved it before.</li>

<li>The site may provide poor feedback that the item was added to cart, and the user may press the <em>Add to cart </em>button multiple times.</li>

</ul>

<p>How can designers remind users that an item was already added to cart? Here are some options:</p>

<ul>

<li><strong>Add a message </strong>indicating that the  item is already in the cart. This message should be visually salient and placed next to the <em>Add to Cart</em> button. Additionally, the button’s label should be changed to <em>Add Another</em> (or similar). While not every user will notice these changes, some will.</li>

<li><strong>Gray out</strong> the <em>Add to cart </em>button or change it to <em>View Cart, In Cart, </em>or to a checkmark to indicate that the item is in the cart. <strong>We don’t recommend this option</strong>, because it prevents people from adding more of the same item to the cart. To avoid that problem, many sites that adopt this solution make the label change transient and revert the button back to the standard <em>Add to Cart </em>after a few seconds. This means that some users may miss the label change and will still add the item to cart multiple times.<img alt="" border="0" height="247" loading="lazy" src="file:////Users/page/Library/Group%20Containers/UBF8T346G9.Office/TemporaryItems/msohtmlclip/clip_image007.png" width="469"/></li>

</ul>

<figure class="caption"><img alt="Rose and Rex changed the Add to Cart button to a checkbox temporarily" height="396" loading="lazy" src="https://media.nngroup.com/media/editor/2018/02/16/roseandrexcheckbox.png" width="750"/>

<figcaption><em>Rose &amp; Rex changed the </em>Add to Cart<em> button to a checkbox after an item was added to the cart;  a few seconds later, this label reverted back to a standard </em>Add to Cart,<em> which did not provide any indication that the item was already in the cart.</em></figcaption>

</figure>

<figure class="caption"><img alt="Freshdirect shows a small, easy-to-miss indicator that an item was already in the cart" height="511" loading="lazy" src="https://media.nngroup.com/media/editor/2018/02/16/freshdirectalreadyincart.png" width="750"/>

<figcaption><em>Freshdirect.com showed a small message below the </em>Add to Cart<em> button to indicate that there were already two of this item in the cart. While potentially helpful, such a message is easy to miss.</em></figcaption>

</figure>

<h2 id="toc-conclusion-4">Conclusion</h2>

<p>Give users appropriate feedback when they add an item to their cart, including all of the following:</p>

<ul>

<li>A badge  on the cart icon</li>

<li>A persistent overlay or new interstitial page showing that the item was successfully added to cart (along with details about the product)</li>

<li>A changed <em>Add to Cart</em> button to showcase that the item is already in the cart (but with the ability to add more of that same item to the cart)</li>

</ul>

<p>Learn more about making purchases easier with <a href="https://www.nngroup.com/reports/ecommerce-user-experience/">800+ UX guidelines in the new edition of our Ecommerce report</a> series.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Omnichannel Journeys and Customer Experience" href="/courses/cross-channel-user-experience/?lm=cart-feedback&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Ecommerce,shopping cart,Interaction Design,interfaces</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Ecommerce</span>

<a class="ga-article-related-topic" href="/topic/e-commerce/">Ecommerce</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/interaction-design/">Interaction Design</a>

</li>

</ul>

</div>

</div>

</div>

</div>