from fastapi import APIRouter, BackgroundTasks

router = APIRouter(prefix="/tasks", tags=["Background Tasks"])

def send_email(email: str, message: str):
    print(f"Sending email to {email}: {message}")

@router.post("/send-email/")
def trigger_email(email: str, message: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email, message)
    return {"message": "Email task added to the queue"}
