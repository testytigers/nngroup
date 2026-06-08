# 1994 Design of SunWeb: Sun Microsystems&#x27; Intranet - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">17</span>

<div class="article-header">

<h1 class="article-h1">1994 Design of SunWeb: Sun Microsystems&#x27; Intranet</h1>

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

December 31, 1994

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">1994-12-31</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: 1994 Design of SunWeb: Sun Microsystems&#x27; Intranet&amp;body=https://www.nngroup.com/articles/1994-design-sunweb-sun-microsystems-intranet/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/1994-design-sunweb-sun-microsystems-intranet/&amp;title=1994 Design of SunWeb: Sun Microsystems&#x27; Intranet&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/1994-design-sunweb-sun-microsystems-intranet/&amp;text=1994 Design of SunWeb: Sun Microsystems&#x27; Intranet&amp;via=nngroup" data-share-type="Twitter">

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

</span>This paper presents the methods used to design the user interface and overall structure of the internal web pages (intranet) for Sun Microsystems. Sun had an extensive set of information available on the WWW with the home page as the access point, but also wanted to provide employees access to internal information that could not be made available to the Internet at large.

Much of the user interface work was done in a few weeks with four usability studies completed in a single week: card sorting to discover the users&#x27; view of the information space, an icon intuitiveness study, and two tests of the actual interface.

</div>

<div class="article-body">

<p><strong>Note added May 1995: </strong> This report was written for traditional print publication and is thus not a paragon of hypertext design. Also, the design described in this report is clearly "last year's style" on the Web with its profusion of icons and options on the home page. The design is appropriate for its intended use (a corporate-wide internal information system) but should not be emulated for Web sites intended to present a company's image on the Internet.<br/>

<strong>Added 2002</strong>: For more recent information about intranet design and usability, see Nielsen Norman Group's <a href="http://www.nngroup.com/reports/topic/intranets/" title="Listing of reports with links to immediate download"> usability studies on intranets and Intranet Design Annuals</a>.</p>

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

<a class="ga-article-toc-item" href="#toc-background-1">Background</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-usability-plan-2">Usability Plan</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-iterative-design-3">Iterative Design</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-unified-design-4">Unified Design</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-references-5">References</a>

</li>

</ul>

</div>

</div><h2 id="toc-background-1">Background</h2>

<p>Sun Microsystems is a leading vendor of computer workstations and system software with a large number of branches all over the world. The company has large amounts of internal information that would be of interest to employees but which currently exists in inconsistent formats and in locations that are difficult for new employees to discover. Sun had earlier produced a set of World Wide Web pages with external information for access through the Internet and that system had been favorably received both inside and outside the company, and it was a natural idea to follow up with an internal Web service, especially given that all Sun employees use networked workstations.</p>

<p>For security purposes, it was desirable to have separate visual identities for the internal and external pages (making it clear to users and authors when information could be accessed by outsiders). Also, the type of information available through the internal web was in many ways different in nature from the external information, meaning that a different design would be appropriate. Therefore, a separate SunWeb project was initiated in order to design Sun's internal Web.</p>

<p>SunWeb was designed during the summer of 1994, a period where the number of Web servers on the Internet grew at a rate of about 10,000% per year (doubling every two months). We suspect that the growth of internal Web servers inside Sun's firewall was even faster in this period. Many Sun employees had already built home pages for groups and individuals before the start of the SunWeb project and many more were coming online during the project. As another indication of the growth of the Web inside Sun, the SunWeb server was accessed by 2,649 different employees during a 34-day period of testing where it had not even been announced yet. Thus, work on SunWeb had to be completed within a few months if we were to have any hope of achieving a consistent user interface and not just glom together a set of disparate designs.</p>

<h2 id="toc-usability-plan-2">Usability Plan</h2>

<p>Because of the need to deliver a design quickly, we decided to rely on "discount usability engineering" [Nielsen 1994] to ensure the usability of the design. Discount methods are deliberately informal and rely less on statistics and more on the interface engineer's ability to observe users and interpret results. A major benefit of these methods is that they are fast, and since we were not developing, say, an aircraft cockpit or other interfaces with lives at stake, we were willing to risk the possible downside of not finding every last usability problem in our designs.</p>

<p>We were able to conduct four usability studies over a period of two weeks during which we tested the interface at various stages of design. We used the following sequence of studies:</p>

