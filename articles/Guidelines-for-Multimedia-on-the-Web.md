# Guidelines for Multimedia on the Web - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">10</span>

<div class="article-header">

<h1 class="article-h1">Guidelines for Multimedia on the Web</h1>

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

November 30, 1995

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">1995-11-30</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Guidelines for Multimedia on the Web&amp;body=https://www.nngroup.com/articles/guidelines-for-multimedia-on-the-web/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/guidelines-for-multimedia-on-the-web/&amp;title=Guidelines for Multimedia on the Web&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/guidelines-for-multimedia-on-the-web/&amp;text=Guidelines for Multimedia on the Web&amp;via=nngroup" data-share-type="Twitter">

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

<p>Multimedia is gaining popularity on the Web with several technologies to support use of animation, video, and audio to supplement the traditional media of text and images. These new media provide more design options but also require design discipline. Unconstrained use of multimedia results in user interfaces that confuse users and make it <em> harder </em> for them to understand the information. Not every webpage needs to bombard the user with the equivalent of Times Square in impressions and movement.</p>

<h3>Animation</h3>

<p>Moving images have an overpowering effect on the human peripheral vision. This is a survival instinct from the time when it was of supreme importance to be aware of any saber-toothed tigers before they could sneak up on you. These days, tiger-avoidance is less of an issue, but anything that moves in your peripheral vision still dominates your awareness: it is very hard to, say, concentrate on reading text in the middle of the a page if there is a spinning logo up in the corner. Never include a permanently moving animation on a web page since it will make it very hard for your users to concentrate on reading the text.</p>

<p>Animation is good for:</p>

<ul>

<li><strong>Showing continuity in transitions. </strong> When something has two or more states, then changes between states will be much easier for users to understand if the transitions are animated instead of being instantaneous. An animated transition allows the user to track the mapping between different subparts through the perceptual system instead of having to involve the cognitive system to deduce the mappings. A great example is the winner of the first Java programming contest: proving the Pythagorean theorem by animating the movement of various squares and triangles as they move around to demonstrate that two areas are the same size (unfortunately, this otherwise good page uses animated text inappropriately: the text moves constantly and is hard to relate to the events in the main animation).</li>

<li><strong>Indicating dimensionality in transitions. </strong> Sometimes opposite animated transitions can be used to indicate movement back and forth along some navigational dimension. For example, paging through a series of objects can be shown by an animated sweep from the right to the left for turning the page forward (if using a language where readers start on the left). Turning back to a previous page can then be shown by the opposite animation (sweeping from the left to the right). If users move orthogonally to the sequence of pages then other animated effects can be used to visualize the transition. For example following a hypertext link to a footnote might be shown by a "down" animation and tunneling through hyperspace to a different set of objects might be shown by an "iris open" animation.<br/>

One example used in several user interfaces is the use of zooming to indicate that a new object is "grown" from a previous one (e.g., a detailed view or property list opened by clicking on an icon) or that an object is closed or minimized to a smaller representation. Zooming out from the small object to the enlargement is a navigational dimension and zooming in again as the enlargement is closed down is the opposite direction along that dimension.</li>

<li><strong>Illustrating change over time. </strong> Since an animation is a time-varying display, it provides a one-to-one mapping to phenomena that change over time. For example, <a href="/articles/using-deforestation-rain-forest-example/"> deforestation of the rain forest</a> can be illustrated by showing a map with an animation of the covered area changing over time.</li>

<li><strong>Multiplexing the display. </strong> Animation can be used to show multiple information objects in the same space. A typical example is <a href="http://www-i5.informatik.rwth-aachen.de/mbp/mapzine/test.html"> client-side imagemaps</a> with explanations that pop up as the user moves the cursor over the various hypertext anchors. It is also possible to indicating the active areas by having them shimmer or by surrounding them with a marquee of "marching ants". As always, objects should only move when appropriate (e.g., when the cursor is over the image).</li>

<li><strong>Enriching graphical representations. </strong> Some types of information are easier to visualize with movement than with still pictures. Consider, for example, how to visualize the tool used to remove pixels in a graphics application. The canonical icon is an eraser as shown on the left in the following figure, but in user testing I have sometimes found that people think that the icon is a tool for drawing three-dimensional boxes. Instead, one can use an animated icon as shown on the right in the figure: when the icon animates, the eraser is moved over the background and pixels are removed, clearly showing the functionality of the tool.

<center><img alt="Eraser icon and three stills from an animated eraser icon" height="66" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/eraser_icons.gif" width="248"/></center>

In icon design, it is always easier to illustrate objects (a box) than operations (removing pixels), but animation provides the perfect support for illustrating any kind of change operation. In an experiment reported at the <cite> CHI'91 </cite> conference, <a href="http://ron.taglab.ca/"> Baecker</a>, Small, and Mander increased the comprehension of a set of icons from 62% to 100% by animating them. Of course, an icon should only animate when the user indicates a special interest in it (for example, by placing the mouse cursor over it or by looking at it for more than a second if eye-tracking is available). Especially considering the preponderance of toolbars in current applications it would be highly distracting if all icons were to animate at all times.</li>

