<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Nathan Houel — Data Scientist</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  :root{
    --paper: #F2EEDF;
    --paper-card: #EAE4CE;
    --ink: #1E2A24;
    --ink-soft: #566058;
    --line: #C7BC9C;
    --blue: #2A5D82;
    --amber: #B96A1A;
  }

  *{ box-sizing: border-box; }

  html{ scroll-behavior: smooth; }

  body{
    margin: 0;
    background: var(--paper);
    background-image:
      linear-gradient(var(--line) 1px, transparent 1px),
      linear-gradient(90deg, var(--line) 1px, transparent 1px);
    background-size: 48px 48px;
    background-attachment: fixed;
    background-position: -1px -1px;
    color: var(--ink);
    font-family: 'Space Grotesk', sans-serif;
    -webkit-font-smoothing: antialiased;
  }

  .page{
    max-width: 760px;
    margin: 0 auto;
    padding: 72px 24px 56px;
  }

  @media (max-width: 600px){
    .page{ padding: 48px 18px 40px; }
  }

  /* ---------- Hero ---------- */

  .callsign{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.8rem;
    color: var(--ink-soft);
    letter-spacing: 0.02em;
    margin: 0 0 28px;
  }

  h1{
    font-size: clamp(2.1rem, 5vw, 2.9rem);
    line-height: 1.12;
    margin: 0 0 10px;
    font-weight: 700;
  }

  .role{
    font-size: 1.05rem;
    color: var(--blue);
    font-weight: 500;
    margin: 0 0 22px;
  }

  .intro{
    max-width: 62ch;
    font-size: 1.02rem;
    line-height: 1.65;
    color: var(--ink-soft);
    margin: 0 0 40px;
  }

  .route{
    width: 100%;
    height: auto;
    display: block;
    margin-bottom: 8px;
  }

  .route-caption{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.72rem;
    color: var(--ink-soft);
    text-align: right;
    margin: 0 0 56px;
  }

  /* ---------- Section headers ---------- */

  .section{ margin-bottom: 52px; }

  .section-head{
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 0 0 20px;
  }

  .swatch{
    width: 10px;
    height: 10px;
    background: var(--amber);
    flex-shrink: 0;
  }

  .section-head h2{
    font-size: 1.3rem;
    font-weight: 600;
    margin: 0;
  }

  /* ---------- Interests ---------- */

  .pins{
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
  }

  .pin{
    font-size: 0.9rem;
    padding: 8px 14px;
    border: 1px solid var(--line);
    background: var(--paper-card);
    color: var(--ink);
  }

  /* ---------- Projects ---------- */

  .projects{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
  }

  @media (max-width: 640px){
    .projects{ grid-template-columns: 1fr; }
  }

  .project{
    border: 1px solid var(--line);
    border-left: 3px solid var(--blue);
    background: var(--paper-card);
    padding: 18px 20px;
  }

  .project:nth-child(odd){ border-left-color: var(--amber); }

  .project-title{
    font-size: 1rem;
    font-weight: 600;
    margin: 0 0 6px;
    display: flex;
    align-items: baseline;
    gap: 8px;
  }

  .project-title .emoji{ font-size: 0.95rem; }

  .project p{
    margin: 0;
    font-size: 0.9rem;
    line-height: 1.55;
    color: var(--ink-soft);
  }

  /* ---------- Tech stack ---------- */

  .stack-row{
    display: grid;
    grid-template-columns: 160px 1fr;
    gap: 16px;
    padding: 14px 0;
    border-top: 1px solid var(--line);
  }

  .stack-row:last-child{ border-bottom: 1px solid var(--line); }

  @media (max-width: 560px){
    .stack-row{ grid-template-columns: 1fr; gap: 6px; }
  }

  .stack-label{
    font-size: 0.85rem;
    color: var(--ink-soft);
    padding-top: 3px;
  }

  .stack-items{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.82rem;
    line-height: 1.9;
    color: var(--ink);
  }

  /* ---------- Contact ---------- */

  .contact{
    margin-top: 56px;
    padding-top: 24px;
    border-top: 1px solid var(--line);
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: space-between;
    align-items: center;
  }

  .contact a{
    color: var(--ink);
    text-decoration: none;
    border-bottom: 1px solid var(--blue);
    padding-bottom: 1px;
  }

  .contact a:hover{ color: var(--blue); }

  .contact-links{
    display: flex;
    gap: 24px;
    font-size: 0.92rem;
  }

  .contact-note{
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.72rem;
    color: var(--ink-soft);
  }
