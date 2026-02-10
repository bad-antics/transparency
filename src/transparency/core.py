"""Transparency of Evil Engine"""
import json,random

class TransparencyEngine:
    CONCEPTS={
        "transparency":{"definition":"When everything is visible, evil becomes transparent",
                        "paradox":"Total visibility creates total blindness",
                        "consequence":"Without secrets, nothing has meaning"},
        "obscenity":{"definition":"The state of total visibility without mystery",
                     "paradox":"The more visible, the less real",
                     "consequence":"Meaning implodes under total exposure"},
        "viral":{"definition":"Evil spreads virally through transparency",
                 "paradox":"Openness enables contamination",
                 "consequence":"Systems of control become indistinguishable from freedom"},
        "after_orgy":{"definition":"After the liberation of all values, what remains?",
                      "paradox":"Freedom from constraint = freedom from meaning",
                      "consequence":"Endless simulation replaces genuine transgression"},
    }
    
    def explore_concept(self,concept):
        return self.CONCEPTS.get(concept,{})
    
    def transparency_index(self,factors):
        score=0
        weights={"surveillance":20,"data_collection":15,"social_scoring":20,
                 "total_information":15,"no_privacy":20,"algorithmic_control":10}
        for factor,weight in weights.items():
            if factors.get(factor): score+=weight
        state="OBSCENE" if score>70 else "TRANSPARENT" if score>40 else "TRANSLUCENT" if score>20 else "OPAQUE"
        return {"index":score,"state":state}
    
    def generate_diagnosis(self):
        diagnoses=[
            "We have moved beyond the era of the spectacle into the era of transparency.",
            "Evil is no longer locatable — it has become the system itself.",
            "When everything is political, nothing is political.",
            "The transparency of evil is that evil is everywhere and nowhere.",
        ]
        return random.choice(diagnoses)
