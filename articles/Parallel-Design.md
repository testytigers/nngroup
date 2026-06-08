# Parallel Design and Testing by Jakob Nielsen and Jan Maurits Faber - NN/G

<span id="gaDataLength" class="ga-data-layer" aria-hidden="true">16</span>

<div class="article-header">

<h1 class="article-h1">Improving System Usability Through Parallel Design</h1>

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

February 1, 1996

<span id="gaDataPubDate" class="ga-data-layer" aria-hidden="true">1996-02-01</span>

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

<a class="ga-share-email" target="_blank" href="mailto:?subject=NN/g Article: Improving System Usability Through Parallel Design&amp;body=https://www.nngroup.com/articles/parallel-design/" data-share-type="Email">

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

<a class="ga-share-linkedin" target="_blank" href="http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.nngroup.com/articles/parallel-design/&amp;title=Improving System Usability Through Parallel Design&amp;source=Nielsen%20Norman%20Group" data-share-type="LinkedIn">

<svg fill="none" aria-hidden="true" width="24" class="icon" viewBox="1 0 23 23" xmlns="http://www.w3.org/2000/svg">

<use href="#icon-social-linkedin" />

</svg>

Share on LinkedIn

</a>

</li>

<li class="body-medium">

<a class="ga-share-twitter" target="_blank" href="https://twitter.com/intent/tweet?url=http://www.nngroup.com/articles/parallel-design/&amp;text=Improving System Usability Through Parallel Design&amp;via=nngroup" data-share-type="Twitter">

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

</span>In parallel design multiple designers independently of each other design suggest user interfaces. These interfaces are then merged to a unified design. In a case study, measured usability from version 1 to version 2 was improved by 18% when using traditional iterative design and by 70% when using parallel design.

</div>

<div class="article-body">

<p>

Paper by <a href="/people/jakob-nielsen/" title="Author biography"> Jakob Nielsen</a> and Jan Maurits Faber  <br/>

<em>Originally published in <cite> IEEE Computer </cite> <strong> Vol. 29 </strong> , No. 2 (February 1996), pp. 29-35. </em></p>

<h3>

Introduction</h3>

<p>

Companies are shortening software project schedules to introduce products more rapidly than competitors. At the same time, customers are demanding higher usability. Unfortunately, the goals of increased usability and decreased development time conflict with traditional usability engineering approaches.</p>

<p>

The design process always requires several rounds where interfaces confront users' needs and capabilities and are modified accordingly. This approach is called <a href="http://nngroup.com/articles/iterative-design/" title="Jakob Nielsen: case studies of four iterative design projects"> iterative design</a>. <sup> [Ref. 1] </sup> Our experience indicates the need for at least two iterations, yielding three versions, before the product is good enough for release. However, three or more iterations are better.</p>

<p>

Unfortunately, testing and redesigning take time, thus delaying product release. Because major delays are intolerable, much effort has gone into improving user interface design efficiency, prototyping, and evaluation. This has led to a cheaper and faster approach called <a href="/articles/guerrilla-hci/"> discount usability engineering</a>. <sup> [Ref. 2] </sup> However, even discount usability engineering relies on traditional linear iteration. To yield final designs faster, we want parts of the usability engineering life cycle to take place at the same time, in a process we call parallel user interface design.</p>

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

<a class="ga-article-toc-item" href="#toc-parallel-design-vs-iterative-design-1">

Parallel Design vs. Iterative Design</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-case-study-2">

Case Study</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-parallel-design-stage-3">

Parallel Design Stage</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-merged-design-stage-4">

Merged Design Stage</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-comparing-test-results-5">

Comparing Test Results</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-independent-iterative-design-6">

Independent Iterative Design</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-cost-accounting-7">

Cost Accounting</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-diversified-parallel-design-8">

Diversified Parallel Design</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-deviations-from-recommended-practice-9">

Deviations From Recommended Practice</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-conclusion-10">

Conclusion</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-acknowledgments-11">

Acknowledgments</a>

</li>

<li class="article-table-of-content">

<a class="ga-article-toc-item" href="#toc-references-12">

References</a>

</li>

</ul>

</div>

</div><h2 id="toc-parallel-design-vs-iterative-design-1">

Parallel Design vs. Iterative Design</h2>

<p>

Figure 1 shows the parallel design project model. Both iterative and parallel design are based on a version 0 concept, which describes generally what the interface is supposed to do. Parallel design speeds up time-to-market by exploring design alternatives simultaneously. The initial parallel design versions, denoted 1.a, 1.b, 1.c, and 1.d in Figure 1, do not have to be fully implemented. Merged version 2, based on each designer's best ideas, is the first to be implemented and tested.</p>

<p>

<img alt="Parallel design process, starting at the bottom and working up for improved designs" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/30/fig1.gif" style="width: 500px; height: 352px; "/></p>

<p>

<br/>

