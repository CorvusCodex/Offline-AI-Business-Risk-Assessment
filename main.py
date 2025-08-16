from utils import run_llama

def risk_assessment(project):
    prompt = f"Assess the risks and mitigations for this business project:\n{project}"
    return run_llama(prompt)

if __name__ == "__main__":
    project = input("Project idea: ")
    print(risk_assessment(project))
