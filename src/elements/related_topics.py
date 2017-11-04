# -*- coding: utf-8 -*-
from rake_nltk import Rake
import string
import pdb

class RelatedTopics:
    def __init__(self):
        self.r = Rake()
        self.usable_characters = set('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ')

    def get_name():
        return "RelatedTopics"

    def get_human_readable_name():
        return "Related Topics"

    def clean(self, string):
        return filter(lambda x: x in self.usable_characters, string)

    """
    strings: an array of strings on which to do the data analysis
    """
    def process(self, topicrawdata):
        strings = [self.clean(string) for string in strings]
        [self.r.extract_keywords_from_text(string) for string in strings]
        keywords = self.r.get_ranked_phrases()
        keywords = [self.clean(keyword) for keyword in keywords]
        return keywords


def main():
    example_source_list = ["""
    WASHINGTON — One of President Trump’s biggest disappointments in office, by his own account, was discovering that he is not supposed to personally direct law enforcement decisions by the Justice Department and the F.B.I. So, instead, he has made himself into perhaps the most vocal critic of America’s system of justice ever to occupy the Oval Office.

    Just this week, he denounced the criminal justice system as “a joke” and “a laughingstock.” He demanded that the suspect in the New York terrorist attack be executed. He spent Friday berating the Justice Department and F.B.I. for not investigating his political opponents. He then turned to the military justice system and called a court-martial decision “a complete and total disgrace.”

    The repeated assaults on law enforcement cross lines that presidents have largely observed since the Watergate era, raising questions about the separation of politics and the law. But as extraordinary as Mr. Trump’s broadsides are, perhaps more striking is that investigators and prosecutors are so far ignoring the head of the executive branch in which they serve while military judges and juries are for the most part disregarding the opinions of their commander in chief.

    “You know, the saddest thing is that because I’m the president of the United States, I am not supposed to be involved with the Justice Department,” Mr. Trump said in a radio interview on Thursday on the “Larry O’Connor Show.” “I am not supposed to be involved with the F.B.I. I’m not supposed to be doing the kind of things that I would love to be doing. And I’m very frustrated by it.”

    That frustration has been fueled particularly by Mr. Trump’s inability to control the special counsel investigation into whether his campaign coordinated with Russia during last year’s election, an investigation that unveiled its first criminal charges this week against Mr. Trump’s former campaign chairman and two other advisers.

    Continue reading the main story
    RELATED COVERAGE

    Trump and Sessions Denied Knowing About Russian Contacts. Records Suggest Otherwise. NOV. 2, 2017

    Hillary Clinton Gets an Award and Tears Are Shed NOV. 2, 2017
    ADVERTISEMENT

    Continue reading the main story

    Mr. Trump has made clear that he sees the attorney general and the F.B.I. director as his personal agents rather than independent figures, lashing out at both for not protecting him from the Russia investigation.

    In May, he fired the F.B.I. director, James B. Comey, who later testified that he had refused Mr. Trump’s demands that he pledge loyalty and publicly declare that the president was not personally under investigation. In July, Mr. Trump told The New York Times that he would never have appointed Attorney General Jeff Sessions had he known that Mr. Sessions would recuse himself from overseeing the investigation.

    While his lawyers have for now persuaded Mr. Trump not to publicly attack Robert S. Mueller III, the special counsel, the president has not ruled out firing him, a scenario that other presidents facing special prosecutors considered virtually unthinkable. Asked on Friday whether he might fire Mr. Sessions if the attorney general does not investigate Democrats, Mr. Trump left open the prospect: “I don’t know,” he said.

    The president’s Twitter posts and comments drew rebukes from Democrats and some Republicans. Former Attorney General Eric H. Holder Jr., who served for six years under President Barack Obama, said Mr. Trump’s comments make the job of law enforcement officials more difficult.

    “Combined with his improper attempts to influence Department of Justice actions, this demonstrates that he is a president who is willing to flout those norms that protect the rule of law,” Mr. Holder said in an interview.

    Senator Bob Corker of Tennessee, a Republican who has broken with Mr. Trump, said the Justice Department should be free of political interference.

    “President Trump’s pressuring of the Justice Department and F.B.I. to pursue cases against his adversaries and calling for punishment before trials take place are totally inappropriate and not only undermine our justice system but erode the American people’s confidence in our institutions,” he said.

    Some conservatives defended Mr. Trump’s right to exercise oversight of the country’s law enforcement agencies, saying that it would be dangerous to have an attorney general and an F.B.I. director who were not answerable to elected leaders.

    “The notion that law enforcement, in particular, is somehow to be insulated from political influences and therefore inevitably insulated from political accountability is a horribly dangerous idea from the standpoint of civil liberty,” said David B. Rivkin Jr., a White House and Justice Department lawyer under Presidents Ronald Reagan and George Bush.

    However, Mr. Rivkin added, “That doesn’t mean you exercise your authority to direct those things in a crude and obscene fashion. You have to exercise some politesse about it.”

    Newsletter Sign UpContinue reading the main story
    Morning Briefing
    Get what you need to know to start your day in the United States, Canada and the Americas, delivered to your inbox.


    Enter your email address
     Sign Up

    You agree to receive occasional updates and special offers for The New York Times's products and services.

    SEE SAMPLE MANAGE EMAIL PREFERENCES PRIVACY POLICY OPT OUT OR CONTACT US ANYTIME
    Other presidents have been criticized for political intervention when they spoke out about continuing criminal cases. Peter J. Wallison, who was the White House counsel under Reagan, said his president at times spoke out on cases of interest, including the investigation of Reagan’s onetime adviser Michael K. Deaver.

    “I would try to discourage him, for all the good reasons people in the White House are probably trying to discourage Trump, but it was to no avail,” Mr. Wallison said. “Trump is doing the same, except to a greater extent.”

    Mr. Wallison noted that Mr. Obama at times commented on investigations, recalling statements denying wrongdoing by the Internal Revenue Service when conservative groups found their tax exemptions targeted for scrutiny. “Presidents say these things because they are human beings and have emotions,” he said. “Nevertheless, there is little evidence that public statements have any effect on outcomes.”

    Before Watergate, presidents were less reluctant to intervene in law enforcement. The administrations of Presidents John F. Kennedy and Lyndon B. Johnson had the F.B.I. wiretap the Rev. Dr. Martin Luther King Jr. President Richard M. Nixon had the bureau eavesdrop on the telephone calls of reporters.

    But in the past four decades, no president has sought to publicly pressure law enforcement as much as Mr. Trump.

    In a barrage of a dozen tweets on Thursday night and early Friday, Mr. Trump railed at law enforcement agencies for not investigating Democrats. He cited Tony Podesta — the brother of Hillary Clinton’s campaign chairman, John D. Podesta — who stepped down from his firm this week amid scrutiny of his lobbying business by Mr. Mueller. And he cited a book excerpt by Donna Brazile, the former interim Democratic National Committee chairwoman, who wrote that last year’s primaries were tilted by a fund-raising agreement that the committee made with Mrs. Clinton.

    “I’m really not involved with the Justice Department,” Mr. Trump told reporters before leaving on a 12-day trip to Asia. “I’d like to let it run itself. But honestly, they should be looking at the Democrats. They should be looking at Podesta and all of that dishonesty. They should be looking at a lot of things. And a lot of people are disappointed in the Justice Department, including me.”

    Earlier in the day, Mr. Trump tweeted that Mrs. Clinton “stole the Democratic Primary” from Bernie Sanders and asserted that there was “major violation of Campaign Finance Laws and Money Laundering.”

    “At some point the Justice Department, and the FBI, must do what is right and proper,” Mr. Trump wrote.

    “Everybody is asking why the Justice Department (and FBI) isn’t looking into all of the dishonesty going on with Crooked Hillary & the Dems,” he also tweeted.

    Mr. Trump’s interest in directing law enforcement decisions extends beyond his political opposition but carries its own risk. The president’s support for capital punishment for the New York terrorism suspect, Sayfullo Saipov — “SHOULD GET DEATH PENALTY,” he tweeted — could pose problems for prosecutors and help defense lawyers who could argue that their client cannot get a fair trial.

    Mr. Trump also weighed in again on Friday on the case of Sgt. Bowe Bergdahl, who pleaded guilty to desertion and endangering other troops by walking away from his base in Afghanistan and getting captured by the Taliban. Mr. Trump, who last year called Sergeant Bergdahl a “dirty rotten traitor” who should be executed, expressed outrage when a military judge on Friday gave the sergeant a dishonorable discharge but no jail time.

    “The decision on Sergeant Bergdahl is a complete and total disgrace to our Country and to our Military,” Mr. Trump tweeted.

    But Mr. Trump’s own outspokenness may have helped lead to the very result he was condemning. The judge did not explain his reasoning on Friday but last week said he would consider the president’s past comments as evidence for a lighter sentence."""]

    rt = RelatedTopics()
    print(rt.get_keywords(example_source_list))

if __name__ == "__main__":
    main()
