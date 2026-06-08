# Kinect Gestural UI: First Impressions - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">9</span>

<div class="article-header">

<h1 class="article-h1">Kinect Gestural UI: First Impressions</h1>

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

December 26, 2010

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">2010-12-26</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Kinect Gestural UI: First Impressions&amp;body=https://www.nngroup.com/articles/kinect-gestural-ui-first-impressions/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/kinect-gestural-ui-first-impressions/&amp;title=Kinect Gestural UI: First Impressions&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/kinect-gestural-ui-first-impressions/&amp;text=Kinect Gestural UI: First Impressions&amp;via=nngroup" data-share-type="Twitter">

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

</span>Inconsistent gestures, invisible commands, overlooked warnings, awkward dialog confirmations. But fun to play.

</div>

<div class="article-body">

<p><a class="out" href="http://www.xbox.com/kinect/" title="Microsoft: Kinect product info">Kinect</a> is a new video game system that is fully controlled by <strong> bodily movements</strong>. It's vaguely similar to the Wii, but <strong> doesn't use a controller </strong> (and doesn't have the associated risk of banging up your living room if you lose your grip on the Wii wand during an aggressive tennis swing).</p>

<p>Kinect observes users through a video camera and recognizes gestures they make with different body parts, including hands, arms, legs, and general posture. The fitness program, for example, is fond of telling me to <em> "do deeper squats," </em> which it can do because it knows how my entire body is moving. Analyzing body movements in such detail far exceeds the Wii's capabilities, though it's still not going to put my trainer down at the gym out of work.</p>

<p>Kinect presents a far more <strong> advanced gesture-based user experience </strong> than any previous system seen outside the fancy research labs. Yes, I saw similar interfaces as long ago as 1985 at cutting-edge academic conferences — most notably <a class="out" href="http://www.inventinginteractive.com/2010/03/22/myron-krueger/" title="Inventing Interactive: short history with video clips of Krueger's demos"> Myron Krueger's Videoplace</a>. But there's a big difference between a million-dollar research system and a $150 Xbox add-on.</p>

<p>On the one hand, Kinect is an amazing advance, especially considering its low price. On the other hand, the <strong> 25-year time lag between research and practice </strong> for gesture UIs is slightly worse than the usual fate of <a class="old" href="/articles/top-research-laboratories-in-human-computer-interaction-hci/" title="Alertbox: Top Research Laboratories in Human-Computer Interaction (HCI)"> HCI research</a> advances. For example, 20 years lapsed between Doug Engelbart's invention of the mouse (1964) and the first commercially feasible mouse-based computer (the Mac in 1984).</p>

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

<a class="ga-article-toc-item" href="#toc-gesture-based-ui-usability-weaknesses-1">Gesture-Based UI = Usability Weaknesses</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-good-usability-2">Good Usability</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-fun-game-despite-usability-problems-3">Fun Game, Despite Usability Problems</a>

</li>

</ul>

</div>

</div><h2 id="toc-gesture-based-ui-usability-weaknesses-1">Gesture-Based UI = Usability Weaknesses</h2>

<p>Kinect exhibits many of the weaknesses Don Norman and I listed in our analysis of <a class="old" href="http://www.jnd.org/dn.mss/gestural_interfaces_a_step_backwards_in_usability_6.html" title="Donald A. Norman and Jakob Nielsen essay: Gestural Interfaces: A Step Backwards In Usability"> gestural interfaces' usability problems</a>:</p>

<h3>Visibility</h3>

<p>Sometimes options display as an explicit menu, making them visible. But there are no explicit affordances on the screen during gameplay for most of the things you can do. Primarily, users are forced to rely on <strong> memorizing the instructions </strong> shown before the game started. (Even though it's a key <a class="new" href="http://www.nngroup.com/courses/hci/" title="Nielsen Norman Group course: From Science to Design - Applying HCI Principles to Real World Problems"> human factors principle</a> to reduce reliance on the <a class="old" href="/articles/short-term-memory-and-web-usability/" title="Alertbox: Short-Term Memory and Web Usability"> highly fallible human memory</a>.)</p>

<p>For example, how do you know to jump <em> up </em> to make a <em> long </em> jump in <cite> Kinect Sports</cite>, even though it's a completely illogical move (and would make more sense for a <em> high </em> jump)? By remembering what you read before your avatar entered the stadium, of course.</p>

<p style="text-align: center; "><img alt="Screenshot from Kinect Adventures, showing pregame instructions" height="335" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/kinect-pregame-instructions.jpg" width="600"/><br/>

<em>Read the manual before using the interface.<br/>

(Yes, it's a </em> *cute* <em> manual, but these are still instructions to memorize.)<br/>

(<cite>Kinect Adventures</cite>) </em></p>

<p>Kinect exhibits another type of visibility problem: <strong> on-screen alerts are easily overlooked </strong> because the user's attention is focused elsewhere. This rarely happens with <a class="new" href="http://www.nngroup.com/courses/mobile-apps-touchscreens/" title="Nielsen Norman Group course: Mobile User Experience 2 - Touchscreen Application Usability"> mobile touch-UIs</a>: because of their small size, you see anything that pops up on the screen. In contrast, it's common for users to <a class="old" href="/articles/error-message-guidelines/" title="Alertbox: Error Message Guidelines"> overlook error messages</a> on cluttered Web pages.</p>

<p>On Kinect, users don't overlook messages because of clutter, but because of engaging action. For example, in observing users play <cite> Kinect Adventures</cite>, I frequently saw a warning message in the upper left telling users to move to a different part of the floor. Yes, as the usability observer I saw this — but the game-playing users didn't. They were too focused on the compelling movements in the middle of the screen. They watched their avatar and the gamespace, and didn't notice the appearance of UI chrome in the corner.</p>

<p style="text-align: center; "><img alt="Screenshot from Kinect Adventures, game in progress with an alert message" height="337" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/kinect-message-overlooked.jpg" width="600"/><br/>

<em>How can users miss the huge "Move Forward" warning?<br/>

They miss it because they're fully engaged in steering their raft down the river.<br/>

(<cite>Kinect Adventures</cite>) </em></p>

<p>A similar, but less serious problem occurs in <cite> Your Shape: Fitness Evolved </cite> when you're trying to complete a hard cardio program. The number of reps left in the set counts down in the corner, but you tend to focus on your trainer and keeping up with her movements.</p>

<p>It'll be a design challenge to increase users' awareness of system messages without detracting from their engagement in the game's primary activity.</p>

<h3>Feedback</h3>

<p>Related to the lack of visibility, it is hard to know why certain actions have specific effects because there is little direct feedback. In the table tennis game, making a smacking movement with your hand mimics hitting the ball with a paddle and you do get immediate feedback showing whether or not you "hit" the ball. But it's difficult to figure out why you sometimes succeed in making a hard smash. For sure, it's not dictated solely by hand-movement speed.</p>

<p>Other times, Kinect gives great feedback based on its direct observation of your movements. In <cite> Dance Central </cite> , you try to follow the movements of an on-screen dancer, whose body parts light up to indicate where your dance moves are lacking. This is better (and less disruptive) feedback than a voiceover saying, "move your left arm up more."</p>

<h3>Consistency and Standards</h3>

<p>That there are no universal standards for gestural interactions yet is a problem in its own right, because the UI <strong> cannot rely on learned behavior </strong> . The Kinect has a few system-wide standards, however, which do help users.</p>

<p>For example, there is a standard way to pause a game to bring up the menu: stand with your right arm straight down and your left arm held at a 45-degree angle. Definitely not a natural stance — indeed, it was probably chosen because it will never occur in normal gameplay.</p>

<p>The pause gesture becomes the user's lifeline, but there are no standards for other, commonly desired <a class="old" href="/articles/generic-commands/" title="Alertbox"> generic commands</a>, such as "back." This makes it harder for users to navigate the UI, because they need to figure out these basic operations every time. Less learning takes place when the same thing is done differently in different games.</p>

<p>As the following two screenshots show, there's not even consistency as to which hand is used for "back," let alone which gesture to use or how the feature is presented visually.</p>

<p style="text-align: center; "><img alt="Screenshot from Kinect Sports, where back is an option in the upper right" height="335" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/kinect-back-right.jpg" width="600"/><br/>

<em>"Back" in upper right; activated by holding hand still over button.<br/>

(<cite>Kinect Sports</cite>) </em></p>

<p style="text-align: center; "><img alt="Screenshot from Dance Central, menu mainly on the right, but back option is on the left and is activated by a left-hand gesture" height="337" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/kinect-back-left.jpg" width="600"/><br/>

<em>"Back" in lower left; activated by swiping left hand rightwards.<br/>

(<cite>Dance Central</cite>) </em></p>

<p>At least you can tell that the designers have done their usability testing: they've applied a Band-Aid to the UI in the form of a note saying "left hand" next to <cite> Dance Central</cite>'s inconsistent "Back" command. Whenever you have to explain a GUI widget, it's probably wrong.</p>

<p>Within <cite> Kinect Sports</cite>, different movements are used to throw a bowling ball, a discus, and a javelin, and still different moves are used to smack a table-tennis ball and kick a soccer ball. However, this across-game inconsistency is less of a problem, because the design embodies <strong> external consistency</strong>: the game gestures are similar to those used to deal with these objects in the real world.</p>

<h3>Reliability and Accidental Activation</h3>

<p>Kinect generally does a good job of protecting against the accidental activation we see so often when <a class="old" href="/articles/mobile-usability-update/" title="Alertbox: Mobile Usability"> testing mobile devices</a>. If your finger brushes against something on your phone or iPad, off you go — often without knowing what happened (because you don't know what you touched).</p>

<p>Kinect usually demands a <strong> confirmation gesture </strong> before it acts on user commands. This request for confirmation alerts users that something is about to happen, and prevents unintentional gestures from initiating actions. Unfortunately, the confirmations are inconsistent:</p>

<ul>

<li>Hold your hand still over a button, while an animated circle is completed. (Most games)</li>

<li>After selecting a menu item, swipe your hand left — unless you want the "back" feature, in which case you swipe right. ( <cite> Dance Central </cite> )</li>

<li>First select a command, and then keep your hand still over a small confirmation button that pops up next to that command. ( <cite> Your Shape </cite> )</li>

</ul>

<p style="text-align: center; "><img alt="Screenshot from Your Shape: Fitness Evolved, showing user selecting a menu option and being presented with an additional button to confirm this selection" height="324" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/kinect-confirmation-gesture.jpg" width="600"/><br/>

<em>Touching a button doesn't activate it;<br/>

instead, this gesture brings up another button as a confirmation step.<br/>

(<cite>Your Shape: Fitness Evolved</cite>) </em></p>

<p>These confirmation gestures are annoying, even though I'm sure they save time in the long run by reducing accidental activation. (I still occasionally activated features accidentally by leaving my hand over something for too long. That's when the <strong> poor undo </strong> support and inconsistent "back" features become doubly annoying.)</p>

<h2 id="toc-good-usability-2">Good Usability</h2>

<p>Kinect has many great design elements that clearly show that the team (a) knows usability, (b) did user testing, and (c) had management support to prioritize usability improvements, even when they required extra development work.</p>

<p>This makes sense; the only reason for Kinect to exist in the first place is as a casual game system that's easy to pick up. It's not for hardcore gamers who are willing to suffer through contorted combos of button-pushes to make their game characters do moves. Kinect is targeted at the much broader masses, which requires strong usability. (Indeed, the game sold 4 M units during the first 6 weeks after launch.)</p>

<p>Good usability examples include the above mentioned on-screen hint in the exact spot of a command that would have been otherwise difficult to activate. How do the designers know where users need hints? From having watched real people play games and taken note of where they got stuck.</p>

<p>Another nice example of usability fit-and-finish is the snap-to effect: buttons feel "magnetic" and attract the cursor whenever your hand moves close to a button. (Thus enlarging the effective <a class="old" href="http://www.asktog.com/columns/022DesignedToGiveFitts.html" title="Bruce 'Tog' Tognazzini: A Quiz Designed to Give You Fitts"> Fitts' Law</a> size of the button and alleviating the impact of shaky hand movements.)</p>

<p>The most compelling usability advance is the way Kinect automatically signs in users after recognizing their faces. Step in front of the sensor, and <em> "Jakob recognized" </em> appears on the screen, after which the current game starts using my customized avatar. This is the type of interaction technique I called a "<a class="old" href="/articles/noncommand/" title="Jakob Nielsen: academic research paper from 1993">non-command user interface</a>" in 1993: You don't feel that you're issuing commands to a computer; you simply go about your business the way you normally would, and the computer does what's needed to complete its part of the task.</p>

<p>We know from <a class="old" href="/articles/intranet-portals/" title="Alertbox: Enterprise Portals Are Popping"> researching enterprise portals</a> that <strong> single sign-on </strong> is one of the most wanted (but least-delivered) intranet features. But automated sign-on is even better and eliminates an entire class of interaction steps.</p>

<h2 id="toc-fun-game-despite-usability-problems-3">Fun Game, Despite Usability Problems</h2>

<p>We set up a Kinect system in the coffee break area during the recent Las Vegas <a class="new" href="http://www.nngroup.com/training/" title="Nielsen Norman Group: conference site"> Usability Week conference</a> so that conference participants could experience this new UI paradigm firsthand.</p>

<p><strong>People had great fun </strong> and were able to play the games after only a short demo.</p>

<p>As was clear in this situation, the same type usability issues that cause substantial problems in <a class="old" href="/articles/ipad-usability-year-one/" title="Alertbox: iPad Usability - First Findings From User Testing"> iPad user testing</a> are brushed off by Kinect users. So how come Kinect's overall user experience works, despite its many user interface deficiencies?</p>

<p>The explanation lies in the <strong> difference in user tasks </strong> between the two systems. <a class="old" href="/articles/usability-101-introduction-to-usability/" title="Alertbox: Usability 101 - Introduction to Usability"> Usability is defined relative to two points</a>: the users and their tasks. Comparing iPad and Kinect, even if the users are the same, usability will differ if people are trying to do two very different things.</p>

<p>Sure, people play games on iPad — indeed I have whiled away many hours in airports with <cite> Solitaire City </cite> and <cite> We Rule</cite>, and other members of Nielsen Norman Group swear by <cite> Angry Birds</cite>. However, whacky interaction styles in games rarely pose problems. What we really care about in tablet design are <strong> business-oriented user interfaces </strong> for things like e-commerce, stock trading, and information access. That's when inconsistencies and weird design reduce usage, and thus cost you business.</p>

<p>Also, Kinect users don't jump from one context to another every minute or two the way mobile users do. When you play a Kinect game, you're immersed in that game (often for half an hour or more) and don't see any of the other games. In fact, switching games is done not through on-screen navigation, but by swapping DVDs, thus reducing the load on the on-screen UI.</p>

<p>Finally, different games often have wildly different activities and goals, so it's okay to have varying user interfaces. Whitewater rafting and dancing to Lady Gaga's latest creation are no more similar than chalk and cheese.</p>

<p>On the iPad, whether you're shopping for one thing or another, you expect to be treated to <a class="new" href="http://www.nngroup.com/reports/ecommerce-user-experience/" title="Nielsen Norman Group report series: E-Commerce Usability Guidelines"> best practices for e-commerce user experience</a> as defined by the countless websites you've already used. Similarly, whether you're reading a magazine or a newspaper, you expect similarities in the UI for navigating among articles and for moving through an individual story's content. And whether you're researching investments in your brokerage account, checking the weather forecast, or modifying an airline reservation, you expect similar interaction techniques for operations like filtering long lists or changing measurement units.</p>

<ul>

<li><strong>Purposeful use </strong> of iPad or gesture interfaces on other tablets and phones is comprised of fairly similar tasks, with strong user expectations and frequent context switches that penalize inconsistent design. Also, users have to manipulate large data sets with feature-rich commands and spend a fairly large percentage of their total time operating the UI. User experience quality is mainly determined by UI usability and whether the content easily satisfies users' information needs.</li>

<li><strong>Playing </strong> with Kinect involves highly distinctive activities, where users focus on one game at a time and thus are better able to overcome inconsistencies. Here, users navigate a fairly small data space and spend most of their time playing with only the occasional detour outside the gameworld to operate the command-oriented part of the UI. User experience quality is mainly determined by gameplay.</li>

</ul>

<p>A final difference is that mobile devices are the ultimate in <strong> individual use</strong>: your phone is <em> yours </em> and it's usually a solitary activity to interact with the device. Even when connecting to a social network, the on-screen actual user interface is being operated by you alone. In contrast, gaming consoles are often used in a <strong> group setting </strong> where new users get a gentle introduction to the new user interface by the more experienced users in the group.</p>

<p>This difference in usage circumstances means that consoles can rely less on having a self-explanatory UI, whereas a mobile UI must have extremely high learnability.</p>

<table align="center" style="border-style: solid; border-color: #cccccc; border-width: 1px; border-collapse: collapse; max-width: 50em;">

<tbody>

<tr>

<th style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; background-color:  #003366; color: #ffffff; width: 30%;"> </th>

<th style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: center; background-color:  #003366; color: #ffffff; width: 35%;">Kinect<br/>

(+ other game consoles)</th>

<th style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: center; background-color:  #003366; color: #ffffff; width: 35%;">iPad/tablets/mobiles<br/>

(when not used for games)</th>

</tr>

<tr>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">User's main goal</td>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">Entertainment</td>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">Getting things done</td>

</tr>

<tr>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">What's being controlled</td>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">Self-contained gameworld</td>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">The real world</td>

</tr>

<tr>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">Consequence of user errors</td>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">Your avatar "dies" &amp; restarts level</td>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">Lose your job and investments</td>

</tr>

<tr>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">Diversity of activities</td>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">Wide</td>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">Fairly similar operations across tasks</td>

</tr>

<tr>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">Time spent within one UI</td>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">1 hour per game</td>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">1–2 minutes per site/app</td>

</tr>

<tr>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">Navigation space</td>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">Small<br/>

(except for gameworld locations)</td>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">Mid-sized (apps) to<br/>

immense (Web)</td>

</tr>

<tr>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">Commands</td>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">Few</td>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">Many</td>

</tr>

<tr>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">Data objects manipulated</td>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">Handful</td>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">Hundreds to millions</td>

</tr>

<tr>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">Usage context</td>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">Often communal<br/>

(experienced users help newbies)</td>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">Usually solitary<br/>

(figure it out on your own)</td>

</tr>

<tr>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">UX quality determinants</td>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">Gameplay</td>

<td style="border-style: solid; border-width: 1px; padding: 0.5ex; text-align: left; vertical-align: middle;">UI usability;<br/>

whether content easily satisfies information needs</td>

</tr>

</tbody>

</table>

<p>Kinect is an exciting advance in user interface technology, but many of the user experience characteristics that make it so also mean that it's not the road ahead for the practical user interfaces that businesses, government agencies, and <a class="new" href="/articles/non-profit-websites-donations/" title="Alertbox: Non-Profit Organization Websites: Increasing Donations and Volunteering"> non-profit organizations</a> need for their everyday websites, intranets, and applications. Design ideas that make Kinect fun could cost you millions.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Emerging Patterns in Interface Design" href="/courses/emerging-patterns-interface-design/?lm=kinect-gestural-ui-first-impressions&amp;pt=article">

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">gestures,Human Computer Interaction,new technologies,games</span>

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