<strong>Figure 1. </strong> <em> Recommended parallel design project model. Note that this article's case study followed Figure 3's slightly different project model. </em></p>

<p>

Each merged design element can be the best of the parallel versions' corresponding elements or a synthesis of several parallel versions' elements. The merging designer can also introduce new elements, although it is probably better to postpone the introduction of most new elements until the iterative part of the parallel process, which begins with version 3.</p>

<p>

A weakness of parallel design is the waste of resources when several designers do the same work, even though some design ideas will not be used. Because of this, we do not recommend final polishing of parallel design versions. A skilled designer can often produce reasonable design descriptions in less than a day. For very large and complicated systems, more time is needed. But it may be possible to concentrate initial parallel design efforts on a subset of the total system to explore alternatives without fully designing the interface.</p>

<p>

Parallel design's basic trade-off is that more staff work is invested up front in order to spend less time exploring design revisions. Therefore, parallel design is best suited for projects where reduced time-to-market is essential and makes the up-front investment acceptable. For projects where cost savings are more important than early release, traditional iterative design is preferable.</p>

<p>

Some readers may object to parallel design, calling it design by committee. Indeed, as far back as the year 959, the Viking Olaf the Peacock said, "I want only the shrewdest to decide; in my opinion the council of fools is all the more dangerous the more of them there are." <sup> [Ref. 3] </sup> To make parallel design work best, designers should work independently and promote their ideas without the type of compromises that lead to the camel that is a horse designed by committee. The merged design can draw upon their best ideas but should not be beholden to any designer nor necessarily include ideas from all designs.</p>

<h2 id="toc-case-study-2">

Case Study</h2>

<p>

In our previous projects, we found that parallel designs were excellent for exploring design options. <sup> [Ref. 4] </sup> However, we did not collect metrics for the resulting designs' usability or the method's impact on shipment schedule or on the need for future revisions. Therefore, we conducted a study that implemented all designs and subjected them to traditional, controlled-usability measurements, even though this involved considerable resource expenditure that could be justified only for research purposes.</p>

<p>

The case study concerned screen-based user interfaces to advanced telephone services like call forwarding, where incoming calls are routed to another telephone, and call waiting, where you are notified if somebody calls while you are on the line. Instead of using a screen-based telephone, we simulated this type of telephone on a personal computer, as shown in Figure 2. Using simulation was more flexible than using the telephone network and allowed faster implementation of alternative designs.</p>

<p>

<img alt="Picture of a smartphone" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/30/fig2.gif" style="width: 386px; height: 556px; "/><br/>

</p>

<p>

<strong>Figure 2. </strong> <em> Software mock-up of a screen-based advanced telephone service interface. The user would operate this interface by clicking on button images with a mouse. In this example, the user has selected call forwarding from the main menu and is entering the number to which calls should be forwarded. </em></p>

<p>

Our software mock-up was patterned after realistic telephone hardware, using a small set of buttons and an alphanumeric screen with 16 40-character lines. Of course, test users could not place calls using the simulated telephone, but that was not a problem because our project concerned only features used to dial and set up calls, not the calls themselves. Also, we could easily use a computer to generate a log file with exact user-action timings.</p>

<p>

For our parallel design project, we first defined a functional specification for the interface, which was easy, as our functionality was that offered by the telephone network. For most projects, though, task analysis and customer field visits would be needed for the specification stage. We defined a set of 16 user test tasks. One task was, "You are waiting for an important business call from 758-2307 or 758-2257. However, you are going to your neighbor's house for a while. Arrange it so that calls from either business number will go to your neighbor's house, but other calls will ring at your house. Your neighbor's phone number is 201-4232." We defined measured usability to be a function of how well our test users performed these tasks.</p>

<h2 id="toc-parallel-design-stage-3">

Parallel Design Stage</h2>

<p>

Figure 3 shows our project model. Four user-interface designers took part in our parallel design stage. We chose this number of designers based on earlier experience with projects where three designers were used with great success <sup> [Ref. 4] </sup> but where more designers would have improved results. We do not claim that four is the optimal number of designers for all projects.</p>

<p>

<img alt="Design process for this research study (not recommended for commercial projects)." loading="lazy" src="//media.nngroup.com/media/editor/2012/10/30/fig3.gif" style="width: 500px; height: 311px; "/></p>

<p>

<br/>

<strong>Figure 3. </strong> <em> The project model used in the case study. For practical projects, we recommend the model in Figure 1. </em></p>

<p>

Our four designers worked independently and had access only to their own designs. Each designer was first given the desired functionality's specification and the equipment's limitations. Each then designed a user interface and described it to a research assistant, who implemented it. To save time, the designers provided their specifications in a mixture of natural language and hand-drawn screen layouts. To reduce the possibility that the research assistant misinterpreted the designer's intentions, the assistant showed the designer the interface's running version. Designers were asked not to engage in iterative design at this stage but only to identify and correct disparities between the implemented design and their original intentions.</p>

