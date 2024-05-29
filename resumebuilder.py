from groq import Groq
import os
import datetime

client = Groq(
    api_key = os.environ.get("GROQ_API_KEY")
)

with open('resume.txt', 'r') as resume_file:
    resume = resume_file.read()

with open('jobDescription.txt', 'r') as job_description_file:
    jobDescription = job_description_file.read()

completion = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        {
            "role": "user",
            "content": "Build a customer resume for this job posting here is the resume:" + resume + "and here is the job description:" + jobDescription + ". In the experience section tweak language to suit the job description"
        },
        {
            "role": "assistant",
            "content": "Here's a sample customer resume that highlights a candidate's skills and experience in customer-facing roles:\n\n**Name:** Emily Johnson\n\n**Contact Information:**\n\n* Email: [ejohnson@email.com](mailto:ejohnson@email.com)\n* Phone: 555-555-5555\n* LinkedIn: linkedin.com/in/emilyjohnson\n\n**Summary:**\nResults-driven customer service professional with 5+ years of experience in delivering exceptional customer experiences, driving customer satisfaction, and increasing loyalty. Skilled in conflict resolution, active listening, and effective communication. Proficient in a variety of customer relationship management (CRM) software.\n\n**Professional Experience:**\n\n**Customer Service Representative**, XYZ Corporation (2018-Present)\n\n* Handle customer inquiries and concerns via phone, email, and chat\n* Resolve customer complaints and concerns in a timely and professional manner\n* Collaborate with internal teams to resolve complex customer issues\n* Achieved a 95% customer satisfaction rate\n* Trained new customer service representatives to ensure consistency in customer service\n\n**Customer Service Representative**, ABC Company (2015-2018)\n\n* Provided exceptional customer service via phone, email, and in-person\n* Resolved customer complaints and concerns in a timely and professional manner\n* Worked closely with internal teams to resolve complex customer issues\n* Consistently met or exceeded monthly sales targets\n* Participated in cross-functional teams to develop and implement customer retention strategies\n\n**Education:**\n\n* Bachelor's Degree in Marketing, [University Name] (2015)\n\n**Skills:**\n\n* Customer service and relations\n* Conflict resolution and negotiation\n* Effective communication and interpersonal skills\n* CRM software (Salesforce, HubSpot, etc.)\n* Time management and prioritization\n* Team collaboration and leadership\n* Basic computer skills and Microsoft Office applications\n\n**Achievements:**\n\n* Consistently received positive feedback from customers and supervisors\n* Achieved a 90% customer satisfaction rate in a previous role\n* Developed and implemented a customer retention program that resulted in a 25% increase in customer loyalty\n* Completed a customer service training program and received a certification in customer service excellence\n\n**Certifications/Awards:**\n\n* Customer Service Certification, [Certification Name] (2017)\n* Employee of the Quarter, [Company Name] (2016)\n\n**References:**\nAvailable upon request.\n\nRemember to tailor your resume to the specific job posting you're applying for, highlighting the skills and experience that align with the job requirements."
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
output_file_name = f"resume_{timestamp}.md"
with open(output_file_name, 'w') as output_file:
    for chunk in completion:
        output_file.write(chunk.choices[0].delta.content)

# for chunk in completion:
#     print(chunk.choices[0].delta.content or "", end="")