<li><strong>Visualizing three-dimensional structures. </strong> Since the computer screen is two-dimensional, users can never get a full understanding of a three-dimensional structure by a single illustration, no matter how well designed. Animation can be used to emphasize the three-dimensional nature of objects and make it easier for users to visualize their spatial structure. The animation need not necessarily spin the object in a full circle: just slowly turning it back and forth a little will often be sufficient. The movement should be slow to allow the user to focus on the structure of the object. Three-dimensional objects may be moved under user control, but often it is better if the designer determines in advance how to best animate a movement that provides optimal understanding of the object: this pre-determined animation can then be activated by the user by simply placing the cursor over the object, whereas user-controlled movements require the user to understand how to manipulate the object (which is inherently difficult with a two-dimensional control device like the mouse used with most computers - to be honest, <a class="old" href="/articles/2d-is-better-than-3d/" title="Alertbox Nov. 1998: Why 2D is better than 3D"> 3D is never going to make it</a> big time in user interfaces until we get a true 3D control device).</li>

<li><strong>Attracting attention. </strong> Finally, there are a few cases where the ability of animation to dominate the user's visual awareness can be turned to an advantage in the interface. If the goal is to draw the user's attention to a single element out of several or to alert the user to updated information then an animated headline will do the trick. Animated text should be drawn by a one-time animation (e.g., text sliding in from the right, growing from the first character, or smoothly becoming larger) and never by a continuous animation since moving text is much harder to read than static text. The user should be drawn to the new text by the initial animation and then left in peace to read the text without further distraction.</li>

</ul>

<p><em>(For newer guidelines, see article on <a href="/articles/animation-usability/"> animation for attention and comprehension</a>.)</em></p>

<h3>Video</h3>

<p>Due to bandwidth constraints, use of video should currently be minimized on the web. Eventually, video will be used more widely, but for the next few years most videos will be short and will use very small viewing areas. Under these constraints, video has to serve as a supplement to text and images more often than it will provide the main content of a website.</p>

<p>Currently, video is good for:</p>

<ul>

<li>Promoting television shows, films, or other non-computer media that traditionally have used trailers in their advertising.</li>

<li>Giving users an impression of a speaker's personality. Unfortunately, most corporate executives project a lot less personality than, say, Captain Janeway from Star Trek, so it is not necessarily a good idea to show a talking head unless the video clip truly adds to the user's experience.</li>

<li>Showing things that move. For example a clip from a ballet. Product demos of physical products (e.g., a coin counter) are also well suited for video, whereas software demos are often better presented as a series of full-sized screendumps where the potential customer can study the features at length.</li>

</ul>

<p>A major problem with most videos on the web right now is that their production values are much too low. User studies of CD-ROM productions have found that users expect broadcast-quality production values and that users get very impatient with low-quality video.</p>

<p>A special consideration for video (and spoken audio) is that any narration may lead to difficulty for international users as well as for users with a hearing disability. People may be able to understand written text in a foreign language because they have time to read it at their own speed and because they can look up any unknown words in a dictionary. Spoken words are sometimes harder to understand, especially if the speaker is sloppy, has a dialect, speaks over a distracting soundtrack, or simply speaks very fast. Poor audio quality may contribute to the difficulty of understanding spoken text: it is recommended to use professional quality audio equipment and/or lavaliere microphones when recording a narrator. The classic solution to these problems is to use subtitles but as shown in the following figure, subtitles require special attention on the web.</p>

<p> </p>

<center><img alt="Three screendumps from a videotape with different kinds of

subtitles" height="186" loading="lazy" src="//media.nngroup.com/media/editor/alertbox/subtitles.jpg" width="580"/></center>

<p>The figure shows a subtitled frame from Sun's Starfire video. The small subtitles (left image) look good on the <a href="http://media.nngroup.com/media/editor/2013/03/14/sunpad_original.jpg"> original video tape </a> (JPEG, 197 K) but are virtually unreadable on the smaller image size currently used for computerized videos. Using bigger subtitles that have been anti-aliased for computer viewing (middle image) improves readability significantly, but the best results are achieved by the letterbox format (right image). In this example, the subtitles in the letterbox are constructed by enlarging the video area for the movie file with a 24-pixels high black area. Doing so does not increase the file size proportionally since the black area compresses very nicely. Even so, it would be better to transmit the subtitles as ASCII (or Unicode) and have them rendered in the letterbox on the client machine: a perfect job for an applet. It would even be possible to have the user select the language for the subtitles through a preference setting or a <a href="http://media.nngroup.com/media/editor/2013/03/14/9512_simulated_popup.jpg"> pop-up menu</a> (JPEG, 206 K).</p>

<p><em>(For newer findings, see article on <a class="new" href="/articles/talking-head-video-is-boring-online/" title="Alertbox: Talking-Head Video Is Boring Online"> eyetracking studies of video clips on websites</a>.) </em></p>

<h3>Audio</h3>

