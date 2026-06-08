# Designing Scroll Behavior: When to Save a User’s Place

**Author:** Megan ChanMegan ChanJuly 11, 20252025-07-11

**Topics:** Interaction Design

**Source:** https://www.nngroup.com/articles/saving-scroll-position/

---

July 11, 20252025-07-11

Share

One of the fastest ways to frustrate a user is by losing their progress. Imagine this: you scroll, scroll, scroll down a long list…click…read, and hit theBackbutton, only to land back at the top of the list instead of where you left off.

It’s a small moment, but failing to save scroll position increases theinteraction costof using sites with long pages. Most of the time, saving scroll position reduces user effort.

That being said, there’s noalwaysinUX. It is important to consider user intent, and there are a few cases where saving scroll position is not the right choice.

Pogo stickingrefers to the pattern of navigating back and forth between a routing page (usually, a list such as a search-results page or a list of products) to a page deeper in the site’s hierarchy, linked from that routing page (for example, a product page). It happens a lot when people visit news aggregators or ecommerce product-listing pages, and it’s also one of the common cases when people lose their spot on the page. That’s because when users navigate back to the routing page, the page often resets to the top of the list, forcing the user to scroll and scan again to return to their original position.

In a recent study, a participant was browsing podcast episodes in the Spotify app. He scrolled down past episodes that he had already listened to, looking for a new one. After the participant clicked on an episode to check out the details, he decided that he wanted to go back and continue browsing. However, he was returned to the top of the list, which meant that he had to scroll down again to find his place. This design unnecessarily increased interaction cost.

To work around this issue, many (but not all) users usepage parking— opening items in new tabs. However, this technique is not always available, either because using tabs is cumbersome or even unavailable (e.g., in a mobile app), or the user may not be aware of it. Instead of forcing users to rely on workarounds like page parking, we can reduce friction by saving their scroll position.

In most cases, preserving scroll position is the right choice as it minimizes interaction cost. When it’s not saved, simple tasks like shopping, reading, or choosing a podcast become more tedious than necessary.

Saving scroll position is helpful when users come back to the page during the same session, and the page content has not changed.

It’s the same as withpagination. Users expect to return to the same page they were on while browsing a paginated list. If the user clicks into an item on page 8 and then returns to the list, they should not land back on page 1.

While saving a user’s place is often the right choice, there are some cases where it is more helpful to reset the scroll position. To determine the best design for scroll behavior, consider the context: the type of content that is being shown, how often it updates, and what the user is trying to accomplish.

If the content has been updated since the user last viewed the page, saving their old scroll position may cause them to be placed in an outdated or irrelevant part of the list. This can be particularly problematic in real-time or fast-changing sites.

For example, during a political debate or a live sports event, updates are posted constantly as the event unfolds. If a user returns to the same scroll position after stepping away, they might miss important developments that have occurred since they left.

When important, timely updates occur, automatically resetting the scroll position helps surface the newest content for users right away.

When resetting the scroll position,use a clear visual indicator to show that the content has changed and the scroll position has reset.TheScore’s app uses a scrollanimationthat brings the latest chat messages into view. The animation communicates to the user that they are seeing new content and helps them stay oriented.

Saving scroll position works best when users return shortly after leaving a page, while their mental context is still fresh. However, as time passes, the mental anchor that helped them remember their place begins to fade. Therefore, saving scroll position should only apply in individual sessions — roughly up to 30–60 minutes after the last user action.

Users who return after hours, days, or even weeks may not remember where they left off or why they were there. In these cases, dropping them back into a deep scroll position risks confusion:Why am I halfway down this list?What was I looking for?Refreshing the page and sending users to the top helps reestablish context and gives them a clean starting point after the session has ended.

On mobile, users often leave tabs open for long periods of time. When users return to the tab long after their session ends, it’s likely they intend to start over rather than pick up where they left off.

Sometimes, users want to pick up exactly where they left off on a page. Other times, they need the page to refresh so they can view the most recent content right away. It’s important to understand user intent when designing interactions, since what works well in one scenario can cause annoyance in another. In cases when user intent varies, choose the lowest-friction default. Typically, that meanssaving the scroll position and offering an easy way to reset the position if users prefer so.Take ChatGPT: A user might scan up through their current conversation and, as they’re doing so, switch conversations to confirm a fact or look something up, then return to the chat to continue their train of thought. In that case, saving the scroll position would reduce friction.

Or, the user may come back and want to ask a new question, in which case, seeing the latest bot-message and the chat box might be more helpful.

It’s hard to say which of the two designs would be best for a particular context. In such situations, the solution is to choose the least disruptive design. In the case of ChatGPT, this design would preserve the last scroll position and would offer users a persistent chat box or aJumptoLatest Messagebutton that would allow them to quickly navigate to the end of the conversation. (This, unfortunately, is not the current design used by ChatGPT. The scroll position is not saved when the user returns to a conversation, even though the chat box is persistent.)

Scroll position is a small UX detail that shapes the experience. You might not notice it when it works, but you definitely notice it when it doesn’t.

Like all UX decisions, scroll behavior should be guided by context. A thoughtful approach to scroll behavior can make the difference between a frustrating experience and an efficient one.

Design how users connect, navigate, and engage with your interfaces

Interaction

Strategically combine content, visuals, and interactive components to design successful web pages

Interaction