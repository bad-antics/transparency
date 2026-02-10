from transparency.core import TransparencyEngine
t=TransparencyEngine()
for c in ["transparency","obscenity","viral","after_orgy"]:
    info=t.explore_concept(c)
    print(f"{c}: {info['paradox']}")
print(f"\nTransparency index: {t.transparency_index({'surveillance':True,'data_collection':True,'no_privacy':True})}")
print(f"Diagnosis: {t.generate_diagnosis()}")