<p>

<the> <img alt="Four different version one designs" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/30/fig4.gif" style="width: 600px; height: 565px; "/> </the></p>

<p>

<the><br/>

<strong>Figure 4. </strong> <em> The initial screens from each of the four parallel designs. Top: versions 1.a and 1.b. Bottom: versions 1.c and 1.d. For the user tests, each screen was displayed as part of the simulated telephone interface in Figure 2. </em> </the></p>

<h3>

User Testing</h3>

<p>

Each version was tested with 10 people who were timed performing the 16 test tasks. To keep performance from being affected by skills learned during earlier tests, rather than version usability, no person was used more than once. The designers were then given only their own test results and were told to modify their designs. Thus, their redesigns, versions 2.a-d, correspond to traditional iterative design and were produced only to compare iterative and parallel design.</p>

<p>

We measured the time it took to perform the 16 test tasks and the number of times the user completed a task incorrectly and was told to try again. Task time is the classic usability metric. The number of errors was especially important to us because people generally use telephones without assistance.</p>

<p>

To assess relative usability changes, we normalized the raw test results so that the overall usability score derived from the average task time and average error rate for all four designs would be 100. Improvements yielded higher scores. Overall usability was calculated as the geometric mean of the normalized scores for task time and number of errors, because this emphasized improved and reduced usability equally.</p>

<p>

Test results for the initial parallel versions and their iterative design revisions are shown in Table 1. For the four designs, the usability improvement after one iteration ranged from 12 to 29 percent and averaged 18 percent. This was less than expected from our earlier survey, <sup> [Ref. 1] </sup> where iterative design improvement averaged 38 percent per iteration. However, the results were still within expected values, given that two projects in the earlier survey had improvements of 17 and 19 percent per iteration.</p>

<p>

</p>

<table border="1">

<caption align="bottom">

<strong>Table 1. </strong> <em> Measured usability for the four initial parallel designs and for the redesigned versions produced by the initial designers. </em></caption>

<tbody>

<tr>

<th align="LEFT" valign="top">

<font color="purple">Version </font></th>

<th align="CENTER" valign="top">

<font color="purple"><b>Task time in minutes </b> </font></th>

<th align="CENTER" valign="top">

<font color="purple"><b>Normalized task time </b> </font></th>

<th align="CENTER" valign="top">

<font color="purple"><b>Errors per task </b> </font></th>

<th align="CENTER" valign="top">

<font color="purple"><b>Normalized errors </b> </font></th>

<th align="CENTER" valign="top">

<font color="purple"><b>Overall usability </b> </font></th>

</tr>

<tr>

<td align="LEFT" valign="top">

<font color="purple">1.a </font></td>

<td align="CENTER" valign="top">

<font color="purple">27 </font></td>

<td align="CENTER" valign="top">

<font color="purple">106 </font></td>

<td align="CENTER" valign="top">

<font color="purple">1.4 </font></td>

<td align="CENTER" valign="top">

<font color="purple">176 </font></td>

<td align="CENTER" valign="top">

<font color="purple"><b>136 </b> </font></td>

</tr>

<tr>

<td align="LEFT" valign="top">

<font color="purple">1.b </font></td>

<td align="CENTER" valign="top">

<font color="purple">41 </font></td>

<td align="CENTER" valign="top">

<font color="purple">70 </font></td>

<td align="CENTER" valign="top">

<font color="purple">3.3 </font></td>

<td align="CENTER" valign="top">

<font color="purple">75 </font></td>

<td align="CENTER" valign="top">

<font color="purple"><b>73 </b> </font></td>

</tr>

<tr>

<td align="LEFT" valign="top">

<font color="purple">1.c </font></td>

<td align="CENTER" valign="top">

<font color="purple">25 </font></td>

<td align="CENTER" valign="top">

<font color="purple">116 </font></td>

<td align="CENTER" valign="top">

<font color="purple">2.8 </font></td>

<td align="CENTER" valign="top">

<font color="purple">88 </font></td>

<td align="CENTER" valign="top">

<font color="purple"><b>101 </b> </font></td>

</tr>

<tr>

<td align="LEFT" valign="top">

<font color="purple">1.d </font></td>

<td align="CENTER" valign="top">

<font color="purple">26 </font></td>

<td align="CENTER" valign="top">

<font color="purple">110 </font></td>

<td align="CENTER" valign="top">

<font color="purple">2.7 </font></td>

<td align="CENTER" valign="top">

<font color="purple">91 </font></td>

<td align="CENTER" valign="top">

<font color="purple"><b>100 </b> </font></td>

</tr>

<tr style="background-color: #ccffff">

<td align="LEFT" valign="top">

<font color="purple">1 average </font></td>

<td align="CENTER" valign="top">

<font color="purple">29 </font></td>

<td align="CENTER" valign="top">

<font color="purple">99 </font></td>

<td align="CENTER" valign="top">

<font color="purple">2.4 </font></td>

