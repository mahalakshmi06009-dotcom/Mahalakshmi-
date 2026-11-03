# NOTE-TAKING 1 - Benefits of Reading

print("Title: Importance of Reading\n")

notes = {
    "1. Benefits of Reading": [
        "Improves vocabulary",
        "Enhances concentration",
        "Develops critical thinking"
    ],
    "2. Broadens Knowledge": [
        "Introduces new ideas",
        "Exposes readers to different cultures and perspectives"
    ],
    "3. Academic Advantages": [
        "Improves performance in studies",
        "Enhances subject knowledge"
    ],
    "4. Personal Development": [
        "Stimulates imagination and creativity",
        "Encourages lifelong learning"
    ],
    "Conclusion": [
        "Daily reading habit contributes to personal growth and continuous learning"
    ]
}

for title, points in notes.items():
    print(title)
    for point in points:
        print(f"  ✦ {point}")
    print()

print("--- Prepared by Mahalakshmi - Civil ---")