<ol>

<li>Card sorting to discover categories (4 users)</li>

<li>Icon intuitiveness testing (4 users)</li>

<li>Card distribution to icons (4 users)</li>

<li>Thinking aloud walkthrough of page mock-up (3 users)</li>

</ol>

<p>The participants in the last two tests were also asked for ratings of icon aesthetics. Note that we used different users in each of the four studies in order to avoid any learning effects.</p>

<h3>Card Sorting</h3>

<p><a href="/articles/card-sorting-how-many-users-to-test/">Card sorting</a> is a common usability technique that is often used to discover users' mental model of an information space. A typical application is to get ideas for menu structures by asking users to sort cards with the command names: commands that get sorted together often should probably be in the same menu. A downside of the method is that users may not always have optimal models, and card sorting (or other similarity measures) is often used to assess the difference between the way novice and expert users understand a system.</p>

<p>Before our card sorting study, the SunWeb development group had brainstormed about possible information services to be provided over the system, resulting in a list of 51 types of information. We wrote the name of each of these services on a 3-by-4 inch notecard. In a few cases we also wrote a one-line explanation on the card.</p>

<p>Before each user entered the lab, the cards were scattered around the desk in random order. The users were asked to sit down at a table and sort the cards into piles according to similarity. Users were encouraged not to produce too small or too large piles but they were not requested to place any specific number of cards in each pile. After a user had sorted the cards into piles of similar cards, the user was asked to group the piles into larger groups that seemed to belong together and to invent a name for each group. These names were written on Post-It notes and placed on the table next to the groups. The users typically completed the entire process in about 30 minutes, though some took about 40 minutes.</p>

<p>The data from this study was lists of named groups of cards with subgroups corresponding to the original piles. Based on this information, it is possible to calculate similarity ratings for the various concepts by giving a pair of concepts one similarity point for each time both concepts occur in the same larger cluster and two points for each time they occur in the same pile. This similarity matrix can then be fed to one of the many standard statistics packages for a cluster analysis. It is also possible to use other statistical techniques such as multidimensional scaling.</p>

<p>We actually computed a statistical cluster analysis at the end of the project, but we initially did not have time to code the data appropriately, so our design was based on "data eyeballing" and not on formal statistics. Given our discount usability engineering approach with only four users, the statistical methods are not that reliable anyway but, as it turned out, the statistical cluster analysis was very similar to that we had constructed manually. For our manual clustering, we worked bottom- up and initially grouped concepts that most users had sorted together. We then expanded these small groups into larger clusters by adding concepts that some users had sorted with most of the concepts in the group if the grouping made sense to us. This subjective interpretation of the data is dubious if the objective "truth" is desired, but in our case we were after a coherent design, so we felt justified in applying our judgment in those cases where the user data was too sparse for a clear conclusion to be drawn on the basis of the numbers. Eyeballing the data took one person about two hours and resulted in a list of recommended groups of features as well as initial names for the groups. The names were often inspired by the labels provided by the users, but due to the verbal disagreement phenomenon [Furnas et al. 1987], the users obviously had not used exactly the same terms, so we also had to apply our judgment in choosing appropriate names.</p>

<h3>Icon Intuitiveness</h3>

<p>Based on the results from the card sorting study, we defined fifteen first-level groupings of the information in SunWeb and designed icons for each of them for use on the home page. The icons would be presented with labels to enhance users' ability to understand. Even so, we wanted to make the icons themselves as understandable as possible, and in order to achieve this goal we conducted an icon intuitiveness study where four users were shown the icons without labels and asked to tell us what they thought each icon was supposed to represent.</p>

<table border="1">

<caption align="bottom"><strong>Table 1. </strong> <em> Results of icon intuitiveness study with four users (some users gave more than one interpretation of some icons). </em></caption>

<tbody>

<tr valign="middle">

<td><img alt="" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/icon_globe.gif" style="width: 76px; height: 48px;"/></td>

<td><em>Intended Meaning: </em> Geographic view of the company (branch offices in different locations).</td>

<td><em>Test Users' Interpretations: </em> World, global view, planet, the world, Earth.</td>

</tr>

<tr valign="middle">

<td><img alt="Money bag icon" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/icon_benefits.gif" style="width: 76px; height: 48px;"/></td>

<td><em>Intended Meaning: </em> Benefits.</td>