<td align="CENTER" valign="top">

<font color="purple">101 </font></td>

<td align="CENTER" valign="top">

<font color="purple"><b>100 </b> </font></td>

</tr>

<tr>

<td align="LEFT" valign="top">

<font color="purple">2.a </font></td>

<td align="CENTER" valign="top">

<font color="purple">24 </font></td>

<td align="CENTER" valign="top">

<font color="purple">118 </font></td>

<td align="CENTER" valign="top">

<font color="purple">1.2 </font></td>

<td align="CENTER" valign="top">

<font color="purple">205 </font></td>

<td align="CENTER" valign="top">

<font color="purple"><b>156 </b> </font></td>

</tr>

<tr>

<td align="LEFT" valign="top">

<font color="purple">2.b </font></td>

<td align="CENTER" valign="top">

<font color="purple">35 </font></td>

<td align="CENTER" valign="top">

<font color="purple">82 </font></td>

<td align="CENTER" valign="top">

<font color="purple">2.3 </font></td>

<td align="CENTER" valign="top">

<font color="purple">107 </font></td>

<td align="CENTER" valign="top">

<font color="purple"><b>94 </b> </font></td>

</tr>

<tr>

<td align="LEFT" valign="top">

<font color="purple">2.c </font></td>

<td align="CENTER" valign="top">

<font color="purple">25 </font></td>

<td align="CENTER" valign="top">

<font color="purple">116 </font></td>

<td align="CENTER" valign="top">

<font color="purple">2.0 </font></td>

<td align="CENTER" valign="top">

<font color="purple">123 </font></td>

<td align="CENTER" valign="top">

<font color="purple"><b>119 </b> </font></td>

</tr>

<tr>

<td align="LEFT" valign="top">

<font color="purple">2.d </font></td>

<td align="CENTER" valign="top">

<font color="purple">30 </font></td>

<td align="CENTER" valign="top">

<font color="purple">97 </font></td>

<td align="CENTER" valign="top">

<font color="purple">1.9 </font></td>

<td align="CENTER" valign="top">

<font color="purple">129 </font></td>

<td align="CENTER" valign="top">

<font color="purple"><b>112 </b> </font></td>

</tr>

<tr style="background-color: #ccffff">

<td align="LEFT" valign="top">

<font color="purple">2 average </font></td>

<td align="CENTER" valign="top">

<font color="purple">28 </font></td>

<td align="CENTER" valign="top">

<font color="purple">102 </font></td>

<td align="CENTER" valign="top">

<font color="purple">1.8 </font></td>

<td align="CENTER" valign="top">

<font color="purple">137 </font></td>

<td align="CENTER" valign="top">

<font color="purple"><b>118 </b> </font></td>

</tr>

</tbody>

</table>

<p>

Figure 5 shows the measured usability of the original designs and their respective redesigns connected by arrows. The longer arrows indicate greater improvements. We used a logarithmic scale to give equal prominence to relative improvements, the most reasonable indication of redesign skill. Thus, all redesigns that reduced user errors by the same percentage would have equally long arrows.</p>

<p>

<img alt="Improvements in measured usability from one round to the next" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/30/fig5.gif" style="width: 700px; height: 680px; "/><br/>

<strong>Figure 5. </strong> <em> Diagram showing the various designs' measured usability. Each circle indicates one design, and the placement of the circle shows that design's task time (how fast users were at using it) on the x-axis and its error rate on the y-axis (how many errors people made). Arrows connect iterative revisions of a design from one version to the next. Merged versions 2.x and 2.y were based on all four initial parallel versions, 1.a-d. </em></p>

<p>

Optimal usability is in Figure 5's lower left corner, and most of the arrows point there, indicating task time and error rate improvements. The main exception is version 2.d, where the error rate dropped substantially but the task time increased slightly, because the design's help system was too extensive. Figure 5 shows it was easier to reduce user error rates than to speed up task performance, which is consistent with our experience from other development projects.</p>

<h2 id="toc-merged-design-stage-4">

Merged Design Stage</h2>

<p>

Versions 2.x and 2.y represent the unifying step of the parallel design process. They are shown in Figure 5 with their subsequent iterative redesigns, versions 3.x and 3.y, and in Figure 6.</p>

<p>

<img alt="Merged Designs" loading="lazy" src="//media.nngroup.com/media/editor/2012/10/30/fig6.gif" style="width: 600px; height: 265px; "/><br/>

<strong>Figure 6. </strong> <em> Merged designs based on the initial parallel versions shown in Figure 4. Left: version 2.x, produced by a designer who was shown the initial designs but not their user test results. Right: version 2.y, produced by a designer who was shown the initial designs and their user test results. </em></p>

<p>

The designers of these merged versions did not participate in producing the original versions, but they were experienced user-interface professionals on about the same level as the four original designers. In other projects, one would often choose the most senior original designer to produce the merged design to avoid having to teach yet another designer about the project. A potential problem, though, is that some designers may become too enamored of their own ideas to fully appreciate competing designs. Under these circumstances, it is best to use senior designers and ask them to guard against bias.</p>

