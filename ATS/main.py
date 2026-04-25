from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
import shutil
import os

from langchain.chat_models import init_chat_model
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from data.verbs.verbs import ACTION_VERBS
from data.keywords.all import ALL_SKILLS
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


model = init_chat_model("mistral-small-latest")


@app.get('/')
def root():
    return {'message': 'welcome to ATS checker'}


@app.post('/check-resume')
async def check_resume(file: UploadFile = File(...)):

    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    
    resume_location = PyPDFLoader(temp_path)
    user_resume = resume_location.load()
    score = 0
    resume = []

    for i in user_resume:
        resume.append(i.page_content.lower())

    updated_resume = "".join(resume)
    updated_resume = updated_resume.replace(" ", "")
    updated_resume = updated_resume.replace("%", " ")
    updated_resume = updated_resume.replace("/", " ")

    
    missing_sections = []   
    low_scores = []         
    score_messages = []     

    
    if "achievements" in updated_resume or "achievement" in updated_resume:
        score += 3
        score_messages.append("Achievements section found (+3)")
    else:
        score -= 3
        missing_sections.append("Add an Achievements section to highlight your wins")
        score_messages.append("Achievements not mentioned (-3)")

    if "skills" in updated_resume or "skill" in updated_resume:
        score += 3
        score_messages.append("Skills section found (+3)")
    else:
        score -= 3
        missing_sections.append("Add a Skills section listing your technical abilities")
        score_messages.append("Skills not mentioned (-3)")

    if "@" in updated_resume:
        score += 2
        score_messages.append("Email found (+2)")
    else:
        score -= 2
        missing_sections.append("Add your email address so recruiters can contact you")
        score_messages.append("Email not mentioned (-2)")

    if "linkedin" in updated_resume:
        score += 2
        score_messages.append("LinkedIn found (+2)")
    else:
        score -= 2
        missing_sections.append("Add your LinkedIn profile URL")
        score_messages.append("LinkedIn not mentioned (-2)")

    if "github" in updated_resume:
        score += 2
        score_messages.append("GitHub found (+2)")
    else:
        score -= 2
        missing_sections.append("Add your GitHub profile to showcase your code")
        score_messages.append("GitHub not mentioned (-2)")

    if "portfolio" in updated_resume:
        score += 2
        score_messages.append("Portfolio found (+2)")
    else:
        score -= 2
        missing_sections.append("Add a portfolio link to display your work")
        score_messages.append("Portfolio not mentioned (-2)")

    if "education" in updated_resume:
        score += 3
        score_messages.append("Education section found (+3)")
    else:
        score -= 3
        missing_sections.append("Add an Education section with your degrees")
        score_messages.append("Education not mentioned (-3)")

    if "projects" in updated_resume:
        score += 3
        score_messages.append("Projects section found (+3)")
    else:
        score -= 3
        missing_sections.append("Add a Projects section to demonstrate your skills")
        score_messages.append("Projects not mentioned (-3)")

    if "certifications" in updated_resume or "certificates" in updated_resume:
        score += 3
        score_messages.append("Certifications found (+3)")
    else:
        score -= 3
        missing_sections.append("Add any certifications or courses you've completed")
        score_messages.append("Certifications not listed (-3)")

    
    user_role_prompt = ChatPromptTemplate.from_messages([
        ("system", """
You are an expert resume analyzer.
Return ONLY one job role in lowercase, 2-4 words, no punctuation.
Examples: software developer, data analyst, frontend developer
"""),
        ("user", "Analyze this CV and return ONLY the role:\n{resume_text}")
    ])

    final_role_prompt = user_role_prompt.invoke({'resume_text': updated_resume})
    result = model.invoke(final_role_prompt)
    user_role = result.content.strip()

    
    user_skills_prompt = ChatPromptTemplate.from_messages([
        ("system", """
Extract skills ONLY from the skills section. Comma separated, lowercase.
If no skills section, return: none
"""),
        ("user", "Extract skills from:\n{resume_text}")
    ])

    final_user_skills = user_skills_prompt.invoke({'resume_text': updated_resume})
    result = model.invoke(final_user_skills)

    user_skills_readable = [s.strip().lower() for s in result.content.split(",")]
    user_skills = [s.replace(" ", "").replace(".", "") for s in user_skills_readable]

    
    skill_score = 0
    for skill in user_skills:
        if skill in ALL_SKILLS:
            weight = ALL_SKILLS[skill]['weight']
            if skill_score + weight <= 30:
                score += weight
                skill_score += weight
                score_messages.append(f"Skill '{skill}' found (+{weight})")

  
    missing_skills_prompt = ChatPromptTemplate.from_messages([
        ("system", """
    You are a career advisor for the role: {user_role}

    Your task: Suggest 5-8 IMPORTANT skills the candidate should ADD to become more competitive for this role.

    STRICT RULES:
    - ALWAYS return 5-8 skills (never return "none")
    - DO NOT include skills the user ALREADY has (check the user skills list carefully)
    - Focus on industry-standard tools, frameworks, and concepts for the role
    - Include modern/trending skills employers expect in 2025
    - Output: comma separated, lowercase, no explanations
    - Each skill must be 1-3 words max
    - NO bullet points, NO numbers, NO markdown

    GUIDELINES BY ROLE:
    - For "android app developer": think jetpack compose, mvvm, room, retrofit, dagger hilt, coroutines, kotlin flows, material design 3, firebase analytics, play store deployment
    - For "frontend developer": think nextjs, typescript, redux, testing, accessibility, web performance
    - For "backend developer": think docker, kubernetes, microservices, redis, message queues
    - For "data analyst": think tableau, power bi, statistics, excel advanced, etl

    EXAMPLE OUTPUT for android app developer:
    jetpack compose, mvvm architecture, room database, retrofit, dagger hilt, coroutines, material design 3
    """),
        ("user", """
    Target Role: {user_role}

    Skills user ALREADY HAS (do NOT repeat these):
    {user_skills}

    Return 5-8 skills the user is MISSING that would make them stronger for the {user_role} role.
    """)
    ])
    missing_final = missing_skills_prompt.invoke({
        'user_role': user_role,
        'user_skills': ", ".join(user_skills_readable)
    })
    result = model.invoke(missing_final)
    missing_skills_raw = result.content.strip()

    
    if missing_skills_raw.lower() == "none" or missing_skills_raw == "":
        missing_skills_list = []
    else:
        missing_skills_list = [
            s.strip().replace("*", "")
            for s in missing_skills_raw.split(",")
            if s.strip() and len(s.strip()) < 50
        ]

    
    work_prompt = ChatPromptTemplate.from_messages([
        ("system", """
Extract work experience as valid JSON only.
Format:
{{
  "total_experience_years": 1.5,
  "experiences": [
    {{"name": "company", "role": "role", "duration": "dates", "relevant": true}}
  ]
}}
"""),
        ("user", "CV:\n{resume_text}")
    ])

    work_final = work_prompt.invoke({'resume_text': updated_resume})
    result = model.invoke(work_final)
    clean = result.content.replace("```json", "").replace("```", "")

    try:
        work_experience_data = json.loads(clean)
    except Exception:
        work_experience_data = {"total_experience_years": 0, "experiences": []}

    if work_experience_data.get('total_experience_years', 0) == 0:
        score -= 5
        low_scores.append("No clear work experience dates found in your resume")
        score_messages.append("No work experience date mentioned (-5)")

    exp_score = 0
    for exp in work_experience_data.get('experiences', []):
        if exp.get('relevant') == True:
            if exp_score + 4 <= 20:
                score += 4
                exp_score += 4
                score_messages.append(f"Relevant experience at {exp['name']} (+4)")
        else:
            score -= 2
            low_scores.append(f"Experience at {exp.get('name', 'unknown')} doesn't match your target role")
            score_messages.append(f"No relevant experience at {exp.get('name')} (-2)")

    
    action_verbs_prompt = ChatPromptTemplate.from_messages([
        ("system", """
You are a resume verb improver.

Your ONLY job: find weak/passive verbs in the resume and suggest stronger replacements from the given list.

STRICT OUTPUT FORMAT (one suggestion per line):
weak_verb -> strong_verb

RULES:
- Maximum 5 suggestions
- NO markdown
- NO bold (no ** symbols)
- NO headings
- NO section names
- NO project names
- NO bullet points
- NO numbered lists
- ONLY the verb replacements
- If no weak verbs found, return exactly: none

EXAMPLE OUTPUT:
worked on -> developed
helped with -> collaborated on
made -> engineered
"""),
        ("user", "Strong verbs list:\n{verbs}\n\nResume:\n{resume_text}\n\nReturn ONLY verb replacements.")
    ])

    final_verbs = ", ".join(ACTION_VERBS) if isinstance(ACTION_VERBS, list) else str(ACTION_VERBS)
    action_final = action_verbs_prompt.invoke({
        'verbs': final_verbs,
        'resume_text': updated_resume
    })
    result = model.invoke(action_final)
    action_raw = result.content.strip()

    
    verb_improvements = []
    if action_raw.lower() != "none":
        for line in action_raw.split("\n"):
            cleaned = line.strip().replace("*", "").lstrip("-•").strip()
            if not cleaned or len(cleaned) > 80:
                continue
            if cleaned.endswith(":"):
                continue
            
            if "->" in cleaned:
                parts = cleaned.split("->")
            elif "→" in cleaned:
                parts = cleaned.split("→")
            else:
                continue
            if len(parts) == 2:
                weak = parts[0].strip()
                strong = parts[1].strip()
                if weak and strong and len(weak) < 30 and len(strong) < 30:
                    verb_improvements.append({
                        "weak": weak,
                        "strong": strong
                    })
            if len(verb_improvements) >= 5:
                break

    
    education_prompt = ChatPromptTemplate.from_messages([
        ("system", """
Extract education as JSON array only.
Format: [{{"name": "string", "total_years": number, "percentage": number}}]
Convert CGPA to percentage (cgpa/10)*100. If unknown use null.
"""),
        ("user", "Resume:\n{resume_text}")
    ])

    edu_final = education_prompt.invoke({'resume_text': updated_resume})
    result = model.invoke(edu_final)
    clean = result.content.replace("```json", "").replace("```", "")

    try:
        education_data = json.loads(clean)
    except Exception:
        education_data = []

    edu_score = 0
    for edu in education_data:
        if edu.get("percentage") is not None:
            if edu["percentage"] > 90:
                if edu_score + 5 <= 15:
                    score += 5
                    edu_score += 5
                    score_messages.append(f"Above 90% in {edu['name']} (+5)")
            elif 70 < edu["percentage"] < 90:
                if edu_score + 3 <= 15:
                    score += 3
                    edu_score += 3
                    score_messages.append(f"70-90% in {edu['name']} (+3)")
            elif edu["percentage"] < 70:
                score -= 2
                low_scores.append(f"Your percentage at {edu['name']} is below 70% — consider adding context")
                score_messages.append(f"Below 70% in {edu['name']} (-2)")

    
    os.remove(temp_path)

    
    if score > 100:
        score = 100
    if score < 0:
        score = 0

    
    return {
        "total_score": score,
        "role": user_role,
        "user_skills": user_skills_readable,
        "missing_skills": missing_skills_list,        
        "verb_improvements": verb_improvements,       
        "missing_sections": missing_sections,         
        "low_scores": low_scores,                     
        "work_experience": work_experience_data,
        "education": education_data,
        "score_messages": score_messages              
    }