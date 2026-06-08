# In-Page Links for Content Navigation

**Author:** Huei-Hsin WangHuei-Hsin WangOctober 1, 20232023-10-01

**Topics:** Web Usability, Design Patterns, Interaction Design

**Source:** https://www.nngroup.com/articles/in-page-links-content-navigation/

---

October 1, 20232023-10-01

Share

Navigating long-form content can be challenging, akin to climbing stairs in a tall building. Just like elevators can take you straight to the destination floors, in-page links helpusers navigate through page content with just one click.

In-page links(also known asjump linksoranchor links) are links that take users to a specific section on the same page.

In-page links can serve various purposes, such as aBack to Toplink or aSkip to Contentlink for keyboard users, but one of their most common uses is in a table of contents. A table of contents, usually found at the top of information-rich pages, presents a structured list of the content topics on that page, allowing users to click and navigate directly to their desired sections. While there are alternative formats for tables of contents (e.g.,accordions,sticky navigation bars), this article exclusively focuses on its implementation using in-page links.

To facilitate navigation within this article, the section below also presents a list of in-page links that can direct you to specific parts of the article.

Despite their ability to facilitate content navigation, in-page links have historically raised usability concerns as theybreak the mental model for a link.Traditionally, on the web, links lead to external pages. Due to this reason, when in-page links initially made their appearance on the web, our recommendation was to avoid them.

However, with the increased prevalence of in-page links, we have seen a growing familiarity with this design pattern. A few years ago, wereassessed the use of in-page linksand provided guidelines for its implementation (which are still applicable today). In our most recent study on how people read long content pages, we observed participants naturally engage with the table-of-contents links; these behaviors demonstrate increased awareness and understanding of the interaction pattern. Many study participantsused, commented on, and appreciated the in-page linksin tables of contents. Below we highlight some key research findings.

Most of our study participants, regardless of age, were familiar with in-page links.Only 2 out of 11 participants showed no engagement with in-page links when those were presented to them.

Despite the familiarity,in-page links, when not formatted with intention, can still surprise users.One participant, who adeptly used in-page links to navigate two other pages, expected that the in-page links on the Phone Arena page take her to another page. The confusion is likely due to how these links were styled on the Phone Arena page: they were right above theRead Moresection and looked exactly like regular links that lead to other pages. It is likely that theproximityandsimilarityof the two sections tricked her into thinking that the links from both sections serve the same purpose.

Like with any link, it’s important tosignify clickabilitythroughproper styling of the link. Users should also be able to tell whether the link will keep them on the current page. This can sometimes be done through contextual cues, like in the case of the Healthline article, where the participant was able to infer that the links under the article title are in-page links because they were directly related to the article title. However, in most scenarios that will not be apparent. It’s, thus, a good idea to use a label such asTable of ContentsorOn This Pageto help users identify in-page links.

As one study participant was exploring an article, he said about the table of contents:I like that section heading up here. That kind of gives you the outline of the article so you can jump to a specific section rather than having to scroll through everything if you're only looking for a specific bit of information.

This quote highlights two ways in which tables of contents with in-page links are useful:

Allow Users to Skip to Relevant Sections

Peopleread little on web pages. Several participants commented that in-page links helped them skip content that they were not interested in, allowing them to avoid scrolling through screenfuls of irrelevant information. Offeringdirect accessto specific sections on the page minimizes scrolling and helps users navigate more efficiently.

In our study, wefunneled tasks: we asked participants to first explore the page, and then we gave them more directed tasks. We observed that users tended to skip in-page links in their initial exploration and clicked on in-page navigation linkswhen they had a specific information need. For instance, one participant did not use or comment on the table-of-content links when we asked him to explore a smartphone review. Later, when he had to compare camera features on two phones, he immediately navigated to the table of contents and clicked on the in-page links to jump to the right section. We observed this behavior recur on different participants across several websites.

Provide an Outline of the Page Content

When in-page links were presented at the top of the page, several study participants spent time examining the list before exploring the content. The upfront overview of the content allows users to form amental modelof the page and quicklyassess whether the page satisfies their information needs, giving thema reason to continue to scroll.

To maximize the value of in-page links, consider the following aspects before incorporating them into your design:

In-page links are most valuable for long-form content. For shorter pages with minimal information, users are unlikely to require in-page links for navigation. Including a table of contents with in-page links on such pages can add unnecessary length to the page and push content further away below the fold.

While in-page links are valuable tools for facilitating page navigation, the content remains the core of the experience. When considering the use of in-page links for long-form content, assess whether the content can be condensed. Shorter, scannable content significantly enhances the overall reading experience. Eliminating unnecessary details helps reduce page length, potentially to a point where in-page tables of contents become unnecessary.

While showing everything on one page and incorporating in-page links for navigation might seem appealing, this design choice comes with two significant disadvantages:  excessively long pages and large load times. These disadvantages can beproblematic for mobile usersbecause of:

How you decide to lay out content should depend on the informationon your page. Users are willing to scroll through a long page if all the presented information is highly relevant to their needs. However, if your page includes several distantly related topics, breaking it across multiple pages might be more practical.

Using in-page links as a table of contents on the page requires breaking down the content into distinct chunks that can be summarized with a heading.Chunking information improves scannability and comprehension, but if the information is better presented in one cohesive body, in-page links are not useful.

Accordions andtabsare alternative design patterns for implementing tables of contents on long content pages.

These 3 interaction patterns share some similar characteristics:

The table below highlights their differences:

In-Page Links

Accordions

Tabs

Function

Navigation

Content structuring

Page length

Increased

Decreased

Is some content hidden by default?

No

Yes

Access to parallel content sections

Yes

No if only one accordion can remain open at a time

No

Main use case

Embedded into the body text as a table of contents

Formatting multiple short content sections

For formatting few longer content sections

Among the three,accordions shine through inmobile usage.In contrast to in-page links that push down content, accordions reduce page length by doubling as both section headings and content container controls.

Tabs suffer from low discoverability. In many cases, users tend to focus on the content in the default tab and ignore the information presented in the other tabs. Tabs also make it difficult to refer to information in two tabs at the same time. On mobile, the list of tabs may not entirely fit on the small screen, forcing designers to resort to imperfect solutions such as label truncation or hiding some of the tabs in a carousel.

When choosing among these design patterns, assess user goals and weigh the benefits and tradeoffs of each option. Two key questions to consider are:

One key point is that content structure and format should comebefore choosing a design pattern. By prioritizing content organization, you can make informed decisions that lead to better user experiences.

Tables of contents based on in-page links are a valuable tool for navigating long-form content. Research indicates that users are increasingly familiar with this design pattern. When properly styled and labeled, in-page links provide a useful overview and a quick way to access specific page sections. The decision to implement in-page links should be based on thoughtful consideration of the content structure and user needs. If in doubt, conduct usability testing to assess if in-page links are suitable for your page.

Check out our full-day courseWeb Page UX Design

Use psychology to predict and explain how your customers think and act

Interaction

Strategically combine content, visuals, and interactive components to design successful web pages

Interaction

Create and evaluate applications for advanced decision making, complicated workflows, and complex domains

Interaction