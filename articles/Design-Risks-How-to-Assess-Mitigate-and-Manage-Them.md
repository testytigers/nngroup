# Design Risks: How to Assess, Mitigate, and Manage Them

**Author:** Therese FessendenTherese FessendenMay 28, 20232023-05-28

**Topics:** Strategy, Design Process

**Source:** https://www.nngroup.com/articles/design-risk-management/

---

May 28, 20232023-05-28

Share

It’s impossible to see into the future and anticipate every possible outcome of our design decisions. As a result, every major design decision comes withrisks: risk that the design will be unfamiliar or hard to use or unpopular, risk that it will cost too much money, or risk that it will be abused or cause harm.

If a design is well-evaluated before it is implemented, these risks will be small and its benefits will outweigh them. If a design is not well-evaluated, these risks could go unchecked, causing long-term harm to the organization and its customers.

To reduce harm and maximize the benefits of our designs, we need to incorporaterisk managementinto our design decisions toidentify,assess,control, andevaluatethe risks in a systematic way.

Design risk:The likelihood that an aspect of a new or existing design will negatively impact the business or its customers.

The magnitude of that risk can be written as:

Risk = Likelihood x Impact

with thelikelihoodbeing the probability that a negative outcome (sometimes called ahazard) will be observed and theimpactrepresenting the severity of that outcome.

Organizations strive to mitigate risk to reduce harm, maximize profits, and improve the chance that customers will return.Mitigation, however, means reducing a risk, not necessarily eliminating it.

The process ofrisk managementenables organizations to assess risks during the design process in order to better address them. It ultimately involves making sure that the assumed risks of our actions are outweighed by these actions’ expected benefits.

There are many published risk-management process frameworks, but most can be distilled down to the 6 steps described below:

To illustrate the risk-management process in a UX context, we will use the example of an ecommerce team working to improve the checkout process on its company’s website.

No organization or person ever intentionally takes on a risk unless there is a benefit. Put another way, a team cannot decide whether a risk is worth taking unless it is aligned onwhythe risk must be taken: that is, it understands the benefits of the associated action. So, it’s important that organizations establish and prioritize key success criteria for the organization and for the design before evaluating potential risks.

For our UX example, let’s imagine that our ecommerce team has a high-priority objective: to increase revenue per visitor. To increase revenue per visitor, a proposed design might include1-click purchasing, which allows for a transaction to happen with a single click.

Information about hazards (things which have the potential to cause harm) can be found through a number of different qualitative sources likebehavioral or attitudinal research,cause-and-effect (“if [this], then [that]”) or flow diagrams, and audits (or data from other assessments).These can shed light on common complaints, challenges, and concerns.Analytics, support-ticket data, and case logsmayalsooffer quantitative information about the frequency and outcomes of certain hazards.

As you can see, several of these data sources relate topastexperiences or historical data about a product. If these are not available because your product does not exist yet, contextual knowledge obtained by qualitative research andsecondary (desk) research(i.e., literature reviews) may give you a high-level idea of what risks to expect.

However, secondary research is not a substitute for observational research. Whenever possible, rely on observational research to assess hazards.

In our ecommerce example, at this step, the team needs to identify the hazards associated with1-click purchasing. The team may review any third-party sources that document possible issues with this solution. It may also conduct someuser research on competitor productswho use this type of design. Here are some of the hazards that could emerge as a result of this research:

As we mentioned earlier, a risk is the combination of thelikelihood(probability) that harm will happen and theimpact(severity) of the consequence. Thus, to accurately assess risk, the knowledge around that risk must be more specific than a vague idea of negative outcomes. If we have information about the likelihood of a hazard and the severity of the consequences, we can then “plot” the risk associated to that hazard on arisk-assessment matrix, to evaluate how detrimental it is, and how crucial it is to mitigate it.

Each team will define the risk-assessment matrix associated with their outcomes and then will “plot” each hazard on this matrix.

Consider the ecommerce example of1-click purchasingand the hazards we identified earlier:

Hazard

Risk Likelihood (Probability)

Risk Impact (Severity)

Likely

Moderate

Occasional

Critical

Frequent

Moderate

We could then plot these onto a risk-assessment matrix to visualize the relative risk:

Remember that the risk isLikelihoodxSeverity.Thus,the best way to mitigate risk is to either reduce its likelihood or limit its severity (or, ideally, both). While extremely high and high risks should be mitigated, low risks might not warrant special mitigation, especially if it means taking time away from other high-priority efforts.

Let’s go back to our ecommerce example. In our case, B (increased number of fraudulent transactions) and C (increased shipping costs) are high. The team may consider a few strategies to mitigate these risks:

Considering the hazards we’ve identified, we might mitigate risk as follows:

Hazard

Mitigation

New Risk Probability

New Risk Severity

Immediately provide confirmation and cancellation options, but delay sending order info to fulfillment center by 12 hours.

Occasional

Negligible

Require authentication within 12–24 hours as a condition of1-click ordering

Seldom

Critical

Offer two forms of 1-click shipping:Ship NowandShipwithNextBatch.

Likely

Moderate

Reassessing risks after mitigation strategies are proposed can give an objective perspective of whether risks are truly mitigated or still too high to move forward with a decision. It also allows teams to propose more-involved or less-involved mitigation strategies, depending on their risk-tolerance levels, while the risks are still objectively evaluated the same way every time.

While your team may have developed strategies to reduce design risks to an acceptable level, that does not mean it should automatically implement them. Just because something is “low risk” does not mean it’s still worth pursuing. Risk mitigation may also interfere with the team’s original objectives.

With our earlier1-click ordering example, possible mitigation strategies might involve introducing friction, like one more click to confirm purchase (and thus, reduce the probability of accidental purchases), or slowing down backend processes to give users time to undo any accidental transactions without impacting customer-support costs. However, either of these strategies may also slow the speed of the transaction or shipping to the point it’s not much faster than the existing checkout process.

So, while the risk of accidental purchases may be lower, the benefit of amildlyfaster transaction may still not outweigh the implementation cost and the remaining risk of an accidental purchase. Therefore, a more risk-tolerantteam may opt to implement 1-click ordering without the mitigation, while a more risk-averseteam may decide that the conversion-rate improvement is worth it only if it doesnotresult in swamping the customer-support staff and may, therefore, choose to mitigate the risk (or forgo the initial design choice entirely). Still, even if a team is normally risk-tolerant, facing more risk than usual for other reasons (like an economic recession) may also impact that team’scurrenttolerance to risk.

More importantly, most teams aren’t, as my mother used to say, “made of money.” Risk-mitigation strategies come with their own implementation costs. Teams need to analyze the costs of these strategies and much like a team might prioritize designs by their user impact and feasibility, controls should be pursued by weighing their relative feasibility & overallriskimpact.

Often, these controls come in the form of adjustments or specifications for both new and existing designs, but they may also be changes in workflows, processes, and business models. Regardless what types of controls you’re considering, some well-distributed (and more importantly, well-written) documentation will ensure that the controls are implemented consistently across the organization.

Finally, a risk-management strategy will only be as good as the team’s ability to update it with new and relevant data about those risks. As designs change over time, risk-mitigation strategies may become irrelevant or outdated. Thus, complacency and a false sense of security about previously identified risks can result in disastrous outcomes for users and organizations alike.

To avoid potential damage from insufficient risk mitigation or recurrent risks, teams should consider scheduling routine audits at specified intervals or milestones and regular retrospectives to evaluate whether risk-mitigation strategies are working, or need adjustment with new circumstances.

Not only are some risks entirely out of our control, but some are also impossible to anticipate. “What-if”-ing every design decision to death (“What if an asteroid hits our server?”) is itself a risk to the organization — spending time deliberating about risks that are both unlikely and outside of our control is counterproductive. So, the best we might be able to do in cases of external, uncontrollable risk is to monitor frequently to ensure we are aware of new risks early and adapt our designs to be “resilient” to foreseeable risks.

Risk management is a critical skill that will only become more entwined with UX work as technology scales to impact more people at greater speeds in more places. As the old adage goes, accept the things we cannot change, have courage to change the things we can, and have the wisdom to know the difference.

Set a strategic, practical plan to align, prioritize, and communicate UX work

Management

Capture and communicate UX insights across complex interactions

Research

Build a crossfunctional journey-centric design approach that scales

Management