<td><em>Test Users' Interpretations: </em> Health field, money, health care is expensive, Clinton's health plan, hospital, don't know, benefits.</td>

</tr>

<tr valign="middle">

<td><img alt="TV icon" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/icon_tv.gif" style="width: 76px; height: 48px;"/></td>

<td><em>Intended Meaning: </em> Public relations (TV with commercial).</td>

<td><em>Test Users' Interpretations: </em> TV set, video, TV, TV, TV.</td>

</tr>

<tr valign="middle">

<td><img alt="computer and disc icon" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/icon_productcatalog.gif" style="width: 76px; height: 48px;"/></td>

<td><em>Intended Meaning: </em> Product catalog.</td>

<td><em>Test Users' Interpretations: </em> System oriented, disk, CD, Computer, CD-ROM, CD-ROM.</td>

</tr>

<tr valign="middle">

<td><img alt="briefcase icon" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/icon_toolbox1.gif" style="width: 76px; height: 48px;"/></td>

<td><em>Intended Meaning: </em> Specialized tools (toolbox).</td>

<td><em>Test Users' Interpretations: </em> Briefcase, personal info, briefcase, toolbox, briefcase.</td>

</tr>

<tr valign="middle">

<td><img alt="bulletin board icon" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/icon_bulletinboard.gif" style="width: 76px; height: 48px;"/></td>

<td><em>Intended Meaning: </em> What's new (bulletin board).</td>

<td><em>Test Users' Interpretations: </em> Bulletin board, bulletin board, bulletin board, laundry.</td>

</tr>

<tr valign="middle">

<td><img alt="globe with lines overlay icon" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/icon_www1.gif" style="width: 76px; height: 48px;"/></td>

<td><em>Intended Meaning: </em> World Wide Web.</td>

<td><em>Test Users' Interpretations: </em> Networking on a world scale, map, location, dimensions of the planet, networking around the world, geography, global.</td>

</tr>

</tbody>

</table>

<p>Table 1 shows the results of the icon intuitiveness testing for some of our initial icons. Some icons passed the test easily, with most users either guessing the intended meaning or at least guessing something that was very close and would not be misleading in the context of the full system. For example, only one user explicitly used the word "benefits" to describe our "employee benefits" icon, but descriptions like "hospital" and "Clinton's health plan" actually show that people got the general idea. In cases like this, we were satisfied that users would understand the icon when it was combined with its label in the full system, so we did not feel a need to change it, especially given that we had planned several additional user tests that would reveal any hidden problems. A minor adjustment was made to reduce the emphasis on the money bag.</p>

<p>In other cases, users did not get exactly the correct meaning of an icon but we decided to keep it anyway. The product catalog was one such example, because the CD-ROM component of the icon was so visually powerful that most users focused on it and not on the group of system components. The underlying problem is that software is an abstract concept that is difficult to visualize. In another icon we tried to show "software" by a code listing but that also proved difficult for users to recognize. Our final decision was to keep the product catalog icon since users did recognize its components. In the final design (see Figure 4), we made the workstation screen more visually prominent by giving it a more saturated color.</p>

<p>With respect to the "what's new" bulletin board, one user claimed that it looked like laundry. Even so, three of the four users recognized the icon immediately and we decided to keep it. When conducting user testing with a small number of users it is important not to let results from individual users influence one's decisions unduly. Seen from one perspective, 25% of our sample had trouble with the icon, but seen from another (and more appropriate) perspective, we happened to have asked a person who did not recognize the icon. When designing based on small samples of test users, one has to apply judgment based on general usability principles and one's experience with interaction principles since the data itself is too sparse to use without interpretation.</p>

<p>The toolbox icon was seen by most users as a briefcase. Since briefcases have completely different connotations, this icon would have been misleading to users and we decided to redesign the it by adding a monkey wrench to emphasize the "tool" aspect. Finally, the World Wide Web icon was reasonable: some users got it almost exactly right by guessing "networking on a world scale" or some such, but many of the interpretations had to do with geography or the globe. Since we already had a globe icon to signify geography, these erroneous interpretations of the WWW icon were problematic and we decided to redesign with more emphasis on the network. We also replaced the globe with a flat map to distinguish the WWW icon further from the geography icon.</p>

<h3>Card Distribution to Icons (a Variant of Closed Card Sorting)</h3>