</style>
</head>
<body>
<div class="page">

  <p class="callsign">PROFILE / GITHUB</p>

  <h1>Nathan Houel</h1>
  <p class="role">Data Scientist — Machine Learning, Computer Vision, Sports Analytics</p>
  <p class="intro">
    Engineer specialized in data science, machine learning and computer vision.
    I enjoy turning complex data into insights, models and visualizations that
    help understand and improve real-world systems.
  </p>

  <svg class="route" viewBox="0 0 700 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Diagramme reliant les domaines de travail de Nathan">
    <path d="M20,90 C160,20 220,100 350,55 C460,18 520,95 680,30"
          fill="none" stroke="#2A5D82" stroke-width="1.5" stroke-dasharray="1 7" stroke-linecap="round"/>
    <g fill="#B96A1A">
      <circle cx="20" cy="90" r="4"/>
      <circle cx="230" cy="70" r="4"/>
      <circle cx="350" cy="55" r="4"/>
      <circle cx="500" cy="60" r="4"/>
      <circle cx="680" cy="30" r="4"/>
    </g>
  </svg>
  <p class="route-caption">aviation · sport · earth observation · health · sport</p>

  <div class="section">
    <div class="section-head">
      <span class="swatch"></span>
      <h2>Current interests</h2>
    </div>
    <div class="pins">
      <span class="pin">Data Science &amp; Machine Learning</span>
      <span class="pin">Computer Vision &amp; Image Analysis</span>
      <span class="pin">Sports Analytics</span>
      <span class="pin">Aviation &amp; Mobility</span>
      <span class="pin">Earth Observation &amp; Satellite Imagery</span>
    </div>
  </div>

  <div class="section">
    <div class="section-head">
      <span class="swatch"></span>
      <h2>Featured projects</h2>
    </div>
    <div class="projects">
      <div class="project">
        <p class="project-title"><span class="emoji">✈️</span> AerOptima</p>
        <p>Flight delay prediction on roughly 6 million flights.</p>
      </div>
      <div class="project">
        <p class="project-title"><span class="emoji">🏐</span> VolleyVision</p>
        <p>Volleyball player tracking and sports analytics.</p>
      </div>
      <div class="project">
        <p class="project-title"><span class="emoji">🌍</span> Satellite Road Segmentation</p>
        <p>Semantic segmentation of road networks with U-Net.</p>
      </div>
      <div class="project">
        <p class="project-title"><span class="emoji">🧠</span> Medical Intent Classification</p>
        <p>NLP and explainable AI for medical intent detection.</p>
      </div>
      <div class="project">
        <p class="project-title"><span class="emoji">🏐</span> VA-Pronos</p>
        <p>Prediction platform built for VolleyActu.</p>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="section-head">
      <span class="swatch"></span>
      <h2>Tech stack</h2>
    </div>
    <div class="stack-row">
      <span class="stack-label">Data &amp; ML</span>
      <span class="stack-items">Python · Pandas · NumPy · SQL · Scikit-learn · XGBoost</span>
    </div>
    <div class="stack-row">
      <span class="stack-label">Deep Learning &amp; CV</span>
      <span class="stack-items">PyTorch · TensorFlow · OpenCV · YOLO · U-Net</span>
    </div>
    <div class="stack-row">
      <span class="stack-label">Engineering</span>
      <span class="stack-items">Docker · FastAPI · Git · Linux · PySpark</span>
    </div>
  </div>

  <div class="contact">
    <div class="contact-links">
      <a href="https://www.linkedin.com/in/nathan-houel" target="_blank" rel="noopener">LinkedIn</a>
      <a href="mailto:houel.nathan.18@gmail.com">houel.nathan.18@gmail.com</a>
    </div>
    <span class="contact-note">STRASBOURG, FR</span>
  </div>

</div>
</body>
</html>