<p>

The two designers who produced our merged versions worked independently and were not shown each other's designs. Normally, we would use only a single designer in this step, but we used two to gather additional research data. Version 2.x's designer had access to the four original parallel designs, versions 1.a-d, but was not given user test results. Version 2.y's designer had the four original designs and the user test results. Neither was shown the original designers' redesigns, since those were done only for research purposes and were not part of the parallel design process.</p>

<p>

We did not give the designers of versions 2.x and 2.y any of the design rationale used in the initial versions, so we could keep their work as independent as possible for evaluation and comparison purposes. Normally, one would expect the designers of the merged versions to talk to the original designers. We expect that the availability of design rationale would help the designers of the merged versions make better decisions and make parallel design's relative performance even better than in our project. However, this would also entail additional time for discussions, meetings, and report writing.</p>

<h3>

User Testing</h3>

<p>

The two merged designs were subjected to the same user tests as the earlier versions. The designers then produced redesigns, and the resulting versions 3.x and 3.y were subjected to a final round of testing. The test results for versions 2.x, 2.y, 3.x, and 3.y are in Table 2. Versions 3.x and 3.y had very high measured usability and were on average 2.5 times better than the first versions. It is likely that further improvements could have been achieved by additional iterations, but we did not have resources for that.</p>

<p>

</p>

<table border="1">

<caption align="bottom">

<strong>Table 2. </strong> <em> Measured usability for the two merged designs that were based on the original four parallel designs and for the redesigns of the merged versions. </em></caption>

<tbody>

<tr>

<th align="CENTER" valign="top">

<font color="purple">Version </font></th>

<th align="CENTER" valign="top">

<font color="purple">Task time in minutes </font></th>

<th align="CENTER" valign="top">

<font color="purple">Normalized task time </font></th>

<th align="CENTER" valign="top">

<font color="purple">Errors per task </font></th>

<th align="CENTER" valign="top">

<font color="purple">Normalized errors </font></th>

<th>

<font color="purple">Overall usability </font></th>

</tr>

<tr>

<td align="LEFT" valign="top">

<font color="purple">2.x </font></td>

<td align="CENTER" valign="top">

<font color="purple">19 </font></td>

<td align="CENTER" valign="top">

<font color="purple">152 </font></td>

<td align="CENTER" valign="top">

<font color="purple">0.9 </font></td>

<td align="CENTER" valign="top">

<font color="purple">274 </font></td>

<td align="CENTER" valign="top">

<font color="purple"><b>204 </b> </font></td>

</tr>

<tr>

<td align="LEFT" valign="top">

<font color="purple">2.y </font></td>

<td align="CENTER" valign="top">

<font color="purple">23 </font></td>

<td align="CENTER" valign="top">

<font color="purple">124 </font></td>

<td align="CENTER" valign="top">

<font color="purple">1.5 </font></td>

<td align="CENTER" valign="top">

<font color="purple">164 </font></td>

<td align="CENTER" valign="top">

<font color="purple"><b>143 </b> </font></td>

</tr>

<tr style="background-color: #ccffff">

<td align="LEFT" valign="top">

<font color="purple">2 average </font></td>

<td align="CENTER" valign="top">

<font color="purple">21 </font></td>

<td align="CENTER" valign="top">

<font color="purple">137 </font></td>

<td align="CENTER" valign="top">

<font color="purple">1.2 </font></td>

<td align="CENTER" valign="top">

<font color="purple">212 </font></td>

<td align="CENTER" valign="top">

<font color="purple"><b>170 </b> </font></td>

</tr>

<tr>

<td align="LEFT" valign="top">

<font color="purple">3.x </font></td>

<td align="CENTER" valign="top">

<font color="purple">18 </font></td>

<td align="CENTER" valign="top">

<font color="purple">159 </font></td>

<td align="CENTER" valign="top">

<font color="purple">0.5 </font></td>

<td align="CENTER" valign="top">

<font color="purple">493 </font></td>

<td align="CENTER" valign="top">

<font color="purple"><b>280 </b> </font></td>

</tr>

<tr>

<td align="LEFT" valign="top">

<font color="purple">3.y </font></td>

<td align="CENTER" valign="top">

<font color="purple">20 </font></td>

<td align="CENTER" valign="top">

<font color="purple">147 </font></td>

<td align="CENTER" valign="top">

<font color="purple">0.7 </font></td>

<td align="CENTER" valign="top">

<font color="purple">352 </font></td>

<td align="CENTER" valign="top">

<font color="purple"><b>228 </b> </font></td>

</tr>

<tr style="background-color: #ccffff">

<td align="LEFT" valign="top">

<font color="purple">3 average </font></td>

<td align="CENTER" valign="top">

<font color="purple">19 </font></td>