<p>After a redesign of those icons that tested poorly in the intuitiveness test, we proceeded to test whether users would associate the correct concepts with each of the groups we had defined. For this test, we mocked up a table in our usability laboratory as a large-scale version of the eventual home page design, as shown in Figure 1. We had printed out large magnifications of the icons on a color printer and placed them on the desk in an approximation of the layout we had planned for the SunWeb home page. Even though the desk was several times larger than a typical workstation window, we only printed the icons at 200% magnification since this size (four times the area of screen icons) were large enough to be seen from a distance, whereas larger icons seemed strange. We tested the icons both with and without labels, but we would recommend including the labels in future testing since we did not learn that much more from removing the labels than we had already learned in the icon intuitiveness study.</p>

<p><img alt="Usability Lab photo" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/user_testing.gif" style="width: 499px; height: 418px;"/></p>

<p><strong>Figure 1. </strong> <em> Card distribution to icons in the usability laboratory. In preparation for the test, the icons were printed out in 200% magnification on a color printer and Post-It tape was used to divide the table into areas for each icon. For the test, the user is given a pile of cards and asked to place each card in the area with the most appropriate icon. An observer is in the room with the user to give instructions and take notes. Other observers can watch though the one-way mirror and the session is also videotaped in case further analysis is necessary later.<br/>

[Note added <strong> 2013</strong>: Why does this photo look so bad? Because it was digitized in 1994 and we needed to keep it within a "safe" color space of 50 colors to avoid flicker on the lower-end range of Sun workstations at the time.] </em></p>

<p>We used Post-It(TM) tape to divide the desk into areas for each icon, and each of test user was then asked to distribute the cards among these areas, with each card going to the (labelled) icon most appropriate for it. At the end of the card distribution test, the users were asked to comment on the aesthetics of the icons and to list the icons they liked the most and disliked the most. Figure 1 shows the lab setup during the card distribution test. The card distribution tests took about fifteen minutes per user.</p>

<h3>Thinking Aloud Page Walkthrough</h3>

<p>For our final usability test, we printed out a magnified color screendump of our design for the SunWeb home page. We wanted to test a <a href="http://www.nngroup.com/reports/paper-prototyping-training-video/" title="Nielsen Norman Group: Paper Prototyping, A How-To Video (32 minute film)"> paper version</a> instead of a screen version to avoid the problem of users clicking on buttons that at that time had no effect. The test users were asked to point to each button and think aloud what information they thought would be accessed through that button. At the end of the page walkthrough, the users were asked to comment on the aesthetics of the icons and to list the icons they liked the most and disliked the most.</p>

<p>The card distribution and page walkthrough studies revealed several usability problems in our revised design, leading to additional design changes before we could release the SunWeb user interface. One of these new usability problems is discussed in further detail in the following section. In retrospect, though, we feel that we learned the most from the first two studies, the card sorting and the icon intuitiveness study. In general, we will always recommend thinking aloud studies where users perform tasks with the full user interface, but in the special case where the command structure and interaction techniques are determined by the World Wide Web viewer it was more important to study the information structure that we could actually influence.</p>

