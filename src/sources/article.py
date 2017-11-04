import newspaper

class Article:
    def __init__(self, url):
    	self.url = url
    	self.scrape()

    def get_text(self):
        #temp
        return '''
In August, when Hurricane Harvey was bearing down on Texas, David Clutter was in court, trying one more time to make his insurer pay his flood claim — from Hurricane Sandy, five years before.

Mr. Clutter’s insurer is the federal government. As it resists his claims, he has been forced to take out a third mortgage on his house in Long Beach, N.Y., to pay for repairs to make it habitable for his wife and three children. He owes more than the house is worth, and his flood-insurance premiums just went up.

The government-run National Flood Insurance Program is, for now, virtually the only source of flood insurance for more than five million households in the United States. This hurricane season, as tens of thousands of Americans seek compensation for storm-inflicted water damage, they face a problem: The flood insurance program is broke and broken.

The program, administered by the Federal Emergency Management Agency, has been in the red since Hurricane Katrina flooded New Orleans in 2005. It still has more than a thousand disputed claims left over from Sandy. And in October, it exhausted its $30 billion borrowing capacity and had to get a bailout just to keep paying current claims.

 Congress must decide by Dec. 8 whether to keep the program going. An unusual coalition of insurers, environmentalists and fiscal conservatives has joined the Trump administration in calling for fundamental changes in the program, including direct competition from private insurers. The fiscal conservatives note that the program was supposed to take the burden off taxpayers but has not, and environmentalists argue that it has become an enabler of construction on flood-prone coastlines, by charging premiums too low to reflect the true cost of building there.

Continue reading the main story
The program has other troubles as well. It cannot force vulnerable households to buy insurance, even though they are required by law to have it. Its flood maps can’t keep up with new construction that can change an area’s flood risk. It has spent billions of dollars repairing houses that just flood again. Its records, for instance, show that a house in Spring, Tex., has been repaired 19 times, for a total of $912,732 — even though it is worth only $42,024.

And after really big floods, the program must rely on armies of subcontractors to determine payments, baffling and infuriating policyholders, like Mr. Clutter, who cannot figure out who is opposing their claims, or why.

Roy E. Wright, who has directed the flood insurance program for FEMA since June 2015, acknowledged in an interview on Friday that major changes were called for and said some were already in the works. The program’s rate-setting methods, for example, are 30 years old, he said, and new ones will be phased in over the next two years. But other changes — like cutting off coverage to homes that are repeatedly flooded — would require an act of Congress.

“The administration feels very strongly that there needs to be reform this year,” he said. “I believe strongly that we need to expand flood coverage in the United States, and the private insurers are part of that.”

The federal program was created to fill a void left after the Great Mississippi Flood of 1927, when multiple levees failed, swamping an area bigger than West Virginia and leaving hundreds of thousands homeless. Insurers, terrified of the never-ending claims they might have to pay, started to exclude flooding from homeowners’ insurance policies. For decades, your only hope if your home was damaged in a flood was disaster relief from the government.

Policymakers thought an insurance program would be better than ad hoc bailouts. If crafted properly, it would make developers and homeowners pay for the risks they took.

When Congress established the National Flood Insurance Program in 1968, it hoped to revive the private flood-insurance market. Initially about 130 insurers gave it a shot, pooling their capital with the government. But there were clashes, and eventually the government drove out the insurers and took over most operations.

Since 1983, Washington has set the insurance rates, mapped the floodplains, written the rules and borne all of the risk. The role of private insurers has been confined to marketing policies and processing claims, as government contractors.

That worked for a few decades. But now, relentless coastal development and the increasing frequency of megastorms and billion-dollar floods have changed the calculus.
        '''
    	return self.article.text

    def get_headline(self):
        return self.article.title

    def scrape(self):
        a = newspaper.Article(self.url)
        a.download()
        a.parse()
        self.article = a