<td align="CENTER" valign="top">

<font color="purple">153 </font></td>

<td align="CENTER" valign="top">

<font color="purple">0.6 </font></td>

<td align="CENTER" valign="top">

<font color="purple">417 </font></td>

<td align="CENTER" valign="top">

<font color="purple"><b>252 </b> </font></td>

</tr>

</tbody>

</table>

<p>

Version 2.x had higher measured usability than version 2.y, even though only version 2.y's designer had user test data. However, we do not have enough data to conclude that usability tests are unnecessary for the parallel process' merging step.</p>

<p>

Note that the designer who moved from version 2.y to 3.y had access to the initial parallel versions' test data and achieved substantial measured usability improvements. This designer compared version 2.y's test results with those from the four original versions and looked closely at the original designs that tested better for specific tasks. This let the designer target productive redesign areas and avoid a time-consuming reading of all four usability test reports.</p>

<h2 id="toc-comparing-test-results-5">

Comparing Test Results</h2>

<p>

Tables 1 and 2 show that version 2's average overall usability was 118 when designed by traditional iterative design and 170 when designed by merging four earlier parallel designs. Thus, parallel design was 44 percent better. During the next, iterative phase of the parallel design process, the measured usability improvement going from version 2.x to 3.x and from version 3.x to 3.y averaged 48 percent. This is in the expected range for improvements by iterative design, based on prior experience. <sup> [Ref. 1] </sup> Thus, parallel design did not sacrifice its improvement potential in later stages to achieve its usability boost in the merging stage.</p>

<p>

Another question is whether it's better to simply pick the single best design out of the original options and proceed with that one design and not bother with the "losing" designs. In our case study, version 1.a was the "winner" among the first-round designs (at a usability score of 136). Iterating solely on this design generates a usability score of 156 (for version 2.a), which is lower than the average score for the merged designs (170 points, or 9% better).</p>

<p>

Since our system mirrored the existing telephone system, we can compare our designs' usability with that of the existing system. Earlier studies <sup> [Ref. 5] </sup> showed that people had an average success rate of 61 percent the first time they used one of our system's 10 services on a traditional telephone, 84 percent when they used our parallel versions (1.a-d), and 95 percent when they used our merged versions (2.x and 2.y).</p>

<p>

The earlier study found that people who used these services for the first time on a screen-based telephone, instead of a traditional telephone, had a success rate of 75 percent. Since the screen-based telephone used in the earlier study had a much smaller screen (16 × 7 characters) than the one called for in our design (40 × 16 characters), it is not surprising that its measured usability was poorer than that found for our initial designs.</p>

<p>

We conclude that we had good initial parallel designs. They performed better than traditional telephones and screen-based telephones. Therefore, improvement by the merged versions cannot be attributed to initial design inferiority.</p>

<h2 id="toc-independent-iterative-design-6">

Independent Iterative Design</h2>

<p>

Even though usability improved significantly, one might hypothesize that this was due not to the parallel design method but to the fresh designers who worked on the merged versions. First, we do not believe these designers were better than the four parallel version designers. Also, we tried a project that introduced fresh designers at each stage, using a method we call independent iterative design. The results were miserable.</p>

<p>

The new designers in this project not only fixed the previous design's usability problems but also introduced new ideas. This caused a phenomenon we call design thrashing, where the design never became stable or polished. Each time the design changed direction, new problems were introduced, causing the overall design's measured usability to be no better than that of its predecessor. Thus, it is unlikely that our parallel design project's improvements were due simply to using fresh designers for the merged versions.</p>

<h2 id="toc-cost-accounting-7">

Cost Accounting</h2>

<p>

<strong>Table 3 </strong> shows cost estimates for the parallel design process' various stages. Fixed costs related to project start-up remain the same no matter how many versions are designed and tested, but variable costs are incurred for each version. The variable costs are larger for a first (1.a-d) or merged (2.x-y) version than for a revision (2.a-d and 3.x-y) because the designer, and subsequently the programmer, spend more time on initial design than on revision.</p>

<table border="1">

<caption align="bottom">

<strong>Table 3. </strong> <em> Parallel design project cost estimates, based on costs of $30 per hour for a research assistant (RA), $125 per hour for a usability professional (UP), and a flat fee of $20 for a user. </em></caption>

<tbody>

<tr style="background-color: #ccffff">

<th align="LEFT" valign="top">

<font color="purple">Fixed cost of project start-up </font></th>

<th align="RIGHT" valign="top">

<font color="purple">Cost </font></th>

</tr>

<tr>

<td align="LEFT" valign="top">

<font color="purple">Learning domain, writing specifications: 160 hours RA </font></td>

<td align="RIGHT" valign="top">

<font color="purple">$4,800 </font></td>

</tr>

<tr>

<td align="LEFT" valign="top">

<font color="purple">Constructing test tasks, preparing pilot tests: 40 hours RA </font></td>

