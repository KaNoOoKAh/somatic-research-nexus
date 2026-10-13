Dual-State Telemetry Logging Protocol
This guide outlines the standard operating procedure for capturing hyper-local atmospheric data and subjective somatic-cognitive observations during research trials within the Somatic Research Nexus.

Prerequisites
Python 3.x installed on your system.

Git installed and authenticated with the KaNoOoKAh/somatic-research-nexus repository.

Active internet connection (required to query the Open-Meteo reanalysis API for micro-meteorological variables).

Step 1: Execute the Telemetry Logger

Open your terminal or Command Prompt (cmd).

Navigate to your local project directory:

DOS
cd "%USERPROFILE%\OneDrive\Desktop\somatic-research-nexus"

Run the telemetry logger script:

DOS
python somatic_logger.py

Step 2: Input Somatic & Trial Data
When prompted by the terminal interface, provide your current trial inputs:

Event Type:

Type START prior to initiating the research/exercise block (establishes baseline).

Type STOP upon completing the research/exercise block (captures post-session delta).

Energy Level: Enter a numeric rating from 1 (lowest) to 10 (highest).

Focus / Clarity: Enter a numeric rating from 1 (lowest) to 10 (highest).

Primary Observational State: Provide a qualitative somatic description detailing physical focus areas, muscle tension/relaxation, respiratory feel, or cognitive state.

Note: The script automatically fetches hyper-local environmental data for 3741 Poka Place (temperature, barometric pressure, solar radiation, relative humidity, wind metrics) and stamps the file with the ICeI3 identity marker before saving the .json output in trials/Trial_001/.

Step 3: Commit and Push to GitHub

Once the .json packet has been generated successfully, synchronize your trial data with the GitHub remote repository:

Stage all new telemetry logs:

DOS
git add .
Create a timestamped commit message:

DOS
git commit -m "Log Trial_001 telemetry"
Push the changes to GitHub:

DOS
git push
