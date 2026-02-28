# FirstStep 🚀
## Basic Details
**Team Name:** Pairadox

### Team Members
- **Member 1:** Liya - [Collage of engineering Chengannur]
- **Member 2:** Ardra Vinu - [Collage of engineering Chengannur]

### Hosted Project Link
[Add your hosted link here]

## Project Description
FirstStep is a micro-gig platform connecting fresh graduates with small businesses who have real beginner-friendly work to offer. Students apply with just their skills and availability — no resume, no experience needed. Once someone applies, the gig is marked Taken, ensuring zero competition for every listing.

## The Problem Statement
Millions of fresh graduates in India are stuck in the experience trap — every job platform requires prior experience, making it impossible to get started. Students from colleges without strong placement cells have no way to build a portfolio or prove their skills.

## The Solution
FirstStep lets small businesses post micro-tasks marked as Beginner Friendly. Students browse and apply instantly with just their name, skills, and availability. Each gig accepts only one applicant — eliminating competition and giving every beginner a genuine first opportunity.

## Technical Details
### Technologies/Components Used
For Software:
- **Languages used:** JavaScript, Python, HTML, CSS
- **Frameworks used:** Flask, Flask-CORS
- **Libraries used:** datetime, json (Python built-in)
- **Tools used:** VS Code, Git, GitHub, Brave Browser

## Features
- **Browse Gigs:** Filter gigs by category — Web Dev, Design, Writing, Data Entry
- **Zero Competition:** Gig marked ✓ Taken once one student applies, Apply button hidden
- **Simple Apply Form:** Name, skills, availability only — no resume needed
- **Post a Gig:** Live preview card updates as employer types in real time
- **Employer Dashboard:** View all applicants per gig with skills and availability
- **Auto Timestamp:** Today's date added automatically when a gig is posted

## Implementation
### For Software:
#### Installation
```bash
git clone https://github.com/YOUR_USERNAME/firststep.git
cd firststep
pip install flask flask-cors
```

#### Run
```bash
cd Backend
python app.py
```
Then open `Frontend/index.html` in your browser.

## Project Documentation
### For Software:

#### Screenshots (Add at least 3)
![Homepage](screenshot/homepage.jpeg)
Homepage — hero section with Browse Gigs and Post a Gig buttons

![Browse Gigs](screenshot/browse.jpeg)
Browse page showing gig cards with category filters and ✓ Taken badges

![Apply Form](screenshot/apply.jpeg)
Student application form — name, skills and availability only, no resume

![Dashboard](screenshot/dashboard.jpeg)
Employer dashboard showing all applicants with skills and availability

#### Diagrams
**System Architecture:**

```
Frontend (HTML/CSS/JS)
        |
        | fetch() API calls
        |
Flask Backend (app.py)
        |
        | read/write
        |
JSON Files (gigs.json, applications.json)
```
Frontend communicates with Flask via REST API. Flask reads and writes data to local JSON files.

**Application Workflow:**
```
STUDENT FLOW:
index.html → browse.html → apply.html → Success ✓ → Gig marked Taken

EMPLOYER FLOW:
post.html → gig saved to gigs.json → dashboard.html → view applicants
```

## Additional Documentation
### For Web Projects with Backend:
#### API Documentation
**Base URL:** `http://localhost:5000`

**Endpoints**

GET /gigs
- Description: Fetch all posted gigs
- Response:
```json
[
  {
    "id": "1",
    "title": "Build a Portfolio Website",
    "category": "Web Development",
    "employer_name": "Ravi's Bakery",
    "description": "...",
    "tag": "Beginner Friendly",
    "timestamp": "2026-02-28"
  }
]
```

POST /gigs
- Description: Post a new gig
- Request Body:
```json
{
  "title": "Design a Logo",
  "category": "Graphic Design",
  "employer_name": "GreenRoots NGO",
  "description": "Simple logo for our NGO",
  "tag": "Beginner Friendly"
}
```
- Response: Created gig object with auto-generated id and timestamp, status 201

POST /apply
- Description: Submit a student application
- Request Body:
```json
{
  "gig_id": "1",
  "name": "Arjun Sharma",
  "skills": "HTML, CSS, JavaScript",
  "availability": "Weekends",
  "portfolio_link": "https://github.com/arjun"
}
```
- Response: Created application object, status 201

GET /applications?gig_id=1
- Description: Get all applicants for a specific gig
- Parameters: gig_id (string) — ID of the gig
- Response: Array of application objects for that gig

## Project Demo
### Video
[Add your demo video link here — Google Drive or YouTube]

Walk through: Homepage → Browse Gigs → Apply to a gig → Gig marked Taken → Post a new Gig → Dashboard showing applicants

### Additional Demos
[Add your Netlify/Railway hosted link here]

## AI Tools Used (For Transparency Bonus)
**Tool Used:** Claude (Anthropic)

**Purpose:** Development assistance throughout the hackathon

- Generating and debugging Flask backend routes
- Building and styling all HTML/CSS/JS frontend pages
- Fixing bugs and implementing the Taken status feature
- Writing README and presentation script

**Key Prompts Used:**
- "Build a Flask backend with routes for gigs and applications"
- "Add a taken badge to browse.html when a gig has applicants"
- "Fix the IndentationError in app.py post_gig function"
- "Write a 2 minute hackathon presentation script for FirstStep"

**Percentage of AI-assisted code:** ~60%

**Human Contributions:**
- Problem identification and the core zero competition idea
- All product decisions — what features to build and why
- UI/UX design direction and color choices
- Integration, testing, and debugging on real devices
- Presentation and pitching

## Team Contributions
- **Liya:** Frontend development, UI design, integration, testing, presentation
- **Ardra Vinu:** Backend development, Flask routes, data structure design, GitHub setup

## License
This project is licensed under the MIT License — see the LICENSE file for details.