<td align="RIGHT" valign="top">

<font color="purple">$1,200 </font></td>

</tr>

<tr>

<td align="LEFT" valign="top">

<font color="purple">Pilot testing, 3 hours RA + 3 users </font></td>

<td align="RIGHT" valign="top">

<font color="purple">$150 </font></td>

</tr>

<tr>

<td align="LEFT" valign="top">

<font color="purple"><b>Total </b> </font></td>

<td align="RIGHT" valign="top">

<font color="purple"><b>$6,150 </b> </font></td>

</tr>

<tr style="background-color: #ccffff">

<td align="LEFT" valign="top">

<font color="purple"><b>Variable cost per parallel or merged version </b> </font></td>

<td align="RIGHT" valign="top">

</td>

</tr>

<tr>

<td align="LEFT" valign="top">

<font color="purple">Design session, confirming implementation: 9 hours RA + UP </font></td>

<td align="RIGHT" valign="top">

<font color="purple">$1,395 </font></td>

</tr>

<tr>

<td align="LEFT" valign="top">

<font color="purple">Programming: 17 hours RA </font></td>

<td align="RIGHT" valign="top">

<font color="purple">$510 </font></td>

</tr>

<tr>

<td align="LEFT" valign="top">

<font color="purple">User testing: 20 hours RA + 10 users </font></td>

<td align="RIGHT" valign="top">

<font color="purple">$800 </font></td>

</tr>

<tr>

<td align="LEFT" valign="top">

<font color="purple">Writing test report: 6 hours RA </font></td>

<td align="RIGHT" valign="top">

<font color="purple">$180 </font></td>

</tr>

<tr>

<td align="LEFT" valign="top">

<font color="purple"><b>Total </b> </font></td>

<td align="RIGHT" valign="top">

<font color="purple"><b>$2,885 </b> </font></td>

</tr>

<tr style="background-color: #ccffff">

<td align="LEFT" valign="top">

<font color="purple"><b>Variable cost per iterative design version </b> </font></td>

<td align="RIGHT" valign="top">

</td>

</tr>

<tr>

<td align="LEFT" valign="top">

<font color="purple">Redesign session, confirming implementation: 5 hours RA + UP </font></td>

<td align="RIGHT" valign="top">

<font color="purple">$775 </font></td>

</tr>

<tr>

<td align="LEFT" valign="top">

<font color="purple">Programming: 9 hours RA </font></td>

<td align="RIGHT" valign="top">

<font color="purple">$270 </font></td>

</tr>

<tr>

<td align="LEFT" valign="top">

<font color="purple">User testing: 20 hours RA + 10 users </font></td>

<td align="RIGHT" valign="top">

<font color="purple">$800 </font></td>

</tr>

<tr>

<td align="LEFT" valign="top">

<font color="purple">Writing test report: 6 hours RA </font></td>

<td align="RIGHT" valign="top">

<font color="purple">$180 </font></td>

</tr>

<tr>

<td align="LEFT" valign="top">

<font color="purple"><b>Total </b> </font></td>

<td align="RIGHT" valign="top">

<font color="purple"><b>$2,025 </b> </font></td>

</tr>

</tbody>

</table>

<p>

</p>

<div style="border: solid thin #999999; background-color: #eeeeee; padding: 1ex">

Note added 2006: The numbers in the table were the ones that applied to phone company projects in 1996. Sadly, costs have gone up some for commercial usability projects over the last ten years. In particular, the <a href="http://www.nngroup.com/articles/recruiting-test-participants-for-usability-studies/" title="Alertbox: Recruiting Test Participants for Usability Studies"> cost per test user</a> is closer to $200 when you test a more targeted audience, as is typical for website research. These cost increases don't change our general conclusion, but do be prepared to pay a good deal more than indicated in the table.</div>

<p>

Our overall costs were slightly lower than the estimates for earlier iterative design projects, where the estimated fixed start-up costs ranged from $7,000 to $16,500 and the estimated variable costs for each version after the first ranged from $2,800 to $7,000. Although we are better at controlling costs now, they were lower primarily because this study's interface was smaller and simpler than the interfaces we usually work with.</p>

<p>

There is no doubt that parallel design is more expensive than standard iterative design. If we eliminate the cost of the additional versions we tested only for research purposes, we can calculate the two project models' costs as follows, for a design ending after version 3:</p>

<ul>

<li>

Traditional iterative design: $6,150 fixed costs + $2,885 variable costs for one initial version + $4,050 variable costs for two subsequent versions = $13,085.</li>

<li>

Parallel design: $6,150 fixed costs + $11,540 variable costs for four initial parallel versions + $2,885 variable costs for one merged version + $2,025 variable costs for one subsequent version = $22,600.</li>

</ul>

<p>