<p>The main benefit of audio is that it provides a channel that is separate from that of the display. Speech can be used to offer commentary or help without obscuring information on the screen. Audio can also be used to provide a sense of place or mood as done to perfection in the game <cite> Myst </cite> . Mood-setting audio should employ very quiet background sounds in order not to compete with the main information for the user's attention.</p>

<p>Music is probably the most obvious use of sound. Whenever you need to inform the user about a certain work of music, it makes much more sense to simply play it than to show the notes or to try to describe it in words. For example, if you are out to sell seats to the <a href="http://lascala.milano.it"> La Scala opera</a> in Milan, Italy, it is an obvious ploy to allow users to hear a snippet of the opera: yes, Verdi really <em> could </em> write a good tune (AU file, 1.4 MB), so maybe I will go and hear the opera next time I am over there. In fact, the audio clip is superior to the video clip  from the same opera which is too fidget to impress the user and yet takes much too long to download (QuickTime, 3.6 MB). [Both audio and video clips are now gone from the opera's website — another sad example of <a href="/articles/fighting-linkrot/">linkrot</a>.]</p>

<p>Voice recordings can be used instead of video to provide a sense of the speaker's personality: the benefits are smaller files, easier production, and the fact that people often sound good even if they would look dull on television. Speech is also perfect for teaching users the pronunciation of words as done by the French wine site: it used to be the case that you could buy good wine cheaply by going for chateaus that were hard to pronounce (because nobody dared ask for them in shops or restaurants) -- no more in the webbed world.</p>

<p>Non-speech sound effects can be used as an extra dimension in the user interface to inform users about background events: for example, the arrival of new information could be signaled by the sound of a newspaper dropping on the floor and the progress of a file download could be indicated by the sound of water pouring into a glass that gradually fills up. These kinds of background sounds have to be very quiet and nonintrusive. Also, there always needs to be a user preference setting to turn them off.</p>

<p>Good quality sound is known to enhance the user experience substantially so it is well worth investing in professional quality sound production. The classic example is the video game study where users claimed that the graphics were better when the sound was improved, even though the exact same graphics were used for the poor-quality sound and the good-quality sound experiments. Simple examples from web user interfaces are the use of a low-key clicking sound to emphasize when users click a button and the use of opposing sounds (cheeeek chooook) when moving in different directions through a navigation space.</p>

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

<a class="ga-article-toc-item" href="#toc-response-time-1">Response Time</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-updated-multimedia-guidelines-2">Updated Multimedia Guidelines</a>

</li>

</ul>

</div>

</div><h2 id="toc-response-time-1">Response Time</h2>

<p>Many multimedia elements are big and take a long time to download with the horribly low bandwidth available to most users. It is recommended that the file format and size are indicated in parentheses after the link whenever you point to a file that would take more than 15 seconds to download with the bandwidth available to most of your users. If you don't know what bandwidth your users are using you should do a survey to find out since this information is important for many other page design issues. At this time, most home users have at most 28.8 Kb, meaning that files longer than 50 KB need a size warning. Business users often have higher bandwidth, but you should probably still mark files larger than about 200 KB.</p>

<p>The 15-second guideline in the previous paragraph was derived from the basic set of <a href="/articles/response-times-3-important-limits/"> response time values</a> that have been known since around 1968. System response needs to happen within about 10 seconds to keep the user's attention, so users should be warned before slower operations. On the web, current users have been trained to endure so much suffering that it may be acceptable to increase the limit value to 15 seconds. If we ever want the general population to start treating the web as more than a novelty, we will have to provide response times within the acceptable ranges, though.</p>

<p>Design of client-side multimedia effects has to consider the other two response time limits also:</p>

<ul>

<li>The feeling of directly manipulating objects on the screen requires <strong> 0.1 second </strong> response times. Thus, the time from the user types a key on the keyboard or moves the mouse until the desired effect happens has to be faster than 0.1 seconds if the goal is to let the user control a screen object (e.g., rotate a 3D figure or get pop-ups while moving over an imagemap).</li>

<li>If users do not need to feel a direct physical connection between their actions and the changes on the screen, then response times of about <strong> 1.0 second </strong> become acceptable. Any slower response and the user will start feeling that he or she is waiting for the computer instead of operating freely on the data. So, for example, jumping to <a href="/articles/needing-personal-t1-line/"> a new page</a> or recalculating a spreadsheet should happen within a second. When response times surpass a second, users start changing their behavior to a more restricted use of the system (for example, they won't try out as many options or go to as many pages).</li>

</ul>

<h2 id="toc-updated-multimedia-guidelines-2">Updated Multimedia Guidelines</h2>

<p>We are finding new guidelines on multimedia, now that it's more common and less subject to technical limitations.</p>

<p>I'll present my newest usability guidelines in the tutorial on <a class="new" href="/courses/web-ux-design-guidelines/" title="Nielsen Norman Group: conference tutorial outline"> Top Web UX Design Guidelines</a> at the annual <a class="new" href="/training/" title="Conference program and list of usability training tutorials"> Usability Week conference</a>.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Human Computer Interaction</span>

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