<p>Asking users for subjective ratings of icon aesthetics proved to be useful. Even though people have different taste and liked and disliked different icons, there were two icons that were singled out for criticism by most users: a blackboard we had used to represent education and the TV icon we had used to represent sales, marketing, and PR. Users had no trouble recognizing the TV (see Table 1) and most users easily understood that it represented promotional materials (though only a few of them recognized it as showing a "Sun TV commercial," which was one of the services that we planned to make available through SunWeb's multimedia features). Users just did not like it.</p>

<p>Since subjective satisfaction is at least as important as task performance for a system like SunWeb where we want to encourage people to browse and learn more about their company, we removed these most hated icons and replaced them with more attractive ones. The blackboard was replaced with a graduation cap and a diploma to represent education, and the TV set was replaced with a spotlight to represent promotional materials. Even though the American-style graduation cap is problematic from an international use perspective (not all countries use these caps), we decided to use it for this system because it is intended for internal use in Sun which is a company where most employees understand English and basic aspects of American culture.</p>

<h2 id="toc-iterative-design-3">Iterative Design</h2>

<p>The SunWeb user interface was developed by iterative design, meaning that new versions of the interface were designed each time we discovered a weakness in its usability. We often had to go through a large number of revisions since our "fixes" to the user interface sometimes turned out not to work. An example is shown in Figure 2. Actually, Figure 2 only shows the five main iterations that were tested with users. In total, we designed twenty versions of the icon: seven tool metaphor icons, nine shopping metaphor icons (including shopping carts and a grocery shelf), and four chest icons. In order to produce our many different designs, ideas were gleaned from a thesaurus, a visual dictionary, and catalogs of international signs and symbols.</p>

<p><img alt="briefcase icon" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/icon_toolbox1_.gif" style="width: 76px; height: 48px;"/> <img alt="toolbox with wrench icon" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/icon_toolbox2.gif" style="width: 76px; height: 48px;"/> <img alt="storefront icon" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/icon_storefront1.gif" style="width: 76px; height: 48px;"/> <img alt="alternative storefront icon" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/icon_storefront2.gif" style="width: 76px; height: 48px;"/> <img alt="chest icon" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/icon_chest.gif" style="width: 76px; height: 48px;"/></p>

<p><strong>Figure 2. </strong> <em> Five iterations of the icon to represent a group of special-purpose applications. The first two represent the toolbox metaphor, the next two are "application stores," and the last is the "application chest." </em></p>

<p>As mentioned earlier, the initial toolbox icon was interpreted as a briefcase by most users, so we opened it up and added a monkey wrench. This redesign worked and users in our card distribution study and page walkthroughs had no problems and users sorted a very large numbers of cards onto this icon with the comment that <cite> "oh, this is a tool." </cite> Essentially, almost any concept that represented an executable program was considered a tool. An example is the expense report application which should have been grouped with the travel icon but was often placed in the toolbox.</p>

<p>In order to use a weaker metaphor for the special-purpose applications, we next tried a shopping metaphor with an icon showing a storefront (the middle icon in Figure 2). When we conducted an icon intuitiveness study and showed this icon to a user, he immediately said <cite> "this is a circuit board." </cite> This user happened to be an engineer, but since we do have a very large number of engineers in the user population for SunWeb, we decided to take this comment seriously and redesigned the icon. This is an example where our judgment as user interface specialists was to rely on a result from a single user since we felt that this user's problems would be frequent in real use of the system.</p>

<p>We tried several alternative storefront and other shopping icons (see the fourth icon in Figure 2) before realizing that a successful shopping icon would interfere with one of our other interface elements: the "product catalog" icon. Therefore, we dropped the application store as the metaphor and we finally settled on the "application chest" icon shown as the last icon in Figure 2.</p>

<h2 id="toc-unified-design-4">Unified Design</h2>

<p>To make SunWeb both usable and aesthetically pleasing, basic visual design techniques were applied to graphic elements. A consistent visual design also provided the necessary orientation cues and navigational controls critically needed by users. Applying the same techniques consistently provided users with a predictable location for information and controls on every page of SunWeb. This reinforced user expectations across the entire system of SunWeb, thus enhancing satisfaction and usability.</p>

<p><img alt="Screenshot of two levels of navigation bars" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/sunweb_header.gif" style="width: 468px; height: 224px;"/></p>

<p><strong>Figure 3. </strong> <em> SunWeb main homepage masthead (top) and second level masthead (below). </em></p>

<p>A systematic design solution was needed to provide page identification and access to essential controls, and this was accomplished by developing "banners" (see Figure 3). Present at the top of every SunWeb page, the banners provide a category of essential global controls, including Search, Overview, and Help (C). The vast scope of information included in SunWeb required a Search engine as a prerequisite from the initial functional specification stage. An Overview in the form of a comprehensive content list was also deemed necessary. These buttons were rendered in a somewhat subdued grey, so as not to compete or overpower the other elements on the page. The subdued uniformity also visually separates functionality from the more colorful category icons found on the home page. The SunWeb identifier mark (A) is consistently located on the left half of the banner. This logotype area provides SunWeb the necessary visual distinction from the "look" of Suns' external public server. This area also functions as the link mechanism back to the main SunWeb homepage from anywhere in the system, and is reinforced by a descriptive label. On second level banners, the paging buttons (D) are highlighted when available to allow users paging capability through a series of information, for example, the homepages of members of a certain engineering team, or pages in a product catalog. This avoids the back-next selection cycle, a tedious routine for users if numerous categories of information are available. The 15 different categories of SunWeb information represented by icons are integral second level banner components (B). These icons embedded in the banner function as direct links back to that particular category homepage. In SunWeb, these 15 categories may be thought of as major "hubs," as found in airline route systems, and provide the major arteries through the information space. The ability for users to quickly return to these central homepages was a crucial navigational feature. By clicking on the icon, the user will immediately link to that category homepage, no matter how removed the user may currently be from the second level. The banner icons also function as location cues for user position within SunWeb.</p>

<p>In order to facilitate consistency among contributors to SunWeb, banner components were placed in a central repository, and usage encouraged by the development team. Although not mandated to adopt the banner gif files or adhere to a particular design, many content contributors felt it necessary to "fit-in", and wished to appear consistent with the rest of the top-level SunWeb environment. In this instance, a suitable design solution "given away" provided the initial momentum for widespread exposure and adoption. Banner specification drawings helped to clarify the design, and insured proper implementation. These drawings were distributed in hard copy during the development phase meetings to the various content providers.</p>

<p>As with the icons, the SunWeb banners relied on a minimal color palette in order to reduce the possibility of color-map flashing and unpredictable results. This also would reserve more color space for the content providers, who may feel it necessary to include an undetermined amount of continuous tone photographs, color illustrations and charts, etc., into their SunWeb pages. Subsets from a 64 color palette were adopted for all graphic elements in SunWeb. This would insure hue saturation, intensity, and value consistency across components.</p>

<p><img alt="Screenshot of final intranet homepage launched 1994" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/31/sunweb_final_homepage.gif" style="width: 564px; height: 518px;"/></p>

<p><strong>Figure 4. </strong> <em> The final home page design for SunWeb. Icons sharing design attributes, such as frontal orientation and color palette, insures a visual continuity across the image ensemble. Each icon occupies a similar amount of space within the button graphic, so as to equalize image density. Pre-defined colors are used throughout the icon imagery which represents the 15 major categories of information provided by SunWeb. This provides the necessary visual contrast with the global icon controls in the SunWeb banner, which visually remain monochromatic. Grouping and placement of the categories on the page reflects a hierarchy based on related topics and information precedence. Higher priority information is placed at the top, while categories of lesser importance towards the bottom. It is interesting to note that first iteration of the homepage design presented each icon as a separate graphic ismap. However, due to the length of time required by Mosaic to load each individual image, one at a time, the homepage was redesigned as one large ismap containing all button categories. This dramatically reduced access time for users. Textual labels in the smallest font available was positioned below the ismap (not shown), in case users turn off the load picture functionality. A design should always take into account users who are concerned with speed of access, and therefore prefer not to load any of the graphic gif files. </em></p>

<h2 id="toc-references-5">References</h2>

<p>Furnas, G. W., Landauer, T. K., Gomez, L. M., and Dumais, S. T. (1987). The vocabulary problem in human-system communication. <em> Communications of the ACM </em> <strong> 30 </strong> , 11 (November), 964-971.</p>

<p>Mullet, Kevin, and Sano, Darrell (1994). <a href="http://www.amazon.com/exec/obidos/ISBN=0133033899/ref=nosim/useitcomusableinA/"> <em> Designing Visual Interfaces: Communication Oriented Techniques</em></a>. Sun Microsystems Press/Prentice Hall, New Jersey.</p>

<p>Nielsen, J. (1994). <em> <a href="http://www.nngroup.com/books/usability-engineering/"> Usability Engineering</a></em>, paperback edition. Academic Press, Boston.</p>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<div class="sidebar-item related-courses">

<h2 class="article-heading-small">Related Courses</h2>

<ul>

<li>

<a class="tile ga-article-related-course" data-course-title="Information Architecture" href="/courses/information-architecture/?lm=1994-design-sunweb-sun-microsystems-intranet&amp;pt=article">

<h4 class="title heading-small">Information Architecture</h4>

<p id="information-architecture" class="description body-small">

Organize and structure information to improve findability and discoverability

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

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Information Architecture,Intranets,Navigation,iterative design</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Information Architecture</span>

<a class="ga-article-related-topic" href="/topic/information-architecture/">Information Architecture</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/intranets/">Intranets</a>

</li>

<li>

<a class="ga-article-related-topic" href="/topic/navigation/">Navigation</a>

</li>

</ul>

</div>

</div>

</div>

</div>