In our project, parallel design was 73 percent more expensive than iterative design. We still recommend parallel design because it achieves major usability improvements very fast. We don't know how usability would have improved if we had used iterative design and extended the iterative process. If we assume usability improvements of 18 percent per iteration, which was the average for our four initial designers, version 3's usability level would have been 139. This compares very poorly with the measured usability of 252 for the parallel process' version 3. An average of 6.6 versions, costing $20,375 and considerable time, would have been required for standard iterative design to reach a usability level of 252.</p>

<h2 id="toc-diversified-parallel-design-8">

Diversified Parallel Design</h2>

<p>

In a variant called diversified parallel design, each parallel-stage designer optimizes an interface for one specific platform or user group without considering other platforms or user groups that will have to be supported. For example, one designer can design a novice user interface, while another designs an expert user interface. This allows both designers to explore the design space more fully than if each had to work on an all-encompassing design. This also provides a refined set of ideas from which the eventual unified design will support all intended platforms and users.</p>

<h2 id="toc-deviations-from-recommended-practice-9">

Deviations From Recommended Practice</h2>

<p>

We had at least ten people take each test, even though we would normally recommend using no more than five, because <a href="http://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/" title="Alertbox: Why You Only Need to Test With 5 Users"> almost all interface usability problems can be found with 5 tests</a>. However, our project required many test users to get reasonably tight confidence intervals on our usability measures.</p>

<p>

Our test tasks and system functionality were fixed for all versions. Some development projects require constant specifications, but the product functionality definition normally changes as one learns more about product use. We had to keep our test tasks and product specifications constant to get comparable results from the testing of the various versions.</p>

<p>

Our parallel design phase deviated from what we would recommend. First, we would not ask each parallel designer to redesign without seeing other designers' versions. Thus, versions 2.a-d were produced only for research purposes. Generally, the merged version would be the only version 2. Second, we implemented all versions as complete running programs because we wanted to know exactly how long it took users to perform realistic tasks. It might normally be sufficient for exploration purposes to implement most early versions as low-fidelity prototypes.</p>

<h2 id="toc-conclusion-10">

Conclusion</h2>

<p>

Our case study supports the value of parallel design. It reflects one possible use of the method, which would probably be even more successful for traditional graphical user interfaces with more design space.</p>

<p>

Parallel design is more expensive than traditional iterative design, but it explores the design space in less time. In our case study, the improvement in measured usability from version 1 to 2 was 18 percent with traditional iterative design and 70 percent with parallel design. Since parallel design is more expensive, we cannot recommend it for all projects, but it has value when time-to-market is of the essence.</p>

<h2 id="toc-acknowledgments-11">

Acknowledgments</h2>

<p>

This work was done while the authors were with Bellcore's Applied Research area. The authors thank Sheila Borack for substantial help in scheduling subjects and for other matters related to running experiments. We thank Richard Herring for letting us reuse his task descriptions for user testing of advanced telephone services. We also benefited from George Furnas' helpful comments on a previous version of this article. Finally, we especially thank the six Bellcore user-interface designers who spent significant time designing and redesigning our interface. Since these people were, in some sense, the real subjects for our study, ethical considerations prevent us from listing their names. But they know who they are.</p>

<h2 id="toc-references-12">

References</h2>

<ol>

<li>

J. Nielsen, " <a href="http://www.nngroup.com/articles/iterative-design/"> Iterative User-Interface Design</a>," <cite> IEEE Computer, </cite> Vol. 26, No. 11, Nov. 1993, pp. 32-41.</li>

<li>

J. Nielsen, <a href="http://nngroup.com/books/usability-engineering/"> Usability Engineering,</a> Academic Press, Boston, 1994.</li>

<li>

M. Magnusson and H. Palsson, (translators), <cite> Laxdaela Saga, </cite> Penguin Books, London, 1969, p. 90. A translation of an anonymous Icelandic handwritten manuscript from about 1245.</li>

<li>

J. Nielsen et al., "Comparative Design Review: An Exercise in Parallel Design," <cite> Proc. ACM INTERCHI'93 Conf., </cite> Assoc. for Computing Machinery, New York, 1993, pp. 414-417.</li>

<li>

R.D. Herring, J.A. List, and E.A. Youngs, "Screen-Assisted Telephony and Voice Service Usability," <cite> Proc. 14th Int'l. Symp. on Human Factors in Telecommunications, </cite> 14th Int'l. Symp. on Human Factors in Telecommunications, Darmstadt, Germany, 1993.</li>

</ol>

</div>

</div>

<div class="article-sidebar">

<div class="sidebar-wrapper">

<span id="gaDataAllTopics" class="ga-data-layer" aria-hidden="true">Interaction Design</span>

<div class="sidebar-item related-topics">

<h2 class="article-heading-small">Related Topics</h2>

<ul>

<li>

<span id="gaDataTopic" class="ga-data-layer" aria-hidden="true">Interaction Design</span>

<a class="ga-article-related-topic" href="/topic/interaction-design/">Interaction Design</a>

</li>

</ul>

</div>

</div>

</div>

</div>